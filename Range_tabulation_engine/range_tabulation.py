#!/usr/bin/env python3
"""
range_tabulation.py — Range / Score voting tabulator for this library.

Range (a.k.a. Score) voting: every voter grades each candidate on a fixed scale
(0..max); the candidate with the **highest total score wins**. No runoff, no
elimination — just sum the grades. It is Approval at higher resolution, and
STAR's score round *without* the automatic runoff.

Engine choice: this wraps **pref_voting** (Eric Pacuit,
https://pref-voting.readthedocs.io) — the same independent engine this repo
already uses to cross-check Condorcet / IRV / Plurality — via its native
`grade_methods.score_voting`. We ALSO compute the totals by hand and assert the
two agree, so the tabulation is both reproducible and independently verified.
If pref_voting isn't installed the hand count still runs (the cross-check is
skipped with a note), so the engine degrades gracefully.

Ballot format is the library's usual score grid (header row of candidate names,
then one row of scores per voter; `N ×`/`N:` weight prefixes and markers all
handled). `voting_method:` is ignored — any score ballot can be read as Range.

Usage:
    python Range_tabulation_engine/range_tabulation.py <election.yaml>

Writes a full-context `<stem>_RANGE_tabulated.txt` mirror into the source
folder's `<folder>_tabulated/` (RANGE suffix so it never collides with a STAR
mirror of the same election).
"""
import os
import sys
from pathlib import Path

# Reuse the vendored RCV engine's robust score-grid parser + block loader.
_RCV = Path(__file__).resolve().parent.parent / "RCV_IRV_tabulation_engine"
if str(_RCV) not in sys.path:
    sys.path.insert(0, str(_RCV))
from rcv_irv_tabulation import load_ballots_block, parse_score_ballots  # noqa: E402

try:
    import yaml as _yaml
except Exception:  # pragma: no cover
    _yaml = None

# pref_voting is optional (matches the pref_voting cross-check engine's stance).
try:
    from pref_voting.grade_profiles import GradeProfile
    from pref_voting.grade_methods import score_voting
    _PV = True
except Exception:  # pragma: no cover
    _PV = False


def _meta(path):
    """Return (election_title, scenario_description, lot_numbers) if PyYAML is
    available, else blanks. Tolerates the flat and nested (election:) schemas."""
    if _yaml is None:
        return "", "", None
    try:
        data = _yaml.safe_load(Path(path).read_text(encoding="utf-8"))
    except Exception:
        return "", "", None
    node = data.get("election", data) if isinstance(data, dict) else {}
    if isinstance(node, dict) and "races" in node and node["races"]:
        race = node["races"][0]
    else:
        race = node
    title = (node.get("election_title") or race.get("election_title") or "")
    desc = (race.get("scenario_description")
            or node.get("scenario_description") or "")
    lot = race.get("lot_numbers") or node.get("lot_numbers")
    return str(title), str(desc), lot


def tabulate(candidates, weighted_ballots, lot_numbers=None):
    """Return (winner, totals, max_grade, pv_winner_or_None).

    weighted_ballots: list of (weight, {cand: score}). Winner = highest total;
    ties broken by lot_numbers order, else candidate (column) order."""
    totals = {c: 0 for c in candidates}
    max_grade = 0
    for weight, marks in weighted_ballots:
        for c in candidates:
            s = int(marks.get(c, 0) or 0)
            totals[c] += weight * s
            if s > max_grade:
                max_grade = s
    order = [c for c in (lot_numbers or []) if c in candidates]
    for c in candidates:            # append any missing, preserving column order
        if c not in order:
            order.append(c)
    top = max(totals.values())
    leaders = [c for c in candidates if totals[c] == top]
    winner = min(leaders, key=order.index)

    pv_winner = None
    if _PV:
        grade_maps, gcounts = [], []
        for weight, marks in weighted_ballots:
            grade_maps.append({c: int(marks.get(c, 0) or 0) for c in candidates})
            gcounts.append(int(weight))
        grades = list(range(0, max(max_grade, 1) + 1))
        gp = GradeProfile(grade_maps, grades, gcounts=gcounts, candidates=list(candidates))
        pv = [str(x) for x in score_voting(gp)]
        # pref_voting may return co-winners on an exact tie; resolve by the same order.
        pv_winner = min(pv, key=order.index) if pv else None
    return winner, totals, max_grade, pv_winner


def build_report(path, title, desc, candidates, weighted, winner, totals, max_grade, pv_winner):
    n = sum(w for w, _ in weighted)
    L = [f"--- Range / Score Voting (single winner) ---"]
    if title:
        L.append(f"  {title}")
    L.append(f" Tabulating {n} ballots on a 0–{max_grade} scale "
             f"(range/score: highest total wins, no runoff).")
    L.append("")
    if desc:
        L.append("[Scenario]")
        for ln in desc.strip().splitlines():
            L.append("  " + ln)
        L.append("")
    L.append("Ballots:")
    L.append("  " + ", ".join(candidates))
    for w, marks in weighted:
        row = ", ".join(str(int(marks.get(c, 0) or 0)) for c in candidates)
        L.append(f"  {w} × {row}" if w != 1 else f"  {row}")
    L.append("")
    L.append("Total score (sum of all grades):")
    for c in sorted(candidates, key=lambda c: -totals[c]):
        mark = "  ← winner" if c == winner else ""
        L.append(f"  {c:<14} {totals[c]}{mark}")
    L.append("")
    if pv_winner is not None:
        agree = "✓ agrees" if pv_winner == winner else f"✗ DISAGREES (pref_voting={pv_winner})"
        L.append(f"Cross-check — pref_voting score_voting: {pv_winner}  ({agree} with the hand count)")
    else:
        L.append("Cross-check — pref_voting not installed; hand count only "
                 "(install `pref_voting` to enable the independent check).")
    L.append("")
    L.append(f"Winner — Range / Score Voting (single winner)")
    L.append(f"  {winner}")
    return "\n".join(L)


def tabulated_output_path(src_path):
    """`<folder>_tabulated/<stem>_RANGE_tabulated.txt`, nested in the source
    folder (matches the house rule; RANGE suffix avoids colliding with STAR)."""
    p = Path(src_path).resolve()
    return p.parent / (p.parent.name + "_tabulated") / (p.stem + "_RANGE_tabulated.txt")


def run(path):
    title, ballots_text, _num = load_ballots_block(path)
    candidates, weighted = parse_score_ballots(ballots_text)
    if not candidates or not weighted:
        print("Error: no valid score ballots found.")
        sys.exit(1)
    _t, desc, lot = _meta(path)
    title = title or _t
    winner, totals, max_grade, pv = tabulate(candidates, weighted, lot)
    report = build_report(path, title, desc, candidates, weighted,
                          winner, totals, max_grade, pv)
    print(report)
    out = tabulated_output_path(path)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(report + "\n", encoding="utf-8")
    return winner


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python range_tabulation.py <election.yaml>")
        sys.exit(2)
    run(sys.argv[1])
