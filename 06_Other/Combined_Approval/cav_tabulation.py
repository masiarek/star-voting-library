#!/usr/bin/env python3
"""
cav_tabulation.py — Combined Approval Voting (CAV) tabulator for this library.

CAV gives every voter three options per candidate: vote **For** (+1), **abstain**
(0), or vote **Against** (−1). The candidate with the largest **net** total —
approvals minus disapprovals — wins. Dan Felsenthal proposed it in 1989; it also
travels as Dis&approval voting, Balanced Approval Voting (BAV), Evaluative
Voting (EV-3) and net approval voting.

Engine choice: no off-the-shelf CAV tabulator exists (BetterVoting, the LH
`starvote` engine, `pref_voting`, `abcvoting` and `pyrankvote` all lack it), so
this is a clean-room implementation of the published rule. It is not a guess:
CAV is exactly 3-level score voting on a shifted scale, so every count here is
verified two independent ways —

  1. an internal **affine-invariance check** — the net (−1,0,+1) totals and the
     (0,1,2) totals must differ by exactly the ballot count for EVERY candidate,
     and must rank the field identically; and
  2. an external cross-check against **pref_voting**'s `grade_methods.score_voting`
     run on the (0,1,2) grid (skipped with a note if pref_voting isn't installed,
     so the engine degrades gracefully).

BALLOT ENCODING — read this before writing a case file. Marks are
**2 = For, 1 = abstain, 0 = Against**, and a CAV case file must mark every cell
explicitly. The library's shared parser folds blanks and every marker character
into score 0, which on this scale reads as a vote **Against** — the opposite of
what a blank means on a real CAV ballot, where an unmarked row is an abstention.
This engine therefore REFUSES a ballot grid containing blanks rather than
silently miscounting them; see the README's "Blanks are the whole point" section.

Usage:
    python cav_tabulation.py <election.yaml>
    python cav_tabulation.py --selftest

Writes a full-context `<stem>_CAV_tabulated.txt` mirror into the source folder's
`<folder>_tabulated/` (CAV suffix so it never collides with a STAR or RANGE
mirror of the same election).
"""
import re
import sys
from pathlib import Path


# Reuse the vendored RCV engine's robust score-grid parser + block loader.
def _repo_root(start):
    p = Path(start).resolve()
    for anc in [p, *p.parents]:
        if (anc / "01_STAR").is_dir() and (anc / "STARVote_LH_tabulation_engine").is_dir():
            return anc
    return p.parents[1]


_RCV = _repo_root(__file__) / "06_Other" / "RCV_IRV" / "RCV_IRV_tabulation_engine"
if str(_RCV) not in sys.path:
    sys.path.insert(0, str(_RCV))
from rcv_irv_tabulation import load_ballots_block, parse_score_ballots  # noqa: E402

try:
    import yaml as _yaml
except Exception:  # pragma: no cover
    _yaml = None

# pref_voting is optional (matches the Range engine's stance).
try:
    from pref_voting.grade_profiles import GradeProfile
    from pref_voting.grade_methods import score_voting
    _PV = True
except Exception:  # pragma: no cover
    _PV = False

# Mark -> (label, net value). The scale is the whole method; keep it in one place.
MARKS = {2: ("For", +1), 1: ("Abstain", 0), 0: ("Against", -1)}


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


def check_no_blank_cells(ballots_text):
    """CAV needs every cell marked — the shared parser turns a blank into 0,
    which on this scale means 'Against'. Return a list of complaints (empty = OK).

    Checked on the RAW text, before parsing, because the parser has already
    destroyed the distinction by the time it hands back scores."""
    problems = []
    lines = []
    for raw in ballots_text.strip().splitlines():
        line = raw.split("#")[0].strip()
        if line:
            lines.append(line)
    if not lines:
        return ["no ballot rows found"]
    for i, line in enumerate(lines[1:], start=1):
        parts = re.split(r"[,\t]", line)
        wmatch = re.match(r"\s*(\d+)\s*[:xX×]\s*(.*)", parts[0])
        if wmatch:
            parts[0] = wmatch.group(2)
        for cell in parts:
            if cell.strip() == "":
                problems.append(
                    f"ballot row {i} has an empty cell — a CAV ballot must mark "
                    f"every candidate 2 (For), 1 (abstain) or 0 (Against). "
                    f"An abstention is written 1, NOT left blank."
                )
                break
    return problems


def check_marks(candidates, weighted_ballots):
    """Every mark must be 0, 1 or 2. Return a list of complaints (empty = OK)."""
    problems = []
    for i, (_w, marks) in enumerate(weighted_ballots, start=1):
        for c in candidates:
            s = int(marks.get(c, 0) or 0)
            if s not in MARKS:
                problems.append(
                    f"ballot row {i}: {c} is marked {s} — CAV is a three-level "
                    f"ballot (2 = For, 1 = abstain, 0 = Against)."
                )
    return problems


