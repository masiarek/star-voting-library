"""
test_star_vs_rr_labels.py
=========================
The 30 auto-generated samples in 05_Ranked_Robin/02_Examples/star_vs_rr_divergence/ must
name the winners the ENGINE elects — in every place they name one.

WHY. Those samples were labelled from a numpy model of STAR
(06_Other/simulations/star_vs_rr_divergence.py, star_winner()) whose tie-breaks
were not the engine's. One of the 30 came out wrong at birth:
cycle_C10_fewV29_bloc_2 claimed "STAR A" while its own _tabulated mirror printed
"STAR = C" (fixed in 7ddde36). test_method_positive.py caught the yaml's
`expected_winners`, but the wrong TITLE and DESCRIPTION sailed past it — nothing
tested the prose. This test closes that gap: it checks the answer key, the title,
the description, the `_tabulated` mirror and the folder README row, all against a
real tabulation.

The self-check tests exist because a checker that cannot fail is worse than no
checker: they corrupt a sample and assert the checker notices.
"""
import shutil
import sys
from pathlib import Path

import pytest

ENGINE_DIR = Path(__file__).resolve().parent.parent
REPO_ROOT = ENGINE_DIR.parent
sys.path.insert(0, str(ENGINE_DIR / "tools_adam" / "scripts"))

import check_star_vs_rr_labels as checker  # noqa: E402

SAMPLE_DIR = REPO_ROOT / "05_Ranked_Robin" / "02_Examples" / "star_vs_rr_divergence"


def _samples():
    return sorted(SAMPLE_DIR.glob("*.yaml")) if SAMPLE_DIR.is_dir() else []


SAMPLES = _samples()
IDS = [p.stem for p in SAMPLES]

pytestmark = pytest.mark.skipif(not SAMPLES, reason="divergence sample set not present")


def test_discovery_not_vacuous():
    """If the glob silently stops finding samples, this test would pass by
    checking nothing. The set is 30 files; allow it to grow, not vanish."""
    assert len(SAMPLES) >= 25, f"only {len(SAMPLES)} samples found in {SAMPLE_DIR}"


@pytest.mark.parametrize("path", SAMPLES, ids=IDS)
def test_sample_labels_match_engine(path):
    """Answer key, title, description, mirror and README row all name the
    winners a real tabulation produces."""
    problems = checker.check_file(path, checker.readme_table(SAMPLE_DIR))
    assert not problems, f"{path.name}:\n  - " + "\n  - ".join(problems)


# --- self-checks: prove the checker can actually fail ------------------------

def _one_sample_folder(tmp_path, stem="cycle_C10_fewV29_bloc_2"):
    """A minimal copy of the sample set: one yaml + its mirror + a README row."""
    src = SAMPLE_DIR / f"{stem}.yaml"
    if not src.exists():                                  # pragma: no cover
        pytest.skip(f"{stem} not present")
    folder = tmp_path / SAMPLE_DIR.name
    (folder / f"{SAMPLE_DIR.name}_tabulated").mkdir(parents=True)
    shutil.copy2(src, folder / src.name)
    mirror = checker.mirror_path(src)
    if mirror.exists():
        shutil.copy2(mirror, checker.mirror_path(folder / src.name))
    star, rr = checker.engine_winners(src)
    (folder / "README.md").write_text(
        "| flavor | cands | voters | electorate | STAR | RR | IRV | Appr | Plur | file |\n"
        f"| cycle | 10 | 29 | grouped | **{star}** | **{rr}** | B | A | B | "
        f"[`{stem}`](x/{stem}.md) |\n", encoding="utf-8")
    return folder, folder / src.name, star, rr


def _wrong_name(path, correct):
    """Some candidate on the ballot that is NOT the correct answer."""
    header = [c.strip() for c in
              path.read_text(encoding="utf-8").split("ballots: |-")[1]
              .strip().splitlines()[0].split(":")[-1].split(",")]
    return next(c for c in header if c != correct)


def test_checker_catches_a_wrong_answer_key(tmp_path):
    folder, yml, star, _rr = _one_sample_folder(tmp_path)
    wrong = _wrong_name(yml, star)
    text = yml.read_text(encoding="utf-8")
    yml.write_text(checker.KEY_SITE.sub(lambda m: m.group(1) + wrong, text, count=1),
                   encoding="utf-8")
    problems = checker.check_file(yml, checker.readme_table(folder))
    assert any("expected_winners" in p for p in problems), problems


def test_checker_catches_wrong_prose_even_when_the_key_is_right(tmp_path):
    """The exact hole that let 7ddde36's bad title and description survive:
    expected_winners correct, the prose still naming the model's answer."""
    folder, yml, star, _rr = _one_sample_folder(tmp_path)
    wrong = _wrong_name(yml, star)
    text = yml.read_text(encoding="utf-8")
    text = text.replace(f"(STAR {star},", f"(STAR {wrong},")
    text = text.replace(f"STAR elects {star};", f"STAR elects {wrong};")
    yml.write_text(text, encoding="utf-8")

    problems = checker.check_file(yml, checker.readme_table(folder))
    assert any("election_title" in p for p in problems), problems
    assert any("description headline" in p for p in problems), problems
    assert not any("expected_winners" in p for p in problems), (
        "the answer key was left correct — only the prose should be flagged")


def test_fix_repairs_labels_and_leaves_clean_files_untouched(tmp_path):
    folder, yml, star, _rr = _one_sample_folder(tmp_path)
    original = yml.read_text(encoding="utf-8")
    wrong = _wrong_name(yml, star)
    yml.write_text(original.replace(f"(STAR {star},", f"(STAR {wrong},")
                   .replace(f"STAR elects {star};", f"STAR elects {wrong};"),
                   encoding="utf-8")

    changed, notes = checker.fix_file(yml)
    assert changed and not notes, notes
    assert yml.read_text(encoding="utf-8") == original, (
        "--fix must restore the file byte-for-byte, adding no whitespace drift")
    assert not checker.check_file(yml, checker.readme_table(folder))

    # a second pass on an already-correct file must be a no-op
    changed_again, _ = checker.fix_file(yml)
    assert not changed_again, "--fix churned a file whose labels were already right"
