"""
test_result_json.py
===================
Guards the machine-readable result contract — `result_json.py`, the `--json`
CLI mode, and `star_result.schema.json`.

Why this file exists, in one sentence: the library's 567 answer keys pin the
*winner* and nothing else, so an implementation can get every case right by the
wrong path and never be caught. These tests hold the wider contract — the
rounds, the runoff denominator, the tie-break rung — to the same standard.

What is checked:
  * every ballot-carrying case emits JSON that VALIDATES against the published
    schema (the schema is a contract only if something checks it);
  * every case with an answer key elects the winners that key names, through
    the JSON path specifically — the same claim `test_single_winner_positive`
    makes for the STAR path alone, extended to all six families;
  * the numbers agree with the ENGINE's own, not with a second implementation
    living in the builder (the runoff funnel is recomputed here from the raw
    ballots and must reconcile);
  * `--json` is pure: JSON on stdout, no report, and no `_tabulated` mirror
    written as a side effect;
  * an unsupported method is refused as unsupported, not answered wrongly.
"""

import contextlib
import io
import json
import subprocess
import sys
from pathlib import Path

import pytest

ENGINE_DIR = Path(__file__).resolve().parent.parent
REPO_ROOT = ENGINE_DIR.parent
sys.path.insert(0, str(ENGINE_DIR))

import result_json  # noqa: E402
import starvote  # noqa: E402
import starvote_larry_hastings as w  # noqa: E402

jsonschema = pytest.importorskip("jsonschema")

SCHEMA = json.loads((ENGINE_DIR / "star_result.schema.json").read_text("utf-8"))


