#!/usr/bin/env python3
"""
check_external_links.py — weekly external-link rot checker.

check_repo_hygiene.py validates only *relative* (internal) links, so external
link rot is invisible to it — that's how the dead CES `/library/` and equal.vote
`/star-vs-rcv` pages slipped through until a manual audit. This script closes
that gap: it extracts every http(s) URL from the repo's Markdown, checks each
one, and reports ONLY the genuinely-dead ones.

The hard part of link-checking is false positives — a naive `curl` flags dozens
of live pages as broken. The 2026-07 audit catalogued exactly which, and those
findings are baked in as filters below, so this script's "DEAD" list is trustworthy:

  * SKIP_HOSTS — never checked at all:
      - bettervoting.com / realrcv.equal.vote are single-page apps: a direct
        request 404s even though the page loads fine in a browser.
      - docs.google.com / drive.google.com are auth-walled.
      - localhost / 127.0.0.1 / example.* are code placeholders.
  * BLOCKED_STATUS — reachable but bot-blocked or rate-limited, NEVER "dead":
      403 / 405 / 406 / 429 / 451 / 503 / 999 (Wikipedia 429, LinkedIn 999,
      Cloudflare 403, etc.). Reported separately as "couldn't verify", not failures.
  * HEAD→GET fallback + a browser User-Agent + redirect-following, so servers
    that reject HEAD or bare clients aren't miscounted.
  * A URL is called DEAD only on 404 / 410 / DNS failure / connection refused /
    persistent timeout — and only after a confirming GET also fails.

Advisory by design: prints a grouped report and exits 1 only if a genuinely-dead
link is found (so cron/launchd can mail you), 0 otherwise. It never edits anything.

    python3 STARVote_LH_tabulation_engine/tools_adam/scripts/check_external_links.py

Run it about once a week. To automate on macOS, either a crontab line:

    # Mondays 09:15 — mails stdout to the local user if anything is dead
    15 9 * * 1 cd "/Volumes/T7/Voting/Larry Hastings/YAML" && \
      /usr/bin/python3 STARVote_LH_tabulation_engine/tools_adam/scripts/check_external_links.py

or a launchd agent (survives reboots, better on macOS) — see the block at the
bottom of this file for a ready-to-save ~/Library/LaunchAgents plist.

Options:
    --timeout N     per-request timeout seconds (default 12)
    --workers N     concurrent checks (default 8)
    --report PATH   also write the full report to a file
    --show-blocked  list the "couldn't verify" bucket too (default: just a count)
"""
import argparse
import concurrent.futures as futures
import os
import re
import sys
import time
import urllib.error
import urllib.request


def _find_repo(start):
    p = os.path.dirname(os.path.abspath(start))
    while p != os.path.dirname(p):
        if os.path.isdir(os.path.join(p, "01_STAR")) and os.path.isdir(os.path.join(p, "STARVote_LH_tabulation_engine")):
            return p
        p = os.path.dirname(p)
    return os.path.dirname(os.path.abspath(start))


REPO = _find_repo(__file__)

SKIP_DIRS = {".git", ".venv", "node_modules", "__pycache__",
             "_demo_dropbox", ".idea", ".junie", ".claude", "site"}


def _skip_dir(rel):
    parts = rel.split(os.sep)
    return (any(p in SKIP_DIRS for p in parts)
            or "_tabulated" in rel or "_generated" in rel)


# --- False-positive filters (from the 2026-07 link audit) --------------------

# Hosts we never check: SPAs that 404 to non-browser clients, auth walls,
# and code placeholders. Matched as a suffix on the hostname.
SKIP_HOSTS = (
    "bettervoting.com",        # SPA — 404s to curl, loads in browser
    "realrcv.equal.vote",      # SPA — same
    "docs.google.com",         # auth-walled
    "drive.google.com",        # auth-walled
    "localhost", "127.0.0.1", "0.0.0.0",
    "example.com", "example.org", "example.net",
)

# Statuses that mean "reachable but wouldn't let us confirm" — bot-blocking or
# rate-limiting. NEVER counted as dead; surfaced only as "couldn't verify".
BLOCKED_STATUS = {401, 403, 405, 406, 429, 451, 503, 999}

