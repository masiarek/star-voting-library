"""
test_allocated_weight_accounting.py
===================================
Guards the fork's Allocated Score count-vs-weight fix
(BUG_allocated_count_vs_weight.md, upstream issue larryhastings/starvote#20):
the ballot-allocation round must fill the Hare quota by ballot WEIGHT, not
ballot count, so a bloc surrenders one full quota of weight per seat.

Upstream 2.1.6 uses the score group's row count in the overfill test, the
quota subtraction, and the surplus factor. Counts and weights coincide while
all weights are 1, so single-surplus fixtures pass on both accountings; the
bug needs a second allocation event on already-reduced ballots. Buggy engines
then reduce a solid bloc by the same factor every round (geometric decay,
D'Hondt-flavored); the fixed engine matches BetterVoting production and the
reference implementation shipped in starvote/reference.py (both verified
2026-08-09, BV live via /API/Sandbox).
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import starvote  # noqa: E402


def test_fingerprint_slates_elect_hamilton_not_dhondt():
    """41/19/6 party-line slates, 5 seats: 3.11/1.44/0.45 quotas => 3-1-1.

    Buggy engines elect a fourth A candidate (4-1-0, D'Hondt's answer)
    because the A slate pays 13.2/41 = 32.20% of its remaining weight per
    seat forever instead of a full quota per seat.
    """
    cands = ["A1", "A2", "A3", "A4", "B1", "B2", "B3", "C1", "C2"]
    rows = (
        [[5, 5, 5, 5, 0, 0, 0, 0, 0]] * 41
        + [[0, 0, 0, 0, 5, 5, 5, 0, 0]] * 19
        + [[0, 0, 0, 0, 0, 0, 0, 5, 5]] * 6
    )
    ballots = [dict(zip(cands, r)) for r in rows]
    tiebreaker = starvote.predefined_permutation_tiebreaker(cands)
    winners = starvote.allocated_score_voting(ballots, seats=5, tiebreaker=tiebreaker)
    assert sorted(winners) == ["A1", "A2", "A3", "B1", "C1"]


def test_coop_board_third_seat_goes_to_amy():
    """The organic repo case the bug bit: 9 voters, 5 candidates, 3 seats.

    After Ben's seat the count accounting retired 3 ballots carrying only
    2.6 weight and called the 3.0 quota filled, leaving Member 4's ballot
    unspent — which lifted Dana (8.6) over Amy (8.2). Weight-true accounting
    spends the missing 0.4 from the 2.4-star group and elects Amy
    (7.8 vs 7.0; no ties either way). BetterVoting production agrees.
    """
    cands = ["Amy", "Ben", "Chris", "Dana", "Ella"]
    rows = [
        [5, 1, 3, 3, 4],
        [2, 2, 4, 3, 0],
        [0, 4, 4, 2, 3],
        [1, 3, 4, 4, 4],
        [5, 2, 5, 2, 5],
        [1, 2, 4, 0, 0],
        [1, 2, 5, 4, 2],
        [2, 5, 4, 0, 4],
        [1, 3, 3, 5, 0],
    ]
    ballots = [dict(zip(cands, r)) for r in rows]
    winners = starvote.allocated_score_voting(ballots, seats=3)
    assert sorted(winners) == ["Amy", "Ben", "Chris"]


def test_single_surplus_fixture_unchanged():
    """BetterVoting's own unit fixture (bkk2gxj): one surplus event on
    full-weight ballots — count and weight coincide, so the fix must not
    change this result. Allison's 8 five-star supporters each keep 0.25
    weight after her seat (quota 6), and Doug takes the second chair.
    """
    cands = ["Allison", "Bill", "Carmen", "Doug"]
    rows = (
        [[5, 5, 1, 0]] * 7
        + [[5, 4, 4, 0]]
        + [[0, 0, 0, 3]]
        + [[0, 0, 4, 5]] * 3
    )
    ballots = [dict(zip(cands, r)) for r in rows]
    winners = starvote.allocated_score_voting(ballots, seats=2)
    assert sorted(winners) == ["Allison", "Doug"]
