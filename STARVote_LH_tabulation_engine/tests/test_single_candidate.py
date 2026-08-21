"""An unopposed race elects the candidate, not the first letter of their name.

`_star_round` short-circuits when only one candidate is on the ballot — "Only
one candidate, they win." — and returned `list(scores)[0][0]`. But
`_scoring_round` hands back a **dict** (`_sort_score_dict` rebuilds one), so
`list(scores)[0]` is already the candidate's name and the second index took its
first CHARACTER: an unopposed race for `Ada` elected `A`, and one for `Zebra`
elected `Z`.

It survived because nothing in this library has a one-candidate race — every
ballot-carrying case is contested — so the whole suite was blind to it, while an
uncontested seat is among the most ordinary things a real ballot carries. Found by [`tools_adam/tie_taxonomy_sweep.py`](../tools_adam/tie_taxonomy_sweep.py)
probing degenerate shapes; fixed in the vendored engine (FORK_NOTES.md).

The name is deliberately multi-character in every assertion here: a
single-letter candidate would pass even with the bug.
"""

import sys
from pathlib import Path

import pytest

ENGINE_DIR = Path(__file__).resolve().parent.parent
if str(ENGINE_DIR) not in sys.path:
    sys.path.insert(0, str(ENGINE_DIR))

import starvote                       # noqa: E402
import starvote_larry_hastings as w   # noqa: E402


def _ballots(text):
    return w.parse_ballots_from_string(text)[1]


@pytest.mark.parametrize("name", ["Ada", "Zebra", "Nashville", "Chocolate Chip"])
def test_unopposed_race_elects_the_whole_name(name):
    result = starvote.election(starvote.star, _ballots(f"{name}\n5\n0\n"),
                               maximum_score=5)
    assert result == [name]


def test_unopposed_race_wins_on_zero_score_too():
    """Nobody scored the only candidate. They still win — there is no one else."""
    assert starvote.election(starvote.star, _ballots("Ada\n0\n0\n"),
                             maximum_score=5) == ["Ada"]


def test_the_json_contract_agrees(tmp_path):
    """The machine-readable result must carry the same name the report prints."""
    import result_json
    case = tmp_path / "unopposed.yaml"
    case.write_text(
        "election_title: Unopposed\n"
        "voting_method: STAR\n"
        "num_winners: 1\n"
        "ballots: |-\n  Ada\n  5\n  3\n",
        encoding="utf-8")
    doc = result_json.build(case)
    assert doc["result"]["winners"] == ["Ada"]
    assert doc["election"]["candidates"] == ["Ada"]
