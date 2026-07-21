# STAR vs Ranked Robin divergence — cycle_09_c3_v21 (STAR A, RR B)

*Generated from [`cycle_09_c3_v21.yaml`](../cycle_09_c3_v21.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** A

## Scenario

Auto-generated STAR-vs-Ranked-Robin divergence sample (cycle). 3 candidates, 21 voters, noise model. STAR elects A; Ranked Robin elects B; no Condorcet winner (cycle). See the [Divergence from STAR] block below for RCV-IRV, Approval and Plurality on the same ballots.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:A,B,C
1:0,5,3
1:0,5,5
1:0,5,4
1:3,5,0
1:4,5,0
1:4,5,0
1:0,4,5
1:5,0,3
1:2,0,5
1:4,0,5
1:5,5,0
1:5,0,0
1:0,4,5
1:5,0,4
1:4,0,5
1:0,5,5
1:0,1,5
1:5,0,0
1:2,5,0
1:5,0,3
1:5,2,0
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR                   = A
  Choose-One (Plurality) = B   (differs from STAR)
  RCV-IRV                = B   (differs from STAR)
  Approval               = C   (differs from STAR)
  RCV-RR                 = B   (differs from STAR)
  Note: 3 of 21 ballots (14%) had equal non-zero scores, so their ranks were
        decided by candidate priority order. The RCV-IRV result may be an
        artifact of score-to-rank tie-breaking rather than a deep
        difference.
  Note: Ranked Robin (RCV-RR) sides with RCV-IRV, so STAR is the outlier
        here — STAR need not elect the Condorcet candidate.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: star_vs_rr_divergence_tabulated/cycle_09_c3_v21_RCV-IRV_tabulated.txt
  RCV-RR round-robin: star_vs_rr_divergence_tabulated/cycle_09_c3_v21_RCV-RR_tabulated.txt

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 21 ballots.
Count x A,B,C
    2 x 0,5,5
    2 x 4,5,0
    2 x 0,4,5
    2 x 5,0,3
    2 x 4,0,5
    2 x 5,0,0
    1 x 0,5,3
    1 x 0,5,4
    1 x 3,5,0
    1 x 2,0,5
    1 x 5,5,0
    1 x 5,0,4
    1 x 0,1,5
    1 x 2,5,0
    1 x 5,2,0

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   A             -- 58 -- First place
   C             -- 57 -- Second place
   B             -- 56
 A and C advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   A             -- 11 -- First place
   C             -- 10
   Equal Support --  0
 A wins.
   Runoff math:
     21  ballots cast
   −  0  Equal Support (no preference between the two finalists)
     ──
     21  voters with a preference  (majority = 11)
           A 11 (52%)  ·  C 10 (48%)

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
           * A > |     ---      | 9 -  1 - 11 |11 -  0 - 10 |
             B > | 11 -  1 -  9 |    ---      | 8 -  4 -  9 |
           * C > | 10 -  0 - 11 | 9 -  4 -  8 |    ---      |

[Condorcet Winner]
  No Condorcet winner (majority cycle: A > C > B > A)

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
A          7  4  1  2  0  7  |    58   2.8
B          9  2  0  1  1  8  |    56   2.7
C          8  2  3  0  0  8  |    57   2.7
```

Everything in one file: the [`_tabulated` mirror](../star_vs_rr_divergence_tabulated/cycle_09_c3_v21_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 05_Ranked_Robin/star_vs_rr_divergence/cycle_09_c3_v21.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [cycle_01_c5_v21](cycle_01_c5_v21.md) · [cycle_02_c5_v15](cycle_02_c5_v15.md) · [cycle_03_c5_v21](cycle_03_c5_v21.md) · [cycle_04_c5_v21](cycle_04_c5_v21.md) · [cycle_05_c5_v15](cycle_05_c5_v15.md) · [cycle_06_c4_v21](cycle_06_c4_v21.md) · [cycle_07_c4_v21](cycle_07_c4_v21.md) · [cycle_10_c4_v15](cycle_10_c4_v15.md) · [cycle_11_c4_v21](cycle_11_c4_v21.md) · [cycle_12_c3_v15](cycle_12_c3_v15.md) · [cycle_13_c5_v21](cycle_13_c5_v21.md) · [cycle_14_c3_v21](cycle_14_c3_v21.md) · [cycle_15_c5_v21](cycle_15_c5_v21.md) · [cycle_16_c3_v15](cycle_16_c3_v15.md) · [darkhorse_01_c5_v21](darkhorse_01_c5_v21.md) · [darkhorse_02_c4_v15](darkhorse_02_c4_v15.md) · [darkhorse_03_c5_v15](darkhorse_03_c5_v15.md) · [darkhorse_04_c4_v21](darkhorse_04_c4_v21.md) · [darkhorse_05_c5_v21](darkhorse_05_c5_v21.md) · [darkhorse_06_c4_v15](darkhorse_06_c4_v15.md) · [darkhorse_08_c5_v21](darkhorse_08_c5_v21.md) · [darkhorse_10_c5_v21](darkhorse_10_c5_v21.md) · [darkhorse_11_c5_v21](darkhorse_11_c5_v21.md) · [darkhorse_12_c5_v21](darkhorse_12_c5_v21.md) · [darkhorse_15_c5_v21](darkhorse_15_c5_v21.md) · [darkhorse_16_c4_v15](darkhorse_16_c4_v15.md) · [darkhorse_18_c4_v21](darkhorse_18_c4_v21.md) · [darkhorse_19_c4_v15](darkhorse_19_c4_v15.md) · [darkhorse_20_c5_v15](darkhorse_20_c5_v15.md)
