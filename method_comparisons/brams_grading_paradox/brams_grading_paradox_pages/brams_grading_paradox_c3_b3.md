# Brams' grading paradox — the grade leader loses the runoff

*Generated from [`brams_grading_paradox_c3_b3.yaml`](../brams_grading_paradox_c3_b3.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Baker

## Scenario

Steven Brams' three-voter grading example (Brams & Potthoff, "The paradox
of grading systems," Public Choice 165, 2015), offered as a critique of
grading systems: the candidate with the best grade total (Adams, 6-5-4) is
not the head-to-head champion (Baker beats both rivals — the Condorcet
winner). Run under STAR, the example vindicates the automatic runoff
instead of indicting it: finalists Adams & Baker, and Baker takes the seat
2-1. Pure score summation (Score voting) elects Adams. The Approval reading
depends entirely on where the 0/1 line is drawn: the engine's any-non-zero
cut elects Adams, Brams' own top-grades cut elects Baker, and two other
reasonable cuts produce ties. Grades {0..3} as in the original slide.
LH-only for now (no BetterVoting election).

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Adams,Baker,Chen
3,0,0   # voter 1 — Adams gets the top grade, zeros for the rest
2,3,3   # voter 2 — Baker and Chen top grades, Adams a friendly 2
1,2,1   # voter 3 — Baker best, mild on Adams and Chen
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR     = Baker
  Approval = Adams   (differs from STAR)

[Runoff Reversal]
 - Score Round Winner(s) = (Adams)
 - Runoff Round Winner   = (Baker)
  Candidate Adams earned the highest total score, but
  Candidate Baker won the automatic runoff — not a malfunction,
  STAR working as designed: the runoff elects the finalist preferred
  by the majority (of voters with a preference).

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 3 ballots.
Adams,Baker,Chen
    3,    0,   0
    2,    3,   3
    1,    2,   1

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Adams         -- 6 -- First place
   Baker         -- 5 -- Second place
   Chen          -- 4
 Adams and Baker advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Baker         -- 2 -- First place
   Adams         -- 1
   Equal Support -- 0
 Baker wins.
   Runoff math:
     3  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     3  voters with a preference  (majority = 2)
           Baker 2 (67%)  ·  Adams 1 (33%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Baker
```

<details>
<summary>Full audit — preference matrix, Condorcet, and score distribution</summary>

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |  * Adams   | * Baker   |    Chen   |
-----------------------------------------------------
     * Adams > |    ---     |1 - 0 - 2  |1 - 1 - 1  |
     * Baker > | 2 - 0 - 1  |   ---     |1 - 2 - 0  |
        Chen > | 1 - 1 - 1  |0 - 2 - 1  |   ---     |

[Condorcet Winner]
  Condorcet Winner: Baker — matches the STAR winner

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Adams      0  0  1  1  1  0  |     6   2.0
Baker      0  0  1  1  0  1  |     5   1.7
Chen       0  0  1  0  1  1  |     4   1.3
```

</details>

Everything in one file: the [`_tabulated` mirror](../brams_grading_paradox_tabulated/brams_grading_paradox_c3_b3_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/brams_grading_paradox/brams_grading_paradox_c3_b3.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Methods disagree on this election](../../divergence_review/cases/APPROVAL_OR_MINOR/brams_grading_paradox_c3_b3.md) — its entry in the divergence review ledger
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README.md)
- [Ties & tie-breaking (topic hub)](../../../00_start_here/topics/ties/README.md)
- [Runoff reversal (worked set)](../../../01_STAR/runoff_overturns_leader/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [brams_ex3_two_candidates_c2_b5](brams_ex3_two_candidates_c2_b5.md) · [brams_ex6_three_winners_c3_b9](brams_ex6_three_winners_c3_b9.md)
