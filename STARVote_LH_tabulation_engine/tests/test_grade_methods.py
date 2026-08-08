"""
test_grade_methods.py
=====================
Answer keys for the **grade-ballot** cases — the files that carry a `grades:`
block instead of `ballots:` because their grades are words (Majority Judgment's
*To Reject … Excellent*) or a scale the LH engine's 0–5 validation refuses
(Felsenthal's 1–10 and A–J).

`test_method_positive.py` skips these on purpose: they are not LH elections, and
running them through that engine would only prove it can't read them. But an
`expected_winners:` nobody checks is worse than none at all — it reads as
verified and isn't — so this runs the tool that *does* count them,
`tools_adam/pref_voting_tabulation_engine/grade_methods_report.py`, and asserts
two things per case:

* the winner under the file's own `grade_method:` matches its answer key;
* the `pref_voting` cross-check printed AGREE — the report computes every number
  twice, by independent code, and this is what makes that mean something.

A case whose grade procedure legitimately disagrees between the two
implementations (MJ's tie-break has two published readings, and they can differ
when medians tie) does not belong here with an answer key; put the divergence on
the page instead.
"""
import re
import subprocess
import sys
from pathlib import Path

import pytest
import yaml

ENGINE_DIR = Path(__file__).resolve().parent.parent
REPO_ROOT = ENGINE_DIR.parent
TOOL = (ENGINE_DIR / "tools_adam" / "pref_voting_tabulation_engine"
        / "grade_methods_report.py")

pytest.importorskip("pref_voting",
                    reason="pref_voting not installed (optional dev dep)")

# Which printed winner line answers for which `grade_method:`.
WINNER_LINE = {
    "majorityjudgment": "Majority Judgment (highest median)",
    "majorityjudgement": "Majority Judgment (highest median)",
    "mj": "Majority Judgment (highest median)",
    "range": "Range Voting (highest mean)",
    "rangevoting": "Range Voting (highest mean)",
}


def _grade_cases():
    for path in sorted(REPO_ROOT.rglob("*.yaml")):
        if any(p.startswith(".") or p.endswith("_tabulated") for p in path.parts):
            continue
        try:
            data = yaml.safe_load(path.read_text(encoding="utf-8"))
        except Exception:
            continue
        if not isinstance(data, dict) or data.get("grades") is None:
            continue
        expected = data.get("expected_winners")
        if not isinstance(expected, list) or not expected:
            continue          # a paradox case with no answer key is fine
        method = str(data.get("grade_method", "")).strip().lower().replace("_", "")
        yield path, expected, method


CASES = list(_grade_cases())
IDS = [str(p.relative_to(REPO_ROOT)) for p, _, _ in CASES]


@pytest.mark.parametrize("path,expected,method", CASES, ids=IDS)
def test_grade_case_elects_expected(path, expected, method):
    assert method in WINNER_LINE, f"{path.name}: unknown grade_method {method!r}"
    r = subprocess.run([sys.executable, str(TOOL), str(path)],
                       capture_output=True, text=True, cwd=str(REPO_ROOT))
    assert r.returncode == 0, f"{path.name} exited {r.returncode}:\n{r.stderr or r.stdout}"

    label = WINNER_LINE[method]
    m = re.search(rf"^Winner — {re.escape(label)}: (.+)$", r.stdout, re.M)
    assert m, f"{path.name}: no '{label}' line in:\n{r.stdout}"
    elected = sorted(w.strip() for w in m.group(1).split("/"))
    assert elected == sorted(expected), (
        f"{path.name}: elected {elected}, expected {expected}")

    # The second, independent count. A case shipped with an answer key must not
    # be one the two implementations disagree about.
    assert "DISAGREE" not in r.stdout, (
        f"{path.name}: pref_voting cross-check disagreed:\n{r.stdout}")


def test_the_word_scale_is_understood_end_to_end():
    """`grade_scale: "a|b|c"` — the form Majority Judgment's own ballot needs.

    Felsenthal's examples are letters and numbers, so the tool ran for a while
    without this; a page teaching the METHOD needs the common language, and a
    silent fallback to letters would quietly reprint the wrong ballot.
    """
    import importlib.util

    spec = importlib.util.spec_from_file_location("grade_methods_report", TOOL)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    scale = mod._scale("To Reject|Poor|Acceptable|Good|Very Good|Excellent")
    assert scale[0] == "To Reject" and scale[-1] == "Excellent" and len(scale) == 6
    assert mod._scale("A-D") == ["A", "B", "C", "D"]
    assert mod._scale("1-3") == [1, 2, 3]
