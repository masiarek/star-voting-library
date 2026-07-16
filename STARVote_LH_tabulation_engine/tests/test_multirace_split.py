"""
test_multirace_split.py
=======================
Two sides of the one-election-per-file rule:

1. ENGINE: a hand-written YAML containing several races must be REJECTED with
   a friendly error (it used to silently count only the first race).
   (The fixture lives in YAML_library/2_negative and is also covered by the
   negative suite; asserted here from the rule's own test for completeness.)

2. CONVERTER: a multi-race BetterVoting JSON export is a POSITIVE scenario —
   the converter must SPLIT it into one canonical YAML per race, each of which
   tabulates cleanly. Synthesized here by duplicating the race inside a real
   frozen export; a genuine multi-race export can replace it later.
"""
import json
import shutil
import subprocess
import sys
from pathlib import Path

ENGINE_DIR = Path(__file__).resolve().parent.parent
REPO_ROOT = ENGINE_DIR.parent
WRAPPER = ENGINE_DIR / "starvote_larry_hastings.py"
LIB_POS = REPO_ROOT / "YAML_library" / "1_positive"
CONVERTER = LIB_POS / "01_convert_json_yaml.py"
NEG_FIXTURE = REPO_ROOT / "YAML_library" / "2_negative" / "neg_two_races_in_one_file.yaml"


def _run(args, cwd):
    return subprocess.run([sys.executable, *args], cwd=str(cwd),
                          capture_output=True, text=True)


def _find_single_race_star_export():
    """Locate a frozen BV export to synthesize the multi-race fixture from.

    The old library fixtures (YAML_library/1_positive/S_W1_N_*.json) migrated
    into the teaching folders as <case>_bv_export.json, so scan the whole repo
    for those instead — case moves then can't strand this test. Filter to the
    shape the synthesis needs: a single-race, single-winner STAR export with
    ballots (the same S/W1 shape the old fixture names encoded)."""
    for p in sorted(REPO_ROOT.rglob("*_bv_export.json")):
        if any(part.startswith(".") or part.endswith("_tabulated")
               for part in p.relative_to(REPO_ROOT).parts):
            continue
        try:
            data = json.loads(p.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            continue
        races = data.get("Election", {}).get("races", [])
        if (len(races) == 1
                and races[0].get("voting_method") == "STAR"
                and races[0].get("num_winners", 1) == 1
                and data.get("Ballots")):
            return p
    return None


def test_engine_rejects_multirace_yaml():
    r = _run([str(WRAPPER), str(NEG_FIXTURE)], ENGINE_DIR)
    out = r.stdout + r.stderr
    assert r.returncode == 1, out
    assert "contains 2 races" in out
    assert "ONE election per file" in out
    assert "Traceback" not in out


def test_converter_splits_multirace_export(tmp_path):
    src_json = _find_single_race_star_export()
    assert src_json is not None, "no frozen BV export found to synthesize from"

    data = json.loads(src_json.read_text(encoding="utf-8"))
    election = data["Election"]          # BV export shape: Election/Ballots/Results
    races = election["races"]
    assert len(races) == 1, "expected a single-race frozen export to duplicate"

    # Second race: same shape, distinct id/title; ballots must reference it,
    # and Results align with races by index — duplicate that entry too.
    import copy
    race2 = copy.deepcopy(races[0])
    old_id = race2.get("race_id")
    race2["race_id"] = "second-race-id"
    race2["title"] = "Second Race"
    races.append(race2)
    for b in data.get("Ballots", []):
        extra = []
        for v in b.get("votes", []):
            if v.get("race_id") == old_id:
                v2 = copy.deepcopy(v)
                v2["race_id"] = "second-race-id"
                extra.append(v2)
        b.get("votes", []).extend(extra)
    results = data.get("Results")
    if isinstance(results, list) and len(results) == 1:
        results.append(copy.deepcopy(results[0]))

    work = tmp_path / "conv"
    work.mkdir()
    shutil.copy(CONVERTER, work / CONVERTER.name)
    (work / "multi_race_export.json").write_text(
        json.dumps(data), encoding="utf-8")

    r = _run([str(work / CONVERTER.name)], work)
    assert r.returncode == 0, f"converter failed:\n{r.stdout}\n{r.stderr}"

    produced = sorted((work / "_generated").glob("*.yaml"))
    assert len(produced) == 2, (
        f"expected 2 YAMLs (one per race), got {len(produced)}:\n"
        + "\n".join(p.name for p in produced) + f"\n{r.stdout}"
    )
    # Every produced YAML must be a valid ONE-race election that tabulates.
    for y in produced:
        rr = _run([str(WRAPPER), str(y)], ENGINE_DIR)
        out = rr.stdout + rr.stderr
        assert rr.returncode == 0, f"{y.name} does not tabulate:\n{out}"
        assert "Traceback" not in out
