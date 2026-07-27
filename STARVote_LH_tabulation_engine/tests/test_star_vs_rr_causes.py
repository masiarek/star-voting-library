"""
test_star_vs_rr_causes.py
=========================
The 30 auto-generated samples in 05_Ranked_Robin/star_vs_rr_divergence/ must
make CAUSE claims the ballots actually support — the cycle chain, the Condorcet
claim, the score rank and the finalist pair each description asserts.

WHY, and how this differs from test_star_vs_rr_labels.py. That test guards every
place a sample NAMES A WINNER, which is what drifted in cycle_C10_fewV29_bloc_2
(7ddde36). This one guards everything else the descriptions assert:

    "no candidate beats all others (A>I>G>A)"
    "F is the Condorcet winner ... but only #9 of 10 by score total
     (1647 vs leader G 1929) ... misses STAR's score finalists (G, C)"

A sample can name both winners correctly — passing every other test — and still
claim a pairwise link that does not exist, or a score rank that is off by one.
For a teaching set whose whole payload IS the cycle chain, that is the claim a
reader is most likely to quote and least able to verify. Nothing checked it.

The self-check tests exist because a checker that cannot fail is worse than no
checker: they corrupt a sample and assert the checker notices. One of them runs
the opposite way — a wrong WINNER with correct causes must come back clean here,
because that is the labels checker's job, not this one's.
"""
import shutil
import sys
from pathlib import Path

import pytest

ENGINE_DIR = Path(__file__).resolve().parent.parent
REPO_ROOT = ENGINE_DIR.parent
sys.path.insert(0, str(ENGINE_DIR / "tools_adam" / "scripts"))

import check_star_vs_rr_causes as checker  # noqa: E402

SAMPLE_DIR = REPO_ROOT / "05_Ranked_Robin" / "star_vs_rr_divergence"

CYCLE_STEM = "cycle_C10_fewV29_bloc_2"
DARKHORSE_STEM = "darkhorse_C03_fewV15_noise_1"


def _samples():
    return sorted(SAMPLE_DIR.glob("*.yaml")) if SAMPLE_DIR.is_dir() else []


SAMPLES = _samples()
IDS = [p.stem for p in SAMPLES]

pytestmark = pytest.mark.skipif(not SAMPLES, reason="divergence sample set not present")


def test_discovery_not_vacuous():
    """If the glob silently stops finding samples, this test would pass by
    checking nothing. The set is 30 files; allow it to grow, not vanish."""
    assert len(SAMPLES) >= 25, f"only {len(SAMPLES)} samples found in {SAMPLE_DIR}"


def test_both_flavours_are_represented():
    """The two cause clauses exercise entirely separate code paths. If the set
    ever lost all of one flavour, half this checker would go untested in the
    parametrised run above without a single test turning red."""
    stems = [p.stem for p in SAMPLES]
    assert any(s.startswith("cycle") for s in stems), "no cycle samples"
    assert any(s.startswith("darkhorse") for s in stems), "no dark-horse samples"


@pytest.mark.parametrize("path", SAMPLES, ids=IDS)
def test_sample_causes_match_ballots(path):
    """Cycle chain, Condorcet claim, score rank/totals and finalist pair all
    hold up against a pairwise matrix built from the ballots."""
    problems = checker.check_file(path)
    assert not problems, f"{path.name}:\n  - " + "\n  - ".join(problems)


# --- self-checks: prove the checker can actually fail ------------------------

def _copy(tmp_path, stem):
    src = SAMPLE_DIR / f"{stem}.yaml"
    if not src.exists():                                  # pragma: no cover
        pytest.skip(f"{stem} not present")
    dst = tmp_path / src.name
    shutil.copy2(src, dst)
    return dst


def _edit(path, old, new):
    text = path.read_text(encoding="utf-8")
    assert old in text, f"fixture text moved — {old!r} not found in {path.name}"
    path.write_text(text.replace(old, new, 1), encoding="utf-8")


def _problems(path):
    return "\n".join(checker.check_file(path))


def test_catches_a_false_cycle_link(tmp_path):
    """Reverse the claimed cycle: every link of a strict cycle run backwards is
    a strict loss, so all three must be reported."""
    yml = _copy(tmp_path, CYCLE_STEM)
    assert not checker.check_file(yml), "fixture was not clean to begin with"
    _edit(yml, "(A>I>G>A)", "(A>G>I>A)")
    out = _problems(yml)
    assert "is false" in out, out


def test_catches_a_cycle_chain_that_does_not_close(tmp_path):
    yml = _copy(tmp_path, CYCLE_STEM)
    _edit(yml, "(A>I>G>A)", "(A>I>G)")
    assert "does not close" in _problems(yml)


