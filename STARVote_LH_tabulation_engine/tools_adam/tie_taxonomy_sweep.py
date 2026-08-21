#!/usr/bin/env python3
"""
tie_taxonomy_sweep.py — drive the Equal Vote methods into their tie corners
==========================================================================
Generate small elections on a **coarse score scale** (0,1,2 by default instead
of 0-5), count every one of them with the LH engine, classify every tie the
count hits, and check each classification against the library's published tie
taxonomy.

**Why a coarse scale.** Ties are the corner this library teaches from, and on a
0-5 ballot they are rare enough that you have to build them by hand — which is
what the `Flat_scores_ties` and `tie_break_dead_rung` sets are. Shrink the scale
to {0,1,2} and ties stop being exotic: three scores across three voters collide
constantly, so a plain exhaustive sweep walks every branch of the ladder without
anybody designing a profile. Same election rules, same engine, denser corners.

**What it is for.** Not to find *a* tie — we have plenty — but to answer a
completeness question: *is every tie the engine can produce already a category
this library has a lesson for?* Every observation is reduced to a signature and
looked up in `TAXONOMY` below. A signature with no entry prints under
**UNMAPPED**, and that is the finding: either a lesson to write, or a category
to add to the map in `07_Concepts/topics/ties/why_contrived_tie_cases.md`.

**Methods.** The Equal Vote Coalition set, which is what this repo teaches:
STAR, Bloc STAR, the proportional STAR family (Allocated Score, SSS, RRV),
Ranked Robin and Approval. Choose-One is available as a control with
`--include-plurality`. RCV-IRV and STV are deliberately out of scope.

**Where the answers come from — two surfaces, on purpose.**

1. `result_json.build()` — the machine-readable result contract, i.e. what a
   second implementation would diff against. Its `tiebreaks: []` is a positive
   claim that no rung fired.
2. `starvote`'s own round narration at `verbosity=2`, captured in-process.
   This is the engine printing what it did, and it is the only surface that
   names the **deterministic** rungs on a multi-winner count — `result_json`
   says so itself (`_lot_ties`: "What this still cannot see ... the rungs BELOW
   the lot on a multi-winner count").

Comparing the two is itself a check: a tie the narration shows and the contract
omits is reported as a `json-blind` observation, not silently dropped. Nothing
here re-counts an election; every number quoted comes from one of those two
engine surfaces.

Examples
--------
    # the default sweep: 3-4 candidates, 3-4 voters, scales {0,1,2} and {0,1,5}
    python tie_taxonomy_sweep.py

    # Adam's degenerate probe on its own: five candidates, three all-zero ballots
    python tie_taxonomy_sweep.py --all-zeros

    # binary ballots, wider field, write one witness case file per category
    python tie_taxonomy_sweep.py --scores 0,1 -c 4 5 -v 3 4 --witness-dir /tmp/w

    # everything, including the Choose-One control, as JSON for further work
    python tie_taxonomy_sweep.py --include-plurality --json out.json
"""

import argparse
import io
import itertools
import json
import random
import re
import sys
import tempfile
from collections import Counter, OrderedDict
from pathlib import Path

ENGINE_DIR = Path(__file__).resolve().parent.parent
REPO_ROOT = ENGINE_DIR.parent
if str(ENGINE_DIR) not in sys.path:
    sys.path.insert(0, str(ENGINE_DIR))

import starvote                       # noqa: E402
import starvote_larry_hastings as w   # noqa: E402
import result_json                    # noqa: E402


# --------------------------------------------------------------------------- #
# The cast. House rule (CLAUDE.md): common, easy to say, distinct initials in
# ballot order, so a name lines up with its column.
# --------------------------------------------------------------------------- #
CAST = ["Ada", "Ben", "Cara", "Dee", "Eli", "Fay", "Gus", "Hana"]

# The ballot is always the repo's 0-5 STAR ballot; `--scores` narrows which of
# those values voters are allowed to USE. That distinction matters for the
# five-star rung, which counts ballots at the scale maximum: on a {0,1,2} sweep
# it is a dead rung by construction, which is why the default also sweeps
# {0,1,5} — same coarseness, live rung.
MAX_SCORE = 5


# --------------------------------------------------------------------------- #
# The methods this sweep counts, with the seat counts each one accepts.
# `yaml` is the string a case file would carry; `fn` is what starvote runs.
# --------------------------------------------------------------------------- #
METHODS = OrderedDict([
    ("STAR",        dict(yaml="STAR",       fn=starvote.star,      seats="one",   family="score")),
    ("Bloc STAR",   dict(yaml="Bloc STAR",  fn=starvote.bloc,      seats="many",  family="score")),
    ("allocated",   dict(yaml="allocated",  fn=starvote.allocated, seats="many",  family="score")),
    ("sss",         dict(yaml="sss",        fn=starvote.sss,       seats="many",  family="score")),
    ("rrv",         dict(yaml="rrv",        fn=starvote.rrv,       seats="many",  family="score")),
    ("RankedRobin", dict(yaml="RankedRobin", fn=None,              seats="any",   family="ranked_robin")),
    ("Approval",    dict(yaml="Approval",   fn=None,               seats="any",   family="approval")),
    ("Plurality",   dict(yaml="Plurality",  fn=None,               seats="any",   family="plurality")),
])

