#!/usr/bin/env python3
"""
cycle_resolution_report.py — the cycle-resolution methods the LH engine can't run.

The LH engine's Ranked Robin is **Copeland** (pairwise wins − losses) plus a
margins tiebreak. That's the right teaching default — but in a Condorcet **cycle**
the whole Condorcet family splits apart, and the other members (Minimax, Ranked
Pairs, Schulze/beat-path, Split Cycle, Stable Voting) have no LH implementation.
This tool prints them, from Eric Pacuit & Wesley Holliday's `pref_voting`, so the
teaching pages on cycles can state verified winners instead of asserted ones.

What it prints, for any ranked-ballot YAML in this repo:
  * the ballots, collapsed
  * every pairwise margin, and whether a Condorcet winner exists
  * the Smith set
  * each cycle-resolution method's winner **set** (they can legitimately return
    more than one candidate — Split Cycle does so on purpose)
  * optionally, with --drop CANDIDATE, the same table with a candidate removed —
    which is how a spoiler / IIA failure is demonstrated

Sorted by Fishburn's classification (see
00_start_here/topics/condorcet/condorcet_reading_list.md): C1 methods read only
who-beat-whom, C2 methods read the margins too.

Usage:
    uv run STARVote_LH_tabulation_engine/tools_adam/pref_voting_tabulation_engine/cycle_resolution_report.py FILE.yaml
    uv run …/cycle_resolution_report.py FILE.yaml --drop Birch

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
    from pref_voting.c1_methods import copeland, smith_set
    from pref_voting.margin_based_methods import (
        minimax, beat_path, ranked_pairs, split_cycle, stable_voting,
    )
except ImportError:  # pragma: no cover - optional dependency
    print("cycle_resolution_report: pref_voting is not installed "
          "(pip install pref_voting, or `uv sync`).", file=sys.stderr)
    raise SystemExit(2)

# (label, function, Fishburn class) — order is the teaching order, simplest first.
METHODS = [
    ("Copeland (= Ranked Robin)", copeland, "C1"),
    ("Minimax", minimax, "C2"),
    ("Ranked Pairs", ranked_pairs, "C2"),
    ("Schulze (beat path)", beat_path, "C2"),
    ("Split Cycle", split_cycle, "C2"),
    ("Stable Voting", stable_voting, "C2"),
]


def build_profile(cands, ranks, drop=None):
    """A pref_voting Profile from this repo's ranked ballots, optionally minus one candidate."""
    keep = [c for c in cands if c != drop]
    idx = {c: i for i, c in enumerate(keep)}
    rankings = [[idx[c] for c in order if c != drop] for order in ranks]
    return Profile(rankings), keep


def _names(winners, keep):
    return ", ".join(keep[c] for c in sorted(winners)) if winners else "(none)"


def report(path, drop=None):
    cands, dicts, ranks, _priority, _has_ties, _vm = parse_election(path)
    if ranks is None:
        raise SystemExit(f"{path}: not a ranked-ballot election "
                         "(this tool reads ranked ballots; score ballots have no pairwise cycle to resolve).")

    if drop is not None and drop not in cands:
        raise SystemExit(f"{path}: no candidate named {drop!r} "
                         f"(candidates: {', '.join(cands)})")
    prof, keep = build_profile(cands, ranks, drop)

    out = []
    out.append("=== Cycle resolution — the Condorcet family, side by side ===")
    label = f" (with {drop} REMOVED from every ballot)" if drop else ""
    out.append(f" {len(ranks)} ranked ballots, {len(keep)} candidates{label}.\n")

    collapsed = Counter(" > ".join(c for c in o if c != drop) for o in ranks)
    out.append("Ballots:")
    for order, cnt in collapsed.most_common():
        out.append(f"   {cnt:>3} × {order}")
    out.append("")

    out.append("Pairwise margins (winner's margin over loser):")
    beats = {c: 0 for c in keep}
    for i, a in enumerate(keep):
        for b in keep[i + 1:]:
            m = prof.margin(keep.index(a), keep.index(b))
            if m > 0:
                out.append(f"   {a} beats {b} by {m}")
                beats[a] += 1
            elif m < 0:
                out.append(f"   {b} beats {a} by {-m}")
                beats[b] += 1
            else:
                out.append(f"   {a} ties {b}")
    cw = [c for c in keep if beats[c] == len(keep) - 1]
    out.append("")
    out.append(f"Condorcet winner: {cw[0]}" if cw
               else "Condorcet winner: NONE — majority preference cycles.")
    out.append(f"Smith set: {_names(smith_set(prof), keep)}")
    out.append("")

    out.append("Winners by method:")
    width = max(len(m[0]) for m in METHODS)
    for name, vm, cls in METHODS:
        out.append(f"   {name:<{width}}  [{cls}]  {_names(vm(prof), keep)}")
    out.append("")
    out.append("A method returning more than one name has not failed — it is reporting a genuine")
    out.append("tie. Split Cycle does this by design; Copeland does it because a cycle often")
    out.append("leaves candidates with identical win-loss records.")
    return "\n".join(out)


def main(argv):
    args = [a for a in argv[1:] if not a.startswith("--")]
    drop = None
    if "--drop" in argv:
        i = argv.index("--drop")
        if i + 1 >= len(argv):
            raise SystemExit("--drop needs a candidate name")
        drop = argv[i + 1]
        args = [a for a in args if a != drop]
    if not args:
        raise SystemExit(__doc__.strip().splitlines()[-4].strip())
    for path in args:
        print(report(path, drop))


if __name__ == "__main__":
    main(sys.argv)
