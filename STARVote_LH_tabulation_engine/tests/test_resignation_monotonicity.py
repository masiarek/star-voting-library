"""
test_resignation_monotonicity.py
================================
Gates `04_Approval/03_Criteria/resignation_monotonicity.md`.

The page makes two kinds of claim and they need different protection:

1. **The paper's claims** (Oh & Peters, arXiv:2608.06156) — PAV, CC, Monroe,
   leximax-Phragmén and Minimax AV lose a survivor on Example 3.2; PAV,
   seq-Phragmén and Equal Shares lose four of them on Example 3.3; plain AV keeps
   everyone. Those are replayed through `abcvoting`, so a change in that library
   (or a fat-fingered profile) fails here rather than quietly making the page
   wrong.

2. **This repo's own claims** — that Allocated Score, Sequentially Spent Score
   and Reweighted Range Voting fail the same axiom on score ballots, and that the
   failure is not a tie-breaking artefact. That second half is the fragile part:
   the same profiles look like violations OR not depending on how ties fall, so
   every verdict is taken over all tie-breaking orders and pinned here.

The four case files are checked to still be the elections the page describes —
a matched before/after pair only teaches anything while the "after" file really
is the "before" file minus one column.
"""
import pathlib
import sys

import pytest

ENGINE_DIR = pathlib.Path(__file__).resolve().parents[1]
REPO_ROOT = ENGINE_DIR.parent
sys.path.insert(0, str(REPO_ROOT / "06_Other/abcvoting_tabulation_engine"))

import resignation_check as rc  # noqa: E402

CASES = REPO_ROOT / "04_Approval/03_Criteria/cases"
PAGE = REPO_ROOT / "04_Approval/03_Criteria/resignation_monotonicity.md"


def test_discovery_not_vacuous():
    """An empty witness list would make every other test in here pass."""
    assert len(rc.SCORE_WITNESSES) >= 4
    assert {w["rule"] for w in rc.SCORE_WITNESSES} == {"allocated", "sss", "rrv"}


@pytest.mark.parametrize(
    "witness", rc.SCORE_WITNESSES, ids=[w["rule"] + ":" + w["label"][:28]
                                        for w in rc.SCORE_WITNESSES])
def test_score_witness_reproduces(witness):
    """Each score-rule violation still holds under EVERY tie-breaking order."""
    ok, lines = rc.check_score(witness)
    assert ok, "\n".join(lines)


def test_bloc_star_is_not_claimed_to_fail():
    """Bloc STAR is the page's one score-rule pass, and it is evidence, not a
    theorem — so the thing to pin is that no witness has been found for it."""
    assert "bloc" not in {w["rule"] for w in rc.SCORE_WITNESSES}
    assert rc.search("bloc", 300, seed=20260822) is None


@pytest.mark.parametrize("witness", [rc.EX_3_2, rc.EX_3_3, rc.AV_CONTROL],
                         ids=["ex3.2", "ex3.3", "ex3.3-av-control"])
def test_paper_witness_reproduces(witness):
    pytest.importorskip("abcvoting")
    ok, lines = rc.check_abc(witness)
    assert ok, "\n".join(lines)


def test_perfect_representation_witness():
    """Proposition 3.5 is a claim about the AXIOM, not about a rule: both
    {c1,c2} and {c3,c4} are perfectly representative, and after c1 resigns only
    one of them is."""
    ok, lines = rc.check_pr(rc.PROP_3_5)
    assert ok, "\n".join(lines)


def test_av_is_the_only_rule_that_holds_on_example_3_3():
    """Theorem 3.1's content, on the paper's own profile: every proportional
    rule tested loses the four survivors; AV keeps them."""
    pytest.importorskip("abcvoting")
    w = rc.EX_3_3
    after = rc.resign(w["voters"], w["cands"], w["resigner"])
    for rule_id in list(w["rules"]) + ["av"]:
        before = rc.abc_outcomes(rule_id, w["voters"], w["cands"], w["k"])
        outs = rc.abc_outcomes(rule_id, *after, w["k"])
        held = any(rc.survivors_retained(outs, W, w["resigner"])
                   for W in before if w["resigner"] in W)
        assert held == (rule_id == "av"), rule_id


BEFORE_AFTER = [
    ("resign_star_pr_seated_c4_b5.yaml",
     "resign_star_pr_after_bruno_c3_b5.yaml", "Bruno"),
    ("resign_rrv_seated_c5_b5.yaml",
     "resign_rrv_after_hana_c4_b5.yaml", "Hana"),
    ("resign_av_holds_c7_b5.yaml",
     "resign_av_holds_after_kai_c6_b5.yaml", "Kai"),
]


@pytest.mark.parametrize("before_file,after_file,resigner", BEFORE_AFTER,
                         ids=[b.split(".")[0] for b, _, _ in BEFORE_AFTER])
def test_after_file_is_the_before_file_minus_one_column(
        before_file, after_file, resigner):
    """The pair must be the SAME election with one candidate struck.

    Nothing else would catch a drift: each file tabulates fine on its own, and a
    silently different ballot block would turn the lesson into two unrelated
    elections that happen to sit next to each other.
    """
    import yaml
    before = yaml.safe_load((CASES / before_file).read_text())
    after = yaml.safe_load((CASES / after_file).read_text())
    assert before["num_winners"] == after["num_winners"]
    assert before["voting_method"] == after["voting_method"]

    def rows(doc):
        body = [ln.split("#")[0].strip()
                for ln in doc["ballots"].strip().splitlines()]
        header = [c.strip() for c in body[0].split(",")]
        return header, [[c.strip() for c in ln.split(",")] for ln in body[1:]]

    hb, rb = rows(before)
    ha, ra = rows(after)
    assert resigner in hb and resigner not in ha, (
        f"{resigner} should be struck from {after_file} and only there")
    assert ha == [c for c in hb if c != resigner]
    drop = hb.index(resigner)
    assert ra == [[s for j, s in enumerate(row) if j != drop] for row in rb], (
        "the after file's ballots are not the before file's minus one column")


def test_page_states_which_rules_fail():
    """The page's verdict table and the code's witnesses must not drift apart."""
    text = PAGE.read_text()
    for name in ("Allocated Score", "Sequentially Spent Score",
                 "Reweighted Range Voting", "Bloc STAR"):
        assert name in text, f"{name} is not mentioned on the page"
    assert "arXiv:2608.06156" in text
    for stem, _after, _r in BEFORE_AFTER:
        assert stem in text, f"{stem} is not linked from the page"
