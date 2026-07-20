# Exercise 2 — The tenth ballot: the nine counted ballots

*Generated from [`ex02_nine_ballots.yaml`](../ex02_nine_ballots.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Alex

## Scenario

The base case: nine club ballots, five candidates. Scoring round: Alex 27,
Bella 25, Chris 24, Eli 22, Dana 20 — Alex and Bella advance, and Alex wins
the runoff 6-3. The exercise (ex02_tenth_ballot.md) then perturbs this
election twice: a forgotten tenth ballot whose FAVORITE is Alex flips the
win to Chris (a participation failure), and Bella withdrawing flips it to
Chris too (a runoff-slot spoiler). Ballots adapted from a RangeVoting.org
example, posed as an exercise in Brendan W. Sullivan, "An Introduction to
the Math of Voting Methods" (2022), ch. 5.

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
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR                   = Alex
  Choose-One (Plurality) = Dana   (differs from STAR)
  RCV-IRV                = Bella   (differs from STAR)
  RCV-RR                 = Eli   (differs from STAR)
  Note: no ballots had tied scores, so RCV-IRV vs STAR here is a genuine
        method difference, not a tie-breaking artifact.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: cases_tabulated/ex02_nine_ballots_RCV-IRV_tabulated.txt
  RCV-RR round-robin: cases_tabulated/ex02_nine_ballots_RCV-RR_tabulated.txt

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 9 ballots.
Count × Alex,Bella,Chris,Dana,Eli
    4 ×    3,    2,    4,   5,  0
    3 ×    3,    5,    0,   0,  4
    2 ×    3,    1,    4,   0,  5

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Alex          -- 27 -- First place
   Bella         -- 25 -- Second place
   Chris         -- 24
   Eli           -- 22
   Dana          -- 20
 Alex and Bella advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Alex          -- 6 -- First place
   Bella         -- 3
   Equal Support -- 0
 Alex wins.
   Runoff math:
     9  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     9  voters with a preference  (majority = 5)
           Alex 6 (67%)  ·  Bella 3 (33%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Alex
```

<details>
<summary>Full audit — preference matrix, Condorcet, and score distribution</summary>

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |   * Alex   | * Bella   |   Chris   |    Dana   |    Eli    |
-----------------------------------------------------------------------------
      * Alex > |    ---     |6 - 0 - 3  |3 - 0 - 6  |5 - 0 - 4  |4 - 0 - 5  |
     * Bella > | 3 - 0 - 6  |   ---     |3 - 0 - 6  |5 - 0 - 4  |7 - 0 - 2  |
       Chris > | 6 - 0 - 3  |6 - 0 - 3  |   ---     |2 - 3 - 4  |4 - 0 - 5  |
        Dana > | 4 - 0 - 5  |4 - 0 - 5  |4 - 3 - 2  |   ---     |4 - 0 - 5  |
         Eli > | 5 - 0 - 4  |2 - 0 - 7  |5 - 0 - 4  |5 - 0 - 4  |   ---     |

[Condorcet Winner]
  No Condorcet winner (majority cycle: Alex > Bella > Dana > Chris > Alex)

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Alex       0  0  9  0  0  0  |    27   3.0
Bella      3  0  0  4  2  0  |    25   2.8
Chris      0  6  0  0  0  3  |    24   2.7
Dana       4  0  0  0  0  5  |    20   2.2
Eli        2  3  0  0  0  4  |    22   2.4
```

</details>

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/ex02_nine_ballots_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/exercises/cases/ex02_nine_ballots.yaml
```

## See also

- [Methods disagree on this election](../../../../method_comparisons/divergence_review/cases/CYCLE_OR_THREE_WAY/ex02_nine_ballots.md) — its entry in the divergence review ledger
- [Vote splitting (worked set)](../../../../method_comparisons/split_voting/README.md)
- [Runoff reversal (worked set)](../../../runoff_overturns_leader/README.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [ex01_district_combined](ex01_district_combined.md) · [ex01_district_east](ex01_district_east.md) · [ex01_district_west](ex01_district_west.md) · [ex02_bella_exits](ex02_bella_exits.md) · [ex02_tenth_ballot](ex02_tenth_ballot.md) · [ex03_five_verdicts](ex03_five_verdicts.md) · [ex04_olympics_1994](ex04_olympics_1994.md) · [ex05_center_squeeze](ex05_center_squeeze.md) · [ex06_bullet_backfire](ex06_bullet_backfire.md) · [ex06_bullet_honest](ex06_bullet_honest.md) · [ex07_vanishing_votes](ex07_vanishing_votes.md) · [ex08_minimal_reversal_2c](ex08_minimal_reversal_2c.md) · [ex08_minimal_reversal_3c](ex08_minimal_reversal_3c.md) · [ex09_game_night_cycle](ex09_game_night_cycle.md) · [ex10_generous](ex10_generous.md) · [ex10_reticent](ex10_reticent.md) · [ex11_spoiler_added](ex11_spoiler_added.md) · [ex11_two_way_base](ex11_two_way_base.md) · [ex12_bloc_sweep](ex12_bloc_sweep.md) · [ex12_proportional_share](ex12_proportional_share.md) · [ex13_approve3](ex13_approve3.md) · [ex13_approve4](ex13_approve4.md) · [ex13_bullet](ex13_bullet.md) · [ex13_opinions](ex13_opinions.md) · [ex14_two_novels](ex14_two_novels.md) · [ex14_two_novels_fullranks](ex14_two_novels_fullranks.md)
