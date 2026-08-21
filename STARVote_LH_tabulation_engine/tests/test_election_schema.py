"""The input contract's own guard.

`star_election.schema.json` describes what a tabulator CONSUMES, the way
`star_result.schema.json` describes what one PRODUCES. Nothing emits it yet
(see 07_Concepts/tabulation_engines/input_schema.md), so the strongest check
available is that the published schema and the published illustrations agree —
plus the handful of semantic rules JSON Schema structurally cannot express.

Three things are asserted here:

1.  Every ```json block on the page validates against the schema. The page's
    later examples are abridged (the envelope is shown once), so a fragment is
    COMPLETED mechanically before validation — schema_version filled in, and a
    candidate list synthesized at the width the ballots imply. The completion is
    deliberately dumb: it adds only what the page elided, so a wrong field name,
    a bad enum value or a mixed ballot set still fails.

2.  The cross-field rules validation cannot reach. JSON Schema has no way to say
    "this array's length equals that array's length", and no way to say "every id
    here appears in the candidates list". Both are real defects a reader would
    hit, so they are checked directly.

3.  The negative cases the design exists to prevent — a ranked row inside a score
    contest, and an `elected` answer key with no winners — must be REJECTED. A
    schema that accepts everything is documentation, not a contract.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

import pytest

jsonschema = pytest.importorskip("jsonschema")

REPO_ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = REPO_ROOT / "STARVote_LH_tabulation_engine" / "star_election.schema.json"
PAGE_PATH = REPO_ROOT / "07_Concepts" / "tabulation_engines" / "input_schema.md"

SCHEMA = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))

# Row key -> the ballot.type it belongs to. One row shape per ballot type, which
# is the whole point of declaring the paper on the election rather than the row.
ROW_KEYS = {
    "scores": "score",
    "approvals": "approval",
    "marks": "choose",
    "ranking": "ranking",
    "grades": "grade",
}


def _json_blocks(text: str) -> list[tuple[int, dict]]:
    """Every ```json fenced block on the page, with the line it starts on."""
    out = []
    for m in re.finditer(r"^```json[^\n]*\n(.*?)^```", text, re.S | re.M):
        line = text[: m.start()].count("\n") + 1
        out.append((line, json.loads(m.group(1))))
    return out


def _widths(doc: dict) -> set[int]:
    """Candidate-count implied by the ballots, for the positional row shapes."""
    widths = set()
    for row in doc.get("ballots", []):
        for key in ("scores", "approvals", "marks", "grades"):
            if key in row:
                widths.add(len(row[key]))
    return widths


def _complete(doc: dict) -> dict:
    """Fill in only what the page abridges: the version line and the roster."""
    doc = json.loads(json.dumps(doc))
    doc.setdefault("schema_version", "1.0.0")
    if "candidates" not in doc:
        widths = _widths(doc)
        if widths:
            n = max(widths)
            names = [f"c{i + 1}" for i in range(n)]
        else:  # ranked ballots name their candidates inline
            names = sorted(
                {cid for row in doc.get("ballots", []) for lvl in row.get("ranking", []) for cid in lvl}
            )
        doc["candidates"] = [{"id": n, "name": n.title()} for n in names]
    return doc


PAGE_TEXT = PAGE_PATH.read_text(encoding="utf-8")
BLOCKS = _json_blocks(PAGE_TEXT)

# A block showing a whole election has an `election` key. A block showing one
# field in isolation (the answer-key forms) does not — those are validated
# against that field's own subschema rather than waved through.
DOCS = [(n, d) for n, d in BLOCKS if "election" in d]
FRAGMENTS = [(n, d) for n, d in BLOCKS if "election" not in d]


def _subschema(key: str) -> dict:
    """One property's schema, carrying $defs so internal $refs still resolve."""
    return {"$defs": SCHEMA["$defs"], **SCHEMA["properties"][key]}


def test_schema_is_valid_draft_2020_12():
    jsonschema.Draft202012Validator.check_schema(SCHEMA)


def test_page_actually_carries_illustrations():
    """Guard against the extraction silently matching nothing."""
    assert len(DOCS) >= 12, f"expected an illustration per method, found {len(DOCS)}"
    assert FRAGMENTS, "the answer-key fragments went missing"


@pytest.mark.parametrize("line,doc", DOCS, ids=[f"L{n}" for n, _ in DOCS])
def test_illustration_validates(line, doc):
    jsonschema.validate(instance=_complete(doc), schema=SCHEMA)


@pytest.mark.parametrize("line,doc", FRAGMENTS, ids=[f"L{n}" for n, _ in FRAGMENTS])
def test_field_fragment_validates(line, doc):
    """Every key in a field fragment is checked against its own subschema."""
    assert doc, f"line {line}: empty fragment"
    for key, value in doc.items():
        assert key in SCHEMA["properties"], f"line {line}: {key!r} is not a field of this schema"
        jsonschema.validate(instance=value, schema=_subschema(key))


@pytest.mark.parametrize("line,doc", DOCS, ids=[f"L{n}" for n, _ in DOCS])
def test_illustration_row_shape_matches_declared_ballot(line, doc):
    """Every row carries the one key its declared ballot type calls for."""
    declared = doc.get("election", {}).get("ballot", {}).get("type")
    if declared is None:  # an `expected`-only fragment
        return
    for row in doc.get("ballots", []):
        present = [k for k in ROW_KEYS if k in row]
        assert len(present) == 1, f"line {line}: row carries {present}, want exactly one"
        assert ROW_KEYS[present[0]] == declared, (
            f"line {line}: {present[0]!r} row in a {declared!r} contest"
        )


@pytest.mark.parametrize("line,doc", DOCS, ids=[f"L{n}" for n, _ in DOCS])
def test_illustration_semantics_json_schema_cannot_express(line, doc):
    """Row width == candidate count, and every id referenced actually exists."""
    doc = _complete(doc)
    ids = [c["id"] for c in doc["candidates"]]
    assert len(ids) == len(set(ids)), f"line {line}: duplicate candidate id"

    for row in doc.get("ballots", []):
        for key in ("scores", "approvals", "marks", "grades"):
            if key in row:
                assert len(row[key]) == len(ids), (
                    f"line {line}: {key} has {len(row[key])} entries, {len(ids)} candidates"
                )
        seen = [cid for lvl in row.get("ranking", []) for cid in lvl]
        assert len(seen) == len(set(seen)), f"line {line}: candidate ranked twice"
        for cid in seen:
            assert cid in ids, f"line {line}: ranking names unknown candidate {cid!r}"

    for cid in doc.get("tiebreak", {}).get("lot_order") or []:
        assert cid in ids, f"line {line}: lot_order names unknown candidate {cid!r}"
    for cid in doc.get("expected", {}).get("winners", []):
        assert cid in ids, f"line {line}: expected winner {cid!r} is not a candidate"


@pytest.mark.parametrize("line,doc", DOCS, ids=[f"L{n}" for n, _ in DOCS])
def test_grade_words_come_from_the_declared_scale(line, doc):
    ballot = doc.get("election", {}).get("ballot", {})
    if ballot.get("type") != "grade":
        return
    scale = set(ballot["scale"])
    for row in doc.get("ballots", []):
        for g in row.get("grades", []):
            assert g is None or g in scale, f"line {line}: grade {g!r} is off the declared scale"


# --- the negatives: what the schema exists to refuse -------------------------

def _valid_star() -> dict:
    return {
        "schema_version": "1.0.0",
        "election": {
            "method": "star", "family": "score", "seats": 1,
            "ballot": {"type": "score", "min": 0, "max": 5},
        },
        "candidates": [{"id": "a", "name": "Ada"}, {"id": "b", "name": "Ben"}],
        "ballots": [{"count": 3, "scores": [5, 2]}],
        "expected": {"outcome": "elected", "winners": ["a"]},
    }


def test_baseline_document_is_accepted():
    """Otherwise the refusals below could pass for the wrong reason."""
    jsonschema.validate(instance=_valid_star(), schema=SCHEMA)


def test_ranked_row_in_a_score_contest_is_refused():
    doc = _valid_star()
    doc["ballots"].append({"count": 9, "ranking": [["a"], ["b"]]})
    with pytest.raises(jsonschema.ValidationError):
        jsonschema.validate(instance=doc, schema=SCHEMA)


def test_elected_without_winners_is_refused():
    doc = _valid_star()
    doc["expected"] = {"outcome": "elected"}
    with pytest.raises(jsonschema.ValidationError):
        jsonschema.validate(instance=doc, schema=SCHEMA)


def test_no_winner_outcome_is_expressible():
    """The gap `expected_winners:` cannot express — two cases here need it."""
    doc = _valid_star()
    doc["expected"] = {"outcome": "no_winner", "reason": "quorum not met"}
    jsonschema.validate(instance=doc, schema=SCHEMA)


def test_score_ballot_requires_a_declared_scale():
    doc = _valid_star()
    del doc["election"]["ballot"]["max"]
    with pytest.raises(jsonschema.ValidationError):
        jsonschema.validate(instance=doc, schema=SCHEMA)


def test_unknown_method_is_refused():
    doc = _valid_star()
    doc["election"]["method"] = "STAR"  # an alias, not the normalized name
    with pytest.raises(jsonschema.ValidationError):
        jsonschema.validate(instance=doc, schema=SCHEMA)


def test_marker_vocabulary_is_closed():
    doc = _valid_star()
    doc["ballots"] = [{"scores": [5, "~"]}]  # the YAML glyph, not the JSON name
    with pytest.raises(jsonschema.ValidationError):
        jsonschema.validate(instance=doc, schema=SCHEMA)


def test_negative_scale_is_allowed():
    """Combined Approval is a real -1/0/+1 ballot; the format must say so."""
    doc = _valid_star()
    doc["election"]["method"] = "cav"
    doc["election"]["ballot"] = {"type": "score", "min": -1, "max": 1}
    doc["ballots"] = [{"count": 4, "scores": [1, -1]}]
    jsonschema.validate(instance=doc, schema=SCHEMA)
