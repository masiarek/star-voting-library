"""
test_abcvoting_crosscheck.py
============================
Cross-checks the LH engine's Approval tabulation against Martin Lackner's
`abcvoting` library (skips cleanly if it isn't installed).

1. For EVERY approval YAML under the teaching roots that declares
   `expected_winners:` (already verified against the LH engine by
   test_method_positive.py), abcvoting's plain `av` rule must elect the same
   committee — an independent witness for the LH approval tally.
2. Pins the proportionality demo: on the majority-sweep case, SPAV / PAV /
   seq-Phragmén must elect Amy + Cora (minority seat), NOT the av sweep.
"""
import pathlib
import sys

import pytest
import yaml

abcvoting = pytest.importorskip("abcvoting")

ENGINE_DIR = pathlib.Path(__file__).resolve().parents[1]
REPO_ROOT = ENGINE_DIR.parent
sys.path.insert(0, str(REPO_ROOT / "abcvoting_tabulation_engine"))
from abc_tabulation import tabulate_abc  # noqa: E402

ROOTS = ["01_STAR", "02_STAR_Bloc", "03_STAR_PR", "04_Approval",
         "05_Ranked_Robin", "method_comparisons", "other_methods"]
SKIP_DIR_SUFFIXES = ("_tabulated", "_generated", "_pages")


def _approval_cases():
    cases = []
    for root in ROOTS:
        base = REPO_ROOT / root
        if not base.is_dir():
            continue
        for p in sorted(base.rglob("*.yaml")):
            if any(part.endswith(SKIP_DIR_SUFFIXES) for part in p.parts):
                continue
            try:
                d = yaml.safe_load(p.read_text())
            except Exception:
                continue
            if not isinstance(d, dict) or "expected_winners" not in d:
                continue
            if "approval" not in str(d.get("voting_method", "")).lower():
                continue
            cases.append((p, sorted(str(w) for w in d["expected_winners"])))
    return cases


CASES = _approval_cases()
IDS = [str(p.relative_to(REPO_ROOT)) for p, _ in CASES]


def test_discovery_not_vacuous():
    assert len(CASES) >= 2, f"only {len(CASES)} approval cases discovered: {IDS}"


@pytest.mark.parametrize("path,expected", CASES, ids=IDS)
def test_av_matches_lh_expected_winners(path, expected):
    """abcvoting `av` == the LH-verified expected winners (ties: expected
    committee must be among the tied committees)."""
    committees = tabulate_abc(path, rules=("av",))["av"]
    assert expected in [sorted(c) for c in committees], (
        f"{path.name}: abcvoting av returned {committees}, expected {expected}")


def test_proportional_rules_break_the_sweep():
    """The multiwinner demo: av ties {Amy,Ben} with {Amy,Cora} (the LH engine
    breaks that tie for Ben by priority order); every proportional rule must
    DECISIVELY seat the minority's Cora alongside Amy."""
    path = REPO_ROOT / "04_Approval/multiwinner/approval_bloc_2seats_c4_b6.yaml"
    result = tabulate_abc(path, rules=("av", "seqpav", "pav", "seqphragmen"))
    assert {frozenset(c) for c in result["av"]} == {
        frozenset({"Amy", "Ben"}), frozenset({"Amy", "Cora"})}
    for rule in ("seqpav", "pav", "seqphragmen"):
        assert result[rule] == [["Amy", "Cora"]], (
            f"{rule} returned {result[rule]}, expected [['Amy', 'Cora']]")
