#!/usr/bin/env python3
"""
check_star_vs_rr_causes.py
==========================
Guard the CAUSE CLAIMS of 05_Ranked_Robin/star_vs_rr_divergence/ against the
ballots — the structural assertions each sample's `scenario_description` makes
about *why* STAR and Ranked Robin disagree.

WHY THIS EXISTS — the gap left by check_star_vs_rr_labels.py. That checker
guards every place a sample *names a winner*, which is what drifted in
cycle_C10_fewV29_bloc_2 (7ddde36). But the descriptions assert a good deal more
than two names, and none of it was checked:

    "CAUSE = CONDORCET CYCLE: no candidate beats all others (A>I>G>A) ..."
    "CAUSE = DARK HORSE: F is the Condorcet winner (beats every rival
     head-to-head) but only #9 of 10 by score total (1647 vs leader G 1929)
     -- ... misses STAR's score finalists (G, C)."

Those are falsifiable statements about the pairwise matrix and the score totals,
and a reader is entitled to trust them: the cycle chain is the sample's whole
teaching payload. A sample could name both winners correctly and still claim a
cycle link that does not exist, a dark horse that is not actually the Condorcet
winner, or a score rank that is off — and every existing test would pass, because
the winners would still be right. The labels checker cannot see any of it.

WHAT IS CHECKED. Truth is the ballots, read through the engine's own pairwise
code (calculate_preference_matrix / condorcet_winner), so "beats head-to-head"
means here exactly what it means in the [Divergence from STAR] block.

  flavour     the filename's flavour (cycle_ / darkhorse_) matches the CAUSE
              clause, and exactly one cause clause is present

  cycle       * no strict Condorcet winner exists ("no candidate beats all
                others" -- note a WEAK Condorcet winner may still exist, and
                does in cycle_C10_fewV29_bloc_2, where B beats all but ties G;
                that is consistent, not a defect)
              * every link of the claimed chain (A>I>G>A) is a real strict
                pairwise win, the chain closes, and it runs through at least
                three distinct candidates

  dark horse  * the named dark horse really is the strict Condorcet winner
              * "#N of M by score total" -- M is the field size and N is the
                dark horse's rank, counted as 1 + (candidates strictly above),
                so ties rank fairly
              * the two score totals quoted, and the named score leader
              * "misses STAR's score finalists (F1, F2)" -- that pair really is
                a valid top-two by score (nobody outside it outscores either
                member), and the dark horse really is not in it

NO --fix, deliberately. check_star_vs_rr_labels.py can rewrite a label because
the right answer is a substitution. A false cause claim is not: if a sample has
no cycle, or its dark horse is not the Condorcet winner, the sample no longer
demonstrates what it exists to demonstrate, and that is a judgement call about
the sample — not a string to swap. So every message quotes the correct value
and leaves the decision to a human.

Usage:
    python tools_adam/scripts/check_star_vs_rr_causes.py            # exit 1 on drift
    python tools_adam/scripts/check_star_vs_rr_causes.py --dir DIR  # check a copy
"""

import argparse
import re
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
ENGINE_DIR = SCRIPT_DIR.parent.parent
REPO_ROOT = ENGINE_DIR.parent
sys.path.insert(0, str(ENGINE_DIR))

import starvote_larry_hastings as wrapper  # noqa: E402

DEFAULT_DIR = REPO_ROOT / "05_Ranked_Robin" / "star_vs_rr_divergence"

CYCLE_CAUSE = re.compile(r"CAUSE = CONDORCET CYCLE: no candidate beats all others"
                         r"(?: \(([A-Za-z0-9>]+)\))?")
DARKHORSE_CAUSE = re.compile(
    r"CAUSE = DARK HORSE: (\w+) is the Condorcet winner \(beats every rival "
    r"head-to-head\) but only #(\d+) of (\d+) by score total "
    r"\((\d+) vs leader (\w+) (\d+)\)")
FINALISTS = re.compile(r"misses STAR's score finalists \((\w+), (\w+)\)")


def ballots_of(path):
    """(candidates, ballots) as the engine parses them — weighted rows expanded."""
    el = wrapper.load_election(str(path))
    candidates, ballots, _ = wrapper.parse_ballots_from_string(el["ballots"])
    return candidates, ballots


def beats(matrix, a, b):
    """Does `a` win the head-to-head against `b` by strict majority?"""
    for_a, against_a = matrix[a][b][0], matrix[a][b][1]
    return for_a > against_a


def score_totals(candidates, ballots):
    return {c: sum(b.get(c, 0) for b in ballots) for c in candidates}


def check_cycle(text, candidates, ballots, matrix, problems):
    """The 'no candidate beats all others (A>I>G>A)' claim."""
    cw = wrapper.condorcet_winner(candidates, ballots)
    if cw is not None:
        problems.append(
            f"claims a Condorcet cycle, but {cw} beats every rival head-to-head "
            f"— this is a dark horse, not a cycle")

    chain = CYCLE_CAUSE.search(text).group(1)
    if not chain:
        return                                   # the chain is optional; 1 of 30 omits it

    names = chain.split(">")
    unknown = [n for n in names if n not in candidates]
    if unknown:
        problems.append(f"cycle chain {chain} names non-candidate(s): {', '.join(unknown)}")
        return
    if names[0] != names[-1]:
        problems.append(f"cycle chain {chain} does not close — "
                        f"starts at {names[0]}, ends at {names[-1]}")
    if len(set(names)) < 3:
        problems.append(f"cycle chain {chain} runs through only {len(set(names))} "
                        f"candidate(s); a cycle needs at least 3")
    for u, v in zip(names, names[1:]):
        if not beats(matrix, u, v):
            f_u, a_u, _ = matrix[u][v]
            verdict = "ties" if f_u == a_u else "loses to"
            problems.append(f"cycle chain {chain}: the claimed link {u}>{v} is false — "
                            f"{u} {verdict} {v} ({f_u} to {a_u})")


