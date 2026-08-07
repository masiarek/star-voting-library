# /// script
# requires-python = ">=3.10"
# dependencies = ["numpy"]
# ///
"""build_ladder.py — regenerate the crowded-field ladder from the positions alone.

WHY A GENERATOR. The point of this case set is that **nothing about the ballots was
tuned**. One electorate is fixed, seven candidate positions are fixed, and the three
rungs are just the same election with 3, then 5, then 7 of those candidates standing.
Every score and every ranking in the generated files is *derived* from those numbers by
the repo's own rules, so a reader can check that the winner changes because the FIELD
changed and for no other reason. Hand-authoring the ballots would leave that open.

THE CONSTRUCTION (all three rungs, no exceptions):

  * 65 voters sit on a one-dimensional spectrum in seven blocs, at 0, 4, 8, 12, 16, 20
    and 24, of sizes 6, 10, 13, 9, 12, 8 and 7. Lumpy but ordinary — no bloc is a
    majority, and nobody sits at an extreme on their own.
  * each candidate stands at a fixed point on that spectrum and never moves:
        Ana 1 · Bruno 6 · Clara 9 · Diego 11 · Elsa 14 · Felix 16 · Greta 22
  * a voter's utility for a candidate is minus the distance between them.
  * the 0-5 SCORE ballot is that bloc's own min-max scaling of its utilities onto 0-5,
    rounded — `scores_from_util()` from 06_Other/simulations/star_vs_rr_divergence.py,
    imported rather than re-implemented so there is one rule in the repo, not two.
  * the RANKED ballot is the same utilities in order, and the APPROVAL ballot is the
    score ballot thresholded at 4.

WHAT MOVES BETWEEN RUNGS. Only the guest list. Diego, at 11, beats every rival
head-to-head at every rung — the electorate never changes its mind, and the Ranked
Robin files prove it three times. What changes is how many other names are on the paper.

NOTHING HERE IS DECIDED BY A TIE-BREAK. The positions and bloc sizes were chosen so
that at all three rungs the plurality count, both score placings, the runoff, every IRV
elimination and the approval count each resolve outright. That matters more than it
sounds: an earlier draft of this ladder had RCV-IRV eliminating on a tied round, and the
"IRV misses the Condorcet winner" result flipped when the engine broke that tie the
other way. A demonstration that turns on a coin demonstrates nothing.

Note that the score ballots DO change between rungs even for a bloc whose opinions did
not: min-max scaling is relative to the field, so a new candidate rescales everyone's
ballot. That is not an artifact of the construction — it is what a real voter does when
a new name appears, and it is part of why field size costs a score ballot accuracy. The
ranked ballots change only by insertion.

Usage:  uv run method_comparisons/crowded_field/build_ladder.py          # rewrite the YAMLs
        uv run method_comparisons/crowded_field/build_ladder.py --check  # verify, write nothing
"""
import argparse
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
sys.path.insert(0, str(REPO / "06_Other" / "simulations"))
from star_vs_rr_divergence import scores_from_util                # noqa: E402

BLOCS = [0, 4, 8, 12, 16, 20, 24]
SIZES = [6, 10, 13, 9, 12, 8, 7]                 # 65 voters
POSITION = {"Ana": 1, "Bruno": 6, "Clara": 9, "Diego": 11,
            "Elsa": 14, "Felix": 16, "Greta": 22}
RUNGS = {
    3: ["Ana", "Diego", "Greta"],
    5: ["Ana", "Bruno", "Diego", "Elsa", "Greta"],
    7: ["Ana", "Bruno", "Clara", "Diego", "Elsa", "Felix", "Greta"],
}
WINNER = {                       # what each rung's files assert
    (3, "star"): "Diego", (3, "rr"): "Diego", (3, "irv"): "Diego", (3, "approval"): "Diego",
    (5, "star"): "Diego", (5, "rr"): "Diego", (5, "irv"): "Elsa",  (5, "approval"): "Diego",
    (7, "star"): "Clara", (7, "rr"): "Diego", (7, "irv"): "Clara", (7, "approval"): "Felix",
}
APPROVAL_CUTOFF = 4              # sincere approval: approve everyone you'd score 4 or 5


def utilities(names):
    b = np.array(BLOCS, dtype=float)[:, None]
    c = np.array([POSITION[n] for n in names], dtype=float)[None, :]
    return -np.abs(b - c)


def score_rows(names):
    return scores_from_util(utilities(names))


def ranked_rows(names):
    out = []
    for row in utilities(names):
        order = sorted(range(len(names)), key=lambda i: -row[i])
        out.append(">".join(names[i] for i in order))
    return out


