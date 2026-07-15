"""
test_approval_artifact_note.py
==============================
Locks the honest-conversion note under the [Divergence from STAR] block's
Approval line. That line converts 0..5 score ballots to Approval with a
3+ stars threshold (APPROVAL_STARS_MIN), so on low-scoring profiles the
"Approval winner" can be decided by the conversion itself rather than the
voters — e.g. the Brams grading-paradox cases (grades {0..2}) give every
candidate 0 approvals and the printed name is just the left-most-column
priority tie-break. The note says so inline, in three variants:

  * ZERO      — no ballot scores anyone >= 3: every candidate has 0 approvals,
                the "winner" is purely the candidate-priority tie-break;
  * TIE       — several candidates tie for most approvals: the single printed
                name was chosen by priority order;
  * MOSTLY-EMPTY — a unique top, but at least half the ballots convert to
                empty Approval ballots, so the result rests on the remainder.

A genuine Approval divergence (unique top, ballots mostly non-empty) must NOT
carry the note. Wording is locked here together with the engine text — change
them together.
"""

import subprocess
import sys
from pathlib import Path

ENGINE_DIR = Path(__file__).resolve().parent.parent
WRAPPER = ENGINE_DIR / "starvote_larry_hastings.py"

THRESHOLD_LEAD = ("Note: the Approval line converts score ballots with a "
                  "3+ stars approval threshold.")

# Grades {0..2} only (Brams ex3 shape): A tops the scores 4-3, B wins the
# runoff 3-2, and NOBODY clears the 3+ approval threshold.
BALLOTS_ZERO = "  A,B\n  2,0\n  2,0\n  0,1\n  0,1\n  0,1\n"
NOTE_ZERO = (
    f"{THRESHOLD_LEAD} No ballot here scores any candidate 3 or higher, so "
    "every candidate has 0 approvals — the printed Approval winner (A) is "
    "just the candidate-priority tie-break, an artifact of the conversion, "
    "not an Approval verdict."
)

# Brams grading-paradox shape: one approval each (b1 approves A, b2 approves
# B and C), so A, B, C tie 1-1-1 and priority picks A; STAR elects B.
BALLOTS_TIE = "  A,B,C\n  3,0,0\n  2,3,3\n  1,2,1\n"
NOTE_TIE = (
    f"{THRESHOLD_LEAD} A, B, C tie at 1 approval each, so the printed "
    "Approval winner (A) was decided by candidate priority order, not by "
    "the voters."
)

# Unique approval top (C, 2 approvals) but 3 of 5 ballots approve nobody;
# STAR elects A (runoff 3-2 over C).
BALLOTS_EMPTY = "  A,B,C\n  0,0,3\n  0,0,4\n  2,1,0\n  2,1,0\n  2,1,0\n"
NOTE_EMPTY = (
    f"{THRESHOLD_LEAD} 3 of 5 ballots score no one that high and convert to "
    "empty Approval ballots, so the Approval result rests on the other 2 "
    "ballots."
)

# Control — a GENUINE Approval divergence: A has a unique 3-approval top and
# no ballot converts empty (STAR elects B via the runoff). No note.
BALLOTS_GENUINE = "  A,B,C\n  4,5,0\n  4,5,0\n  5,0,0\n"


def _run(tmp_path, name, ballots):
    d = tmp_path / name
    d.mkdir()
    p = d / "case.yaml"
    p.write_text(f"voting_method: STAR\nnum_winners: 1\nballots: |-\n{ballots}")
    proc = subprocess.run(
        [sys.executable, str(WRAPPER), str(p)],
        cwd=str(ENGINE_DIR), capture_output=True, text=True,
    )
    assert proc.returncode == 0, proc.stdout + proc.stderr
    # Normalize the textwrap'd note back to one line for exact matching.
    return " ".join(proc.stdout.split())


def test_zero_approvals_note(tmp_path):
    out = _run(tmp_path, "zero", BALLOTS_ZERO)
    assert "Approval = A" in out and "STAR = B" in out
    assert NOTE_ZERO in out


def test_top_tie_note(tmp_path):
    out = _run(tmp_path, "tie", BALLOTS_TIE)
    assert "Approval = A" in out and "STAR = B" in out
    assert NOTE_TIE in out


def test_mostly_empty_note(tmp_path):
    out = _run(tmp_path, "empty", BALLOTS_EMPTY)
    assert "Approval = C" in out and "STAR = A" in out
    assert NOTE_EMPTY in out


def test_genuine_divergence_has_no_note(tmp_path):
    out = _run(tmp_path, "genuine", BALLOTS_GENUINE)
    assert "Approval = A" in out and "STAR = B" in out
    assert "Note: the Approval line converts" not in out
