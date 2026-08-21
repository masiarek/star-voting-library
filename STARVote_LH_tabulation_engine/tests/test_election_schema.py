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


# ===========================================================================
# The emitter, over the whole corpus
# ===========================================================================
#
# The page tests above prove the schema is coherent. These prove the EMITTER is
# faithful, which is a different and stronger claim — and the one a second
# implementation actually depends on.

import subprocess  # noqa: E402
import sys  # noqa: E402

ENGINE_DIR = REPO_ROOT / "STARVote_LH_tabulation_engine"
if str(ENGINE_DIR) not in sys.path:
    sys.path.insert(0, str(ENGINE_DIR))

import election_json  # noqa: E402
from result_json import _expected_winners  # noqa: E402
import starvote_larry_hastings as w  # noqa: E402


def _cases():
    """Every case file the emitter is expected to describe.

    Same walk as tests/test_result_json.py, widened to include the `grades:`
    files — which that contract cannot express and this one can, because
    describing an election is easier than counting one.
    """
    out = []
    for p in sorted(REPO_ROOT.rglob("*.yaml")):
        s = str(p.relative_to(REPO_ROOT))
        if (s.startswith((".claude", ".venv", "site/", "node_modules"))
                or "_tabulated" in s or "negative" in s or "harness_cases" in s):
            continue
        try:
            t = p.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        if not any(k in t for k in ("\nballots:", "\ngrades:")) \
                and not t.startswith(("ballots:", "grades:")):
            continue
        out.append(p)
    return out


CASES = _cases()
SCORED = [p for p in CASES if "\ngrades:" not in p.read_text(encoding="utf-8", errors="replace")]


def _engine_ballots(path):
    """The ballot list the ENGINE parsed — the thing the JSON must preserve."""
    el = w.load_election(str(path))
    cls = w.classify_method(el.get("method_name"), el["ballots"])
    if cls["family"] in ("irv", "stv", "ranked_robin"):
        _names, ballots, _disp, is_ranked = w.ballots_for_pairwise(el["ballots"])
        if is_ranked:
            return ballots
    _h, ballots, _d = w.parse_ballots_from_string(el["ballots"])
    return ballots


def _ballots_from_json(doc):
    """Rebuild the engine's ballot list from the emitted document alone.

    This is what a second implementation does. Markers and blanks collapse to 0
    here — as the engine collapses them — but the DOCUMENT still carries which
    was which, which is the whole reason they are named rather than zeroed.
    """
    ids = [c["id"] for c in doc["candidates"]]
    name = {c["id"]: c["name"] for c in doc["candidates"]}
    out = []
    for row in doc["ballots"]:
        if "scores" in row:
            b = {name[i]: (0 if v is None or isinstance(v, str) else v)
                 for i, v in zip(ids, row["scores"])}
        elif "approvals" in row:
            b = {name[i]: (1 if v is True else 0) for i, v in zip(ids, row["approvals"])}
        elif "marks" in row:
            b = {name[i]: (1 if v else 0) for i, v in zip(ids, row["marks"])}
        elif "ranking" in row:
            depth = len(row["ranking"])
            rank = {}
            for level, group in enumerate(row["ranking"]):
                for cid in group:
                    rank[name[cid]] = depth - level          # top level scores highest
            b = {name[i]: rank.get(name[i], 0) for i in ids}
        else:
            raise AssertionError("ballot row carries no recognised shape")
        out += [b] * row.get("count", 1)
    return out


def test_corpus_discovered():
    assert len(CASES) > 550, f"only {len(CASES)} cases discovered — bad glob?"
    assert len(CASES) - len(SCORED) >= 7, "the grade files went missing"


@pytest.mark.parametrize("path", CASES, ids=lambda p: p.name)
def test_every_case_emits_a_valid_document(path):
    jsonschema.validate(instance=election_json.build(path), schema=SCHEMA)


@pytest.mark.parametrize("path", SCORED, ids=lambda p: p.name)
def test_ballots_reconstruct_exactly(path):
    """The claim the whole contract rests on.

    Validating against a schema proves a document is well-FORMED. It says
    nothing about whether it describes the same election. This does: rebuild the
    engine's own ballot list from the JSON and require it to be identical —
    same ballots, same order, same weights, every case in the library.
    """
    doc = election_json.build(path)
    assert _ballots_from_json(doc) == _engine_ballots(path)


@pytest.mark.parametrize("path", CASES, ids=lambda p: p.name)
def test_row_width_matches_the_roster(path):
    """The rule JSON Schema cannot express, over real files this time."""
    doc = election_json.build(path)
    n = len(doc["candidates"])
    for row in doc["ballots"]:
        for key in ("scores", "approvals", "marks", "grades"):
            if key in row:
                assert len(row[key]) == n, f"{key} is {len(row[key])} wide, {n} candidates"


