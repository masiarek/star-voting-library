#!/usr/bin/env python3
"""
minimax_report.py — tabulate MINIMAX (the Condorcet / Simpson-Kramer procedure).

Why this exists: nothing in this repo counted Minimax. `starvote_larry_hastings.py`
does STAR / Approval / Ranked Robin / SNTV and sends ranked ballots to the vendored
pyrankvote (Hare IRV); BetterVoting offers seven methods and Minimax is not among
them. So `07_Concepts/voting_paradoxes/minimax.md` could only *assert* Felsenthal's
Examples 29-33 in prose. It can now show them counted.

  * **Minimax** — elect the Condorcet winner if one exists; otherwise elect the
    candidate whose WORST pairwise loss is smallest. A genuine Condorcet method,
    so it never misses a Condorcet winner, but its cycle-breaker is what Felsenthal
    puts on trial: Condorcet Loser, Absolute Loser, No-Show, Twin, Truncation,
    Reinforcement and SCC paradoxes all live in that second clause.

**"Worst loss" is measured three different ways, and this matters.** The rule above
is ambiguous until you say what a loss is *worth*, and the three published readings
are genuinely different rules (Wikipedia, "Minimax Condorcet method"):

  * **winning votes** — how many voters backed the winning side. Felsenthal's
    convention, and what his tables print.
  * **margins** — winner's votes minus loser's. `pref_voting`'s default `minimax`.
  * **pairwise opposition** — votes against, whether or not the pair was lost.

This report prints winning votes and margins side by side and says whether they
agree, because with an ODD electorate and no pairwise ties they always do (margin =
2*opposition - n is monotone in opposition), and with an even one they need not.
That is not a footnote: Felsenthal's Example 32 amalgamates two districts into 14
voters precisely to land on a tie.

The report ends with the comparison that carries the teaching: **Copeland** — the
LH engine's Ranked Robin — reading the very same pairwise matrix and often
disagreeing. Minimax asks "whose worst defeat is mildest," Copeland asks "who won
most matchups." Example 29's D loses every matchup narrowly: the best possible
worst-loss and the worst possible win count.

Cross-checked against Eric Pacuit's `pref_voting` on every run, so the winner is
computed twice by independent code. `pref_voting` is declared in pyproject.toml;
install with `uv sync`.

Usage:
    uv run STARVote_LH_tabulation_engine/tools_adam/pref_voting_tabulation_engine/minimax_report.py FILE.yaml
    uv run ... minimax_report.py --drop Bree FILE.yaml    # SCC: recount without a loser
"""
import os
import sys
from collections import Counter

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
from pref_voting_tabulation import (  # noqa: E402
    format_levels, parse_election, ranked_profile,
)
sys.path.insert(0, os.path.join(os.path.dirname(_HERE), "STARVote_LH_tabulation_engine"))
import starvote_larry_hastings as LH  # noqa: E402


def _num(x):
    """Half-votes only appear under --equal-prob; print 7 not 7.0, but 6.5 as 6.5."""
    return f"{x:g}"


def _ballot_lines(cands, dicts, ranks, drop=None):
    """Collapse ballots to 'count × A > B > C' (ranked) or 'count × 5,3,0' (score)."""
    rows = []
    if ranks is not None:
        for order in ranks:
            rows.append(format_levels(order, drop=drop))
    else:
        for b in dicts:
            rows.append(", ".join(str(b.get(c, 0)) for c in cands if c != drop))
    counts = Counter(rows)
    seen = []
    for r in rows:
        if r not in seen:
            seen.append(r)
    return [(counts[r], r) for r in seen]


def _pairwise(dicts, keep, equal_prob=False):
    """{(a,b): (for_a, for_b)} for every pair, plus a flag for whether any ballot
    left a pair unstated.

    Two conventions, and the difference is the whole of Felsenthal's Example 31:

      * **default** — a ballot that ranks neither candidate of a pair (both
        truncated away) contributes NOTHING to that pair. This repo's reading, and
        the LH engine's and BetterVoting's: a voter who said nothing about b-vs-d
        gets no say in b-vs-d.
      * **equal_prob** — that ballot contributes ½ to each side, the
        equal-probability convention Felsenthal applies to unstated preferences.
        It is not a neutral bookkeeping choice: splitting a pair 50/50 INFLATES both
        candidates' opposition counts, and Minimax reads exactly those counts, so
        the convention can move the winner.

    A candidate the ballot ranked always beats one it left unranked, under both
    conventions — truncation expresses "these are worse," just not how they order
    among themselves."""
    n_alive = {c: None for c in keep}
    pair = {}
    unstated = False
    for i, a in enumerate(keep):
        for b in keep[i + 1:]:
            fa = fb = 0.0
            for d in dicts:
                sa, sb = d.get(a), d.get(b)
                if sa is None and sb is None:
                    if equal_prob:
                        fa += 0.5
                        fb += 0.5
                    continue
                sa = 0 if sa is None else sa
                sb = 0 if sb is None else sb
                if sa > sb:
                    fa += 1
                elif sb > sa:
                    fb += 1
            pair[(a, b)] = (fa, fb)
            pair[(b, a)] = (fb, fa)
    for d in dicts:
        if any(d.get(c) is None for c in keep) and sum(
                1 for c in keep if d.get(c) is None) > 1:
            unstated = True
    del n_alive
    return pair, unstated


