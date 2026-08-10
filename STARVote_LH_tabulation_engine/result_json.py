#!/usr/bin/env python3
"""
result_json.py — the machine-readable result contract
=====================================================
One election file in, one JSON object out: winners, the rounds that produced
them, the pairwise matrix, and which tie-break rung fired.

**Why this exists.** The library's 567 answer keys pin the *winner* and nothing
else, and its cross-checks against other engines are run from here, by hand,
against printed text. A second implementation — in Rust, in TypeScript, a
student's — has nothing to diff against. This is that thing: emit it from both
engines and conformance becomes `diff`, not eyeballing.

**The rule that keeps it honest:** this module NEVER re-derives a count. Every
number comes from the same function the printed report calls —
`starvote._scoring_round`, `resolve_finalists`, `ranked_robin_tally`,
`approval_tally`, `first_choice_counts`, `rcv_irv_tabulation.tabulate`. A
number that appears here and not there is a bug in this file.

Contract, versioning and worked examples:
    07_Concepts/tabulation_engines/result_schema.md
Machine-readable schema:
    STARVote_LH_tabulation_engine/star_result.schema.json

CLI:  starvote_larry_hastings.py <file.yaml> --json
"""

import hashlib
import json
import sys
from pathlib import Path

ENGINE_DIR = Path(__file__).resolve().parent
if str(ENGINE_DIR) not in sys.path:
    sys.path.insert(0, str(ENGINE_DIR))

import starvote  # noqa: E402
import starvote_larry_hastings as w  # noqa: E402

# The version of the RESULT CONTRACT, not of the engine. Semantic:
#   patch — wording/doc only; minor — a field ADDED (old readers still work);
#   major — a field removed or its meaning changed (old readers break).
# A stored fixture must keep validating across a minor bump; that is the whole
# point of publishing a number here.
SCHEMA_VERSION = "1.0.0"
SCHEMA_ID = (
    "https://masiarek.github.io/star-voting-library/"
    "STARVote_LH_tabulation_engine/star_result.schema.json"
)

MAX_SCORE = 5  # the fork's teaching guardrail — see CLAUDE.md, not an engine limit


class UnsupportedMethod(Exception):
    """The file names a voting method this engine does not count.

    Distinct from a malformed file on purpose: a conformance runner must be
    able to tell "out of scope for this implementation" from "this
    implementation got it wrong".
    """


# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------

def _expected_winners(path):
    """The file's own answer key, or None when it does not carry one.

    Read here rather than in `load_election()` because it is not an input to
    the count — it is the thing the count is checked against.
    """
    try:
        import yaml
    except ImportError:
        return None
    try:
        data = yaml.safe_load(Path(path).read_text(encoding="utf-8"))
    except Exception:
        return None
    if not isinstance(data, dict):
        return None
    race = w._find_race(data) or data
    ew = race.get("expected_winners")
    if ew is None:
        er = race.get("expected_results")
        if isinstance(er, dict):
            ew = er.get("winners")
    if ew is None:
        return None
    if isinstance(ew, str):
        ew = [ew]
    # YAML 1.1 retyping: an unquoted ballot-measure `No` arrives as False. Keep
    # what the file actually parsed to and let the type check upstream complain
    # — silently coercing here would hide the very bug check_yaml_name_types
    # exists to catch.
    return [x if isinstance(x, str) else x for x in ew]


def _num(x):
    """Whole floats print as integers. pyrankvote counts in floats because STV
    surpluses are fractional; an IRV round of `40.0` is noise in a fixture that
    a second implementation would then have to match."""
    if isinstance(x, float) and x.is_integer():
        return int(x)
    return x


def _sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def _pairwise(candidates, ballots):
    """The full head-to-head matrix as For / Equal Support / Against."""
    m = w.calculate_preference_matrix(candidates, ballots)
    prefer = {}
    for a in candidates:
        row = {}
        for b in candidates:
            if a == b:
                continue
            fa, ag, eq = m[a][b]
            row[b] = {"for": fa, "equal_support": eq, "against": ag}
        prefer[a] = row
    return {"candidates": list(candidates), "prefer": prefer}


def _score_rows(counts, candidates):
    """[{candidate, value}] in descending value, then ballot-column order."""
    idx = {c: i for i, c in enumerate(candidates)}
    return [
        {"candidate": c, "value": counts.get(c, 0)}
        for c in sorted(candidates, key=lambda c: (-counts.get(c, 0), idx[c]))
    ]


