#!/usr/bin/env python3
"""
pr_alabama_paradox.py — does adding a seat ever REMOVE someone under STAR-PR?

WHY THIS EXISTS
---------------
The **Alabama paradox** is a failure of *house size monotonicity*: you enlarge
the body by one seat, recount, and somebody who had a seat no longer does. It is
named for the 1880 US census, where Alabama got 8 seats out of 299 and 7 out of
300.

Classical apportionment theory says exactly where to look. Pukelsheim's
**Coherence Theorem** (Proportional Representation, 2nd ed., ch. 9) proves that
an apportionment method is coherent — and therefore house size monotone — *if
and only if* it is a **divisor** method. **Quota** methods are neither. So the
prediction, before running anything, is:

    Allocated Score  quota   -> paradox possible
    SSS              quota   -> paradox possible
    RRV              divisor -> paradox IMPOSSIBLE

The repo asserted this trade in `03_STAR_PR/01_Learn/STAR_PR/README.md` and
flagged that nobody had checked whether it actually bites STAR-PR, since the
theorems are proved for one-shot party-list apportionment while these methods
are sequential and run on a ballot matrix. This script checks.

WHAT IT MEASURES
----------------
For each random electorate, tabulate at 2, 3, 4 and 5 seats and test whether the
winner set only ever *grows*:

    winners(k) subset-of winners(k+1)   for every k

A violation is an Alabama paradox: somebody seated at k is not seated at k+1.

Only **tie-free** elections count. Passing `tiebreaker=None` makes `starvote`
raise rather than guess, so nothing here is an artifact of a coin toss. (Note
Allocated Score refuses `seats=1` outright, which is why the sweep starts at 2.)

RESULT (seed 20260806, 1200 trials, 5-7 candidates, 25-60 ballots)
-------------------------------------------------------------------
    method       tie-free   paradox    rate
    allocated        1062       391   36.8%
    sss              1126       242   21.5%
    rrv              1142         0    0.0%

RRV's zero is not luck and not a sampling limit — it is the theorem. The two
quota methods fail, and Allocated Score, the recommended STAR-PR tabulation,
fails most often.

READ THE RATE WITH CARE — IT IS AN UPPER BOUND, NOT A FORECAST
---------------------------------------------------------------
Ballots here are independent uniform 0-5 scores. That is an impartial-culture-
style model, and impartial culture is *known* to manufacture far more
paradoxical profiles than real electorates produce — the point
`03_STAR_PR/01_Learn/simulating_pr.md` makes at length, and it applies to this
script as much as to anyone else's. Real voters are correlated; correlated
electorates have more structure and fewer pathologies.

So: **36.8% is not "one election in three".** It is "this is easy to construct
and not a curiosity", which is all a paradox rate from this model can honestly
support. Establishing a realistic frequency would need a clustered spatial
electorate, which this repo does not yet have.

USAGE
-----
    python3 pr_alabama_paradox.py
    python3 pr_alabama_paradox.py --trials 4000 --seed 7
    python3 pr_alabama_paradox.py --show      # print one worked counterexample
"""

from __future__ import annotations

import argparse
import random

import starvote

METHODS = {
    "allocated": (starvote.allocated, "quota"),
    "sss": (starvote.sss, "quota"),
    "rrv": (starvote.rrv, "divisor"),
}

# Allocated Score refuses a single-seat election, so the sweep starts at two.
SEAT_RANGE = (2, 3, 4, 5)


def winners(method, ballots, cast, seats):
    """Tie-free winner set, or None if the result would need a tiebreaker."""
    rows = [{c: s for c, s in zip(cast, b)} for b in ballots]
    try:
        return frozenset(
            starvote.election(
                method, rows, seats=seats, maximum_score=5, tiebreaker=None
            )
        )
    except Exception:
        return None


def sweep(method, ballots, cast):
    """Winner sets across SEAT_RANGE, or None if any of them ties."""
    out = {}
    for k in SEAT_RANGE:
        w = winners(method, ballots, cast, k)
        if w is None:
            return None
        out[k] = w
    return out


def first_violation(sets):
    """The first k where adding a seat drops somebody, else None."""
    for k in SEAT_RANGE[:-1]:
        if not sets[k] <= sets[k + 1]:
            return k
    return None


def random_election(rng):
    ncand = rng.randint(5, 7)
    nball = rng.randint(25, 60)
    cast = list("ABCDEFG")[:ncand]
    ballots = [[rng.randint(0, 5) for _ in range(ncand)] for _ in range(nball)]
    return cast, ballots


def main() -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("--trials", type=int, default=1200)
    ap.add_argument("--seed", type=int, default=20260806)
    ap.add_argument("--show", action="store_true",
                    help="print one worked counterexample per failing method")
    args = ap.parse_args()

    print(f"Alabama paradox under STAR-PR — {args.trials} random electorates, "
          f"seed {args.seed}")
    print("  5–7 candidates, 25–60 ballots, independent uniform 0–5 scores")
    print("  tie-free elections only (tiebreaker=None, so no coin tosses counted)\n")
    print(f"{'method':11} {'family':9} {'tie-free':>9} {'paradox':>8} {'rate':>7}")
    print("-" * 48)

    examples = {}
    for name, (method, family) in METHODS.items():
        rng = random.Random(args.seed)
        clean = hits = 0
        for _ in range(args.trials):
            cast, ballots = random_election(rng)
            sets = sweep(method, ballots, cast)
            if sets is None:
                continue
            clean += 1
            k = first_violation(sets)
            if k is not None:
                hits += 1
                examples.setdefault(name, (cast, ballots, k, sets[k], sets[k + 1]))
        rate = hits / clean if clean else 0.0
        print(f"{name:11} {family:9} {clean:>9} {hits:>8} {rate:>6.1%}")

    print("\nRRV's zero is the Coherence Theorem, not a sampling limit: divisor")
    print("methods are house size monotone, so the paradox is impossible for it.")
    print("The two quota methods fail, and Allocated Score — the recommended")
    print("STAR-PR tabulation — fails most often.")
    print("\nThe RATE is an upper bound, not a forecast. Independent uniform")
    print("ballots are an impartial-culture-style model, which is known to")
    print("manufacture more paradoxes than real electorates contain. Read it as")
    print("'easy to construct', not as 'one election in three'.")

    if args.show:
        for name, (cast, ballots, k, before, after) in examples.items():
            lost = sorted(before - after)
            print(f"\n--- {name}: seats {k} -> {k+1} drops {', '.join(lost)} ---")
            print(f"    cast    : {cast}")
            print(f"    {k} seats : {sorted(before)}")
            print(f"    {k+1} seats : {sorted(after)}")
            print(f"    ballots : {ballots}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
