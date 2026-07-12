#!/usr/bin/env python3
"""
bv_ballot_sheet.py — generate printable STAR paper ballots for a demo / classroom
hand-count exercise, tied to a BetterVoting (BV) election.

The teacher's front-of-workflow tool: you make a real election on BetterVoting,
then print matching paper ballots so a room can vote by hand, hand-count the result
(see 00_start_here/STAR_Voting/count_star_by_hand.md), and compare to BV's official
tally. The `--out` extension picks the format: .txt = plain ASCII (zero deps, prints
anywhere, form-feed page breaks), .pdf = print-ready PDF (via playwright), .html
(default) = styled with a scannable QR (Print -> PDF). Each ballot carries the STAR
instructions, a 0-5 bubble grid per candidate, and the BV election id + results URL
so paper and platform stay linked. Default is one ballot per page.

Candidates + title come from ONE of:
  --yaml FILE          a repo election .yaml (title + candidates from its ballots header;
                       picks up bv_election_id automatically if present)
  --bv-export FILE     a frozen BetterVoting <case>_bv_export.json (also carries the
                       election + race descriptions onto the ballot)
  --candidates "A,B,C" --title "..." [--bv-id ID] [--question "..."]
                       [--description "..."] [--race-description "..."]   manual

Stdlib only — no dependencies (QR is optional via `segno`). `--selftest` runs
known-answer checks. Design spec & rationale: bv_ballot_sheet_FSD.md (beside this file).

Examples
--------
  python3 bv_ballot_sheet.py --yaml 01_STAR/_main/bv2184_fyy886_lunch_vote.yaml --copies 30
  python3 bv_ballot_sheet.py --candidates "Ada,Ben,Cara" --title "Class President" --bv-id demo1
  python3 bv_ballot_sheet.py --selftest
"""

import argparse
import html
import json
import os
import re
import sys
import textwrap


# --------------------------------------------------------------------------- #
# Read candidates / title / bv-id from the supported sources.                  #
# --------------------------------------------------------------------------- #
def from_yaml(path):
    """Return (title, bv_id, [candidates]) from a repo election YAML, parsed
    minimally (no PyYAML dependency): title line, bv_election_id line, and the
    first content row under `ballots:` (the comma-separated candidate header)."""
    title = bv_id = None
    cands = None
    in_ballots = False
    for ln in open(path, encoding="utf-8").read().splitlines():
        s = ln.strip()
        if s.startswith("election_title:"):
            title = s.split(":", 1)[1].strip().strip('"\'')
        elif s.startswith("bv_election_id:"):
            bv_id = s.split(":", 1)[1].strip().strip('"\'')
        elif s.startswith("ballots:"):
            in_ballots = True
        elif in_ballots and cands is None:
            content = s.split("#", 1)[0].strip()
            if content and content not in ("|-", "|", ">-", ">"):
                cands = [c.strip() for c in content.split(",") if c.strip()]
    if not cands:
        raise SystemExit(f"Could not find a candidate header under `ballots:` in {path}")
    # (election/race descriptions in repo YAMLs are block scalars this minimal
    # parser doesn't read; use --description if you want one on a YAML-sourced ballot.)
    return title, bv_id, cands, None, None


def _find_candidate_names(obj):
    """Best-effort recursive search of a BV export for candidate display names."""
    names = []
    if isinstance(obj, dict):
        if isinstance(obj.get("candidates"), list):
            for c in obj["candidates"]:
                if isinstance(c, dict):
                    nm = c.get("candidate_name") or c.get("name") or c.get("longName")
                    if nm:
                        names.append(str(nm))
            if names:
                return names
        for v in obj.values():
            names = _find_candidate_names(v)
            if names:
                return names
    elif isinstance(obj, list):
        for v in obj:
            names = _find_candidate_names(v)
            if names:
                return names
    return names


