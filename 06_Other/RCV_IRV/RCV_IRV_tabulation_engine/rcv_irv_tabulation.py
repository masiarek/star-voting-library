#!/usr/bin/env python3
"""
RCV / IRV tabulation engine wrapper.

Mirrors the role of ``starvote_larry_hastings.py``: it reads the same YAML
election format (score ballots, 0..5) and tabulates a single-winner
Instant-Runoff Voting (IRV) election using the vendored ``pyrankvote``
library (MIT licensed, see ./pyrankvote/LICENSE.txt).

Because the YAML ballots are *scores* but IRV needs *ranks*, this wrapper
converts each score ballot into a ranked ballot. See score_ballot_to_ranking()
for the conversion rules.

Usage:
    python rcv_irv_tabulation.py path/to/election.yaml
"""

import os
import re
import sys

# Make the vendored packages importable no matter where we're launched from.
_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

import pyrankvote  # noqa: E402  (vendored)
from pyrankvote import Ballot, Candidate  # noqa: E402

try:
    import yaml  # PyYAML
except ImportError:  # pragma: no cover
    yaml = None


# Marker characters that all count as "no support" (mirrors the STAR engine).
MARKERS = set("~&^?%-")


# --------------------------------------------------------------------------- #
# YAML loading
# --------------------------------------------------------------------------- #
def load_ballots_block(path):
    """Return (title, ballots_text) from a STAR/IRV-style YAML file."""
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    if yaml is None:
        raise RuntimeError("PyYAML is required to read .yaml election files.")
    data = yaml.safe_load(text)

    # Accept either a flat mapping (voting_method/ballots at top level) or a
    # nested race_* / election wrapper; grab the first mapping that has ballots.
    def find_ballots(d):
        if isinstance(d, dict):
            if "ballots" in d:
                return d
            for v in d.values():
                found = find_ballots(v)
                if found:
                    return found
        elif isinstance(d, list):               # e.g. election: races: [ {...} ]
            for v in d:
                found = find_ballots(v)
                if found:
                    return found
        return None

    race = find_ballots(data) or {}
    ballots_text = race.get("ballots", "")
    title = race.get("election_title") or race.get("title")
    num_winners = race.get("num_winners", race.get("seats", 1))
    try:
        num_winners = max(1, int(num_winners))
    except (TypeError, ValueError):
        num_winners = 1
    return title, ballots_text, num_winners


# --------------------------------------------------------------------------- #
# Score-ballot parsing (subset of the STAR engine's parser)
# --------------------------------------------------------------------------- #
def parse_score_ballots(ballot_string):
    """
    Parse the score-grid format into (candidates, ballots).

    ballots is a list of (weight, {candidate: score}) tuples.

    Supports:
      * header row of candidate names; a leading "Count:" label is stripped
      * per-row weight via the colon/x prefix, e.g. "30:5,4,0" or "30 x 5,4,0"
      * blank cells and marker characters count as score 0
    """
    lines = []
    for raw in ballot_string.strip().splitlines():
        line = raw.split("#")[0].strip()
        if line:
            lines.append(line)
    if not lines:
        return [], []

    headers = [h.strip() for h in re.split(r"[,\t]+", lines[0]) if h.strip()]
    if headers and re.match(r"(?i)^count\s*:", headers[0]):
        headers[0] = headers[0].split(":", 1)[1].strip()

    ballots = []
    for line in lines[1:]:
        weight = 1
        parts = re.split(r"[,\t]", line)
        wmatch = re.match(r"\s*(\d+)\s*[:xX×]\s*(.*)", parts[0])
        if wmatch:
            weight = int(wmatch.group(1))
            parts[0] = wmatch.group(2)
        cells = [p.strip() for p in parts]
        if len(cells) != len(headers):
            continue  # skip malformed rows

        def to_score(c):
            c = c.strip()
            if c == "" or c in MARKERS:
                return 0
            try:
                return int(c)
            except ValueError:
                return 0

        scores = {h: to_score(c) for h, c in zip(headers, cells)}
        ballots.append((weight, scores))
    return headers, ballots


