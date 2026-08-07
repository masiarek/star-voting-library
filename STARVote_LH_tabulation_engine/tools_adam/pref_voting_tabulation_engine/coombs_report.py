#!/usr/bin/env python3
"""
coombs_report.py — tabulate the COOMBS procedure, round by round.

Why this exists: nothing in this repo counted Coombs. `starvote_larry_hastings.py`
sends ranked ballots to the vendored pyrankvote, which counts **Hare** — eliminate
the candidate with the FEWEST first places. Coombs eliminates the one with the MOST
last places, which is a different count on the same ballots and routinely a
different winner. BetterVoting doesn't offer it either. So
`07_Concepts/voting_paradoxes/coombs.md` could only *assert* Felsenthal's Examples
17-22 in prose. It can now show them counted.

  * **Coombs** — if no candidate holds an absolute majority of first places, delete
    the candidate ranked LAST by the most voters; repeat until someone holds a
    majority. IRV read from the bottom of the ballot instead of the top.

The interesting consequence, and the reason Felsenthal devotes §A7 to it: a broad
consensus candidate is typically *everyone's* second choice and *some* faction's
last, so they accumulate both the pairwise wins that make them the Condorcet winner
and the last-place votes that get them deleted first. Example 17 is exactly that.

**Truncated and tied ballots.** A ballot whose bottom rank level holds k > 1
candidates (an explicit `A>B=C` tie, or truncation, where every unranked candidate
shares the bottom) casts 1/k of a last-place vote for each of them — the
equal-probability convention Felsenthal uses for unstated preferences. The report
says so out loud whenever a fractional count actually occurs, because it is a
convention, not arithmetic. With strict complete rankings — every example on the
Coombs page — nothing is fractional and the question doesn't arise.

The report ends with the contrast that carries the teaching: **Hare IRV** on the
same ballots, eliminating from the top instead of the bottom.

Cross-checked against Eric Pacuit's `pref_voting` on every run, so the winner is
computed twice by independent code. `pref_voting` is declared in pyproject.toml;
install with `uv sync`.

Usage:
    uv run STARVote_LH_tabulation_engine/tools_adam/pref_voting_tabulation_engine/coombs_report.py FILE.yaml
    uv run ... coombs_report.py --drop Cole FILE.yaml     # SCC: recount without a loser
"""
import os
import sys
from collections import Counter, defaultdict

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
from pref_voting_tabulation import (  # noqa: E402
    format_levels, parse_election, ranked_profile,
)
sys.path.insert(0, os.path.join(os.path.dirname(_HERE), "STARVote_LH_tabulation_engine"))
import starvote_larry_hastings as LH  # noqa: E402


def _levels(dicts, cands):
    """Per-voter rank levels over `cands`, best first, as lists of names.

    Built from the score dicts so score ballots and ranked ballots take one path:
    equal scores share a level (genuine indifference), and a candidate a ballot
    never mentions scores 0, which puts them in the bottom level alongside every
    other unmentioned name — the truncation reading documented above."""
    out = []
    for b in dicts:
        by_score = defaultdict(list)
        for c in cands:
            by_score[b.get(c, 0)].append(c)
        out.append([by_score[s] for s in sorted(by_score, reverse=True)])
    return out


def _counts(levels, alive):
    """(first-place counts, last-place counts, fractional?) restricted to `alive`."""
    first = {c: 0.0 for c in alive}
    last = {c: 0.0 for c in alive}
    frac = False
    for lv in levels:
        live = [[c for c in level if c in alive] for level in lv]
        live = [l for l in live if l]
        if not live:
            continue
        top, bot = live[0], live[-1]
        for c in top:
            first[c] += 1.0 / len(top)
        for c in bot:
            last[c] += 1.0 / len(bot)
        if len(top) > 1 or len(bot) > 1:
            frac = True
    return first, last, frac


def _fmt(x):
    return f"{x:g}"


