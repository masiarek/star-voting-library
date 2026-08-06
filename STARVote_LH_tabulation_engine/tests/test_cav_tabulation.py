"""
test_cav_tabulation.py
======================
Guards the Combined Approval Voting engine (06_Other/Combined_Approval/
cav_tabulation.py) — a clean-room implementation of Felsenthal's 1989 rule,
since no off-the-shelf CAV tabulator exists.

Three things are worth guarding, and they are the three the engine can get
subtly wrong without anyone noticing:

1. the count itself (net = approvals − disapprovals);
2. the **blank trap** — the library's shared parser folds a blank into score 0,
   which on the CAV scale means "Against". A CAV file must therefore mark every
   cell, and the engine must REFUSE a grid with blanks rather than miscount it;
3. the **blank-is-middle vs blank-is-bottom** contrast that the teaching case
   rests on — the same twelve voters must reverse end-to-end between the CAV
   count and the ordinary score count.

Runs the engine via subprocess like the other engine tests; pref_voting is an
optional cross-check, so the winner is always computable from the stdlib.
"""
import subprocess
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
CAV = REPO_ROOT / "06_Other" / "Combined_Approval" / "cav_tabulation.py"
RANGE = REPO_ROOT / "06_Other" / "Range" / "Range_tabulation_engine" / "range_tabulation.py"
CASES_DIR = REPO_ROOT / "06_Other" / "Combined_Approval" / "cases"


def _winner(stdout, lead):
    lines = stdout.splitlines()
    for i, ln in enumerate(lines):
        if ln.startswith(lead):
            for nxt in lines[i + 1:]:
                if nxt.strip():
                    return nxt.strip()
    return None


def _run(engine, path, *args):
    return subprocess.run([sys.executable, str(engine), str(path), *args],
                          capture_output=True, text=True)


def test_engine_selftest_passes():
    """The engine's own vectors, including both input guards."""
    r = _run(CAV, "--selftest")
    assert r.returncode == 0, r.stderr or r.stdout
    assert "all checks passed" in r.stdout, r.stdout


def test_cav_elects_the_unopposed_newcomer():
    """Cleo: 3 For, 0 Against, 9 abstentions -> +3, ahead of Byron +1, Alma -1.

    The abstentions are free; that is the method."""
    r = _run(CAV, CASES_DIR / "cav_library_board_c3_b12.yaml")
    assert r.returncode == 0, r.stderr or r.stdout
    assert _winner(r.stdout, "Winner — Combined Approval Voting") == "Cleo", r.stdout


def test_affine_invariance_check_holds():
    """The (-1,0,+1) and (0,1,2) readings must agree — checked, not asserted.

    This is what makes 'CAV is three-level score voting' a verified claim
    rather than a footnote."""
    r = _run(CAV, CASES_DIR / "cav_library_board_c3_b12.yaml")
    assert r.returncode == 0, r.stderr or r.stdout
    assert "✓ holds — the (−1,0,+1) and (0,1,2) scales agree." in r.stdout, r.stdout


def test_blank_cells_are_refused_not_miscounted():
    """A blank parses to 0, which on this scale reads as Against. The engine
    must refuse the file with a clear message and exit 1 — no traceback."""
    bad = CASES_DIR / "cases_tabulated" / "_tmp_blank_trap.yaml"
    bad.parent.mkdir(parents=True, exist_ok=True)
    bad.write_text(
        "election_title: blank trap\n"
        "voting_method: CAV\n"
        "ballots: |-\n"
        "  A,B\n"
        "  2,\n"
        "  1,2\n",
        encoding="utf-8")
    try:
        r = _run(CAV, bad)
        assert r.returncode == 1, f"expected exit 1, got {r.returncode}:\n{r.stdout}"
        assert "not a valid CAV ballot grid" in r.stdout, r.stdout
        assert "An abstention is written 1, NOT left blank" in r.stdout, r.stdout
        assert "Traceback" not in (r.stderr + r.stdout), r.stderr
    finally:
        bad.unlink(missing_ok=True)


def test_out_of_range_marks_are_refused():
    """CAV is a three-level ballot; a 5 is not a CAV mark."""
    bad = CASES_DIR / "cases_tabulated" / "_tmp_range_trap.yaml"
    bad.parent.mkdir(parents=True, exist_ok=True)
    bad.write_text(
        "election_title: range trap\n"
        "voting_method: CAV\n"
        "ballots: |-\n"
        "  A,B\n"
        "  5,2\n"
        "  1,2\n",
        encoding="utf-8")
    try:
        r = _run(CAV, bad)
        assert r.returncode == 1, f"expected exit 1, got {r.returncode}:\n{r.stdout}"
        assert "three-level ballot" in r.stdout, r.stdout
        assert "Traceback" not in (r.stderr + r.stdout), r.stderr
    finally:
        bad.unlink(missing_ok=True)


def test_blank_encoding_reverses_the_field():
    """The teaching claim, guarded end to end.

    Same twelve voters, same marks. Read a blank as the MIDDLE grade (CAV) and
    Cleo wins; read it as the BOTTOM grade (ordinary score ballot) and she comes
    last. If either engine's answer drifts, the lesson on the README is wrong."""
    cav = _run(CAV, CASES_DIR / "cav_library_board_c3_b12.yaml")
    rng = _run(RANGE, CASES_DIR / "cav_library_board_blank_is_zero_c3_b12.yaml")
    assert cav.returncode == 0, cav.stderr or cav.stdout
    assert rng.returncode == 0, rng.stderr or rng.stdout

    assert _winner(cav.stdout, "Winner — Combined Approval Voting") == "Cleo"
    assert _winner(rng.stdout, "Winner — Range") == "Byron"

    # ...and Cleo must be dead last on the blank-is-bottom count (6 < 8 < 10).
    totals = rng.stdout.split("Total score (sum of all grades):", 1)[1]
    order = [ln.split()[0] for ln in totals.splitlines() if ln.strip()][:3]
    assert order == ["Byron", "Alma", "Cleo"], f"unexpected score order: {order}"


def test_pref_voting_crosscheck_agrees_when_present():
    """When pref_voting is installed, its score_voting on the equivalent
    (0,1,2) profile must agree with the CAV count."""
    pytest.importorskip("pref_voting")
    r = _run(CAV, CASES_DIR / "cav_library_board_c3_b12.yaml")
    assert r.returncode == 0, r.stderr or r.stdout
    assert "✓ agrees with the CAV count" in r.stdout, (
        "pref_voting cross-check did not agree:\n" + r.stdout)