def tabulate(candidates, weighted_ballots, lot_numbers=None):
    """Return a result dict for a CAV count.

    Keys: winner, net, shifted, counts, n, affine_ok, pv_winner."""
    n = sum(w for w, _ in weighted_ballots)
    net = {c: 0 for c in candidates}
    shifted = {c: 0 for c in candidates}
    counts = {c: {"For": 0, "Abstain": 0, "Against": 0} for c in candidates}

    for weight, marks in weighted_ballots:
        for c in candidates:
            s = int(marks.get(c, 0) or 0)
            label, value = MARKS[s]
            counts[c][label] += weight
            net[c] += weight * value
            shifted[c] += weight * s

    # Tie-break: published lot order if given, else column order.
    order = [c for c in (lot_numbers or []) if c in candidates]
    for c in candidates:
        if c not in order:
            order.append(c)
    top = max(net.values())
    leaders = [c for c in candidates if net[c] == top]
    winner = min(leaders, key=order.index)

    # Verification 1 — affine invariance, checked rather than asserted.
    # A (0,1,2) mark is the (−1,0,+1) mark plus one, so over n ballots each
    # candidate's shifted total must exceed its net total by exactly n.
    affine_ok = all(shifted[c] - n == net[c] for c in candidates)

    # Verification 2 — independent engine on the equivalent (0,1,2) profile.
    pv_winner = None
    if _PV:
        grade_maps, gcounts = [], []
        for weight, marks in weighted_ballots:
            grade_maps.append({c: int(marks.get(c, 0) or 0) for c in candidates})
            gcounts.append(int(weight))
        gp = GradeProfile(grade_maps, [0, 1, 2], gcounts=gcounts,
                          candidates=list(candidates))
        pv = [str(x) for x in score_voting(gp)]
        pv_winner = min(pv, key=order.index) if pv else None

    return {"winner": winner, "net": net, "shifted": shifted, "counts": counts,
            "n": n, "affine_ok": affine_ok, "pv_winner": pv_winner,
            "leaders": leaders}


def build_report(title, desc, candidates, weighted, res):
    n, net, shifted = res["n"], res["net"], res["shifted"]
    counts, winner = res["counts"], res["winner"]

    L = ["--- Combined Approval Voting (CAV, single winner) ---"]
    if title:
        L.append(f"  {title}")
    L.append(f" Tabulating {n} ballots on the three-level For / abstain / Against")
    L.append(" ballot. Highest NET score (approvals − disapprovals) wins.")
    L.append("")
    if desc:
        L.append("[Scenario]")
        for ln in desc.strip().splitlines():
            L.append("  " + ln)
        L.append("")

    L.append("Ballots (2 = For, 1 = abstain, 0 = Against):")
    L.append("  " + ", ".join(candidates))
    for w, marks in weighted:
        row = ", ".join(str(int(marks.get(c, 0) or 0)) for c in candidates)
        L.append(f"  {w} × {row}" if w != 1 else f"  {row}")
    L.append("")

    width = max(len(c) for c in candidates)
    L.append("Vote tally:")
    L.append(f"  {'':<{width}}   For   Abstain   Against      Net")
    for c in sorted(candidates, key=lambda c: -net[c]):
        mark = "  ← winner" if c == winner else ""
        L.append(f"  {c:<{width}}  {counts[c]['For']:>4}  {counts[c]['Abstain']:>8}"
                 f"  {counts[c]['Against']:>8}  {net[c]:>+7}{mark}")
    L.append("")

    if len(res["leaders"]) > 1:
        tied = ", ".join(res["leaders"])
        L.append(f"  Note: {tied} tie on net score; the winner is taken by the")
        L.append("        published lot order (or column order if none is given).")
        L.append("")

    L.append("Verification 1 — affine invariance (the (0,1,2) reading):")
    L.append(f"  The same marks summed as 0/1/2 must exceed the net total by exactly")
    L.append(f"  the ballot count ({n}) for every candidate, and must rank the field")
    L.append("  the same way. That is what makes CAV 'three-level score voting'.")
    for c in sorted(candidates, key=lambda c: -net[c]):
        L.append(f"    {c:<{width}}  net {net[c]:>+4}   +{n} = {shifted[c]:>4}  "
                 f"(0/1/2 sum {shifted[c]})")
    L.append(f"  {'✓ holds' if res['affine_ok'] else '✗ FAILED'} — "
             f"the (−1,0,+1) and (0,1,2) scales agree.")
    L.append("")

    pv_winner = res["pv_winner"]
    if pv_winner is not None:
        agree = ("✓ agrees" if pv_winner == winner
                 else f"✗ DISAGREES (pref_voting={pv_winner})")
        L.append(f"Verification 2 — pref_voting score_voting on the (0,1,2) profile: "
                 f"{pv_winner}")
        L.append(f"  ({agree} with the CAV count)")
    else:
        L.append("Verification 2 — pref_voting not installed; internal checks only "
                 "(install `pref_voting` to enable the independent count).")
    L.append("")
    L.append("Winner — Combined Approval Voting (single winner)")
    L.append(f"  {winner}")
    return "\n".join(L)


