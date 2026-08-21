#!/usr/bin/env python3
"""
election_json.py — the machine-readable ELECTION contract (the input half)
=========================================================================
One case file in, one normalized JSON object out: the contest, the candidates,
and the ballots — described so that a tabulator in any language reads exactly
the election this one does.

**Why this exists.** `result_json.py` made two *counts* comparable. It quietly
assumes the two engines read the same *election*, and carries no field able to
check it. They need not: PyYAML resolves YAML **1.1**, so an unquoted `No`
arrives as `False`, `12:30` as `750` and `007` as `7`; every YAML parser in the
Rust, Go and modern JS ecosystems resolves YAML **1.2** and reads all three as
strings. Identical bytes, two different elections — and the *more correct*
implementation is the one a conformance run scores as divergent.
`source.sha256` cannot see it, because the bytes really did match.

On top of that, `ballots:` is a bespoke DSL inside a YAML block literal: a
header row, `Count:` prefixes, `:`/`x`/`×` weights, `>`/`=` rankings, five
markers, `#,` comment rows, a compact underscore form, and a whitespace-
alignment rescue that 183 of the 612 ballot-carrying files depend on. Every
engine that reads a case file directly must reimplement all of it, exactly.

Emitting this document means that parser has **one implementation, forever, in
Python** — and that the artifact every other engine reads is JSON, which has no
implicit typing at all.

**The rule that keeps it honest, inherited from `result_json.py`:** this module
never re-parses a ballot. Candidates, weights, markers and rank levels all come
back from the same functions the printed report calls — `load_election`,
`classify_method`, `parse_ballots_from_string` (whose `display_rows` are what
preserve a marker), and `ballots_for_pairwise` for ranked ballots. A ballot that
appears here differently from the report is a bug in this file.

**It does not tabulate**, which is the point of a separate module: describing an
election is easier than counting one, so this contract covers methods the result
contract must refuse — Range at 0–9, CAV, and the grade methods, none of which
this engine counts.

Contract, per-method illustrations and design rationale:
    07_Concepts/tabulation_engines/input_schema.md
Machine-readable schema:
    STARVote_LH_tabulation_engine/star_election.schema.json

CLI:  starvote_larry_hastings.py <file.yaml> --emit-election-json
"""

import hashlib
import json
import re
import sys
from pathlib import Path

ENGINE_DIR = Path(__file__).resolve().parent
if str(ENGINE_DIR) not in sys.path:
    sys.path.insert(0, str(ENGINE_DIR))

import starvote_larry_hastings as w  # noqa: E402
from result_json import UnsupportedMethod, _expected_winners  # noqa: E402

# The version of the ELECTION CONTRACT, not of the engine, and independent of
# the result contract's number — the two move for different reasons.
SCHEMA_VERSION = "1.0.0"
SCHEMA_ID = (
    "https://masiarek.github.io/star-voting-library/"
    "STARVote_LH_tabulation_engine/star_election.schema.json"
)

GENERATOR = "starvote_larry_hastings.py --emit-election-json"

# The house scale. A case file does not DECLARE its range anywhere — 0–5 is the
# convention, enforced by validate_star_rows(max_score=5) — so it is assumed and
# then widened to fit the data, which is how a Range 0–9 file keeps its scale.
# Making this explicit in the emitted document is half the reason to emit one.
HOUSE_MAX = 5

# The five markers, by the name a stranger can read. All tabulate as the bottom
# of the scale; what they preserve is what the voter DID, which is the subject
# of several cases here. `-` is a blank and becomes JSON null.
MARKER_NAMES = {
    "-": None,
    "~": "abstain_race",
    "&": "abstain_candidate",
    "?": "spoiled",
    "%": "spoiled_reissued",
}

# `classify_method` normalizes case, hyphens and spaces but deliberately keeps
# ALIASES ("rr", "bloc", "irv", "consensus"). The published contract has one
# name per method, so the aliases collapse here — once, in the emitter — and a
# reader of the JSON never runs an alias table.
SCORE_CANON = {
    "": "star",            # no voting_method: -> the engine's own default
    "star": "star",
    "bloc": "bloc_star",
    "bloc_star": "bloc_star",
    "allocated": "allocated",
    "allocated_score": "allocated",
    "sss": "sss",
    "rrv": "rrv",
    "score": "score",
    "range": "range",
    "cav": "cav",
    "3_2_1": "3_2_1",
}


