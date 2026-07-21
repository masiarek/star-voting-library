# STAR vs Ranked Robin divergence — darkhorse_12_c5_v21 (STAR B, RR C)

*Generated from [`darkhorse_12_c5_v21.yaml`](../darkhorse_12_c5_v21.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** B

## Scenario

Auto-generated STAR-vs-Ranked-Robin divergence sample (darkhorse). 5 candidates, 21 voters, faction2d model. STAR elects B; Ranked Robin elects C; Condorcet winner C. See the [Divergence from STAR] block below for RCV-IRV, Approval and Plurality on the same ballots.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:A,B,C,D,E
1:5,4,0,3,2
1:5,4,0,3,5
1:3,4,5,3,0
1:3,4,5,3,0
1:2,5,0,2,0
1:3,4,5,3,0
1:3,5,0,4,1
1:3,5,0,4,0
1:5,4,0,4,1
1:3,4,4,5,0
1:4,4,5,5,0
1:4,3,5,1,0
1:3,3,0,2,5
1:2,4,5,3,0
1:2,3,5,4,0
1:4,5,5,3,0
1:4,4,5,3,0
1:5,4,0,4,4
1:4,5,3,2,0
1:5,3,4,4,0
1:4,4,5,4,0
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR                   = B
  Choose-One (Plurality) = C   (differs from STAR)
  RCV-RR (Condorcet)     = C   (differs from STAR)
  Full round-by-round reports (generated for review):
  RCV-RR round-robin: star_vs_rr_divergence_tabulated/darkhorse_12_c5_v21_RCV-RR_tabulated.txt

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 21 ballots.
Count x A,B,C,D,E
    3 x 3,4,5,3,0
    1 x 5,4,0,3,2
    1 x 5,4,0,3,5
    1 x 2,5,0,2,0
    1 x 3,5,0,4,1
    1 x 3,5,0,4,0
    1 x 5,4,0,4,1
    1 x 3,4,4,5,0
    1 x 4,4,5,5,0
    1 x 4,3,5,1,0
    1 x 3,3,0,2,5
    1 x 2,4,5,3,0
    1 x 2,3,5,4,0
    1 x 4,5,5,3,0
    1 x 4,4,5,3,0
    1 x 5,4,0,4,4
    1 x 4,5,3,2,0
    1 x 5,3,4,4,0
    1 x 4,4,5,4,0

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   B             -- 85 -- First place
   A             -- 76 -- Second place
   D             -- 69
   C             -- 61
   E             -- 18
 B and A advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   B             -- 11 -- First place
   A             --  6
   Equal Support --  4
 B wins.
   Runoff math:
     21  ballots cast
   −  4  Equal Support (no preference between the two finalists)
     ──
     17  voters with a preference  (majority = 9)
           B 11 (65%)  ·  A 6 (35%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 B
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |     * A      |    * B      |      C      |      D      |      E      |
-----------------------------------------------------------------------------------------
           * A > |     ---      | 6 -  4 - 11 |10 -  0 - 11 |10 -  5 -  6 |19 -  1 -  1 |
           * B > | 11 -  4 -  6 |    ---      | 9 -  2 - 10 |14 -  3 -  4 |18 -  1 -  2 |
             C > | 11 -  0 - 10 |10 -  2 -  9 |    ---      |10 -  2 -  9 |13 -  2 -  6 |
             D > |  6 -  5 - 10 | 4 -  3 - 14 | 9 -  2 - 10 |    ---      |18 -  1 -  2 |
             E > |  1 -  1 - 19 | 2 -  1 - 18 | 6 -  2 - 13 | 2 -  1 - 18 |    ---      |

[Condorcet Winner]
  Condorcet Winner: C — STAR elected B instead (C was eliminated in the scoring round)

[Score Distribution] (how many ballots gave each star rating)
                   Score
Candidate   5   4   3   2   1   0  | Total   Avg
A           5   6   7   3   0   0  |    76   3.6
B           5  12   4   0   0   0  |    85   4.0
C          10   2   1   0   0   8  |    61   2.9
D           2   7   8   3   1   0  |    69   3.3
E           2   1   0   1   2  15  |    18   0.9
```

Everything in one file: the [`_tabulated` mirror](../star_vs_rr_divergence_tabulated/darkhorse_12_c5_v21_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 05_Ranked_Robin/star_vs_rr_divergence/darkhorse_12_c5_v21.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [cycle_01_c5_v21](cycle_01_c5_v21.md) · [cycle_02_c5_v15](cycle_02_c5_v15.md) · [cycle_03_c5_v21](cycle_03_c5_v21.md) · [cycle_04_c5_v21](cycle_04_c5_v21.md) · [cycle_05_c5_v15](cycle_05_c5_v15.md) · [cycle_06_c4_v21](cycle_06_c4_v21.md) · [cycle_07_c4_v21](cycle_07_c4_v21.md) · [cycle_09_c3_v21](cycle_09_c3_v21.md) · [cycle_10_c4_v15](cycle_10_c4_v15.md) · [cycle_11_c4_v21](cycle_11_c4_v21.md) · [cycle_12_c3_v15](cycle_12_c3_v15.md) · [cycle_13_c5_v21](cycle_13_c5_v21.md) · [cycle_14_c3_v21](cycle_14_c3_v21.md) · [cycle_15_c5_v21](cycle_15_c5_v21.md) · [cycle_16_c3_v15](cycle_16_c3_v15.md) · [darkhorse_01_c5_v21](darkhorse_01_c5_v21.md) · [darkhorse_02_c4_v15](darkhorse_02_c4_v15.md) · [darkhorse_03_c5_v15](darkhorse_03_c5_v15.md) · [darkhorse_04_c4_v21](darkhorse_04_c4_v21.md) · [darkhorse_05_c5_v21](darkhorse_05_c5_v21.md) · [darkhorse_06_c4_v15](darkhorse_06_c4_v15.md) · [darkhorse_08_c5_v21](darkhorse_08_c5_v21.md) · [darkhorse_10_c5_v21](darkhorse_10_c5_v21.md) · [darkhorse_11_c5_v21](darkhorse_11_c5_v21.md) · [darkhorse_15_c5_v21](darkhorse_15_c5_v21.md) · [darkhorse_16_c4_v15](darkhorse_16_c4_v15.md) · [darkhorse_18_c4_v21](darkhorse_18_c4_v21.md) · [darkhorse_19_c4_v15](darkhorse_19_c4_v15.md) · [darkhorse_20_c5_v15](darkhorse_20_c5_v15.md)