def from_bv_export(path):
    """Return (title, bv_id, [candidates], election_desc, race_desc) from a frozen
    BV export JSON."""
    data = json.load(open(path, encoding="utf-8"))
    # A frozen BV UI export nests everything under a capitalized "Election" key
    # (siblings "Ballots"/"Results"); older/plain GETs use lowercase or are flat.
    election = data if not isinstance(data, dict) else (
        data.get("Election") or data.get("election") or data)
    title = election.get("title") or election.get("name")
    bv_id = (election.get("election_id") or election.get("id")
             or data.get("election_id") or data.get("Election", {}).get("election_id"))
    cands = _find_candidate_names(data)
    if not cands:
        raise SystemExit(f"Could not find candidate names in {path} "
                         f"(pass --candidates manually).")
    edesc = election.get("description") or None
    races = election.get("races") or []
    rdesc = races[0].get("description") if races and isinstance(races[0], dict) else None
    return title, bv_id, cands, edesc, (rdesc or None)


# --------------------------------------------------------------------------- #
# HTML ballot rendering.                                                       #
# --------------------------------------------------------------------------- #
INSTRUCTIONS = ("Score each candidate 0 to 5 (fill ONE bubble per row). "
                "Give your favorite 5, your last choice 0 (or leave blank). "
                "Equal scores are allowed. Two or more bubbles in a row is a "
                "spoiled score for that candidate. The two highest-scoring "
                "candidates have an automatic runoff.")

# Printed on every ballot by default: this tool only ever makes DEMO ballots, so
# a standing notice keeps that honest and — crucially — makes the optional serial
# number read as a teaching device, not surveillance (a numbered *real* ballot
# would break the secret ballot). Suppress with --no-notice; override with --notice.
# Kept 7-bit ASCII (plain '-') so it survives into the .txt output unchanged.
DEFAULT_NOTICE = "EDUCATION ONLY - a STAR Voting teaching demo, not a secret ballot."


def qr_data_uri(url):
    """An inline QR (data: URI) for `url` if the pure-python `segno` library is
    installed; None otherwise (the tool stays stdlib-only, QR just degrades)."""
    try:
        import segno
    except ImportError:
        return None
    try:
        return segno.make(url, error="m").svg_data_uri(scale=3, border=1)
    except Exception:
        return None

def html_to_pdf(html_str, pdf_path):
    """Render the ballot HTML straight to a print-ready PDF via headless Chromium
    (the already-declared `playwright` dep). Returns True on success; False if
    playwright isn't installed/usable, so the caller can fall back to writing HTML.
    page.pdf() emulates print media, so the @media-print page-breaks apply."""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        return False
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.set_content(html_str, wait_until="load")
            page.pdf(path=pdf_path, format="Letter", print_background=True,
                     margin={"top": "0.4in", "bottom": "0.4in",
                             "left": "0.4in", "right": "0.4in"})
            browser.close()
        return True
    except Exception as e:
        print(f"[pdf] playwright present but PDF render failed ({e}); "
              "falling back to HTML.")
        return False


CSS = """
:root { color-scheme: light; }
body { font-family: -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif;
       margin: 0; color: #111; }
.ballot { border: 2px solid #111; border-radius: 8px; padding: 14px 18px;
          margin: 12px; page-break-inside: avoid; }
.ballot h2 { margin: 0 0 2px; font-size: 17px; }
.q { margin: 0 0 8px; color: #333; font-size: 13px; }
.edesc { margin: 0 0 7px; color: #555; font-size: 12px; font-style: italic; }
.inst { margin: 0 0 10px; font-size: 11.5px; color: #444; }
table { border-collapse: collapse; width: 100%; }
th, td { border: 1px solid #999; padding: 6px 4px; text-align: center; font-size: 13px; }
th.cand, td.cand { text-align: left; width: 42%; font-weight: 600; }
.bub { display: inline-block; width: 15px; height: 15px; border: 1.6px solid #333;
       border-radius: 50%; }
.foot { margin-top: 8px; font-size: 10.5px; color: #555; display: flex;
        justify-content: space-between; }
.bhead { display: flex; justify-content: space-between; align-items: flex-start; gap: 10px; }
.qr { text-align: center; font-size: 9px; color: #555; }
.qr img { width: 72px; height: 72px; display: block; }
.wline { display: inline-block; border-bottom: 1px solid #333; width: 55%; height: 1em; }
.serial { font-weight: 700; }
.notice { border: 1.5px solid #c0392b; border-radius: 5px; padding: 3px 8px;
          margin: 0 0 9px; font-size: 10.5px; font-weight: 700; color: #c0392b;
          text-align: center; text-transform: uppercase; letter-spacing: .4px; }
@media print { .noprint { display: none; } .ballot { margin: 0 0 8px; }
  .ballot.pagebreak { page-break-after: always; } }
"""


