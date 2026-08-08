#!/usr/bin/env python3
"""
rctab_convert.py — turn a repo ranked-ballot YAML into RCTab input.

RCTab (https://www.rcvresources.org/rctab) is the federally-tested, state-certified
tabulator that US jurisdictions actually run on election night. It reads cast vote
records from Dominion / ES&S / Hart / Clear Ballot — and, via a sixth provider its
published documentation does not mention, from a **generic CSV**:

    CSV("genericCsv", "CSV"),        # ContestConfig.java, present in the v2.1.0 tag

whose reader states its own design: *"Parses a CSV with candidates in columns, cast
vote records in rows, and vote rankings in cells."* That is the same shape as this
repo's `ballots:` block, so a case converts by transposition.

This script writes the two files RCTab needs — `<stem>.csv` and `<stem>_config.json` —
and needs no Java. Running them is `rctab_crosscheck.py`'s job.

THE INVERSION (the whole reason this is a script and not a sed command)
----------------------------------------------------------------------
Our ballots and RCTab's mean opposite things by the same numbers:

    ours (score)   Ada,Ben,Cara  /  5,2,0     5 is BEST,  0 is counted-and-worthless
    RCTab (rank)   Ada,Ben,Cara  /  1,2,<->   1 is BEST,  blank is NOT RANKED

A pass-through would hand RCTab a ballot ranking each voter's favourite last. So the
`A>B>C` level list is expanded to rank integers per candidate, and a candidate the
voter never ranked is left **blank**, not zero.

EQUAL RANKS ARE REFUSED (--allow-equal-ranks to override)
---------------------------------------------------------
This repo's ranked ballots may tie candidates within a level (`Ava=Bianca>Cara`), and
the LH engine honours that as genuine indifference. RCTab's ranked ballots do not have
that concept: two candidates sharing a rank is an **overvote**, disposed of by the
config's `overvoteRule`. Emitting them silently would compare two different elections,
so by default this refuses. The override exists for deliberately studying the overvote
rules, and says so in the generated `rulesDescription`.

CANDIDATE ORDER IS LOAD-BEARING
-------------------------------
Under `tiebreakMode: useCandidateOrder`, the order of the `candidates` array IS the
tiebreak ladder. `--candidate-order` controls it (`ballot` = first appearance across
the ballots, `alpha`, or an explicit comma-separated list) — which is what lets a
caller show that RCTab's tie answer moves with a *declared, auditable* order, where
the vendored pyrankvote's moves with the order the ballot rows happen to be typed in.

Usage:
    uv run STARVote_LH_tabulation_engine/tools_adam/rctab_tabulation_engine/rctab_convert.py FILE.yaml [-o OUTDIR]
    ... --batch-elimination --tiebreak useCandidateOrder --candidate-order ballot
"""
import argparse
import csv
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_TOOLS = os.path.dirname(_HERE)
_ENGINE = os.path.dirname(_TOOLS)
sys.path.insert(0, os.path.join(_TOOLS, "pref_voting_tabulation_engine"))
sys.path.insert(0, _ENGINE)
# parse_election handles nested/flat YAML and both ballot families; no pref_voting needed.
from pref_voting_tabulation import parse_election  # noqa: E402

# ContestConfig.java Provider enum — the value the published docs omit.
PROVIDER = "genericCsv"

# Tabulator.java WinnerElectionMode / ContestConfig.java TiebreakMode.
TIEBREAK_MODES = [
    "random", "stopCountingAndAsk", "previousRoundCountsThenRandom",
    "previousRoundCountsThenAsk", "useCandidateOrder", "generatePermutation",
]
OVERVOTE_RULES = ["alwaysSkipToNextRank", "exhaustImmediately", "exhaustIfMultipleContinuing"]


def load_yaml_meta(path):
    """election_title, straight from the file (parse_election drops it)."""
    try:
        import yaml
        with open(path, encoding="utf-8") as fh:
            doc = yaml.safe_load(fh) or {}
        return doc.get("election_title") or doc.get("title") or os.path.basename(path)
    except Exception:
        return os.path.basename(path)


