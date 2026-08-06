#!/usr/bin/env python3
"""
contingent_vote_report.py — tabulate the CONTINGENT VOTE and the SUPPLEMENTARY VOTE.

Why this exists: neither engine in this repo counts these. `starvote_larry_hastings.py`
does STAR / Approval / Ranked Robin / SNTV and dispatches ranked ballots to the vendored
pyrankvote, which counts **Hare** — eliminate one candidate at a time. The contingent
vote eliminates *everyone below the top two in a single batch*, which is a different
count and can pick a different winner on the same ballots. Concept page:
`06_Other/RCV_IRV/concepts/variants/RCV-IRV-contingent-supplementary.md`.

  * **Contingent Vote** — tally first choices; if nobody has a majority, keep only the
    top two and transfer every other ballot to whichever finalist it ranks higher.
  * **Supplementary Vote** — the same count with the BALLOT capped at two choices
    (`--ranks 2`). A ballot naming neither finalist in its two marks exhausts. This is
    the form used for the Mayor of London and English PCCs until the Elections Act 2022.

The report prints the count, then the three comparisons that make it mean something —
full Hare IRV, the Condorcet winner, and plain Plurality — all computed independently by
Eric Pacuit's `pref_voting`, plus a cross-check of our contingent winner against
`pref_voting`'s own `plurality_with_runoff_put`. Same three-ways-must-agree discipline as
`ranked_robin_report.py`.

`pref_voting` is declared in pyproject.toml; install with `uv sync`.

Usage:
    uv run STARVote_LH_tabulation_engine/tools_adam/pref_voting_tabulation_engine/contingent_vote_report.py FILE.yaml
    uv run ... contingent_vote_report.py --ranks 2 FILE.yaml     # Supplementary Vote
"""
import os
import sys
from collections import Counter

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
from pref_voting_tabulation import (  # noqa: E402
    format_levels, parse_election, ranked_profile,
)


def _truncate(levels, cap):
    """Keep only a voter's top `cap` rank LEVELS — the Supplementary Vote's ballot cap.

    Capping levels (not names) is the honest reading of a two-column ballot: an `A=B`
    first mark is one choice-level, not two. `cap=None` leaves the ballot whole, which
    is the Contingent Vote."""
    return levels if cap is None else levels[:cap]


def _first_choices(voters, cands):
    """Plurality tally of the top level. A voter whose top level ties k candidates
    contributes 1/k to each — the same fractional convention the rest of the repo uses
    for an equal-rank pair, rather than silently dropping the ballot."""
    tally = {c: 0.0 for c in cands}
    for levels in voters:
        if not levels:
            continue
        top = levels[0]
        for c in top:
            tally[c] += 1.0 / len(top)
    return tally


def _prefers(levels, a, b):
    """Which of {a, b} does this ballot rank higher? Returns a, b, or None.

    A ballot that names only one of the pair prefers the one it named — a ranked
    candidate beats an unranked one. Naming neither (or both at the same level) is no
    preference, which for the contingent vote means the ballot EXHAUSTS."""
    pos = {}
    for i, lvl in enumerate(levels):
        for c in lvl:
            pos.setdefault(c, i)
    ia, ib = pos.get(a), pos.get(b)
    if ia is None and ib is None:
        return None
    if ib is None:
        return a
    if ia is None:
        return b
    if ia == ib:
        return None
    return a if ia < ib else b


