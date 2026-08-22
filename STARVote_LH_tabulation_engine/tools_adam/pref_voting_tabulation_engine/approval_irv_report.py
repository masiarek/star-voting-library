#!/usr/bin/env python3
"""
approval_irv_report.py — count the two ways IRV can be extended to EQUAL RANKS.

Why this exists: deployed instant runoff refuses a tie. Rank two candidates equal
on a US RCV ballot and you have cast an *overvote*; the ballot is rejected, or
counted until the tied rank is reached and then set aside. This repo says so in
several places, and it is true of every jurisdiction that runs the rule. What it
is NOT is a mathematical necessity — IRV can be generalized to weak orders
(rankings with ties), and there are exactly two natural ways to do it:

  * **Approval-IRV** — a ballot gives **one full point to each** candidate in its
    top surviving indifference class. Eliminate the lowest, repeat.
  * **Split-IRV** — a ballot **splits one point evenly** among the candidates in
    its top surviving class (t of them -> 1/t each). Eliminate the lowest, repeat.

Both agree with ordinary IRV on strict ballots. They routinely disagree with each
other once a single voter marks a tie, and Delemazure & Peters (EC'24,
arXiv:2404.11407) prove the disagreement is not a coin flip: **Approval-IRV is the
unique elimination scoring rule that keeps independence of clones and respect for
cohesive majorities**, and the unique one that extends IRV monotonically. Split-IRV
— the generalization actually in the field, used by the John Muir Trust and the
London Mathematical Society and implemented in R's `vote` package — fails all three.

Nothing else in this repo counts either rule. `starvote_larry_hastings.py` sends
ranked ballots to the vendored pyrankvote, which counts **Hare** and cannot
represent a tie at all: its parser reads `a=b` and silently emits `a>b`, in ballot
column order. So an equal-rank ballot has never had a truthful count here. It does
now.

**Reading a 0.** These weak orders are COMPLETE by default — every candidate sits
in some indifference class, and a score of 0 is the bottom class, not an absence.
That is the model the paper works in. This repo's own RCV reading is different (0 =
unranked, and the ballot exhausts), so when any ballot holds a 0 the report counts
it BOTH ways and prints both answers. Where they differ, neither is "the" answer
and the report says which convention bought which winner.

**Ties.** Elimination ties are resolved by parallel-universe tie-breaking, which is
the paper's own definition: follow every branch and take the union of the winners.
A multi-candidate answer is therefore a real tie under the rule, not this tool
declining to choose.

Cross-checked two ways, on every run that admits one: on a profile with NO ties
both rules must equal `pref_voting`'s `instant_runoff`, and on a DICHOTOMOUS
profile (every ballot two classes) Approval-IRV must equal the plain approval
count. Where a profile admits neither check the report says so rather than
implying a witness it does not have.

Usage:
    uv run STARVote_LH_tabulation_engine/tools_adam/pref_voting_tabulation_engine/approval_irv_report.py FILE.yaml
    uv run ... approval_irv_report.py --drop Cody FILE.yaml   # clone check: recount without a clone
"""
import os
import sys
from fractions import Fraction
from itertools import combinations

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
from pref_voting_tabulation import (  # noqa: E402
    PREF_VOTING_AVAILABLE, format_levels, parse_election, ranked_profile,
)

try:
    from pref_voting.iterative_methods import instant_runoff as pv_irv
except Exception:  # pragma: no cover
    pv_irv = None


# --------------------------------------------------------------------------- #
# Weak orders out of the repo's two ballot shapes
# --------------------------------------------------------------------------- #
def weak_orders(cands, dicts, voters):
    """Per-voter indifference classes, best first, as lists of names.

    Ranked ballots arrive already levelled (`a=b>c` -> [[a,b],[c]]); a candidate
    left off such a ballot joins the bottom class. Score ballots are levelled by
    equal score, which is the same statement in the other notation: two 4s are one
    indifference class, exactly as `a=b` is."""
    out = []
    for i, b in enumerate(dicts):
        if voters is not None:
            lv = [list(l) for l in voters[i]]
            named = {c for l in lv for c in l}
            rest = [c for c in cands if c not in named]
            if rest:
                lv.append(rest)
        else:
            by = {}
            for c in cands:
                by.setdefault(b.get(c, 0), []).append(c)
            lv = [by[s] for s in sorted(by, reverse=True)]
        out.append(lv)
    return out


def top_class(levels, alive, exhaust_zeros=None, scores=None):
    """The voter's best surviving indifference class, or None if exhausted.

    `exhaust_zeros` switches to this repo's RCV reading: a 0 is not a preference,
    so once a ballot's only survivors are 0s the ballot has stopped counting."""
    for lvl in levels:
        live = [c for c in lvl if c in alive]
        if live:
            if exhaust_zeros and scores is not None and all(
                    scores.get(c, 0) == 0 for c in live):
                return None
            return live
    return None


