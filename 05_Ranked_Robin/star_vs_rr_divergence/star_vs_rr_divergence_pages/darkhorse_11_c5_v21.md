# STAR vs Ranked Robin divergence — darkhorse_11_c5_v21 (STAR D, RR E)

*Generated from [`darkhorse_11_c5_v21.yaml`](../darkhorse_11_c5_v21.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** D

## Scenario

Auto-generated STAR-vs-Ranked-Robin divergence sample (darkhorse). 5 candidates, 21 voters, faction2d model. STAR elects D; Ranked Robin elects E; Condorcet winner E. See the [Divergence from STAR] block below for RCV-IRV, Approval and Plurality on the same ballots.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:A,B,C,D,E
1:0,1,4,5,3
1:0,2,4,5,2
1:5,0,3,2,4
1:0,1,5,5,3
1:0,1,5,5,3
1:5,0,2,2,3
1:5,0,3,3,5
1:1,0,5,5,3
1:5,0,3,2,4
1:5,0,2,2,3
1:5,0,2,2,4
1:5,0,3,2,4
1:0,1,4,5,2
1:5,0,4,3,5
1:5,0,3,3,4
1:0,2,4,5,3
1:0,1,4,5,2
1:0,1,3,5,2
1:5,0,3,2,4
1:5,0,3,3,5
1:0,2,4,5,3
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR                   = D
  Choose-One (Plurality) = A   (differs from STAR)
  RCV-IRV                = A   (differs from STAR)
  Approval               = C   (differs from STAR)
  RCV-RR (Condorcet)     = E   (differs from STAR)
  Note: 11 of 21 ballots (52%) had equal non-zero scores, so their ranks
        were decided by candidate priority order. The RCV-IRV result may be
        an artifact of score-to-rank tie-breaking rather than a deep
        difference.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: star_vs_rr_divergence_tabulated/darkhorse_11_c5_v21_RCV-IRV_tabulated.txt
  RCV-RR round-robin: star_vs_rr_divergence_tabulated/darkhorse_11_c5_v21_RCV-RR_tabulated.txt

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 21 ballots.
Count x A,B,C,D,E
    4 x 5,0,3,2,4
    2 x 0,1,5,5,3
    2 x 5,0,2,2,3
    2 x 5,0,3,3,5
    2 x 0,1,4,5,2
    2 x 0,2,4,5,3
    1 x 0,1,4,5,3
    1 x 0,2,4,5,2
    1 x 1,0,5,5,3
    1 x 5,0,2,2,4
    1 x 5,0,4,3,5
    1 x 5,0,3,3,4
    1 x 0,1,3,5,2

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   D             -- 76 -- First place
   C             -- 73 -- Second place
   E             -- 71
   A             -- 56
   B             -- 12
 D and C advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   D             -- 7 -- First place
   C             -- 5
   Equal Support -- 9
 D wins.
   Runoff math:
     21  ballots cast
   −  9  Equal Support (no preference between the two finalists)
     ──
     12  voters with a preference  (majority = 7)
           D 7 (58%)  ·  C 5 (42%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 D
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |       A      |      B      |    * C      |    * D      |      E      |
-----------------------------------------------------------------------------------------
             A > |     ---      |12 -  0 -  9 |11 -  0 - 10 |11 -  0 - 10 | 8 -  3 - 10 |
             B > |  9 -  0 - 12 |    ---      | 0 -  0 - 21 | 0 -  0 - 21 | 0 -  1 - 20 |
           * C > | 10 -  0 - 11 |21 -  0 -  0 |    ---      | 5 -  9 -  7 |10 -  0 - 11 |
           * D > | 10 -  0 - 11 |21 -  0 -  0 | 7 -  9 -  5 |    ---      |10 -  0 - 11 |
             E > | 10 -  3 -  8 |20 -  1 -  0 |11 -  0 - 10 |11 -  0 - 10 |    ---      |

[Condorcet Winner]
  Condorcet Winner: E — STAR elected D instead (E was eliminated in the scoring round)

[Score Distribution] (how many ballots gave each star rating)
                   Score
Candidate   5   4   3   2   1   0  | Total   Avg
A          11   0   0   0   1   9  |    56   2.7
B           0   0   0   3   6  12  |    12   0.6
C           3   7   8   3   0   0  |    73   3.5
D          10   0   4   7   0   0  |    76   3.6
E           3   6   8   4   0   0  |    71   3.4
```

Everything in one file: the [`_tabulated` mirror](../star_vs_rr_divergence_tabulated/darkhorse_11_c5_v21_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 05_Ranked_Robin/star_vs_rr_divergence/darkhorse_11_c5_v21.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [cycle_01_c5_v21](cycle_01_c5_v21.md) · [cycle_02_c5_v15](cycle_02_c5_v15.md) · [cycle_03_c5_v21](cycle_03_c5_v21.md) · [cycle_04_c5_v21](cycle_04_c5_v21.md) · [cycle_05_c5_v15](cycle_05_c5_v15.md) · [cycle_06_c4_v21](cycle_06_c4_v21.md) · [cycle_07_c4_v21](cycle_07_c4_v21.md) · [cycle_09_c3_v21](cycle_09_c3_v21.md) · [cycle_10_c4_v15](cycle_10_c4_v15.md) · [cycle_11_c4_v21](cycle_11_c4_v21.md) · [cycle_12_c3_v15](cycle_12_c3_v15.md) · [cycle_13_c5_v21](cycle_13_c5_v21.md) · [cycle_14_c3_v21](cycle_14_c3_v21.md) · [cycle_15_c5_v21](cycle_15_c5_v21.md) · [cycle_16_c3_v15](cycle_16_c3_v15.md) · [darkhorse_01_c5_v21](darkhorse_01_c5_v21.md) · [darkhorse_02_c4_v15](darkhorse_02_c4_v15.md) · [darkhorse_03_c5_v15](darkhorse_03_c5_v15.md) · [darkhorse_04_c4_v21](darkhorse_04_c4_v21.md) · [darkhorse_05_c5_v21](darkhorse_05_c5_v21.md) · [darkhorse_06_c4_v15](darkhorse_06_c4_v15.md) · [darkhorse_08_c5_v21](darkhorse_08_c5_v21.md) · [darkhorse_10_c5_v21](darkhorse_10_c5_v21.md) · [darkhorse_12_c5_v21](darkhorse_12_c5_v21.md) · [darkhorse_15_c5_v21](darkhorse_15_c5_v21.md) · [darkhorse_16_c4_v15](darkhorse_16_c4_v15.md) · [darkhorse_18_c4_v21](darkhorse_18_c4_v21.md) · [darkhorse_19_c4_v15](darkhorse_19_c4_v15.md) · [darkhorse_20_c5_v15](darkhorse_20_c5_v15.md)
