# Brams Example 3 — two candidates: two loud fans vs three mild preferences

*Generated from [`brams_ex3_two_candidates_c2_b5.yaml`](../brams_ex3_two_candidates_c2_b5.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Beth

## Scenario

Example 3 of Brams & Potthoff, "The paradox of grading systems" (Public
Choice 165, 2015): the strong paradox needs only TWO candidates. Grades
{0..2}, five voters: two grade (Alan 2, Beth 0), three grade (Alan 0,
Beth 1). Alan wins the grade totals 4-3 on the strength of two maximal
fans, but three of the five voters grade Beth higher — the purest
"strength of support vs number of supporters" collision, with no
finalist-selection step to muddy it. STAR's automatic runoff is the
whole story at two candidates: Beth wins it 3-2. Pure score summation
elects Alan.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Alan,Beth
2,0   # two voters — all-in for Alan
2,0
0,1   # three voters — mildly prefer Beth
0,1
0,1
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR     = Beth
  Approval = Alan   (differs from STAR)

[Runoff Reversal]
 - Score Round Winner(s) = (Alan)
 - Runoff Round Winner   = (Beth)
  Candidate Alan earned the highest total score, but
  Candidate Beth won the automatic runoff — not a malfunction,
  STAR working as designed: the runoff elects the finalist preferred
  by the majority (of voters with a preference).

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 5 ballots.
Count × Alan,Beth
    3 ×    0,   1
    2 ×    2,   0

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Alan          -- 4 -- First place
   Beth          -- 3 -- Second place
 Alan and Beth advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Beth          -- 3 -- First place
   Alan          -- 2
   Equal Support -- 0
 Beth wins.
   Runoff math:
     5  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     5  voters with a preference  (majority = 3)
           Beth 3 (60%)  ·  Alan 2 (40%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Beth
```

<details>
<summary>Full audit — preference matrix, Condorcet, and score distribution</summary>

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |   * Alan   |  * Beth   |
-----------------------------------------
      * Alan > |    ---     |2 - 0 - 3  |
      * Beth > | 3 - 0 - 2  |   ---     |

[Condorcet Winner]
  Condorcet Winner: Beth — matches the STAR winner

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Alan       0  0  0  2  0  3  |     4   0.8
Beth       0  0  0  0  3  2  |     3   0.6
```

</details>

Everything in one file: the [`_tabulated` mirror](../brams_grading_paradox_tabulated/brams_ex3_two_candidates_c2_b5_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/brams_grading_paradox/brams_ex3_two_candidates_c2_b5.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Runoff reversal (worked set)](../../../01_STAR/runoff_overturns_leader/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [brams_ex6_three_winners_c3_b9](brams_ex6_three_winners_c3_b9.md) · [brams_grading_paradox_c3_b3](brams_grading_paradox_c3_b3.md)
