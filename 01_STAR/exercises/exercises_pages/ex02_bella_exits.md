# Exercise 2 — The tenth ballot: Bella withdraws

*Generated from [`ex02_bella_exits.yaml`](../ex02_bella_exits.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Chris

## Scenario

The original nine ballots with Bella's column removed — she withdrew before
the count, and no scores change for anyone else. Scoring round: Alex 27,
Chris 24, Eli 22, Dana 20 — with Bella gone, Chris takes her runoff slot and
beats Alex head-to-head 6-3. A candidate who was NOT going to win still
changed who does (a runoff-slot spoiler, the independence-of-irrelevant-
alternatives family): Bella's presence was what kept Chris out of the
runoff. Part of the exercise ex02_tenth_ballot.md. Ballots adapted from a
RangeVoting.org example, posed as an exercise in Brendan W. Sullivan,
"An Introduction to the Math of Voting Methods" (2022), ch. 5.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Alex,Chris,Dana,Eli
3,4,5,0 # 4 voters: Dana first, Chris close second
3,4,5,0
3,4,5,0
3,4,5,0
3,0,0,4 # 3 voters: (Bella was their favorite) Eli second
3,0,0,4
3,0,0,4
3,4,0,5 # 2 voters: Eli first, Chris second
3,4,0,5
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR                   = Chris
  Choose-One (Plurality) = Eli   (differs from STAR)
  RCV-IRV                = Eli   (differs from STAR)
  Approval               = Alex   (differs from STAR)
  RCV-RR (Condorcet)     = Eli   (differs from STAR)
  Note: no ballots had tied scores, so RCV-IRV vs STAR here is a genuine
        method difference, not a tie-breaking artifact.
  Note: Ranked Robin (RCV-RR) sides with RCV-IRV, so STAR is the outlier
        here — STAR need not elect the Condorcet candidate.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: exercises_tabulated/ex02_bella_exits_RCV-IRV_tabulated.txt
  RCV-RR round-robin: exercises_tabulated/ex02_bella_exits_RCV-RR_tabulated.txt

[Runoff Reversal]
 - Score Round Winner(s) = (Alex)
 - Runoff Round Winner   = (Chris)
  Candidate Alex earned the highest total score, but
  Candidate Chris won the automatic runoff — not a malfunction,
  STAR working as designed: the runoff elects the finalist preferred
  by the majority (of voters with a preference).

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 9 ballots.
Count × Alex,Chris,Dana,Eli
    4 ×    3,    4,   5,  0
    3 ×    3,    0,   0,  4
    2 ×    3,    4,   0,  5

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Alex          -- 27 -- First place
   Chris         -- 24 -- Second place
   Eli           -- 22
   Dana          -- 20
 Alex and Chris advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Chris         -- 6 -- First place
   Alex          -- 3
   Equal Support -- 0
 Chris wins.
   Runoff math:
     9  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     9  voters with a preference  (majority = 5)
           Chris 6 (67%)  ·  Alex 3 (33%)

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
               |   * Alex   | * Chris   |    Dana   |    Eli    |
-----------------------------------------------------------------
      * Alex > |    ---     |3 - 0 - 6  |5 - 0 - 4  |4 - 0 - 5  |
     * Chris > | 6 - 0 - 3  |   ---     |2 - 3 - 4  |4 - 0 - 5  |
        Dana > | 4 - 0 - 5  |4 - 3 - 2  |   ---     |4 - 0 - 5  |
         Eli > | 5 - 0 - 4  |5 - 0 - 4  |5 - 0 - 4  |   ---     |

[Condorcet Winner]
  Condorcet Winner: Eli — STAR elected Chris instead (Eli was eliminated in the scoring round)

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Alex       0  0  9  0  0  0  |    27   3.0
Chris      0  6  0  0  0  3  |    24   2.7
Dana       4  0  0  0  0  5  |    20   2.2
Eli        2  3  0  0  0  4  |    22   2.4
```

</details>

Everything in one file: the [`_tabulated` mirror](../exercises_tabulated/ex02_bella_exits_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/exercises/ex02_bella_exits.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Methods disagree on this election](../../../method_comparisons/divergence_review/cases/STAR_OUTLIER_RR_WITH_IRV/ex02_bella_exits.md) — its entry in the divergence review ledger
- [Vote splitting (worked set)](../../../method_comparisons/split_voting/README.md)
- [Runoff reversal (worked set)](../../runoff_overturns_leader/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [ex01_district_combined](ex01_district_combined.md) · [ex01_district_east](ex01_district_east.md) · [ex01_district_west](ex01_district_west.md) · [ex02_nine_ballots](ex02_nine_ballots.md) · [ex02_tenth_ballot](ex02_tenth_ballot.md) · [ex03_five_verdicts](ex03_five_verdicts.md) · [ex04_olympics_1994](ex04_olympics_1994.md) · [ex05_center_squeeze](ex05_center_squeeze.md) · [ex06_bullet_backfire](ex06_bullet_backfire.md) · [ex06_bullet_honest](ex06_bullet_honest.md) · [ex07_vanishing_votes](ex07_vanishing_votes.md) · [ex08_minimal_reversal_2c](ex08_minimal_reversal_2c.md) · [ex08_minimal_reversal_3c](ex08_minimal_reversal_3c.md) · [ex09_game_night_cycle](ex09_game_night_cycle.md) · [ex10_generous](ex10_generous.md) · [ex10_reticent](ex10_reticent.md) · [ex11_spoiler_added](ex11_spoiler_added.md) · [ex11_two_way_base](ex11_two_way_base.md) · [ex12_bloc_sweep](ex12_bloc_sweep.md) · [ex12_proportional_share](ex12_proportional_share.md) · [ex13_approve3](ex13_approve3.md) · [ex13_approve4](ex13_approve4.md) · [ex13_bullet](ex13_bullet.md) · [ex13_opinions](ex13_opinions.md) · [ex14_two_novels](ex14_two_novels.md) · [ex14_two_novels_fullranks](ex14_two_novels_fullranks.md)