# ---------------------------------------------------------------------------
# per-family builders — each returns (winners, rounds, pairwise, tiebreaks)
# ---------------------------------------------------------------------------

def _build_score(el, cls):
    """STAR and the other score methods (Bloc STAR, sss, rrv, allocated)."""
    candidates, ballots, _display = w.parse_ballots_from_string(el["ballots"])
    seats = el["seats"] or 1
    lot = el.get("lot_numbers") or []
    method = el["method"] or starvote.star

    # Winners: the engine's own count, run silently — identical call to the one
    # the CLI makes (verbosity=1 matters; see scenario_eval.py's note on sss).
    tiebreaker = w.LotNumberTiebreaker(lot_numbers=lot, silent=True)
    result = starvote.election(
        method, ballots, seats=seats, maximum_score=MAX_SCORE,
        tiebreaker=tiebreaker, verbosity=1, print=lambda *a, **k: None,
    )
    winners = [str(x) for x in (result if isinstance(result, (list, tuple))
                                else [result])]

    rounds = {"scoring": _score_rows(starvote._scoring_round(ballots), candidates)}
    tiebreaks = []

    # The Automatic Runoff is a single-winner STAR concept. A Bloc/PR count
    # elects by a different rule, so reporting "the runoff" there would be a
    # number the method never used.
    if method is starvote.star and seats == 1:
        priority = lot or candidates
        order_map = {c: i for i, c in enumerate(priority)}
        finalists, ft = w.resolve_finalists(ballots, order_map,
                                            maximum_score=MAX_SCORE)
        rounds["finalists"] = list(finalists)
        if ft:
            tiebreaks.append({
                "stage": "finalists",
                "tied": list(ft["tied"]),
                "at": ft["score"],
                "rung": ft["rung"],
                "advanced": list(ft["advanced"]),
                "eliminated": list(ft["eliminated"]),
            })
        if len(finalists) == 2:
            prefs, equal = starvote._preference_round(ballots, finalists)
            a, b = finalists
            decided = prefs.get(a, 0) + prefs.get(b, 0)
            rounds["runoff"] = {
                "finalists": [
                    {"candidate": a, "preferred_by": prefs.get(a, 0)},
                    {"candidate": b, "preferred_by": prefs.get(b, 0)},
                ],
                "equal_support": equal,
                "decided_voters": decided,
                "ballots_cast": len(ballots),
                # A strict majority OF THE DECIDED VOTERS — the denominator the
                # report prints. Not a majority of ballots cast.
                "majority": decided // 2 + 1 if decided else 0,
                "tied": prefs.get(a, 0) == prefs.get(b, 0),
            }

    return winners, rounds, _pairwise(candidates, ballots), tiebreaks, len(ballots), candidates


def _build_approval(el, cls):
    candidates, ballots, _ = w.parse_ballots_from_string(el["ballots"])
    t = w.approval_tally(candidates, ballots, seats=el["seats"] or 1,
                         priority=el.get("lot_numbers"))
    rounds = {
        "approval": _score_rows(t["counts"], candidates),
        "abstentions": t["abstentions"],
    }
    tiebreaks = []
    seats, ranked, counts = t["seats"], t["ranked"], t["counts"]
    if seats < len(candidates) and counts[ranked[seats - 1]] == counts[ranked[seats]]:
        cutoff = counts[ranked[seats - 1]]
        tied = [c for c in t["order"] if counts[c] == cutoff]
        tiebreaks.append({
            "stage": "seat_cutoff",
            "tied": tied,
            "at": cutoff,
            "rung": "candidate priority order",
            "advanced": [c for c in tied if c in t["winners"]],
            "eliminated": [c for c in tied if c not in t["winners"]],
        })
    return (list(t["winners"]), rounds, _pairwise(candidates, ballots),
            tiebreaks, t["total"], candidates)


