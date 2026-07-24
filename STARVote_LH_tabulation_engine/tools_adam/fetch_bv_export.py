#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["requests"]
# ///
"""
fetch_bv_export.py — freeze a BetterVoting election's full export via the public API
=====================================================================================

Downloads everything the BV UI's manual "export" gives you — Election config,
Ballots, and Results — and writes the house-format frozen export
(`{"Election": …, "Ballots": …, "Results": …}`) without anyone clicking through
the UI. Ends the "Adam must export from the UI" step of the case workflow.

HOW IT WORKS — three ANONYMOUS public GETs (no login, no token):

    GET /API/Election/{id}                     -> .election   == export "Election"
    GET /API/Election/{id}/anonymizedBallots   -> .ballots    == export "Ballots"
    GET /API/ElectionResult/{id}               -> .results    == export "Results"

(The admin-only `GET /API/Election/{id}/ballots` returns 401 anonymously, but
`anonymizedBallots` is public and — verified against the frozen `vqyqkr` export —
carries the identical ballot_id / election_id / precinct / votes shape. Results
are tabulated on demand by `getElectionResultsController`, so an election never
needs to be "closed" first.)

USAGE (uv-native, PEP 723 — no venv needed):

    # one election, explicit output path (house naming: <yaml stem>_bv_export.json)
    uv run fetch_bv_export.py 7mckyg -o 01_STAR/favorite_betrayal/cases/bv2206_7mckyg_fbc_honest_tepid_consensus_bv_export.json

    # several at once, default names <id>_bv_export.json in the current dir
    uv run fetch_bv_export.py 7mckyg b6xrdr 39py93

    # a crash-case election whose Results endpoint 500s (e.g. the STV
    # sole-survivor crashers): freeze config+ballots now, Results as []
    uv run fetch_bv_export.py gvtg2h --without-results -o …_bv_export.json

CAVEATS:
* Frozen means frozen: an existing output file is NEVER overwritten unless you
  pass --force. Re-fetching a live election can differ in ballot order and
  volatile fields (update_date / state), so don't casually re-freeze.
* --without-results writes `"Results": []` plus a `_note` field naming the HTTP
  error, so the gap is self-documenting; re-fetch without the flag once BV fixes
  the tabulator (then diff + replace deliberately).
"""

import argparse
import json
import sys
from pathlib import Path

import requests

BASE = "https://bettervoting.com/API"
TIMEOUT = 60


def _get(path):
    """GET a BV API path; return (status_code, parsed json or None)."""
    url = f"{BASE}/{path}"
    r = requests.get(url, timeout=TIMEOUT)
    try:
        body = r.json()
    except ValueError:
        body = None
    return r.status_code, body


def fetch_export(eid, without_results=False):
    """Fetch and assemble the frozen-export dict for one election id.

    Returns (export_dict, notes:list[str]). Raises RuntimeError on a failure
    that should stop the freeze (bad id, missing ballots, results error
    without --without-results)."""
    notes = []

    code, el = _get(f"Election/{eid}")
    if code != 200 or not isinstance(el, dict) or "election" not in el:
        raise RuntimeError(f"{eid}: GET /Election -> HTTP {code} (bad id, or BV down?)")
    election = el["election"]

    code, bal = _get(f"Election/{eid}/anonymizedBallots")
    if code != 200 or not isinstance(bal, dict) or "ballots" not in bal:
        raise RuntimeError(f"{eid}: GET /anonymizedBallots -> HTTP {code}")
    ballots = bal["ballots"]
    if not ballots:
        notes.append("WARNING: zero ballots on the server")

    export = {"Election": election, "Ballots": ballots, "Results": []}

    code, res = _get(f"ElectionResult/{eid}")
    if code == 200 and isinstance(res, dict) and "results" in res:
        export["Results"] = res["results"]
    elif without_results:
        export["_note"] = (f"Results omitted: GET /API/ElectionResult/{eid} returned "
                           f"HTTP {code} at freeze time (known-crash election). "
                           "Re-fetch without --without-results once BV fixes the tabulator.")
        notes.append(f"Results endpoint returned HTTP {code} — froze WITHOUT Results")
    else:
        raise RuntimeError(
            f"{eid}: GET /ElectionResult -> HTTP {code}. If this is a known-crash "
            "election (e.g. the STV sole-survivor cases), re-run with --without-results.")
    return export, notes


def summarize(export):
    """One-line-per-race human summary so the terminal shows what got frozen."""
    e = export["Election"]
    lines = [f'  "{e.get("title", "?")}"  (state: {e.get("state", "?")}, '
             f'{len(export["Ballots"])} ballots)']
    cand_name = {}
    for race in e.get("races", []):
        for c in race.get("candidates", []):
            cand_name[c.get("candidate_id")] = c.get("candidate_name")
    for i, r in enumerate(export["Results"]):
        elected = ", ".join(c.get("name") or cand_name.get(c.get("candidate_id"), "?")
                            for c in r.get("elected", []))
        lines.append(f'  race {i + 1}: {r.get("votingMethod", "?")} -> {elected or "(none)"}')
    if not export["Results"]:
        lines.append("  (no Results block)")
    return "\n".join(lines)


def main(argv=None):
    ap = argparse.ArgumentParser(description="Freeze BetterVoting election export(s) "
                                             "via the public API.")
    ap.add_argument("election_ids", nargs="+", help="BV election id(s), e.g. 7mckyg")
    ap.add_argument("-o", "--output", help="output path (only with a single id); "
                                           "default <id>_bv_export.json in cwd")
    ap.add_argument("--force", action="store_true",
                    help="overwrite an existing output file (frozen means frozen — "
                         "only with intent)")
    ap.add_argument("--without-results", action="store_true",
                    help="tolerate a failing Results endpoint and freeze with "
                         "Results: [] (crash-case elections)")
    args = ap.parse_args(argv)

    if args.output and len(args.election_ids) > 1:
        ap.error("-o/--output only makes sense with a single election id")

    failures = 0
    for eid in args.election_ids:
        out = Path(args.output) if args.output else Path(f"{eid}_bv_export.json")
        if out.exists() and not args.force:
            print(f"✗ {eid}: {out} already exists — frozen means frozen "
                  "(use --force to overwrite deliberately).")
            failures += 1
            continue
        try:
            export, notes = fetch_export(eid, without_results=args.without_results)
        except RuntimeError as ex:
            print(f"✗ {ex}")
            failures += 1
            continue
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(export, indent=2, ensure_ascii=False) + "\n",
                       encoding="utf-8")
        print(f"✓ {eid} -> {out}")
        print(summarize(export))
        for n in notes:
            print(f"  ⚠ {n}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
