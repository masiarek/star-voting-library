"""
test_abif_conversion.py
=======================
Guards the ABIF <-> YAML-grid converter (`tools_adam/convert_abif.py`, the
companion to the ABIF explainer). Checks that:
  * a rated ABIF file (the electorama `test003.abif`) converts to a grid that
    tabulates to the SAME STAR winner (Allie) — the conversion preserves the count;
  * a ranked ABIF file converts to ranked lines that tabulate (Ranked Robin);
  * round-tripping grid -> ABIF -> grid preserves the ballots;
  * the `--operators` ABIF form re-parses to the same ballots;
  * the consistency guards fire (operator contradicting scores; mixed rated/unrated);
  * `--rescale` maps a wide range down into 0-5.
"""

import subprocess
import sys
from pathlib import Path

import pytest

ENGINE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ENGINE_DIR))
sys.path.insert(0, str(ENGINE_DIR / "tools_adam"))

import convert_abif as C  # noqa: E402
from scenario_eval import scenario_winners  # noqa: E402

# The exact electorama testfiles/test003.abif (rated, with >/= operators).
TEST003 = """\
# Case 3 — Scores using = and > as delimiters
12: Allie/5 =Billy/5 >Candace/4 >Dennis/3 =Edith/3 >Frank/2 >Georgie/1 >Harold/0
 7: Georgie/5 >Allie/4 >Dennis/3 =Harold/3 >Candace/2 >Edith/1 >Billy/0 =Frank/0
 5: Frank/5 >Edith/4 =Harold/4 >Billy/3 =Dennis/3 =Georgie/3 >Candace/2 >Allie/0
"""

TENNESSEE_RANKED = """\
42: Memphis > Nashville > Chattanooga > Knoxville
26: Nashville > Chattanooga > Knoxville > Memphis
15: Chattanooga > Knoxville > Nashville > Memphis
17: Knoxville > Chattanooga > Nashville > Memphis
"""


def _winners(tmp_path, yaml_text, name="case.yaml"):
    p = tmp_path / name
    p.write_text(yaml_text, encoding="utf-8")
    winners, _ = scenario_winners(str(p))
    return winners


def _cli_report(tmp_path, yaml_text, name="ranked.yaml"):
    """Tabulate via the engine CLI, which dispatches to Ranked Robin / IRV / etc.
    (scenario_winners only drives the STAR/score path)."""
    p = tmp_path / name
    p.write_text(yaml_text, encoding="utf-8")
    r = subprocess.run([sys.executable, str(ENGINE_DIR / "starvote_larry_hastings.py"),
                        str(p)], capture_output=True, text=True)
    return r.returncode, r.stdout + r.stderr


def test_rated_abif_tabulates_to_same_winner(tmp_path):
    yaml_text, _ = C.abif_to_grid(TEST003)
    assert "voting_method: STAR" in yaml_text
    assert _winners(tmp_path, yaml_text) == ["Allie"]


def test_ranked_abif_tabulates(tmp_path):
    yaml_text, _ = C.abif_to_grid(TENNESSEE_RANKED)
    assert "voting_method: RankedRobin" in yaml_text
    rc, report = _cli_report(tmp_path, yaml_text)
    assert rc == 0
    # Chattanooga is the Condorcet winner of this profile.
    assert "Chattanooga" in report and "Condorcet" in report


def test_round_trip_grid_to_abif_to_grid_preserves_ballots(tmp_path):
    grid_yaml, _ = C.abif_to_grid(TEST003)
    abif = C.grid_to_abif(grid_yaml)               # grid -> ABIF (comma form)
    back, _ = C.abif_to_grid(abif)                 # ABIF -> grid again
    assert _winners(tmp_path, back) == ["Allie"]
    # and the parsed ballot data is identical
    a = C.parse_abif(TEST003)
    b = C.parse_abif(abif)
    assert set(a["candidates"]) == set(b["candidates"])
    assert sorted(a["ballots"]) == sorted(b["ballots"])


def test_operators_form_reparses_identically():
    grid_yaml, _ = C.abif_to_grid(TEST003)
    abif_ops = C.grid_to_abif(grid_yaml, operators=True)   # A/5 > B/4 = C/4 form
    reparsed = C.parse_abif(abif_ops)
    original = C.parse_abif(TEST003)
    assert sorted(reparsed["ballots"]) == sorted(original["ballots"])


def test_operator_contradicting_scores_is_rejected():
    with pytest.raises(C.ABIFError):
        C.parse_abif("3: A/5 > B/6\n")            # '>' but B scores higher


def test_mixed_rated_and_unrated_is_rejected():
    with pytest.raises(C.ABIFError):
        C.parse_abif("A/5 > B > C\n")


def test_rescale_maps_wide_range_into_0_5():
    yaml_text, notes = C.abif_to_grid("5: A/9 > B/6 > C/0\n", rescale=True)
    assert any("rescal" in n for n in notes)
    cells = [int(x) for x in yaml_text.split("A, B, C")[1].split("×")[1].split(",")]
    assert max(cells) <= 5
