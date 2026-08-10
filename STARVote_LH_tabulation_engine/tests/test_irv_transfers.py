"""
test_irv_transfers.py
=====================
Guards the transfer / inactive-ballot block the RCV-IRV path appends to
`_tabulated` mirrors.

WHY THE BLOCK EXISTS. pyrankvote renders each round as a column of totals and
nothing else, so the two numbers every exhausted-ballot and center-squeeze page
in this repo argues about were never printed by any engine here: where a
transferred vote came FROM, and how many ballots have stopped counting (which is
what makes IRV's "majority" a majority of a shrinking denominator). The Sankey
art shows the first, but only on a generated page — a mirror is plain text.

House contract, same as `show_smith_set`: OFF in the on-screen echo, ALWAYS ON in
the mirror, and on screen under `--full`.

TWO THINGS THIS FILE IS REALLY PROTECTING
-----------------------------------------
1. **The final round transfers nothing.** pyrankvote marks the runner-up
   "Rejected" in its last table, but the count has already stopped — printing a
   transfer there would invent a round that never happened, and would erase the
   nonexhausted-untransferred case the block exists to expose. The first draft
   did exactly that (it reported "Right eliminated with 9 → Left 9" for an
   election that ended 18–9).
2. **The eliminations are read back from pyrankvote, never recomputed.** If this
   block worked out its own eliminations it could contradict the table directly
   above it whenever an elimination tie is resolved by the second-choices ladder.

The numbers asserted below are cross-checked against RCTab 2.0.0 — the federally
tested, state-certified tabulator — in
`tools_adam/rctab_tabulation_engine/rctab_cases/`: it reports the same transfers
and the same shrinking thresholds (26 → 26 → 22 → 15 on the ceiling case).
"""
import subprocess
import sys
from pathlib import Path

ENGINE_DIR = Path(__file__).resolve().parent.parent
REPO_ROOT = ENGINE_DIR.parent
WRAPPER = ENGINE_DIR / "starvote_larry_hastings.py"

HEADER = "--- Transfers and inactive ballots (what the round tables leave out) ---"

SQUEEZE = REPO_ROOT / "method_comparisons/center_squeeze/cases/center_squeeze_irv.yaml"
CEILING = (REPO_ROOT / "method_comparisons/paradoxes_and_whoops/cases"
           / "bv2183_dfw8rj_forced_exhaustion_ceiling.yaml")
STV = REPO_ROOT / "06_Other/STV/cases/03a_stv_3seats.yaml"


def _run(path, *args):
    return subprocess.run([sys.executable, str(WRAPPER), str(path), *args],
                          capture_output=True, text=True, cwd=str(ENGINE_DIR))


def _mirror(path):
    # The engine derives the mirror from the yaml's OWN parent, so it nests
    # inside it: `<dir>/<dir>_tabulated/<stem>_tabulated.txt`.
    d = path.parent
    return (d / (d.name + "_tabulated")
            / (path.stem + "_tabulated.txt")).read_text(encoding="utf-8")


def test_block_is_mirror_only_and_full_puts_it_on_screen():
    assert HEADER not in _run(SQUEEZE).stdout, "on-screen echo must stay minimal"
    assert HEADER in _mirror(SQUEEZE), "the mirror always renders maximum info"
    assert HEADER in _run(SQUEEZE, "--full").stdout


def test_transfer_destinations_are_named():
    text = _mirror(SQUEEZE)
    assert "Center eliminated with 6:" in text
    assert "→ Left" in text
    # 27 ballots, all three ranked: nothing exhausts, and the block says so.
    assert "Inactive ballots at the final round: 0 of 27 (0.0%)." in text


def test_final_round_transfers_nothing_and_names_the_unread_ballots():
    """The runner-up is 'Rejected' in pyrankvote's last table but nothing moved."""
    text = _mirror(SQUEEZE)
    final = text.split("FINAL ROUND", 1)[1]
    assert "Right eliminated" not in final, \
        "the final round must not invent a transfer out of the runner-up"
    assert "Never exhausted, never transferred:" in final
    assert "9 ballots held by Right carried a lower ranking that was never read" in final


def test_shrinking_denominator_is_computed_not_asserted():
    text = _mirror(CEILING)
    # RCTab agrees round for round, including these thresholds.
    for line in ["ROUND 3 — 42 of 50 ballots still active (8 inactive); majority = 22",
                 "FINAL ROUND — 29 of 50 ballots still active (21 inactive); majority = 15"]:
        assert line in text, line
    assert "Inactive ballots at the final round: 21 of 50 (42.0%)." in text
    assert "still active but only 30.0% of all 50 cast" in text


def test_singular_ballot_is_not_pluralized():
    text = _mirror(REPO_ROOT / "06_Other/RCV_IRV/cases/batch_all_out_cycle_c3_b3.yaml")
    assert "1 ballot held by" in text and "1 ballots held by" not in text


def test_stv_gets_no_block():
    """Surplus transfers are fractional and are NOT modelled — better silent."""
    assert HEADER not in _mirror(STV)


def test_a_count_with_no_eliminations_gets_no_block():
    """Two candidates, or a first-round majority: there is nothing to report."""
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "rcv_irv_tabulation",
        REPO_ROOT / "06_Other/RCV_IRV/RCV_IRV_tabulation_engine/rcv_irv_tabulation.py")
    mod = importlib.util.module_from_spec(spec)
    sys.modules["rcv_irv_tabulation"] = mod
    spec.loader.exec_module(mod)

    import pyrankvote
    from pyrankvote import Ballot, Candidate
    a, b = Candidate("A"), Candidate("B")
    ballots = [Ballot(ranked_candidates=[a, b])] * 3 + \
              [Ballot(ranked_candidates=[b, a])] * 2
    result = pyrankvote.instant_runoff_voting([a, b], ballots)
    rows = [(3, ["A", "B"]), (2, ["B", "A"])]
    assert mod.build_transfer_block(rows, result, 5) is None