def render_ballot(title, question, candidates, bv_id, qr_uri=None,
                  serial=None, write_ins=0, qr_caption="scan to vote",
                  break_after=False, notice="", blurb=""):
    rows = []
    header = "".join(f"<th>{n}</th>" for n in range(6))
    bubbles = "".join('<td><span class="bub"></span></td>' for _ in range(6))
    for c in candidates:
        rows.append(f'<tr><td class="cand">{html.escape(c)}</td>{bubbles}</tr>')
    for _ in range(write_ins):
        rows.append(f'<tr><td class="cand">Write-in: <span class="wline"></span>'
                    f'</td>{bubbles}</tr>')
    results = (f'results: bettervoting.com/{html.escape(bv_id)}/results'
               if bv_id else 'STAR Voting — Score Then Automatic Runoff')
    idpieces = []
    if serial is not None:
        idpieces.append(f'Ballot <span class="serial">#{html.escape(str(serial))}</span> '
                        f'— keep this to verify it was counted')
    idpieces.append(f'Election {html.escape(bv_id)}' if bv_id else 'demo ballot')
    idline = " · ".join(idpieces)
    qr_block = (f'<div class="qr"><img src="{qr_uri}" alt="QR code">'
                f'<span>{html.escape(qr_caption)}</span></div>'
                if qr_uri else "")
    cls = "ballot pagebreak" if break_after else "ballot"
    notice_block = (f'<div class="notice">{html.escape(notice)}</div>'
                    if notice else "")
    blurb_block = (f'<p class="edesc">{html.escape(blurb)}</p>' if blurb else "")
    return f"""
<div class="{cls}">
  {notice_block}
  <div class="bhead">
    <div>
      <h2>{html.escape(title or 'STAR Voting ballot')}</h2>
      {blurb_block}
      <p class="q">{html.escape(question)}</p>
    </div>{qr_block}
  </div>
  <p class="inst">{INSTRUCTIONS}</p>
  <table>
    <tr><th class="cand">Candidate</th>{header}</tr>
    {''.join(rows)}
  </table>
  <p class="foot"><span>{idline}</span><span>{results}</span></p>
</div>"""


def render_sheet(title, question, candidates, bv_id, copies, per_page,
                 qr=True, serials=False, write_ins=0, qr_url=None, notice="", blurb=""):
    # QR points to --qr-url if given (works even LH-only, no BV), else the BV
    # election if there is one, else nothing.
    url = qr_url or (f"https://bettervoting.com/{bv_id}" if bv_id else None)
    caption = "scan" if qr_url else "scan to vote"
    qr_uri = qr_data_uri(url) if (url and qr) else None
    pp = max(1, per_page)
    ballots = "\n".join(
        render_ballot(title, question, candidates, bv_id, qr_uri,
                      serial=(i + 1 if serials else None), write_ins=write_ins,
                      qr_caption=caption, notice=notice, blurb=blurb,
                      # force a page break after every `per_page` ballots (but not
                      # after the last — a trailing break makes a blank page).
                      break_after=((i + 1) % pp == 0 and i + 1 < copies))
        for i in range(copies))
    perpage_txt = ('one ballot per page' if pp == 1 else f'{pp} ballots per page')
    hint = ('<p class="noprint" style="margin:12px 18px;color:#666;font-size:13px">'
            f'{copies} ballots · {perpage_txt} — use your browser\'s '
            'Print → "Save as PDF" (or run with --out ballots.pdf for a PDF directly). '
            'This is the print-and-hand-count front end; '
            'count with count_star_by_hand.md, then compare to BetterVoting.</p>')
    return (f'<!doctype html><html><head><meta charset="utf-8">'
            f'<title>STAR ballots — {html.escape(title or bv_id or "demo")}</title>'
            f'<style>{CSS}</style></head><body>{hint}{ballots}</body></html>')


