"""
test_pyyaml_fallback.py
=======================
The engine must stay usable on a bare system python3 with no PyYAML installed
(CLAUDE.md explicitly allows quick checks with it): load_election() then falls
back to the built-in `_yaml_lite` reader. These tests run the real CLI in a
subprocess with the `yaml` module HIDDEN (sys.modules['yaml'] = None makes
`import yaml` raise ImportError even though the test venv has PyYAML) and pin
the fallback contract:

  1. inline '# comments' after a value are stripped, as real YAML would —
     `voting_method: STAR   # note` must tabulate as STAR, not exit 1 with
     "unknown voting_method 'STAR   # note'";
  2. block-scalar text fields (scenario_description) and the plain
     election_title are carried into the report, not silently dropped;
  3. option values survive their inline comments (matrix_finalists_only);
  4. the run announces itself loudly — a PyYAML warning on stderr;
  5. an EXISTING _tabulated mirror is never overwritten by a degraded run
     (the lite reader still ignores blocs / lot_numbers / quorum, so a
     degraded rewrite could silently strip content from a committed mirror);
     a brand-new mirror may still be created — there is nothing to clobber;
  6. control: the same file under normal PyYAML DOES rewrite the mirror, so
     the degraded-mode guard cannot be over-broad.

Everything runs on temp copies; no repo mirror is touched.
"""

import shutil
import subprocess
import sys
from pathlib import Path

import pytest

ENGINE_DIR = Path(__file__).resolve().parent.parent
REPO_ROOT = ENGINE_DIR.parent
WRAPPER = ENGINE_DIR / "starvote_larry_hastings.py"

# The file from the original bug report: `voting_method: STAR   # STAR Voting
# - Single-winner` plus a `scenario_description: |-` block scalar.
REAL_CASE = (REPO_ROOT / "01_STAR" / "02_Examples" / "cases"
             / "03b_c3_b3_1_style-protest-vote.yaml")

# Synthetic case exercising every trouble spot in one small file.
# STAR: scores Ann 12, Bob 14, Cal 3 -> finalists Ann & Bob; runoff Bob 2-1.
CASE = """\
election_title: Fallback smoke — comments & block scalars
scenario_description: |-
  Two lines of description that the PyYAML-less fallback
  must carry into the tabulation report.

options:
  show_description: true    # shown on screen so stdout can be asserted
  show_matrix: true         # matrix on, so the next option is observable
  matrix_finalists_only: true   # inline comment must not corrupt the value
  collapse_ballots: true    # inline comment must not turn this into junk

voting_method: STAR   # inline comment must be stripped (the reported bug)
num_winners: 1
ballots: |-
  Ann,Bob,Cal
  5,4,0
  3,5,2
  4,5,1
"""

DESCRIPTION_SNIPPET = "must carry into the tabulation report"


def _run_cli_no_pyyaml(target):
    """Run the engine CLI in a subprocess with the yaml module hidden."""
    code = (
        "import sys, runpy\n"
        "sys.modules['yaml'] = None   # 'import yaml' -> ImportError\n"
        f"sys.path.insert(0, {str(ENGINE_DIR)!r})\n"
        f"sys.argv = [{str(WRAPPER)!r}, {str(target)!r}]\n"
        f"runpy.run_path({str(WRAPPER)!r}, run_name='__main__')\n"
    )
    return subprocess.run(
        [sys.executable, "-c", code],
        cwd=str(ENGINE_DIR), capture_output=True, text=True,
    )


def _run_cli_normal(target):
    return subprocess.run(
        [sys.executable, str(WRAPPER), str(target)],
        cwd=str(ENGINE_DIR), capture_output=True, text=True,
    )


def _write_case(tmp_path):
    work_dir = tmp_path / "case"
    work_dir.mkdir()
    work = work_dir / "fallback_smoke.yaml"
    work.write_text(CASE, encoding="utf-8")
    return work


def _tabulated_sibling(path):
    return path.parent / (path.parent.name + "_tabulated") / (
        path.stem + "_tabulated.txt"
    )


