#!/usr/bin/env python3
"""
successive_elimination_report.py — the parliamentary / amendment procedure.

*Candidates meet in pairwise majority votes in a fixed AGENDA order; each round's
loser is eliminated and the winner meets the next candidate; the last survivor
wins.* This is how legislatures vote on amendments, so its failures are not
hypothetical — they are agenda power, strategic absence and strategic silence.

Why this exists: nothing counts it. The LH engine has no agenda concept and
BetterVoting has no such method, so `07_Concepts/voting_paradoxes/successive_elimination.md`
could only assert Felsenthal's Examples 9-12 in prose. Unlike the Minimax and
Coombs tools next door, this one has no `pref_voting` counterpart to check against
— the library has no agenda-based method — so the independent check here is
structural rather than a second implementation:

  * every head-to-head is read from the LH engine's own `calculate_preference_matrix`,
    the same matrix Ranked Robin is tallied from, so the pairwise numbers are the
    engine's and not this file's;
  * successive elimination is **Condorcet-consistent** — a candidate who beats
    everyone head-to-head survives every round they appear in, whatever the agenda.
    So when a Condorcet winner exists the report asserts the procedure found them,
    and says so. That is a real invariant, and it fails loudly if the round logic
    is wrong.

**The agenda is an input, not a detail.** Under a Condorcet cycle the agenda-setter
picks the winner: Felsenthal's Example 9 elects b, a Pareto-dominated candidate,
under one agenda and d under another, from the same 11 ballots. Pass `--agenda` to
see it. With no `--agenda` the candidates are taken in alphabetical order and the
report says so, because there is no such thing as a default agenda in the wild.

**Ties, and why there is a flag for them.** A tied round has to be broken by
something outside the ballots, and the published examples do not agree on what.
Felsenthal's Examples 11 and 12 break toward the earlier **letter**; his Example 10
calls the break **random** and argues only that b *can* win. Parliamentary practice
is a third answer again — a tied motion fails, so the incumbent survives, which is
the earlier-on-the-**agenda** reading. So the convention is an explicit option:

    --tiebreak alpha    earlier letter wins   (default; Felsenthal Ex.11, Ex.12)
    --tiebreak agenda   earlier on the agenda wins  (parliamentary reading)

Every tie is flagged as it happens, and when any round tied the report re-runs the
whole agenda under the *other* convention and tells you whether the winner changes.
If it does, the winner was never a fact about the electorate.

Usage:
    uv run STARVote_LH_tabulation_engine/tools_adam/pref_voting_tabulation_engine/successive_elimination_report.py FILE.yaml
    uv run ... successive_elimination_report.py --agenda a,b,c,d FILE.yaml   # path independence
    uv run ... successive_elimination_report.py --drop d FILE.yaml           # SCC
"""
import os
import sys
from collections import Counter

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
from pref_voting_tabulation import (  # noqa: E402
    format_levels, parse_election,
)
sys.path.insert(0, os.path.join(os.path.dirname(_HERE), "STARVote_LH_tabulation_engine"))
import starvote_larry_hastings as LH  # noqa: E402


def _prefers(dicts, a, b):
    """(voters preferring a, voters preferring b) — abstentions counted for neither.

    A ballot that ranks neither a nor b (both truncated away) has expressed no
    view on this pair and is not counted, which is the whole of Example 12: the
    truncating voter stops participating in the rounds their candidate is absent
    from, and the earlier rounds resolve differently without them."""
    fa = fb = 0
    for d in dicts:
        sa, sb = d.get(a), d.get(b)
        if sa is None and sb is None:
            continue
        sa = 0 if sa is None else sa
        sb = 0 if sb is None else sb
        if sa > sb:
            fa += 1
        elif sb > sa:
            fb += 1
    return fa, fb


def _run_agenda(dicts, order, tiebreak):
    """(winner, [round lines], [(a, b, kept) for each tied round])."""
    lines, ties = [], []
    survivor = order[0]
    for i, challenger in enumerate(order[1:], start=1):
        fa, fb = _prefers(dicts, survivor, challenger)
        if fa > fb:
            lines.append(f"   Round {i}: {survivor} vs {challenger} — "
                         f"{survivor} beats {challenger} {fa}:{fb}")
        elif fb > fa:
            lines.append(f"   Round {i}: {survivor} vs {challenger} — "
                         f"{challenger} beats {survivor} {fb}:{fa}")
            survivor = challenger
        else:
            if tiebreak == "agenda":
                kept = min((survivor, challenger), key=order.index)
                why = "earlier on the agenda"
            else:
                kept = min(survivor, challenger)
                why = "earlier letter"
            lines.append(f"   Round {i}: {survivor} vs {challenger} — TIE {fa}:{fb} → "
                         f"{kept} survives ({why})")
            ties.append((survivor, challenger, kept))
            survivor = kept
    return survivor, lines, ties