# --------------------------------------------------------------------------- #
# Plain-ASCII output: zero dependencies, prints from anywhere (`lpr file.txt`   #
# or any editor). One ballot per page via the form-feed char (\f). No QR (the   #
# URL is printed instead) — the purest, most portable ballot.                   #
# --------------------------------------------------------------------------- #
TEXT_WIDTH = 72
TEXT_INSTRUCTIONS = ("Fill ONE circle per row, 0 (worst) to 5 (best). A blank row "
                     "counts as 0. Two or more marks in one row is a spoiled score "
                     "for that candidate. The two highest-scoring candidates have an "
                     "automatic runoff.")


def _ascii_row(label, name_w):
    cells = "   ".join("( )" for _ in range(6))
    return f"  {label[:name_w].ljust(name_w)}  {cells}"


def render_ballot_text(title, question, candidates, bv_id,
                       serial=None, write_ins=0, notice="", blurb=""):
    rule = "=" * TEXT_WIDTH
    name_w = max([len("Candidate")] + [len(c) for c in candidates] + [11]) + 1
    name_w = min(name_w, 34)
    lines = [rule]
    lines.append((title or "STAR Voting ballot").center(TEXT_WIDTH).rstrip())
    if serial is not None:
        lines.append(f"  Ballot #{serial} - keep this to verify it was counted")
    if notice:
        bar = "  " + "-" * (TEXT_WIDTH - 4)
        lines.append("")
        lines.append(bar)
        for ln in textwrap.wrap(notice, TEXT_WIDTH - 4):
            lines.append("  " + ln)
        lines.append(bar)
    if blurb:
        lines.append("")
        lines += textwrap.wrap(blurb, TEXT_WIDTH - 2, initial_indent="  ",
                               subsequent_indent="  ")
    lines.append("")
    lines += textwrap.wrap(question, TEXT_WIDTH - 2, initial_indent="  ",
                           subsequent_indent="  ")
    lines.append("")
    lines += textwrap.wrap(TEXT_INSTRUCTIONS, TEXT_WIDTH - 2, initial_indent="  ",
                           subsequent_indent="  ")
    lines.append("")
    header = f"  {'Candidate'.ljust(name_w)}  " + "   ".join(f" {n} " for n in range(6))
    lines.append(header)
    lines.append(f"  {'-' * name_w}  " + "   ".join("---" for _ in range(6)))
    for c in candidates:
        lines.append(_ascii_row(c, name_w))
    for _ in range(write_ins):
        lines.append(_ascii_row("Write-in: " + "_" * (name_w - 10), name_w))
    lines.append("")
    if bv_id:
        lines.append(f"  Election {bv_id}  |  results: bettervoting.com/{bv_id}/results")
    else:
        lines.append("  STAR Voting — Score Then Automatic Runoff")
    lines.append(rule)
    return "\n".join(lines)


def render_sheet_text(title, question, candidates, bv_id, copies, per_page,
                      serials=False, write_ins=0, notice="", blurb=""):
    pp = max(1, per_page)
    out = []
    for i in range(copies):
        out.append(render_ballot_text(title, question, candidates, bv_id,
                                      serial=(i + 1 if serials else None),
                                      write_ins=write_ins, notice=notice, blurb=blurb))
        last = (i + 1 == copies)
        if not last:
            # form-feed = a hard page break for printers; a blank gap otherwise.
            out.append("\f" if (i + 1) % pp == 0 else "\n")
    return "\n".join(out) + "\n"


