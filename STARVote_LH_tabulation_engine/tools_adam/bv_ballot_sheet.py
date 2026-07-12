#!/usr/bin/env python3
"""
bv_ballot_sheet.py — generate printable STAR paper ballots for a demo / classroom
hand-count exercise, tied to a BetterVoting (BV) election.

The teacher's front-of-workflow tool: you make a real election on BetterVoting,
then print matching paper ballots so a room can vote by hand, hand-count the result
(see 00_start_here/STAR_Voting/count_star_by_hand.md), and compare to BV's official
tally. This script writes a self-contained, print-ready HTML file — open it and
"Print to PDF". Each ballot carries the STAR instructions, a 0-5 bubble grid per
candidate, and the BV election id + results URL so paper and platform stay linked.

Candidates + title come from ONE of:
  --yaml FILE          a repo election .yaml (title + candidates from its ballots header;
                       picks up bv_election_id automatically if present)
  --bv-export FILE     a frozen BetterVoting <case>_bv_export.json
  --candidates "A,B,C" --title "..." [--bv-id ID] [--question "..."]   manual

Stdlib only — no dependencies. `--selftest` runs known-answer checks.

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
    return title, bv_id, cands


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
    """Return (title, bv_id, [candidates]) from a frozen BV export JSON."""
    data = json.load(open(path, encoding="utf-8"))
    election = data.get("election", data) if isinstance(data, dict) else {}
    title = election.get("title") or election.get("name")
    bv_id = election.get("election_id") or election.get("id") or data.get("election_id")
    cands = _find_candidate_names(data)
    if not cands:
        raise SystemExit(f"Could not find candidate names in {path} "
                         f"(pass --candidates manually).")
    return title, bv_id, cands


# --------------------------------------------------------------------------- #
# HTML ballot rendering.                                                       #
# --------------------------------------------------------------------------- #
INSTRUCTIONS = ("Score each candidate 0 to 5 (fill one bubble per row). "
                "Give your favorite 5, your last choice 0 (or leave blank). "
                "Equal scores are allowed. The two highest-scoring candidates "
                "have an automatic runoff.")

CSS = """
:root { color-scheme: light; }
body { font-family: -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif;
       margin: 0; color: #111; }
.ballot { border: 2px solid #111; border-radius: 8px; padding: 14px 18px;
          margin: 12px; page-break-inside: avoid; }
.ballot h2 { margin: 0 0 2px; font-size: 17px; }
.q { margin: 0 0 8px; color: #333; font-size: 13px; }
.inst { margin: 0 0 10px; font-size: 11.5px; color: #444; }
table { border-collapse: collapse; width: 100%; }
th, td { border: 1px solid #999; padding: 6px 4px; text-align: center; font-size: 13px; }
th.cand, td.cand { text-align: left; width: 42%; font-weight: 600; }
.bub { display: inline-block; width: 15px; height: 15px; border: 1.6px solid #333;
       border-radius: 50%; }
.foot { margin-top: 8px; font-size: 10.5px; color: #555; display: flex;
        justify-content: space-between; }
@media print { .noprint { display: none; } .ballot { margin: 0 0 8px; } }
"""


def render_ballot(title, question, candidates, bv_id):
    rows = []
    header = "".join(f"<th>{n}</th>" for n in range(6))
    for c in candidates:
        cells = "".join('<td><span class="bub"></span></td>' for _ in range(6))
        rows.append(f'<tr><td class="cand">{html.escape(c)}</td>{cells}</tr>')
    results = (f'results: bettervoting.com/{html.escape(bv_id)}/results'
               if bv_id else 'STAR Voting — Score Then Automatic Runoff')
    idline = f'Election {html.escape(bv_id)}' if bv_id else 'demo ballot'
    return f"""
<div class="ballot">
  <h2>{html.escape(title or 'STAR Voting ballot')}</h2>
  <p class="q">{html.escape(question)}</p>
  <p class="inst">{INSTRUCTIONS}</p>
  <table>
    <tr><th class="cand">Candidate</th>{header}</tr>
    {''.join(rows)}
  </table>
  <p class="foot"><span>{idline}</span><span>{results}</span></p>
</div>"""


def render_sheet(title, question, candidates, bv_id, copies, per_page):
    ballots = "\n".join(
        render_ballot(title, question, candidates, bv_id) for _ in range(copies))
    hint = ('<p class="noprint" style="margin:12px 18px;color:#666;font-size:13px">'
            f'{copies} ballots · aim for ~{per_page} per page — use your browser\'s '
            'Print → "Save as PDF". This is the print-and-hand-count front end; '
            'count with count_star_by_hand.md, then compare to BetterVoting.</p>')
    return (f'<!doctype html><html><head><meta charset="utf-8">'
            f'<title>STAR ballots — {html.escape(title or bv_id or "demo")}</title>'
            f'<style>{CSS}</style></head><body>{hint}{ballots}</body></html>')


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
        ("3 ballots rendered", html_out.count('class="ballot"') == 3),
        ("0-5 bubble grid (18 bubbles/ballot = 3 cands x 6)", html_out.count('class="bub"') == 3 * 6 * 3),
        ("html escaping of a tricky name",
         "&lt;b&gt;" in render_ballot("t", "q", ["<b>"], None)),
    ]
    for label, cond in checks:
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
    ap.add_argument("--per-page", type=int, default=2)
    ap.add_argument("--out", default="ballots.html")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()

    if args.selftest:
        raise SystemExit(0 if selftest() else 1)

    title = args.title
    bv_id = args.bv_id
    candidates = None
    if args.yaml:
        title, bv_id2, candidates = from_yaml(args.yaml)
        bv_id = bv_id or bv_id2
        title = args.title or title
    elif args.bv_export:
        t2, bv_id2, candidates = from_bv_export(args.bv_export)
        title = args.title or t2
        bv_id = bv_id or bv_id2
    elif args.candidates:
        candidates = [c.strip() for c in args.candidates.split(",") if c.strip()]
    else:
        raise SystemExit("Provide one of --yaml / --bv-export / --candidates "
                         "(see --help). Run --selftest to verify the tool.")

    question = args.question or "Score each candidate from 0 (worst) to 5 (best)."
    sheet = render_sheet(title, question, candidates, bv_id, args.copies, args.per_page)
    with open(args.out, "w", encoding="utf-8") as f:
        f.write(sheet)
    print(f"Wrote {args.copies} STAR ballots ({len(candidates)} candidates) to "
          f"{os.path.abspath(args.out)}")
    print("Open it in a browser and Print → Save as PDF.")
    if bv_id:
        print(f"Linked to BetterVoting election {bv_id} "
              f"(results: https://bettervoting.com/{bv_id}/results).")


if __name__ == "__main__":
    main()
