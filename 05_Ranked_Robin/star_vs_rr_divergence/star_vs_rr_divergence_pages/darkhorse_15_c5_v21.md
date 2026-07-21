# STAR vs Ranked Robin divergence — darkhorse_15_c5_v21 (STAR B, RR A)

*Generated from [`darkhorse_15_c5_v21.yaml`](../darkhorse_15_c5_v21.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** B

## Scenario

Auto-generated STAR-vs-Ranked-Robin divergence sample (darkhorse). 5 candidates, 21 voters, noise model. STAR elects B; Ranked Robin elects A; Condorcet winner A. See the [Divergence from STAR] block below for RCV-IRV, Approval and Plurality on the same ballots.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:A,B,C,D,E
1:5,5,3,5,0
1:1,0,4,1,5
1:3,5,5,0,1
1:5,4,0,3,4
1:5,1,1,0,3
1:0,0,0,2,5
1:0,5,1,5,5
1:0,4,4,5,3
1:5,4,3,0,4
1:5,3,0,5,5
1:5,4,4,0,3
1:0,4,5,3,0
1:0,5,3,1,0
1:1,5,4,2,0
1:1,2,0,5,5
1:4,5,5,0,2
1:3,2,5,0,3
1:5,5,5,0,5
1:3,2,0,3,5
1:5,2,1,0,1
1:5,0,2,0,3
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR                   = B
  Choose-One (Plurality) = A   (differs from STAR)
  RCV-IRV                = A   (differs from STAR)
  Approval               = E   (differs from STAR)
  RCV-RR (Condorcet)     = A   (differs from STAR)
  Note: 16 of 21 ballots (76%) had equal non-zero scores, so their ranks
        were decided by candidate priority order. The RCV-IRV result may be
        an artifact of score-to-rank tie-breaking rather than a deep
        difference.
  Note: Ranked Robin (RCV-RR) sides with RCV-IRV, so STAR is the outlier
        here — STAR need not elect the Condorcet candidate.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: star_vs_rr_divergence_tabulated/darkhorse_15_c5_v21_RCV-IRV_tabulated.txt
  RCV-RR round-robin: star_vs_rr_divergence_tabulated/darkhorse_15_c5_v21_RCV-RR_tabulated.txt

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 21 ballots.
A,B,C,D,E
5,5,3,5,0
1,0,4,1,5
3,5,5,0,1
5,4,0,3,4
5,1,1,0,3
0,0,0,2,5
0,5,1,5,5
0,4,4,5,3
5,4,3,0,4
5,3,0,5,5
5,4,4,0,3
0,4,5,3,0
0,5,3,1,0
1,5,4,2,0
1,2,0,5,5
4,5,5,0,2
3,2,5,0,3
5,5,5,0,5
3,2,0,3,5
5,2,1,0,1
5,0,2,0,3

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   B             -- 67 -- First place
   E             -- 62 -- Second place
   A             -- 61
   C             -- 55
   D             -- 40
 B and E advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   B             -- 9 -- First place
   E             -- 8
   Equal Support -- 4
 B wins.
   Runoff math:
     21  ballots cast
   −  4  Equal Support (no preference between the two finalists)
     ──
     17  voters with a preference  (majority = 9)
           B 9 (53%)  ·  E 8 (47%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 B
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |       A      |    * B      |      C      |      D      |    * E      |
-----------------------------------------------------------------------------------------
             A > |     ---      |10 -  3 -  8 |10 -  2 -  9 |10 -  4 -  7 |10 -  5 -  6 |
           * B > |  8 -  3 - 10 |    ---      |10 -  7 -  4 |12 -  3 -  6 | 9 -  4 -  8 |
             C > |  9 -  2 - 10 | 4 -  7 - 10 |    ---      |13 -  0 -  8 | 9 -  2 - 10 |
             D > |  7 -  4 - 10 | 6 -  3 - 12 | 8 -  0 - 13 |    ---      | 5 -  3 - 13 |
           * E > |  6 -  5 - 10 | 8 -  4 -  9 |10 -  2 -  9 |13 -  3 -  5 |    ---      |

[Condorcet Winner]
  Condorcet Winner: A — STAR elected B instead (A was eliminated in the scoring round)

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
A          9  1  3  0  3  5  |    61   2.9
B          7  5  1  4  1  3  |    67   3.2
C          5  4  3  1  3  5  |    55   2.6
D          5  0  3  2  2  9  |    40   1.9
E          7  2  5  1  2  4  |    62   3.0
```

Everything in one file: the [`_tabulated` mirror](../star_vs_rr_divergence_tabulated/darkhorse_15_c5_v21_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 05_Ranked_Robin/star_vs_rr_divergence/darkhorse_15_c5_v21.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [cycle_01_c5_v21](cycle_01_c5_v21.md) · [cycle_02_c5_v15](cycle_02_c5_v15.md) · [cycle_03_c5_v21](cycle_03_c5_v21.md) · [cycle_04_c5_v21](cycle_04_c5_v21.md) · [cycle_05_c5_v15](cycle_05_c5_v15.md) · [cycle_06_c4_v21](cycle_06_c4_v21.md) · [cycle_07_c4_v21](cycle_07_c4_v21.md) · [cycle_09_c3_v21](cycle_09_c3_v21.md) · [cycle_10_c4_v15](cycle_10_c4_v15.md) · [cycle_11_c4_v21](cycle_11_c4_v21.md) · [cycle_12_c3_v15](cycle_12_c3_v15.md) · [cycle_13_c5_v21](cycle_13_c5_v21.md) · [cycle_14_c3_v21](cycle_14_c3_v21.md) · [cycle_15_c5_v21](cycle_15_c5_v21.md) · [cycle_16_c3_v15](cycle_16_c3_v15.md) · [darkhorse_01_c5_v21](darkhorse_01_c5_v21.md) · [darkhorse_02_c4_v15](darkhorse_02_c4_v15.md) · [darkhorse_03_c5_v15](darkhorse_03_c5_v15.md) · [darkhorse_04_c4_v21](darkhorse_04_c4_v21.md) · [darkhorse_05_c5_v21](darkhorse_05_c5_v21.md) · [darkhorse_06_c4_v15](darkhorse_06_c4_v15.md) · [darkhorse_08_c5_v21](darkhorse_08_c5_v21.md) · [darkhorse_10_c5_v21](darkhorse_10_c5_v21.md) · [darkhorse_11_c5_v21](darkhorse_11_c5_v21.md) · [darkhorse_12_c5_v21](darkhorse_12_c5_v21.md) · [darkhorse_16_c4_v15](darkhorse_16_c4_v15.md) · [darkhorse_18_c4_v21](darkhorse_18_c4_v21.md) · [darkhorse_19_c4_v15](darkhorse_19_c4_v15.md) · [darkhorse_20_c5_v15](darkhorse_20_c5_v15.md)