# --------------------------------------------------------------------------- #
# Score -> rank conversion
# --------------------------------------------------------------------------- #
def score_ballot_to_ranking(scores, candidate_order):
    """
    Convert one score ballot {candidate: score} into an ordered list of
    candidate names (most-preferred first).

    Rules:
      * Higher score  -> more preferred.
      * Score 0 (or blank/marker) -> UNRANKED; the candidate is left off the
        ballot entirely (matches STAR's "0 = no support" semantics, and means
        the ballot becomes exhausted rather than transferring to a 0-score).
      * Equal NON-zero scores -> a tie. IRV needs a strict order, so ties are
        broken deterministically by candidate column order (the order the
        candidates appear in the ballot header). This is a documented
        simplification; equal-rank IRV is not represented.
    """
    ranked = [c for c in candidate_order if scores.get(c, 0) > 0]
    col_index = {c: i for i, c in enumerate(candidate_order)}
    ranked.sort(key=lambda c: (-scores[c], col_index[c]))
    return ranked


# --------------------------------------------------------------------------- #
# Ranked-ballot parsing (native RCV format, e.g. "40:A>C>B")
# --------------------------------------------------------------------------- #
def parse_ranked_ballots(ballot_string):
    """
    Parse native ranked ballots into (candidates, ballots).

    Each line is an optional weight prefix plus a '>'-separated preference
    order, most-preferred first:  "40:A>C>B"  or  "A > C > B".

    Equal ranks ("A=B") are not representable in IRV, so tied candidates are
    listed in left-to-right order (a documented simplification). Candidates that
    don't appear on a ballot are simply unranked (the ballot can exhaust).
    """
    ballots = []
    candidates = []  # first-appearance order
    for raw in ballot_string.strip().splitlines():
        line = raw.split("#")[0].strip()
        if not line:
            continue
        weight = 1
        m = re.match(r"\s*(\d+)\s*[:xX×]\s*(.*)", line)
        if m:
            weight = int(m.group(1))
            line = m.group(2).strip()
        ranking = []
        for group in line.split(">"):
            for name in group.split("="):  # equal ranks -> listed order
                name = name.strip()
                if name:
                    ranking.append(name)
                    if name not in candidates:
                        candidates.append(name)
        if ranking:
            ballots.append((weight, ranking))
    return candidates, ballots


# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #
def build_transfer_block(ranked_rows, result, total):
    """Where the votes went, and how many stopped counting — as report lines.

    WHY THIS EXISTS. The round tables above are pyrankvote's own rendering, and
    they give each candidate's total per round and nothing else. The two numbers
    every teaching page in this repo argues about are the two they omit: where a
    transferred vote came FROM, and how many ballots have gone inactive — so the
    "majority" a round declares can be checked against the ballots actually cast
    rather than taken on faith. (The Sankey art shows the first of those, but
    only on a generated page; a `_tabulated` mirror is plain text.)

    THE ELIMINATIONS ARE READ BACK, NEVER RECOMPUTED. `result.rounds` carries
    pyrankvote's own per-round status for every candidate, so the eliminated set
    each round is taken from the count that just printed. Only the *destinations*
    are worked out here, by walking each held ballot to its next surviving
    preference. Recomputing the eliminations instead would let this block
    contradict the table above it whenever an elimination tie is resolved by the
    second-choices ladder — which is exactly the case a reader would be reading
    this block to understand.

    Returns None when there is nothing to add: STV (surplus transfers are
    fractional and are NOT modelled here), or a count that never eliminated
    anyone.
    """
    from pyrankvote.helpers import CandidateStatus

    rounds = getattr(result, "rounds", None)
    if not rounds or total <= 0:
        return None

    # Per round: who was still standing, and who this round rejected.
    all_names = [cr.candidate.name for cr in rounds[0].candidate_results]
    gone, steps = set(), []
    for rnd in rounds:
        active = [n for n in all_names if n not in gone]
        tally = {cr.candidate.name: cr.number_of_votes for cr in rnd.candidate_results}
        rejected = [cr.candidate.name for cr in rnd.candidate_results
                    if cr.status == CandidateStatus.Rejected
                    and cr.candidate.name not in gone]
        elected = [cr.candidate.name for cr in rnd.candidate_results
                   if cr.status == CandidateStatus.Elected]
        steps.append({"active": active, "tally": tally,
                      "rejected": rejected, "elected": elected})
        gone |= set(rejected)

    if len(elected) > 1:            # STV — surplus transfers aren't modelled
        return None
    if not any(s["rejected"] for s in steps[:-1]):
        return None                 # nobody was ever eliminated: no transfers

    def held_by(ranks, active):
        return next((c for c in ranks if c in active), None)

    L = ["--- Transfers and inactive ballots (what the round tables leave out) ---",
         "The tables above give each candidate's round total but not where a",
         "transferred vote came FROM, nor how many ballots stopped counting.",
         "Both are recomputed from the ballots, using the eliminations the",
         "count above actually made."]

    last_active_ballots = total
    for i, step in enumerate(steps):
        active_ballots = sum(step["tally"].get(n, 0) for n in step["active"])
        active_ballots = int(round(active_ballots))
        last_active_ballots = active_ballots
        majority = active_ballots // 2 + 1
        head = "FINAL ROUND" if i == len(steps) - 1 else f"ROUND {i + 1}"
        inactive = total - active_ballots
        L.append("")
        L.append(f"{head} — {active_ballots} of {total} ballots still active"
                 + (f" ({inactive} inactive)" if inactive else "")
                 + f"; majority = {majority}")

        # THE FINAL ROUND TRANSFERS NOTHING, whatever its Status column says.
        # pyrankvote marks every non-winner "Rejected" in the last table, but the
        # count has already stopped: those ballots are not eliminated-and-moved,
        # they are simply where the election ended. Printing a transfer for them
        # would invent a round that never happened — and would paper over the
        # very case this block exists to expose (a ballot that stayed active to
        # the end and still had its lower rankings go unread).
        if i == len(steps) - 1:
            for n in sorted(step["active"],
                            key=lambda c: -step["tally"].get(c, 0)):
                got = int(round(step["tally"].get(n, 0)))
                pct = got / active_ballots * 100 if active_ballots else 0.0
                mark = "  ← elected" if n in step["elected"] else ""
                L.append(f"   {n:<20} {got:>6}  ({pct:.1f}% of the still-active)"
                         f"{mark}")
            # Ballots that never exhausted and never transferred: held by a
            # candidate who was still standing when counting stopped, yet
            # carrying a further preference nobody ever read.
            unread = {}
            for weight, ranks in ranked_rows:
                held = held_by(ranks, step["active"])
                if held is None or held in step["elected"]:
                    continue
                if ranks[ranks.index(held) + 1:]:
                    unread[held] = unread.get(held, 0) + weight
            if unread:
                L.append("   Never exhausted, never transferred:")
                for n, count in sorted(unread.items(), key=lambda kv: -kv[1]):
                    word = "ballot" if count == 1 else "ballots"
                    L.append(f"      {count} {word} held by {n} carried a lower "
                             "ranking that was never read")
                L.append("      (the count stopped here, so those preferences did "
                         "nothing).")
            continue

        after = [n for n in step["active"] if n not in step["rejected"]]
        moved = {n: {} for n in step["rejected"]}
        for weight, ranks in ranked_rows:
            held = held_by(ranks, step["active"])
            if held not in moved:
                continue
            dest = held_by(ranks, after) or "(no continuing ranking)"
            moved[held][dest] = moved[held].get(dest, 0) + weight
        for n in sorted(step["rejected"], key=lambda c: step["tally"].get(c, 0)):
            got = int(round(step["tally"].get(n, 0)))
            L.append(f"   {n} eliminated with {got}:")
            dests = sorted(moved[n].items(), key=lambda kv: (-kv[1], kv[0]))
            for dest, count in dests:
                tag = "  ← these ballots go inactive" \
                    if dest.startswith("(no continuing") else ""
                L.append(f"      → {dest:<20} {count:>6}{tag}")
            if not dests:
                L.append("      → (held no ballots)")

    winner = steps[-1]["elected"][0] if steps[-1]["elected"] else None
    inactive = total - last_active_ballots
    L.append("")
    L.append(f"Inactive ballots at the final round: {inactive} of {total} "
             f"({inactive / total * 100:.1f}%).")
    if winner:
        got = int(round(steps[-1]["tally"].get(winner, 0)))
        of_cast = got / total * 100
        if got * 2 > total:
            L.append(f"   {winner}'s {got} is a majority of the {last_active_ballots} "
                     f"still active AND of all {total} cast ({of_cast:.1f}%).")
        else:
            L.append(f"   {winner}'s {got} is a majority of the {last_active_ballots} "
                     f"still active but only {of_cast:.1f}% of all {total} cast —")
            L.append("   the 'majority' here is of a shrunken denominator. See")
            L.append("   06_Other/RCV_IRV/concepts/RCV_IRV_exhausted_ballots.md")
    return L


