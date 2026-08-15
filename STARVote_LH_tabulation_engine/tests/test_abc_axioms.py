"""
test_abc_axioms.py
==================
Gates the recomputed Table 3.1 in `04_Approval/03_Criteria/README.md`.

The table's `x` cells are the repo's claim that thirteen approval-based
committee rules break six named axioms in specific, reproducible ways. Each of
those cells has a witness profile from Lackner & Skowron's Appendix A, encoded
in `06_Other/abcvoting_tabulation_engine/abc_axiom_check.py`. If a witness stops
reproducing — because `abcvoting` changed a tiebreak, a rule's implementation
moved, or someone edited a profile — the published table is wrong and this fails.

Skips cleanly if `abcvoting` isn't installed (same contract as
test_abcvoting_crosscheck.py).
"""
import pathlib
import sys

import pytest

pytest.importorskip("abcvoting")

ENGINE_DIR = pathlib.Path(__file__).resolve().parents[1]
REPO_ROOT = ENGINE_DIR.parent
sys.path.insert(0, str(REPO_ROOT / "06_Other/abcvoting_tabulation_engine"))

from abc_axiom_check import (  # noqa: E402
    TABLE_RULES, WITNESSES, check_witness, parse_profile, resolute_winner,
)

CRITERIA = REPO_ROOT / "04_Approval/03_Criteria"

IDS = [f"{w['axiom']}-{w['rule']}" for w in WITNESSES]


def test_discovery_not_vacuous():
    """A silently-empty witness list would make every other test here pass."""
    assert len(WITNESSES) >= 30, f"only {len(WITNESSES)} witnesses encoded"
    axioms = {w["axiom"] for w in WITNESSES}
    assert axioms == {
        "pareto", "committee_monotonicity", "support_mono_with",
        "support_mono_without", "consistency", "inclusion_sp",
    }, f"axiom coverage changed: {sorted(axioms)}"


@pytest.mark.parametrize("witness", WITNESSES, ids=IDS)
def test_witness_reproduces(witness):
    """Every `x` cell in the published table replays through abcvoting."""
    ok, msg = check_witness(witness)
    assert ok, f"{witness['rule']} / {witness['axiom']} ({witness['cite']}): {msg}"


def test_all_thirteen_table_rules_are_computable():
    """Every rule named in the published table can actually be run."""
    profile, _ = parse_profile([(2, "a"), (3, "ac"), (3, "bc"), (2, "b")])
    for label, rule_id in TABLE_RULES:
        committee = resolute_winner(rule_id, profile, 2)
        assert len(committee) == 2, f"{label} ({rule_id}) returned {committee}"


def test_committee_monotonicity_case_files_are_the_same_election():
    """The 1-seat and 2-seat case files must differ ONLY in num_winners.

    The lesson is 'same ballots, one more seat'. If the ballot blocks drift
    apart the pair stops demonstrating anything, and nothing else would catch
    it — each file tabulates fine on its own.
    """
    import yaml
    one = yaml.safe_load(
        (CRITERIA / "cases/abc_committee_monotonicity_1seat_c3_b10.yaml").read_text())
    two = yaml.safe_load(
        (CRITERIA / "cases/abc_committee_monotonicity_2seats_c3_b10.yaml").read_text())
    assert one["ballots"] == two["ballots"], "the matched pair's ballots have drifted"
    assert one["num_winners"] == 1 and two["num_winners"] == 2


def test_published_table_matches_the_witnesses():
    """Every rule/axiom pair with a witness must be marked as FAILING in the
    published table — otherwise the page and the code disagree."""
    text = (CRITERIA / "README.md").read_text()
    column = {  # axiom -> its 0-based column offset after the rule name
        "pareto": 0, "committee_monotonicity": 1, "support_mono_with": 2,
        "support_mono_without": 3, "consistency": 4, "inclusion_sp": 5,
    }
    label_for = {rule_id: label for label, rule_id in TABLE_RULES}
    rows = {}
    for line in text.splitlines():
        if not line.startswith("| **"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        rows[cells[0].strip("*").replace("é", "e")] = cells[1:]

    for w in WITNESSES:
        label = label_for[w["rule"]].replace("é", "e")
        assert label in rows, f"{label} is not a row of the published table"
        cell = rows[label][column[w["axiom"]]]
        # `?` is legitimate ONLY where the witness needs a particular tiebreak —
        # the two cells (CC, leximax-Phragmen) the book leaves open even though
        # Proposition A.4 hands each a counterexample. Anywhere else a `?` over a
        # reproducing witness means the table is wrong.
        allowed = ("✗", "weak", "cand")
        if w.get("tiebreak_dependent"):
            allowed += ("?",)
        assert cell in allowed, (
            f"{label} / {w['axiom']}: the table says {cell!r}, but a witness "
            f"reproduces a violation ({w['cite']})")


def test_open_cells_are_exactly_the_tiebreak_dependent_ones():
    """The `?` cells and the tiebreak-dependent witnesses must be the same two.

    This is the repo's own finding, so it is the one most worth pinning: Table
    3.1 marks CC and leximax-Phragmen OPEN for inclusion-strategyproofness while
    Proposition A.4's prose lists both as failing. The reconciliation is that
    their counterexamples only pay off under some tiebreaking orders. If a future
    `abcvoting` resolves one of those ties differently, this fails rather than
    letting the page keep an explanation that no longer holds.
    """
    dependent = {w["rule"] for w in WITNESSES if w.get("tiebreak_dependent")}
    assert dependent == {"cc", "leximaxphragmen"}, dependent

    from abc_axiom_check import inclusion_sp_tiebreak_dependence
    for w in WITNESSES:
        if w["axiom"] != "inclusion_sp":
            continue
        dep = inclusion_sp_tiebreak_dependence(
            w["rule"], w["spec"], w["k"], w["voter_index"], w["new_ballot"],
            num_cand=w.get("num_cand"))
        if dep is None:            # honest outcome itself tied — not comparable
            continue
        paying, non_paying = dep
        assert bool(paying and non_paying) == bool(w.get("tiebreak_dependent")), (
            f"{w['rule']}: {len(paying)} paying / {len(non_paying)} non-paying "
            f"tied committees contradicts tiebreak_dependent="
            f"{w.get('tiebreak_dependent', False)}")
