#!/usr/bin/env python3
"""
rctab_sweep.py — run EVERY ranked case in the library through RCTab, in one pass.

`rctab_crosscheck.py` is the microscope: one case, round by round, with the tiebreak
sweeps. This is the wide-angle lens — it converts and counts the whole ranked corpus
and prints one line per case, so a regression anywhere shows up as a row that stopped
saying AGREE.

WHAT IT SELECTS
---------------
Ranked-ballot elections only, and by default only the ones RCTab can actually count:

  IRV / RCV_IRV / RCV-IRV      single-winner instant runoff   → --irv (the default)
  STV                          multi-seat transferable        → --stv
  RankedRobin                  NEVER — RCTab implements no Condorcet method at all,
                               so "agreement" would be a coincidence of the profile,
                               not a check of anything. Refused rather than reported.

Score-ballot files (STAR, Approval, Score) are not ranked and are skipped outright.

SKIPS ARE PRINTED, NOT SWALLOWED
--------------------------------
A case the converter refuses — equal-rank levels, a score ballot, a non-STV multi-seat
method — is listed as SKIP with its reason. A sweep that quietly counted 60 of 70 cases
and reported "all agree" would be worse than useless, so the summary always states how
many were converted, skipped and failed.

Usage:
    RCTAB_HOME=/path/to/rcv \\
      uv run STARVote_LH_tabulation_engine/tools_adam/rctab_tabulation_engine/rctab_sweep.py
    ... --stv                 # STV cases instead of IRV
    ... --all                 # both
    ... --jobs 4              # parallel JVM launches (default 4)
    ... --keep                # keep each case's converted CSV + config under rctab_cases/
    ... --only burlington     # substring filter on the path
"""
import argparse
import os
import shutil
import sys
import tempfile
from concurrent.futures import ThreadPoolExecutor

_HERE = os.path.dirname(os.path.abspath(__file__))
_TOOLS = os.path.dirname(_HERE)
_ENGINE = os.path.dirname(_TOOLS)
REPO = os.path.dirname(_ENGINE)
sys.path.insert(0, _HERE)
sys.path.insert(0, os.path.join(_TOOLS, "pref_voting_tabulation_engine"))

from rctab_convert import convert  # noqa: E402
from rctab_crosscheck import (  # noqa: E402
    find_rctab, rctab_version, run_rctab, winners_of, expected_from_yaml,
)

IRV_METHODS = {"IRV", "RCV_IRV", "RCV-IRV", "RCV_IRV_HARE"}
STV_METHODS = {"STV"}
# Directories that hold deliberately-malformed fixtures or engine internals.
SKIP_DIRS = {".git", "site", "node_modules", "__pycache__", "2_negative", "negative_cases",
             "harness_cases", "rctab_cases", "output"}


def discover(want_irv, want_stv, only):
    """Every ranked election file whose method is in scope, as (path, method, seats)."""
    import yaml as Y
    found = []
    for dirpath, dirnames, files in os.walk(REPO):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS
                       and not d.startswith(".")
                       and not d.endswith(("_tabulated", "_pages"))]
        for fn in sorted(files):
            if not fn.endswith(".yaml"):
                continue
            path = os.path.join(dirpath, fn)
            if only and only not in os.path.relpath(path, REPO):
                continue
            try:
                doc = Y.safe_load(open(path, encoding="utf-8")) or {}
            except Exception:
                continue
            if not isinstance(doc, dict) or "ballots" not in doc:
                continue
            body = str(doc.get("ballots") or "")
            if ">" not in "\n".join(l.split("#")[0] for l in body.splitlines()):
                continue                                   # not a ranked ballot
            method = str(doc.get("voting_method") or "").strip()
            seats = int(doc.get("num_winners") or 1)
            if method in IRV_METHODS and want_irv:
                found.append((path, method, seats))
            elif method in STV_METHODS and want_stv:
                found.append((path, method, seats))
    return sorted(found)


def convert_case(path, method, seats, version, outroot, keep):
    """Convert one case. SERIAL by design — see below. Returns (result, cfg_path|None).

    convert() prints, and silencing it means swapping the process-wide sys.stdout.
    That is not thread-safe: run under a pool, one worker closes the devnull handle
    while another is mid-write and every case after it dies with "I/O operation on
    closed file". Conversion is pure Python and takes milliseconds, so it runs here
    on one thread and only the JVM launches — the part actually worth parallelising —
    go to the pool.
    """
    rel = os.path.relpath(path, REPO)
    stem = os.path.splitext(os.path.basename(path))[0]
    outdir = os.path.join(outroot, stem) if keep else tempfile.mkdtemp(prefix=f"rctab_{stem}_")
    args = argparse.Namespace(
        yaml=path, outdir=outdir, tiebreak="useCandidateOrder",
        overvote_rule="alwaysSkipToNextRank", candidate_order="ballot",
        batch_elimination=False, continue_until_two=False, random_seed="",
        allow_equal_ranks=False, tabulator_version=version, hand_count_quota=False,
        seats=None,
    )
    res = {"rel": rel, "stem": stem, "method": method, "seats": seats,
           "status": "?", "rctab": [], "ours": expected_from_yaml(path),
           "note": "", "outdir": outdir, "keep": keep}
    try:
        buf, sys.stdout = sys.stdout, open(os.devnull, "w")
        try:
            _csv, cfg = convert(args)
        finally:
            sys.stdout.close()
            sys.stdout = buf
    except SystemExit as e:
        res["status"] = "SKIP"
        res["note"] = str(e).splitlines()[0].replace("refusing to convert: ", "")
        return res, None
    except Exception as e:                                  # noqa: BLE001
        res["status"] = "ERROR"
        res["note"] = f"convert: {type(e).__name__}: {e}"
        return res, None
    return res, cfg


