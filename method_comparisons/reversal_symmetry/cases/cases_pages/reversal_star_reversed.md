# Reversal symmetry — STAR, reversed: A (differs from original B — no winner=loser)

*Generated from [`reversal_star_reversed.yaml`](../reversal_star_reversed.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** A

## Scenario

The STAR original (reversal_star_original) with every preference reversed (scores re-mapped
5/3/0 to the reversed ranking). STAR elects A — different from the original winner B — so unlike
RCV-IRV (which elects A both ways), STAR's "best" and "worst" here are not the same candidate.
Scope note per ../README.md: this demonstrates STAR avoiding the winner=loser on this example,
not a general reversal-symmetry proof. Condorcet cycle electorate.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:A,B,C
9:5,0,3
8:0,3,5
7:3,5,0
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR     = A
  Approval = C   (differs from STAR)

[Runoff Reversal]
 - Score Round Winner(s) = (C)
 - Runoff Round Winner   = (A)
  Candidate C earned the highest total score, but
  Candidate A won the automatic runoff — not a malfunction,
  STAR working as designed: the runoff elects the finalist preferred
  by the majority (of voters with a preference).

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 24 ballots.
Count × A,B,C
    9 × 5,0,3
    8 × 0,3,5
    7 × 3,5,0

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   C             -- 67 -- First place
   A             -- 66 -- Second place
   B             -- 59
 C and A advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   A             -- 16 -- First place
   C             --  8
   Equal Support --  0
 A wins.
   Runoff math:
     24  ballots cast
   −  0  Equal Support (no preference between the two finalists)
     ──
     24  voters with a preference  (majority = 13)
           A 16 (67%)  ·  C 8 (33%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 A
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |     * A      |      B      |    * C      |
-------------------------------------------------------------
           * A > |     ---      | 9 -  0 - 15 |16 -  0 -  8 |
             B > | 15 -  0 -  9 |    ---      | 7 -  0 - 17 |
           * C > |  8 -  0 - 16 |17 -  0 -  7 |    ---      |

[Condorcet Winner]
  No Condorcet winner (majority cycle: A > C > B > A)

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
A          9  0  7  0  0  8  |    66   2.8
B          7  0  8  0  0  9  |    59   2.5
C          8  0  9  0  0  7  |    67   2.8
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/reversal_star_reversed_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/reversal_symmetry/cases/reversal_star_reversed.yaml
```

## See also

- [Methods disagree on this election](../../../divergence_review/cases/APPROVAL_OR_MINOR/reversal_star_reversed.md) — its entry in the divergence review ledger
- [Condorcet efficiency (topic hub)](../../../../00_start_here/topics/condorcet/README.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [reversal_irv_original](reversal_irv_original.md) · [reversal_irv_reversed](reversal_irv_reversed.md) · [reversal_star_original](reversal_star_original.md)
