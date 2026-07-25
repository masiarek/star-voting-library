"""
test_condorcet_loser.py
=======================
Locks the `[Condorcet Loser]` block (printed by print_condorcet under the
same show_condorcet flag as `[Condorcet Winner]`, and forced on in the
`_tabulated` mirror like every analysis).

The block prints ONLY when a strict or unique weak Condorcet loser exists:
  - strict:  "Condorcet Loser: X — loses every head-to-head matchup"
  - weak:    "No strict Condorcet loser; weak Condorcet loser: X (never wins
             a matchup)"
plus an " — elected by <methods>!" flag when STAR / Choose-One (Plurality) /
Approval actually elected that loser (the audit case — Burlington 2009 for
Plurality). STAR and Ranked Robin structurally can't elect a STRICT Condorcet
loser, so a strict-CL "elected by STAR" assertion would be vacuous — the STAR
flag is reachable only via the weak-CL score tiebreaker.

Change the wording in starvote_larry_hastings.py and here together.
"""
import subprocess
import sys
from pathlib import Path

ENGINE_DIR = Path(__file__).resolve().parent.parent
WRAPPER = ENGINE_DIR / "starvote_larry_hastings.py"

OPTS = "options:\n  show_condorcet: true\n  show_matrix: false\n  brief: true\n"


def _run(path):
    return subprocess.run([sys.executable, str(WRAPPER), str(path)],
                          capture_output=True, text=True, cwd=str(ENGINE_DIR))


def test_strict_loser_elected_by_plurality(tmp_path):
    """Burlington shape: Alma is the strict Condorcet loser (loses both
    head-to-heads 6-9) yet leads first choices 6-5-4 — Plurality elects her,
    and the block must say so."""
    f = tmp_path / "cl_plurality.yaml"
    f.write_text(
        "voting_method: STAR\nnum_winners: 1\n" + OPTS +
        "ballots: |-\n"
        "  Count:Alma,Beck,Cole\n"
        "  6:5,0,0\n"
        "  5:0,5,4\n"
        "  4:0,4,5\n"
    )
    r = _run(f)
    assert r.returncode == 0, r.stderr
    assert ("Condorcet Loser: Alma — loses every head-to-head matchup"
            " — elected by Choose-One (Plurality)!") in r.stdout
    # Winner block is untouched by the feature.
    assert "Condorcet Winner: Beck — matches the STAR winner" in r.stdout


def test_no_loser_no_block(tmp_path):
    """A Rock/Paper/Scissors cycle has no (strict or weak) Condorcet loser —
    the block must not print at all."""
    f = tmp_path / "cycle.yaml"
    f.write_text(
        "voting_method: STAR\nnum_winners: 1\n" + OPTS +
        "ballots: |-\n"
        "  Count:Rock,Paper,Scissors\n"
        "  7:5,0,3\n"
        "  7:3,5,0\n"
        "  6:0,3,5\n"
    )
    r = _run(f)
    assert r.returncode == 0, r.stderr
    assert "[Condorcet Loser]" not in r.stdout


def test_weak_loser_wording(tmp_path):
    """Dana never wins a matchup but ties one (Beck): a unique WEAK Condorcet
    loser, with the softer wording and no strict claim."""
    f = tmp_path / "weak_cl.yaml"
    # Pairwise: Alma beats everyone (CW). Beck beats Cole; Cole beats Dana;
    # Beck vs Dana is an exact 6-6 tie (third bloc scores both 4). So Dana
    # never wins a matchup but isn't a STRICT loser — the unique weak CL.
    f.write_text(
        "voting_method: STAR\nnum_winners: 1\n" + OPTS +
        "ballots: |-\n"
        "  Count:Alma,Beck,Cole,Dana\n"
        "  6:5,4,3,0\n"
        "  6:5,0,3,2\n"
        "  6:5,4,0,4\n"
    )
    r = _run(f)
    assert r.returncode == 0, r.stderr
    out = r.stdout
    assert ("No strict Condorcet loser; weak Condorcet loser: Dana "
            "(never wins a matchup)") in out
    assert "Condorcet Loser: Dana —" not in out


def test_joint_weak_losers_star_elects_one(tmp_path):
    """Weak-CL flagship shape (mirrors the BV2249 lesson): Ada is the CW but
    polarizing, so the two JOINTLY winless candidates (Ben ties Cora 2-2,
    both lose to Ada) reach the runoff and the score tiebreaker seats Ben —
    a weak Condorcet loser elected by STAR. The joint line must name both
    and flag who got elected."""
    f = tmp_path / "joint_wcl.yaml"
    f.write_text(
        "voting_method: STAR\nnum_winners: 1\n" + OPTS +
        "ballots: |-\n"
        "  Ada,Ben,Cora\n"
        "  5,4,4\n"
        "  5,4,3\n"
        "  5,3,4\n"
        "  0,3,4\n"
        "  0,4,1\n"
    )
    r = _run(f)
    assert r.returncode == 0, r.stderr
    assert ("No strict Condorcet loser; jointly weak Condorcet losers: "
            "Ben, Cora (winless — pairwise ties) — Ben elected by STAR, "
            "Approval!") in r.stdout
    assert "Condorcet Winner: Ada — STAR elected Ben instead" in r.stdout
