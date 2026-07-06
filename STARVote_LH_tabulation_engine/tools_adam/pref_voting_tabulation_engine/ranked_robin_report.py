#!/usr/bin/env python3
"""
ranked_robin_report.py — an INDEPENDENT Ranked Robin (RCV-RR / Copeland) check.

Why this exists: `starvote_larry_hastings.py` now has a **native** Ranked Robin
tabulator (`run_ranked_robin()`, dispatched by `voting_method: RankedRobin`) —
it prints the round-robin report and writes the `_tabulated` mirror. This tool is
the **third opinion** used to guard against that native code misbehaving: it
prints the Ranked Robin view (ballots, full pairwise table, win–loss record,
winner) and — critically — cross-checks the winner against Eric Pacuit's
`pref_voting` library, whose Copeland is computed **independently** from a fresh
`Profile` built off the raw ballots (it does NOT reuse LH's matrix), so a bug in
the shared helper can't hide.

So a Ranked Robin case can be tallied three ways that must agree:
  1. LH native  — starvote_larry_hastings.run_ranked_robin()
  2. BetterVoting — RankedRobin.ts (the frozen _bv_export.json Results)
  3. pref_voting — the independent Copeland cross-check printed below

(The round-robin table here still uses LH's `calculate_preference_matrix` for
display; the load-bearing independent verdict is the `pref_voting` line.)
`pref_voting` is declared in pyproject.toml; install with `uv sync`.

Usage:
    uv run STARVote_LH_tabulation_engine/tools_adam/pref_voting_tabulation_engine/ranked_robin_report.py FILE.yaml
"""
import os
import sys
from collections import Counter

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
# parse_election (handles nested/flat YAML, ranked + score) needs no pref_voting.
from pref_voting_tabulation import parse_election  # noqa: E402
sys.path.insert(0, os.path.join(os.path.dirname(_HERE), "STARVote_LH_tabulation_engine"))
import starvote_larry_hastings as LH  # noqa: E402


def _ballot_lines(cands, dicts, ranks):
    """Collapse ballots to 'count × A > B > C' (ranked) or 'count × 5,3,0' (score)."""
    rows = []
    if ranks is not None:
        for order in ranks:
            rows.append(" > ".join(order))
    else:
        for b in dicts:
            rows.append(", ".join(str(b.get(c, 0)) for c in cands))
    counts = Counter(rows)
    # preserve first-seen order
    seen = []
    for r in rows:
        if r not in seen:
            seen.append(r)
    return [(counts[r], r) for r in seen]


def report(path):
    cands, dicts, ranks, priority, has_ties, vm = parse_election(path)
    n = len(dicts)
    matrix = LH.calculate_preference_matrix(cands, dicts)

    out = []
    out.append("=== Ranked Robin (RCV-RR / Copeland) — single winner ===")
    kind = "ranked" if ranks is not None else "score"
    out.append(f" Tabulating {n} {kind} ballots, {len(cands)} candidates.\n")

    out.append("Ballots:")
    for cnt, r in _ballot_lines(cands, dicts, ranks):
        out.append(f"   {cnt:>3} × {r}")
    out.append("")

    # Each unordered pair, head-to-head.
    out.append('Round-robin — every pair, head-to-head (votes For – Against):')
    wins = {c: [] for c in cands}
    losses = {c: [] for c in cands}
    ties = {c: [] for c in cands}
    margin = {c: 0 for c in cands}
    for i, a in enumerate(cands):
        for b in cands[i + 1:]:
            fa, aa, _ = matrix[a][b]      # a-For, a-Against
            margin[a] += fa - aa
            margin[b] += aa - fa
            if fa > aa:
                wins[a].append(b); losses[b].append(a)
                out.append(f"   {a} beats {b}   {fa} – {aa}")
            elif aa > fa:
                wins[b].append(a); losses[a].append(b)
                out.append(f"   {b} beats {a}   {aa} – {fa}")
            else:
                ties[a].append(b); ties[b].append(a)
                out.append(f"   {a} ties {b}    {fa} – {aa}")
    out.append("")

    # Win–loss record; Ranked Robin = most wins, then highest total margin.
    out.append("Win–loss record (most head-to-head wins wins; ties broken by total margin):")
    ranked = sorted(cands, key=lambda c: (-len(wins[c]), -margin[c],
                                          priority.index(c) if c in priority else 1e9))
    for c in ranked:
        w, l, t = len(wins[c]), len(losses[c]), len(ties[c])
        rec = f"{w}–{l}" + (f"–{t}t" if t else "")
        beat = f"   (beats: {', '.join(wins[c])})" if wins[c] else ""
        out.append(f"   {c:<8} {rec:<6} margin {margin[c]:+d}{beat}")
    out.append("")

    # Winner + why.
    top_wins = len(wins[ranked[0]])
    leaders = [c for c in cands if len(wins[c]) == top_wins]
    winner = ranked[0]
    if len(leaders) == 1:
        if len(losses[winner]) == 0:
            why = "beats every opponent head-to-head — the Condorcet winner."
        else:
            why = f"the most head-to-head wins ({top_wins})."
        out.append(f"Winner — Ranked Robin: {winner}\n   {why}")
    else:
        out.append(f"Winner — Ranked Robin: {winner}")
        out.append(f"   ⚠️  {len(leaders)} candidates tie on wins ({', '.join(leaders)}) — "
                   "a cycle. Broken by total margin, then lot order. "
                   "(This is where Minimax / Ranked Pairs / Schulze differ — see "
                   "cycle_resolution.md.)")

    # --- Independent third opinion: pref_voting's Copeland (see module docstring).
    # Loud, not silent: if the library is missing we SAY so, so a skipped check is
    # never mistaken for a passed one.
    out.append("")
    try:
        from pref_voting.profiles import Profile
        from pref_voting.c1_methods import copeland
    except Exception:
        out.append(" [pref_voting cross-check SKIPPED — library not installed. "
                   "Run `uv sync` (pref_voting is declared in pyproject.toml).]")
        return "\n".join(out)

    if ranks is None:
        out.append(" [pref_voting cross-check SKIPPED — score ballots; the "
                   "independent Copeland check runs on ranked ballots.]")
        return "\n".join(out)

    I = {c: i for i, c in enumerate(cands)}
    try:
        prof = Profile([[I[c] for c in o] for o in ranks])
        pv_winners = sorted(cands[x] for x in copeland(prof))
    except Exception as ex:
        out.append(f" [pref_voting cross-check ERROR: {ex!r}]")
        return "\n".join(out)

    # pref_voting's copeland returns the Copeland-leader SET (no margin/lot tiebreak).
    # A unique match is a clean agreement; if it returns several and LH's winner is
    # among them, LH merely tie-broke within that set — still consistent.
    if len(pv_winners) == 1 and pv_winners[0] == winner:
        verdict = "AGREE ✓  (unique Copeland winner)"
    elif winner in pv_winners:
        verdict = (f"CONSISTENT ✓  (LH tie-broke within pref_voting's "
                   f"{len(pv_winners)}-way Copeland-leader set)")
    else:
        verdict = "DISAGREE ✗  — INVESTIGATE"
    out.append(f" pref_voting Copeland leader(s): {', '.join(pv_winners)}")
    out.append(f" cross-check vs Ranked Robin winner ({winner}): {verdict}")
    return "\n".join(out)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("usage: python ranked_robin_report.py FILE.yaml [FILE2.yaml ...]")
    for p in sys.argv[1:]:
        print(report(p))
        print()