def check_darkhorse(text, candidates, ballots, matrix, problems):
    """The 'X is the Condorcet winner but only #N of M by score total' claim."""
    m = DARKHORSE_CAUSE.search(text)
    horse, rank, field, horse_score, leader, leader_score = (
        m.group(1), int(m.group(2)), int(m.group(3)),
        int(m.group(4)), m.group(5), int(m.group(6)))

    if horse not in candidates:
        problems.append(f"dark horse {horse} is not a candidate")
        return

    cw = wrapper.condorcet_winner(candidates, ballots)
    if cw != horse:
        problems.append(
            f"claims {horse} is the Condorcet winner, but "
            + (f"{cw} is" if cw else "no candidate beats every rival (a cycle)"))

    totals = score_totals(candidates, ballots)
    if field != len(candidates):
        problems.append(f"claims a field of {field}, but there are {len(candidates)} candidates")
    if totals[horse] != horse_score:
        problems.append(f"claims {horse} scores {horse_score}, actual total is {totals[horse]}")

    real_rank = 1 + sum(1 for c in candidates if totals[c] > totals[horse])
    if real_rank != rank:
        problems.append(f"claims {horse} is #{rank} by score total, actual rank is "
                        f"#{real_rank} (ties counted fairly)")

    top = max(totals.values())
    if leader not in candidates:
        problems.append(f"named score leader {leader} is not a candidate")
    elif totals[leader] != top:
        problems.append(f"claims {leader} leads on score, but {totals[leader]} is behind "
                        f"the top total {top} ({'/'.join(sorted(c for c in candidates if totals[c] == top))})")
    elif totals[leader] != leader_score:
        problems.append(f"claims leader {leader} scores {leader_score}, "
                        f"actual total is {totals[leader]}")

    fm = FINALISTS.search(text)
    if not fm:
        problems.append("dark-horse clause names no score finalists")
        return
    pair = [fm.group(1), fm.group(2)]
    unknown = [c for c in pair if c not in candidates]
    if unknown:
        problems.append(f"claimed finalists name non-candidate(s): {', '.join(unknown)}")
        return
    if pair[0] == pair[1]:
        problems.append(f"claimed finalists are the same candidate ({pair[0]})")
        return
    # A valid top-two by score: nobody outside the pair outscores either member.
    cutoff = min(totals[c] for c in pair)
    above = [c for c in candidates if c not in pair and totals[c] > cutoff]
    if above:
        problems.append(
            f"claimed score finalists ({', '.join(pair)}) are not the top two — "
            f"{', '.join(sorted(above))} outscore(s) them "
            f"(top totals: {', '.join(f'{c} {totals[c]}' for c in sorted(candidates, key=lambda c: -totals[c])[:3])})")
    if horse in pair:
        problems.append(f"claims the dark horse {horse} MISSES the finalists, "
                        f"but names it as one of them")


def check_file(path):
    """Return a list of problem strings for one sample (empty == clean)."""
    problems = []
    try:
        candidates, ballots = ballots_of(path)
        matrix = wrapper.calculate_preference_matrix(candidates, ballots)
    except Exception as e:  # noqa: BLE001
        return [f"could not read ballots: {e}"]
    if not matrix:
        return ["engine produced no preference matrix"]

    text = path.read_text(encoding="utf-8")
    is_cycle = CYCLE_CAUSE.search(text) is not None
    is_darkhorse = DARKHORSE_CAUSE.search(text) is not None

    if is_cycle and is_darkhorse:
        return ["description states BOTH a cycle and a dark-horse cause"]
    if not (is_cycle or is_darkhorse):
        return ["description states no recognised CAUSE clause "
                "(expected 'CAUSE = CONDORCET CYCLE' or 'CAUSE = DARK HORSE')"]

    # The filename carries the flavour; it must agree with the prose.
    stem_flavour = "cycle" if path.stem.startswith("cycle") else (
        "darkhorse" if path.stem.startswith("darkhorse") else None)
    prose_flavour = "cycle" if is_cycle else "darkhorse"
    if stem_flavour and stem_flavour != prose_flavour:
        problems.append(f"filename says '{stem_flavour}' but the description "
                        f"states a {prose_flavour} cause")

    if is_cycle:
        check_cycle(text, candidates, ballots, matrix, problems)
    else:
        check_darkhorse(text, candidates, ballots, matrix, problems)
    return problems


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dir", default=str(DEFAULT_DIR),
                    help="sample folder to check (default: the divergence set)")
    args = ap.parse_args(argv)

    folder = Path(args.dir).resolve()
    samples = sorted(folder.glob("*.yaml"))
    if not samples:
        print(f"no samples found in {folder}", file=sys.stderr)
        return 2

    print(f"Checking {len(samples)} sample(s) in {folder.name} — cause claims vs the ballots\n")
    bad = 0
    for p in samples:
        problems = check_file(p)
        if problems:
            bad += 1
            print(f"  FAIL {p.name}")
            for prob in problems:
                print(f"       - {prob}")
    if bad:
        print(f"\n{bad} of {len(samples)} sample(s) make a cause claim the ballots "
              f"do not support.\nThese are not relabellings — check whether the sample "
              f"still demonstrates what it was built for.")
        return 1
    print(f"  OK — all {len(samples)} samples: cycle chains, Condorcet claims, score "
          f"ranks\n       and finalist pairs all match the ballots.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