EVC_METHODS = ["STAR", "Bloc STAR", "allocated", "sss", "rrv", "RankedRobin", "Approval"]


# --------------------------------------------------------------------------- #
# THE TAXONOMY.
#
# One entry per tie category this library already teaches. `signature` is what
# the observer below produces; anything it produces that is not a key here is
# printed as UNMAPPED, which is the whole point of the sweep.
#
# `lesson` is repo-relative. `note` is the one-line reason the category is its
# own thing rather than a variant of its neighbour.
# --------------------------------------------------------------------------- #
class Cat:
    def __init__(self, cid, title, lesson, note):
        self.id, self.title, self.lesson, self.note = cid, title, lesson, note


TAXONOMY = OrderedDict([
    # ---- single-winner STAR: the scoring round ----------------------------
    ("STAR/scoring/head-to-head", Cat(
        "S-F1", "Scoring tie → head-to-head (matchups won) picks the finalists",
        "01_STAR/03_Criteria/tie_break_ladder/README.md",
        "rung 1 of the finalists ladder; at 3+ tied it counts matchups WON, not preference votes")),
    ("STAR/scoring/five-star", Cat(
        "S-F2", "Scoring tie → five-star rung picks the finalists",
        "01_STAR/03_Criteria/tie_break_ladder/bv2180_fp62p2_ice_cream_ladder.md",
        "rung 2; counts ballots at the scale maximum only")),
    ("STAR/scoring/lot", Cat(
        "S-F3", "Scoring tie → dead rung → lot picks the finalists",
        "01_STAR/03_Criteria/tie_break_dead_rung/README.md",
        "the floor: published lot order, disclosed")),
    # ---- single-winner STAR: the automatic runoff -------------------------
    ("STAR/runoff/score", Cat(
        "S-R1", "Runoff tie → higher total score wins",
        "01_STAR/03_Criteria/tie_break_ladder/bv830_vb3xv2_no_condorcet_tie_score.md",
        "each round breaks its tie with the OTHER round's yardstick")),
    ("STAR/runoff/five-star", Cat(
        "S-R2", "Runoff tie → five-star rung wins",
        "01_STAR/03_Criteria/tie_break_ladder/README.md",
        "rung 2 of the runoff ladder")),
    ("STAR/runoff/lot", Cat(
        "S-R3", "Runoff tie → dead rung → lot wins",
        "01_STAR/03_Criteria/tie_break_dead_rung/lot_random_vs_published_jfk7pd/lot_random_vs_published_jfk7pd.md",
        "the floor of the second ladder")),
    # ---- Bloc STAR: the same two ladders, once per seat -------------------
    ("Bloc/scoring/head-to-head", Cat(
        "B-F1", "Bloc seat: scoring tie → head-to-head", "02_STAR_Bloc/01_Learn/bloc_tiebreaks.md",
        "N full STAR rounds with the winner removed, so every rung recurs per seat")),
    ("Bloc/scoring/five-star", Cat(
        "B-F2", "Bloc seat: scoring tie → five-star", "02_STAR_Bloc/01_Learn/bloc_tiebreaks.md", "")),
    ("Bloc/scoring/lot", Cat(
        "B-F3", "Bloc seat: scoring tie → lot", "02_STAR_Bloc/02_Examples/b484mbm_tie_every_rung.md",
        "the LH report prints each seat's tiebreaks; BetterVoting keeps only the last seat's")),
    ("Bloc/runoff/score", Cat(
        "B-R1", "Bloc seat: runoff tie → higher total score", "02_STAR_Bloc/01_Learn/bloc_tiebreaks.md", "")),
    ("Bloc/runoff/five-star", Cat(
        "B-R2", "Bloc seat: runoff tie → five-star", "02_STAR_Bloc/01_Learn/bloc_tiebreaks.md", "")),
    ("Bloc/runoff/lot", Cat(
        "B-R3", "Bloc seat: runoff tie → lot", "02_STAR_Bloc/02_Examples/bv750_tie_breaking_bloc.md",
        "a runoff tie seats ONE candidate, never both")),
    # ---- the proportional STAR family: one rung per seat, then the floor --
    ("PR/selection/lot", Cat(
        "P-1", "STAR-PR / SSS / RRV: a tie on the round's weighted score total → lot",
        "07_Concepts/tabulation_engines/tiebreak_ladders.md",
        "shortest ladder in the library — no head-to-head rung, no five-star rung")),
    # ---- Ranked Robin -----------------------------------------------------
    ("RR/copeland/1st Degree", Cat(
        "R-1", "Copeland tie → 1st Degree (margins among the tied finalists)",
        "05_Ranked_Robin/03_Criteria/rr_tiebreaks/degrees_of_ties.md",
        "for exactly two finalists the 1st Degree IS their head-to-head")),
    ("RR/copeland/2nd Degree", Cat(
        "R-2", "Copeland tie → 2nd Degree (margins over the whole field)",
        "05_Ranked_Robin/03_Criteria/rr_tiebreaks/degrees_of_ties.md",
        "same arithmetic as the 1st Degree, different pool — and that alone changes winners")),
    ("RR/copeland/lot", Cat(
        "R-3", "Copeland tie → lot (dead heat, cycle, or a mixed group)",
        "05_Ranked_Robin/03_Criteria/rr_tiebreaks/dead_heat_lot_tiebreak.md",
        "the shape (dead heat / cycle / mixed) is reported separately by the engine")),
    ("RR/cutoff/lot", Cat(
        "R-4", "Bloc Ranked Robin: the last seat ties → lot",
        "05_Ranked_Robin/03_Criteria/rr_tiebreaks/README.md",
        "the ladder used as a ranking, sliced at N")),
    # ---- Approval ---------------------------------------------------------
    ("Approval/winner/candidate priority order", Cat(
        "A-1", "Approval: a tie for the win → candidate priority order",
        "04_Approval/01_Learn/approval_indeterminacy.md",
        "approvals, then the floor — Approval has no intermediate rung at all")),
    ("Approval/cutoff/candidate priority order", Cat(
        "A-2", "Multi-winner Approval: a tie on the seat cut line → candidate priority order",
        "04_Approval/01_Learn/Multiwinner_Approval/README.md",
        "same one rung, but now it decides who is IN the committee")),
    # ---- Choose-One (control) --------------------------------------------
    ("Plurality/winner/lot", Cat(
        "C-1", "Choose-One: a tie for first → lot",
        "06_Other/Plurality/cases/cases_pages/lunch_choose_one_dead_tie.md",
        "counting the marks is all a choose-one ballot can do")),
    ("Plurality/cutoff/lot", Cat(
        "C-2", "SNTV / Block: the last seat ties → lot",
        "07_Concepts/tabulation_engines/tiebreak_ladders.md", "")),
    # ---- cross-cutting shapes, not rungs ----------------------------------
    ("*/above-cut/silent", Cat(
        "X-1", "Multi-winner: candidates tie ABOVE the cut line — ordered silently",
        "07_Concepts/topics/ties/silent_tiebreak.md",
        "consequence-free for the SET of winners, but it still orders them by the floor and says nothing")),
    ("*/scoring/partial-separation", Cat(
        "X-4", "A rung eliminates PART of the tied group and the survivors go on down the ladder",
        "01_STAR/01_Learn/Tie_Breaking_STAR/matchups_won_vs_preference_votes.md",
        "only reachable with 3+ tied, which is exactly what a symmetric probe cannot build — "
        "and it is the branch where matchups-won and preference-votes part company")),
    ("*/winner/zero-support", Cat(
        "X-2", "A winner elected with zero support — nobody scored, approved or marked anybody",
        "07_Concepts/topics/ties/ties_are_forced.md",
        "the degenerate limit: the tie is the whole electorate, and the lot elects from a field nobody voted for")),
    ("*/contract/json-blind", Cat(
        "X-3", "A tie the engine's report narrates but the JSON contract does not list",
        "07_Concepts/tabulation_engines/result_schema.md",
        "`tiebreaks: []` is a positive claim; this is where it is not earned")),
])