class UnrepresentableElection(Exception):
    """The file cannot be described in this contract.

    Kept distinct from `UnsupportedMethod` (which means "this engine does not
    COUNT that") because they are different answers: a Range 0–9 file is
    perfectly representable here and simply uncountable there.
    """


# ---------------------------------------------------------------------------
# candidates — identity, separate from display
# ---------------------------------------------------------------------------

def _slug(name):
    """A stable id from a display name, matching the schema's id pattern."""
    s = re.sub(r"[^A-Za-z0-9_.:-]+", "_", str(name).strip().lower()).strip("_")
    return (s or "c")[:64]


def _candidates(names):
    """[{id, name}] with ids made unique.

    The id is what ballots, lot orders and winners reference, so a candidate
    legitimately named `No`, `007` or `12:30` is inert everywhere downstream —
    which is the structural half of the fix this contract exists for.
    """
    out, seen = [], {}
    for name in names:
        base = _slug(name)
        if base in seen:
            seen[base] += 1
            cid = f"{base}_{seen[base]}"
        else:
            seen[base] = 1
            cid = base
        out.append({"id": cid, "name": str(name)})
    return out


def _by_name(cands):
    """name -> id, for resolving a lot order and an answer key."""
    return {c["name"]: c["id"] for c in cands}


# ---------------------------------------------------------------------------
# method
# ---------------------------------------------------------------------------

def _canonical_method(cls, seats):
    """One published name per method, from the family plus the normalized name."""
    fam, norm = cls["family"], (cls["normalized"] or "")
    if fam == "ranked_robin":
        return "ranked_robin"
    if fam == "irv":
        return "rcv_irv"
    if fam == "stv":
        return "stv"
    if fam == "approval":
        return "approval" if seats == 1 else "approval_multi_winner"
    if fam == "plurality":
        # Multi-winner Choose-One is SNTV in this engine (`run_plurality_multi`),
        # and it counts every mark where the single-winner path spoils an
        # overvote — different rules, so they get different names.
        return "plurality" if seats == 1 else "sntv"
    if norm in SCORE_CANON:
        return SCORE_CANON[norm]
    raise UnsupportedMethod(
        f"voting_method {cls['declared']!r} has no name in the election contract"
    )


# ---------------------------------------------------------------------------
# ballots
# ---------------------------------------------------------------------------

def _aggregate(rows):
    """Collapse CONSECUTIVE identical ballots back into counted rows.

    `parse_ballots_from_string` expands a weighted row into that many ballots,
    consecutively, so grouping runs recovers the file's own `12 × 5,0,3` shape
    exactly. Grouping only runs (never the whole list) keeps two separately
    written but identical rows separate, as the file wrote them.
    """
    out = []
    for row in rows:
        if out and out[-1][0] == row:
            out[-1][1] += 1
        else:
            out.append([row, 1])
    return out


def _score_cells(display_row):
    """One score ballot's cells, markers intact, from the report's own echo."""
    cells = []
    for cell in display_row.split(","):
        cell = cell.strip()
        if cell in MARKER_NAMES:
            cells.append(MARKER_NAMES[cell])
        else:
            cells.append(int(cell))
    return cells


def _score_ballots(display_rows):
    return [
        {"count": n, "scores": cells} if n > 1 else {"scores": cells}
        for cells, n in [(_score_cells(r), n) for r, n in _aggregate(display_rows)]
    ]


def _approval_ballots(display_rows):
    """1 -> Yes, 0 -> an explicit No, blank/marker -> neither bubble filled.

    Three states, not two: on the double-bubble paper this library draws, a real
    0 IS a No, and it is a different mark from leaving the candidate alone.
    """
    out = []
    for row, n in _aggregate(display_rows):
        marks = []
        for cell in row.split(","):
            cell = cell.strip()
            marks.append(None if cell in MARKER_NAMES else bool(int(cell)))
        out.append({"count": n, "approvals": marks} if n > 1 else {"approvals": marks})
    return out


def _choose_ballots(display_rows):
    out = []
    for row, n in _aggregate(display_rows):
        marks = []
        for cell in row.split(","):
            cell = cell.strip()
            marks.append(False if cell in MARKER_NAMES else bool(int(cell)))
        out.append({"count": n, "marks": marks} if n > 1 else {"marks": marks})
    return out


