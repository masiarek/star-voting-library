# Exercise 8 — a small runoff reversal (sample solution, three candidates)

*Generated from [`ex08_minimal_reversal_3c.yaml`](../ex08_minimal_reversal_3c.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** A

## Scenario

A second sample solution to the construction exercise
ex08_build_a_reversal.md, with a third candidate so the finalist
selection is non-trivial. Five voters: B leads the scoring round 22-15-2
on the strength of two maximal ballots plus three friendly 4s — but
those three 4-givers all score A higher, so A wins the automatic runoff
3-2. The recipe visible in the ballots: give the score leader BREADTH
(many mid-high scores) and the runoff winner DEPTH (a majority that
ranks them on top).

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
A,B,C
5,4,0 # three voters: A first, B a friendly 4
5,4,0
5,4,0
0,5,1 # two voters: B first, a token point to C
0,5,1
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR     = A
  Approval = B   (differs from STAR)

[Runoff Reversal]
 - Score Round Winner(s) = (B)
 - Runoff Round Winner   = (A)
  Candidate B earned the highest total score, but
  Candidate A won the automatic runoff — not a malfunction,
  STAR working as designed: the runoff elects the finalist preferred
  by the majority (of voters with a preference).

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 5 ballots.
Count × A,B,C
    3 × 5,4,0
    2 × 0,5,1

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   B             -- 22 -- First place
   A             -- 15 -- Second place
   C             --  2
 B and A advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   A             -- 3 -- First place
   B             -- 2
   Equal Support -- 0
 A wins.
   Runoff math:
     5  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     5  voters with a preference  (majority = 3)
           A 3 (60%)  ·  B 2 (40%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 A
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |    * A     |   * B     |     C     |
-----------------------------------------------------
         * A > |    ---     |3 - 0 - 2  |3 - 0 - 2  |
         * B > | 2 - 0 - 3  |   ---     |5 - 0 - 0  |
           C > | 2 - 0 - 3  |0 - 0 - 5  |   ---     |

[Condorcet Winner]
  Condorcet Winner: A — matches the STAR winner

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
A          3  0  0  0  0  2  |    15   3.0
B          2  3  0  0  0  0  |    22   4.4
C          0  0  0  0  2  3  |     2   0.4
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/ex08_minimal_reversal_3c_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/exercises/cases/ex08_minimal_reversal_3c.yaml
```

## See also

- [Methods disagree on this election](../../../../method_comparisons/divergence_review/cases/APPROVAL_OR_MINOR/ex08_minimal_reversal_3c.md) — its entry in the divergence review ledger
- [Runoff reversal (worked set)](../../../runoff_overturns_leader/README.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [ex01_district_combined](ex01_district_combined.md) · [ex01_district_east](ex01_district_east.md) · [ex01_district_west](ex01_district_west.md) · [ex02_bella_exits](ex02_bella_exits.md) · [ex02_nine_ballots](ex02_nine_ballots.md) · [ex02_tenth_ballot](ex02_tenth_ballot.md) · [ex03_five_verdicts](ex03_five_verdicts.md) · [ex04_olympics_1994](ex04_olympics_1994.md) · [ex05_center_squeeze](ex05_center_squeeze.md) · [ex06_bullet_backfire](ex06_bullet_backfire.md) · [ex06_bullet_honest](ex06_bullet_honest.md) · [ex07_vanishing_votes](ex07_vanishing_votes.md) · [ex08_minimal_reversal_2c](ex08_minimal_reversal_2c.md) · [ex09_game_night_cycle](ex09_game_night_cycle.md) · [ex10_generous](ex10_generous.md) · [ex10_reticent](ex10_reticent.md) · [ex11_spoiler_added](ex11_spoiler_added.md) · [ex11_two_way_base](ex11_two_way_base.md) · [ex12_bloc_sweep](ex12_bloc_sweep.md) · [ex12_proportional_share](ex12_proportional_share.md) · [ex13_approve3](ex13_approve3.md) · [ex13_approve4](ex13_approve4.md) · [ex13_bullet](ex13_bullet.md) · [ex13_opinions](ex13_opinions.md) · [ex14_two_novels](ex14_two_novels.md) · [ex14_two_novels_fullranks](ex14_two_novels_fullranks.md)