# --------------------------------------------------------------------------- #
# Ballot generation
# --------------------------------------------------------------------------- #
def ballot_universe(n_cands, scores, style):
    """Every distinct ballot a voter could cast, for this ballot style."""
    if style == "plurality":
        # A choose-one ballot: one mark, or none. Generating score rows here
        # would spoil almost every ballot as an overvote and the sweep would
        # measure the validator instead of the ladder.
        rows = [tuple(0 for _ in range(n_cands))]
        for i in range(n_cands):
            rows.append(tuple(1 if j == i else 0 for j in range(n_cands)))
        return rows
    if style == "approval":
        return list(itertools.product((0, 1), repeat=n_cands))
    return list(itertools.product(scores, repeat=n_cands))


# --------------------------------------------------------------------------- #
# Profile SHAPES.
#
# `--scores` narrows which values a voter may use; a shape constrains how the
# ballots relate to EACH OTHER. The two are orthogonal, and the second is where
# the interesting ties live: a random draw from {0,1,2} ties by collision, while
# a rotation or a mirrored electorate ties by CONSTRUCTION and keeps tying as
# the field grows. Every shape here is a published or folklore probe:
#
#   random    the plain draw — the baseline
#   bullet    every voter maxes exactly one candidate and zeroes the rest.
#             The strategic-voting limit, and the profile a real STAR election
#             degenerates toward under bullet-voting pressure.
#   flat      every voter scores the whole field the same (possibly a different
#             level per voter) — the `Flat_scores_ties` set, generalized.
#   rotation  Moulin's impossibility witness: k voters per cyclic rotation of one
#             base ballot, so the electorate is symmetric under relabelling and
#             SOMETHING has to break neutrality. Needs voters % candidates == 0.
#   mirror    every ballot paired with its reflection through the middle of the
#             range, so each pair contributes the same total to every candidate
#             — an electorate that cannot separate anybody on score, whatever it
#             says otherwise. The most efficient tie generator here by far, and
#             the only one that reaches the five-star rung on a small
#             electorate; read its caveat below before quoting that.
#   clone     one candidate's column copied onto another: perfect clones, which
#             are exactly equal on every rung a ballot can express.
# --------------------------------------------------------------------------- #
SHAPES = ("random", "bullet", "flat", "rotation", "mirror", "clone")