def approval_rows(names):
    """Sincere approval, from the SAME score ballot: approve at 4 or 5.

    The cutoff is a modelling choice, not a fact about Approval — it is why the method
    has no single answer here or anywhere, and it is stated on every file it produces.
    """
    return (score_rows(names) >= APPROVAL_CUTOFF).astype(int)


def no_equidistance():
    """Every ranked ballot must be strict — checked, not assumed."""
    pos = [POSITION[n] for n in RUNGS[7]]
    for b in BLOCS:
        d = sorted(abs(b - p) for p in pos)
        for x, y in zip(d, d[1:]):
            if abs(x - y) < 1e-9:
                raise AssertionError(
                    f"the bloc at {b} is equidistant from two candidates; its ranked "
                    "ballot would need an arbitrary tie-break"
                )


# --- shared blocks -----------------------------------------------------------
OPTIONS_STAR = """options:
  show_description: false
  show_matrix: true
  matrix_finalists_only: false
  show_condorcet: true
  show_score_counts: false
  show_irv: true
  show_runoff_percent: true
  brief: true
  collapse_ballots: true
  count_separator: "×"
"""

OPTIONS_RR = """options:
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

OPTIONS_PLAIN = """options:
  show_description: false
  show_matrix: false
  matrix_finalists_only: false
  show_condorcet: false
  show_score_counts: false
  show_irv: false
  show_runoff_percent: true
  brief: true
  collapse_ballots: true
  count_separator: "×"