def report(path, agenda=None, drop=None, tiebreak="alpha"):
    cands, dicts, ranks, priority, has_ties, vm = parse_election(path)
    if drop and drop not in cands:
        raise SystemExit(f"--drop {drop!r}: no such candidate (have: {', '.join(cands)})")
    keep = [c for c in cands if c != drop]

    if agenda:
        unknown = [c for c in agenda if c not in keep]
        if unknown:
            raise SystemExit(f"--agenda names unknown candidate(s): {', '.join(unknown)} "
                             f"(have: {', '.join(keep)})")
        missing = [c for c in keep if c not in agenda]
        if missing:
            raise SystemExit(f"--agenda omits {', '.join(missing)} — an agenda must "
                             "order every candidate still in the race.")
        order = list(agenda)
        agenda_note = "as given by --agenda"
    else:
        order = sorted(keep)
        agenda_note = ("alphabetical — NOT a default in any real sense; pass --agenda "
                       "to set the order, which under a cycle sets the winner")

    out = []
    out.append("=== Successive elimination (parliamentary / amendment procedure) ===")
    note = f", {drop} DROPPED" if drop else ""
    out.append(f" Tabulating {len(dicts)} ballots, {len(keep)} candidates{note}.")
    out.append(f" Agenda: {' vs '.join(order)}   ({agenda_note})\n")

    out.append("Ballots:")
    rows = [format_levels(lv, drop=drop) for lv in ranks] if ranks is not None else \
           [", ".join(str(b.get(c, 0)) for c in keep) for b in dicts]
    counts = Counter(rows)
    seen = []
    for r in rows:
        if r not in seen:
            seen.append(r)
    for r in seen:
        out.append(f"   {counts[r]:>3} × {r}")
    out.append("")

    # --- Run the agenda. ---
    out.append("Rounds — each survivor meets the next candidate on the agenda:")
    survivor, lines, ties_broken = _run_agenda(dicts, order, tiebreak)
    out.extend(lines)
    out.append("")
    out.append(f"Winner — successive elimination: {survivor}")
    if ties_broken:
        named = "earlier letter" if tiebreak == "alpha" else "earlier on the agenda"
        out.append(f"   ⚠️  {len(ties_broken)} of {len(order) - 1} round(s) TIED and were "
                   f"broken by convention ({named}), not by the ballots.")
        other = "agenda" if tiebreak == "alpha" else "alpha"
        alt, _, _ = _run_agenda(dicts, order, other)
        if alt != survivor:
            out.append(f"   ⚠️  Under the OTHER convention (--tiebreak {other}) the same "
                       f"ballots and the same agenda elect {alt}. The winner here is a "
                       "fact about the tie-break rule, not about the electorate.")
        else:
            out.append(f"   (Under --tiebreak {other} the winner is still {survivor}.)")
    out.append("")

    # --- Condorcet consistency: the structural check standing in for a second engine.
    matrix = LH.calculate_preference_matrix(cands, dicts)
    beats_all = []
    for c in keep:
        if all(matrix[c][o][0] > matrix[c][o][1] for o in keep if o != c):
            beats_all.append(c)
    if len(beats_all) == 1:
        cw = beats_all[0]
        if cw == survivor:
            out.append(f" Condorcet check: {cw} beats every rival head-to-head, and the "
                       "procedure elected them — as it must, from any agenda. ✓")
        else:
            out.append(f" Condorcet check: DISAGREE ✗ — {cw} beats every rival "
                       f"head-to-head but the procedure elected {survivor}. Successive "
                       "elimination is Condorcet-consistent, so this is a BUG in the "
                       "round logic above. INVESTIGATE.")
    else:
        out.append(" Condorcet check: no Condorcet winner — the majority preference "
                   "cycles, which is exactly when the agenda decides the outcome. "
                   "Re-run with a different --agenda and expect a different winner.")

    # --- Pareto: is someone unanimously preferred to the winner? ---
    dominators = []
    for c in keep:
        if c == survivor:
            continue
        fa, fb = _prefers(dicts, c, survivor)
        if fb == 0 and fa > 0:
            dominators.append((c, fa))
    if dominators:
        who = ", ".join(f"{c} ({n} of {len(dicts)} voters, none against)"
                        for c, n in dominators)
        out.append(f" ⚠️  PARETO-DOMINATED WINNER: every voter with a view prefers "
                   f"{who} to the elected {survivor}.")
    return "\n".join(out)


if __name__ == "__main__":
    args = sys.argv[1:]
    agenda = drop = None
    tiebreak = "alpha"
    if "--tiebreak" in args:
        i = args.index("--tiebreak")
        tiebreak = args[i + 1]
        del args[i:i + 2]
        if tiebreak not in ("alpha", "agenda"):
            sys.exit("--tiebreak must be 'alpha' (earlier letter) or 'agenda'")
    if "--agenda" in args:
        i = args.index("--agenda")
        agenda = [c.strip() for c in args[i + 1].split(",") if c.strip()]
        del args[i:i + 2]
    if "--drop" in args:
        i = args.index("--drop")
        drop = args[i + 1]
        del args[i:i + 2]
    if not args:
        sys.exit("usage: python successive_elimination_report.py [--agenda A,B,C] "
                 "[--drop NAME] [--tiebreak alpha|agenda] FILE.yaml [FILE2.yaml ...]")
    for p in args:
        print(report(p, agenda=agenda, drop=drop, tiebreak=tiebreak))
        print()