def _shape_universe(n_cands, scores, style, shape):
    """The ballots a shape draws from, or None when the shape builds whole
    profiles rather than picking rows independently."""
    vals = (0, 1) if style in ("approval", "plurality") else tuple(scores)
    top = max(vals)
    if shape == "bullet":
        rows = [tuple(0 for _ in range(n_cands))]
        rows += [tuple(top if j == i else 0 for j in range(n_cands))
                 for i in range(n_cands)]
        return rows
    if shape == "flat":
        return [tuple(v for _ in range(n_cands)) for v in vals]
    return None


def iter_profiles(n_cands, n_voters, scores, style, limit, rng, shape="random"):
    """Profiles as multisets of ballots — the anonymity quotient of the space.

    Two ballot orderings of the same votes are the same election to every
    method here, so enumerating orderings would multiply the work without
    adding a single new count.
    """
    base = ballot_universe(n_cands, scores, style)
    vals = sorted({v for row in base for v in row})
    top = max(vals)

    if shape == "rotation":
        # Every distinct base ballot, rotated through all n_cands positions,
        # each rotation cast by the same number of voters. Yields nothing when
        # the electorate does not divide evenly — say so by yielding nothing
        # rather than by silently rounding.
        if n_voters % n_cands:
            return
        k = n_voters // n_cands
        seen = set()
        for row in base:
            rots = tuple(sorted(row[i:] + row[:i] for i in range(n_cands)))
            if rots in seen:
                continue
            seen.add(rots)
            yield [r for r in rots for _ in range(k)]
        return

    if shape == "mirror":
        # Half the electorate drawn freely, the other half its reflection
        # through the middle of the range in use, so each PAIR contributes the
        # same total to every candidate. An odd voter gets a flat ballot, which
        # is its own mirror.
        #
        # CAVEAT, because it changes what a result means: a reflection is only
        # closed inside `--scores` when that set is symmetric about its own
        # midpoint. `{0,1,5}` is not — reflecting a 1 gives a 4 — so this shape
        # can put values on the ballot that the sweep was not asked for, and a
        # rung it reaches may have been reached by the extra values rather than
        # by the symmetry. Use a symmetric set (`{0,5}`, `{0,1,2,3,4,5}`,
        # `{0,2,3,5}`) when that distinction matters.
        lo, hi = min(vals), max(vals)
        half = n_voters // 2
        odd = n_voters % 2
        for _ in range(limit):
            picks = [rng.choice(base) for _ in range(half)]
            prof = picks + [tuple(lo + hi - v for v in b) for b in picks]
            if odd:
                prof.append((rng.choice(vals),) * n_cands)
            yield prof
        return

    if shape == "clone":
        # Candidate B's column replaced by candidate A's: perfect clones, equal
        # on every rung a ballot can express. Needs somebody to be a clone OF.
        if n_cands < 2:
            return
        for _ in range(limit):
            prof = [list(rng.choice(base)) for _ in range(n_voters)]
            for b in prof:
                b[1] = b[0]
            yield [tuple(b) for b in prof]
        return

    universe = _shape_universe(n_cands, scores, style, shape) or base
    total = 1
    for i in range(n_voters):
        total = total * (len(universe) + i) // (i + 1)
    if total <= limit:
        for combo in itertools.combinations_with_replacement(universe, n_voters):
            yield list(combo)
    else:
        for _ in range(limit):
            yield [rng.choice(universe) for _ in range(n_voters)]


def profile_yaml(profile, n_cands, method_yaml, seats, title):
    cands = CAST[:n_cands]
    rows = "\n".join("  " + ",".join(str(s) for s in b) for b in profile)
    return (
        f"election_title: {title}\n"
        f"voting_method: {method_yaml}\n"
        f"num_winners: {seats}\n"
        f"lot_numbers: [{', '.join(cands)}]\n"
        f"ballots: |-\n  {','.join(cands)}\n{rows}\n"
    )


# --------------------------------------------------------------------------- #
# Surface 2: starvote's own round narration
# --------------------------------------------------------------------------- #
_HEAD = re.compile(r"^\[(?P<path>[^\]]+)\]\s*$")
_TIE = re.compile(r"There's (?:a|still a) (?P<n>[\w-]+)-way tie for (?P<place>\w+)")
_ADVANCES = re.compile(r"(?P<who>[\w ,]+) advances, but there's still a")