def tabulate(path):
    """Count the file and return the result data, printing NOTHING.

    Split out of `run()` so a machine-readable consumer (the JSON result
    contract — see `STARVote_LH_tabulation_engine/result_json.py`) gets the
    same rounds, the same eliminations and the same seeded tie ladder as the
    printed report, instead of re-deriving them or scraping the text.

    Returns a dict: title, seats, ranked_mode, candidates, ranked_rows
    (weight, ranking), total ballots, and pyrankvote's `result`.
    """
    # Elimination ties: seed the RNG so the last rung is stable run to run.
    # See run()'s note for what the seed does and does not buy.
    import random
    random.seed(0)
    title, ballots_text, num_winners = load_ballots_block(path)
    seats = max(1, int(num_winners or 1))

    # Auto-detect: '>' means native ranked ballots; otherwise score ballots.
    # Strip per-line comments first, so a rank annotation in a score-ballot
    # comment (e.g. "14:4,3,5,2,1  # Carmen base (C > A > B)") doesn't get
    # misread as a real ranked ballot. (Mirrors the STAR engine.)
    _detect = "\n".join(line.split("#")[0] for line in ballots_text.splitlines())
    ranked_mode = ">" in _detect
    if ranked_mode:
        candidates_names, parsed = parse_ranked_ballots(ballots_text)
    else:
        candidates_names, parsed = parse_score_ballots(ballots_text)
    if not parsed:
        print("Error: no valid ballots found.")
        sys.exit(1)                             # an error must not exit 0

    cand_objs = {name: Candidate(name) for name in candidates_names}
    pv_ballots = []
    ranked_rows = []            # (weight, ranking) — what build_transfer_block walks
    total = 0
    for weight, payload in parsed:
        if ranked_mode:
            ranking = payload  # already an ordered list of names
        else:
            ranking = score_ballot_to_ranking(payload, candidates_names)
        ranked_objs = [cand_objs[n] for n in ranking]
        for _ in range(weight):
            pv_ballots.append(Ballot(ranked_candidates=ranked_objs))
        ranked_rows.append((weight, list(ranking)))
        total += weight

    if seats > 1:
        result = pyrankvote.single_transferable_vote(
            list(cand_objs.values()), pv_ballots, number_of_seats=seats
        )
    else:
        result = pyrankvote.instant_runoff_voting(
            list(cand_objs.values()), pv_ballots
        )

    return {
        "title": title,
        "seats": seats,
        "ranked_mode": ranked_mode,
        "candidates": candidates_names,
        "ranked_rows": ranked_rows,
        "total": total,
        "result": result,
    }


