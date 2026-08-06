"""
test_matrix_finalists.py
========================
Locks the ``*`` markers on the Runoff (Preference) Matrix to the candidates
that ACTUALLY reach the automatic runoff.

The matrix legend promises "* indicates Top 2 Finalist", and
``matrix_finalists_only: true`` filters the whole grid down to that pair — so
if the marker set is wrong, the matrix names a finalist who never ran AND can
hide the head-to-head that decided the race.

The bug this guards against: ``get_top_two_finalists()`` used to rank by total
score with lot-number priority as the only tiebreak, skipping the two
DETERMINISTIC rungs STAR actually uses first. Whenever a scoring-round tie was
settled by the pairwise or five-star rung, the second-highest SCORER got the
star and the real finalist got none.

STAR's scoring-round ladder, in order:

  1. total score
  2. pairwise — "the candidate preferred in the most head-to-head matchups
     advances", counted WITHIN the tied group (ballots on which a candidate
     outscores another tied member, summed over the group)
  3. five-star — "the candidate with the most votes of score 5 advances"
  4. lot numbers

Both live cases below are checked against the tiebreak the engine itself
prints, so the test and the tabulator can't drift apart silently.
"""

import importlib.util
import pathlib

import pytest

ENGINE = pathlib.Path(__file__).resolve().parent.parent / "starvote_larry_hastings.py"


def _load_engine():
    spec = importlib.util.spec_from_file_location("lh_engine_for_tests", ENGINE)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


lh = _load_engine()


def _ballots(candidates, rows):
    return [dict(zip(candidates, row)) for row in rows]


def _finalists(candidates, rows):
    order_map = {c: i for i, c in enumerate(candidates)}
    return set(lh.get_top_two_finalists(_ballots(candidates, rows), order_map))


# --------------------------------------------------------------------------
# The two live cases in 01_STAR/03_Criteria/tie_break_ladder
# --------------------------------------------------------------------------

def test_pairwise_rung_advances_the_tiebreak_winner_not_the_scorer():
    """bv2276_qhjyr2_second_finalist_tie — Ben and Cora BOTH score 14.

    The engine prints:
        Scoring Round: First tiebreaker
          Cora -- 3 -- Second place
          Ben  -- 2
        Ana and Cora advance.

    So Cora is a finalist and Ben is not, even though they tied on score and
    Ben is listed first. This is the case that exposed the bug.
    """
    candidates = ["Ana", "Ben", "Cora", "Dev"]
    rows = [[5, 3, 5, 0], [3, 1, 3, 0], [5, 4, 2, 1], [1, 4, 0, 5], [1, 2, 4, 5]]

    assert _finalists(candidates, rows) == {"Ana", "Cora"}


def test_five_star_rung_breaks_a_three_way_pairwise_deadlock():
    """bv2180_fp62p2_ice_cream_ladder — Chocolate, Chocolate Chip and Vanilla
    all score 5, and the pairwise rung leaves all three on 2 (a genuine
    deadlock). The five-star rung then advances Chocolate Chip, the only one
    with a 5 on any ballot."""
    candidates = [
        "Chocolate", "Chocolate Chip", "Fudge Brownie",
        "Vanilla", "Strawberry", "Mango",
    ]
    rows = [[4, 5, 4, 1, 2, 0], [1, 0, 0, 4, 5, 4]]

    assert _finalists(candidates, rows) == {"Strawberry", "Chocolate Chip"}


# --------------------------------------------------------------------------
# The rungs in isolation
# --------------------------------------------------------------------------

def test_pairwise_count_matches_the_engines_printed_tally():
    """The rung-2 numbers the engine prints are 'ballots on which this
    candidate outscores another TIED candidate', summed over the group — not
    matchups won. Both cases above print totals that only this reading
    reproduces (Cora 3 / Ben 2; and 2 / 2 / 2 for the ice-cream trio)."""
    cands = ["Ana", "Ben", "Cora", "Dev"]
    rows = [[5, 3, 5, 0], [3, 1, 3, 0], [5, 4, 2, 1], [1, 4, 0, 5], [1, 2, 4, 5]]
    ballots = _ballots(cands, rows)
    tied = ["Ben", "Cora"]

    assert lh._pairwise_preference_count("Cora", tied, ballots) == 3
    assert lh._pairwise_preference_count("Ben", tied, ballots) == 2

    ice = ["Chocolate", "Chocolate Chip", "Fudge Brownie",
           "Vanilla", "Strawberry", "Mango"]
    ice_ballots = _ballots(ice, [[4, 5, 4, 1, 2, 0], [1, 0, 0, 4, 5, 4]])
    trio = ["Chocolate", "Chocolate Chip", "Vanilla"]
    assert [lh._pairwise_preference_count(c, trio, ice_ballots) for c in trio] == [2, 2, 2]


def test_five_star_count_counts_only_top_scores():
    cands = ["A", "B"]
    ballots = _ballots(cands, [[5, 4], [5, 5], [3, 0]])

    assert lh._five_star_count("A", ballots) == 2
    assert lh._five_star_count("B", ballots) == 1


# --------------------------------------------------------------------------
# Shapes that must keep working
# --------------------------------------------------------------------------

def test_no_tie_is_plain_score_order():
    assert _finalists(["A", "B", "C"], [[5, 3, 1], [5, 3, 0]]) == {"A", "B"}


def test_tie_for_first_advances_both_without_a_tiebreak():
    """Two candidates tied at the top fill both slots outright — the ladder
    must not be consulted, because there is nothing to decide."""
    assert _finalists(["A", "B", "C"], [[5, 5, 0], [5, 5, 1]]) == {"A", "B"}


def test_lot_order_is_the_last_resort():
    """A perfectly symmetric three-way cycle for two slots: all three tie on
    score (9 each), on the pairwise rung (3 each) and on five-star (1 each),
    so every deterministic rung is exhausted and only the lot separates them.

    Whichever two the lot ranks first are the finalists — so changing the lot
    order changes the pair, and nothing else does.
    """
    cands = ["A", "B", "C"]
    ballots = _ballots(cands, [[5, 3, 1], [1, 5, 3], [3, 1, 5]])

    trio = ["A", "B", "C"]
    assert [lh._pairwise_preference_count(c, trio, ballots) for c in trio] == [3, 3, 3]
    assert [lh._five_star_count(c, ballots) for c in trio] == [1, 1, 1]

    assert set(lh.get_top_two_finalists(ballots, {"A": 0, "B": 1, "C": 2})) == {"A", "B"}
    assert set(lh.get_top_two_finalists(ballots, {"C": 0, "A": 1, "B": 2})) == {"C", "A"}
    assert set(lh.get_top_two_finalists(ballots, {"B": 0, "C": 1, "A": 2})) == {"B", "C"}


def test_a_group_that_exactly_fills_the_remaining_slots_needs_no_rung():
    """A and B tie on score and there are exactly two slots, so both advance
    outright — the ladder must not be consulted to rank them against each
    other, because there is nothing to decide."""
    assert _finalists(["A", "B", "C"], [[5, 1, 0], [1, 5, 0]]) == {"A", "B"}


def test_returns_at_most_two():
    assert len(lh.get_top_two_finalists(_ballots(["A", "B", "C", "D"],
                                                 [[3, 3, 3, 3]]), {})) == 2


@pytest.mark.parametrize("rows", [[[5, 4, 3]], [[0, 0, 0]], [[5, 5, 5], [0, 0, 0]]])
def test_never_raises_on_degenerate_ballots(rows):
    assert len(_finalists(["A", "B", "C"], rows)) == 2
