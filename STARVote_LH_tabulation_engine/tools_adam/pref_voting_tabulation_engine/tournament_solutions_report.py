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

Works on RANKED ballots (where these rules genuinely apply) and on SCORE
ballots (STAR / Approval / Score), where it prints the tournament those ballots
imply and lets you ask whether the score method's winner is COVERED — see
00_start_here/topics/uncovered_set.md. A score method has no Fishburn class and
is not one of the rules below; the tool says so on every score file.

What it prints, for any election YAML in this repo:
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
    applied to a generalization. The tool says so when it happens, and prints all
    four published covering variants, which disagree exactly then.
  * a choice set with several names has **not failed**. Irresoluteness is the
    normal state of a tournament solution — narrowing to one winner always takes
    extra information or a lot.

Usage:
    uv run STARVote_LH_tabulation_engine/tools_adam/pref_voting_tabulation_engine/tournament_solutions_report.py FILE.yaml

Requires: pref_voting (declared in pyproject.toml; `uv sync`).
"""
import itertools
import os
import sys
from collections import Counter

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
from pref_voting_tabulation import (  # noqa: E402
    format_levels, parse_election, ranked_profile,
)

try:
    from pref_voting.profiles import Profile
    from pref_voting.weighted_majority_graphs import MajorityGraph
    from pref_voting.c1_methods import (
        banks, bipartisan, copeland, gocha, slater, top_cycle, uc_gill,
        uc_fish, uc_bordes, uc_mckelvey,
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


def build_graph_from_scores(cands, score_dicts):
    """The tournament implied by SCORE ballots: a > b iff more ballots score a above b.

    Score ballots are not a ranked profile — a rule like STAR is not a function of the
    ranked profile at all (topics/what_a_method_reads.md). But the pairwise *comparisons*
    are perfectly well defined (this is exactly the engine's For / Equal Support / Against
    matrix), so the covering relation and every solution below can still be asked about a
    STAR or Approval election. That is how we check whether a score method elected a
    COVERED candidate. Returns (MajorityGraph, ties).
    """
    edges, ties = [], []
    for a, b in itertools.combinations(range(len(cands)), 2):
        ca, cb = cands[a], cands[b]
        fa = sum(1 for s in score_dicts if s[ca] > s[cb])
        fb = sum(1 for s in score_dicts if s[cb] > s[ca])
        if fa > fb:
            edges.append((a, b))
        elif fb > fa:
            edges.append((b, a))
        else:
            ties.append((cands[a], cands[b]))
    return MajorityGraph(list(range(len(cands))), edges), ties


def _names(winners, cands):
    return "{" + ", ".join(cands[c] for c in sorted(winners)) + "}" if winners else "{}"


def report(path):
    cands, dicts, ranks, _priority, _has_ties, vm = parse_election(path)
    m = len(cands)
    out = []
    out.append("=== Tournament solutions — every C1 rule on one election ===")

    if ranks is not None:
        # ProfileWithTies, so a '=' level or a truncated ballot stays what the voter
        # cast. A drawn PAIR then shows up as margin 0 and is reported as a weak
        # tournament below, rather than being silently turned into a strict edge.
        prof, _keep = ranked_profile(cands, dicts)
        ties = [(cands[i], cands[j]) for i, j in itertools.combinations(range(m), 2)
                if prof.margin(i, j) == 0]
        graph = prof
        out.append(f" {len(ranks)} ranked ballots, {m} candidates.\n")
        out.append("Ballots:")
        for order, cnt in Counter(format_levels(o) for o in ranks).most_common():
            out.append(f"   {cnt:>3} x {order}")
    else:
        # SCORE ballots (STAR / Approval / Score). The rules below cannot CLASSIFY such a
        # method — its winner is not a function of the ranked profile — but the pairwise
        # comparisons are well defined, so we can still ask whether its winner is COVERED.
        graph, ties = build_graph_from_scores(cands, dicts)
        out.append(f" {len(dicts)} SCORE ballots, {m} candidates"
                   f"{f' (method: {vm})' if vm else ''}.\n")
        out.append("!! SCORE ballots. The tournament below is the one these ballots imply")
        out.append("   (a > b iff more ballots score a above b) — the engine's own")
        out.append("   For / Equal Support / Against matrix, read for direction only.")
        out.append("   A score method has NO Fishburn class and is not one of the rules")
        out.append("   below: its winner is not a function of this graph. What you CAN ask")
        out.append("   is whether its winner survives these filters — e.g. whether it")
        out.append("   elected a COVERED candidate. See topics/uncovered_set.md.")
        out.append("")
        out.append("Ballots (scores):")
        for s in dicts:
            out.append("   " + ", ".join(f"{c} {s[c]}" for c in cands))
    out.append("")

    # The tournament: direction only. This is the whole input for every rule below.
    dominion = {c: [] for c in cands}
    for i, a in enumerate(cands):
        for b in cands[i + 1:]:
            if (a, b) in ties or (b, a) in ties:
                continue
            if graph.majority_prefers(i, cands.index(b)):
                dominion[a].append(b)
            else:
                dominion[b].append(a)

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
        out.append(f"   {name:<{width}}  {_names(fn(graph), cands):<28} [{cost}]")
        out.append(f"   {'':<{width}}  {note}")
    out.append("")
    out.append("   Markov set (MA) — pref_voting has no implementation; see the chapter.")
    if ties:
        out.append("")
        out.append("The four published COVERING variants (they coincide only without ties):")
        for fn, nm in [(uc_gill, "Gillies"), (uc_fish, "Fishburn"),
                       (uc_bordes, "Bordes"), (uc_mckelvey, "McKelvey")]:
            out.append(f"   UC[{nm:<9}] = {_names(fn(graph), cands)}")
    out.append("")

    out.append("Axioms, as stated in the chapter (not inferred here):")
    out.append(f"   {'solution':<{width}}  {'monotonic':<10} {'stable':<24} composition-consistent")
    for name, _fn, _cost, _note in SOLUTIONS:
        if name in AXIOMS:
            mono, stab, comp = AXIOMS[name]
            out.append(f"   {name:<{width}}  {mono:<10} {stab:<24} {comp}")
    out.append("")

    # The point that matters for this repo.
    co = sorted(copeland(graph))
    if len(co) > 1:
        names = ", ".join(cands[c] for c in co)
        # Margins exist only on the ranked profile; the score path's MajorityGraph has
        # thrown them away (its .margin() raises), which is the point made just below.
        margins = ({cands[c]: sum(graph.margin(c, o) for o in range(len(cands)) if o != c)
                    for c in co} if ranks is not None else None)
        best = max(margins, key=margins.get) if margins else None
        out.append(f"The tournament does NOT decide this election: Copeland ties {{{names}}}.")
        if margins:
            out.append(f"LH's Ranked Robin breaks that tie by TOTAL MARGIN — "
                       f"{', '.join(f'{k} {v:+d}' for k, v in margins.items())} — electing {best}.")
        else:
            out.append("LH's Ranked Robin would break that tie by TOTAL MARGIN — which this")
            out.append("graph no longer holds. Run the LH engine on the file for the margins.")
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