def report(path, drop=None):
    cands, dicts, ranks, priority, has_ties, vm = parse_election(path)
    if drop and drop not in cands:
        raise SystemExit(f"--drop {drop!r}: no such candidate (have: {', '.join(cands)})")
    alive = [c for c in cands if c != drop]
    n = len(dicts)
    levels = _levels(dicts, alive)

    out = []
    out.append("=== Coombs' procedure — delete the most-hated, single winner ===")
    kind = "ranked" if ranks is not None else "score"
    note = f", {drop} DROPPED" if drop else ""
    out.append(f" Tabulating {n} {kind} ballots, {len(alive)} candidates{note}.\n")

    out.append("Ballots:")
    rows = [format_levels(lv, drop=drop) for lv in (ranks if ranks is not None else levels)]
    counts = Counter(rows)
    seen = []
    for r in rows:
        if r not in seen:
            seen.append(r)
    for r in seen:
        out.append(f"   {counts[r]:>3} × {r}")
    out.append("")

    majority = n / 2.0
    out.append(f"Majority to win: more than {_fmt(majority)} of {n} first places.\n")

    winner, saw_frac, rnd = None, False, 0
    eliminated = []
    while True:
        rnd += 1
        first, last, frac = _counts(levels, alive)
        saw_frac = saw_frac or frac
        out.append(f"Round {rnd} — first places:")
        for c in sorted(alive, key=lambda c: (-first[c], c)):
            out.append(f"   {c:<10} {_fmt(first[c]):>6}")
        lead = max(alive, key=lambda c: first[c])
        if first[lead] > majority:
            out.append(f"   → {lead} holds an absolute majority "
                       f"({_fmt(first[lead])} of {n}). Elected.\n")
            winner = lead
            break
        if len(alive) <= 1:
            winner = alive[0] if alive else None
            out.append(f"   → only {winner} remains. Elected.\n")
            break
        out.append(f"   No absolute majority (leader {lead} has {_fmt(first[lead])}).")
        out.append(f"   Last places — Coombs deletes the maximum:")
        for c in sorted(alive, key=lambda c: (-last[c], c)):
            out.append(f"   {c:<10} {_fmt(last[c]):>6}")
        worst = max(last[c] for c in alive)
        doomed = [c for c in alive if last[c] == worst]
        if len(doomed) > 1:
            pick = min(doomed, key=lambda c: priority.index(c) if c in priority else 1e9)
            out.append(f"   ⚠️  {len(doomed)} candidates tie on {_fmt(worst)} last places "
                       f"({', '.join(sorted(doomed))}) — the deletion is decided by LOT. "
                       f"Taking {pick} (lot order), but the result is NOT determinate.")
        else:
            pick = doomed[0]
            out.append(f"   → delete {pick} ({_fmt(worst)} last places).")
        out.append("")
        alive = [c for c in alive if c != pick]
        eliminated.append(pick)

    if saw_frac:
        out.append(" NOTE: some ballots tie or truncate at the top or bottom, so a "
                   "first/last place was SPLIT equally among the tied candidates "
                   "(Felsenthal's equal-probability convention). That is a convention, "
                   "not arithmetic — a different reading can move the deletion.\n")

    out.append(f"Winner — Coombs: {winner}")
    if eliminated:
        out.append(f"   Deletion order: {' → '.join(eliminated)}")
    out.append("")

    # --- The contrast: the same ballots read from the top. ---
    try:
        irv, *_ = LH.compute_irv_winner(alive + eliminated, dicts, priority)
    except Exception:
        irv = None
    if irv:
        agree = "the same winner." if irv == winner else f"a DIFFERENT winner: {irv}."
        out.append(f"Same ballots, read from the top — Hare IRV (fewest first places "
                   f"eliminated): {agree}")
        out.append("   Coombs punishes a candidate for having too many enemies, IRV for "
                   "having too few friends. A consensus candidate — everyone's second "
                   "choice — can be short of both.")
        out.append("")

    # --- Independent second computation. Loud when skipped, never silently. ---
    try:
        from pref_voting.iterative_methods import coombs as pv_coombs
    except Exception:
        out.append(" [pref_voting cross-check SKIPPED — library not installed. "
                   "Run `uv sync` (pref_voting is declared in pyproject.toml).]")
        return "\n".join(out)
    if ranks is None:
        out.append(" [pref_voting cross-check SKIPPED — score ballots; the independent "
                   "Coombs check runs on ranked ballots.]")
        return "\n".join(out)
    try:
        prof, kept = ranked_profile(cands, dicts, drop=drop)
        # pref_voting's coombs is numba-jitted over STRICT linear orders and cannot
        # consume a ProfileWithTies. Convert when the ballots really are strict;
        # to_linear_profile() returns None when they aren't, and then we say so
        # rather than flattening a tie into an order nobody cast.
        linear = prof.to_linear_profile()
        if linear is None:
            out.append(" [pref_voting cross-check UNAVAILABLE — these ballots tie or "
                       "truncate, and pref_voting's coombs takes strict linear orders "
                       "only. The count above stands on its own; treat it as "
                       "unwitnessed.]")
            return "\n".join(out)
        pv = sorted(kept[x] for x in pv_coombs(linear))
    except Exception as ex:
        out.append(f" [pref_voting cross-check ERROR: {ex!r}]")
        return "\n".join(out)

    if pv == [winner]:
        status = "AGREE ✓  (unique Coombs winner)"
    elif winner in pv:
        status = (f"CONSISTENT ✓  (this report broke a tie within pref_voting's "
                  f"{len(pv)}-way set — see the lot warning above)")
    else:
        status = "DISAGREE ✗  — INVESTIGATE"
    out.append(f" pref_voting coombs: {', '.join(pv)}")
    out.append(f" cross-check vs this report's winner ({winner}): {status}")
    return "\n".join(out)


if __name__ == "__main__":
    args = sys.argv[1:]
    drop = None
    if "--drop" in args:
        i = args.index("--drop")
        drop = args[i + 1]
        del args[i:i + 2]
    if not args:
        sys.exit("usage: python coombs_report.py [--drop NAME] FILE.yaml [FILE2.yaml ...]")
    for p in args:
        print(report(p, drop=drop))
        print()