"""

CONSTRUCTION = """  Construction: build_ladder.py in this folder. 65 voters in seven blocs at 0, 4, 8, 12,
  16, 20, 24 (sizes 6, 10, 13, 9, 12, 8, 7); candidates fixed at Ana 1 · Bruno 6 ·
  Clara 9 · Diego 11 · Elsa 14 · Felix 16 · Greta 22; utility = minus distance; scores =
  each bloc's own min-max scaling onto 0–5. Nothing is tuned, and no count at any rung is
  settled by a tie-break."""


# --- the per-file prose ------------------------------------------------------
STAR_STORY = {
    3: """  RUNG 1 of the crowded-field ladder — three candidates, and all six methods agree.

  Diego stands at 11 on a 0–24 spectrum, near the middle of where the voters are. He
  beats both rivals head-to-head, so he is the Condorcet winner; he leads the scoring
  round 266 to Greta's 123 and Ana's 119, and takes the runoff 50–15 with nobody
  undecided. He even holds an outright majority of first choices, 34 of 65.

  Ranked Robin, Score, Approval, RCV-IRV and Choose-One elect him too. That is the point
  of this rung: with a small field there is nothing to argue about, so any disagreement
  further up the ladder was caused by the candidates who joined — the voters never move.""",
    5: """  RUNG 2 — the same 65 voters, the same opinions, two more names on the paper.

  Bruno (6) and Elsa (14) join, one on each side of Diego. Nobody has changed their mind:
  Diego still beats all four rivals head-to-head, so he is still the Condorcet winner,
  and STAR still elects him — 244 in the scoring round to Elsa's 220, then the runoff
  38–27.

  The choose-one family has already broken, in two different directions. Choose-One now
  elects Bruno, whose 23 first choices beat Diego's 9 — and Diego's collapse from 34 to 9
  is arithmetic, not persuasion: Bruno and Elsa now stand between him and the voters who
  previously had nobody closer. RCV-IRV elects Elsa. Both results are in
  crowded_field_c5_irv.yaml, which counts them on real ranked ballots.

  Score and Approval are still with STAR here. They break at the next rung.""",
    7: """  RUNG 3 — seven candidates, and the score ballot runs out of room.

  Clara (9) and Felix (16) join, one on each side again, both closer in than the last
  pair. Diego STILL beats every one of the other six head-to-head — six wins out of six,
  the Condorcet winner for the third rung running, and Ranked Robin returns him
  (crowded_field_c7_ranked_robin.yaml).

  STAR does not. Clara, standing two steps from Diego, edges him in the scoring round
  225 to 219. Both reach the runoff — so this is NOT the top-two rule discarding anyone,
  the mechanism people usually reach for — and Clara wins it 23–17, with **25 of the 65
  voters expressing no preference at all** between the two. That is the lesson in one
  line: seven candidates on a six-rung ballot (0–5) leaves little room to separate two
  candidates standing near each other, so a preference that is perfectly real on the
  spectrum is not on the paper.

  Read the pairwise matrix against the score totals. Diego wins every column and loses
  the election. On the ranked ballots of the same voters he beats Clara 36–29
  (crowded_field_c7_ranked_robin.yaml); on this 0–5 ballot that margin has been rounded
  away.

  One warning about this file's [Divergence from STAR] block: it converts scores to ranks
  to guess at RCV-IRV and Choose-One, and the engine's own note says how many ballots
  carry tied scores. Take those two results from crowded_field_c7_irv.yaml instead, where
  the ballots are real rankings.""",
}

RR_STORY = {
    3: """  RUNG 1, counted by Ranked Robin. Diego beats Ana 49–16 and Greta 50–15: a clean
  Condorcet winner and a Smith set of one. Agrees with crowded_field_c3_star.yaml and
  with every other method at this rung.""",
    5: """  RUNG 2, counted by Ranked Robin. Two candidates joined; Diego still beats all four
  rivals, so the Smith set is still {Diego} and the electorate's answer has not moved.
  Hold this next to crowded_field_c5_star.yaml, where STAR agrees — and against
  crowded_field_c5_irv.yaml, where instant runoff and Choose-One do not.""",
    7: """  RUNG 3, counted by Ranked Robin — the control for the whole ladder.

  Diego beats all SIX rivals head-to-head. The electorate's answer has not budged since
  rung 1, and Ranked Robin returns it, because a ranked ballot at seven candidates can
  still say which of Clara and Diego a voter prefers: **Diego beats Clara 36–29** right
  here in the round-robin. The 0–5 score ballot in crowded_field_c7_star.yaml largely
  cannot — 25 of 65 voters score the two identically there, and Clara takes the runoff
  23–17 out of what is left.

  So this file is the control, and it carries the caveat that goes with being one: it
  reads a full-resolution ranking while the STAR file reads six rungs. Part of the gap
  between the two at this rung is ballot expressiveness rather than tabulation rule. A
  real 0–5 STAR election really does have only six rungs, so the cost still lands on
  STAR — but it is not the automatic runoff that caused it. The folder README works
  through both halves of that.""",
}

IRV_STORY = {
    3: """  RUNG 1, counted by RCV-IRV on the voters' real rankings. Diego takes 34 first
  choices of 65 — an outright majority in round 1 — and the count ends there. Nothing
  for instant runoff to get wrong yet.

  Round 1 of this report is also the Choose-One (Plurality) result: Diego, 34 of 65.""",
    5: """  RUNG 2 — the same voters, two more candidates, and both choose-one methods lose the
  Condorcet winner.

  Diego still beats all four rivals head-to-head (crowded_field_c5_ranked_robin.yaml
  proves it). But first choices are what these methods count, and Bruno at 6 and Elsa at
  14 now stand between Diego and the voters who previously had nobody closer. Diego drops
  from 34 first choices to 9, is eliminated early, and the seat goes to Elsa.

  Round 1 is also the Choose-One count, and it elects Bruno on 23 of 65 — a candidate
  Diego beats head-to-head. Note what caused all of this: not one voter changing their
  mind, only two more names on the ballot.""",
    7: """  RUNG 3 — seven candidates, and Diego is down to 9 first choices out of 65 while
  still beating all six rivals head-to-head.

  He is eliminated; RCV-IRV elects Clara. Round 1 doubles as the Choose-One count, which
  elects Greta on 15 — the candidate standing furthest from the middle of the electorate,
  and one Diego beats 50–15 one-on-one.

  Counted here on the ranked ballots, deliberately. At seven candidates the 0–5 ballot in
  crowded_field_c7_star.yaml carries ties on most rows, so reading IRV or Choose-One off
  it — as that file's divergence block is forced to — measures the score-to-rank
  tie-break rather than the method. These are the numbers to quote.""",
}

APPROVAL_STORY = {
    3: """  RUNG 1, counted by Approval — each bloc approves everyone it would have scored 4 or
  5 on the STAR ballot for this rung. Diego wins with 44 approvals of 65. Every method at
  this rung agrees.""",
    5: """  RUNG 2, counted by Approval. Diego again, 34 to Bruno's and Elsa's 29 — Approval is
  still with STAR, Score and Ranked Robin at five candidates, while RCV-IRV and
  Choose-One have already left.

  Standing caveat: Approval's answer is the most cutoff-dependent of the six methods on
  this ladder. Approve-at-3 and approve-at-4 are different elections, which is why there
  is no such thing as "Approval's result" without the rule attached.""",
    7: """  RUNG 3, counted by Approval. Felix wins on 36 while the Condorcet winner Diego takes
  22 — third from last, on the same fixed approve-at-4 rule that elected him at both
  earlier rungs.

  Diego's collapse is the crowded-field effect in a form all its own. He is nearly
  everyone's second or third choice, but a wider field pushes each bloc's approval line
  past him: the blocs at 12 and 16 now have Clara, Elsa or Felix sitting where Diego used
  to be on their ballot. Approval reads where you drew the line, not whom you preferred.

  Same caveat as rung 2, doubled — quote this column only with the cutoff attached.""",
}


# --- emitters ----------------------------------------------------------------
def _weighted_score_block(names, rows):
    lines = [f"  Count:{','.join(names)}"]
    for pos, n, row in zip(BLOCS, SIZES, rows):
        lines.append(f"  {n}:{','.join(str(int(x)) for x in row)}    # bloc at {pos}")
    return "\n".join(lines)


def _weighted_rank_block(names):
    return "\n".join(f"  {c}:{row}    # bloc at {p}"
                     for p, c, row in zip(BLOCS, SIZES, ranked_rows(names)))


def star_yaml(n):
    names = RUNGS[n]
    return f"""election_title: "Crowded field, rung {len(names)} — {len(names)} candidates, 65 voters, counted by STAR"

