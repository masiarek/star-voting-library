# Reversal symmetry — STAR, original: B (STAR does not winner=loser here)

*Generated from [`reversal_star_original.yaml`](../reversal_star_original.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** B

## Scenario

The same 24-voter cycle scored 0-5 (rank->score 5/3/0). STAR elects B (scoring round B 69,
runoff 17-7). The companion reversal_star_reversed reverses every preference and STAR elects
A — a DIFFERENT winner, so STAR does not exhibit the winner=loser failure RCV-IRV shows on this
example (see ../README.md). Honest scope note: this shows STAR AVOIDS the failure on these
ballots; it is not a claim that STAR satisfies the reversal-symmetry criterion in general (STAR
is a hybrid — additive scoring round + pairwise runoff — and the rank->score mapping is a modeling
choice). The electorate is a Condorcet cycle, so no winner is "correct."

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:A,B,C
9:0,5,3
8:5,3,0
7:3,0,5
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR    = B
  RCV-IRV = A   (differs from STAR)
  Note: no ballots had tied scores, so RCV-IRV vs STAR here is a genuine
        method difference, not a tie-breaking artifact.
  Note: Ranked Robin (RCV-RR) agrees with STAR, so RCV-IRV is the lone
        outlier — the classic center-squeeze signature.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: cases_tabulated/reversal_star_original_RCV-IRV_tabulated.txt

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 24 ballots.
Count × A,B,C
    9 × 0,5,3
    8 × 5,3,0
    7 × 3,0,5

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   B             -- 69 -- First place
   C             -- 62 -- Second place
   A             -- 61
 B and C advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   B             -- 17 -- First place
   C             --  7
   Equal Support --  0
 B wins.
   Runoff math:
     24  ballots cast
   −  0  Equal Support (no preference between the two finalists)
     ──
     24  voters with a preference  (majority = 13)
           B 17 (71%)  ·  C 7 (29%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 B
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |       A      |    * B      |    * C      |
-------------------------------------------------------------
             A > |     ---      |15 -  0 -  9 | 8 -  0 - 16 |
           * B > |  9 -  0 - 15 |    ---      |17 -  0 -  7 |
           * C > | 16 -  0 -  8 | 7 -  0 - 17 |    ---      |

[Condorcet Winner]
  No Condorcet winner (majority cycle: A > B > C > A)

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
A          8  0  7  0  0  9  |    61   2.5
B          9  0  8  0  0  7  |    69   2.9
C          7  0  9  0  0  8  |    62   2.6
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/reversal_star_original_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/reversal_symmetry/cases/reversal_star_original.yaml
```

## See also

- [Methods disagree on this election](../../../divergence_review/cases/CYCLE_OR_THREE_WAY/reversal_star_original.md) — its entry in the divergence review ledger
- [Condorcet efficiency (topic hub)](../../../../00_start_here/topics/condorcet/README.md)
- [Runoff reversal (worked set)](../../../../01_STAR/runoff_overturns_leader/README.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [reversal_irv_original](reversal_irv_original.md) · [reversal_irv_reversed](reversal_irv_reversed.md) · [reversal_star_reversed](reversal_star_reversed.md)
