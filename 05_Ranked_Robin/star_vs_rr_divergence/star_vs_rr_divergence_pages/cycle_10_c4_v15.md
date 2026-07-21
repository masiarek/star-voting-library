# STAR vs Ranked Robin divergence — cycle_10_c4_v15 (STAR C, RR A)

*Generated from [`cycle_10_c4_v15.yaml`](../cycle_10_c4_v15.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** C

## Scenario

Auto-generated STAR-vs-Ranked-Robin divergence sample (cycle). 4 candidates, 15 voters, noise model. STAR elects C; Ranked Robin elects A; no Condorcet winner (cycle). See the [Divergence from STAR] block below for RCV-IRV, Approval and Plurality on the same ballots.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:A,B,C,D
1:0,4,3,5
1:3,0,4,5
1:5,2,4,0
1:1,0,5,1
1:3,2,5,0
1:2,5,5,0
1:5,5,0,2
1:2,2,5,0
1:0,5,2,2
1:5,0,2,4
1:5,0,4,2
1:1,0,5,5
1:5,0,0,1
1:5,0,2,5
1:5,0,0,5
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR                   = C
  Choose-One (Plurality) = A   (differs from STAR)
  Approval               = A   (differs from STAR)
  RCV-RR                 = A   (differs from STAR)
  Full round-by-round reports (generated for review):
  RCV-RR round-robin: star_vs_rr_divergence_tabulated/cycle_10_c4_v15_RCV-RR_tabulated.txt

[Runoff Reversal]
 - Score Round Winner(s) = (A)
 - Runoff Round Winner   = (C)
  Candidate A earned the highest total score, but
  Candidate C won the automatic runoff — not a malfunction,
  STAR working as designed: the runoff elects the finalist preferred
  by the majority (of voters with a preference).

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 15 ballots.
A,B,C,D
0,4,3,5
3,0,4,5
5,2,4,0
1,0,5,1
3,2,5,0
2,5,5,0
5,5,0,2
2,2,5,0
0,5,2,2
5,0,2,4
5,0,4,2
1,0,5,5
5,0,0,1
5,0,2,5
5,0,0,5

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   A             -- 47 -- First place
   C             -- 46 -- Second place
   D             -- 37
   B             -- 25
 A and C advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   C             -- 8 -- First place
   A             -- 7
   Equal Support -- 0
 C wins.
   Runoff math:
     15  ballots cast
   −  0  Equal Support (no preference between the two finalists)
     ──
     15  voters with a preference  (majority = 8)
           C 8 (53%)  ·  A 7 (47%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 C
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |     * A      |      B      |    * C      |      D      |
---------------------------------------------------------------------------
           * A > |     ---      |10 -  2 -  3 | 7 -  0 -  8 | 8 -  3 -  4 |
             B > |  3 -  2 - 10 |    ---      | 3 -  3 -  9 | 6 -  0 -  9 |
           * C > |  8 -  0 -  7 | 9 -  3 -  3 |    ---      | 6 -  2 -  7 |
             D > |  4 -  3 -  8 | 9 -  0 -  6 | 7 -  2 -  6 |    ---      |

[Condorcet Winner]
  No Condorcet winner (majority cycle: A > D > C > A)

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
A          7  0  2  2  2  2  |    47   3.1
B          3  1  0  3  0  8  |    25   1.7
C          5  3  1  3  0  3  |    46   3.1
D          5  1  0  3  2  4  |    37   2.5
```

Everything in one file: the [`_tabulated` mirror](../star_vs_rr_divergence_tabulated/cycle_10_c4_v15_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 05_Ranked_Robin/star_vs_rr_divergence/cycle_10_c4_v15.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [cycle_01_c5_v21](cycle_01_c5_v21.md) · [cycle_02_c5_v15](cycle_02_c5_v15.md) · [cycle_03_c5_v21](cycle_03_c5_v21.md) · [cycle_04_c5_v21](cycle_04_c5_v21.md) · [cycle_05_c5_v15](cycle_05_c5_v15.md) · [cycle_06_c4_v21](cycle_06_c4_v21.md) · [cycle_07_c4_v21](cycle_07_c4_v21.md) · [cycle_09_c3_v21](cycle_09_c3_v21.md) · [cycle_11_c4_v21](cycle_11_c4_v21.md) · [cycle_12_c3_v15](cycle_12_c3_v15.md) · [cycle_13_c5_v21](cycle_13_c5_v21.md) · [cycle_14_c3_v21](cycle_14_c3_v21.md) · [cycle_15_c5_v21](cycle_15_c5_v21.md) · [cycle_16_c3_v15](cycle_16_c3_v15.md) · [darkhorse_01_c5_v21](darkhorse_01_c5_v21.md) · [darkhorse_02_c4_v15](darkhorse_02_c4_v15.md) · [darkhorse_03_c5_v15](darkhorse_03_c5_v15.md) · [darkhorse_04_c4_v21](darkhorse_04_c4_v21.md) · [darkhorse_05_c5_v21](darkhorse_05_c5_v21.md) · [darkhorse_06_c4_v15](darkhorse_06_c4_v15.md) · [darkhorse_08_c5_v21](darkhorse_08_c5_v21.md) · [darkhorse_10_c5_v21](darkhorse_10_c5_v21.md) · [darkhorse_11_c5_v21](darkhorse_11_c5_v21.md) · [darkhorse_12_c5_v21](darkhorse_12_c5_v21.md) · [darkhorse_15_c5_v21](darkhorse_15_c5_v21.md) · [darkhorse_16_c4_v15](darkhorse_16_c4_v15.md) · [darkhorse_18_c4_v21](darkhorse_18_c4_v21.md) · [darkhorse_19_c4_v15](darkhorse_19_c4_v15.md) · [darkhorse_20_c5_v15](darkhorse_20_c5_v15.md)