def run_case(launcher, res, cfg):
    """Count one already-converted case. Pool-safe: no shared state, never raises."""
    seats, outdir, keep = res["seats"], res["outdir"], res["keep"]
    try:
        report, blob = run_rctab(launcher, cfg)
    except Exception as e:                                  # noqa: BLE001
        res["status"] = "ERROR"
        res["note"] = f"run: {type(e).__name__}: {e}"
        return res

    if report is None:
        sev = [l.split("SEVERE: ", 1)[-1] for l in blob.splitlines() if "SEVERE" in l]
        res["status"] = "ERROR"
        res["note"] = (sev[0] if sev else "no report produced")[:150]
        return res

    res["rctab"] = winners_of(report)
    res["tiebreaks"] = sum(1 for l in blob.splitlines() if "tie-breaker" in l)
    if not res["ours"]:
        res["status"] = "NO-KEY"
    elif seats > 1:
        res["status"] = "AGREE" if set(res["rctab"]) == set(res["ours"]) else "DISAGREE"
    else:
        res["status"] = "AGREE" if (res["rctab"] and res["rctab"][0] in res["ours"]) else "DISAGREE"

    if not keep:
        shutil.rmtree(outdir, ignore_errors=True)
    else:
        shutil.rmtree(os.path.join(outdir, "output"), ignore_errors=True)
    return res


def main():
    p = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    p.add_argument("--irv", action="store_true", help="single-winner IRV cases (default)")
    p.add_argument("--stv", action="store_true", help="multi-seat STV cases")
    p.add_argument("--all", action="store_true", help="both")
    p.add_argument("--only", help="substring filter on the repo-relative path")
    p.add_argument("--jobs", type=int, default=4, help="parallel JVM launches (default 4)")
    p.add_argument("--keep", action="store_true",
                   help="keep each case's CSV + config under rctab_cases/<stem>/")
    args = p.parse_args()

    want_irv = args.irv or args.all or not (args.irv or args.stv or args.all)
    want_stv = args.stv or args.all

    launcher = find_rctab()
    version = rctab_version(launcher) or "2.1.0"
    cases = discover(want_irv, want_stv, args.only)
    scope = "+".join([s for s, on in (("IRV", want_irv), ("STV", want_stv)) if on])

    print(f"\nRCTab {version}  ({launcher})")
    print(f"scope: {scope}   cases: {len(cases)}   jobs: {args.jobs}\n")
    if not cases:
        raise SystemExit("no cases matched.")

    outroot = os.path.join(_HERE, "rctab_cases")
    # Phase 1, serial: convert everything (fast, and stdout-swapping is not thread-safe).
    prepared = [convert_case(p_, m, s, version, outroot, args.keep) for p_, m, s in cases]
    # Phase 2, parallel: the JVM launches, which are the only slow part.
    results = []
    with ThreadPoolExecutor(max_workers=args.jobs) as pool:
        futures = []
        for res, cfg in prepared:
            futures.append(pool.submit(run_case, launcher, res, cfg) if cfg
                           else pool.submit(lambda r=res: r))
        for fut in futures:
            r = fut.result()
            results.append(r)
            mark = {"AGREE": "✅", "DISAGREE": "❌", "SKIP": "⏭ ", "ERROR": "💥",
                    "NO-KEY": "· "}.get(r["status"], "? ")
            got = ", ".join(r["rctab"]) or "—"
            detail = f"{got}"
            if r["status"] == "DISAGREE":
                detail = f"RCTab {got}   vs ours {', '.join(r['ours'])}"
            elif r["status"] in ("SKIP", "ERROR"):
                detail = r["note"]
            print(f"  {mark} {r['stem'][:46]:<46} {detail}")

    counts = {}
    for r in results:
        counts[r["status"]] = counts.get(r["status"], 0) + 1
    print(f"\n{'='*70}")
    print("  " + "   ".join(f"{k}: {v}" for k, v in sorted(counts.items())))
    ties = sum(r.get("tiebreaks", 0) for r in results)
    print(f"  cases whose count needed a tiebreak: "
          f"{sum(1 for r in results if r.get('tiebreaks'))}  ({ties} tiebreak events)")

    bad = [r for r in results if r["status"] == "DISAGREE"]
    if bad:
        print(f"\n  {len(bad)} DISAGREEMENT(S) — investigate before quoting either number:")
        for r in bad:
            print(f"    {r['rel']}")
            print(f"      RCTab: {', '.join(r['rctab']) or '—'}    ours: {', '.join(r['ours'])}")
    errs = [r for r in results if r["status"] == "ERROR"]
    if errs:
        print(f"\n  {len(errs)} ERROR(S):")
        for r in errs:
            print(f"    {r['rel']}\n      {r['note']}")
    print()
    return 1 if (bad or errs) else 0


if __name__ == "__main__":
    sys.exit(main())
