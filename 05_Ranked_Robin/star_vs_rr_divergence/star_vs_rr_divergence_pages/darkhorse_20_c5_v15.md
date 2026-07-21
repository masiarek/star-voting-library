# STAR vs Ranked Robin divergence — darkhorse_20_c5_v15 (STAR B, RR C)

*Generated from [`darkhorse_20_c5_v15.yaml`](../darkhorse_20_c5_v15.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** B

## Scenario

Auto-generated STAR-vs-Ranked-Robin divergence sample (darkhorse). 5 candidates, 15 voters, faction2d model. STAR elects B; Ranked Robin elects C; Condorcet winner C. See the [Divergence from STAR] block below for RCV-IRV, Approval and Plurality on the same ballots.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:A,B,C,D,E
1:0,4,5,3,3
1:1,5,0,2,3
1:0,5,5,3,5
1:0,3,5,2,4
1:1,5,0,1,3
1:0,5,5,5,4
1:0,5,2,0,4
1:0,4,5,2,4
1:3,5,0,2,4
1:0,3,5,2,4
1:0,3,5,2,4
1:0,3,5,3,3
1:0,3,5,2,4
1:0,5,0,2,3
1:0,5,0,1,3
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR               = B
  RCV-RR (Condorcet) = C   (differs from STAR)
  Full round-by-round reports (generated for review):
  RCV-RR round-robin: star_vs_rr_divergence_tabulated/darkhorse_20_c5_v15_RCV-RR_tabulated.txt

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 15 ballots.
Count x A,B,C,D,E
    4 x 0,3,5,2,4
    1 x 0,4,5,3,3
    1 x 1,5,0,2,3
    1 x 0,5,5,3,5
    1 x 1,5,0,1,3
    1 x 0,5,5,5,4
    1 x 0,5,2,0,4
    1 x 0,4,5,2,4
    1 x 3,5,0,2,4
    1 x 0,3,5,3,3
    1 x 0,5,0,2,3
    1 x 0,5,0,1,3

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   B             -- 63 -- First place
   E             -- 55 -- Second place
   C             -- 47
   D             -- 32
   A             --  5
 B and E advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   B             -- 8 -- First place
   E             -- 4
   Equal Support -- 3
 B wins.
   Runoff math:
     15  ballots cast
   −  3  Equal Support (no preference between the two finalists)
     ──
     12  voters with a preference  (majority = 7)
           B 8 (67%)  ·  E 4 (33%)

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
             A > |     ---      | 0 -  0 - 15 | 3 -  2 - 10 | 1 -  2 - 12 | 0 -  0 - 15 |
           * B > | 15 -  0 -  0 |    ---      | 6 -  2 -  7 |13 -  2 -  0 | 8 -  3 -  4 |
             C > | 10 -  2 -  3 | 7 -  2 -  6 |    ---      | 9 -  1 -  5 | 8 -  1 -  6 |
             D > | 12 -  2 -  1 | 0 -  2 - 13 | 5 -  1 -  9 |    ---      | 1 -  2 - 12 |
           * E > | 15 -  0 -  0 | 4 -  3 -  8 | 6 -  1 -  8 |12 -  2 -  1 |    ---      |

[Condorcet Winner]
  Condorcet Winner: C — STAR elected B instead (C was eliminated in the scoring round)

[Score Distribution] (how many ballots gave each star rating)
                   Score
Candidate   5   4   3   2   1   0  | Total   Avg
A           0   0   1   0   2  12  |     5   0.3
B           8   2   5   0   0   0  |    63   4.2
C           9   0   0   1   0   5  |    47   3.1
D           1   0   3   8   2   1  |    32   2.1
E           1   8   6   0   0   0  |    55   3.7
```

Everything in one file: the [`_tabulated` mirror](../star_vs_rr_divergence_tabulated/darkhorse_20_c5_v15_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 05_Ranked_Robin/star_vs_rr_divergence/darkhorse_20_c5_v15.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [cycle_01_c5_v21](cycle_01_c5_v21.md) · [cycle_02_c5_v15](cycle_02_c5_v15.md) · [cycle_03_c5_v21](cycle_03_c5_v21.md) · [cycle_04_c5_v21](cycle_04_c5_v21.md) · [cycle_05_c5_v15](cycle_05_c5_v15.md) · [cycle_06_c4_v21](cycle_06_c4_v21.md) · [cycle_07_c4_v21](cycle_07_c4_v21.md) · [cycle_09_c3_v21](cycle_09_c3_v21.md) · [cycle_10_c4_v15](cycle_10_c4_v15.md) · [cycle_11_c4_v21](cycle_11_c4_v21.md) · [cycle_12_c3_v15](cycle_12_c3_v15.md) · [cycle_13_c5_v21](cycle_13_c5_v21.md) · [cycle_14_c3_v21](cycle_14_c3_v21.md) · [cycle_15_c5_v21](cycle_15_c5_v21.md) · [cycle_16_c3_v15](cycle_16_c3_v15.md) · [darkhorse_01_c5_v21](darkhorse_01_c5_v21.md) · [darkhorse_02_c4_v15](darkhorse_02_c4_v15.md) · [darkhorse_03_c5_v15](darkhorse_03_c5_v15.md) · [darkhorse_04_c4_v21](darkhorse_04_c4_v21.md) · [darkhorse_05_c5_v21](darkhorse_05_c5_v21.md) · [darkhorse_06_c4_v15](darkhorse_06_c4_v15.md) · [darkhorse_08_c5_v21](darkhorse_08_c5_v21.md) · [darkhorse_10_c5_v21](darkhorse_10_c5_v21.md) · [darkhorse_11_c5_v21](darkhorse_11_c5_v21.md) · [darkhorse_12_c5_v21](darkhorse_12_c5_v21.md) · [darkhorse_15_c5_v21](darkhorse_15_c5_v21.md) · [darkhorse_16_c4_v15](darkhorse_16_c4_v15.md) · [darkhorse_18_c4_v21](darkhorse_18_c4_v21.md) · [darkhorse_19_c4_v15](darkhorse_19_c4_v15.md)