def test_fallback_strips_inline_comments_and_keeps_text_fields(tmp_path):
    work = _write_case(tmp_path)
    proc = _run_cli_no_pyyaml(work)

    assert proc.returncode == 0, (
        f"fallback run exited {proc.returncode}\n--- stdout ---\n{proc.stdout}"
        f"\n--- stderr ---\n{proc.stderr}"
    )
    # 1. the commented voting_method parsed as STAR (the reported failure).
    assert "unknown voting_method" not in proc.stdout + proc.stderr
    assert "Bob" in proc.stdout  # the STAR winner was actually elected

    # 2. title (plain scalar) and description (|- block scalar) reach stdout.
    assert "Fallback smoke — comments & block scalars" in proc.stdout
    assert DESCRIPTION_SNIPPET in proc.stdout

    # 3. matrix_finalists_only survived its inline comment: the on-screen
    # matrix shows only the two finalists — no 'Cal >' row.
    assert "Ann >" in proc.stdout and "Bob >" in proc.stdout
    assert "Cal >" not in proc.stdout

    # 4. the run declares itself degraded, loudly, on stderr.
    assert "PyYAML" in proc.stderr


def test_fallback_on_real_repo_file_from_bug_report(tmp_path):
    if not REAL_CASE.exists():
        pytest.skip(f"repo case moved: {REAL_CASE}")
    work_dir = tmp_path / "case"
    work_dir.mkdir()
    work = work_dir / REAL_CASE.name
    shutil.copy(REAL_CASE, work)

    proc = _run_cli_no_pyyaml(work)
    assert proc.returncode == 0, (
        f"exited {proc.returncode}\n--- stdout ---\n{proc.stdout}"
        f"\n--- stderr ---\n{proc.stderr}"
    )
    assert "unknown voting_method" not in proc.stdout + proc.stderr
    assert "Almond" in proc.stdout  # its expected winner


def test_degraded_run_creates_fresh_mirror_with_description(tmp_path):
    work = _write_case(tmp_path)
    proc = _run_cli_no_pyyaml(work)
    assert proc.returncode == 0

    tab = _tabulated_sibling(work)
    assert tab.exists(), "a brand-new mirror should still be written"
    # The mirror embeds the original file too, so check the RESULTS section
    # specifically: the block-scalar description must appear in the rendered
    # report, not only in the source echo.
    results = tab.read_text(encoding="utf-8").split("TABULATION RESULTS", 1)[1]
    assert DESCRIPTION_SNIPPET in results


def test_degraded_run_never_overwrites_existing_mirror(tmp_path):
    work = _write_case(tmp_path)
    tab = _tabulated_sibling(work)
    tab.parent.mkdir(parents=True)
    sentinel = "SENTINEL: committed mirror content — must survive a degraded run\n"
    tab.write_text(sentinel, encoding="utf-8")

    proc = _run_cli_no_pyyaml(work)
    assert proc.returncode == 0
    assert tab.read_text(encoding="utf-8") == sentinel, (
        "a PyYAML-less (degraded) run overwrote an existing _tabulated mirror"
    )
    assert "left untouched" in proc.stderr


def test_normal_pyyaml_run_still_rewrites_mirror(tmp_path):
    # Control for the guard above: with PyYAML available the mirror must be
    # regenerated as always.
    work = _write_case(tmp_path)
    tab = _tabulated_sibling(work)
    tab.parent.mkdir(parents=True)
    sentinel = "SENTINEL: stale mirror content\n"
    tab.write_text(sentinel, encoding="utf-8")

    proc = _run_cli_normal(work)
    assert proc.returncode == 0, (
        f"exited {proc.returncode}\n--- stdout ---\n{proc.stdout}"
        f"\n--- stderr ---\n{proc.stderr}"
    )
    content = tab.read_text(encoding="utf-8")
    assert content != sentinel, "normal run should have rewritten the mirror"
    assert "TABULATION RESULTS" in content
