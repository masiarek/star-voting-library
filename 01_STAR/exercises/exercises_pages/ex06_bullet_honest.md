# Exercise 6 — Bullet voting backfires: the honest ballots

*Generated from [`ex06_bullet_honest.yaml`](../ex06_bullet_honest.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Bree

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/x4dkfd) · **[results ↗](https://bettervoting.com/x4dkfd/results)** (election `x4dkfd`).

## Scenario

The base case: nine voters, three speakers. Ari's four fans vote
honestly (Ari 5, Bree 3, Cash 0). Scoring round: Bree 25, Cash 21,
Ari 20 — Bree and Cash advance, and Bree (the broad compromise) beats
Cash 5-4 in the runoff. Ari's fans get their second choice. The
companion file ex06_bullet_backfire.yaml reruns the SAME election with
those four fans bullet voting (Ari 5, everyone else 0) — and hands the
win to Cash, their nightmare. Exercise: ex06_bullet_backfire.md.
Ballots and cast are this repo's own.
Live on BetterVoting (Test ID BV2193): https://bettervoting.com/x4dkfd/results
— with RCV-IRV and Ranked Robin races on the same opinions (IRV elects
Cash even on the honest ballots — the squeeze cameo; RR confirms Bree).

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Ari,Bree,Cash
5,3,0 # 4 voters: Ari fans, honest about liking Bree too
5,3,0
5,3,0
5,3,0
0,2,5 # 4 voters: Cash fans, Bree tolerable
0,2,5
0,2,5
0,2,5
0,5,1 # 1 voter: Bree all the way
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR                   = Bree
  Choose-One (Plurality) = Ari   (differs from STAR)
  RCV-IRV                = Cash   (differs from STAR)
  Note: no ballots had tied scores, so RCV-IRV vs STAR here is a genuine
        method difference, not a tie-breaking artifact.
  Note: Ranked Robin (RCV-RR) agrees with STAR, so RCV-IRV is the lone
        outlier — the classic center-squeeze signature.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: exercises_tabulated/ex06_bullet_honest_RCV-IRV_tabulated.txt

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 9 ballots.
Count × Ari,Bree,Cash
    4 ×   5,   3,   0
    4 ×   0,   2,   5
    1 ×   0,   5,   1

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Bree          -- 25 -- First place
   Cash          -- 21 -- Second place
   Ari           -- 20
 Bree and Cash advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Bree          -- 5 -- First place
   Cash          -- 4
   Equal Support -- 0
 Bree wins.
   Runoff math:
     9  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     9  voters with a preference  (majority = 5)
           Bree 5 (56%)  ·  Cash 4 (44%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Bree
```

<details>
<summary>Full audit — preference matrix, Condorcet, and score distribution</summary>

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |     Ari    |  * Bree   |  * Cash   |
-----------------------------------------------------
         Ari > |    ---     |4 - 0 - 5  |4 - 0 - 5  |
      * Bree > | 5 - 0 - 4  |   ---     |5 - 0 - 4  |
      * Cash > | 5 - 0 - 4  |4 - 0 - 5  |   ---     |

[Condorcet Winner]
  Condorcet Winner: Bree — matches the STAR winner

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Ari        4  0  0  0  0  5  |    20   2.2
Bree       1  0  4  4  0  0  |    25   2.8
Cash       4  0  0  0  1  4  |    21   2.3
```

</details>

Everything in one file: the [`_tabulated` mirror](../exercises_tabulated/ex06_bullet_honest_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/exercises/ex06_bullet_honest.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Methods disagree on this election](../../../method_comparisons/divergence_review/cases/IRV_OUTLIER_RR_WITH_STAR/ex06_bullet_honest.md) — its entry in the divergence review ledger
- [Runoff reversal (worked set)](../../runoff_overturns_leader/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [ex01_district_combined](ex01_district_combined.md) · [ex01_district_east](ex01_district_east.md) · [ex01_district_west](ex01_district_west.md) · [ex02_bella_exits](ex02_bella_exits.md) · [ex02_nine_ballots](ex02_nine_ballots.md) · [ex02_tenth_ballot](ex02_tenth_ballot.md) · [ex03_five_verdicts](ex03_five_verdicts.md) · [ex04_olympics_1994](ex04_olympics_1994.md) · [ex05_center_squeeze](ex05_center_squeeze.md) · [ex06_bullet_backfire](ex06_bullet_backfire.md) · [ex07_vanishing_votes](ex07_vanishing_votes.md) · [ex08_minimal_reversal_2c](ex08_minimal_reversal_2c.md) · [ex08_minimal_reversal_3c](ex08_minimal_reversal_3c.md) · [ex09_game_night_cycle](ex09_game_night_cycle.md) · [ex10_generous](ex10_generous.md) · [ex10_reticent](ex10_reticent.md) · [ex11_spoiler_added](ex11_spoiler_added.md) · [ex11_two_way_base](ex11_two_way_base.md) · [ex12_bloc_sweep](ex12_bloc_sweep.md) · [ex12_proportional_share](ex12_proportional_share.md) · [ex13_approve3](ex13_approve3.md) · [ex13_approve4](ex13_approve4.md) · [ex13_bullet](ex13_bullet.md) · [ex13_opinions](ex13_opinions.md) · [ex14_two_novels](ex14_two_novels.md) · [ex14_two_novels_fullranks](ex14_two_novels_fullranks.md)