_WORD_N = {"two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7,
           "eight": 8, "nine": 9, "ten": 10}

# The rung a "First/Second tiebreaker" heading means depends on which round it
# sits under — that is the whole "each round breaks its tie with the other
# round's yardstick" idea, and it is why this cannot be one flat table.
RUNGS = {
    ("scoring", 1): "head-to-head",
    ("scoring", 2): "five-star",
    ("runoff", 1): "score",
    ("runoff", 2): "five-star",
}


def narrate(method_fn, ballots, seats, lot, max_score):
    """Run the count with the engine printing, and hand back (lines, events).

    `events` is the lot tiebreaker's own log — read off the object that broke
    the tie, never recomputed (the rule `result_json._lot_ties` follows).
    """
    lines = []
    tb = w.LotNumberTiebreaker(lot_numbers=lot, silent=True)
    starvote.election(method_fn, ballots, seats=seats, maximum_score=max_score,
                      tiebreaker=tb, verbosity=2,
                      print=lambda *a, **k: lines.extend(
                          " ".join(str(x) for x in a).splitlines() or [""]))
    return lines, tb.events


def parse_narration(lines):
    """Turn the printed rounds into tie events.

    Returns a list of dicts: {locus, round, rungs_run, partial, unresolved}.
    A locus is 'scoring' (which candidates advance), 'runoff' (which finalist
    wins the seat) or 'selection' (a proportional round's one weighted rung).
    """
    events, cur = [], None
    for raw in lines:
        line = raw.rstrip()
        m = _HEAD.match(line.strip())
        if m:
            path = m.group("path")
            parts = [p.strip() for p in path.split(":")]
            rnd = next((int(p.split()[1]) for p in parts
                        if p.startswith("Round ") and p.split()[1].isdigit()), None)
            # A "Ballot allocation round" is bookkeeping between seats, not a
            # selection round; its nested "Round N" headings would otherwise
            # be read as extra seats.
            if any(p.startswith(("Ballot allocation", "Reweighing")) for p in parts):
                cur = None
                continue
            if any(p == "Scoring Round" for p in parts):
                locus = "scoring"
            elif any(p == "Automatic Runoff Round" for p in parts):
                locus = "runoff"
            elif parts[-1].startswith("Round ") or parts[-1] == "Score round":
                locus = "selection"
            else:
                cur = None
                continue
            rung = 0
            if parts[-1] == "First tiebreaker":
                rung = 1
            elif parts[-1] == "Second tiebreaker":
                rung = 2
            if rung and cur and cur["locus"] == locus and cur["round"] == rnd:
                cur["rungs_run"] = max(cur["rungs_run"], rung)
                cur["still_tied"] = False   # re-decided by the lines below
            else:
                cur = {"locus": locus, "round": rnd, "rungs_run": rung,
                       "partial": False, "still_tied": False, "size": 0}
                events.append(cur)
            continue
        if cur is None:
            continue
        if _ADVANCES.search(line):
            cur["partial"] = True
        t = _TIE.search(line)
        if t:
            cur["still_tied"] = True
            n = t.group("n")
            cur["size"] = max(cur["size"], _WORD_N.get(n, 2))
    # Keep only rounds that actually tied at some point.
    return [e for e in events if e["size"] or e["rungs_run"]]


# --------------------------------------------------------------------------- #
# The observer — one election in, a list of signatures out
# --------------------------------------------------------------------------- #
class Obs:
    def __init__(self, sig, detail, extra=None):
        self.sig, self.detail, self.extra = sig, detail, extra or {}


def _tally_rows(doc):
    """The one reported tally a cut-line question can be asked of."""
    r = doc["rounds"]
    for key in ("approval", "votes"):
        if key in r:
            return [(x["candidate"], x["value"]) for x in r[key]]
    if "record" in r:
        return [(x["candidate"], x["copeland"]) for x in r["record"]]
    return None


