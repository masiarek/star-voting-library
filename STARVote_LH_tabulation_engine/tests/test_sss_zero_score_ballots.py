"""
test_sss_zero_score_ballots.py
==============================
Guards the fork's SSS zero-score-ballot fix (BUG_sss_zero_score_ballots.md,
upstream issue larryhastings/starvote#19): a ballot that scored the round's
winner 0 spent nothing and must keep its full remaining budget for later
rounds (vote unitarity).

Upstream 2.1.6 appends surviving ballots to the rebuilt remaining-ballots
list only inside `if score:`, and swaps to the rebuilt list whenever any
ballot exhausts — so in any round where a supporter exhausts (raw 5, no
surplus), every zero-score ballot was silently removed with its unspent
budget, which can flip the committee. The fork dedents the append out of
`if score:`; only exhausted ballots are dropped.

The profile below is the minimal known trigger: round 1 seats Cy with no
surplus, one `Cy: 5` ballot exhausts, and two Amy bullet voters score Cy 0.
Buggy engines elect Bo for the second seat; textbook SSS elects Amy
(11 3/5 vs 5 1/5 in round 2 — the two kept ballots carry 5 stars each).
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import starvote  # noqa: E402


def _ballots():
    """BUG_sss_zero_score_ballots.md repro: 7 voters, 3 candidates, 2 seats."""
    return [
        {"Amy": 0, "Bo": 5, "Cy": 3},
        {"Amy": 5, "Bo": 0, "Cy": 0},  # Amy bullet voter — scores Cy 0
        {"Amy": 0, "Bo": 3, "Cy": 4},
        {"Amy": 2, "Bo": 2, "Cy": 5},  # exhausts in round 1 (raw 5, no surplus)
        {"Amy": 5, "Bo": 1, "Cy": 0},  # scores Cy 0
        {"Amy": 0, "Bo": 0, "Cy": 4},
        {"Amy": 2, "Bo": 2, "Cy": 1},
    ]


def _run(verbosity, sink=None):
    def _print(*args, **kwargs):
        if sink is not None:
            sink.append(" ".join(str(a) for a in args))

    return sorted(
        starvote.election(
            starvote.sss,
            _ballots(),
            seats=2,
            maximum_score=5,
            verbosity=verbosity,
            print=_print,
        )
    )


def test_zero_score_ballots_keep_their_budget():
    # The exact failure mode: buggy engines drop the two Amy bullet voters
    # when the Cy:5 ballot exhausts, and elect [Bo, Cy] instead.
    for verbosity in (0, 1, 2):
        assert _run(verbosity) == ["Amy", "Cy"], (
            f"verbosity={verbosity}: zero-score ballots lost their budget"
        )


def test_repro_profile_still_exercises_the_trigger():
    # Guard the guard: the profile is only a regression test while a ballot
    # actually exhausts in a no-surplus round. If a future edit to _ballots()
    # stops the exhaustion, the test above would pass vacuously.
    lines = []
    _run(1, sink=lines)
    assert any("no surplus to give back" in l for l in lines), lines
    assert any("Allocated 1 ballot" in l for l in lines), lines
