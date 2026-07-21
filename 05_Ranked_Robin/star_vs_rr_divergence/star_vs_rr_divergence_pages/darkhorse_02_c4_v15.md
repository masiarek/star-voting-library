# STAR vs Ranked Robin divergence — darkhorse_02_c4_v15 (STAR A, RR C)

*Generated from [`darkhorse_02_c4_v15.yaml`](../darkhorse_02_c4_v15.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** A

## Scenario

Auto-generated STAR-vs-Ranked-Robin divergence sample (darkhorse). 4 candidates, 15 voters, noise model. STAR elects A; Ranked Robin elects C; Condorcet winner C. See the [Divergence from STAR] block below for RCV-IRV, Approval and Plurality on the same ballots.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:A,B,C,D
1:3,2,5,0
1:5,0,0,0
1:1,5,2,0
1:4,3,5,0
1:0,0,5,4
1:5,3,0,4
1:1,0,5,5
1:2,1,0,5
1:5,0,5,4
1:0,0,5,4
1:2,0,4,5
1:3,5,0,4
1:4,0,5,4
1:3,5,0,3
1:5,2,0,1
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR                   = A
  Choose-One (Plurality) = C   (differs from STAR)
  RCV-IRV                = C   (differs from STAR)
  Approval               = D   (differs from STAR)
  RCV-RR (Condorcet)     = C   (differs from STAR)
  Note: 4 of 15 ballots (27%) had equal non-zero scores, so their ranks were
        decided by candidate priority order. The RCV-IRV result may be an
        artifact of score-to-rank tie-breaking rather than a deep
        difference.
  Note: Ranked Robin (RCV-RR) sides with RCV-IRV, so STAR is the outlier
        here — STAR need not elect the Condorcet candidate.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: star_vs_rr_divergence_tabulated/darkhorse_02_c4_v15_RCV-IRV_tabulated.txt
  RCV-RR round-robin: star_vs_rr_divergence_tabulated/darkhorse_02_c4_v15_RCV-RR_tabulated.txt

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 15 ballots.
Count x A,B,C,D
    2 x 0,0,5,4
    1 x 3,2,5,0
    1 x 5,0,0,0
    1 x 1,5,2,0
    1 x 4,3,5,0
    1 x 5,3,0,4
    1 x 1,0,5,5
    1 x 2,1,0,5
    1 x 5,0,5,4
    1 x 2,0,4,5
    1 x 3,5,0,4
    1 x 4,0,5,4
    1 x 3,5,0,3
    1 x 5,2,0,1

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   A             -- 43 -- First place
   D             -- 43 -- Second place
   C             -- 41
   B             -- 26
 A and D advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   A             -- 7 -- First place
   D             -- 6
   Equal Support -- 2
 A wins.
   Runoff math:
     15  ballots cast
   −  2  Equal Support (no preference between the two finalists)
     ──
     13  voters with a preference  (majority = 7)
           A 7 (54%)  ·  D 6 (46%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 A
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |     * A      |      B      |      C      |    * D      |
---------------------------------------------------------------------------
           * A > |     ---      |10 -  2 -  3 | 6 -  1 -  8 | 7 -  2 -  6 |
             B > |  3 -  2 - 10 |    ---      | 6 -  1 -  8 | 6 -  1 -  8 |
             C > |  8 -  1 -  6 | 8 -  1 -  6 |    ---      | 7 -  2 -  6 |
           * D > |  6 -  2 -  7 | 8 -  1 -  6 | 6 -  2 -  7 |    ---      |

[Condorcet Winner]
  Condorcet Winner: C — STAR elected A instead (C was eliminated in the scoring round)

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
A          4  2  3  2  2  2  |    43   2.9
B          3  0  2  2  1  7  |    26   1.7
C          7  1  0  1  0  6  |    41   2.7
D          3  6  1  0  1  4  |    43   2.9
```

Everything in one file: the [`_tabulated` mirror](../star_vs_rr_divergence_tabulated/darkhorse_02_c4_v15_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 05_Ranked_Robin/star_vs_rr_divergence/darkhorse_02_c4_v15.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [cycle_01_c5_v21](cycle_01_c5_v21.md) · [cycle_02_c5_v15](cycle_02_c5_v15.md) · [cycle_03_c5_v21](cycle_03_c5_v21.md) · [cycle_04_c5_v21](cycle_04_c5_v21.md) · [cycle_05_c5_v15](cycle_05_c5_v15.md) · [cycle_06_c4_v21](cycle_06_c4_v21.md) · [cycle_07_c4_v21](cycle_07_c4_v21.md) · [cycle_09_c3_v21](cycle_09_c3_v21.md) · [cycle_10_c4_v15](cycle_10_c4_v15.md) · [cycle_11_c4_v21](cycle_11_c4_v21.md) · [cycle_12_c3_v15](cycle_12_c3_v15.md) · [cycle_13_c5_v21](cycle_13_c5_v21.md) · [cycle_14_c3_v21](cycle_14_c3_v21.md) · [cycle_15_c5_v21](cycle_15_c5_v21.md) · [cycle_16_c3_v15](cycle_16_c3_v15.md) · [darkhorse_01_c5_v21](darkhorse_01_c5_v21.md) · [darkhorse_03_c5_v15](darkhorse_03_c5_v15.md) · [darkhorse_04_c4_v21](darkhorse_04_c4_v21.md) · [darkhorse_05_c5_v21](darkhorse_05_c5_v21.md) · [darkhorse_06_c4_v15](darkhorse_06_c4_v15.md) · [darkhorse_08_c5_v21](darkhorse_08_c5_v21.md) · [darkhorse_10_c5_v21](darkhorse_10_c5_v21.md) · [darkhorse_11_c5_v21](darkhorse_11_c5_v21.md) · [darkhorse_12_c5_v21](darkhorse_12_c5_v21.md) · [darkhorse_15_c5_v21](darkhorse_15_c5_v21.md) · [darkhorse_16_c4_v15](darkhorse_16_c4_v15.md) · [darkhorse_18_c4_v21](darkhorse_18_c4_v21.md) · [darkhorse_19_c4_v15](darkhorse_19_c4_v15.md) · [darkhorse_20_c5_v15](darkhorse_20_c5_v15.md)