# --------------------------------------------------------------------------- #
# The two rules
# --------------------------------------------------------------------------- #
def round_scores(profile, alive, mode, exhaust_zeros=False):
    """Approval (1 point each) or split (1/t each) scores for one round."""
    sc = {c: Fraction(0) for c in alive}
    exhausted = 0
    for w, lv, sd in profile:
        top = top_class(lv, alive, exhaust_zeros, sd)
        if not top:
            exhausted += w
            continue
        pts = Fraction(1) if mode == "approval" else Fraction(1, len(top))
        for c in top:
            sc[c] += pts * w
    return sc, exhausted


def winners(profile, cands, mode, exhaust_zeros=False, _alive=None, _memo=None):
    """Winner SET under parallel-universe tie-breaking (the paper's definition)."""
    alive = frozenset(cands) if _alive is None else _alive
    memo = {} if _memo is None else _memo
    if alive in memo:
        return memo[alive]
    if len(alive) == 1:
        return set(alive)
    sc, _ = round_scores(profile, alive, mode, exhaust_zeros)
    lo = min(sc.values())
    out = set()
    for loser in sorted(c for c in alive if sc[c] == lo):
        out |= winners(profile, cands, mode, exhaust_zeros, alive - {loser}, memo)
    memo[alive] = out
    return out


def trace(profile, cands, mode, exhaust_zeros=False):
    """Round-by-round table down the FIRST branch, plus where branches opened."""
    alive, rows, branched = set(cands), [], []
    while len(alive) > 1:
        sc, ex = round_scores(profile, alive, mode, exhaust_zeros)
        lo = min(sc.values())
        tied = sorted(c for c in alive if sc[c] == lo)
        rows.append((sorted(alive, key=lambda c: (-sc[c], c)), dict(sc), tied, ex))
        if len(tied) > 1:
            branched.append((len(rows), tied))
        alive -= {tied[0]}
    return rows, branched


def fmt(x):
    """Fractions as they were cast: 8 stays 8, 25/3 prints as 8.33."""
    return str(x) if x.denominator == 1 else f"{float(x):.2f}"


# --------------------------------------------------------------------------- #
# Respect for cohesive majorities (Delemazure & Peters, Definition 3.3)
# --------------------------------------------------------------------------- #
def cohesive_violations(profile, cands, win):
    """Every (rallying candidate, excluded winner, size) that breaks the axiom.

    The axiom quantifies over all majorities S that share some candidate c on top,
    and demands the winner be top-ranked by at least one member of S. A winner w
    therefore breaks it exactly when more than half the voters rank c on top and w
    NOT on top -- those voters alone are a cohesive majority whose union of top
    sets misses w. One pass over (c, w) pairs decides the axiom outright; no subset
    enumeration is needed."""
    n = sum(w for w, _, _ in profile)
    tops = [(w, set(top_class(lv, set(cands)) or [])) for w, lv, _ in profile]
    bad = []
    for c in cands:
        for x in sorted(win):
            k = sum(w for w, t in tops if c in t and x not in t)
            if 2 * k > n:
                bad.append((c, x, k))
    return bad, n


# --------------------------------------------------------------------------- #
# Report
# --------------------------------------------------------------------------- #
def _rule_block(out, label, profile, cands, mode, exhaust_zeros):
    rows, branched = trace(profile, cands, mode, exhaust_zeros)
    win = sorted(winners(profile, cands, mode, exhaust_zeros))
    out.append(f"  {label}")
    for i, (order, sc, tied, ex) in enumerate(rows, 1):
        cells = "  ".join(f"{c} {fmt(sc[c])}" for c in order)
        tail = f"   -> eliminate {tied[0]}"
        if len(tied) > 1:
            tail += f"  [{len(tied)}-way tie: {', '.join(tied)}]"
        if ex:
            tail += f"  ({ex} exhausted)"
        out.append(f"    round {i}:  {cells}{tail}")
    out.append(f"    winner: {', '.join(win)}"
               + ("   [tie under the rule]" if len(win) > 1 else ""))
    if branched:
        out.append(f"    note: elimination tied in round(s) "
                   f"{', '.join(str(r) for r, _ in branched)}; the winner above is "
                   f"the union over every branch (parallel-universe tie-breaking).")
    return win


