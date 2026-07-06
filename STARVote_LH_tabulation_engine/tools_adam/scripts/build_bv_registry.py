#!/usr/bin/env python3
"""
build_bv_registry.py — a repo-native registry of the BetterVoting test cases.

Scans the YAML election files, pulls out each case's BV metadata, and writes:

  * 00_start_here/YAML_test_case_index/bv_cases.csv   — sortable table (GitHub
    renders CSV with clickable column-sort), one row per BV-tracked case.
  * 00_start_here/YAML_test_case_index/BV_registry.md — the same as a Markdown
    table + a summary (methods breakdown, sorted Test IDs, and the free gaps in
    the repo's BV-number range) so "what BV numbers are taken?" is answerable
    from the repo, not only the Google Sheet.

Metadata sources, per file (explicit field wins; filename is the fallback):
  * Test ID       — `bv_test_id:` field, else the `bv<NNN[letter]>` filename prefix.
  * BV election id — `bv_election_id:` field, else the 2nd filename segment.
  * results URL    — `bv_results_url:` field, else built from the election id.
  * method / winners / expected — the ordinary race fields.
  * candidates / ballots — parsed from the `ballots:` block.

Only BV-tracked cases are listed (a `bv_test_id` field OR a `bv…` filename).
The master Google Sheet stays authoritative for the FULL numbering (it also
tracks non-tabulation QA that has no YAML); this registry covers the repo subset.

Run from the repo root:
    python STARVote_LH_tabulation_engine/tools_adam/scripts/build_bv_registry.py
"""

import csv
import glob
import json
import os
import re
import sys

import yaml

EXCLUDE = ("/_tabulated", "_tabulated/", "/_demo_dropbox/", "/_generated",
           "/negative", "/tests/", "/test_elections/", "/YAML_library/2_negative")


def _find_repo(start):
    d = start
    while d != os.path.dirname(d):
        if os.path.isdir(os.path.join(d, "00_start_here")):
            return d
        d = os.path.dirname(d)
    sys.exit("could not locate repo root (no 00_start_here/ above this script)")


