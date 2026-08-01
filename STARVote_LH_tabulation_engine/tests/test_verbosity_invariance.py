"""
test_verbosity_invariance.py
============================
Guards the fork's SSS verbosity fix (BUG_sss_verbosity.md, upstream issue
larryhastings/starvote#17): `verbosity` is a presentation option and must never
change who wins.

Upstream 2.1.6 nested the whole SSS ballot-allocation step (spending stars,
reweighting, removing exhausted ballots) inside `if options.verbosity:`, so a
quiet run never spent any ballots and SSS silently degenerated into repeated
bloc score voting — the minority bloc lost its proportional seat. The fork
dedents that machinery so it runs at every verbosity; only the printing stays
guarded.

Every multiwinner method is asserted invariant (not just SSS), so a future
edit that re-introduces a verbosity-gated computation anywhere fails loudly.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import starvote  # noqa: E402


def _ballots():
    """The BUG_sss_verbosity.md repro: a ~2/3 bloc (Alice/Ben/Cara) and a
    ~1/3 bloc (Dan/Eve). Proportional methods must seat Dan; a method that
    ignores ballot spending sweeps all three seats for the majority bloc."""
    ballots = []

    def add(n, d):
        for _ in range(n):
            ballots.append(dict(d))

    add(6, {"Alice": 5, "Ben": 4, "Cara": 3, "Dan": 0, "Eve": 0})
    add(4, {"Alice": 4, "Ben": 5, "Cara": 3, "Dan": 0, "Eve": 0})
    add(3, {"Alice": 3, "Ben": 4, "Cara": 5, "Dan": 0, "Eve": 0})
    add(5, {"Alice": 0, "Ben": 0, "Cara": 0, "Dan": 5, "Eve": 4})
    add(3, {"Alice": 0, "Ben": 0, "Cara": 0, "Dan": 4, "Eve": 5})
    return ballots


def _silent(*args, **kwargs):
    pass


def _run(method, verbosity):
    return sorted(
        starvote.election(
            method,
            _ballots(),
            seats=3,
            maximum_score=5,
            verbosity=verbosity,
            print=_silent,
        )
    )


def test_multiwinner_methods_are_verbosity_invariant():
    for method in (starvote.sss, starvote.allocated, starvote.rrv, starvote.bloc):
        quiet = _run(method, 0)
        assert quiet == _run(method, 1) == _run(method, 2), (
            f"{method.name}: winners changed with verbosity"
        )


def test_sss_quiet_run_is_proportional():
    # The exact failure mode of the upstream bug: at verbosity=0 SSS returned
    # the majority sweep [Alice, Ben, Cara] instead of seating Dan.
    assert _run(starvote.sss, 0) == ["Alice", "Ben", "Dan"]
