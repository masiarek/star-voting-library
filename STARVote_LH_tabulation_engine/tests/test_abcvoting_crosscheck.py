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
3. Pins the tie contract: every rule runs irresolute (resolute=False), so a
   seqpav / seqphragmen tie comes back as several committees instead of being
   broken silently by column order (abcvoting's default for its sequential
   rules); a rule with no irresolute form is flagged, not faked.
4. Pins one place the two libraries answer different questions: an election in
   which every ballot approves nobody is a lot-decided tie to the LH engine and
   an invalid profile to abcvoting.
"""
import pathlib
import sys

import pytest
import yaml

abcvoting = pytest.importorskip("abcvoting")

ENGINE_DIR = pathlib.Path(__file__).resolve().parents[1]
REPO_ROOT = ENGINE_DIR.parent
sys.path.insert(0, str(REPO_ROOT / "06_Other/abcvoting_tabulation_engine"))
from abc_tabulation import tabulate_abc  # noqa: E402

ROOTS = ["01_STAR", "02_STAR_Bloc", "03_STAR_PR", "04_Approval",
         "05_Ranked_Robin", "method_comparisons", "06_Other"]
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


def _approves_nobody(path):
    """True when not one ballot on the file marks an approval.

    `abcvoting` builds its `Profile` from approval SETS, so a ballot approving
    nobody contributes no voter at all — an election where every ballot is
    empty arrives as a profile of length zero.
    """
    d = yaml.safe_load(path.read_text())
    rows = [ln.split("#")[0].strip()
            for ln in str(d.get("ballots", "")).splitlines()[1:]]
    return all(set(r.replace(",", "").replace(" ", "")) <= {"0", ""}
               for r in rows if r)


@pytest.mark.parametrize("path,expected", CASES, ids=IDS)
def test_av_matches_lh_expected_winners(path, expected):
    """abcvoting `av` == the LH-verified expected winners (ties: expected
    committee must be among the tied committees).

    One case is answered by a refusal instead of a committee — see
    `test_abcvoting_refuses_an_election_with_no_approvals` below. That is a
    real difference between the two libraries, so it is asserted here rather
    than skipped past.
    """
    try:
        committees = tabulate_abc(path, rules=("av",))["av"]
    except ValueError as exc:
        assert "no voters" in str(exc) and _approves_nobody(path), (
            f"{path.name}: abcvoting refused a profile that does have "
            f"approvals — {exc}")
        return
    assert expected in [sorted(c) for c in committees], (
        f"{path.name}: abcvoting av returned {committees}, expected {expected}")


def test_abcvoting_refuses_an_election_with_no_approvals():
    """The zero-support election is not a tie to `abcvoting` — it is not an
    election.

    Three ballots are cast and every one of them approves nobody. The LH engine
    counts it (0 approvals each, candidate priority order elects Ada, and the
    report says so); `abcvoting` builds its profile from approval sets, sees
    zero voters, and raises. Neither is wrong — they answer different questions
    — but a cross-check that quietly skipped this would hide the sharpest
    disagreement in the corpus. The teaching page:
    method_comparisons/zero_support_election/README.md
    """
    path = (REPO_ROOT / "method_comparisons" / "zero_support_election" / "cases"
            / "zero_support_approval.yaml")
    assert path.exists(), f"case moved: {path}"
    with pytest.raises(ValueError, match="no voters"):
        tabulate_abc(path, rules=("av",))


def test_proportional_rules_break_the_sweep():
    """The multiwinner demo: av ties {Amy,Ben} with {Amy,Cora} (the LH engine
    breaks that tie for Ben by priority order); every proportional rule must
    DECISIVELY seat the minority's Cora alongside Amy."""
    path = REPO_ROOT / "04_Approval/02_Examples/multiwinner/cases/approval_bloc_2seats_c4_b6.yaml"
    result = tabulate_abc(path, rules=("av", "seqpav", "pav", "seqphragmen"))
    assert {frozenset(c) for c in result["av"]} == {
        frozenset({"Amy", "Ben"}), frozenset({"Amy", "Cora"})}
    for rule in ("seqpav", "pav", "seqphragmen"):
        assert result[rule] == [["Amy", "Cora"]], (
            f"{rule} returned {result[rule]}, expected [['Amy', 'Cora']]")


def test_sequential_rules_surface_their_ties():
    """The wrapper passes resolute=False to EVERY rule. abcvoting's sequential
    rules default to resolute=True and break a candidate tie by smallest index
    — ballot-header column order here — with no marker. On the 3-seat council
    case bloc av is decisive, but seqpav and seqphragmen leave THREE committees
    open; a resolute run would return only the first of them, silently."""
    path = REPO_ROOT / "04_Approval/02_Examples/multiwinner/cases/approval_bloc_3seats_c6_b5.yaml"
    result = tabulate_abc(path, rules=("av", "seqpav", "seqphragmen"))
    assert result["av"] == [["Adams", "Brown", "Clark"]]
    open_three = [["Adams", "Brown", "Clark"], ["Adams", "Brown", "Evans"],
                  ["Brown", "Clark", "Evans"]]
    for rule in ("seqpav", "seqphragmen"):
        assert sorted(result[rule]) == open_three, (
            f"{rule} returned {result[rule]} — a resolute (column-order) "
            "tie-break would show only the first committee")
    assert result["_meta"]["resolute_only"] == []


def test_rule_without_irresolute_form_is_flagged():
    """greedy-monroe is DEFINED by a tiebreaking order, so abcvoting refuses
    resolute=False for it; the wrapper falls back to resolute and records it."""
    path = REPO_ROOT / "04_Approval/02_Examples/multiwinner/cases/approval_bloc_3seats_c6_b5.yaml"
    result = tabulate_abc(path, rules=("greedy-monroe",))
    assert len(result["greedy-monroe"]) == 1
    assert result["_meta"]["resolute_only"] == ["greedy-monroe"]
