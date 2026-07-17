# Exercise 10 — Later-no-harm: the generous ballots

*Generated from [`ex10_generous.yaml`](../ex10_generous.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Bess

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/yyhj9x) · **[results ↗](https://bettervoting.com/yyhj9x/results)** (election `yyhj9x`).

## Scenario

The same nine voters as ex10_reticent.yaml, but Amir's four fans now
score honestly: Amir 5, Bess 3, Cato 0 — they genuinely like Bess
second. Those twelve extra points lift Bess from 13 to 25: scoring
round Bess 25, Amir 24, Cato 15 — and Bess beats Amir in the runoff
5-4. The fans' generosity cost their favorite the win: a LATER-NO-HARM
failure, live. The counter-reading: Bess is this electorate's Condorcet
winner (beats Amir 5-4, Cato 6-3) and is scored 1+ by all nine voters —
the reticent ballots didn't protect Amir so much as HIDE Bess. STAR
gives up later-no-harm on purpose: protecting favorites by hiding
compromises is exactly what it declines to reward. Exercise:
ex10_later_no_harm.md. Ballots and cast are this repo's own.
Live on BetterVoting (Test ID BV2196): https://bettervoting.com/yyhj9x/results
— with an RCV-IRV race (still Amir: IRV keeps later-no-harm precisely
by center-squeezing the Condorcet winner Bess).

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Amir,Bess,Cato
5,3,0 # 4 voters: Amir fans, honest about liking Bess second
5,3,0
5,3,0
5,3,0
2,5,0 # 2 voters: Bess first, mild nod to Amir — unchanged
2,5,0
0,1,5 # 3 voters: Cato first, a token point to Bess — unchanged
0,1,5
0,1,5
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR                   = Bess
  Choose-One (Plurality) = Amir   (differs from STAR)
  RCV-IRV                = Amir   (differs from STAR)
  Note: no ballots had tied scores, so RCV-IRV vs STAR here is a genuine
        method difference, not a tie-breaking artifact.
  Note: Ranked Robin (RCV-RR) agrees with STAR, so RCV-IRV is the lone
        outlier — the classic center-squeeze signature.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: exercises_tabulated/ex10_generous_RCV-IRV_tabulated.txt

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 9 ballots.
Count × Amir,Bess,Cato
    4 ×    5,   3,   0
    3 ×    0,   1,   5
    2 ×    2,   5,   0

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Bess          -- 25 -- First place
   Amir          -- 24 -- Second place
   Cato          -- 15
 Bess and Amir advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Bess          -- 5 -- First place
   Amir          -- 4
   Equal Support -- 0
 Bess wins.
   Runoff math:
     9  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     9  voters with a preference  (majority = 5)
           Bess 5 (56%)  ·  Amir 4 (44%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Bess
```

<details>
<summary>Full audit — preference matrix, Condorcet, and score distribution</summary>

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |   * Amir   |  * Bess   |    Cato   |
-----------------------------------------------------
      * Amir > |    ---     |4 - 0 - 5  |6 - 0 - 3  |
      * Bess > | 5 - 0 - 4  |   ---     |6 - 0 - 3  |
        Cato > | 3 - 0 - 6  |3 - 0 - 6  |   ---     |

[Condorcet Winner]
  Condorcet Winner: Bess — matches the STAR winner

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Amir       4  0  0  2  0  3  |    24   2.7
Bess       2  0  4  0  3  0  |    25   2.8
Cato       3  0  0  0  0  6  |    15   1.7
```

</details>

Everything in one file: the [`_tabulated` mirror](../exercises_tabulated/ex10_generous_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/exercises/ex10_generous.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Methods disagree on this election](../../../method_comparisons/divergence_review/cases/IRV_OUTLIER_RR_WITH_STAR/ex10_generous.md) — its entry in the divergence review ledger
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README.md)
- [Runoff reversal (worked set)](../../runoff_overturns_leader/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [ex01_district_combined](ex01_district_combined.md) · [ex01_district_east](ex01_district_east.md) · [ex01_district_west](ex01_district_west.md) · [ex02_bella_exits](ex02_bella_exits.md) · [ex02_nine_ballots](ex02_nine_ballots.md) · [ex02_tenth_ballot](ex02_tenth_ballot.md) · [ex03_five_verdicts](ex03_five_verdicts.md) · [ex04_olympics_1994](ex04_olympics_1994.md) · [ex05_center_squeeze](ex05_center_squeeze.md) · [ex06_bullet_backfire](ex06_bullet_backfire.md) · [ex06_bullet_honest](ex06_bullet_honest.md) · [ex07_vanishing_votes](ex07_vanishing_votes.md) · [ex08_minimal_reversal_2c](ex08_minimal_reversal_2c.md) · [ex08_minimal_reversal_3c](ex08_minimal_reversal_3c.md) · [ex09_game_night_cycle](ex09_game_night_cycle.md) · [ex10_reticent](ex10_reticent.md) · [ex11_spoiler_added](ex11_spoiler_added.md) · [ex11_two_way_base](ex11_two_way_base.md) · [ex12_bloc_sweep](ex12_bloc_sweep.md) · [ex12_proportional_share](ex12_proportional_share.md) · [ex13_approve3](ex13_approve3.md) · [ex13_approve4](ex13_approve4.md) · [ex13_bullet](ex13_bullet.md) · [ex13_opinions](ex13_opinions.md) · [ex14_two_novels](ex14_two_novels.md) · [ex14_two_novels_fullranks](ex14_two_novels_fullranks.md)