def observe(doc, narration, label):
    """Every tie this count hit, as taxonomy signatures.

    Reads only what the two engine surfaces reported. `label` prefixes the
    score-family signatures so a STAR ladder and a Bloc seat's ladder stay
    distinguishable — they are the same rungs but different lessons.
    """
    out = []
    seats = doc["election"]["seats"]
    reported = doc.get("tiebreaks", [])

    # --- score family: the narration is the authority on which rung fired ---
    for e in narration:
        locus, rung_n = e["locus"], e["rungs_run"]
        if locus == "selection":
            if e["still_tied"] or e["size"] > 1:
                out.append(Obs(f"{label}/selection/lot",
                               f"round {e['round']}: {e['size'] or 2} tied on the "
                               f"weighted total, straight to the lot",
                               {"round": e["round"]}))
            continue
        if e["still_tied"] and rung_n >= 2:
            rung = "lot"
        elif rung_n == 0:
            continue                      # tied at the top but nothing to break
        else:
            rung = RUNGS[(locus, rung_n)]
        sig = f"{label}/{locus}/{rung}"
        if e["partial"]:
            # Partial separation is orthogonal to which rung finally decided:
            # rung 1 can eliminate two of four and leave the survivors to the
            # five-star rung or the lot. Reported as its own shape so it is not
            # swallowed by whichever rung happened to finish the job.
            out.append(Obs("*/scoring/partial-separation",
                           f"round {e['round'] or 1}: a rung eliminated part of a "
                           f"{e['size'] or 3}-way tie; the rest carried on to the "
                           f"{rung} rung"))
        out.append(Obs(sig, f"round {e['round'] or 1}: {e['size'] or 2}-way tie "
                            f"at the {locus} step, resolved by the {rung} rung"
                            + (" (after rung 1 eliminated part of the group)"
                               if e["partial"] and rung_n == 1 else ""),
                       {"round": e["round"]}))

    # --- the non-score families report their rung in the contract itself ----
    if not narration:
        fam = doc["election"]["family"]
        pretty = {"ranked_robin": "RR", "approval": "Approval",
                  "plurality": "Plurality"}.get(fam, fam)
        lead_tied = {frozenset(t["tied"]) for t in reported
                     if t["stage"] == "copeland_leaders"}
        for t in reported:
            locus = {"copeland_leaders": "copeland", "seat_cutoff": "cutoff",
                     "winner": "winner", "finalists": "scoring"}.get(t["stage"], t["stage"])
            # At one seat the "cut line" IS the win, so the contract reports the
            # same tie twice — once as the leaders' tie and once as the cutoff.
            # Counting both would inflate a category and invent a Bloc tie in a
            # single-winner race.
            if locus == "cutoff" and seats == 1:
                if any(set(t["tied"]) <= s for s in lead_tied) or fam != "ranked_robin":
                    locus = "winner"
                if fam == "ranked_robin":
                    continue
            out.append(Obs(f"{pretty}/{locus}/{t['rung']}",
                           f"{len(t['tied'])} tied at {t['at']}: {', '.join(t['tied'])}"))

    # --- cross-cutting: a tie wholly above the cut line ---------------------
    rows = _tally_rows(doc)
    if rows and seats > 1:
        values = [v for _, v in rows[:seats]]
        if len(values) != len(set(values)):
            out.append(Obs("*/above-cut/silent",
                           f"{Counter(values).most_common(1)[0][1]} winners share a "
                           f"value above the cut — the SET is safe, the ORDER is not"))

    # --- cross-cutting: nobody supported anybody -----------------------------
    zero = False
    if rows:
        zero = all(v == 0 for _, v in rows)
    else:
        sc = doc["rounds"].get("scoring")
        zero = bool(sc) and all(x["value"] == 0 for x in sc)
    if zero:
        out.append(Obs("*/winner/zero-support",
                       f"every candidate scored 0; {', '.join(doc['result']['winners'])} "
                       f"elected by the floor alone"))

    # --- cross-cutting: narrated but not in the contract ---------------------
    # Count only narrated ties that actually RAN a rung: two candidates tied at
    # the top of the scoring round both advance, which is not a tie to break and
    # correctly appears in neither surface.
    # The `*/...` signatures are cross-cutting SHAPES, not ladder steps, so they
    # must not be counted against the contract's list of rungs — doing so made
    # every partial separation look like a swallowed tie as well.
    narrated_breaks = [o for o in out if not o.sig.startswith("*/")
                       and ("/scoring/" in o.sig or "/runoff/" in o.sig
                            or "/selection/" in o.sig)]
    if len(narrated_breaks) > len(reported):
        loci = ", ".join(sorted({o.sig.split("/")[1] for o in narrated_breaks}))
        out.append(Obs("*/contract/json-blind",
                       f"the report narrates {len(narrated_breaks)} tie(s) at "
                       f"[{loci}]; the JSON contract lists {len(reported)}"))
    return out


# --------------------------------------------------------------------------- #
# The sweep
# --------------------------------------------------------------------------- #
def label_for(method_key):
    return {"STAR": "STAR", "Bloc STAR": "Bloc"}.get(
        method_key, "PR" if method_key in ("allocated", "sss", "rrv") else method_key)


def seat_choices(kind, n_cands, wanted):
    if kind == "one":
        return [1]
    if kind == "many":
        return [s for s in wanted if 2 <= s < n_cands]
    return [s for s in wanted if 1 <= s < n_cands]


def run_one(tmp, profile, n_cands, method_key, seats, max_score):
    """Count one election on both surfaces. Returns (doc, narration) or None."""
    spec = METHODS[method_key]
    tmp.write_text(profile_yaml(profile, n_cands, spec["yaml"], seats,
                                f"tie sweep {method_key} c{n_cands} s{seats}"),
                   encoding="utf-8")
    doc = result_json.build(tmp)
    narration = []
    if spec["family"] == "score":
        cands, ballots, _ = w.parse_ballots_from_string(
            "\n".join([",".join(CAST[:n_cands])]
                      + [",".join(str(x) for x in b) for b in profile]))
        lines, _events = narrate(spec["fn"], ballots, seats, cands, max_score)
        narration = parse_narration(lines)
    return doc, narration


