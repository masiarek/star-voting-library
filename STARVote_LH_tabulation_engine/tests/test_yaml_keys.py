"""
test_yaml_keys.py
=================
Guards the election-YAML top-level schema (check_repo_hygiene.ELECTION_KEYS).

The engine validates unknown method names, lot names, and bloc members with
did-you-mean hints — but it never checked top-level KEYS, so a typo in a
load-bearing key (`expected_winers:`) tabulated fine and silently removed the
case from test discovery. This test makes that class of mistake loud.
"""
import importlib.util
import sys
from pathlib import Path

ENGINE_DIR = Path(__file__).resolve().parent.parent
REPO_ROOT = ENGINE_DIR.parent
HYGIENE = REPO_ROOT / "STARVote_LH_tabulation_engine" / "tools_adam" / "scripts" / "check_repo_hygiene.py"


def _load_hygiene():
    spec = importlib.util.spec_from_file_location("check_repo_hygiene_keys", HYGIENE)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["check_repo_hygiene_keys"] = mod
    spec.loader.exec_module(mod)
    return mod


def test_every_election_yaml_uses_documented_keys():
    mod = _load_hygiene()
    bad = mod.check_top_level_keys()
    assert not bad, (
        f"{len(bad)} unknown top-level YAML key(s):\n"
        + "\n".join(f"  {f}: {msg}" for f, msg in bad)
        + "\n(Fix the typo, or add a genuinely new key to ELECTION_KEYS in "
        "check_repo_hygiene.py AND to the field reference in "
        "07_Concepts/about_this_repo/YAML_authoring_template.md.)"
    )


def test_typoed_key_is_flagged_with_suggestion():
    # The exact silent-failure scenario: a misspelled expected_winners.
    mod = _load_hygiene()
    flagged = mod.unknown_top_level_keys(
        {"voting_method": "STAR", "ballots": "A,B\n5,0", "expected_winers": ["A"]}
    )
    assert flagged, "a typo'd key must be flagged"
    key, hint = flagged[0]
    assert key == "expected_winers"
    assert hint == "expected_winners", f"did-you-mean should fire, got {hint!r}"
