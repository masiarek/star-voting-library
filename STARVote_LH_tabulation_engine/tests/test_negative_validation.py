"""
test_negative_validation.py
===========================
Negative tests: malformed single-winner files must FAIL with a clear, specific
error message (exit code 1) — not a traceback, and not a silent wrong answer.

Fixtures live in `tests/negative_cases/`. Each is a current-schema (flat YAML)
STAR file with one deliberate defect, plus one file that bundles several defects
to confirm they're reported together.

Covers:
  * wrong number of columns (too few / too many)
  * invalid characters / out-of-range scores
  * ranked ballots under a score method
  * single-winner method asked for multiple seats
  * MULTIPLE errors in a single file (all reported before exit)
"""

import subprocess
import sys
from pathlib import Path

import pytest

ENGINE_DIR = Path(__file__).resolve().parent.parent
REPO_ROOT = ENGINE_DIR.parent
WRAPPER = ENGINE_DIR / "starvote_larry_hastings.py"
NEG_DIR = Path(__file__).resolve().parent / "negative_cases"
LIB_NEG_DIR = REPO_ROOT / "YAML_library" / "2_negative"


def _run_cli(path):
    return subprocess.run(
        [sys.executable, str(WRAPPER), str(path)],
        cwd=str(ENGINE_DIR), capture_output=True, text=True,
    )


# fixture filename -> substrings that MUST appear in the error output
SINGLE_ERROR_CASES = {
    "neg_wrong_columns.yaml":  ["Error: STAR ballots use scores 0..5",
                                "has 2 value(s), expected 3"],
    "neg_extra_columns.yaml":  ["has 4 value(s), expected 3"],
    "neg_bad_characters.yaml": ["invalid: Bob=x"],
    "neg_out_of_range.yaml":   ["invalid: Bob=7"],
    "neg_ranked_in_star.yaml": ["is a score-ballot method, but the ballots are ranked"],
    "neg_seats_mismatch.yaml": ["elects a single winner", "seats=3"],
}


@pytest.mark.parametrize(
    "fname,needles", list(SINGLE_ERROR_CASES.items()), ids=list(SINGLE_ERROR_CASES)
)
def test_negative_reports_expected_message(fname, needles):
    proc = _run_cli(NEG_DIR / fname)
    assert proc.returncode == 1, (
        f"{fname}: expected exit 1, got {proc.returncode}\n{proc.stdout}\n{proc.stderr}"
    )
    out = proc.stdout + proc.stderr
    assert "Traceback" not in out, f"{fname}: leaked a traceback:\n{out}"
    for needle in needles:
        assert needle in out, f"{fname}: expected {needle!r} in:\n{out}"


def test_multiple_errors_in_one_file_are_all_reported():
    proc = _run_cli(NEG_DIR / "neg_multiple_errors.yaml")
    assert proc.returncode == 1
    out = proc.stdout + proc.stderr
    assert "Traceback" not in out
    # all three distinct defects appear together (wrong columns + 2 invalids)
    assert "has 2 value(s), expected 3" in out
    assert "invalid: Bob=x" in out
    assert "invalid: Bob=7" in out
    # at least three per-ballot offending lines listed before the single exit
    offending = [l for l in out.splitlines() if l.strip().startswith("ballot ")]
    assert len(offending) >= 3, f"expected >=3 offending-ballot lines:\n{out}"


def test_old_nested_schema_gives_friendly_error_not_traceback():
    """A file in the OLD nested schema (or with no flat 'ballots:') must produce a
    friendly message, not a Python KeyError traceback."""
    proc = _run_cli(NEG_DIR / "neg_old_nested_schema.yaml")
    assert proc.returncode == 1
    out = proc.stdout + proc.stderr
    assert "Traceback" not in out, f"leaked a traceback:\n{out}"
    assert "no 'ballots:' block found" in out
    assert "Minimal example (copy & paste):" in out   # the key-components template


# --- The YAML_library/2_negative fixtures (SELF-DESCRIBING) -------------------
# Every fixture carries its own expected-message contract as comments:
#
#     # expect: <substring that must appear in the error output>
#
# Adding a new negative case = drop in one .yaml with '# expect:' lines.
# No test edit needed; this parametrization discovers it automatically.
def _lib_fixtures():
    cases = []
    for p in sorted(LIB_NEG_DIR.glob("*.yaml")):
        needles = []
        for ln in p.read_text(encoding="utf-8").splitlines():
            m = ln.strip()
            if m.startswith("# expect:"):
                needles.append(m[len("# expect:"):].strip())
        cases.append((p.name, needles))
    return cases


LIB_FIXTURES = _lib_fixtures()


def test_library_discovery_not_vacuous():
    assert len(LIB_FIXTURES) >= 20, "negative library shrank unexpectedly"
    with_expect = [f for f, n in LIB_FIXTURES if n]
    assert len(with_expect) >= 20, "most fixtures should declare '# expect:' lines"


@pytest.mark.parametrize("fname,needles", LIB_FIXTURES,
                         ids=[f for f, _ in LIB_FIXTURES])
def test_yaml_library_negative(fname, needles):
    """Every fixture must exit non-zero, with no traceback, a clear Error, and
    every message substring its '# expect:' lines declare."""
    proc = _run_cli(LIB_NEG_DIR / fname)
    out = proc.stdout + proc.stderr
    assert proc.returncode != 0, (
        f"{fname}: expected non-zero exit (file must be REJECTED)\n{out}"
    )
    assert "Traceback" not in out, f"{fname}: leaked a traceback:\n{out}"
    assert "Error" in out or "error" in out, f"{fname}: no error message:\n{out}"
    for needle in needles:
        assert needle in out, f"{fname}: expected {needle!r} in:\n{out}"