# Statuses that mean genuinely gone.
DEAD_STATUS = {404, 410}

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/125.0 Safari/537.36")

# Note: ')' is intentionally NOT excluded — a URL may legitimately contain one
# (e.g. ballotpedia.org/Ranked-choice_voting_(RCV)). We grab greedily, then
# balance the parens in _clean_url() so the markdown-link closer ')' is dropped
# but a paren that's part of the URL is kept.
URL_RE = re.compile(r'https?://[^\s>\]"`}|\\]+')
# trailing punctuation that is almost never part of the URL itself
TRAILING = '.,;:!?'


def _clean_url(url):
    # A URL may legitimately contain balanced parens — Wikipedia's
    # `Plurality_(voting)`, ballotpedia's `Ranked-choice_voting_(RCV)`. But when
    # the URL sits inside a markdown `](…)` link, the CLOSING paren (and any
    # trailing `**`, `--`, `.` emphasis after it) rides along. The link closer is
    # the first ')' that has no matching '(' earlier in the URL — truncate there.
    depth = 0
    for i, ch in enumerate(url):
        if ch == "(":
            depth += 1
        elif ch == ")":
            if depth == 0:
                url = url[:i]
                break
            depth -= 1
    return url.rstrip(TRAILING)


def extract_urls():
    """Return {url: sorted[(relpath, lineno)]} across all tracked Markdown."""
    seen = {}
    for root, dirs, files in os.walk(REPO):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        rel_root = os.path.relpath(root, REPO)
        if _skip_dir(rel_root):
            continue
        for fn in files:
            if not fn.endswith(".md"):
                continue
            path = os.path.join(root, fn)
            rel = os.path.relpath(path, REPO)
            if _skip_dir(rel):
                continue
            try:
                with open(path, encoding="utf-8", errors="replace") as fh:
                    for lineno, line in enumerate(fh, 1):
                        for m in URL_RE.finditer(line):
                            url = _clean_url(m.group(0))
                            seen.setdefault(url, set()).add((rel, lineno))
            except OSError:
                continue
    return {u: sorted(locs) for u, locs in seen.items()}


def _host(url):
    m = re.match(r'https?://([^/]+)', url)
    h = (m.group(1) if m else "").lower()
    return h.split("@")[-1].split(":")[0]          # strip any user@ and :port


def _skipped(url):
    h = _host(url)
    # A host with no dot is not a public FQDN — it's an internal/docker service
    # name or a bare placeholder (localhost, web, db, api…). Never checkable.
    if "." not in h:
        return True
    return any(h == s or h.endswith("." + s) for s in SKIP_HOSTS)


def _request(url, method, timeout):
    req = urllib.request.Request(url, method=method, headers={
        "User-Agent": UA,
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.9",
    })
    # GET fallback (for servers that reject HEAD): we never .read() the body, so
    # closing the response early avoids downloading the page. A Range header here
    # made some hosts (GitHub) disagree with their own HEAD, so we don't send it.
    return urllib.request.urlopen(req, timeout=timeout)


def check(url, timeout):
    """Return (status, detail): status in {'live','blocked','dead'}."""
    last = None
    for attempt in range(2):                       # HEAD, then GET fallback
        method = "HEAD" if attempt == 0 else "GET"
        try:
            resp = _request(url, method, timeout)
            code = resp.getcode() or 200
            resp.close()
            if 200 <= code < 400:
                return "live", code
            if code in BLOCKED_STATUS:
                return "blocked", code
            if code in DEAD_STATUS:
                last = ("dead", code)
                continue                            # confirm with the other verb
            last = ("blocked", code)                # unknown 4xx/5xx: don't cry wolf
        except urllib.error.HTTPError as e:
            if e.code in BLOCKED_STATUS:
                return "blocked", e.code
            if e.code in DEAD_STATUS:
                last = ("dead", e.code)
                continue
            last = ("blocked", e.code)
        except urllib.error.URLError as e:
            reason = getattr(e, "reason", e)
            rs = str(reason).lower()
            # DNS / refused / reset = gone; timeouts get one retry then blocked.
            if any(k in rs for k in ("name or service not known", "nodename",
                                     "getaddrinfo", "refused", "reset",
                                     "no route", "unknown")):
                return "dead", f"conn: {reason}"
            last = ("blocked", f"net: {reason}")
        except Exception as e:                       # noqa: BLE001 — be robust
            last = ("blocked", f"err: {e}")
        time.sleep(0.4)
    return last or ("blocked", "unknown")


