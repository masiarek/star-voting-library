"""
test_unbreakable_tie_message.py
===============================
Guards the fork's unbreakable-tie message fix: the `UnbreakableTieError` raised
by `_star_round()` must name the tie in words ("three-way tie in Scoring
Round"), not echo its own source text.

Upstream 2.1.6 omits the `f` prefix on both `options.break_tie(...)` strings in
`_star_round()`, so the placeholder is never interpolated and the exception
message arrives as the literal
`{int_to_words(len(tie), flowery=False)}-way tie in Scoring Round`. The same
strings in `allocated_score_voting()` and `sequentially_spent_score()` DO carry
the prefix, which is why only STAR and Bloc STAR (both of which route through
`_star_round()`) show it. Reported upstream; the printed report was never
affected, so only the API path exposes it.

Two layers of guard: the behavioural tests below pin the message for the three
reachable `_star_round()` ties, and `test_no_break_tie_message_is_unformatted`
parses the engine source so the two sites that are awkward to trigger
(allocated / SSS) cannot regress either.
"""
import ast
import sys
from pathlib import Path

import pytest

ENGINE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ENGINE_DIR))
import starvote  # noqa: E402

PLACEHOLDER = "int_to_words"


def _silent(*args, **kwargs):
    pass


def _tie_message(method, ballots, **kwargs):
    """Run an election that cannot break its tie; return the error message."""
    with pytest.raises(starvote.UnbreakableTieError) as excinfo:
        starvote.election(
            method,
            ballots,
            maximum_score=5,
            tiebreaker=None,
            print=_silent,
            **kwargs,
        )
    return str(excinfo.value)


# Rock-paper-scissors scores: every candidate collects one 3, one 4 and one 5,
# wins exactly one head-to-head, and holds exactly one 5 — so the scoring round
# and both of its tiebreakers tie, and the engine has to give up.
ROTATING = [
    {"a": 3, "b": 4, "c": 5},
    {"a": 5, "b": 3, "c": 4},
    {"a": 4, "b": 5, "c": 3},
]

# Two candidates, mirror-image ballots: they tie on score, tie the runoff 1-1,
# and hold one 5 each — the Automatic Runoff Round's own dead end.
MIRRORED = [
    {"a": 5, "b": 3},
    {"a": 3, "b": 5},
]


def test_star_scoring_round_tie_message():
    message = _tie_message(starvote.STAR_Voting, ROTATING)
    assert "three-way tie in Scoring Round" in message
    assert PLACEHOLDER not in message


def test_bloc_star_scoring_round_tie_message():
    # The reported repro: Bloc STAR shares `_star_round()` with single-winner STAR.
    message = _tie_message(starvote.Bloc_STAR_Voting, ROTATING, seats=2)
    assert "three-way tie in Scoring Round" in message
    assert PLACEHOLDER not in message


def test_automatic_runoff_round_tie_message():
    message = _tie_message(starvote.STAR_Voting, MIRRORED)
    assert "two-way tie in Automatic Runoff Round" in message
    assert PLACEHOLDER not in message


def test_no_break_tie_message_is_unformatted():
    """No `break_tie()` description may be a plain string holding a placeholder.

    Catches the two `_star_round()` sites above plus the `allocated_score_voting()`
    and `sequentially_spent_score()` ones, whose ties are awkward to provoke.
    Parsed rather than grepped so the engine's deliberate `.format()` templates
    (`exception_prefix_format`, `repeated_key_format`) don't read as failures.
    """
    source = (ENGINE_DIR / "starvote" / "__init__.py").read_text()
    offenders = []
    for node in ast.walk(ast.parse(source)):
        if not (isinstance(node, ast.Call) and node.args):
            continue
        name = getattr(node.func, "attr", None) or getattr(node.func, "id", None)
        if name != "break_tie":
            continue
        description = node.args[0]
        # An f-string parses to JoinedStr; a plain literal to Constant.
        if isinstance(description, ast.Constant) and "{" in str(description.value):
            offenders.append(f"line {description.lineno}: {description.value!r}")
    assert not offenders, (
        "break_tie() description(s) with a {placeholder} but no f prefix: "
        f"{offenders}"
    )
