# Exercise 2 — The tenth ballot: all ten ballots

*Generated from [`ex02_tenth_ballot.yaml`](../ex02_tenth_ballot.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Chris

## Scenario

The same nine ballots plus the forgotten tenth — a voter whose favorite is
Alex (5), with Chris at 2 and everyone else at 0. The ballot ADDS more to
Alex's total than to anyone else's, yet it flips the win away from Alex:
scoring round Alex 32, Chris 26, Bella 25, Eli 22, Dana 20 — the extra 2
points lift Chris past Bella into the runoff, and Chris beats Alex
head-to-head 6-4. STAR fails the PARTICIPATION criterion: casting an honest
ballot can occasionally hurt your favorite (here, by changing WHO Alex has
to face). Part of the exercise ex02_tenth_ballot.md. Ballots adapted from a
RangeVoting.org example, posed as an exercise in Brendan W. Sullivan,
"An Introduction to the Math of Voting Methods" (2022), ch. 5.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Alex,Bella,Chris,Dana,Eli
3,2,4,5,0 # 4 voters: Dana first, Chris close second
3,2,4,5,0
3,2,4,5,0
3,2,4,5,0
3,5,0,0,4 # 3 voters: Bella first, Eli second
3,5,0,0,4
3,5,0,0,4
3,1,4,0,5 # 2 voters: Eli first, Chris second
3,1,4,0,5
5,0,2,0,0 # the forgotten TENTH ballot: Alex is this voter's favorite
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR                   = Chris
  Choose-One (Plurality) = Dana   (differs from STAR)
  RCV-IRV                = Bella   (differs from STAR)
  Approval               = Alex   (differs from STAR)
  Note: no ballots had tied scores, so RCV-IRV vs STAR here is a genuine
        method difference, not a tie-breaking artifact.
  Note: Ranked Robin (RCV-RR) agrees with STAR, so RCV-IRV is the lone
        outlier — the classic center-squeeze signature.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: exercises_tabulated/ex02_tenth_ballot_RCV-IRV_tabulated.txt

[Runoff Reversal]
 - Score Round Winner(s) = (Alex)
 - Runoff Round Winner   = (Chris)
  Candidate Alex earned the highest total score, but
  Candidate Chris won the automatic runoff — not a malfunction,
  STAR working as designed: the runoff elects the finalist preferred
  by the majority (of voters with a preference).

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 10 ballots.
Count × Alex,Bella,Chris,Dana,Eli
    4 ×    3,    2,    4,   5,  0
    3 ×    3,    5,    0,   0,  4
    2 ×    3,    1,    4,   0,  5
    1 ×    5,    0,    2,   0,  0

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Alex          -- 32 -- First place
   Chris         -- 26 -- Second place
   Bella         -- 25
   Eli           -- 22
   Dana          -- 20
 Alex and Chris advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Chris         -- 6 -- First place
   Alex          -- 4
   Equal Support -- 0
 Chris wins.
   Runoff math:
     10  ballots cast
   −  0  Equal Support (no preference between the two finalists)
     ──
     10  voters with a preference  (majority = 6)
           Chris 6 (60%)  ·  Alex 4 (40%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Chris
```

<details>
<summary>Full audit — preference matrix, Condorcet, and score distribution</summary>

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |   * Alex   |   Bella   | * Chris   |    Dana   |    Eli    |
-----------------------------------------------------------------------------
      * Alex > |    ---     |7 - 0 - 3  |4 - 0 - 6  |6 - 0 - 4  |5 - 0 - 5  |
       Bella > | 3 - 0 - 7  |   ---     |3 - 0 - 7  |5 - 1 - 4  |7 - 1 - 2  |
     * Chris > | 6 - 0 - 4  |7 - 0 - 3  |   ---     |3 - 3 - 4  |5 - 0 - 5  |
        Dana > | 4 - 0 - 6  |4 - 1 - 5  |4 - 3 - 3  |   ---     |4 - 1 - 5  |
         Eli > | 5 - 0 - 5  |2 - 1 - 7  |5 - 0 - 5  |5 - 1 - 4  |   ---     |

[Condorcet Winner]
  No Condorcet winner (majority cycle: Alex > Bella > Dana > Chris > Alex)

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Alex       1  0  9  0  0  0  |    32   3.2
Bella      3  0  0  4  2  1  |    25   2.5
Chris      0  6  0  1  0  3  |    26   2.6
Dana       4  0  0  0  0  6  |    20   2.0
Eli        2  3  0  0  0  5  |    22   2.2
```

</details>

Everything in one file: the [`_tabulated` mirror](../exercises_tabulated/ex02_tenth_ballot_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/exercises/ex02_tenth_ballot.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Methods disagree on this election](../../../method_comparisons/divergence_review/cases/CYCLE_OR_THREE_WAY/ex02_tenth_ballot.md) — its entry in the divergence review ledger
- [Runoff reversal (worked set)](../../runoff_overturns_leader/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [ex01_district_combined](ex01_district_combined.md) · [ex01_district_east](ex01_district_east.md) · [ex01_district_west](ex01_district_west.md) · [ex02_bella_exits](ex02_bella_exits.md) · [ex02_nine_ballots](ex02_nine_ballots.md) · [ex03_five_verdicts](ex03_five_verdicts.md) · [ex04_olympics_1994](ex04_olympics_1994.md) · [ex05_center_squeeze](ex05_center_squeeze.md) · [ex06_bullet_backfire](ex06_bullet_backfire.md) · [ex06_bullet_honest](ex06_bullet_honest.md) · [ex07_vanishing_votes](ex07_vanishing_votes.md) · [ex08_minimal_reversal_2c](ex08_minimal_reversal_2c.md) · [ex08_minimal_reversal_3c](ex08_minimal_reversal_3c.md) · [ex09_game_night_cycle](ex09_game_night_cycle.md) · [ex10_generous](ex10_generous.md) · [ex10_reticent](ex10_reticent.md) · [ex11_spoiler_added](ex11_spoiler_added.md) · [ex11_two_way_base](ex11_two_way_base.md) · [ex12_bloc_sweep](ex12_bloc_sweep.md) · [ex12_proportional_share](ex12_proportional_share.md) · [ex13_approve3](ex13_approve3.md) · [ex13_approve4](ex13_approve4.md) · [ex13_bullet](ex13_bullet.md) · [ex13_opinions](ex13_opinions.md) · [ex14_two_novels](ex14_two_novels.md) · [ex14_two_novels_fullranks](ex14_two_novels_fullranks.md)
