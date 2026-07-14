"""
test_divergence_ties.py
=======================
Locks the tie-honesty rules of the [Divergence from STAR] block.

The block compares STAR against Choose-One (Plurality), RCV-IRV, Approval,
Ranked Robin (Copeland) and Condorcet. Each comparison method yields the SET
of candidates tied at its top; historically an exact tie was silently broken
by the priority/lot order (or pyrankvote's tie comparator) and printed as a
clean single winner — misleading for a teaching repo (e.g. a 1-1-1 three-way
first-choice tie printed as "Choose-One (Plurality) = Ann (differs from
STAR)").

Behaviour locked here:
  * an exact tie prints as a tie, listing the tied candidates:
        Choose-One (Plurality) = tie (Ann / Bob)   (differs from STAR)
  * a tie counts as a DIVERGENCE only when the STAR winner is NOT among the
    tied candidates;
  * a tie that INCLUDES the STAR winner never triggers the block, but when
    the block prints anyway (some other method genuinely differs) the tie is
    shown labeled "(tie — includes the STAR winner)" — a tie is never full
    agreement, and never sold as a different winner;
  * an exact tie at the RCV-IRV deciding round (equal final-round votes) is
    detected and printed as a tie, not as pyrankvote's comparator pick;
  * clean single-winner divergences print exactly as before.
"""

import subprocess
import sys
from pathlib import Path

ENGINE_DIR = Path(__file__).resolve().parent.parent
WRAPPER = ENGINE_DIR / "starvote_larry_hastings.py"
if str(ENGINE_DIR) not in sys.path:
    sys.path.insert(0, str(ENGINE_DIR))

import starvote_larry_hastings as w  # noqa: E402


def _run_cli(path):
    return subprocess.run(
        [sys.executable, str(WRAPPER), str(path)],
        cwd=str(ENGINE_DIR), capture_output=True, text=True,
    )


def _write(tmp_path, name, ballots):
    d = tmp_path / name
    d.mkdir()
    p = d / "case.yaml"
    rows = "".join(f"  {ln}\n" for ln in ballots.strip().splitlines())
    p.write_text(f"voting_method: STAR\nnum_winners: 1\nballots: |-\n{rows}")
    return p


CANDS = ["Ann", "Bob", "Cal"]

# STAR = Cal; first choices Ann 2 / Bob 2 / Cal 1 -> plurality tie (Ann/Bob)
# EXCLUDING the STAR winner; IRV genuinely elects Ann (Cal eliminated first).
TIE_EXCLUDES_STAR = """
Ann,Bob,Cal
5,0,4
5,0,4
0,5,4
0,5,4
1,0,5
"""

# STAR = Cal; first choices 1-1-1 -> plurality tie (Ann/Bob/Cal) INCLUDING the
# STAR winner; IRV, Approval, RR and Condorcet all elect Cal outright.
TIE_INCLUDES_STAR_ONLY = """
Ann,Bob,Cal
5,0,4
0,5,4
1,0,5
"""


# --- end-to-end: tie excluding the STAR winner is a printed divergence ------

def test_tie_excluding_star_prints_as_tie(tmp_path):
    proc = _run_cli(_write(tmp_path, "excl", TIE_EXCLUDES_STAR))
    assert proc.returncode == 0, proc.stdout + proc.stderr
    assert "[Divergence from STAR]" in proc.stdout
    assert ("Choose-One (Plurality) = tie (Ann / Bob)   (differs from STAR)"
            in proc.stdout), proc.stdout
    # The silently-broken single-name form must be gone.
    assert "Choose-One (Plurality) = Ann " not in proc.stdout, proc.stdout


# --- end-to-end: tie including the STAR winner alone never triggers ---------

def test_tie_including_star_does_not_trigger_block(tmp_path):
    proc = _run_cli(_write(tmp_path, "incl", TIE_INCLUDES_STAR_ONLY))
    assert proc.returncode == 0, proc.stdout + proc.stderr
    assert "[Divergence from STAR]" not in proc.stdout, proc.stdout


# --- function level: the "includes the STAR winner" label -------------------

def _parse(ballots):
    return [dict(zip(CANDS, (int(x) for x in ln.split(","))))
            for ln in ballots.strip().splitlines()[1:]]


def test_tie_including_star_is_labeled_when_block_prints(capsys):
    # Same ballots as TIE_EXCLUDES_STAR, but pretend STAR elected Bob: the
    # plurality tie (Ann/Bob) now includes the "STAR winner" while Approval
    # and RCV-IRV genuinely differ, so the block prints and must carry the
    # honest tie label instead of "(differs from STAR)".
    w.print_method_comparison(CANDS, _parse(TIE_EXCLUDES_STAR), "Bob", CANDS)
    out = capsys.readouterr().out
    assert "[Divergence from STAR]" in out
    assert ("Choose-One (Plurality) = tie (Ann / Bob)   "
            "(tie — includes the STAR winner)") in out, out


def test_clean_divergence_unchanged(capsys):
    # Classic center squeeze: no exact ties anywhere; the block must still
    # print plain single-name divergences exactly as before.
    ballots = ([{"Ann": 5, "Cal": 4, "Bob": 0}] * 35
               + [{"Bob": 5, "Cal": 4, "Ann": 0}] * 33
               + [{"Cal": 5, "Ann": 1, "Bob": 0}] * 16
               + [{"Cal": 5, "Bob": 1, "Ann": 0}] * 16)
    w.print_method_comparison(CANDS, ballots, "Cal", CANDS)
    out = capsys.readouterr().out
    assert "Choose-One (Plurality) = Ann   (differs from STAR)" in out, out
    assert "RCV-IRV                = Ann   (differs from STAR)" in out, out
    assert "tie (" not in out, out


# --- helpers: leader sets and the IRV deciding-round tie --------------------

def test_leader_sets_report_exact_ties():
    ballots = _parse(TIE_INCLUDES_STAR_ONLY)
    assert w.plurality_leaders(CANDS, ballots, CANDS) == ["Ann", "Bob", "Cal"]
    assert w.approval_leaders(CANDS, ballots, CANDS) == ["Cal"]
    assert w.copeland_leaders(CANDS, ballots, CANDS) == ["Cal"]


def test_irv_deciding_tie_detected():
    # Bob is eliminated first; Ann and Cal then split the final round 2-2 —
    # pyrankvote's comparator picks one, but the block must see the exact tie.
    ballots = [
        {"Ann": 5, "Bob": 1, "Cal": 0},
        {"Ann": 5, "Bob": 1, "Cal": 0},
        {"Ann": 0, "Bob": 1, "Cal": 5},
        {"Ann": 0, "Bob": 1, "Cal": 5},
    ]
    result, _, _ = w._run_irv(CANDS, ballots, CANDS)
    assert w.irv_deciding_tie(result, CANDS) == ["Ann", "Cal"]


def test_irv_clean_win_is_not_a_tie():
    ballots = _parse(TIE_EXCLUDES_STAR)
    result, _, _ = w._run_irv(CANDS, ballots, CANDS)
    assert w.irv_deciding_tie(result, CANDS) == []