REPO = _find_repo(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(REPO, "00_start_here", "YAML_test_case_index")

# Test ID from a `bv<num>[letter|-rN]_...` filename. Election id is NEVER guessed
# from the filename (descriptor words like "score"/"guido" would be mistaken for
# BV ids); it comes from the `bv_election_id` field or the frozen export.
FN_RE = re.compile(r"^bv(\d+(?:-?r\d+|[a-z])?)_", re.IGNORECASE)


def _export_election_id(yaml_path):
    """The authoritative BV election id from the case's frozen export sibling."""
    exp = yaml_path[:-5] + "_bv_export.json"
    if not os.path.exists(exp):
        return ""
    try:
        d = json.load(open(exp))
        E = d.get("Election") or d.get("election") or {}
        return E.get("election_id", "") or ""
    except Exception:
        return ""


def _race(d):
    if not isinstance(d, dict):
        return {}
    if isinstance(d.get("races"), list) and d["races"]:
        return d["races"][0]
    if isinstance(d.get("election"), dict):
        e = d["election"]
        return (e.get("races") or [e])[0] if isinstance(e.get("races"), list) else e
    return d


def _ballot_shape(race):
    """(n_candidates, n_voters) parsed from the ballots block string.

    Counts VOTERS, not lines: a weighted row like `9: 5,3,1` or `42:A>B>C` is 9 /
    42 ballots, not one. Handles both score ballots (CSV with a candidate header)
    and ranked ballots (`A>B>C`, no header). A row may carry only markers (e.g.
    `-,-` — a blank/abstention ballot); it is still a cast ballot and counts."""
    b = race.get("ballots")
    if not isinstance(b, str):
        return ("", "")
    raw = [ln.split("#", 1)[0].strip() for ln in b.splitlines()]
    raw = [ln for ln in raw if ln]
    if not raw:
        return ("", "")

    def _weight(ln):
        m = re.match(r"^\s*(\d+)\s*[:xX×]", ln)
        return int(m.group(1)) if m else 1

    def _strip_weight(ln):
        return re.sub(r"^\s*\d+\s*[:xX×]\s*", "", ln)

    if any(">" in ln for ln in raw):          # ranked ballots — no header line
        rows = raw
        cands = set()
        for ln in rows:
            for tok in _strip_weight(ln).split(">"):
                t = tok.strip()
                if t:
                    cands.add(t)
        n_cand = len(cands)
    else:                                     # score ballots — first line is the header
        n_cand = len([c for c in raw[0].split(",") if c.strip()])
        rows = raw[1:]
    n_voters = sum(_weight(ln) for ln in rows)
    return (n_cand, n_voters)


def _test_num(test_id):
    """BV27 -> 27 ; BV95a -> 95 ; BV130-r2 -> 130. Only BV-numbered ids (a leading
    'BV<n>'); returns None for non-numbered case ids like 'Runoff_01' or 'pet'."""
    m = re.match(r"\s*BV\s*(\d+)", test_id or "", re.IGNORECASE)
    return int(m.group(1)) if m else None


def collect():
    rows = []
    for p in sorted(glob.glob(os.path.join(REPO, "**", "*.yaml"), recursive=True)):
        rel = os.path.relpath(p, REPO).replace(os.sep, "/")
        if any(s in "/" + rel for s in EXCLUDE):
            continue
        name = os.path.basename(rel)
        if any(t in name.lower() for t in ("temp", "trash", "scratch")):
            continue
        try:
            d = yaml.safe_load(open(p))
        except Exception:
            continue
        if not isinstance(d, dict):
            continue
        race = _race(d)
        if not isinstance(race, dict) or "ballots" not in race:
            continue

        fn = FN_RE.match(name)
        test_id = d.get("bv_test_id") or (f"BV{fn.group(1)}" if fn else "")
        election_id = d.get("bv_election_id") or _export_election_id(p)
        if not test_id and not election_id:
            continue                    # neither a BV number nor a BV election id

        results_url = d.get("bv_results_url") or (
            f"https://bettervoting.com/{election_id}/results" if election_id else "")
        method = str(race.get("voting_method", "STAR")).strip()
        try:
            nw = int(race.get("num_winners", 1) or 1)
        except Exception:
            nw = 1
        n_cand, n_ballots = _ballot_shape(race)
        # expected winners: flat `expected_winners:` OR nested `expected_results: {winners: […]}`
        exp = race.get("expected_winners")
        if not isinstance(exp, list):
            er = race.get("expected_results")
            exp = er.get("winners") if isinstance(er, dict) else None
        expected = ", ".join(map(str, exp)) if isinstance(exp, list) else ""
        # Write-up page: a same-stem sibling `<stem>.md`, else the folder's
        # generated page `<folder>_pages/<stem>.md`.
        stem = os.path.basename(rel)[:-5]
        folder = os.path.dirname(rel)
        sib = rel[:-5] + ".md"
        pages = f"{folder}/{os.path.basename(folder)}_pages/{stem}.md" if folder else ""
        md_rel = (sib if os.path.exists(os.path.join(REPO, sib))
                  else pages if pages and os.path.exists(os.path.join(REPO, pages))
                  else "")

        rows.append({
            "TestID": str(test_id), "Case": name[:-5], "ElectionID": str(election_id),
            "Method": method, "Winners": nw, "Candidates": n_cand,
            "Ballots": n_ballots, "Expected": expected,
            "YAML": rel, "MD": md_rel, "ResultsURL": results_url,
        })
    # BV-numbered cases first (by number), then export-only cases (no BV number).
    rows.sort(key=lambda r: (_test_num(r["TestID"]) is None,
                             _test_num(r["TestID"]) or 0, r["Case"]))
    return rows


COLS = ["TestID", "Case", "ElectionID", "Method", "Winners", "Candidates",
        "Ballots", "Expected", "YAML", "MD", "ResultsURL"]


def write_csv(rows):
    path = os.path.join(OUT_DIR, "bv_cases.csv")
    with open(path, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=COLS)
        w.writeheader()
        w.writerows(rows)
    return path


def write_md(rows):
    nums = sorted({n for r in rows if (n := _test_num(r["TestID"])) is not None})
    methods = {}
    for r in rows:
        methods[r["Method"]] = methods.get(r["Method"], 0) + 1

    out = ["# BetterVoting test-case registry (repo subset)\n",
           "**Auto-generated — do not edit by hand.** Run "
           "`python STARVote_LH_tabulation_engine/tools_adam/scripts/build_bv_registry.py`.\n",
           "Every BV-backed case in this repo (a `bv_test_id:` field, a `bv…` filename, "
           "or a frozen `_bv_export.json`). Cases with a real BetterVoting election but "
           "no assigned BV number (e.g. the `Runoff_NN` set) appear under their case "
           "name. Machine-readable twin: [`bv_cases.csv`](bv_cases.csv) "
           "(GitHub sorts CSV columns on click). **The master Google Sheet stays "
           "authoritative for the full BV numbering** — it also tracks non-tabulation "
           "QA (UI, roles, archive…) that has no YAML here.\n"]
    out.append(f"**{len(rows)} cases** · methods: "
               + ", ".join(f"{m} ({c})" for m, c in sorted(methods.items())) + ".\n")
    out.append("> Multi-race (contested) elections are grouped race-by-race in "
               "[multirace_elections.md](multirace_elections.md).\n")
    numbered = [r['TestID'] for r in rows if _test_num(r['TestID']) is not None]
    unnumbered = sum(1 for r in rows if _test_num(r['TestID']) is None)
    out.append(f"**BV-numbered Test IDs:** {', '.join(numbered)}."
               + (f"  (+{unnumbered} export-backed cases with no BV number.)" if unnumbered else "")
               + "\n")
    if nums:
        out.append(f"Highest number here is **BV{nums[-1]}** → the next free number above "
                   f"the repo is **BV{nums[-1] + 1}**. (Numbering is sparse and the master "
                   f"Google Sheet is authoritative for choosing the next number; this list "
                   f"only avoids collisions with existing repo files.)\n")

    out.append("| Test ID | Case | BV id | Method | W | Cand | Ballots | Winners | Page | YAML |")
    out.append("|---------|------|-------|--------|:-:|:-:|:-:|---------|------|------|")
    for r in rows:
        page = f"[page]({os.path.relpath(os.path.join(REPO, r['MD']), OUT_DIR).replace(os.sep,'/')})" if r["MD"] else "—"
        yl = f"[yaml]({os.path.relpath(os.path.join(REPO, r['YAML']), OUT_DIR).replace(os.sep,'/')})"
        bv = f"[`{r['ElectionID']}`]({r['ResultsURL']})" if r["ElectionID"] and r["ResultsURL"] else (r["ElectionID"] or "—")
        out.append(f"| {r['TestID'] or '—'} | {r['Case']} | {bv} | {r['Method']} | {r['Winners']} | "
                   f"{r['Candidates']} | {r['Ballots']} | {r['Expected']} | {page} | {yl} |")
    path = os.path.join(OUT_DIR, "BV_registry.md")
    open(path, "w").write("\n".join(out) + "\n")
    return path


if __name__ == "__main__":
    rows = collect()
    c = write_csv(rows)
    m = write_md(rows)
    print(f"wrote {os.path.relpath(c, REPO)} and {os.path.relpath(m, REPO)} "
          f"({len(rows)} BV cases)")