def run(path, extras=False):
    """Tabulate and print. Returns the transfer/inactive block as text (or None).

    `extras` controls only whether that block is PRINTED. It is always returned,
    so the LH engine can append it to the always-full `_tabulated` mirror while
    the on-screen echo stays minimal — the same split the STAR side uses. The
    standalone CLI passes extras=True: running this file directly is the
    everything-on view.
    """
    # Elimination ties. pyrankvote's ladder (_cmp_candidate_vote_counts in
    # pyrankvote/helpers.py) is better than "it flips a coin": on equal first
    # choices it compares MOST SECOND CHOICES, then thirds, then fourths, and
    # only reaches random.choice() once it runs out of ranks — structurally the
    # same shape as the STAR engine's pairwise -> five-star -> lot ladder.
    # Seed the RNG so that last rung is at least stable run to run; unseeded,
    # the SAME ballots can elect DIFFERENT winners on consecutive runs, which is
    # unacceptable for a library whose counts must reproduce.
    #
    # KNOWN LIMITATION, and do not overstate what the seed buys. sorted() feeds
    # the comparator pairs in an order set by the input list, and that list is
    # built in order of each candidate's FIRST APPEARANCE across the ballot
    # rows. So a fixed seed pins the SEQUENCE of coin flips, not the CANDIDATE
    # each flip lands on. When the ladder dies — every candidate tied at every
    # rank, e.g. a perfect 3-cycle — the winner is the first row's first choice,
    # and re-ordering the identical ballots elects somebody else. That is an
    # ANONYMITY failure (who cast which ballot changed the result), and the
    # report does not disclose it.
    #
    # Pinned by tests/test_rcv_irv_tie_order_sensitivity.py; explained in
    # RCV_IRV_tabulation_engine/README.md ("Known limitation — elimination
    # ties") and 07_Concepts/topics/ties/batch_elimination.md.
    t = tabulate(path)
    title, seats, total = t["title"], t["seats"], t["total"]
    ranked_mode, ranked_rows = t["ranked_mode"], t["ranked_rows"]
    result = t["result"]

    if seats > 1:
        label = f"STV / Single Transferable Vote (multi-winner — {seats} seats)"
    else:
        label = "RCV / Instant-Runoff Voting (single winner)"

    print(f"\n--- {label} ---")
    if title:
        print(f"  {title}")
    source = ("ranked ballots" if ranked_mode
              else "converted from score ballots; 0 = unranked")
    print(f" Tabulating {total} ballots ({source}).")
    if seats > 1:
        # Name the quota the COUNT applies, not a different one.
        # pyrankvote's single_transferable_vote uses the EXACT Droop quota
        # votes/(seats+1): it elects at >= that line and measures every
        # surplus from it. "Droop quota" also names the integer form
        # floor(votes/(seats+1))+1 used by Irish/Scottish hand counts, one
        # vote higher — so print both, or a reader hand-checking the count
        # cannot reconcile the final table with this header.
        quota = total / (seats + 1)
        hand = total // (seats + 1) + 1
        print(f" {seats} seats; quota = {quota:.2f} "
              f"(exact Droop, votes/(seats+1)) — {quota / total * 100:.1f}% of {total}.")
        print(f" Elected at >= quota, and every surplus is measured from it.")
        print(f" (Hand-count Droop, floor({total}/{seats + 1})+1 = {hand}, is a "
              f"different but equally standard rule.)")
    print()

    print(result)

    winners = result.get_winners()
    print(f"\nWinner(s) — {label}")
    if winners:
        for w in winners:
            print(f"  {w.name}")
    else:
        print("  (no winner)")

    block = None
    if seats == 1:
        try:
            lines = build_transfer_block(ranked_rows, result, total)
            block = "\n".join(lines) if lines else None
        except Exception:
            block = None            # a report add-on must never fail a count
    if block and extras:
        print()
        print(block)
    return block


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    run(sys.argv[1], extras=True)
