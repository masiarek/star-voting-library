# BV126 — ties at every step (single-winner STAR); #1052

*Generated from [`bv126_ties_every_step_8fvd2x.yaml`](../bv126_ties_every_step_8fvd2x.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Amy

**Official tie-break (lot) order:** Amy > Chuck > Brian — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

The LH reference for BetterVoting test BV126 ("ties every time — every step",
real election 8fvd2x). Single-winner STAR, 3 candidates, 7 ballots — five of
them flat 5,5,5. This is the worst case for the tie-break ladder: Amy, Brian and
Chuck tie at EVERY step.

Totals 29-29-29 (a three-way scoring tie); pairwise 2-2-2 (the two non-flat
ballots split evenly, the five flat ones are Equal Support); five-star 5-5-5.
Every deterministic rung ties, so the LOT picks the two finalists (Amy, Chuck);
the runoff ties too and the lot picks Amy. Lot [Amy, Chuck, Brian] reproduces
BetterVoting's drawn result.

Two BV issues surface together:
  1. #1052 — flat ballots dropped: the export reports nAbstentions=5,
     nTallyVotes=2 (only the two non-flat ballots), which is why BV shows a wrong
     count / "no ballots" style message. LH counts all 7 (Equal Support = 5).
  2. Random tie-break -> non-reproducible (cf. #1063 / #1417 / jfk7pd): BV drew
     Amy; a different draw elects Brian or Chuck. The winner is unaffected by the
     dropped flats (flat ballots never change a STAR result) — it's the lot order
     that decides.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Amy,Brian,Chuck
3,2,1
5,5,5
5,5,5
1,2,3
5,5,5
5,5,5
5,5,5
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 7 ballots.
Count × Amy,Brian,Chuck
    5 ×   5,    5,    5
    1 ×   3,    2,    1
    1 ×   1,    2,    3

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Amy           -- 29 -- Tied for first place
   Brian         -- 29 -- Tied for first place
   Chuck         -- 29 -- Tied for first place
 There's a three-way tie for first.

[STAR Voting: Scoring Round: First tiebreaker]
 The two candidates preferred in the most head-to-head matchups advance.
   Amy           -- 2 -- Tied for first place
   Brian         -- 2 -- Tied for first place
   Chuck         -- 2 -- Tied for first place
   Equal Support -- 5
 There's still a three-way tie for first.

[STAR Voting: Scoring Round: Second tiebreaker]
 The two candidates with the most votes of score 5 advance.
   Amy           -- 5 -- Tied for first place
   Brian         -- 5 -- Tied for first place
   Chuck         -- 5 -- Tied for first place
 There's still a three-way tie for first.

*(Ties are resolved by choosing the tied candidate with the highest-priority official lot number.)*
    Lot-number priority order: ['Amy', 'Chuck', 'Brian']

[Tiebreaker: Lot Number Priority]
  Tie among: ['Amy', 'Brian', 'Chuck']
  Resolved: ['Amy', 'Chuck'] (selected by lot-number priority).

[Lot-decided tie — rare]
  ⚠ The ballots did not break this tie: the deterministic rungs
    (pairwise / score, then five-star) all came back equal, so the
    pre-published LOT order chose among the tied candidates — the
    result here was set by lot, not by the votes. Usually the
    "dead rung": no tied candidate held a score-5 vote (five-star
    counts fives, not fours). Verify the tied candidates' 5-counts.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Amy           -- 1 -- Tied for first place
   Chuck         -- 1 -- Tied for first place
   Equal Support -- 5
 There's a two-way tie for first.

[STAR Voting: Automatic Runoff Round: First tiebreaker]
 The highest-scoring candidate wins.
   Amy           -- 29 -- Tied for first place
   Chuck         -- 29 -- Tied for first place
 There's still a two-way tie for first.

[STAR Voting: Automatic Runoff Round: Second tiebreaker]
 The candidate with the most votes of score 5 wins.
   Amy           -- 5 -- Tied for first place
   Chuck         -- 5 -- Tied for first place
 There's still a two-way tie for first.

[Tiebreaker: Lot Number Priority]
  Tie among: ['Amy', 'Chuck']
  Resolved: ['Amy'] (selected by lot-number priority).

[Lot-decided tie — rare]
  ⚠ The ballots did not break this tie: the deterministic rungs
    (pairwise / score, then five-star) all came back equal, so the
    pre-published LOT order chose among the tied candidates — the
    result here was set by lot, not by the votes. Usually the
    "dead rung": no tied candidate held a score-5 vote (five-star
    counts fives, not fours). Verify the tied candidates' 5-counts.

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Amy
```

<details>
<summary>Full audit — preference matrix, Condorcet, and score distribution</summary>

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |   * Amy    |   Brian   | * Chuck   |
-----------------------------------------------------
       * Amy > |    ---     |1 - 5 - 1  |1 - 5 - 1  |
       Brian > | 1 - 5 - 1  |   ---     |1 - 5 - 1  |
     * Chuck > | 1 - 5 - 1  |1 - 5 - 1  |   ---     |

[Condorcet Winner]
  No strict Condorcet winner; unbeaten candidates: Amy, Brian, Chuck (pairwise ties)

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Amy        5  0  1  0  1  0  |    29   4.1
Brian      5  0  0  2  0  0  |    29   4.1
Chuck      5  0  1  0  1  0  |    29   4.1
```

</details>

Everything in one file: the [`_tabulated` mirror](../tie_break_dead_rung_tabulated/bv126_ties_every_step_8fvd2x_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/tie_break_dead_rung/bv126_ties_every_step_8fvd2x.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Ties & tie-breaking (topic hub)](../../../00_start_here/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)
- [Vote splitting (worked set)](../../../method_comparisons/split_voting/README.md)
- [Runoff reversal (worked set)](../../runoff_overturns_leader/README.md)
- [Ballot & terminology basics](../../../00_start_here/topics/ballot_and_terminology_basics.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [dead_rung_scoring_dead_cap2](dead_rung_scoring_dead_cap2.md) · [dead_rung_scoring_dead_cap3](dead_rung_scoring_dead_cap3.md) · [dead_rung_scoring_dead_cap4](dead_rung_scoring_dead_cap4.md) · [tie_break_01_scoring_five_star_breaks](tie_break_01_scoring_five_star_breaks.md) · [tie_break_02_scoring_no_fives_to_lot](tie_break_02_scoring_no_fives_to_lot.md) · [tie_break_03_runoff_no_fives_to_lot](tie_break_03_runoff_no_fives_to_lot.md) · [tie_break_04_runoff_five_star_breaks](tie_break_04_runoff_five_star_breaks.md) · [tie_break_05_scoring_five_star_vs_adversarial_lot](tie_break_05_scoring_five_star_vs_adversarial_lot.md) · [tie_break_06_scoring_dead_rung_adversarial_lot](tie_break_06_scoring_dead_rung_adversarial_lot.md) · [tie_break_07_runoff_five_star_vs_adversarial_lot](tie_break_07_runoff_five_star_vs_adversarial_lot.md) · [tie_break_08_runoff_dead_rung_adversarial_lot](tie_break_08_runoff_dead_rung_adversarial_lot.md) · [tie_break_09_five_star_tied_nonzero](tie_break_09_five_star_tied_nonzero.md)
