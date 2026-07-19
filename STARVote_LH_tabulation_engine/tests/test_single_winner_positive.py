"""
test_single_winner_positive.py
==============================
Positive regression tests for the single-winner STAR example/test cases.

Covers both file schemas: flat (`expected_winners` at top level) and nested
BV/converter (`election.races[0].expected_results.winners`), single-race only.

For every single-winner STAR file that declares an expected winner, we:
  1. run the engine through its CLI (a subprocess) — this is the real path that
     also (re)writes the `*_tabulated/<name>_tabulated.txt` sibling, so the test
     doubles as a check that tabulation succeeds and the _tabulated file is
     produced;
  2. assert the process exits 0;
  3. assert the elected winner equals `expected_winners` (computed with the
     shared, no-print `scenario_eval` helper so we don't parse report text);
  4. assert the `_tabulated` sibling now exists.

Scope: single-winner *score* methods only (voting_method STAR / default).
Ranked (RCV/STV) and Approval files are skipped — they have their own paths.
"""

import shutil
import subprocess
import sys
from pathlib import Path

import pytest
import yaml

ENGINE_DIR = Path(__file__).resolve().parent.parent
REPO_ROOT = ENGINE_DIR.parent
WRAPPER = ENGINE_DIR / "starvote_larry_hastings.py"

# tools_adam holds the shared no-print evaluator used by the engine + tests.
sys.path.insert(0, str(ENGINE_DIR / "tools_adam"))
from scenario_eval import scenario_winners  # noqa: E402

# Folders that hold single-winner example/test cases.
SINGLE_WINNER_DIRS = [
    REPO_ROOT / "01_STAR" / "_main",
    REPO_ROOT / "01_STAR" / "silly_two_cand_STAR",
    REPO_ROOT / "01_STAR" / "runoff_overturns_leader",
    REPO_ROOT / "01_STAR" / "runoff_reversal_bv_cases",
    REPO_ROOT / "01_STAR" / "tie_break_dead_rung",
    REPO_ROOT / "01_STAR" / "tie_break_dead_rung" / "lot_random_vs_published_jfk7pd",
    REPO_ROOT / "01_STAR" / "tie_break_dead_rung" / "three_way_dead_rung_tie",
    REPO_ROOT / "01_STAR" / "exercises",
    REPO_ROOT / "01_STAR" / "Flat_scores_ties",
    REPO_ROOT / "01_STAR" / "iia_cycle_spoiler",
    REPO_ROOT / "01_STAR" / "pet_real_bv_election",
    REPO_ROOT / "01_STAR" / "tie_break_ladder",
    REPO_ROOT / "method_comparisons" / "alaska_2022",
    REPO_ROOT / "method_comparisons" / "alaska_2022_general",
    REPO_ROOT / "method_comparisons" / "center_squeeze",
    REPO_ROOT / "method_comparisons" / "minority_winner",
    REPO_ROOT / "method_comparisons" / "paradoxes_and_whoops",
    REPO_ROOT / "method_comparisons" / "monotonicity",
    REPO_ROOT / "method_comparisons" / "summability_demo",
    REPO_ROOT / "method_comparisons" / "BV_Library",
    REPO_ROOT / "method_comparisons" / "split_voting" / "_main",
    REPO_ROOT / "method_comparisons" / "brams_grading_paradox",
    REPO_ROOT / "YAML_library" / "1_positive",
    REPO_ROOT / "06_Other" / "ballot_style_lab",
]


def _load(path):
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except Exception:
        return None