def report(path, drop=None, equal_prob=False):
    cands, dicts, ranks, priority, has_ties, vm = parse_election(path)
    if drop and drop not in cands:
        raise SystemExit(f"--drop {drop!r}: no such candidate (have: {', '.join(cands)})")
    keep = [c for c in cands if c != drop]
    n = len(dicts)
    pair, unstated = _pairwise(dicts, keep, equal_prob=equal_prob)

    out = []
    out.append("=== Minimax (Condorcet / Simpson-Kramer) — single winner ===")
    kind = "ranked" if ranks is not None else "score"
    note = f", {drop} DROPPED" if drop else ""
    out.append(f" Tabulating {n} {kind} ballots, {len(keep)} candidates{note}.\n")

    out.append("Ballots:")
    for cnt, r in _ballot_lines(cands, dicts, ranks, drop=drop):
        out.append(f"   {cnt:>3} × {r}")
    out.append("")

    if unstated:
        conv = ("EQUAL-PROBABILITY (Felsenthal): a pair both truncated away counts ½–½"
                if equal_prob else
                "this repo's default: a pair both truncated away counts for NEITHER")
        out.append(f" Truncated ballots present. Convention — {conv}.")
        out.append(" Re-run with --equal-prob (or without it) to see the other reading;"
                   " on Example 31 they elect different candidates.\n")

    # --- Every pair, head to head. This matrix is the whole input to Minimax. ---
    out.append("Round-robin — every pair, head-to-head (votes For – Against):")
    # worst[c] under each convention; also the win/loss record for the Copeland contrast.
    worst_wv = {c: 0 for c in keep}      # most votes cast for an opponent who BEAT c
    worst_mg = {c: 0 for c in keep}      # largest margin by which c was beaten
    worst_op = {c: 0 for c in keep}      # most votes against c in any pair, won or lost
    wins = {c: [] for c in keep}
    losses = {c: [] for c in keep}
    ties = {c: [] for c in keep}
    for i, a in enumerate(keep):
        for b in keep[i + 1:]:
            fa, aa = pair[(a, b)]        # a-For, a-Against
            worst_op[a] = max(worst_op[a], aa)
            worst_op[b] = max(worst_op[b], fa)
            if fa > aa:
                wins[a].append(b); losses[b].append(a)
                worst_wv[b] = max(worst_wv[b], fa)
                worst_mg[b] = max(worst_mg[b], fa - aa)
                out.append(f"   {a} beats {b}   {_num(fa)} – {_num(aa)}")
            elif aa > fa:
                wins[b].append(a); losses[a].append(b)
                worst_wv[a] = max(worst_wv[a], aa)
                worst_mg[a] = max(worst_mg[a], aa - fa)
                out.append(f"   {b} beats {a}   {_num(aa)} – {_num(fa)}")
            else:
                ties[a].append(b); ties[b].append(a)
                out.append(f"   {a} ties {b}    {_num(fa)} – {_num(aa)}")
    out.append("")

    # Guard the hand-rolled matrix against the engine's, in the mode where they
    # must agree. A silent divergence here would corrupt every number above.
    if not equal_prob and not drop:
        lh = LH.calculate_preference_matrix(cands, dicts)
        for i, a in enumerate(keep):
            for b in keep[i + 1:]:
                if (lh[a][b][0], lh[a][b][1]) != pair[(a, b)]:
                    out.append(f"   ⚠️  matrix disagrees with the LH engine on "
                               f"{a} vs {b}: LH {lh[a][b][0]}–{lh[a][b][1]}, "
                               f"here {_num(pair[(a, b)][0])}–{_num(pair[(a, b)][1])}. "
                               "INVESTIGATE — do not trust the numbers above.")
        out.append("")

    # --- A Condorcet winner short-circuits the rule: Minimax elects them outright. ---
    unbeaten = [c for c in keep if not losses[c] and not ties[c]]
    cw = unbeaten[0] if len(unbeaten) == 1 else None

    # --- The worst-loss table, both conventions side by side. ---
    out.append("Worst pairwise loss — the number Minimax minimises:")
    out.append(f"   {'':<10}{'winning votes':>15}{'margin':>10}{'opposition':>13}")
    for c in sorted(keep, key=lambda c: (worst_wv[c], worst_mg[c])):
        wv = _num(worst_wv[c]) if losses[c] else "— (unbeaten)"
        mg = _num(worst_mg[c]) if losses[c] else "—"
        out.append(f"   {c:<10}{wv:>15}{mg:>10}{_num(worst_op[c]):>13}")
    out.append("")

    def _leaders(score):
        lo = min(score[c] for c in keep)
        return sorted(c for c in keep if score[c] == lo)

    win_wv = [cw] if cw else _leaders(worst_wv)
    win_mg = [cw] if cw else _leaders(worst_mg)

    if cw:
        out.append(f"Winner — Minimax: {cw}")
        out.append(f"   {cw} beats every opponent head-to-head — the Condorcet winner, "
                   "elected by the rule's first clause. No cycle-breaking needed.")
    else:
        agree = win_wv == win_mg
        head = win_wv[0] if len(win_wv) == 1 else " / ".join(win_wv)
        out.append(f"Winner — Minimax (winning votes, Felsenthal's convention): {head}")
        if len(win_wv) > 1:
            out.append(f"   ⚠️  {len(win_wv)} candidates tie on the smallest worst loss "
                       f"({worst_wv[win_wv[0]]}) — Minimax is INDECISIVE here and the "
                       "result turns on a lot. Reporting the leader set rather than "
                       "inventing a tiebreak.")
        else:
            out.append(f"   No Condorcet winner (the top cycles), so the second clause "
                       f"decides: {head}'s worst defeat ({worst_wv[head]} votes) is the "
                       "mildest on the board.")
        if agree:
            out.append("   The margins convention agrees. (It must, on an odd electorate "
                       "with no pairwise ties: margin = 2·votes − n rises with votes.)")
        else:
            out.append(f"   ⚠️  CONVENTION SPLIT — by margins the winner is "
                       f"{' / '.join(win_mg)}, not {head}. Same rule name, different "
                       "rule. See the module docstring.")
    out.append("")

    # --- The contrast that earns its place: same matrix, the other cycle-breaker. ---
    cope = {c: len(wins[c]) + 0.5 * len(ties[c]) for c in keep}
    top = max(cope.values())
    cope_leaders = sorted(c for c in keep if cope[c] == top)
    out.append("Same matrix, the other cycle-breaker — Copeland (= LH's Ranked Robin):")
    for c in sorted(keep, key=lambda c: (-cope[c], c)):
        w, l, t = len(wins[c]), len(losses[c]), len(ties[c])
        rec = f"{w}–{l}" + (f"–{t}t" if t else "")
        out.append(f"   {c:<10} {rec:<7} Copeland {cope[c]:g}")
    same = set(cope_leaders) == set(win_wv)
    verdict = ("agrees with Minimax." if same else
               f"DISAGREES with Minimax ({' / '.join(win_wv)}).")
    out.append(f"   Copeland leader(s): {', '.join(cope_leaders)} — {verdict}")
    if not same:
        out.append("   Minimax asks whose worst defeat is mildest; Copeland asks who won "
                   "the most matchups. A candidate who loses every pairing narrowly "
                   "scores best on the first and worst on the second.")
    out.append("")

    # --- Independent second computation. Loud when skipped, never silently. ---
    try:
        from pref_voting.margin_based_methods import minimax as pv_minimax
    except Exception:
        out.append(" [pref_voting cross-check SKIPPED — library not installed. "
                   "Run `uv sync` (pref_voting is declared in pyproject.toml).]")
        return "\n".join(out)
    if ranks is None:
        out.append(" [pref_voting cross-check SKIPPED — score ballots; the independent "
                   "Minimax check runs on ranked ballots.]")
        return "\n".join(out)
    if equal_prob:
        out.append(" [pref_voting cross-check SKIPPED — --equal-prob is Felsenthal's "
                   "convention for unstated pairs, which pref_voting does not "
                   "implement; it would be checking a different rule. Run without "
                   "the flag for the witnessed count.]")
        return "\n".join(out)
    try:
        prof, kept = ranked_profile(cands, dicts, drop=drop)
        pv = sorted(kept[x] for x in pv_minimax(prof))
    except Exception as ex:
        out.append(f" [pref_voting cross-check ERROR: {ex!r}]")
        return "\n".join(out)

    # pref_voting's minimax is the MARGINS reading, so compare it to win_mg.
    if pv == win_mg:
        status = "AGREE ✓"
    elif set(pv) & set(win_mg):
        status = f"PARTIAL — overlapping leader sets, investigate"
    else:
        status = "DISAGREE ✗  — INVESTIGATE"
    out.append(f" pref_voting minimax (margins): {', '.join(pv)}")
    out.append(f" cross-check vs this report's margins winner "
               f"({' / '.join(win_mg)}): {status}")
    return "\n".join(out)


if __name__ == "__main__":
    args = sys.argv[1:]
    drop = None
    equal_prob = False
    if "--equal-prob" in args:
        args.remove("--equal-prob")
        equal_prob = True
    if "--drop" in args:
        i = args.index("--drop")
        drop = args[i + 1]
        del args[i:i + 2]
    if not args:
        sys.exit("usage: python minimax_report.py [--drop NAME] [--equal-prob] "
                 "FILE.yaml [FILE2.yaml ...]")
    for p in args:
        print(report(p, drop=drop, equal_prob=equal_prob))
        print()
