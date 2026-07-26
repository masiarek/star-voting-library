"""
test_approval_threshold.py
==========================
Guards the Approval cross-check used by the STAR report's `[Divergence from
STAR]` block and its Condorcet-loser audit.

The bug this locks down: the comparator hard-coded "a score of 3, 4 or 5 is an
approval" while the real Approval tabulator counts ANY non-zero score. On a
ballot whose top score was below 3 the bar was unreachable, so every candidate
scored zero approvals and the empty tally fell through to priority order —
printing the first CSV column as a confident (wrong) winner, and even accusing
it of having "elected the Condorcet loser".

Three properties are locked here:

  1. the threshold fits the ballot's scale (and is never above a reachable
     score), while a 0..5 ballot still reads at the familiar 3;
  2. on dichotomous 0/1 ballots the cross-check and `tabulate_approval` agree
     BY CONSTRUCTION — that tabulator accepts only 0/1 rows, so this is the one
     input where the two rules are directly comparable, and they must not part;
  3. an uninformative tally (nobody approved, or everyone tied) never
     manufactures a divergence from STAR.
"""
import subprocess
import sys
from pathlib import Path

ENGINE_DIR = Path(__file__).resolve().parent.parent
WRAPPER = ENGINE_DIR / "starvote_larry_hastings.py"
sys.path.insert(0, str(ENGINE_DIR))

import starvote_larry_hastings as lh  # noqa: E402


def _ballots(rows):
    candidates, ballots, _ = lh.parse_ballots_from_string(rows)
    return candidates, ballots


# --------------------------------------------------------------------------- #
# 1. the threshold fits the ballot's scale
# --------------------------------------------------------------------------- #

def test_threshold_scales_to_the_ballot():
    # (top score actually used on the ballot, expected approval threshold)
    cases = [
        (5, 3),    # the usual 0..5 STAR ballot — the familiar "3+ stars"
        (4, 3),    # a 0..5 ballot where nobody used the top rung: STILL 3
        (3, 3),    # ditto
        (2, 2),    # a compressed scale: only the top grade clears
        (1, 1),    # approval-style 0/1 ballots: any mark approves
        (10, 5),   # a wider range ballot — 3 would be a very low bar
    ]
    for top_score, expected in cases:
        got = lh.approval_threshold(["A"], [{"A": top_score}])
        assert got == expected, (
            f"top score {top_score}: threshold {got}, expected {expected}")


def test_threshold_is_always_reachable():
    """The bug in one line: a bar nobody can clear is not a bar."""
    for top_score in range(0, 12):
        thr = lh.approval_threshold(["A"], [{"A": top_score}])
        assert thr >= 1, "a score of 0 must never count as an approval"
        if top_score >= 1:
            assert thr <= top_score, (
                f"threshold {thr} is above every score on a 0..{top_score} "
                f"ballot — the tally can only come out empty")


# --------------------------------------------------------------------------- #
# 2. on 0/1 ballots the cross-check agrees with the real Approval tabulator
# --------------------------------------------------------------------------- #

def test_dichotomous_ballots_match_the_approval_tabulator(tmp_path):
    """`tabulate_approval` takes only 0/1 rows, so that's where the two rules
    must agree. Counting the marks gives Dana; the old fixed threshold of 3
    approved nobody and named Ann, the first column."""
    rows = ("Ann,Bram,Cleo,Dana\n"
            "0,0,1,1\n"
            "1,0,0,1\n"
            "1,1,0,1\n"
            "0,0,0,0\n"
            "1,1,1,1\n")
    candidates, ballots = _ballots(rows)

    counts, threshold = lh.approval_counts(candidates, ballots)
    assert threshold == 1
    assert counts == {"Ann": 3, "Bram": 2, "Cleo": 2, "Dana": 4}
    assert lh.approval_winner(candidates, ballots, candidates) == "Dana"

    # ...and the real tabulator, run end to end, elects the same candidate.
    src = tmp_path / "dichotomous.yaml"
    src.write_text("voting_method: Approval\nnum_winners: 1\nballots: |-\n"
                   + "".join(f"  {line}\n" for line in rows.strip().splitlines())
                   + "expected_winners:\n  - Dana\n")
    r = subprocess.run([sys.executable, str(WRAPPER), str(src)],
                       capture_output=True, text=True, cwd=str(ENGINE_DIR))
    assert r.returncode == 0, r.stderr or r.stdout
    assert "Dana" in r.stdout.split("Winner")[-1]


# --------------------------------------------------------------------------- #
# 3. an uninformative tally never manufactures a result
# --------------------------------------------------------------------------- #

def test_all_zero_tally_has_no_winner():
    """Nobody approved anyone: there is no winner to report, and naming one
    would just be reporting whichever candidate sits in the first column."""
    candidates, ballots = _ballots("Ann,Bram,Cleo\n0,0,0\n0,0,0\n")
    winner, tied, counts, _ = lh.approval_top(candidates, ballots, candidates)
    assert winner is None
    assert set(counts.values()) == {0}
    assert lh.approval_winner(candidates, ballots, candidates) is None


def test_tied_tally_is_not_a_divergence_from_star(tmp_path):
    """Approval-style ballots plus one all-fives ballot: at a 0..5 reading the
    approval tally ties every candidate at 1, so Approval is indifferent — it
    must not be printed as disagreeing with STAR. (This is the live case that
    used to print a confident `Approval = A`.)"""
    src = tmp_path / "tied_approval.yaml"
    src.write_text(
        "voting_method: STAR\n"
        "num_winners: 1\n"
        "ballots: |-\n"
        "  A,B,C,D\n"
        "  -,-,1,1\n"
        "  1,0,0,1\n"
        "  1,1,0,1\n"
        "  0,0,0,0\n"
        "  5,5,5,5\n"
        "expected_winners:\n"
        "  - D\n"
    )
    r = subprocess.run([sys.executable, str(WRAPPER), str(src)],
                       capture_output=True, text=True, cwd=str(ENGINE_DIR))
    assert r.returncode == 0, r.stderr or r.stdout
    assert "Approval" not in r.stdout.split("[Divergence from STAR]")[-1][:400], (
        "Approval tied every candidate here, so it cannot be reported as "
        "differing from STAR:\n" + r.stdout)


def test_genuine_approval_divergence_still_prints(tmp_path):
    """The suppression above must not silence a real disagreement: here STAR
    elects Cleo while Approval clearly prefers Bram."""
    src = tmp_path / "real_divergence.yaml"
    src.write_text(
        "voting_method: STAR\n"
        "num_winners: 1\n"
        "ballots: |-\n"
        "  Ann,Bram,Cleo\n"
        "  0,3,5\n"
        "  0,3,5\n"
        "  0,3,5\n"
        "  5,3,0\n"
        "  5,3,0\n"
        "expected_winners:\n"
        "  - Cleo\n"
    )
    r = subprocess.run([sys.executable, str(WRAPPER), str(src)],
                       capture_output=True, text=True, cwd=str(ENGINE_DIR))
    assert r.returncode == 0, r.stderr or r.stdout
    candidates, ballots = _ballots(
        "Ann,Bram,Cleo\n0,3,5\n0,3,5\n0,3,5\n5,3,0\n5,3,0\n")
    assert lh.approval_winner(candidates, ballots, candidates) == "Bram"
    assert "[Divergence from STAR]" in r.stdout
    assert "Approval" in r.stdout.split("[Divergence from STAR]")[-1][:400]
