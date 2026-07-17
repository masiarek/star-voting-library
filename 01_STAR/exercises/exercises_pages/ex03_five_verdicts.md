# Exercise 3 — One electorate, five verdicts (the snack vote)

*Generated from [`ex03_five_verdicts.yaml`](../ex03_five_verdicts.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Cherry

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/ywqhq4) · **[results ↗](https://bettervoting.com/ywqhq4/results)** (election `ywqhq4`).

## Scenario

Nine voters pick the office snack. Choose-One elects Apple (4 first
choices) — who loses head-to-head to BOTH rivals (the Condorcet loser).
RCV-IRV eliminates Cherry first (2 first choices) and elects Banana.
Approval (approve = score 3+) gives Cherry 9 of 9. Score gives Cherry 34
of a possible 45. STAR advances Cherry and Apple and Cherry wins the
runoff 5-4. And Ranked Robin confirms Cherry as the Condorcet winner.
One electorate, five different verdicts from five tabulations — the
ballot-vs-method lesson of the exercise ex03_five_verdicts.md. Structure
inspired by the worked comparisons in Brendan W. Sullivan, "An
Introduction to the Math of Voting Methods" (2022), ch. 5; ballots and
cast are this repo's own.
Live on BetterVoting (Test ID BV2191): https://bettervoting.com/ywqhq4/results
— one election, five races (Choose-One, RCV-IRV, Approval, STAR, Ranked
Robin), all five verdicts live; BV agrees with LH on every race.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Apple,Banana,Cherry
5,0,3 # 4 voters: Apple fans, Cherry a solid second
5,0,3
5,0,3
5,0,3
0,5,4 # 3 voters: Banana fans, Cherry nearly as good
0,5,4
0,5,4
0,1,5 # 2 voters: Cherry fans, cool on both others
0,1,5
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR                   = Cherry
  Choose-One (Plurality) = Apple   (differs from STAR)
  RCV-IRV                = Banana   (differs from STAR)
  Note: no ballots had tied scores, so RCV-IRV vs STAR here is a genuine
        method difference, not a tie-breaking artifact.
  Note: Ranked Robin (RCV-RR) agrees with STAR, so RCV-IRV is the lone
        outlier — the classic center-squeeze signature.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: exercises_tabulated/ex03_five_verdicts_RCV-IRV_tabulated.txt

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 9 ballots.
Count × Apple,Banana,Cherry
    4 ×     5,     0,     3
    3 ×     0,     5,     4
    2 ×     0,     1,     5

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Cherry        -- 34 -- First place
   Apple         -- 20 -- Second place
   Banana        -- 17
 Cherry and Apple advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Cherry        -- 5 -- First place
   Apple         -- 4
   Equal Support -- 0
 Cherry wins.
   Runoff math:
     9  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     9  voters with a preference  (majority = 5)
           Cherry 5 (56%)  ·  Apple 4 (44%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Cherry
```

<details>
<summary>Full audit — preference matrix, Condorcet, and score distribution</summary>

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |  * Apple   |   Banana  | * Cherry  |
-----------------------------------------------------
     * Apple > |    ---     |4 - 0 - 5  |4 - 0 - 5  |
      Banana > | 5 - 0 - 4  |   ---     |3 - 0 - 6  |
    * Cherry > | 5 - 0 - 4  |6 - 0 - 3  |   ---     |

[Condorcet Winner]
  Condorcet Winner: Cherry — matches the STAR winner

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Apple      4  0  0  0  0  5  |    20   2.2
Banana     3  0  0  0  2  4  |    17   1.9
Cherry     2  3  4  0  0  0  |    34   3.8
```

</details>

Everything in one file: the [`_tabulated` mirror](../exercises_tabulated/ex03_five_verdicts_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/exercises/ex03_five_verdicts.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Methods disagree on this election](../../../method_comparisons/divergence_review/cases/IRV_OUTLIER_RR_WITH_STAR/ex03_five_verdicts.md) — its entry in the divergence review ledger
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README.md)
- [Runoff reversal (worked set)](../../runoff_overturns_leader/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [ex01_district_combined](ex01_district_combined.md) · [ex01_district_east](ex01_district_east.md) · [ex01_district_west](ex01_district_west.md) · [ex02_bella_exits](ex02_bella_exits.md) · [ex02_nine_ballots](ex02_nine_ballots.md) · [ex02_tenth_ballot](ex02_tenth_ballot.md) · [ex04_olympics_1994](ex04_olympics_1994.md) · [ex05_center_squeeze](ex05_center_squeeze.md) · [ex06_bullet_backfire](ex06_bullet_backfire.md) · [ex06_bullet_honest](ex06_bullet_honest.md) · [ex07_vanishing_votes](ex07_vanishing_votes.md) · [ex08_minimal_reversal_2c](ex08_minimal_reversal_2c.md) · [ex08_minimal_reversal_3c](ex08_minimal_reversal_3c.md) · [ex09_game_night_cycle](ex09_game_night_cycle.md) · [ex10_generous](ex10_generous.md) · [ex10_reticent](ex10_reticent.md) · [ex11_spoiler_added](ex11_spoiler_added.md) · [ex11_two_way_base](ex11_two_way_base.md) · [ex12_bloc_sweep](ex12_bloc_sweep.md) · [ex12_proportional_share](ex12_proportional_share.md) · [ex13_approve3](ex13_approve3.md) · [ex13_approve4](ex13_approve4.md) · [ex13_bullet](ex13_bullet.md) · [ex13_opinions](ex13_opinions.md) · [ex14_two_novels](ex14_two_novels.md) · [ex14_two_novels_fullranks](ex14_two_novels_fullranks.md)
