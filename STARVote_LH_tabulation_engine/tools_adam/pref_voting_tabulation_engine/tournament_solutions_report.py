#!/usr/bin/env python3
"""
tournament_solutions_report.py — the C1 tournament solutions, side by side.

A **tournament solution** is a rule that reads *only* the tournament: who beat
whom, direction only, margins thrown away. That is Fishburn's C1 tier (see
00_start_here/topics/what_a_method_reads.md), and the academic literature on it
is large — Brandt, Brill & Harrenstein, "Tournament Solutions," ch. 3 of the
*Handbook of Computational Social Choice* (2016).

The LH engine implements exactly one of them: **Copeland**, as Ranked Robin.
This tool prints the rest, from Eric Pacuit & Wesley Holliday's `pref_voting`,
so the teaching pages can state verified choice sets instead of asserted ones.

What it prints, for any ranked-ballot YAML in this repo:
  * the ballots, collapsed
  * the **tournament itself** — the adjacency matrix M(T), direction only,
    which is the object every rule below actually reads
  * the outdegrees (= Copeland scores)
  * each solution's **choice set**, coarsest first, with its complexity
  * whether the tournament alone decides the election, or whether LH's Ranked
    Robin had to reach outside C1 (to margins) to break a Copeland tie

Two honest caveats it prints for you:
  * a tournament requires **no pairwise ties**. Real ballots tie, and then the
    object is a *weak* tournament (chapter §3.5) and these functions are being
    applied to a generalization. The tool says so when it happens.
  * a choice set with several names has **not failed**. Irresoluteness is the
    normal state of a tournament solution — narrowing to one winner always takes
    extra information or a lot.

Usage:
    uv run STARVote_LH_tabulation_engine/tools_adam/pref_voting_tabulation_engine/tournament_solutions_report.py FILE.yaml

Requires: pref_voting (declared in pyproject.toml; `uv sync`).
"""
import os
import sys
from collections import Counter

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
from pref_voting_tabulation import parse_election  # noqa: E402

try:
    from pref_voting.profiles import Profile
    from pref_voting.c1_methods import (
        banks, bipartisan, copeland, gocha, slater, top_cycle, uc_gill,
    )
except ImportError:  # pragma: no cover - optional dependency
    print("tournament_solutions_report: pref_voting is not installed "
          "(pip install pref_voting, or `uv sync`).", file=sys.stderr)
    raise SystemExit(2)

# (label, function, complexity, note) — coarsest solution first, which is also
# the teaching order. Complexity claims are the chapter's theorems 3.2-3.7.
SOLUTIONS = [
    ("Top cycle (TC / Smith set)", top_cycle, "linear",
     "smallest set beating everyone outside it"),
    ("Schwartz set (GOCHA)", gocha, "linear",
     "the tighter cousin; differs from TC only under pairwise ties"),
    ("Uncovered set (UC)", uc_gill, "poly, O(m^2.38)",
     "reaches every rival in <=2 steps; the graph-theoretic KINGS"),
    ("Banks set (BA)", banks, "NP-complete",
     "tops of the maximal transitive subtournaments"),
    ("Bipartisan set (BP)", bipartisan, "poly (LP)",
     "support of the tournament game's unique Nash equilibrium"),
    ("Copeland set (CO)", copeland, "linear",
     "most head-to-head wins == Ranked Robin's own rule"),
    ("Slater set (SL)", slater, "NP-hard",
     "tops of the closest linear orders (min feedback arc set)"),
]

# Axioms, exactly as stated in the chapter's Section 3.3 — nothing inferred.
# (label, monotonic, stable, composition-consistent)
AXIOMS = {
    "Uncovered set (UC)": ("yes", "NO (not even idempotent)", "yes"),
    "Banks set (BA)": ("yes", "NO", "yes"),
    "Bipartisan set (BP)": ("yes", "yes", "yes"),
    "Copeland set (CO)": ("yes", "NO (not idempotent)", "NO (even weak fails)"),
    "Slater set (SL)": ("yes", "NO", "NO (weak version holds)"),
}


def build_profile(cands, ranks):
    idx = {c: i for i, c in enumerate(cands)}
    return Profile([[idx[c] for c in order] for order in ranks])


def _names(winners, cands):
    return "{" + ", ".join(cands[c] for c in sorted(winners)) + "}" if winners else "{}"