def main():
    ap = argparse.ArgumentParser(description="Weekly external-link rot checker.")
    ap.add_argument("--timeout", type=int, default=12)
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--report")
    ap.add_argument("--show-blocked", action="store_true")
    args = ap.parse_args()

    urls = extract_urls()
    checkable = {u: locs for u, locs in urls.items() if not _skipped(u)}
    n_skipped = len(urls) - len(checkable)

    print(f"external-link check: {len(urls)} unique URLs "
          f"({len(checkable)} checked, {n_skipped} skipped by filter)…",
          file=sys.stderr)

    results = {}
    with futures.ThreadPoolExecutor(max_workers=args.workers) as ex:
        fut = {ex.submit(check, u, args.timeout): u for u in checkable}
        for i, f in enumerate(futures.as_completed(fut), 1):
            u = fut[f]
            try:
                results[u] = f.result()
            except Exception as e:                   # noqa: BLE001
                results[u] = ("blocked", f"err: {e}")
            if i % 25 == 0:
                print(f"  …{i}/{len(checkable)}", file=sys.stderr)

    dead = sorted(u for u, (s, _) in results.items() if s == "dead")
    blocked = sorted(u for u, (s, _) in results.items() if s == "blocked")
    live = sum(1 for s, _ in results.values() if s == "live")

    out = []
    out.append("=" * 72)
    out.append(f"EXTERNAL-LINK REPORT — {live} live · {len(blocked)} unverifiable "
               f"· {len(dead)} DEAD  (of {len(checkable)} checked)")
    out.append("=" * 72)

    if dead:
        out.append("\nDEAD — fix these (replace, or pin a web.archive.org snapshot):\n")
        for u in dead:
            code = results[u][1]
            out.append(f"  ✗ [{code}] {u}")
            for rel, ln in urls[u]:
                out.append(f"        {rel}:{ln}")
    else:
        out.append("\n✓ No dead links.")

    if blocked:
        out.append(f"\nCOULDN'T VERIFY ({len(blocked)}) — bot-blocked / rate-limited, "
                   "almost always live; spot-check in a browser if worried.")
        if args.show_blocked:
            for u in blocked:
                out.append(f"  ? [{results[u][1]}] {u}")

    report = "\n".join(out)
    print(report)
    if args.report:
        with open(args.report, "w", encoding="utf-8") as fh:
            fh.write(report + "\n")

    return 1 if dead else 0


if __name__ == "__main__":
    sys.exit(main())


# --- launchd agent (macOS) ---------------------------------------------------
# Save as ~/Library/LaunchAgents/com.masiarek.starlib.linkcheck.plist, then:
#   launchctl load ~/Library/LaunchAgents/com.masiarek.starlib.linkcheck.plist
# Runs Mondays 09:15; writes the report to the repo scratch and logs dead links.
#
# <?xml version="1.0" encoding="UTF-8"?>
# <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
#   "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
# <plist version="1.0"><dict>
#   <key>Label</key><string>com.masiarek.starlib.linkcheck</string>
#   <key>ProgramArguments</key><array>
#     <string>/usr/bin/python3</string>
#     <string>/Volumes/T7/Voting/Larry Hastings/YAML/STARVote_LH_tabulation_engine/tools_adam/scripts/check_external_links.py</string>
#     <string>--report</string>
#     <string>/tmp/starlib_linkcheck.txt</string>
#   </array>
#   <key>StartCalendarInterval</key><dict>
#     <key>Weekday</key><integer>1</integer>
#     <key>Hour</key><integer>9</integer><key>Minute</key><integer>15</integer>
#   </dict>
#   <key>StandardOutPath</key><string>/tmp/starlib_linkcheck.log</string>
#   <key>StandardErrorPath</key><string>/tmp/starlib_linkcheck.err</string>
# </dict></plist>