def report(path, cap=None):
    cands, dicts, ranks, priority, _has_ties, _vm = parse_election(path)
    if ranks is None:
        return (f"=== {os.path.basename(path)} ===\n"
                " [SKIPPED — score ballots. The contingent vote is a ranked count; "
                "give it a ranked YAML (A>B>C).]")

    voters = [_truncate(lv, cap) for lv in ranks]
    n = len(voters)
    name = "Supplementary Vote" if cap == 2 else (
        "Contingent Vote" if cap is None else f"Contingent Vote (ballot capped at {cap})")

    out = [f"=== {name} — single winner ===",
           f" Source: {path}",
           f" Tabulating {n} ranked ballots, {len(cands)} candidates."]
    if cap is not None:
        out.append(f" Ballot cap: voters may mark {cap} choices; "
                   "marks beyond that are not on the ballot.")
    out.append("")

    out.append("Ballots (as counted):")
    rows = [format_levels(lv) or "(blank)" for lv in voters]
    counts = Counter(rows)
    for r in dict.fromkeys(rows):
        out.append(f"   {counts[r]:>4} × {r}")
    out.append("")

    # --- Round 1 ------------------------------------------------------------
    fc = _first_choices(voters, cands)
    order = sorted(cands, key=lambda c: (-fc[c], priority.index(c)
                                         if c in priority else 1e9))
    out.append("Round 1 — first choices:")
    for c in order:
        out.append(f"   {c:<10} {fc[c]:>8g}   ({fc[c] / n * 100:5.1f}%)")
    out.append("")

    majority = n / 2.0
    if fc[order[0]] > majority:
        out.append(f"Winner — {name}: {order[0]}")
        out.append(f"   Outright majority of first choices "
                   f"({fc[order[0]]:g} of {n}). No runoff is held.")
        winner, finalists = order[0], None
    else:
        a, b = order[0], order[1]
        finalists = (a, b)
        out.append(f"No majority ({fc[order[0]]:g} of {n}, majority needs more than "
                   f"{majority:g}).")
        out.append(f"   Top two advance: {a} and {b}. "
                   f"{', '.join(order[2:])} eliminated — all at once, in one step.")
        out.append("")

        tot = {a: 0.0, b: 0.0}
        exhausted = 0.0
        for levels in voters:
            p = _prefers(levels, a, b)
            if p is None:
                exhausted += 1
            else:
                tot[p] += 1
        counted = tot[a] + tot[b]
        out.append("Instant runoff — every ballot to whichever finalist it ranks higher:")
        for c in (a, b) if tot[a] >= tot[b] else (b, a):
            share = (tot[c] / counted * 100) if counted else 0.0
            out.append(f"   {c:<10} {tot[c]:>8g}   ({share:5.1f}% of ballots still "
                       f"counting, {tot[c] / n * 100:5.1f}% of ballots cast)")
        out.append(f"   {'exhausted':<10} {exhausted:>8g}   "
                   f"(ranked neither finalist — {exhausted / n * 100:5.1f}% of "
                   "ballots cast)")
        out.append("")
        out.append("   Runoff math:")
        out.append(f"     {n:>6g}  ballots cast")
        out.append(f"   − {exhausted:>6g}  exhausted (ranked neither finalist)")
        out.append("     ──────")
        out.append(f"     {counted:>6g}  ballots still counting  "
                   f"(majority of these = {int(counted // 2) + 1})")
        out.append("")
        winner = a if tot[a] > tot[b] else (b if tot[b] > tot[a] else None)
        if winner is None:
            out.append(f"Winner — {name}: TIED ({a} and {b} both {tot[a]:g}).")
        else:
            out.append(f"Winner — {name}: {winner}")
            if tot[winner] > majority:
                out.append(f"   {tot[winner]:g} of {n} ballots cast — an outright "
                           "majority of everyone who voted.")
            else:
                out.append(f"   {tot[winner]:g} of {n} ballots cast "
                           f"({tot[winner] / n * 100:.1f}%) — a majority of the ballots "
                           "still counting, but NOT of the ballots cast.")

    # --- The comparisons that make it mean something ------------------------
    out.append("")
    try:
        from pref_voting.c1_methods import copeland
        from pref_voting.iterative_methods import (
            instant_runoff_for_truncated_linear_orders as pv_irv,
            plurality_with_runoff_put,
        )
        from pref_voting.profiles import Profile
        from pref_voting.profiles_with_ties import ProfileWithTies
    except Exception:
        out.append(" [pref_voting comparisons SKIPPED — library not installed. "
                   "Run `uv sync` (pref_voting is declared in pyproject.toml).]")
        return "\n".join(out)

    # Build profiles from the SAME (possibly capped) ballots, so every method below is
    # answering the question about the ballots this count actually saw. TWO shapes are
    # needed, because the two questions differ on what an UNRANKED candidate means:
    #
    #   * Pairwise (Copeland/Condorcet) — unranked candidates sit tied at the BOTTOM,
    #     so a ranked candidate beats an unranked one and two unranked are no
    #     preference. That is the rule LH, BetterVoting and `ranked_profile` all apply.
    #   * Instant runoff — unranked candidates are simply ABSENT; the ballot exhausts
    #     when its ranked candidates are gone. pref_voting's truncated-orders IRV
    #     rejects a tied bottom level outright (it reads as an overvote).
    #
    # Feeding one profile to both would either break IRV or invent preferences nobody
    # cast, so they are built separately.
    tdicts = [{c: len(lv) - i for i, lvl in enumerate(lv) for c in lvl}
              for lv in voters]
    try:
        cope_prof, keep = ranked_profile(cands, tdicts)
        cope_w = sorted(keep[x] for x in copeland(cope_prof))
    except Exception as ex:
        out.append(f" [pref_voting Copeland comparison ERROR: {ex!r}]")
        return "\n".join(out)
    try:
        idx = {c: i for i, c in enumerate(cands)}
        rmaps = [{idx[c]: i for i, lvl in enumerate(lv) for c in lvl} for lv in voters]
        irv_prof = ProfileWithTies(rmaps, candidates=list(range(len(cands))))
        irv_w = sorted(cands[x] for x in pv_irv(irv_prof))
    except Exception as ex:
        irv_w = None
        irv_note = f"[ERROR: {ex!r}]"

    plur = [c for c in cands if fc[c] == max(fc.values())]
    out.append("Same ballots, other counts (all computed independently by pref_voting):")
    out.append(f"   Plurality (choose-one)        : {', '.join(sorted(plur))}")
    out.append(f"   {name:<30}: {winner or 'tied'}")
    out.append(f"   RCV-IRV (Hare, full rounds)   : "
               f"{', '.join(irv_w) if irv_w else irv_note}")
    out.append(f"   Ranked Robin (Copeland)       : {', '.join(cope_w)}")

    # Is there a Condorcet winner, and did this count find it?
    cw = None
    if len(cope_w) == 1:
        c = cope_w[0]
        beats_all = all(_beats(voters, c, o) for o in cands if o != c)
        cw = c if beats_all else None
    if cw:
        out.append("")
        verdict = "✓ elects it." if winner == cw else "✗ does NOT elect it."
        out.append(f"   Condorcet winner (beats every rival head-to-head): {cw}")
        out.append(f"   {name} {verdict}")
        if winner != cw and irv_w:
            hare = "finds it" if cw in irv_w else "also misses it"
            out.append(f"   (For contrast, full Hare IRV on these same ballots {hare}: "
                       f"{', '.join(irv_w)}.)")
        if winner != cw:
            out.append(f"   Note: the ballots DO contain the answer — {cw} wins every "
                       "pairing on this very same data. This count just never asks.")
    else:
        out.append("")
        out.append("   No Condorcet winner on these ballots (a cycle, or a pairwise tie).")

    # --- Cross-check our contingent count against pref_voting's own ---------
    out.append("")
    strict = all(len(lv) == len(cands) and all(len(x) == 1 for x in lv) for lv in voters)
    if not strict:
        out.append(" [plurality_with_runoff_put cross-check SKIPPED — it needs complete "
                   "strict rankings, and these ballots are truncated or have equal ranks. "
                   "The count above handles both; run without --ranks to cross-check.]")
        return "\n".join(out)
    try:
        idx = {c: i for i, c in enumerate(cands)}
        rankings = [[idx[lv[0]] for lv in levels] for levels in voters]
        pv = sorted(cands[x] for x in
                    plurality_with_runoff_put(Profile(rankings)))
    except Exception as ex:
        out.append(f" [plurality_with_runoff_put cross-check ERROR: {ex!r}]")
        return "\n".join(out)
    if len(pv) == 1 and pv[0] == winner:
        verdict = "AGREE ✓  (unique winner)"
    elif winner in pv:
        verdict = f"CONSISTENT ✓  (pref_voting returns a {len(pv)}-way PUT set)"
    else:
        verdict = "DISAGREE ✗  — INVESTIGATE"
    out.append(f" pref_voting plurality_with_runoff_put: {', '.join(pv)}")
    out.append(f" cross-check vs our contingent winner ({winner}): {verdict}")
    return "\n".join(out)


def _beats(voters, a, b):
    f = sum(1 for lv in voters if _prefers(lv, a, b) == a)
    g = sum(1 for lv in voters if _prefers(lv, a, b) == b)
    return f > g


if __name__ == "__main__":
    args = sys.argv[1:]
    cap = None
    if "--ranks" in args:
        i = args.index("--ranks")
        cap = int(args[i + 1])
        del args[i:i + 2]
    if not args:
        sys.exit("usage: python contingent_vote_report.py [--ranks N] FILE.yaml [...]")
    for p in args:
        print(report(p, cap))
        print()