def _ranking_ballots(display_rows, name_to_id):
    """Rank levels as sets of ids, from the report's own `A > B=C > D` echo.

    `ballots_for_pairwise` builds each display row as
    `" > ".join("=".join(level))`, so splitting it back is reading that
    function's output rather than re-parsing the source ballots.
    """
    out = []
    for row, n in _aggregate(display_rows):
        levels = []
        for level in row.split(">"):
            group = [name_to_id[c.strip()] for c in level.split("=") if c.strip()]
            if group:
                levels.append(group)
        out.append({"count": n, "ranking": levels} if n > 1 else {"ranking": levels})
    return out


# ---------------------------------------------------------------------------
# grade files — not LH elections at all, so a separate door
# ---------------------------------------------------------------------------

def _grade_scale(raw):
    """`To Reject|Poor|…` — or `1-10` / `A-H`, the two shorthand forms."""
    raw = str(raw).strip()
    if "|" in raw:
        return [g.strip() for g in raw.split("|") if g.strip()]
    m = re.match(r"^(\d+)\s*-\s*(\d+)$", raw)
    if m:
        return [str(i) for i in range(int(m.group(1)), int(m.group(2)) + 1)]
    m = re.match(r"^([A-Za-z])\s*-\s*([A-Za-z])$", raw)
    if m:
        return [chr(c) for c in range(ord(m.group(1)), ord(m.group(2)) + 1)]
    raise UnrepresentableElection(f"grade_scale {raw!r} is not a scale this reads")


def _build_grade(path, data):
    """A `grades:` file: transposed on disk, one row per VOTER here."""
    sys.path.insert(0, str(ENGINE_DIR / "tools_adam" / "scripts"))
    try:
        from build_style_ballot_images import parse_grade_block
    except ImportError as exc:  # pragma: no cover - depends on the tools tree
        raise UnrepresentableElection(f"grade parser unavailable: {exc}") from exc

    scale = _grade_scale(data["grade_scale"])
    notes = data.get("voter_notes") or {}
    # (candidates, one BallotRow per VOTER, voter names) — the block on disk is
    # transposed, and the parser is what transposes it back.
    cast, ballot_rows, _voters = parse_grade_block(data["grades"], scale, notes)
    cands = _candidates(cast)

    ballots = []
    for br in ballot_rows:
        # `.cells` is the grade WORD as written ("" for ungraded); `.scores` is
        # its index on the scale. The word is what the ballot said.
        row = {"grades": [word or None for word in br.cells]}
        if br.note:
            row["note"] = br.note
        ballots.append(row)

    method = str(data.get("grade_method") or "MajorityJudgment").strip().lower()
    method = "majority_judgment" if "majority" in method else "range"
    return {
        "election": {
            "title": data.get("election_title"),
            "declared_method": data.get("grade_method"),
            "method": method,
            "family": "grade",
            "seats": int(data.get("num_winners") or 1),
            "ballot": {"type": "grade", "scale": scale},
        },
        "candidates": cands,
        "ballots": ballots,
        # Not bookkeeping: an ungraded candidate taking the scale floor is the
        # entire mechanism of the truncation paradox.
        "rules": {"ungraded": "bottom_of_scale"},
    }


# ---------------------------------------------------------------------------
# build
# ---------------------------------------------------------------------------

def _raw_yaml(path):
    try:
        import yaml
    except ImportError:  # pragma: no cover
        return {}
    try:
        data = yaml.safe_load(Path(path).read_text(encoding="utf-8"))
    except Exception:
        return {}
    return data if isinstance(data, dict) else {}


def build(path):
    """Read `path` and return the normalized election as a plain dict."""
    path = Path(path)
    raw = _raw_yaml(path)

    if "grades" in raw and "ballots" not in raw:
        doc = _build_grade(path, raw)
    else:
        doc = _build_election(path)

    doc = {
        "$schema": SCHEMA_ID,
        "schema_version": SCHEMA_VERSION,
        "source": {
            "file": path.name,
            "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
            "generator": GENERATOR,
        },
        **doc,
    }

    try:
        expected = _expected_winners(path)
    except KeyError:
        # `_expected_winners` walks for a race, and `_find_race` raises when the
        # file has no `ballots:` block at all — which is every grade file. Their
        # answer key is a plain top-level list.
        expected = raw.get("expected_winners")
        if isinstance(expected, str):
            expected = [expected]
    if expected is not None:
        by_name = _by_name(doc["candidates"])
        ids = [by_name.get(str(x)) for x in expected]
        if all(ids):
            doc["expected"] = {"outcome": "elected", "winners": ids}
        # An unresolvable name means the answer key does not name a candidate on
        # these ballots — which is exactly the YAML-coercion bug this contract
        # exists to make impossible. Say nothing rather than emit a broken
        # reference: absent `expected` asserts nothing, and that is honest.
    return doc