def report(path, drop=None):
    cands, dicts, voters, _lot, _has_ties, vm = parse_election(path)
    if drop:
        cands = [c for c in cands if c != drop]
        dicts = [{k: v for k, v in b.items() if k != drop} for b in dicts]
        if voters is not None:
            voters = [[[c for c in l if c != drop] for l in lv] for lv in voters]
            voters = [[l for l in lv if l] for lv in voters]

    levels = weak_orders(cands, dicts, voters)
    profile = [(1, lv, dicts[i]) for i, lv in enumerate(levels)]
    n = len(profile)
    ties = sum(1 for lv in levels if any(len(l) > 1 for l in lv))
    dicho = all(len(lv) == 2 for lv in levels)

    out = [f"=== Approval-IRV vs Split-IRV — {os.path.basename(path)} ===",
           f" method in file: {vm}   candidates: {', '.join(cands)}   ballots: {n}"]
    if drop:
        out.append(f" [--drop {drop}: recounted with that candidate removed]")
    out.append(f" ballots marking at least one tie: {ties} of {n}"
               + ("   (none — both rules must agree with plain IRV)" if not ties else ""))
    out.append("")
    out.append(" Ballots (best class first):")
    seen = []
    for lv in levels:                       # collapse identical ballots with x,
        txt = format_levels(lv)             # the house style for a weighted bloc
        if seen and seen[-1][1] == txt:
            seen[-1][0] += 1
        elif any(t == txt for _, t in seen):
            for row in seen:
                if row[1] == txt:
                    row[0] += 1
                    break
        else:
            seen.append([1, txt])
    for w, txt in seen:
        out.append(f"   {txt}" if w == 1 else f"   {w} x  {txt}")
    out.append("")

    approval = _rule_block(out, "Approval-IRV  (1 point to EACH top choice)",
                           profile, cands, "approval", False)
    out.append("")
    split = _rule_block(out, "Split-IRV     (1 point SPLIT among top choices)",
                        profile, cands, "split", False)
    out.append("")
    verdict = ("the two generalizations AGREE here"
               if approval == split else
               f"the two generalizations DISAGREE: Approval-IRV {', '.join(approval)}"
               f"  vs  Split-IRV {', '.join(split)}")
    out.append(f" -> {verdict}")

    # The repo's own 0-is-unranked reading, whenever a 0 is actually present.
    if any(any(b.get(c, 0) == 0 for c in cands) for b in dicts):
        a2 = sorted(winners(profile, cands, "approval", True))
        s2 = sorted(winners(profile, cands, "split", True))
        same = (a2 == approval and s2 == split)
        out.append("")
        out.append(f" Under this repo's RCV reading instead (a 0 is not a preference, so a"
                   f" ballot whose\n survivors are all 0 has exhausted): Approval-IRV "
                   f"{', '.join(a2)}, Split-IRV {', '.join(s2)}."
                   + ("  Same answers — the convention is not doing any work here."
                      if same else
                      "  DIFFERENT from the complete-weak-order count above; the"
                      " convention, not the ballots, is deciding."))

    # Respect for cohesive majorities.
    out.append("")
    for label, win in (("Approval-IRV", approval), ("Split-IRV", split)):
        bad, tot = cohesive_violations(profile, cands, win)
        if bad:
            c, x, k = bad[0]
            out.append(f" Respect for cohesive majorities — {label}: VIOLATED. {k} of "
                       f"{tot} voters rank {c} top and do not rank {x} top; that "
                       f"majority is cohesive on {c}, yet {x} wins.")
        else:
            out.append(f" Respect for cohesive majorities — {label}: satisfied.")

    out.append("")
    out.append(_crosscheck(cands, dicts, ties, dicho, approval, split))
    return "\n".join(out)


def _crosscheck(cands, dicts, ties, dicho, approval, split):
    lines = [" [cross-check]"]
    if ties == 0:
        if not (PREF_VOTING_AVAILABLE and pv_irv):
            lines.append("  pref_voting unavailable — install with `uv sync`.")
            return "\n".join(lines)
        try:
            prof, kept = ranked_profile(cands, dicts)
            linear = prof.to_linear_profile()
            if linear is None:
                lines.append("  strict-ballot check UNAVAILABLE (pref_voting's IRV takes "
                             "linear orders only).")
            else:
                pv = sorted(kept[x] for x in pv_irv(linear))
                ok = (approval == pv and split == pv)
                lines.append(f"  no ballot ties, so both rules must equal plain IRV. "
                             f"pref_voting instant_runoff: {', '.join(pv)} — "
                             f"{'AGREE ✓' if ok else 'DISAGREE ✗ — INVESTIGATE'}")
        except Exception as ex:
            lines.append(f"  pref_voting cross-check ERROR: {ex!r}")
    else:
        lines.append("  ballots carry ties, and no third-party library in this repo "
                     "counts either rule on weak orders — pref_voting's IRV takes "
                     "strict linear orders. Treat the counts above as UNWITNESSED "
                     "except for the dichotomous check below.")
    if dicho:
        # On dichotomous ballots every eliminated candidate's supporters fall back
        # to the same bottom class, which lifts all survivors equally — so the
        # approval ORDER never changes and Approval-IRV must elect an approval
        # winner. An independent statement of the same count.
        tally = {}
        for c in cands:
            tally[c] = sum(1 for b in dicts if b.get(c, 0) > 0)
        hi = max(tally.values())
        av = sorted(c for c in cands if tally[c] == hi)
        ok = approval == av
        lines.append(f"  every ballot is dichotomous, so Approval-IRV must elect the "
                     f"plain approval winner. Approval tally: "
                     f"{', '.join(f'{c} {tally[c]}' for c in sorted(cands))} -> "
                     f"{', '.join(av)} — {'AGREE ✓' if ok else 'DISAGREE ✗ — INVESTIGATE'}")
    return "\n".join(lines)


if __name__ == "__main__":
    args = sys.argv[1:]
    drop = None
    if "--drop" in args:
        i = args.index("--drop")
        drop = args[i + 1]
        del args[i:i + 2]
    if not args:
        sys.exit("usage: python approval_irv_report.py [--drop NAME] FILE.yaml [...]")
    for p in args:
        print(report(p, drop=drop))
        print()