def _cases():
    """Every ballot-carrying case file in the teaching tree.

    Deliberately NOT limited to one method or one folder: the point of the
    contract is that it covers whatever the library counts.
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
        if "\nballots:" not in t and not t.startswith("ballots:"):
            continue
        out.append(p)
    return out


CASES = _cases()


def _build(path):
    """Build, or skip when the method is out of this engine's scope.

    Out-of-scope is a real, reportable state — Range at 0–9, CAV, 3-2-1 are
    counted elsewhere in the repo — and it must stay distinguishable from a
    wrong answer, which is what `UnsupportedMethod` is for.
    """
    try:
        return result_json.build(path)
    except result_json.UnsupportedMethod as e:
        pytest.skip(str(e))


def test_at_least_one_case_discovered():
    assert len(CASES) > 400, f"only {len(CASES)} cases discovered — bad glob?"


@pytest.mark.parametrize("path", CASES, ids=lambda p: p.name)
def test_result_validates_against_published_schema(path):
    jsonschema.validate(instance=_build(path), schema=SCHEMA)


@pytest.mark.parametrize(
    "path", [p for p in CASES], ids=lambda p: p.name
)
def test_winners_match_the_files_answer_key(path):
    doc = _build(path)
    if doc["result"]["matches_expected"] is None:
        pytest.skip("no expected_winners in the file")
    assert doc["result"]["matches_expected"], (
        f"{path.name}: JSON winners {doc['result']['winners']} != "
        f"answer key {doc['result']['expected_winners']}"
    )


@pytest.mark.parametrize(
    "path",
    [p for p in CASES if "01_STAR" in str(p)][:60],
    ids=lambda p: p.name,
)
def test_runoff_reconciles(path):
    """total = decided + equal support, and the majority is of the DECIDED.

    This is the arithmetic the printed "Runoff math" funnel shows. Getting it
    wrong is the classic way to overstate a STAR win: quote the winner's share
    of ballots cast rather than of voters who expressed a preference.
    """
    doc = _build(path)
    r = doc["rounds"].get("runoff")
    if not r:
        pytest.skip("no two-finalist runoff")
    a, b = (f["preferred_by"] for f in r["finalists"])
    assert a + b == r["decided_voters"]
    assert r["decided_voters"] + r["equal_support"] == r["ballots_cast"]
    assert r["majority"] == r["decided_voters"] // 2 + 1


def test_json_cli_is_pure(tmp_path):
    """`--json` emits JSON and NOTHING else — and writes no mirror.

    A conformance runner pipes this straight into a parser; one stray "Note:"
    line on stdout breaks every consumer. And a read-only inspection must not
    leave a regenerated `_tabulated` file behind in the caller's tree.
    """
    case = tmp_path / "case.yaml"
    case.write_text(
        "election_title: Tiny\n"
        "voting_method: STAR\n"
        "num_winners: 1\n"
        "ballots: |-\n"
        "  Ada,Ben,Cara\n"
        "  5,2,0\n"
        "  0,4,5\n"
        "  2,5,4\n"
        "expected_winners: [Ben]\n",
        encoding="utf-8",
    )
    r = subprocess.run(
        [sys.executable, str(ENGINE_DIR / "starvote_larry_hastings.py"),
         str(case), "--json"],
        capture_output=True, text=True,
    )
    assert r.returncode == 0, r.stdout + r.stderr
    doc = json.loads(r.stdout)          # raises if anything else was printed
    assert doc["result"]["winners"] == ["Ben"]
    assert doc["result"]["matches_expected"] is True
    jsonschema.validate(instance=doc, schema=SCHEMA)
    assert not list(tmp_path.glob("*_tabulated*")), "--json wrote a mirror"


def test_no_answer_key_is_null_not_false(tmp_path):
    """"We did not check" must not read as "we checked and it passed/failed"."""
    case = tmp_path / "nokey.yaml"
    case.write_text(
        "election_title: No key\n"
        "voting_method: STAR\n"
        "num_winners: 1\n"
        "ballots: |-\n"
        "  Ada,Ben\n"
        "  5,0\n",
        encoding="utf-8",
    )
    doc = result_json.build(case)
    assert doc["result"]["expected_winners"] is None
    assert doc["result"]["matches_expected"] is None


def test_unsupported_method_is_refused_not_guessed(tmp_path):
    case = tmp_path / "weird.yaml"
    case.write_text(
        "election_title: Not ours\n"
        "voting_method: Range\n"
        "num_winners: 1\n"
        "ballots: |-\n"
        "  Ada,Ben\n"
        "  9,0\n",
        encoding="utf-8",
    )
    with pytest.raises(result_json.UnsupportedMethod):
        result_json.build(case)


def test_tiebreak_rung_is_reported(tmp_path):
    """A tie in the Scoring Round must SAY which rung advanced whom.

    Ada and Ben tie at 6; Cara is out. The finalists are settled by the ladder,
    and a result that hid that would be indistinguishable from a clean count.
    """
    case = tmp_path / "tie.yaml"
    case.write_text(
        "election_title: Second-finalist tie\n"
        "voting_method: STAR\n"
        "num_winners: 1\n"
        "ballots: |-\n"
        "  Ada,Ben,Cara\n"
        "  5,3,0\n"
        "  0,3,5\n"
        "  1,0,1\n",
        encoding="utf-8",
    )
    doc = result_json.build(case)
    scores = {r["candidate"]: r["value"] for r in doc["rounds"]["scoring"]}
    assert scores["Ada"] == scores["Ben"] == 6
    tb = doc["tiebreaks"]
    assert tb and tb[0]["stage"] == "finalists"
    assert set(tb[0]["tied"]) >= {"Ada", "Ben"}
    assert tb[0]["rung"] in {"head-to-head", "five-star", "lot"}


# ---------------------------------------------------------------------------
# the LOT rung — the tie the contract used to swallow
# ---------------------------------------------------------------------------
#
# `tiebreaks: []` is a POSITIVE claim that no rung fired, and until 2026-08-21
# the score path made it falsely on 23 cases: the builder could see only the
# finalists ladder `resolve_finalists()` replays for single-winner STAR, so a
# Bloc/PR seat decided by lot — and a single-winner Automatic RUNOFF decided by
# lot — reported nothing at all. These pin both halves.

MULTIWINNER_LOT_CASE = (
    REPO_ROOT / "02_STAR_Bloc" / "02_Examples" / "cases"
    / "b484mbm_tie_every_rung.yaml"
)
SINGLE_WINNER_LOT_CASE = (
    REPO_ROOT / "YAML_library" / "1_positive" / "lot_tiebreak_published_order.yaml"
)


def test_multiwinner_lot_decided_seat_is_reported():
    """Bloc STAR, 3 candidates / 2 seats, tied at every rung: 12 = 12 = 12.

    Nothing in the ballots separates the three, so the lot fills both seats.
    A result that said `tiebreaks: []` here would be claiming the votes decided
    an election the file's own description calls "the smallest election that
    ties all the way down".
    """
    assert MULTIWINNER_LOT_CASE.exists(), f"case moved: {MULTIWINNER_LOT_CASE}"
    doc = result_json.build(MULTIWINNER_LOT_CASE)
    assert doc["election"]["seats"] == 2
    assert doc["result"]["matches_expected"] is True
    tb = doc["tiebreaks"]
    assert tb, "a lot-decided seat reported no tiebreak at all"
    t = tb[0]
    assert t["rung"] == "lot"
    assert set(t["tied"]) == {"Arden", "Blythe", "Corin"}
    assert t["advanced"] == doc["result"]["winners"]
    # The score they tied on, and the round it happened in — a multi-winner
    # entry that named neither would not say which seat was bought by lot.
    assert t["at"] == 12
    assert t["round"] == 1


def test_single_winner_runoff_lot_is_reported():
    """The same gap on the single-winner path, which is the easier one to miss.

    Two candidates tie on score, so they are simply both finalists and there is
    no finalists tie to break — then the runoff ties 1-1, five-star ties, and
    the published lot picks the winner. `resolve_finalists()` sees none of it.
    """
    assert SINGLE_WINNER_LOT_CASE.exists(), f"case moved: {SINGLE_WINNER_LOT_CASE}"
    doc = result_json.build(SINGLE_WINNER_LOT_CASE)
    assert doc["rounds"]["runoff"]["tied"] is True
    tb = doc["tiebreaks"]
    assert tb, "the lot decided the winner and tiebreaks was empty"
    t = tb[0]
    assert t["stage"] == "winner" and t["rung"] == "lot"
    assert t["advanced"] == doc["result"]["winners"]
    # One round, so no round number to report — absent, not zero.
    assert "round" not in t


def test_every_lot_banner_has_a_json_entry():
    """The mirror claim, over the whole score corpus.

    `LotNumberTiebreaker` prints one `[Tiebreaker: Lot Number Priority]` banner
    per tie it breaks. The contract must carry exactly that many `rung: "lot"`
    entries — no more (the finalists ladder replay must not double-count the
    banner it shares) and no fewer. Run as one sweep rather than 300 parametrized
    cases so a regression names every file it broke at once.
    """
    mismatched = []
    for path in CASES:
        el = w.load_election(str(path))
        if w.classify_method(el.get("method_name"), el["ballots"])["family"] != "score":
            continue
        try:
            doc = result_json.build(path)
        except result_json.UnsupportedMethod:
            continue
        _cands, ballots, _ = w.parse_ballots_from_string(el["ballots"])
        buf = io.StringIO()
        loud = w.LotNumberTiebreaker(lot_numbers=el.get("lot_numbers") or [],
                                     silent=False)
        with contextlib.redirect_stdout(buf):
            starvote.election(
                el["method"] or starvote.star, ballots, seats=el["seats"] or 1,
                maximum_score=result_json.MAX_SCORE, tiebreaker=loud,
                verbosity=1, print=lambda *a, **k: None,
            )
        banners = buf.getvalue().count("[Tiebreaker: Lot Number Priority]")
        lots = [t for t in doc["tiebreaks"] if t["rung"] == "lot"]
        if banners != len(lots):
            mismatched.append(f"{path.name}: {banners} banner(s), "
                              f"{len(lots)} lot entr(ies)")
    assert not mismatched, "report and contract disagree:\n  " + "\n  ".join(mismatched)


def test_family_dispatch_uses_one_alias_table():
    """`classify_method` is the single source — the JSON's `family` must be it.

    Copied alias sets were how the dispatch and its consumers drifted; this
    pins the two together.
    """
    assert w.classify_method("Ranked Robin")["family"] == "ranked_robin"
    assert w.classify_method("RCV_IRV")["family"] == "irv"
    assert w.classify_method("STV")["family"] == "stv"
    assert w.classify_method("Approval_Multi_Winner")["family"] == "approval"
    assert w.classify_method("Choose_One")["family"] == "plurality"
    assert w.classify_method("Bloc STAR")["family"] == "score"
    assert w.classify_method("")["family"] == "score"
    # No declared method + ranked ballots still routes to IRV.
    assert w.classify_method("", "A>B>C")["family"] == "irv"
    assert not w.classify_method("STARR")["known"]