def _star_single_view(data):
    """Normalize a loaded YAML into (method, num_winners, ballots, winners) for a
    single-winner case, handling BOTH schemas:

      * flat        — top-level `voting_method` / `num_winners` / `ballots` /
                      `expected_winners` (Burlington-style teaching files);
      * nested BV   — `election: { races: [ {voting_method, num_winners, ballots,
                      expected_results: {winners: [...]}} ] }` (converter / BV-backed
                      cases like bv830, bv2212).

    Returns None if `data` isn't a dict, or is a *multi*-race nested file (those are
    covered by the multirace tests, not here)."""
    if not isinstance(data, dict):
        return None
    election = data.get("election")
    if isinstance(election, dict) and "races" in election:
        races = election.get("races")
        if not (isinstance(races, list) and len(races) == 1):
            return None                    # multi-race -> not this suite
        race = races[0]
        if not isinstance(race, dict) or "ballots" not in race:
            return None
        er = race.get("expected_results")
        winners = er.get("winners") if isinstance(er, dict) else None
        return (
            str(race.get("voting_method", "star")).strip().lower(),
            race.get("num_winners", 1),
            str(race.get("ballots", "")),
            winners,
        )
    if "ballots" not in data:
        return None
    return (
        str(data.get("voting_method", "star")).strip().lower(),
        data.get("num_winners", 1),
        str(data.get("ballots", "")),
        data.get("expected_winners"),
    )


def _single_winner_positive_files():
    files = []
    for d in SINGLE_WINNER_DIRS:
        if not d.is_dir():
            continue
        for p in sorted(d.glob("*.yaml")):
            view = _star_single_view(_load(p))
            if view is None:
                continue
            method, num_winners, ballots, ew = view
            if method != "star":          # single-winner STAR only
                continue
            if num_winners not in (1, None):
                continue
            # ranked ballots (A>B>C) -> not a score/STAR file. Strip per-line
            # comments first, so a rank annotation in a comment (e.g.
            # "14:4,3,5,2,1  # Carmen base (C > A > B)") doesn't exclude a
            # genuine score file. (Mirrors the engines' own detection.)
            _ballots = "\n".join(ln.split("#")[0] for ln in ballots.splitlines())
            if ">" in _ballots:
                continue
            if not (isinstance(ew, list) and len(ew) == 1):
                continue
            files.append(p)
    return files


POSITIVE = _single_winner_positive_files()
POSITIVE_IDS = [str(p.relative_to(REPO_ROOT)) for p in POSITIVE]


def _run_cli(path):
    return subprocess.run(
        [sys.executable, str(WRAPPER), str(path)],
        cwd=str(ENGINE_DIR), capture_output=True, text=True,
    )


def _tabulated_sibling(path):
    return path.parent / (path.parent.name + "_tabulated") / (
        path.stem + "_tabulated.txt"
    )


def test_at_least_one_case_discovered():
    assert POSITIVE, "no single-winner positive cases were discovered"


@pytest.mark.parametrize("path", POSITIVE, ids=POSITIVE_IDS)
def test_single_winner_tabulates_and_elects_expected(path, tmp_path):
    expected = _star_single_view(_load(path))[3]

    # Run the CLI on a TEMP COPY so the engine writes its _tabulated artifact
    # into tmp_path, never the tracked repo copy. (The engine derives the output
    # path from the source file's location, so a copy under tmp redirects it.)
    work_dir = tmp_path / "src"
    work_dir.mkdir()
    work = work_dir / path.name
    shutil.copy(path, work)

    # 1-2. Full CLI run: must succeed (this also writes the _tabulated copy).
    proc = _run_cli(work)
    assert proc.returncode == 0, (
        f"{path.name} exited {proc.returncode}\n--- stdout ---\n{proc.stdout}\n"
        f"--- stderr ---\n{proc.stderr}"
    )

    # 3. Winner matches expectation (structured, not text-parsed). Evaluated on
    # the original file; scenario_winners does not write any artifact.
    winners, seats = scenario_winners(path)
    assert seats == 1, f"{path.name}: num_winners should be 1, got {seats}"
    assert sorted(winners) == sorted(str(w) for w in expected), (
        f"{path.name}: elected {winners}, expected {expected}"
    )

    # 4. The _tabulated sibling was produced (in tmp, not the repo).
    tab = _tabulated_sibling(work)
    assert tab.exists(), f"{path.name}: expected _tabulated file at {tab}"