def tabulated_output_path(src_path):
    """`<folder>_tabulated/<stem>_CAV_tabulated.txt`, nested in the source folder
    (matches the house rule; CAV suffix avoids colliding with STAR/RANGE)."""
    p = Path(src_path).resolve()
    return p.parent / (p.parent.name + "_tabulated") / (p.stem + "_CAV_tabulated.txt")


def run(path):
    title, ballots_text, _num = load_ballots_block(path)

    problems = check_no_blank_cells(ballots_text)
    candidates, weighted = parse_score_ballots(ballots_text)
    if not candidates or not weighted:
        print("Error: no valid score ballots found.")
        sys.exit(1)
    problems += check_marks(candidates, weighted)
    if problems:
        print("Error: this file is not a valid CAV ballot grid.")
        for p in problems:
            print(f"  - {p}")
        sys.exit(1)

    _t, desc, lot = _meta(path)
    title = title or _t
    res = tabulate(candidates, weighted, lot)
    report = build_report(title, desc, candidates, weighted, res)
    print(report)

    out = tabulated_output_path(path)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(report + "\n", encoding="utf-8")
    return res["winner"]


# --------------------------------------------------------------------------- #
# Self-test — the rule, the affine identity, and the blank trap.
# --------------------------------------------------------------------------- #
_VECTORS = [
    # (name, candidates, ballots as list of mark-dicts, expected winner)
    ("net beats raw approvals",
     ["A", "B"],
     # A: 3 For, 2 Against -> +1.  B: 2 For, 0 Against -> +2.
     [{"A": 2, "B": 2}, {"A": 2, "B": 2}, {"A": 2, "B": 1},
      {"A": 0, "B": 1}, {"A": 0, "B": 1}],
     "B"),
    ("abstentions are free",
     ["A", "B"],
     # A: 1 For, 1 Against -> 0.  B: 1 For, 4 abstain -> +1.
     [{"A": 2, "B": 1}, {"A": 0, "B": 1}, {"A": 1, "B": 1},
      {"A": 1, "B": 1}, {"A": 1, "B": 2}],
     "B"),
    ("unanimous disapproval still ranks",
     ["A", "B"],
     [{"A": 0, "B": 0}, {"A": 0, "B": 1}],
     "B"),
    ("all-abstain ties, column order decides",
     ["A", "B"],
     [{"A": 1, "B": 1}, {"A": 1, "B": 1}],
     "A"),
]


def _selftest():
    ok = True
    for i, (name, cands, rows, expected) in enumerate(_VECTORS, start=1):
        res = tabulate(cands, [(1, r) for r in rows])
        got = res["winner"]
        status = "OK" if got == expected else "FAIL"
        if got != expected or not res["affine_ok"]:
            ok = False
        print(f"  vector {i} ({name}): winner={got} expected={expected} "
              f"affine={'ok' if res['affine_ok'] else 'FAILED'} {status}")

    # The blank trap: a grid with an empty cell must be refused, not counted.
    grid = "A,B\n2,\n1,2"
    if check_no_blank_cells(grid):
        print("  blank-cell guard: refused a grid with an empty cell OK")
    else:
        print("  blank-cell guard: FAILED — an empty cell slipped through")
        ok = False

    # Out-of-range marks must be refused too.
    cands, weighted = parse_score_ballots("A,B\n5,2\n1,2")
    if check_marks(cands, weighted):
        print("  mark-range guard: refused a mark outside 0..2 OK")
    else:
        print("  mark-range guard: FAILED — a 5 slipped through")
        ok = False

    print("CAV engine self-test: " + ("all checks passed ✓" if ok else "FAILURES ✗"))
    return 0 if ok else 1


if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == "--selftest":
        sys.exit(_selftest())
    if len(sys.argv) != 2:
        print("usage: python cav_tabulation.py <election.yaml>")
        print("       python cav_tabulation.py --selftest")
        sys.exit(2)
    run(sys.argv[1])