def ballots_to_rankings(voters, allow_equal):
    """[[['Amy'],['Bruno']], ...] -> [{'Amy': 1, 'Bruno': 2}, ...]

    Level index i (0-based) becomes rank i+1. Candidates sharing a level share a
    rank — an overvote to RCTab — so that is refused unless explicitly allowed.
    """
    rows, equal_seen = [], False
    for levels in voters:
        ranking = {}
        for i, level in enumerate(levels):
            if len(level) > 1:
                equal_seen = True
            for cand in level:
                # First mention wins: a repeated candidate on one ballot is a
                # duplicate ranking, which RCTab handles via exhaustOnDuplicateCandidate.
                ranking.setdefault(cand, i + 1)
        rows.append(ranking)
    if equal_seen and not allow_equal:
        raise SystemExit(
            "refusing to convert: this file has EQUAL RANKS (a 'Ava=Bianca>Cara' level).\n"
            "  The LH engine reads those as genuine indifference; RCTab reads two candidates\n"
            "  at one rank as an OVERVOTE and applies its overvoteRule. Converting silently\n"
            "  would compare two different elections.\n"
            "  Pass --allow-equal-ranks (and pick --overvote-rule) to study that on purpose."
        )
    return rows, equal_seen


def order_candidates(cands_sorted, voters, how):
    """Resolve --candidate-order into the config's candidate array order."""
    if how == "alpha":
        return list(cands_sorted)
    if how == "ballot":
        seen = []
        for levels in voters:
            for level in levels:
                for cand in level:
                    if cand not in seen:
                        seen.append(cand)
        # anyone never ranked still has to appear
        return seen + [c for c in cands_sorted if c not in seen]
    explicit = [c.strip() for c in how.split(",") if c.strip()]
    missing = set(cands_sorted) - set(explicit)
    unknown = set(explicit) - set(cands_sorted)
    if missing or unknown:
        raise SystemExit(
            f"--candidate-order must list every candidate exactly once.\n"
            f"  missing: {sorted(missing) or 'none'}\n  unknown: {sorted(unknown) or 'none'}"
        )
    return explicit


def write_csv(path, candidates, rankings):
    """Column 1 = ballot id, columns 2.. = candidates; cells = rank ints, blank = unranked."""
    with open(path, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["Ballot ID"] + candidates)
        for i, ranking in enumerate(rankings, 1):
            w.writerow([f"b{i}"] + [ranking.get(c, "") for c in candidates])


def build_config(title, csv_name, candidates, args, equal_seen, n_ballots):
    notes = [f"Converted from {os.path.basename(args.yaml)} by rctab_convert.py",
             f"candidate order: {args.candidate_order}"]
    if equal_seen:
        notes.append("WARNING: equal ranks emitted as shared rank (overvote to RCTab)")
    return {
        "tabulatorVersion": args.tabulator_version,
        "outputSettings": {
            "contestName": title[:110],
            "outputDirectory": "output",
            "contestDate": "",
            "contestJurisdiction": "star-voting-library",
            "contestOffice": "",
            "tabulateByBatch": False,
            "tabulateByPrecinct": False,
            "generateCdfJson": False,
        },
        "cvrFileSources": [{
            "filePath": csv_name,
            "contestId": "",
            "firstVoteColumnIndex": "2",   # 1-based; column 1 is the ballot id
            "firstVoteRowIndex": "2",      # 1-based; row 1 is the candidate header
            "idColumnIndex": "1",
            "batchColumnIndex": "",
            "precinctColumnIndex": "",
            "overvoteDelimiter": "",
            "provider": PROVIDER,
            "overvoteLabel": "",
            "skippedRankLabel": "",
            "undeclaredWriteInLabel": "",
            "treatBlankAsUndeclaredWriteIn": False,
        }],
        "candidates": [{"name": c, "excluded": False, "aliases": []} for c in candidates],
        "rules": {
            "tiebreakMode": args.tiebreak,
            "overvoteRule": args.overvote_rule,
            "winnerElectionMode": "singleWinnerMajority",
            "randomSeed": args.random_seed,
            "numberOfWinners": "1",
            "multiSeatBottomsUpPercentageThreshold": "",
            # RCTab validates this as 1..20 — "0" is rejected outright. Irrelevant to a
            # single-winner whole-vote count, but it has to be a legal value.
            "decimalPlacesForVoteArithmetic": "4",
            "minimumVoteThreshold": "0",
            "maxSkippedRanksAllowed": "unlimited",
            "maxRankingsAllowed": str(len(candidates)),
            "nonIntegerWinningThreshold": False,
            "doesFirstRoundDetermineThreshold": False,
            "hareQuota": False,
            "batchElimination": args.batch_elimination,
            "continueUntilTwoCandidatesRemain": args.continue_until_two,
            "stopTabulationEarlyAfterRound": "",
            "exhaustOnDuplicateCandidate": False,
            "rulesDescription": " | ".join(notes)[:1000],
            "treatBlankAsUndeclaredWriteIn": False,
        },
        # Not read by RCTab — a provenance trail for whoever finds these files later.
        "_starVotingLibrary": {
            "sourceYaml": os.path.relpath(os.path.abspath(args.yaml), _ENGINE + "/.."),
            "ballotsConverted": n_ballots,
        },
    }


