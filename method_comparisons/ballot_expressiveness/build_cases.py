# /// script
# requires-python = ">=3.10"
# ///
"""build_cases.py — generate the five ballot-expressiveness case files.

ONE electorate, FIVE papers. Twenty-five voters and nine candidates sit at frozen
positions on a single left-right spectrum; every ballot below is derived from those
positions by a stated rule, never hand-written. What changes between the files is only
what the voter is allowed to write down:

    _star.yaml       a 0-5 score ballot          -> elects Finn  (the Condorcet winner)
    _rr_full.yaml    a ranking of all nine       -> elects Finn
    _rr_top5.yaml    a ranking capped at five    -> elects Gus
    _irv_full.yaml   a ranking of all nine       -> elects Ben
    _irv_top5.yaml   a ranking capped at five    -> elects Ben

The pair worth staring at is _rr_full vs _rr_top5: SAME voters, SAME Copeland rule,
different paper, different winner. The cap is not invented for the lesson -- New York
City and Maine cap their ranked ballots at five, and San Francisco used three for years.

NOTHING HERE IS SETTLED BY A TIE-BREAK. That is a search constraint, not luck. An
earlier candidate electorate for this folder had an 8-8 IRV elimination tie, so its
IRV leg came out Cleo under one lot rule and Dev under the engine's -- a lesson a coin
could flip is not a lesson. Every count below has a strict winner at every decision:
unique Copeland maxima, a unique second finalist and an untied runoff in STAR, and a
unique fewest-first-choices candidate in every IRV round.

Positions are frozen constants, not sampled, so this script is deterministic and needs
no numpy. They came from a search over spatial1d electorates for a case where the coarse
score ballot finds the Condorcet winner and the capped ranked ballot loses them
(06_Other/simulations/condorcet_efficiency_simulation.py --expressiveness measures how
often that happens; this file is one instance of it).

Usage:  uv run method_comparisons/ballot_expressiveness/build_cases.py
"""
from pathlib import Path

NAMES = ["Ada", "Ben", "Cleo", "Dev", "Emma", "Finn", "Gus", "Hugo", "Iris"]
CAND = [-0.7269, -0.3746, -0.1827, -0.1650, -0.1137, 0.2417, 0.4095, 0.8009, 0.8421]
VOTERS = [-0.4328, 0.5994, -0.6703, 0.8948, 0.1779, -0.1281, 0.5876, 0.7194, 0.3397,
          0.6943, 0.2346, -0.3001, -0.5104, 0.8892, -0.0534, 0.6022, 0.2785, -0.4001,
          0.6223, -0.6336, 0.2744, -0.6116, -1.3335, -0.2318, -1.8171]
CAP = 5                                     # NYC and Maine cap at five ranks
HERE = Path(__file__).resolve().parent / "cases"


def utilities(v):
    """One voter's opinion of every candidate: minus the distance along the spectrum."""
    return [-abs(v - c) for c in CAND]


def scores(v):
    """The voter's own min-max scaling of those opinions onto 0-5, rounded.

    Rounding to six rungs is the whole subject: it is what forces a voter with nine
    genuine opinions to say the same thing about two of them.
    """
    u = utilities(v)
    lo, hi = min(u), max(u)
    span = (hi - lo) or 1.0
    return [round(5 * (x - lo) / span) for x in u]


def ranking(v, cap=None):
    """The voter's strict ranking, best first, optionally cut off after `cap` names."""
    order = sorted(range(len(CAND)), key=lambda i: -utilities(v)[i])
    return [NAMES[i] for i in (order[:cap] if cap else order)]


OPTIONS_SCORE = """options:
  show_description: false
  show_matrix: true
  matrix_finalists_only: false
  show_condorcet: true
  show_score_counts: false
  show_irv: false
  show_runoff_percent: true
  brief: true
  collapse_ballots: true
  count_separator: "×"
"""

OPTIONS_RANKED = """options:
  show_description: false
  show_matrix: true
  matrix_finalists_only: false
  show_condorcet: true
  show_score_counts: false
  show_irv: false
  show_smith_set: true
  show_runoff_percent: true
  brief: true
  collapse_ballots: true
  count_separator: "×"
"""

CONSTRUCTION = """  Construction: build_cases.py in this folder. 25 voters and 9 candidates at frozen
  positions on one spectrum — Ada −0.73 · Ben −0.37 · Cleo −0.18 · Dev −0.17 ·
  Emma −0.11 · Finn +0.24 · Gus +0.41 · Hugo +0.80 · Iris +0.84; utility = minus the
  distance; scores = each voter's own min-max scaling onto 0–5; rankings = those same
  utilities in order. Nothing is tuned to the result, and **no count in this folder is
  settled by a tie-break** — that was a search constraint, so every winner here survives
  any lot rule."""