def report(path):
    cands, _dicts, ranks, _priority, _has_ties, _vm = parse_election(path)
    if ranks is None:
        raise SystemExit(
            f"{path}: not a ranked-ballot election. A tournament is built from pairwise "
            "comparisons of RANKED ballots; score ballots (STAR/Approval) are not a "
            "function of the ranked profile at all — see "
            "00_start_here/topics/what_a_method_reads.md.")

    prof = build_profile(cands, ranks)
    m = len(cands)
    out = []
    out.append("=== Tournament solutions — every C1 rule on one election ===")
    out.append(f" {len(ranks)} ranked ballots, {m} candidates.\n")

    out.append("Ballots:")
    for order, cnt in Counter(" > ".join(o) for o in ranks).most_common():
        out.append(f"   {cnt:>3} x {order}")
    out.append("")

    # The tournament: direction only. This is the whole input for every rule below.
    ties = []
    dominion = {c: [] for c in cands}
    for i, a in enumerate(cands):
        for b in cands[i + 1:]:
            mg = prof.margin(i, cands.index(b))
            if mg > 0:
                dominion[a].append(b)
            elif mg < 0:
                dominion[b].append(a)
            else:
                ties.append((a, b))

    out.append("The tournament M(T) — 1 means the row beats the column (margins DISCARDED):")
    w = max(max(len(c) for c in cands), 5)
    out.append("        " + " ".join(f"{c:>{w}}" for c in cands))
    for a in cands:
        row = [("-" if b == a else ("1" if b in dominion[a] else "0")) for b in cands]
        out.append(f"   {a:<5} " + " ".join(f"{v:>{w}}" for v in row))
    out.append("")
    out.append("Outdegree = Copeland score (how many rivals each one beats):")
    for c in sorted(cands, key=lambda c: -len(dominion[c])):
        beats = ", ".join(dominion[c]) or "nobody"
        out.append(f"   {c:<8} {len(dominion[c])}   beats {beats}")
    out.append("")

    if ties:
        out.append("!! PAIRWISE TIES PRESENT — " +
                   ", ".join(f"{a}={b}" for a, b in ties) + ".")
        out.append("   This is a WEAK tournament, not a tournament. The rules below are")
        out.append("   generalizations here, and the literature offers no single canonical")
        out.append("   extension (chapter Section 3.5). Read the sets with that caveat.")
        out.append("")

    cw = [c for c in cands if len(dominion[c]) == m - 1]
    out.append(f"Condorcet winner: {cw[0]} — every solution below returns exactly {{{cw[0]}}}."
               if cw else
               "Condorcet winner: NONE — majority preference cycles. This is where the "
               "solutions come apart.")
    out.append("")

    out.append("Choice sets (coarsest first):")
    width = max(len(s[0]) for s in SOLUTIONS)
    for name, fn, cost, note in SOLUTIONS:
        out.append(f"   {name:<{width}}  {_names(fn(prof), cands):<28} [{cost}]")
        out.append(f"   {'':<{width}}  {note}")
    out.append("")
    out.append("   Markov set (MA) — pref_voting has no implementation; see the chapter.")
    out.append("")

    out.append("Axioms, as stated in the chapter (not inferred here):")
    out.append(f"   {'solution':<{width}}  {'monotonic':<10} {'stable':<24} composition-consistent")
    for name, _fn, _cost, _note in SOLUTIONS:
        if name in AXIOMS:
            mono, stab, comp = AXIOMS[name]
            out.append(f"   {name:<{width}}  {mono:<10} {stab:<24} {comp}")
    out.append("")

    # The point that matters for this repo.
    co = sorted(copeland(prof))
    if len(co) > 1:
        names = ", ".join(cands[c] for c in co)
        margins = {cands[c]: sum(prof.margin(c, o) for o in prof.candidates if o != c)
                   for c in co}
        best = max(margins, key=margins.get)
        out.append(f"The tournament does NOT decide this election: Copeland ties {{{names}}}.")
        out.append(f"LH's Ranked Robin breaks that tie by TOTAL MARGIN — "
                   f"{', '.join(f'{k} {v:+d}' for k, v in margins.items())} — electing {best}.")
        out.append("Margins are not in the tournament. The moment Ranked Robin reaches for")
        out.append("them it has stepped out of C1 and is reading C2 information.")
    else:
        out.append(f"The tournament decides: Copeland returns the single winner "
                   f"{_names(co, cands)}, no tiebreak needed.")
    return "\n".join(out)


def main(argv):
    args = [a for a in argv[1:] if not a.startswith("--")]
    if not args:
        raise SystemExit("usage: tournament_solutions_report.py FILE.yaml [FILE.yaml ...]")
    for path in args:
        print(report(path))


if __name__ == "__main__":
    main(sys.argv)