def convert(args):
    cands_sorted, _dicts, voters, _lot, _has_eq, vm = parse_election(args.yaml)
    if voters is None:
        raise SystemExit(
            f"refusing to convert: {os.path.basename(args.yaml)} has SCORE ballots "
            f"(voting_method: {vm}).\n"
            "  RCTab counts ranked ballots only — every winnerElectionMode it has is IRV or STV.\n"
            "  There is nothing for it to say about STAR, Score, Approval or Ranked Robin."
        )
    rankings, equal_seen = ballots_to_rankings(voters, args.allow_equal_ranks)
    candidates = order_candidates(cands_sorted, voters, args.candidate_order)

    stem = os.path.splitext(os.path.basename(args.yaml))[0]
    outdir = args.outdir or os.path.join(_HERE, "rctab_cases", stem)
    os.makedirs(outdir, exist_ok=True)
    csv_name = f"{stem}.csv"
    csv_path = os.path.join(outdir, csv_name)
    cfg_path = os.path.join(outdir, f"{stem}_config.json")

    write_csv(csv_path, candidates, rankings)
    cfg = build_config(load_yaml_meta(args.yaml), csv_name, candidates, args, equal_seen, len(rankings))
    with open(cfg_path, "w", encoding="utf-8") as fh:
        json.dump(cfg, fh, indent=2)
        fh.write("\n")

    print(f"  candidates : {', '.join(candidates)}   ({args.candidate_order} order)")
    print(f"  ballots    : {len(rankings)}")
    print(f"  tiebreak   : {args.tiebreak}   batchElimination: {args.batch_elimination}")
    print(f"  csv        : {csv_path}")
    print(f"  config     : {cfg_path}")
    return csv_path, cfg_path


def add_args(p):
    p.add_argument("yaml", help="a ranked-ballot election YAML")
    p.add_argument("-o", "--outdir", help="output dir (default: rctab_cases/<stem>/ beside this script)")
    p.add_argument("--tiebreak", default="useCandidateOrder", choices=TIEBREAK_MODES,
                   help="RCTab tiebreakMode (default: useCandidateOrder — declared and reproducible)")
    p.add_argument("--overvote-rule", default="alwaysSkipToNextRank", choices=OVERVOTE_RULES)
    p.add_argument("--candidate-order", default="ballot",
                   help="'ballot' (first appearance), 'alpha', or an explicit comma-separated list. "
                        "Under useCandidateOrder this IS the tiebreak ladder.")
    p.add_argument("--batch-elimination", action="store_true",
                   help="eliminate every candidate tied for last in one step")
    p.add_argument("--continue-until-two", action="store_true")
    p.add_argument("--random-seed", default="", help="only meaningful for the random tiebreak modes")
    p.add_argument("--allow-equal-ranks", action="store_true",
                   help="emit '=' levels as a shared rank (an OVERVOTE to RCTab) instead of refusing")
    p.add_argument("--tabulator-version", default="2.1.0")
    return p


if __name__ == "__main__":
    parser = add_args(argparse.ArgumentParser(description=__doc__.split("\n")[1]))
    convert(parser.parse_args())
