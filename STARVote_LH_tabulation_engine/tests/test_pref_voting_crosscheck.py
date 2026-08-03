"""
test_pref_voting_crosscheck.py
==============================
Cross-checks the LH engine against Eric Pacuit's `pref_voting` library — an
independent, peer-reviewed social-choice package — on the ranked-ballot methods
both compute: **Condorcet, RCV-IRV, Plurality**.

For every cross-checkable single-winner election in the repo we assert the LH
engine and pref_voting agree:
  - **Condorcet** winner always (tie-aware on both sides);
  - **IRV / Plurality** when the result is unambiguous; when pref_voting reports a
    *tie* (a set of co-winners), we only require LH's pick to be *among* them,
    since cross-engine tie-breaking legitimately differs.

pref_voting has no STAR, so STAR's runoff itself isn't checked here — that's the
job of the STAR positive tests. This validates the surrounding ranked machinery.

Skipped entirely if `pref_voting` isn't installed (it's an optional dev dep:
`pip install pref_voting`).
"""
import sys
from pathlib import Path

import pytest

pytest.importorskip("pref_voting",
                    reason="pref_voting not installed (optional dev dep)")

ENGINE_DIR = Path(__file__).resolve().parent.parent
REPO_ROOT = ENGINE_DIR.parent
sys.path.insert(0, str(REPO_ROOT / "STARVote_LH_tabulation_engine" / "tools_adam" / "pref_voting_tabulation_engine"))

from pref_voting_tabulation import crosscheck, discover  # noqa: E402

CROSS_DIRS = [
    str(REPO_ROOT / "01_STAR" / "02_Examples"),
    str(REPO_ROOT / "01_STAR" / "02_Examples" / "runoff_overturns_leader"),
    str(REPO_ROOT / "01_STAR" / "03_Criteria" / "Flat_scores_ties"),
    str(REPO_ROOT / "method_comparisons" / "paradoxes_and_whoops"),
    str(REPO_ROOT / "method_comparisons" / "summability_demo"),
    str(REPO_ROOT / "method_comparisons" / "BV_Library"),
    str(REPO_ROOT / "method_comparisons" / "center_squeeze"),
    str(REPO_ROOT / "method_comparisons" / "monotonicity"),
    str(REPO_ROOT / "method_comparisons" / "split_voting" / "_main"),
    str(REPO_ROOT / "YAML_library" / "1_positive"),
]

FILES = discover(CROSS_DIRS)
IDS = [str(Path(f).relative_to(REPO_ROOT)) for f in FILES]


def test_at_least_some_files_discovered():
    assert len(FILES) >= 20, f"expected many cross-checkable files, got {len(FILES)}"


@pytest.mark.parametrize("path", FILES, ids=IDS)
def test_lh_matches_pref_voting(path):
    result = crosscheck(path)
    bad = {m: (lh, pv) for m, (lh, pv, st) in result.items() if st == "mismatch"}
    assert not bad, (
        f"LH vs pref_voting disagree in {Path(path).name}: "
        + "; ".join(f"{m}: LH={lh} pref_voting={pv}" for m, (lh, pv) in bad.items())
    )


def test_equal_rank_levels_are_parsed_as_ties_not_phantom_candidates(tmp_path):
    """'=' equal-rank levels must become genuine INDIFFERENCE, not a candidate.

    Regression for a parser that split ballots on '>' only, leaving "A=B=D" standing
    as a single phantom candidate — so the whole cross-check ran over a cast that
    never existed and reported confident, wrong winners. The election below has four
    real candidates and every ballot ties at least two of them.

    Asserts what actually matters: the candidate set is exactly the four real names,
    the drawn pairs come out at margin 0, and the Copeland leaders match the LH
    engine's own answer for the same ballots (A and D, both 1-0-2)."""
    from pref_voting_tabulation import parse_election, ranked_profile, format_levels
    from pref_voting.c1_methods import copeland

    f = tmp_path / "equal_levels.yaml"
    f.write_text(
        "voting_method: RankedRobin\nnum_winners: 1\nballots: |-\n"
        "  6:A=B=D>C\n  7:A=C=D>B\n  6:B>C>A=D\n"
    )
    cands, dicts, ranks, _priority, has_ties, _vm = parse_election(str(f))

    assert cands == ["A", "B", "C", "D"], cands          # no "A=B=D" phantom
    assert has_ties is True                              # equal levels are reported
    assert len(dicts) == 19                              # weights expanded
    # Ballots round-trip back to repo notation, levels intact.
    assert format_levels(ranks[0]) == "A=B=D > C"

    prof, keep = ranked_profile(cands, dicts)
    ix = {c: i for i, c in enumerate(keep)}
    # A ties C and D; A beats B by 1. (Same pairwise table the LH engine prints.)
    assert prof.margin(ix["A"], ix["C"]) == 0
    assert prof.margin(ix["A"], ix["D"]) == 0
    assert prof.margin(ix["A"], ix["B"]) == 1
    # Copeland (wins + ½·ties) leaders: A and D, matching the LH engine.
    assert sorted(keep[x] for x in copeland(prof)) == ["A", "D"]