def _build_plurality(el, cls):
    """Choose-One at both seat counts — and they are NOT the same rule.

    Single-winner spoils an overvote (a ballot marking two candidates counts
    for nobody); multi-winner counts every mark, because the ballot itself is
    a block/limited ballot. Deriving one from the other elected the wrong slate
    on five block-voting cases before this used the engine's own tallies.
    """
    seats = el["seats"] or 1
    lot = el.get("lot_numbers")
    if seats > 1:
        t = w.plurality_multi_tally(el["ballots"], lot_numbers=lot,
                                    num_winners=seats)
        rounds = {
            "votes": _score_rows(t["votes"], t["candidates"]),
            "variant": t["variant"],
            "votes_per_voter": t["votes_per_voter"],
            "abstentions": t["abstain"],
        }
        ties = []
        if t["cutoff_lot_tie"]:
            n = t["num_winners"]
            ties.append({
                "stage": "seat_cutoff",
                "tied": [t["order"][n - 1], t["order"][n]],
                "at": t["votes"][t["order"][n - 1]],
                "rung": "lot",
                "advanced": [t["order"][n - 1]],
                "eliminated": [t["order"][n]],
            })
        return (list(t["winners"]), rounds,
                _pairwise(t["candidates"], t["ballots"]), ties,
                t["n"], t["candidates"])

    t = w.plurality_single_tally(el["ballots"], lot_numbers=lot)
    rounds = {
        "votes": _score_rows(t["votes"], t["candidates"]),
        "variant": "Choose-One / Plurality",
        "votes_per_voter": 1,
        "overvotes": len(t["overvotes"]),   # spoiled: marked more than one
        "blanks": len(t["blanks"]),
    }
    ties = []
    if len(t["tied_at_top"]) > 1:
        ties.append({
            "stage": "winner",
            "tied": list(t["tied_at_top"]),
            "at": t["votes"][t["tied_at_top"][0]],
            "rung": "lot",
            "advanced": [t["winner"]],
            "eliminated": [c for c in t["tied_at_top"] if c != t["winner"]],
        })
    return ([t["winner"]] if t["winner"] else [], rounds,
            _pairwise(t["candidates"], t["ballots"]), ties,
            t["n"], t["candidates"])


def _build_ranked_robin(el, cls):
    t = w.ranked_robin_tally(el["ballots"], lot_numbers=el.get("lot_numbers"),
                             num_winners=el["seats"] or 1)
    cands = t["candidates"]
    record = [
        {
            "candidate": c,
            "wins": len(t["wins"][c]),
            "losses": len(t["losses"][c]),
            "draws": len(t["ties"][c]),
            "copeland": t["copeland"][c],
            "margin": t["margin"][c],
            "beats": list(t["wins"][c]),
        }
        for c in t["order"]
    ]
    smith = w.smith_set(cands, t["matrix"])
    rounds = {"record": record, "smith_set": sorted(smith, key=cands.index)}
    tiebreaks = []
    if len(t["leaders"]) > 1:
        tiebreaks.append({
            "stage": "copeland_leaders",
            "tied": list(t["leaders"]),
            "at": t["copeland"][t["leaders"][0]],
            # LH's ladder: total margin, then the published lot. (BetterVoting's
            # rung 2 is head-to-head instead — a documented divergence.)
            "rung": "total margin, then lot",
            "advanced": [c for c in t["leaders"] if c in t["winners"]],
            "eliminated": [c for c in t["leaders"] if c not in t["winners"]],
        })
    if t["cutoff_lot_tie"]:
        tiebreaks.append({
            "stage": "seat_cutoff",
            "tied": [t["order"][t["num_winners"] - 1], t["order"][t["num_winners"]]],
            "at": t["copeland"][t["order"][t["num_winners"] - 1]],
            "rung": "lot",
            "advanced": [t["order"][t["num_winners"] - 1]],
            "eliminated": [t["order"][t["num_winners"]]],
        })
    return (list(t["winners"]), rounds,
            _pairwise(cands, t["ballots"]), tiebreaks, t["n"], cands)