scenario_description: |-
{STAR_STORY[n]}

{CONSTRUCTION}

voting_method: STAR
num_winners: 1

lot_numbers: [{", ".join(names)}]

{OPTIONS_STAR}
ballots: |-
{_weighted_score_block(names, score_rows(names))}

expected_winners:
  - {WINNER[(n, 'star')]}
"""


def rr_yaml(n):
    names = RUNGS[n]
    return f"""election_title: "Crowded field, rung {len(names)} — {len(names)} candidates, 65 voters, counted by Ranked Robin"

scenario_description: |-
{RR_STORY[n]}

  Same 65 voters and the same fixed candidate positions as crowded_field_c{n}_star.yaml;
  this file hands them a ranked ballot instead of a 0–5 one.

{CONSTRUCTION}

voting_method: RankedRobin
num_winners: 1

lot_numbers: [{", ".join(names)}]

{OPTIONS_RR}
ballots: |-
{_weighted_rank_block(names)}

expected_winners:
  - {WINNER[(n, 'rr')]}
"""


def irv_yaml(n):
    names = RUNGS[n]
    return f"""election_title: "Crowded field, rung {len(names)} — {len(names)} candidates, 65 voters, counted by RCV-IRV"

scenario_description: |-
{IRV_STORY[n]}

  Same 65 voters and the same fixed candidate positions as crowded_field_c{n}_star.yaml,
  on a ranked ballot — the same ballots as crowded_field_c{n}_ranked_robin.yaml, counted by
  elimination instead of head-to-head.

{CONSTRUCTION}

voting_method: RCV_IRV
num_winners: 1

lot_numbers: [{", ".join(names)}]

{OPTIONS_PLAIN}
ballots: |-
{_weighted_rank_block(names)}

expected_winners:
  - {WINNER[(n, 'irv')]}
"""


def approval_yaml(n):
    names = RUNGS[n]
    return f"""election_title: "Crowded field, rung {len(names)} — {len(names)} candidates, 65 voters, counted by Approval"

scenario_description: |-
{APPROVAL_STORY[n]}

  Same 65 voters and the same fixed candidate positions as crowded_field_c{n}_star.yaml;
  the approval ballot is that file's 0–5 ballot thresholded at {APPROVAL_CUTOFF} (approve everyone you
  would score {APPROVAL_CUTOFF} or 5). Change the cutoff in build_ladder.py and this file changes with it.

{CONSTRUCTION}

voting_method: Approval
num_winners: 1

lot_numbers: [{", ".join(names)}]

{OPTIONS_PLAIN}
ballots: |-
{_weighted_score_block(names, approval_rows(names))}

expected_winners:
  - {WINNER[(n, 'approval')]}
"""


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true",
                    help="verify the committed YAMLs match this construction; write nothing")
    a = ap.parse_args()

    no_equidistance()
    out = HERE / "cases"
    out.mkdir(exist_ok=True)
    stale = []
    for n in RUNGS:
        for kind, text in (("star", star_yaml(n)), ("ranked_robin", rr_yaml(n)),
                           ("irv", irv_yaml(n)), ("approval", approval_yaml(n))):
            path = out / f"crowded_field_c{n}_{kind}.yaml"
            if a.check:
                if (path.read_text() if path.exists() else "") != text:
                    stale.append(path.relative_to(REPO))
            else:
                path.write_text(text)
                print(f"wrote {path.relative_to(REPO)}")
    if a.check:
        if stale:
            print("STALE — rerun without --check:")
            for p in stale:
                print(f"  {p}")
            return 1
        print(f"all {4 * len(RUNGS)} case files match the construction")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
