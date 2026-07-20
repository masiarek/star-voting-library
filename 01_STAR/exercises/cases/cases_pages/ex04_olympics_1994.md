# Exercise 4 — Lillehammer 1994: nine judges, three skaters, two winners

*Generated from [`ex04_olympics_1994.yaml`](../ex04_olympics_1994.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Baiul

## Scenario

The real final ordinals of the 1994 Winter Olympics ladies figure
skating: nine judges ranked Oksana Baiul, Nancy Kerrigan, and Chen Lu —
five judges put Baiul first (Kerrigan second), four put Kerrigan first;
Lu is ranked third by seven judges and second by two. Ranks are mapped
to 0-5 scores with the repo's standard order-preserving map (top=5,
mid=3, bottom=1). Scoring round: Kerrigan 35, Baiul 33, Lu 13 — KERRIGAN
leads the scores. Automatic runoff: five of the nine judges prefer
Baiul, so BAIUL wins 5-4 — matching the real 5-4 judging split that
decided the gold medal. Score voting and STAR genuinely diverge on real
data; and Chen Lu can never win under ANY honest scoring, because every
single judge ranks Kerrigan above her (Pareto dominance). The exercise
is ex04_olympics_1994.md. Ordinals as reproduced in Brendan W. Sullivan,
"An Introduction to the Math of Voting Methods" (2022), ch. 5.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Baiul,Kerrigan,Lu
5,3,1 # judges 1-5: Baiul > Kerrigan > Lu
5,3,1
5,3,1
5,3,1
5,3,1
3,5,1 # judges 6-7: Kerrigan > Baiul > Lu
3,5,1
1,5,3 # judges 8-9: Kerrigan > Lu > Baiul
1,5,3
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR     = Baiul
  Approval = Kerrigan   (differs from STAR)

[Runoff Reversal]
 - Score Round Winner(s) = (Kerrigan)
 - Runoff Round Winner   = (Baiul)
  Candidate Kerrigan earned the highest total score, but
  Candidate Baiul won the automatic runoff — not a malfunction,
  STAR working as designed: the runoff elects the finalist preferred
  by the majority (of voters with a preference).

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 9 ballots.
Count × Baiul,Kerrigan,Lu
    5 ×     5,       3, 1
    2 ×     3,       5, 1
    2 ×     1,       5, 3

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Kerrigan      -- 35 -- First place
   Baiul         -- 33 -- Second place
   Lu            -- 13
 Kerrigan and Baiul advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Baiul         -- 5 -- First place
   Kerrigan      -- 4
   Equal Support -- 0
 Baiul wins.
   Runoff math:
     9  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     9  voters with a preference  (majority = 5)
           Baiul 5 (56%)  ·  Kerrigan 4 (44%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Baiul
```

<details>
<summary>Full audit — preference matrix, Condorcet, and score distribution</summary>

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |   * Baiul    | * Kerrigan  |      Lu     |
-------------------------------------------------------------
       * Baiul > |     ---      | 5 - 0 - 4   | 7 - 0 - 2   |
    * Kerrigan > |  4 - 0 - 5   |    ---      | 9 - 0 - 0   |
            Lu > |  2 - 0 - 7   | 0 - 0 - 9   |    ---      |

[Condorcet Winner]
  Condorcet Winner: Baiul — matches the STAR winner

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Baiul      5  0  2  0  2  0  |    33   3.7
Kerrigan   4  0  5  0  0  0  |    35   3.9
Lu         0  0  2  0  7  0  |    13   1.4
```

</details>

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/ex04_olympics_1994_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/exercises/cases/ex04_olympics_1994.yaml
```

## See also

- [Methods disagree on this election](../../../../method_comparisons/divergence_review/cases/APPROVAL_OR_MINOR/ex04_olympics_1994.md) — its entry in the divergence review ledger
- [Vote splitting (worked set)](../../../../method_comparisons/split_voting/README.md)
- [Runoff reversal (worked set)](../../../runoff_overturns_leader/README.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [ex01_district_combined](ex01_district_combined.md) · [ex01_district_east](ex01_district_east.md) · [ex01_district_west](ex01_district_west.md) · [ex02_bella_exits](ex02_bella_exits.md) · [ex02_nine_ballots](ex02_nine_ballots.md) · [ex02_tenth_ballot](ex02_tenth_ballot.md) · [ex03_five_verdicts](ex03_five_verdicts.md) · [ex05_center_squeeze](ex05_center_squeeze.md) · [ex06_bullet_backfire](ex06_bullet_backfire.md) · [ex06_bullet_honest](ex06_bullet_honest.md) · [ex07_vanishing_votes](ex07_vanishing_votes.md) · [ex08_minimal_reversal_2c](ex08_minimal_reversal_2c.md) · [ex08_minimal_reversal_3c](ex08_minimal_reversal_3c.md) · [ex09_game_night_cycle](ex09_game_night_cycle.md) · [ex10_generous](ex10_generous.md) · [ex10_reticent](ex10_reticent.md) · [ex11_spoiler_added](ex11_spoiler_added.md) · [ex11_two_way_base](ex11_two_way_base.md) · [ex12_bloc_sweep](ex12_bloc_sweep.md) · [ex12_proportional_share](ex12_proportional_share.md) · [ex13_approve3](ex13_approve3.md) · [ex13_approve4](ex13_approve4.md) · [ex13_bullet](ex13_bullet.md) · [ex13_opinions](ex13_opinions.md) · [ex14_two_novels](ex14_two_novels.md) · [ex14_two_novels_fullranks](ex14_two_novels_fullranks.md)