def _build_election(path):
    el = w.load_election(str(path))
    cls = w.classify_method(el.get("method_name"), el["ballots"])
    seats = int(el["seats"] or 1)
    method = _canonical_method(cls, seats)
    family = cls["family"]

    if family in ("irv", "stv", "ranked_robin"):
        names, _b, display_rows, is_ranked = w.ballots_for_pairwise(el["ballots"])
        cands = _candidates(names)
        by_name = _by_name(cands)
        if not is_ranked:
            # A ranked METHOD counting SCORE ballots — legal in this engine, and
            # a different piece of paper, so it must be described as one.
            headers, _bb, srows = w.parse_ballots_from_string(el["ballots"])
            cands = _candidates(headers)
            ballot = _score_spec(srows)
            ballots = _score_ballots(srows)
        else:
            ballots = _ranking_ballots(display_rows, by_name)
            ballot = {
                "type": "ranking",
                "equal_ranks": "allowed" if any("=" in r for r in display_rows) else "forbidden",
                "truncation": "allowed",
            }
    else:
        headers, _b, display_rows = w.parse_ballots_from_string(el["ballots"])
        cands = _candidates(headers)
        if family == "approval":
            ballot = {"type": "approval", "form": "double_bubble"}
            ballots = _approval_ballots(display_rows)
        elif family == "plurality":
            ballot = {
                "type": "choose",
                "marks_allowed": seats,
                # Single-winner Choose-One spoils an overvote; the multi-winner
                # paper counts every mark. Not derivable from one another.
                "overvote": "spoil" if seats == 1 else "count_all",
            }
            ballots = _choose_ballots(display_rows)
        else:
            ballot = _score_spec(display_rows)
            ballots = _score_ballots(display_rows)

    doc = {
        "election": {
            "title": el.get("title"),
            "declared_method": cls["declared"],
            "method": method,
            "family": family,
            "seats": seats,
            "ballot": ballot,
        },
        "candidates": cands,
        "ballots": ballots,
    }

    rules = _rules(family, method)
    if rules:
        doc["rules"] = rules

    lot = [str(x) for x in (el.get("lot_numbers") or [])]
    by_name = _by_name(cands)
    if lot and all(n in by_name for n in lot):
        doc["tiebreak"] = {
            "floor": "published_lot",
            "lot_order": [by_name[n] for n in lot],
        }
    else:
        # The engine's documented fallback when no lot is published: earliest
        # ballot column wins. Stated rather than left for a reader to assume.
        doc["tiebreak"] = {"floor": "candidate_order"}

    if raw_voters := _raw_yaml(path).get("eligible_voters"):
        doc["election"]["eligible_voters"] = int(raw_voters)
    return doc


def _score_spec(display_rows):
    """The scale. A case file never declares one, so 0–5 is assumed and then
    WIDENED to fit the data — which is how a Range 0–9 file keeps its range
    instead of being silently clipped to the teaching guardrail."""
    top = HOUSE_MAX
    for row in display_rows:
        for cell in row.split(","):
            cell = cell.strip()
            if cell not in MARKER_NAMES:
                top = max(top, int(cell))
    return {"type": "score", "min": 0, "max": top}


def _rules(family, method):
    """Only what this engine actually does, and only where the method name alone
    does not settle it. STAR gets nothing, which is a fact about STAR."""
    if family == "ranked_robin":
        # wins + half a draw: what this engine, BetterVoting and pref_voting all
        # score, and NOT what Ranked Robin's published definition literally says.
        return {"copeland_draw_value": 0.5}
    if family == "stv":
        # votes/(seats+1); the Irish/Scottish hand-count rule is one vote higher.
        return {"quota": "droop_exact"}
    return {}


def dumps(path, indent=2):
    return json.dumps(build(path), indent=indent, ensure_ascii=False)


if __name__ == "__main__":  # pragma: no cover
    if len(sys.argv) != 2:
        print("usage: election_json.py <case.yaml>", file=sys.stderr)
        sys.exit(1)
    print(dumps(sys.argv[1]))