def test_catches_a_two_candidate_cycle(tmp_path):
    """A>I>A is not a cycle, it is a contradiction."""
    yml = _copy(tmp_path, CYCLE_STEM)
    _edit(yml, "(A>I>G>A)", "(A>I>A)")
    assert "at least 3" in _problems(yml)


def test_catches_a_cycle_chain_naming_a_non_candidate(tmp_path):
    yml = _copy(tmp_path, CYCLE_STEM)
    _edit(yml, "(A>I>G>A)", "(A>Z>G>A)")
    assert "non-candidate" in _problems(yml)


def test_catches_a_cycle_claim_when_a_condorcet_winner_exists(tmp_path):
    """Give a dark-horse sample (which HAS a Condorcet winner) the cycle prose."""
    yml = _copy(tmp_path, DARKHORSE_STEM)
    text = yml.read_text(encoding="utf-8")
    start = text.index("CAUSE = DARK HORSE")
    end = text.index("See the [Divergence from STAR]")
    yml.write_text(text[:start] + "CAUSE = CONDORCET CYCLE: no candidate beats all "
                   "others (A>B>C>A), so there is no 'right' winner. " + text[end:],
                   encoding="utf-8")
    out = _problems(yml)
    assert "beats every rival head-to-head" in out and "not a cycle" in out, out


def test_catches_a_dark_horse_that_is_not_the_condorcet_winner(tmp_path):
    yml = _copy(tmp_path, DARKHORSE_STEM)
    assert not checker.check_file(yml), "fixture was not clean to begin with"
    _edit(yml, "CAUSE = DARK HORSE: C is the Condorcet winner",
          "CAUSE = DARK HORSE: B is the Condorcet winner")
    assert "is the Condorcet winner, but" in _problems(yml)


def test_catches_a_wrong_score_rank(tmp_path):
    yml = _copy(tmp_path, DARKHORSE_STEM)
    _edit(yml, "but only #3 of 3 by score total", "but only #2 of 3 by score total")
    assert "actual rank is" in _problems(yml)


def test_catches_a_wrong_field_size(tmp_path):
    yml = _copy(tmp_path, DARKHORSE_STEM)
    _edit(yml, "but only #3 of 3 by score total", "but only #3 of 7 by score total")
    assert "claims a field of 7" in _problems(yml)


def test_catches_a_wrong_score_total(tmp_path):
    yml = _copy(tmp_path, DARKHORSE_STEM)
    _edit(yml, "(48 vs leader A 50)", "(47 vs leader A 50)")
    assert "actual total is 48" in _problems(yml)


def test_catches_a_wrong_score_leader(tmp_path):
    yml = _copy(tmp_path, DARKHORSE_STEM)
    _edit(yml, "(48 vs leader A 50)", "(48 vs leader B 50)")
    assert "leads on score" in _problems(yml)


def test_catches_finalists_that_are_not_the_top_two(tmp_path):
    """C is the dark horse precisely because it is NOT a score finalist, so
    naming it as one must fail on both counts."""
    yml = _copy(tmp_path, DARKHORSE_STEM)
    _edit(yml, "misses STAR's score finalists (A, B)",
          "misses STAR's score finalists (B, C)")
    out = _problems(yml)
    assert "are not the top two" in out, out
    assert "MISSES the finalists" in out, out


def test_catches_a_flavour_mismatch_between_filename_and_prose(tmp_path):
    """A file named cycle_* whose description states a dark-horse cause."""
    yml = _copy(tmp_path, DARKHORSE_STEM)
    renamed = yml.parent / yml.name.replace("darkhorse", "cycle")
    yml.rename(renamed)
    assert "filename says 'cycle'" in _problems(renamed)


def test_catches_a_missing_cause_clause(tmp_path):
    yml = _copy(tmp_path, CYCLE_STEM)
    _edit(yml, "CAUSE = CONDORCET CYCLE", "CAUSE = SOMETHING ELSE")
    assert "no recognised CAUSE clause" in _problems(yml)


def test_ignores_a_wrong_winner_that_is_the_labels_checker_s_job(tmp_path):
    """Separation of concerns, asserted rather than assumed: corrupt only the
    winner names and this checker must stay silent — otherwise the two checkers
    overlap and a single failure would be reported twice, in two vocabularies."""
    yml = _copy(tmp_path, CYCLE_STEM)
    text = yml.read_text(encoding="utf-8")
    text = text.replace("(STAR C, RR B)", "(STAR J, RR B)")
    text = text.replace("STAR elects C; Ranked Robin elects B.",
                        "STAR elects J; Ranked Robin elects B.")
    text = text.replace("expected_winners:\n  - C", "expected_winners:\n  - J")
    yml.write_text(text, encoding="utf-8")
    assert not checker.check_file(yml), (
        "the cause checker fired on a pure winner-label error — that belongs to "
        "check_star_vs_rr_labels.py")
