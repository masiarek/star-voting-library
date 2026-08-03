"""
test_json_to_yaml_conversion.py
===============================
Guards the BetterVoting-export -> YAML pipeline (`YAML_library/1_positive/
01_convert_json_yaml.py`). It runs the converter on an ISOLATED copy of a real
BetterVoting JSON export (in pytest's tmp_path, so the repo is never mutated) and
checks that:
  * exactly one YAML file is produced,
  * it has the expected structure (candidates + ballots),
  * the expected-winners step actually ran — non-empty winners, no error in the
    report (this is the regression guard for the `parse_ballots_from_string`
    arity drift that silently emptied the winners),
  * the embedded winners agree with a fresh tabulation of the produced file.
"""

import importlib.util
import shutil
import sys
from pathlib import Path

import pytest
import yaml

ENGINE_DIR = Path(__file__).resolve().parent.parent
REPO_ROOT = ENGINE_DIR.parent
LIB_POS = REPO_ROOT / "YAML_library" / "1_positive"
CONVERTER = LIB_POS / "01_convert_json_yaml.py"
# The frozen real BetterVoting export used as converter input: jfk7pd, the
# live dead-rung-tie election (drawn perm [Ben, Ada] certified Ben). Also
# exercised — via the separate two_way_import tool — by
# test_lot_number_tiebreak.py; here it feeds the YAML_library converter.
SOURCE_JSON = (
    REPO_ROOT
    / "01_STAR" / "03_Criteria" / "tie_break_dead_rung"
    / "lot_random_vs_published_jfk7pd"
    / "lot_random_vs_published_jfk7pd_bv_export.json"
)

sys.path.insert(0, str(ENGINE_DIR))
sys.path.insert(0, str(ENGINE_DIR / "tools_adam"))
import starvote_larry_hastings as engine  # noqa: E402
from scenario_eval import scenario_winners  # noqa: E402


def _load_converter():
    spec = importlib.util.spec_from_file_location("bv_json_converter", CONVERTER)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


@pytest.mark.skipif(
    not CONVERTER.exists(),
    reason="converter not present",
)
def test_bettervoting_json_converts_to_tabulating_yaml(tmp_path):
    # A missing fixture must FAIL, not skip: this test silently skipped for
    # weeks when its original fixture was never committed.
    assert SOURCE_JSON.exists(), (
        f"frozen converter fixture missing: {SOURCE_JSON} — "
        "the converter's end-to-end regression guard cannot run"
    )
    conv = _load_converter()

    # Run on an isolated copy so the repo's files are never touched.
    work_json = tmp_path / SOURCE_JSON.name
    shutil.copy(SOURCE_JSON, work_json)
    conv.convert_election_data(str(work_json), engine)

    # The converter writes into a "_generated/" staging subfolder.
    produced = list((tmp_path / "_generated").glob("*.yaml"))
    assert len(produced) == 1, f"expected exactly one produced YAML, got {produced}"
    yml = produced[0]

    data = yaml.safe_load(yml.read_text(encoding="utf-8"))
    race = data["election"]["races"][0]
    assert str(race["ballots"]).strip(), "no ballots block produced"
    assert race["candidates"], "no candidates produced"

    embedded = [str(w) for w in race["expected_results"]["winners"]]
    report = str(race["expected_results"]["report"])

    # Regression guard: the expected-results step must actually run.
    assert embedded, "converter produced EMPTY expected winners (pipeline broken)"
    assert "Error generating expected results" not in report, report

    # The embedded winners must agree with a fresh tabulation of the produced file.
    winners, _seats = scenario_winners(yml)
    assert sorted(winners) == sorted(embedded), (
        f"produced file tabulates {winners}, but its embedded winners are {embedded}"
    )
    # Known answer for jfk7pd: BV's certified winner Ben, reconstructed from
    # the export's recorded drawn tiebreak order (perm [Ben, Ada]).
    assert embedded == ["Ben"], f"unexpected winners for jfk7pd: {embedded}"
