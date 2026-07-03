"""
test_range_tabulation.py
========================
Guards the Range / Score voting engine (Range_tabulation_engine/range_tabulation.py,
which wraps pref_voting's score_voting and cross-checks a hand sum).

Skips cleanly if the engine's dependencies (pyrankvote for the shared score-grid
parser, and/or pref_voting) aren't installed — the engine is optional, like the
pref_voting cross-check engine.
"""
import subprocess
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
ENGINE = REPO_ROOT / "Range_tabulation_engine" / "range_tabulation.py"

# The engine wires its own path to the vendored RCV score-grid parser and only
# needs the stdlib for the hand count (pref_voting is an optional cross-check),
# so the winner is always computable — run it via subprocess like the other
# engine tests.

CASES = [
    ("06_Other/Range/range_101_c3_b5.yaml", "Beth"),
    ("method_comparisons/black_curtain/Black_Curtain_01_c3_b5_hidden-consensus.yaml", "Bob"),
    ("method_comparisons/black_curtain/Black_Curtain_02_c3_b5_near-clones.yaml", "Cal"),
    ("method_comparisons/black_curtain/Black_Curtain_03_c3_b5_polarized-on-cal.yaml", "Ann"),
    ("method_comparisons/black_curtain/Black_Curtain_04_c4_b5_four-candidates.yaml", "Cal"),
]


def _winner(stdout):
    lines = stdout.splitlines()
    for i, ln in enumerate(lines):
        if ln.startswith("Winner — Range"):
            for nxt in lines[i + 1:]:
                if nxt.strip():
                    return nxt.strip()
    return None


@pytest.mark.parametrize("rel,expected", CASES, ids=[c[0].split("/")[-1] for c in CASES])
def test_range_elects_expected(rel, expected):
    path = REPO_ROOT / rel
    r = subprocess.run([sys.executable, str(ENGINE), str(path)],
                       capture_output=True, text=True)
    assert r.returncode == 0, f"{rel} exited {r.returncode}:\n{r.stderr or r.stdout}"
    assert _winner(r.stdout) == expected, f"{rel}: got {_winner(r.stdout)!r}, expected {expected!r}"


def test_pref_voting_crosscheck_agrees_when_present():
    """When pref_voting is installed, its score_voting must agree with the hand sum."""
    pytest.importorskip("pref_voting")
    path = REPO_ROOT / "06_Other/Range/range_101_c3_b5.yaml"
    r = subprocess.run([sys.executable, str(ENGINE), str(path)],
                       capture_output=True, text=True)
    assert r.returncode == 0, r.stderr or r.stdout
    assert "✓ agrees with the hand count" in r.stdout, (
        "pref_voting cross-check did not agree:\n" + r.stdout)
