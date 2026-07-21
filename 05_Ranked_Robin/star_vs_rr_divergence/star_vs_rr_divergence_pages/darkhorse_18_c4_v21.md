# STAR vs Ranked Robin divergence — darkhorse_18_c4_v21 (STAR D, RR A)

*Generated from [`darkhorse_18_c4_v21.yaml`](../darkhorse_18_c4_v21.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** D

## Scenario

Auto-generated STAR-vs-Ranked-Robin divergence sample (darkhorse). 4 candidates, 21 voters, spatial2d model. STAR elects D; Ranked Robin elects A; Condorcet winner A. See the [Divergence from STAR] block below for RCV-IRV, Approval and Plurality on the same ballots.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:A,B,C,D
1:3,0,5,1
1:1,5,5,0
1:3,0,2,5
1:1,0,2,5
1:4,0,5,2
1:5,0,3,4
1:2,0,1,5
1:0,5,0,5
1:2,0,3,5
1:5,0,3,4
1:3,0,2,5
1:5,0,4,2
1:5,0,4,4
1:5,0,2,4
1:3,0,5,1
1:2,0,5,0
1:3,3,5,0
1:2,0,1,5
1:4,0,5,1
1:5,0,4,4
1:3,0,2,5
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR               = D
  Approval           = A   (differs from STAR)
  RCV-RR (Condorcet) = A   (differs from STAR)
  Full round-by-round reports (generated for review):
  RCV-RR round-robin: star_vs_rr_divergence_tabulated/darkhorse_18_c4_v21_RCV-RR_tabulated.txt

[Runoff Reversal]
 - Score Round Winner(s) = (C)
 - Runoff Round Winner   = (D)
  Candidate C earned the highest total score, but
  Candidate D won the automatic runoff — not a malfunction,
  STAR working as designed: the runoff elects the finalist preferred
  by the majority (of voters with a preference).

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 21 ballots.
Count x A,B,C,D
    3 x 3,0,2,5
    2 x 3,0,5,1
    2 x 5,0,3,4
    2 x 2,0,1,5
    2 x 5,0,4,4
    1 x 1,5,5,0
    1 x 1,0,2,5
    1 x 4,0,5,2
    1 x 0,5,0,5
    1 x 2,0,3,5
    1 x 5,0,4,2
    1 x 5,0,2,4
    1 x 2,0,5,0
    1 x 3,3,5,0
    1 x 4,0,5,1

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   C             -- 68 -- First place
   D             -- 67 -- Second place
   A             -- 66
   B             -- 13
 C and D advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   D             -- 11 -- First place
   C             --  8
   Equal Support --  2
 D wins.
   Runoff math:
     21  ballots cast
   −  2  Equal Support (no preference between the two finalists)
     ──
     19  voters with a preference  (majority = 10)
           D 11 (58%)  ·  C 8 (42%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 D
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |       A      |      B      |    * C      |    * D      |
---------------------------------------------------------------------------
             A > |     ---      |18 -  1 -  2 |11 -  1 -  9 |13 -  0 -  8 |
             B > |  2 -  1 - 18 |    ---      | 1 -  1 - 19 | 2 -  2 - 17 |
           * C > |  9 -  1 - 11 |19 -  1 -  1 |    ---      | 8 -  2 - 11 |
           * D > |  8 -  0 - 13 |17 -  2 -  2 |11 -  2 -  8 |    ---      |

[Condorcet Winner]
  Condorcet Winner: A — STAR elected D instead (A was eliminated in the scoring round)

[Score Distribution] (how many ballots gave each star rating)
                   Score
Candidate   5   4   3   2   1   0  | Total   Avg
A           6   2   6   4   2   1  |    66   3.1
B           2   0   1   0   0  18  |    13   0.6
C           7   3   3   5   2   1  |    68   3.2
D           8   5   0   2   3   3  |    67   3.2
```

Everything in one file: the [`_tabulated` mirror](../star_vs_rr_divergence_tabulated/darkhorse_18_c4_v21_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 05_Ranked_Robin/star_vs_rr_divergence/darkhorse_18_c4_v21.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [cycle_01_c5_v21](cycle_01_c5_v21.md) · [cycle_02_c5_v15](cycle_02_c5_v15.md) · [cycle_03_c5_v21](cycle_03_c5_v21.md) · [cycle_04_c5_v21](cycle_04_c5_v21.md) · [cycle_05_c5_v15](cycle_05_c5_v15.md) · [cycle_06_c4_v21](cycle_06_c4_v21.md) · [cycle_07_c4_v21](cycle_07_c4_v21.md) · [cycle_09_c3_v21](cycle_09_c3_v21.md) · [cycle_10_c4_v15](cycle_10_c4_v15.md) · [cycle_11_c4_v21](cycle_11_c4_v21.md) · [cycle_12_c3_v15](cycle_12_c3_v15.md) · [cycle_13_c5_v21](cycle_13_c5_v21.md) · [cycle_14_c3_v21](cycle_14_c3_v21.md) · [cycle_15_c5_v21](cycle_15_c5_v21.md) · [cycle_16_c3_v15](cycle_16_c3_v15.md) · [darkhorse_01_c5_v21](darkhorse_01_c5_v21.md) · [darkhorse_02_c4_v15](darkhorse_02_c4_v15.md) · [darkhorse_03_c5_v15](darkhorse_03_c5_v15.md) · [darkhorse_04_c4_v21](darkhorse_04_c4_v21.md) · [darkhorse_05_c5_v21](darkhorse_05_c5_v21.md) · [darkhorse_06_c4_v15](darkhorse_06_c4_v15.md) · [darkhorse_08_c5_v21](darkhorse_08_c5_v21.md) · [darkhorse_10_c5_v21](darkhorse_10_c5_v21.md) · [darkhorse_11_c5_v21](darkhorse_11_c5_v21.md) · [darkhorse_12_c5_v21](darkhorse_12_c5_v21.md) · [darkhorse_15_c5_v21](darkhorse_15_c5_v21.md) · [darkhorse_16_c4_v15](darkhorse_16_c4_v15.md) · [darkhorse_19_c4_v15](darkhorse_19_c4_v15.md) · [darkhorse_20_c5_v15](darkhorse_20_c5_v15.md)
