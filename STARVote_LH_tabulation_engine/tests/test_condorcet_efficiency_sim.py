"""Guards the Condorcet-efficiency simulation's harness.

The numbers published in 00_start_here/topics/condorcet/condorcet_efficiency_measured.md
are only worth anything if the harness is sound, and the harness has exactly one
self-evident check: **Ranked Robin (Copeland) is Condorcet-efficient by construction, so
its column must read 100.0%.** Any cell below that means the pairwise code and the method
code disagree, and every other number in the run is suspect.

These tests are cheap on purpose — they lock the invariants, not the published figures
(which are seeded and reproducible from the script itself).
"""
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[2]
SIM_DIR = REPO / "06_Other" / "simulations"

np = pytest.importorskip("numpy", reason="the simulations need numpy")

if str(SIM_DIR) not in sys.path:
    sys.path.insert(0, str(SIM_DIR))

ces = pytest.importorskip(
    "condorcet_efficiency_simulation", reason="simulation script not importable"
)


def test_ranked_robin_control_is_exactly_100_percent():
    """The control column. If this ever drops below 1.0 the whole sweep is void."""
    rng = np.random.default_rng(20260727)
    for model, C, V in [("noise", 3, 51), ("spatial2d", 5, 25), ("faction2d", 7, 51)]:
        _, eff, _ = ces.run_cell(rng, model, V, C, 200, 4)
        assert eff["RankedRobin"] == 1.0, (
            f"Ranked Robin scored {eff['RankedRobin']:.4f} on {model} C={C} V={V}; "
            "Copeland is Condorcet-efficient by construction, so this means the "
            "pairwise code and the method code disagree."
        )


def test_center_squeeze_known_answers():
    """The textbook squeeze: B is the CW; STAR/Score/RR elect them, IRV/Plurality don't."""
    util = ces._center_squeeze()
    scores = ces.scores_from_util(util)
    cw = ces.condorcet_winner(util)
    assert cw == 1, "B (index 1) is the Condorcet winner of the squeeze profile"

    won = ces.winners(util, scores, 4)
    assert won["RankedRobin"] == cw
    assert won["STAR"] == cw
    assert won["Score"] == cw
    assert won["RCV-IRV"] != cw, "IRV eliminates the centrist — that is the squeeze"
    assert won["Plurality"] != cw


def test_cycles_are_excluded_from_the_denominator():
    """A cycle has no CW, so it must not count against any method.

    This is the definitional trap the page is careful about: folding cycles in would
    measure the electorate, not the method.
    """
    rng = np.random.default_rng(11)
    cw_rate, eff, _ = ces.run_cell(rng, "noise", 51, 7, 300, 4)
    assert 0.0 < cw_rate < 1.0, "impartial culture at 7 candidates should produce cycles"
    # Every method's efficiency is a rate over CW-elections only, so all stay in [0, 1]
    # and the control stays pinned at 1.0 despite a third of elections being cycles.
    assert eff["RankedRobin"] == 1.0
    assert all(0.0 <= v <= 1.0 for v in eff.values())


def test_star_finalists_matches_the_engine_faithful_winner():
    """The mechanism split is only meaningful if the finalists are STAR's real ones.

    star_finalists() must always contain the winner star_winner() returns — an
    argsort shortcut breaks exactly this when the score round ties for second.
    """
    rng = np.random.default_rng(4242)
    for _ in range(400):
        util = ces.gen(rng, "noise", 15, 5)      # small + noisy = tie-heavy on purpose
        scores = ces.scores_from_util(util)
        assert ces.star_winner(scores) in ces.star_finalists(scores)


def test_selftest_passes():
    """The script's own known-answer suite, run end to end."""
    assert ces.selftest() == 0