def sweep(args):
    rng = random.Random(args.seed)
    hits = OrderedDict()          # signature -> {count, witness}
    counted = 0
    scales = [[int(x) for x in s.split(",")] for s in args.scores]
    methods = list(args.methods)

    # Each combo is one (scale, field size, electorate size) shape to enumerate.
    # `fixed` pins a single profile instead — that is the all-zeros probe.
    combos = []
    if args.all_zeros:
        combos.append(("random", [0], args.zero_candidates, args.zero_voters,
                       [tuple([0] * args.zero_candidates)] * args.zero_voters))
    else:
        for shape in args.shapes:
            for scores in scales:
                for n_cands in args.candidates:
                    for n_voters in args.voters:
                        combos.append((shape, scores, n_cands, n_voters, None))

    for shape, scores, n_cands, n_voters, fixed in combos:
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td) / "sweep.yaml"
            for method_key in methods:
                spec = METHODS[method_key]
                style = ("approval" if spec["family"] == "approval" else
                         "plurality" if spec["family"] == "plurality" else "score")
                for seats in seat_choices(spec["seats"], n_cands, args.seats):
                    src = ([fixed] if fixed else
                           iter_profiles(n_cands, n_voters, scores, style,
                                         args.max_profiles, rng, shape))
                    for profile in src:
                        try:
                            doc, narration = run_one(tmp, profile, n_cands,
                                                     method_key, seats, MAX_SCORE)
                        except Exception as exc:            # noqa: BLE001
                            sig = f"!error/{method_key}/{type(exc).__name__}"
                            rec = hits.setdefault(sig, {"count": 0, "witness": None})
                            rec["count"] += 1
                            if rec["witness"] is None:
                                rec["witness"] = {"method": method_key, "seats": seats,
                                                  "profile": [list(b) for b in profile],
                                                  "candidates": n_cands,
                                                  "detail": str(exc)[:200], "scores": scores}
                            continue
                        counted += 1
                        for obs in observe(doc, narration, label_for(method_key)):
                            rec = hits.setdefault(obs.sig, {"count": 0, "witness": None})
                            rec["count"] += 1
                            size = (len(profile), n_cands)
                            if rec["witness"] is None or size < rec["witness"]["size"]:
                                rec["witness"] = {
                                    "method": method_key, "seats": seats,
                                    "candidates": n_cands, "scores": scores,
                                    "profile": [list(b) for b in profile],
                                    "winners": doc["result"]["winners"],
                                    "shape": shape,
                                    "detail": obs.detail, "size": size,
                                }
    return hits, counted


# --------------------------------------------------------------------------- #
# Reporting
# --------------------------------------------------------------------------- #
def witness_block(wit):
    cands = CAST[:wit["candidates"]]
    rows = "\n".join("    " + ",".join(str(s) for s in b) for b in wit["profile"])
    return (f"    {','.join(cands)}\n{rows}")


def report(hits, counted, args):
    print(f"\n{'=' * 78}\nTIE TAXONOMY SWEEP — {counted} elections counted")
    if args.all_zeros:
        print(f"the degenerate probe only: {args.zero_candidates} candidates, "
              f"{args.zero_voters} ballots, every score 0")
    else:
        print(f"scales: {' · '.join('{' + s + '}' for s in args.scores)}"
              f"   candidates: {args.candidates}   voters: {args.voters}   seats: {args.seats}")
        print(f"shapes: {', '.join(args.shapes)}")
    print(f"methods: {', '.join(args.methods)}\n{'=' * 78}")

    known = [(s, r) for s, r in hits.items() if s in TAXONOMY]
    unmapped = [(s, r) for s, r in hits.items() if s not in TAXONOMY and not s.startswith("!")]
    errors = [(s, r) for s, r in hits.items() if s.startswith("!")]

    print(f"\n--- MAPPED categories ({len(known)} of {len(TAXONOMY)} known) ---")
    for sig, rec in sorted(known, key=lambda x: TAXONOMY[x[0]].id):
        cat = TAXONOMY[sig]
        wit = rec["witness"]
        print(f"\n[{cat.id}] {cat.title}")
        print(f"      hits: {rec['count']}   lesson: {cat.lesson}")
        if cat.note:
            print(f"      why its own category: {cat.note}")
        print(f"      smallest witness: {wit['method']}, {wit['seats']} seat(s), "
              f"scale {{{','.join(map(str, wit['scores']))}}}, {wit.get('shape', '?')} shape "
              f"→ {', '.join(wit['winners']) if wit.get('winners') else '?'}")
        print(witness_block(wit))
        print(f"      {wit['detail']}")

    missed = [s for s in TAXONOMY if s not in hits]
    if missed:
        print(f"\n--- categories in the map this sweep did NOT reach ({len(missed)}) ---")
        for sig in missed:
            print(f"      [{TAXONOMY[sig].id}] {sig}  — {TAXONOMY[sig].title}")
        print("      (a coverage gap in the SWEEP, not necessarily in the engine —"
              "\n       widen --scores / --candidates / --seats before reading anything into it)")

    print(f"\n--- UNMAPPED — tie shapes with no lesson in the taxonomy ({len(unmapped)}) ---")
    if not unmapped:
        print("      none. Every tie this sweep produced is already a category the library teaches.")
    for sig, rec in unmapped:
        wit = rec["witness"]
        print(f"\n  !! {sig}   hits: {rec['count']}")
        print(f"     {wit['method']}, {wit['seats']} seat(s), scale "
              f"{{{','.join(map(str, wit['scores']))}}} → {', '.join(wit.get('winners') or ['?'])}")
        print(witness_block(wit))
        print(f"     {wit['detail']}")

    if errors:
        print(f"\n--- engine errors ({len(errors)}) ---")
        for sig, rec in errors:
            print(f"  {sig}  hits: {rec['count']}  e.g. {rec['witness']['detail']}")
    print()