# --------------------------------------------------------------------------- #
# Self-tests.                                                                  #
# --------------------------------------------------------------------------- #
def selftest():
    ok = True
    html_out = render_sheet("Test", "Score each", ["Ann", "Bob", "Cal"], "abc123",
                            copies=3, per_page=2)
    checks = [
        ("all three candidates present", all(n in html_out for n in ("Ann", "Bob", "Cal"))),
        ("bv id + results url", "bettervoting.com/abc123/results" in html_out),
        ("3 ballots rendered", html_out.count('class="ballot') == 3),
        ("0-5 bubble grid (18 bubbles/ballot = 3 cands x 6)", html_out.count('class="bub"') == 3 * 6 * 3),
        ("html escaping of a tricky name",
         "&lt;b&gt;" in render_ballot("t", "q", ["<b>"], None)),
    ]
    for label, cond in checks:
        print(f"[selftest] {label}: {'OK' if cond else 'FAIL'}")
        ok &= cond
    # serials + write-in rows
    s2 = render_sheet("T", "q", ["A", "B"], "x", copies=2, per_page=1,
                      qr=False, serials=True, write_ins=1)
    extra = [
        ("serial numbers per ballot", '#1</span>' in s2 and '#2</span>' in s2),
        ("write-in row added (1 per ballot x 2)", s2.count("Write-in:") == 2),
        ("bubbles = (2 cands + 1 write-in) x 6 x 2 ballots",
         s2.count('class="bub"') == (2 + 1) * 6 * 2),
    ]
    for label, cond in extra:
        print(f"[selftest] {label}: {'OK' if cond else 'FAIL'}")
        ok &= cond
    # pagination: page-break after every `per_page` ballots, never after the last.
    one = render_sheet("T", "q", ["A"], None, copies=3, per_page=1, qr=False)
    two = render_sheet("T", "q", ["A"], None, copies=3, per_page=2, qr=False)
    page = [
        ("one-per-page: breaks after all but last (3 copies -> 2 breaks)",
         one.count('class="ballot pagebreak"') == 2),
        ("two-per-page: break after ballot 2 only (3 copies -> 1 break)",
         two.count('class="ballot pagebreak"') == 1),
    ]
    for label, cond in page:
        print(f"[selftest] {label}: {'OK' if cond else 'FAIL'}")
        ok &= cond
    # plain-ASCII output: zero deps, form-feed page breaks, results URL not QR.
    txt = render_sheet_text("Pets", "q", ["ala", "bob"], "mptvrm",
                            copies=3, per_page=1, serials=True)
    is_ascii = all(ord(ch) < 128 for ch in txt)
    txtchecks = [
        ("ascii: candidates + results url present",
         "ala" in txt and "bob" in txt and "bettervoting.com/mptvrm/results" in txt),
        ("ascii: one-per-page form-feeds (3 copies -> 2)", txt.count("\f") == 2),
        ("ascii: 6 markable circles per candidate row", "( )   ( )   ( )   ( )   ( )   ( )" in txt),
        ("ascii: serial receipt line", "Ballot #1 - keep" in txt),
        ("ascii: strictly 7-bit ASCII (no QR, no unicode)", is_ascii),
    ]
    for label, cond in txtchecks:
        print(f"[selftest] {label}: {'OK' if cond else 'FAIL'}")
        ok &= cond
    # QR is optional (needs segno); test whichever path applies.
    if qr_data_uri("https://bettervoting.com/abc123"):
        has_qr = 'class="qr"' in html_out and "data:image/svg" in html_out
        print(f"[selftest] QR embedded (segno present): {'OK' if has_qr else 'FAIL'}")
        ok &= has_qr
    else:
        no_qr = 'class="qr"' not in html_out
        print(f"[selftest] graceful no-QR (segno absent): {'OK' if no_qr else 'FAIL'}")
        ok &= no_qr
    # BV-export parsing: a frozen UI export nests everything under capitalized
    # "Election" (siblings "Ballots"/"Results") — regression guard for that schema.
    import tempfile, os
    export = {"Election": {"title": "Pets", "election_id": "mptvrm",
                           "description": "Our class demo election.",
                           "races": [{"description": "Which pet is best?",
                                      "candidates": [{"candidate_name": "ala"},
                                                     {"candidate_name": "bob"}]}]},
              "Ballots": [], "Results": []}
    fd, tmp = tempfile.mkstemp(suffix=".json")
    with os.fdopen(fd, "w") as f:
        json.dump(export, f)
    try:
        t, bid, cs, ed, rd = from_bv_export(tmp)
        bv_ok = (t == "Pets" and bid == "mptvrm" and cs == ["ala", "bob"]
                 and ed == "Our class demo election." and rd == "Which pet is best?")
    finally:
        os.remove(tmp)
    print(f"[selftest] BV export (capital 'Election'): title+id+candidates+descriptions: "
          f"{'OK' if bv_ok else 'FAIL'}")
    ok &= bv_ok
    # descriptions print on the ballot: election desc as blurb, race desc as question.
    html_d = render_sheet("Pets", "Which pet is best?", ["A"], "x", copies=1,
                          per_page=1, qr=False, blurb="Our class demo election.")
    txt_d = render_sheet_text("Pets", "Which pet is best?", ["A"], "x", copies=1,
                              per_page=1, blurb="Our class demo election.")
    desc_checks = [
        ("HTML ballot shows election description (blurb)",
         'class="edesc"' in html_d and "Our class demo election." in html_d),
        ("HTML ballot shows race description (question)", "Which pet is best?" in html_d),
        ("ASCII ballot shows both descriptions",
         "Our class demo election." in txt_d and "Which pet is best?" in txt_d),
    ]
    for label, cond in desc_checks:
        print(f"[selftest] {label}: {'OK' if cond else 'FAIL'}")
        ok &= cond
    # demonstration / secret-ballot notice: on by default, both formats, off-able.
    html_n = render_sheet("T", "q", ["A"], "x", copies=1, per_page=1, qr=False,
                          notice=DEFAULT_NOTICE)
    html_off = render_sheet("T", "q", ["A"], "x", copies=1, per_page=1, qr=False,
                            notice="")
    txt_n = render_sheet_text("T", "q", ["A"], "x", copies=1, per_page=1,
                              notice=DEFAULT_NOTICE)
    notice_checks = [
        ("notice: default text mentions 'not a secret ballot'",
         "not a secret ballot" in DEFAULT_NOTICE),
        ("notice: HTML ballot shows it (class=notice)",
         'class="notice"' in html_n and "secret ballot" in html_n),
        ("notice: --no-notice omits it from HTML", 'class="notice"' not in html_off),
        ("notice: ASCII ballot shows it and stays 7-bit",
         "secret ballot" in txt_n and all(ord(c) < 128 for c in txt_n)),
    ]
    for label, cond in notice_checks:
        print(f"[selftest] {label}: {'OK' if cond else 'FAIL'}")
        ok &= cond
    print(f"[selftest] {'ALL PASS' if ok else 'FAILURES PRESENT'}")
    return ok


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--yaml")
    ap.add_argument("--bv-export")
    ap.add_argument("--candidates", help='comma-separated, e.g. "Ada,Ben,Cara"')
    ap.add_argument("--title")
    ap.add_argument("--question", help="the ballot question line")
    ap.add_argument("--bv-id")
    ap.add_argument("--copies", type=int, default=30)
    ap.add_argument("--per-page", type=int, default=1,
                    help="ballots per printed page (default 1 — one ballot per page, "
                         "the right choice for ballots you hand out individually)")
    ap.add_argument("--out", default="ballots.html",
                    help="output file — extension picks the format: .txt = plain "
                         "ASCII (zero deps, prints anywhere), .pdf = print-ready PDF "
                         "(needs `playwright`), .html (default) = styled, Print → PDF")
    ap.add_argument("--no-qr", action="store_true",
                    help="omit the QR code (QR needs the `segno` library)")
    ap.add_argument("--qr-url",
                    help="point the QR at any URL (e.g. a 'learn STAR' page) — useful "
                         "for LH-only demos with no BV election; default is the BV election")
    ap.add_argument("--serials", action="store_true",
                    help="number each ballot (a 'keep this to verify it was counted' "
                         "receipt — see the secret-ballot caveat in the demo page)")
    ap.add_argument("--write-ins", type=int, default=0, metavar="N",
                    help="add N blank write-in rows per ballot")
    ap.add_argument("--notice", metavar="TEXT",
                    help="the 'this is a demo, not a secret ballot' notice printed on "
                         f"every ballot (default: \"{DEFAULT_NOTICE}\")")
    ap.add_argument("--no-notice", action="store_true",
                    help="omit the demonstration/secret-ballot notice (not recommended "
                         "— it's what keeps the serial number a teaching device)")
    ap.add_argument("--description", metavar="TEXT",
                    help="election description printed under the title (a --bv-export "
                         "supplies this automatically from the election's description)")
    ap.add_argument("--race-description", metavar="TEXT",
                    help="race/contest description used as the ballot question line "
                         "(a --bv-export supplies this from the race's description)")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()

    if args.selftest:
        raise SystemExit(0 if selftest() else 1)

    title = args.title
    bv_id = args.bv_id
    candidates = None
    edesc = rdesc = None
    if args.yaml:
        title, bv_id2, candidates, edesc, rdesc = from_yaml(args.yaml)
        bv_id = bv_id or bv_id2
        title = args.title or title
    elif args.bv_export:
        t2, bv_id2, candidates, edesc, rdesc = from_bv_export(args.bv_export)
        title = args.title or t2
        bv_id = bv_id or bv_id2
    elif args.candidates:
        candidates = [c.strip() for c in args.candidates.split(",") if c.strip()]
    else:
        raise SystemExit("Provide one of --yaml / --bv-export / --candidates "
                         "(see --help). Run --selftest to verify the tool.")

    # Description → blurb under the title; race description → the question line.
    # CLI flags win over what the export supplied.
    blurb = (args.description or edesc or "").strip()
    question = (args.question or args.race_description or rdesc
                or "Score each candidate from 0 (worst) to 5 (best).").strip()
    notice = "" if args.no_notice else (args.notice or DEFAULT_NOTICE)

    # Plain-ASCII output: zero deps, prints anywhere, one ballot per page via \f.
    if args.out.lower().endswith(".txt"):
        sheet = render_sheet_text(title, question, candidates, bv_id, args.copies,
                                  args.per_page, serials=args.serials,
                                  write_ins=args.write_ins, notice=notice, blurb=blurb)
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(sheet)
        pp = max(1, args.per_page)
        layout = "one per page" if pp == 1 else f"{pp} per page"
        print(f"Wrote {args.copies} STAR ballots ({len(candidates)} candidates, "
              f"{layout}) to {os.path.abspath(args.out)}")
        print("Plain text — print with `lpr` or any editor (form-feed = page break). "
              "No dependencies, no QR (the results URL is printed).")
        if bv_id:
            print(f"Linked to BetterVoting election {bv_id} "
                  f"(results: https://bettervoting.com/{bv_id}/results).")
        return

    sheet = render_sheet(title, question, candidates, bv_id, args.copies,
                         args.per_page, qr=not args.no_qr, serials=args.serials,
                         write_ins=args.write_ins, qr_url=args.qr_url, notice=notice,
                         blurb=blurb)

    want_pdf = args.out.lower().endswith(".pdf")
    wrote_pdf = False
    if want_pdf:
        wrote_pdf = html_to_pdf(sheet, args.out)
        if not wrote_pdf:
            # Graceful fallback: no playwright → write the HTML beside it so the
            # user can still Print → PDF. (Keeps the tool runnable on plain python3.)
            args.out = args.out[:-4] + ".html"
            print("[pdf] `playwright` not available — install it (uv pip install "
                  "playwright && playwright install chromium) for direct PDF. "
                  f"Writing HTML instead: {args.out}")

    if not wrote_pdf:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(sheet)

    pp = max(1, args.per_page)
    layout = "one per page" if pp == 1 else f"{pp} per page"
    print(f"Wrote {args.copies} STAR ballots ({len(candidates)} candidates, {layout}) "
          f"to {os.path.abspath(args.out)}")
    if wrote_pdf:
        print("Print-ready PDF — send it straight to the printer.")
    else:
        print("Open it in a browser and Print → Save as PDF.")
    if bv_id:
        print(f"Linked to BetterVoting election {bv_id} "
              f"(results: https://bettervoting.com/{bv_id}/results).")


if __name__ == "__main__":
    main()