"""Four of the five papers are also live on BetterVoting as BV2280 (`37yf8x`), one
race each, so a reader can fill the ballots in themselves and watch a nine-candidate
0-5 ballot run out of rungs. BV agrees with the LH engine on all four winners and
reports tieBreakType 'none' throughout. The fifth (IRV capped at five) is LH-only:
it is the control that changes nothing, and it did not earn a permanent public race."""
BV_TEST_ID = "BV2280"
BV_ELECTION_ID = "37yf8x"

# Case stems. The four papers that are live on BetterVoting lead with the bvid, the
# house naming rule for a BV-backed case; the fifth is LH-only and keeps a descriptive
# name. Both forms sit side by side in method_comparisons/felsenthal_paradoxes/ too.
# They are constants rather than literals because the scenario_descriptions cross-
# reference each other by filename, and a rename that updated the files but not the
# prose would leave every case pointing at a name that no longer exists.
S_STAR = f"bv2280_{BV_ELECTION_ID}_star"
S_RR_FULL = f"bv2280_{BV_ELECTION_ID}_rr_full"
S_RR_TOP5 = f"bv2280_{BV_ELECTION_ID}_rr_top5"
S_IRV_FULL = f"bv2280_{BV_ELECTION_ID}_irv_full"
S_IRV_TOP5 = "ballot_expressiveness_c9_irv_top5"      # LH-only: no BV race


def bv_fields(on_bv):
    if not on_bv:
        return ("# Not on BetterVoting: this is the control leg that changes nothing.\n"
                "# The other four papers are BV2280 (37yf8x).\n")
    return (f'bv_test_id: {BV_TEST_ID}\n'
            f'bv_election_id: {BV_ELECTION_ID}\n'
            f'bv_results_url: https://bettervoting.com/{BV_ELECTION_ID}/results\n')


def write(stem, title, method, description, ballots, winner, on_bv=True):
    opts = OPTIONS_SCORE if method == "STAR" else OPTIONS_RANKED
    body = f"""election_title: "{title}"

scenario_description: |-
{description}

{CONSTRUCTION}

voting_method: {method}
num_winners: 1

{bv_fields(on_bv)}
lot_numbers: [{", ".join(NAMES)}]

{opts}
ballots: |-
{ballots}

expected_winners:
  - {winner}

# file: {stem}.yaml
"""
    (HERE / f"{stem}.yaml").write_text(body)
    print(f"wrote cases/{stem}.yaml")


def score_block():
    rows = [f"  {','.join(NAMES)}"]
    rows += [f"  {','.join(str(x) for x in scores(v))}    # voter at {v:+.2f}"
             for v in VOTERS]
    return "\n".join(rows)


def rank_block(cap=None):
    return "\n".join(f"  {'>'.join(ranking(v, cap))}    # voter at {v:+.2f}"
                     for v in VOTERS)