def _build_ranked(el, cls, path):
    """RCV-IRV and STV — counted by the vendored pyrankvote, read back never
    recomputed (the same rule the transfer block follows)."""
    irv_dir = (ENGINE_DIR.parent / "06_Other" / "RCV_IRV"
               / "RCV_IRV_tabulation_engine")
    if str(irv_dir) not in sys.path:
        sys.path.insert(0, str(irv_dir))
    import rcv_irv_tabulation as irv

    t = irv.tabulate(str(path))
    result = t["result"]
    cands = t["candidates"]

    rounds_out = []
    for i, rnd in enumerate(getattr(result, "rounds", []) or [], start=1):
        tallies, eliminated, elected = [], [], []
        for cr in rnd.candidate_results:
            name = cr.candidate.name
            status = str(getattr(cr, "status", "")).split(".")[-1]
            tallies.append({"candidate": name,
                            "votes": _num(cr.number_of_votes),
                            "status": status})
            if status.lower().startswith("reject"):
                eliminated.append(name)
            elif status.lower().startswith("elect"):
                elected.append(name)
        counted = sum(x["votes"] for x in tallies)
        rounds_out.append({
            "round": i,
            "tallies": tallies,
            # Ballots that have stopped counting: cast minus still-active. The
            # number pyrankvote's own table never prints, and the one an IRV
            # "majority" has to be reconciled against.
            "exhausted": _num(t["total"] - counted),
            "eliminated_this_round": eliminated,
            "elected_this_round": elected,
        })

    # Eliminations are read back from the engine's rounds, never recomputed:
    # a recomputed order can contradict the table above it on a tie settled by
    # pyrankvote's second-choices ladder.
    prev = set()
    elimination_order = []
    for r in rounds_out:
        for name in r["eliminated_this_round"]:
            if name not in prev:
                prev.add(name)
                elimination_order.append({"round": r["round"], "candidate": name})

    winners = [c.name for c in result.get_winners()]
    rounds = {
        "irv_rounds": rounds_out,
        "elimination_order": elimination_order,
        "ballot_source": ("ranked ballots" if t["ranked_mode"]
                          else "converted from score ballots; 0 = unranked"),
    }
    if t["seats"] > 1:
        rounds["quota"] = {
            "rule": "exact Droop, votes/(seats+1)",
            "value": t["total"] / (t["seats"] + 1),
            "hand_count_droop": t["total"] // (t["seats"] + 1) + 1,
        }

    # The pairwise matrix is not part of the IRV count, but it is what a
    # conformance run needs to check Condorcet/Smith claims about the result.
    pw = None
    try:
        pc, pb, _, _ = w.ballots_for_pairwise(el["ballots"])
        pw = _pairwise(pc, pb)
    except Exception:
        pass
    return winners, rounds, pw, [], t["total"], cands


# ---------------------------------------------------------------------------
# the public entry point
# ---------------------------------------------------------------------------

def build(path):
    """Tabulate `path` and return the result as a plain dict (JSON-ready)."""
    path = Path(path)
    el = w.load_election(str(path))
    cls = w.classify_method(el.get("method_name"), el["ballots"])

    # Refuse an unrecognized method with the CLI's own message rather than a
    # traceback from deep inside the count. `Range` at 0–9 lands here: the
    # method is real and tabulable by other tools, just not by this engine's
    # 0–5 teaching path — an honest "not supported", not a wrong answer.
    if cls["declared"] and not cls["known"]:
        raise UnsupportedMethod(
            f"unknown voting_method {cls['declared']!r} — this engine counts "
            "STAR | Approval | RankedRobin | RCV_IRV | STV | Plurality | "
            "Bloc STAR | sss | rrv | allocated"
        )

    if cls["family"] == "ranked_robin":
        winners, rounds, pw, ties, n, cands = _build_ranked_robin(el, cls)
    elif cls["family"] == "plurality":
        winners, rounds, pw, ties, n, cands = _build_plurality(el, cls)
    elif cls["family"] == "approval":
        winners, rounds, pw, ties, n, cands = _build_approval(el, cls)
    elif cls["family"] in ("irv", "stv"):
        winners, rounds, pw, ties, n, cands = _build_ranked(el, cls, path)
    else:
        winners, rounds, pw, ties, n, cands = _build_score(el, cls)

    expected = _expected_winners(path)
    doc = {
        "$schema": SCHEMA_ID,
        "schema_version": SCHEMA_VERSION,
        "source": {
            "file": path.name,
            "sha256": _sha256(path),
        },
        "election": {
            "title": el.get("title"),
            "declared_method": cls["declared"],
            "method": cls["normalized"] or "star",
            "family": cls["family"],
            "seats": el["seats"] or 1,
            "candidates": list(cands),
            "ballots_cast": n,
            "max_score": MAX_SCORE if cls["family"] in ("score",) else None,
            "lot_order": list(el.get("lot_numbers") or []) or None,
        },
        "result": {
            "winners": winners,
            "expected_winners": expected,
            # null (not false) when the file carries no answer key — "we did not
            # check" and "we checked and it failed" must not look alike.
            "matches_expected": (None if expected is None
                                 else sorted(map(str, expected)) == sorted(winners)),
        },
        "rounds": rounds,
        "tiebreaks": ties,
        "engine": {
            "name": "starvote_larry_hastings",
            "starvote_version": getattr(starvote, "__version__", None),
        },
    }
    if pw is not None:
        doc["pairwise"] = pw
    return doc


def dumps(path, indent=2):
    return json.dumps(build(path), indent=indent, ensure_ascii=False)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    print(dumps(sys.argv[1]))
