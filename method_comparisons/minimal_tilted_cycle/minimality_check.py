#!/usr/bin/env python3
"""
minimality_check.py — brute-force confirmation of the folder README's proof.

Claim (README, "Why 5 voters, and why 3–1–1"):
  * n = 3 → the only Condorcet cycle on 3 candidates is the SYMMETRIC one,
            margins (1, 1, 1);
  * n = 4 → NO cycle exists at all;
  * n = 5 → cycles exist with exactly two margin shapes, (1, 1, 1) and (3, 1, 1)
            — so (3, 1, 1), i.e. 4–1 / 3–2 / 3–2, is the unique minimal
            *tilted* cycle.

The README proves this by a parity/sum argument. This script confirms it the
dumb way: enumerate every multiset of strict rankings over 3 candidates for
n = 1..6 voters, keep the profiles whose pairwise majorities cycle, and report
the distinct margin shapes found. Pure standard library — no engine, no
pref_voting — so it is an independent witness.

Usage:
    python3 minimality_check.py
"""
from itertools import combinations_with_replacement, permutations

CANDS = "ABC"
ORDERS = list(permutations(CANDS))          # the 6 strict rankings
ARCS = [("A", "B"), ("B", "C"), ("C", "A")]  # the cycle A→B→C→A and its reverse


def margin(profile, x, y):
    """Votes for x over y, minus votes for y over x."""
    m = 0
    for order in profile:
        m += 1 if order.index(x) < order.index(y) else -1
    return m


def cycle_shape(profile):
    """Return the sorted margin shape if the profile cycles, else None."""
    for arcs in (ARCS, [(y, x) for x, y in ARCS]):   # both cyclic directions
        margins = [margin(profile, x, y) for x, y in arcs]
        if all(m > 0 for m in margins):
            return tuple(sorted(margins, reverse=True))
    return None


def main():
    print("n   cycles found   distinct margin shapes (largest first)")
    print("--  ------------   ---------------------------------------")
    for n in range(1, 9):
        shapes, count = set(), 0
        for profile in combinations_with_replacement(ORDERS, n):
            shape = cycle_shape(profile)
            if shape:
                count += 1
                shapes.add(shape)
        pretty = ", ".join(str(s) for s in sorted(shapes, reverse=True)) or "—"
        print(f"{n:<3} {count:<14} {pretty}")
    print()
    print("Read the table: the first n with any cycle at all is 3, and at n = 3")
    print("the only shape is (1, 1, 1) — symmetric. n = 4 has none. n = 5 is the")
    print("first n admitting an asymmetric shape, and (3, 1, 1) is its only one.")


if __name__ == "__main__":
    main()
