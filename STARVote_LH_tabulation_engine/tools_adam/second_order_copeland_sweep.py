#!/usr/bin/env python3
"""
second_order_copeland_sweep.py — can a second Copeland round break a Copeland tie?
=================================================================================
Ranked Robin's published ladder breaks a Copeland tie with **margins** (1st
Degree, then 2nd Degree, then a lot). The obvious-looking alternative is to run
Copeland *again* on the tied set — score each candidate by the Copeland scores of
the opponents they defeated. That is a real published rule, **second-order
Copeland**, and it has a genuine selling point: it makes manipulation NP-hard.

This script asks whether it would actually resolve anything, by exhaustive
enumeration rather than sampling. For each field size it walks **every** weak
tournament — every way the pairwise matchups can come out, win / draw / loss on
each of the `C(n,2)` pairs — keeps the ones where the top Copeland score is
shared, and asks whether second-order Copeland leaves exactly one candidate on
top.

**The answer at three candidates is never.** Not "rarely": 0 of 6, every
possible three-candidate Copeland tie, under both published readings of the
second-order score. The reason is small enough to check by hand — with three
candidates, two contenders tied on Copeland have beaten the same *number* of
opponents, and the only opponent outside the tie is the single third candidate,
so their defeated sets carry identical total score. The rule only starts biting
once the field is wide enough for the tied candidates to have beaten *different*
people, and by then a Condorcet winner usually exists anyway.

That is why the ladder reads margins. Ties concentrate in small fields, and in
small fields a second Copeland round is provably silent.

**Why enumerate tournaments instead of ballots.** By McGarvey's theorem every
complete pairwise pattern is produced by some electorate, so enumerating the
patterns loses nothing (see 07_Concepts/topics/tournament_solutions.md). Patterns
containing a draw need an even electorate, and all six three-candidate ties below
are realizable — two of them are already runnable cases in this repo
(rr_degrees_three_way_cycle.yaml, rr_degrees_what_counts_as_a_win.yaml).

Both readings of the second-order score are computed, because the literature
carries both and this repo's house rule is to say which convention a number came
from:
  * **defeated**       — sum of the Copeland scores of the opponents you beat.
  * **defeated−lost**  — that, minus the Copeland scores of those who beat you.

Usage:
    python second_order_copeland_sweep.py            # n = 3, 4, 5
    python second_order_copeland_sweep.py --max-n 6  # slow: 3^15 tournaments
    python second_order_copeland_sweep.py --show 3   # list every tie at n = 3
"""

import argparse
import itertools

WIN, DRAW, LOSS = 1.0, 0.5, 0.0
NAMES = "ABCDEFGH"


def tournaments(n):
    """Yield every weak tournament on n candidates as a matrix M[i][j]."""
    pairs = list(itertools.combinations(range(n), 2))
    for assignment in itertools.product((WIN, DRAW, LOSS), repeat=len(pairs)):
        M = [[None] * n for _ in range(n)]
        for (i, j), v in zip(pairs, assignment):
            M[i][j], M[j][i] = v, 1.0 - v
        yield M


def copeland(M, n):
    """First-order Copeland score: wins + 1/2 * draws."""
    return [sum(M[i][j] for j in range(n) if j != i) for i in range(n)]


def second_order(M, c, n):
    """Both published readings of the second-order Copeland score."""
    beat = [sum(c[j] for j in range(n) if j != i and M[i][j] == WIN) for i in range(n)]
    lost = [sum(c[j] for j in range(n) if j != i and M[i][j] == LOSS) for i in range(n)]
    return beat, [beat[i] - lost[i] for i in range(n)]


def leaders(scores, pool=None):
    pool = range(len(scores)) if pool is None else pool
    best = max(scores[i] for i in pool)
    return [i for i in pool if scores[i] == best]


def describe(M, n):
    parts = []
    for i, j in itertools.combinations(range(n), 2):
        v = M[i][j]
        parts.append(f"{NAMES[i]}>{NAMES[j]}" if v == WIN
                     else f"{NAMES[i]}={NAMES[j]}" if v == DRAW
                     else f"{NAMES[j]}>{NAMES[i]}")
    return "  ".join(parts)


def sweep(n, show=False):
    total = tied = resolved_beat = resolved_net = 0
    rows = []
    for M in tournaments(n):
        total += 1
        c = copeland(M, n)
        lead = leaders(c)
        if len(lead) < 2:
            continue
        tied += 1
        beat, net = second_order(M, c, n)
        r_beat = len(leaders(beat, lead)) == 1
        r_net = len(leaders(net, lead)) == 1
        resolved_beat += r_beat
        resolved_net += r_net
        if show:
            rows.append((describe(M, n), lead, c, beat, net, r_beat, r_net))
    return total, tied, resolved_beat, resolved_net, rows


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[1])
    ap.add_argument("--max-n", type=int, default=5, help="largest field size (default 5)")
    ap.add_argument("--show", type=int, metavar="N", help="list every tied tournament at N candidates")
    args = ap.parse_args()

    print("Does a second Copeland round break a Copeland tie?")
    print("Exhaustive over every weak tournament (win / draw / loss on each pair).\n")
    header = f"{'n':>2}  {'tournaments':>12}  {'Copeland ties':>14}  {'resolved (defeated)':>21}  {'resolved (defeated-lost)':>25}"
    print(header)
    print("-" * len(header))
    for n in range(3, args.max_n + 1):
        total, tied, r_beat, r_net, _ = sweep(n)
        pct = lambda r: f"{r:>7} ({100 * r / tied:5.1f}%)" if tied else "      —"
        print(f"{n:>2}  {total:>12,}  {tied:>14,}  {pct(r_beat):>21}  {pct(r_net):>25}")

    if args.show:
        n = args.show
        _, _, _, _, rows = sweep(n, show=True)
        print(f"\nEvery Copeland tie at n = {n}:\n")
        for desc, lead, c, beat, net, r_beat, r_net in rows:
            fmt = lambda v: "{" + ", ".join(f"{NAMES[i]}:{v[i]:g}" for i in lead) + "}"
            print(f"  {desc:<24}  Copeland {fmt(c):<22} "
                  f"2nd-order {fmt(beat):<20} net {fmt(net):<20} "
                  f"{'RESOLVED' if (r_beat or r_net) else 'still tied'}")

    print("\nAt three candidates a second Copeland round is silent on every possible tie —")
    print("which is why Ranked Robin's ladder breaks ties on margins instead.")
    print("→ 05_Ranked_Robin/03_Criteria/rr_tiebreaks/degrees_of_ties.md")


if __name__ == "__main__":
    main()