def write_witnesses(hits, out_dir):
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    written = []
    for sig, rec in hits.items():
        wit = rec["witness"]
        if not wit:
            continue
        cid = TAXONOMY[sig].id if sig in TAXONOMY else "UNMAPPED-" + re.sub(r"\W+", "_", sig)
        name = re.sub(r"\W+", "_", f"{cid}_{wit['method']}_c{wit['candidates']}_s{wit['seats']}").strip("_")
        path = out / f"{name}.yaml"
        path.write_text(profile_yaml(wit["profile"], wit["candidates"],
                                     METHODS[wit["method"]]["yaml"], wit["seats"],
                                     f"Tie category {cid} — {sig}"),
                        encoding="utf-8")
        written.append(str(path))
    return written


def main(argv=None):
    p = argparse.ArgumentParser(
        description="Sweep coarse-scale elections for ties and check them against the taxonomy.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__.split("Examples")[-1])
    p.add_argument("--scores", action="append", default=None,
                   help="allowed score values, comma separated; repeatable "
                        "(default: 0,1,2 and 0,1,5 — the second keeps the five-star rung alive)")
    p.add_argument("-c", "--candidates", type=int, nargs="+", default=[3, 4])
    p.add_argument("-v", "--voters", type=int, nargs="+", default=[3, 4])
    p.add_argument("-s", "--seats", type=int, nargs="+", default=[1, 2])
    p.add_argument("--methods", nargs="+", default=None,
                   help=f"default: the Equal Vote set ({', '.join(EVC_METHODS)})")
    p.add_argument("--include-plurality", action="store_true",
                   help="add Choose-One as a control")
    p.add_argument("--shapes", nargs="+", default=["random"], choices=SHAPES,
                   help="how the ballots relate to each other, on top of --scores: "
                        + " · ".join(SHAPES) + " (default: random)")
    p.add_argument("--all-zeros", action="store_true",
                   help="only the degenerate probe: every voter scores every candidate 0")
    p.add_argument("--zero-candidates", type=int, default=5)
    p.add_argument("--zero-voters", type=int, default=3)
    p.add_argument("--max-profiles", type=int, default=4000,
                   help="per (method, seats, shape): enumerate exhaustively below this, "
                        "sample randomly above it (default 4000)")
    p.add_argument("--seed", type=int, default=0)
    p.add_argument("--witness-dir", help="write one witness case file per category")
    p.add_argument("--json", dest="json_out", help="write the raw hit table here")
    args = p.parse_args(argv)

    if args.scores is None:
        args.scores = ["0,1,2", "0,1,5"]
    if args.methods is None:
        args.methods = list(EVC_METHODS)
        if args.include_plurality:
            args.methods.append("Plurality")
    for spec in args.scores:
        vals = [int(x) for x in spec.split(",")]
        if not vals or min(vals) < 0 or max(vals) > MAX_SCORE:
            p.error(f"--scores {spec}: values must be 0..{MAX_SCORE} "
                    f"(the fork's teaching guardrail on the STAR ballot)")
    bad = [m for m in args.methods if m not in METHODS]
    if bad:
        p.error(f"unknown method(s): {bad}. Known: {list(METHODS)}")

    hits, counted = sweep(args)
    report(hits, counted, args)
    if args.witness_dir:
        for path in write_witnesses(hits, args.witness_dir):
            print(f"  wrote {path}")
    if args.json_out:
        Path(args.json_out).write_text(json.dumps(
            {"counted": counted,
             "hits": {s: {"count": r["count"], "witness": r["witness"],
                          "category": TAXONOMY[s].id if s in TAXONOMY else None}
                      for s, r in hits.items()}}, indent=2), encoding="utf-8")
        print(f"  wrote {args.json_out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