def main():
    HERE.mkdir(parents=True, exist_ok=True)

    write(
        S_STAR,
        "Nine candidates, 25 voters — the 0–5 score ballot",
        "STAR",
        f"""  THE COARSE BALLOT GETS IT RIGHT. Finn beats all eight rivals head-to-head, and STAR
  elects them from a ballot that cannot even rank the field.

  Nine candidates will not fit on six rungs — 0, 1, 2, 3, 4 and 5 hold six distinct
  places, so every voter here must give at least two candidates the same score. They
  actually tie far more than that minimum: about 16% of all candidate pairs go equal on
  this paper, against a pigeonhole floor of 8%. Most of the flattening is rounding, not
  the hard limit.

  And it does not matter. The preference that decides this election — Finn over everyone
  — survives the rounding, so STAR returns the Condorcet winner anyway.

  Read this file against {S_RR_TOP5}.yaml, where the same 25 voters
  fill in a RANKED ballot capped at five names, the cap New York City and Maine actually
  use, and the count elects Gus instead. The ballot usually called "more expressive"
  loses the answer that these six rungs kept.""",
        score_block(),
        "Finn",
    )

    write(
        S_RR_FULL,
        "Nine candidates, 25 voters — ranking all nine, counted by Ranked Robin",
        "RankedRobin",
        f"""  THE CONTROL. Every voter ranks all nine candidates, nothing truncated and nothing
  rounded, and Ranked Robin returns Finn — the candidate who beats each of the other
  eight head-to-head.

  This is the full-resolution ranked ballot that Condorcet-efficiency simulations
  normally hand to ranked methods. It is also an idealization: no large-field
  jurisdiction issues it. {S_RR_TOP5}.yaml cuts it down to five
  ranks, which is what a real ranked ballot looks like, and the winner changes.

  Compare with {S_STAR}.yaml: the 0–5 score ballot agrees with this
  one. Compare with {S_IRV_FULL}.yaml: the SAME ballots, counted by
  instant runoff, do not — which is the cleanest evidence in this folder that the paper
  and the count are separate things.""",
        rank_block(),
        "Finn",
    )

    write(
        S_RR_TOP5,
        "Nine candidates, 25 voters — ranking only five, counted by Ranked Robin",
        "RankedRobin",
        f"""  THE CAP CHANGES THE WINNER. Same 25 voters, same Ranked Robin rule as
  {S_RR_FULL}.yaml. The only difference is that each voter may name
  five candidates instead of nine — and Gus wins instead of Finn.

  Finn is the Condorcet winner on the electorate's real preferences. What the cap removes
  is the evidence: only 16 of the 25 voters can fit Finn into five names at all. For the
  other 9 Finn is simply absent from the paper, and an absent candidate wins no
  head-to-head.

  This is the reversal worth remembering. A ranked ballot is usually called the more
  expressive one, and at full resolution it is. Capped at five names out of nine it
  records 3,620 distinct opinions where the 0–5 score ballot records 10,077,696 — and
  here it loses an answer that six rungs kept.

  Convention, stated: a candidate left unranked is counted as beaten by everyone the
  voter did rank, and tied with everyone else the voter left off. Other treatments split
  that unstated pair half-and-half. It is a choice, not arithmetic, and it belongs in
  any quotation of this result.""",
        rank_block(CAP),
        "Gus",
    )

    write(
        S_IRV_FULL,
        "Nine candidates, 25 voters — ranking all nine, counted by RCV-IRV",
        "RCV-IRV",
        f"""  THE EXPRESSIVE BALLOT DOES NOT RESCUE THE COUNT. These are the same complete,
  full-resolution rankings as {S_RR_FULL}.yaml — every voter's
  opinion of all nine candidates, nothing rounded and nothing truncated. Instant runoff
  still elects Ben, not the Condorcet winner Finn.

  That is the point this file exists to make, and it is the cleanest comparison in the
  folder because only ONE thing differs from the Ranked Robin control: the count. Same
  voters, same paper, same ink — Ranked Robin returns Finn and RCV-IRV returns Ben. So
  the paper cannot be what decided it.

  The mechanism is center squeeze, sharpened by the crowd: Finn stands in the middle of
  nine candidates on one spectrum,
  so the first-choice votes that elimination reads are split among the neighbours, and
  Finn is eliminated before the head-to-heads Finn wins are ever consulted.

  It also explains a measured oddity on the topic page: IRV's Condorcet efficiency barely
  moves when you hand it a coarse ballot instead of a fine one, because it only ever
  reads each ballot's top surviving choice. Resolution it never looks at costs it
  nothing — and buys it nothing either.""",
        rank_block(),
        "Ben",
    )

    write(
        S_IRV_TOP5,
        "Nine candidates, 25 voters — ranking only five, counted by RCV-IRV",
        "RCV-IRV",
        f"""  BOTH LIMITS AT ONCE, and the winner does not move again. Five ranks out of nine,
  counted by instant runoff: Ben, exactly as in {S_IRV_FULL}.yaml.

  This file is the honest control on the rest of the folder, and it is the one that stops
  the lesson from overreaching. Ranked Robin's winner DID change when the ballot was
  capped (Finn → Gus). IRV's did not — because IRV had already lost Finn on the uncapped
  ballot, for a completely different reason: too few first choices. Truncation and
  elimination are separate failures, and here stacking them changes nothing.

  So "the cap costs you the answer" is a claim about the COUNT as much as the paper. It
  bites a method that reads the whole ballot, and glances off one that only reads the
  top of it.

  Convention, stated: an unranked candidate is beaten by everyone the voter ranked. A
  ballot whose five names have all been eliminated is EXHAUSTED — it leaves the count and
  the majority denominator, which is what a rank cap really does to an instant runoff.""",
        rank_block(CAP),
        "Ben",
        on_bv=False,
    )


if __name__ == "__main__":
    main()
