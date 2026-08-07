"""
test_rcv_irv_tie_order_sensitivity.py
=====================================
Pins how the vendored RCV-IRV engine (pyrankvote) resolves an ELIMINATION TIE,
and specifically pins the one place it gets that wrong.

pyrankvote's ladder (`_cmp_candidate_vote_counts`, in
`06_Other/RCV_IRV/RCV_IRV_tabulation_engine/pyrankvote/helpers.py`) breaks a
first-choice tie on MOST SECOND CHOICES, then thirds, then fourths — a real
ballot-based tiebreak, structurally the same shape as the STAR engine's
pairwise -> five-star -> lot ladder. Only when it runs out of ranks does it fall
to `random.choice`, which `rcv_irv_tabulation.py` seeds with `random.seed(0)`.

Two behaviours, and the tests below hold them apart on purpose:

  * WHILE THE LADDER HAS INFORMATION the count is fully determined by the
    ballots, and the order the ballot rows happen to be written in is
    irrelevant. `test_ladder_makes_row_order_irrelevant` asserts that.

  * ONCE THE LADDER DIES — every candidate tied at every rank, e.g. a perfect
    3-cycle — the seed pins the SEQUENCE of coin flips but not the CANDIDATE
    each flip lands on, because `sorted()` feeds the comparator pairs in an
    order set by the input list, which is built in order of each candidate's
    first appearance across the ballot rows. The winner becomes the first row's
    first choice. `test_dead_ladder_is_decided_by_ballot_row_order` asserts
    that, and it is asserting a DEFECT, not a desirable property: re-ordering
    identical ballots elects somebody else, which is an anonymity failure.

    ** If that test starts failing because the engine LEARNED to handle a total
    tie — batching, reporting the tied set, or applying a published lot order —
    that is the fix landing. Update this test to the new contract; do not
    "repair" the engine back to row-order sensitivity. **

Background: 06_Other/RCV_IRV/RCV_IRV_tabulation_engine/README.md
            ("Known limitation — elimination ties")
            07_Concepts/topics/ties/batch_elimination.md
Cases:      06_Other/RCV_IRV/cases/batch_all_out_{cycle,condorcet}_c3_b3.yaml
"""

import itertools
import subprocess
import sys
from pathlib import Path

ENGINE_DIR = Path(__file__).resolve().parent.parent
WRAPPER = ENGINE_DIR / "starvote_larry_hastings.py"

# Every candidate holds exactly one first, one second and one third choice, so
# every rung of pyrankvote's ladder ties and the count reaches the coin.
DEAD_LADDER = ["Amy>Bruno>Clara", "Bruno>Clara>Amy", "Clara>Amy>Bruno"]

# One ballot changed. First choices still tie 1-1-1, but SECOND choices now
# separate them (Amy 2, Bruno 1, Clara 0), so rung two of the ladder decides.
LIVE_LADDER = ["Amy>Bruno>Clara", "Bruno>Amy>Clara", "Clara>Amy>Bruno"]


def _winner(tmp_path, rows, stem):
    """Tabulate `rows` as a ranked RCV-IRV election; return the winner's name."""
    yaml_path = tmp_path / f"{stem}.yaml"
    yaml_path.write_text(
        "election_title: tie-order probe\n"
        "voting_method: RCV_IRV\n"
        "num_winners: 1\n"
        "ballots: |-\n" + "".join(f"  {r}\n" for r in rows),
        encoding="utf-8",
    )
    proc = subprocess.run(
        [sys.executable, str(WRAPPER), str(yaml_path)],
        cwd=str(ENGINE_DIR), capture_output=True, text=True,
    )
    assert proc.returncode == 0, proc.stdout + proc.stderr
    # The wrapper's last output line is the winner.
    return proc.stdout.strip().splitlines()[-1].strip()


def test_ladder_makes_row_order_irrelevant(tmp_path):
    """Second choices separate the candidates -> every row order elects Amy."""
    winners = {
        _winner(tmp_path, list(perm), f"live{i}")
        for i, perm in enumerate(itertools.permutations(LIVE_LADDER))
    }
    assert winners == {"Amy"}, (
        f"pyrankvote's second-choice rung should decide this outright, "
        f"independent of ballot order; got {sorted(winners)}"
    )


def test_dead_ladder_is_decided_by_ballot_row_order(tmp_path):
    """KNOWN LIMITATION — see the module docstring before 'fixing' this."""
    results = {
        perm: _winner(tmp_path, list(perm), f"dead{i}")
        for i, perm in enumerate(itertools.permutations(DEAD_LADDER))
    }

    # Three distinct winners from one identical multiset of ballots.
    assert len(set(results.values())) == 3, (
        "expected the dead ladder to elect all three candidates across the six "
        f"row orderings; got {sorted(set(results.values()))}"
    )

    # And the rule is exactly "whoever the first row ranked first".
    for perm, winner in results.items():
        assert winner == perm[0].split(">")[0], (
            f"row order {perm} elected {winner}, not the first row's first choice"
        )


def test_seed_makes_a_dead_ladder_reproducible_run_to_run(tmp_path):
    """The seed is not useless: it removes run-to-run variance. Guard that."""
    runs = {_winner(tmp_path, DEAD_LADDER, f"seed{i}") for i in range(3)}
    assert len(runs) == 1, (
        f"identical input elected different winners on repeat runs: {sorted(runs)} "
        "— has random.seed(0) been dropped from rcv_irv_tabulation.py?"
    )