def test_answer_keys_survive_the_id_mapping():
    """A key that names real candidates must come through as ids, not vanish.

    `expected` is omitted when a name does not resolve — the honest answer for a
    YAML-coerced key, and a silent hole if it ever happened in bulk. Detect the
    key the way the engine does rather than by grepping the text: two case files
    DISCUSS `expected_winners:` in prose while deliberately carrying none, and a
    text match reads those as dropped keys.
    """
    carried, dropped, keyless = [], [], []
    for path in CASES:
        doc = election_json.build(path)
        try:
            key = _expected_winners(path)
        except KeyError:                       # a grade file has no race to find
            raw = json.loads(json.dumps(election_json._raw_yaml(path), default=str))
            key = raw.get("expected_winners")
        if key is None:
            keyless.append(path.name)
            assert "expected" not in doc, f"{path.name}: invented an answer key"
            continue
        (carried if "expected" in doc else dropped).append(path.name)

    assert len(carried) > 550, f"only {len(carried)} answer keys carried through"
    assert not dropped, f"answer keys silently dropped: {dropped[:8]}"

    # The two the format genuinely cannot express — the quorum failure that
    # elects nobody, and the 3-seats/3-candidates race the engine refuses. They
    # carry no `expected_winners:` because the key has no way to say "nobody" or
    # "this must not tabulate". `expected.outcome` in the schema is the slot for
    # them; filling it needs a new key in the CASE FILE, not a change here.
    assert "quorum_fail_demo_c3_b6.yaml" in keyless
    assert "bv2269_t488h9_race_nobody_can_lose.yaml" in keyless


def test_emit_is_pure_json_on_stdout():
    """Same contract as --json: no report, and no `_tabulated` mirror written."""
    case = REPO_ROOT / "01_STAR" / "02_Examples" / "cases" / "09_c4_b100_tennessee-capital.yaml"
    mirror = case.parent / "cases_tabulated"
    before = {p.name: p.stat().st_mtime for p in mirror.glob("*")} if mirror.exists() else {}

    proc = subprocess.run(
        [sys.executable, str(ENGINE_DIR / "starvote_larry_hastings.py"),
         str(case), "--emit-election-json"],
        capture_output=True, text=True, cwd=str(ENGINE_DIR),
    )
    assert proc.returncode == 0, proc.stderr
    doc = json.loads(proc.stdout)          # parses, and is the ONLY thing printed
    assert doc["election"]["method"] == "star"
    assert doc["source"]["file"] == case.name

    after = {p.name: p.stat().st_mtime for p in mirror.glob("*")} if mirror.exists() else {}
    assert after == before, "--emit-election-json wrote a _tabulated mirror"


def test_unknown_method_is_refused_not_guessed():
    """`3-2-1` and Range are describable; a typo is not."""
    import tempfile
    with tempfile.TemporaryDirectory() as d:
        p = Path(d) / "typo.yaml"
        p.write_text(
            "election_title: Typo\nvoting_method: STARR\nnum_winners: 1\n"
            "ballots: |-\n  Ada,Ben\n  5,2\n",
            encoding="utf-8",
        )
        with pytest.raises(election_json.UnsupportedMethod):
            election_json.build(p)


def test_range_0_to_9_keeps_its_scale():
    """The 0-5 cap is a teaching guardrail, not the format's business.

    This engine REFUSES to count a Range 0-9 file. The input contract describes
    it fine, which is the point of a separate module.
    """
    case = REPO_ROOT / "06_Other" / "Range" / "cases" / "range_101_0to9_c3_b5.yaml"
    doc = election_json.build(case)
    assert doc["election"]["ballot"] == {"type": "score", "min": 0, "max": 9}
    jsonschema.validate(instance=doc, schema=SCHEMA)


def test_markers_survive_as_names():
    """A blank and a candidate-abstention are different marks in the document,
    even though both tabulate as zero."""
    case = (REPO_ROOT / "01_STAR" / "04_Real_Elections" / "abstain_bugs" / "cases"
            / "bv655_jfrk9t_equal_opposition.yaml")
    doc = election_json.build(case)
    cells = [v for row in doc["ballots"] for v in row["scores"]]
    assert "abstain_candidate" in cells, cells


def test_grade_file_is_describable_and_transposed():
    """Grade cases have no `_tabulated` mirror and no result-contract entry.
    They still describe cleanly here — one row per VOTER, words not numbers."""
    case = REPO_ROOT / "06_Other" / "Majority_Judgment" / "cases" / "mj_101_c3_b5.yaml"
    doc = election_json.build(case)
    assert doc["election"]["family"] == "grade"
    assert doc["election"]["ballot"]["scale"][0] == "To Reject"
    assert len(doc["candidates"]) == 3          # Alice, Bruno, Cleo
    assert len(doc["ballots"]) == 5             # five VOTERS, not three rows
    assert doc["ballots"][4]["grades"][0] is None   # V5 left Alice ungraded
    jsonschema.validate(instance=doc, schema=SCHEMA)
