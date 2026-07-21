# STAR vs Ranked Robin divergence — darkhorse_05_c5_v21 (STAR E, RR B)

*Generated from [`darkhorse_05_c5_v21.yaml`](../darkhorse_05_c5_v21.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** E

## Scenario

Auto-generated STAR-vs-Ranked-Robin divergence sample (darkhorse). 5 candidates, 21 voters, faction2d model. STAR elects E; Ranked Robin elects B; Condorcet winner B. See the [Divergence from STAR] block below for RCV-IRV, Approval and Plurality on the same ballots.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:A,B,C,D,E
1:2,5,4,0,4
1:1,4,5,0,4
1:3,5,3,0,4
1:5,0,1,3,3
1:4,0,5,2,5
1:2,5,4,0,4
1:0,3,5,1,3
1:2,5,3,0,4
1:5,1,0,0,3
1:3,5,3,0,5
1:2,5,3,0,3
1:2,5,3,0,3
1:3,5,4,0,4
1:5,0,4,4,1
1:3,5,4,0,4
1:3,5,4,0,4
1:0,2,5,1,3
1:5,0,2,0,2
1:5,0,2,4,3
1:2,5,5,0,4
1:3,5,3,0,4
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR                   = E
  Choose-One (Plurality) = B   (differs from STAR)
  RCV-IRV                = B   (differs from STAR)
  RCV-RR (Condorcet)     = B   (differs from STAR)
  Note: 17 of 21 ballots (81%) had equal non-zero scores, so their ranks
        were decided by candidate priority order. The RCV-IRV result may be
        an artifact of score-to-rank tie-breaking rather than a deep
        difference.
  Note: Ranked Robin (RCV-RR) sides with RCV-IRV, so STAR is the outlier
        here — STAR need not elect the Condorcet candidate.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: star_vs_rr_divergence_tabulated/darkhorse_05_c5_v21_RCV-IRV_tabulated.txt
  RCV-RR round-robin: star_vs_rr_divergence_tabulated/darkhorse_05_c5_v21_RCV-RR_tabulated.txt

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 21 ballots.
Count x A,B,C,D,E
    3 x 3,5,4,0,4
    2 x 2,5,4,0,4
    2 x 3,5,3,0,4
    2 x 2,5,3,0,3
    1 x 1,4,5,0,4
    1 x 5,0,1,3,3
    1 x 4,0,5,2,5
    1 x 0,3,5,1,3
    1 x 2,5,3,0,4
    1 x 5,1,0,0,3
    1 x 3,5,3,0,5
    1 x 5,0,4,4,1
    1 x 0,2,5,1,3
    1 x 5,0,2,0,2
    1 x 5,0,2,4,3
    1 x 2,5,5,0,4

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   E             -- 74 -- First place
   C             -- 72 -- Second place
   B             -- 70
   A             -- 60
   D             -- 15
 E and C advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   E             -- 7 -- First place
   C             -- 5
   Equal Support -- 9
 E wins.
   Runoff math:
     21  ballots cast
   −  9  Equal Support (no preference between the two finalists)
     ──
     12  voters with a preference  (majority = 7)
           E 7 (58%)  ·  C 5 (42%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 E
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |       A      |      B      |    * C      |      D      |    * E      |
-----------------------------------------------------------------------------------------
             A > |     ---      | 6 -  0 - 15 | 5 -  3 - 13 |19 -  0 -  2 | 5 -  0 - 16 |
             B > | 15 -  0 -  6 |    ---      |12 -  1 -  8 |16 -  1 -  4 |11 -  3 -  7 |
           * C > | 13 -  3 -  5 | 8 -  1 - 12 |    ---      |17 -  2 -  2 | 5 -  9 -  7 |
             D > |  2 -  0 - 19 | 4 -  1 - 16 | 2 -  2 - 17 |    ---      | 2 -  1 - 18 |
           * E > | 16 -  0 -  5 | 7 -  3 - 11 | 7 -  9 -  5 |18 -  1 -  2 |    ---      |

[Condorcet Winner]
  Condorcet Winner: B — STAR elected E instead (B was eliminated in the scoring round)

[Score Distribution] (how many ballots gave each star rating)
                   Score
Candidate   5   4   3   2   1   0  | Total   Avg
A           5   1   6   6   1   2  |    60   2.9
B          12   1   1   1   1   5  |    70   3.3
C           5   6   6   2   1   1  |    72   3.4
D           0   2   1   1   2  15  |    15   0.7
E           2  10   7   1   1   0  |    74   3.5
```

Everything in one file: the [`_tabulated` mirror](../star_vs_rr_divergence_tabulated/darkhorse_05_c5_v21_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 05_Ranked_Robin/star_vs_rr_divergence/darkhorse_05_c5_v21.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [cycle_01_c5_v21](cycle_01_c5_v21.md) · [cycle_02_c5_v15](cycle_02_c5_v15.md) · [cycle_03_c5_v21](cycle_03_c5_v21.md) · [cycle_04_c5_v21](cycle_04_c5_v21.md) · [cycle_05_c5_v15](cycle_05_c5_v15.md) · [cycle_06_c4_v21](cycle_06_c4_v21.md) · [cycle_07_c4_v21](cycle_07_c4_v21.md) · [cycle_09_c3_v21](cycle_09_c3_v21.md) · [cycle_10_c4_v15](cycle_10_c4_v15.md) · [cycle_11_c4_v21](cycle_11_c4_v21.md) · [cycle_12_c3_v15](cycle_12_c3_v15.md) · [cycle_13_c5_v21](cycle_13_c5_v21.md) · [cycle_14_c3_v21](cycle_14_c3_v21.md) · [cycle_15_c5_v21](cycle_15_c5_v21.md) · [cycle_16_c3_v15](cycle_16_c3_v15.md) · [darkhorse_01_c5_v21](darkhorse_01_c5_v21.md) · [darkhorse_02_c4_v15](darkhorse_02_c4_v15.md) · [darkhorse_03_c5_v15](darkhorse_03_c5_v15.md) · [darkhorse_04_c4_v21](darkhorse_04_c4_v21.md) · [darkhorse_06_c4_v15](darkhorse_06_c4_v15.md) · [darkhorse_08_c5_v21](darkhorse_08_c5_v21.md) · [darkhorse_10_c5_v21](darkhorse_10_c5_v21.md) · [darkhorse_11_c5_v21](darkhorse_11_c5_v21.md) · [darkhorse_12_c5_v21](darkhorse_12_c5_v21.md) · [darkhorse_15_c5_v21](darkhorse_15_c5_v21.md) · [darkhorse_16_c4_v15](darkhorse_16_c4_v15.md) · [darkhorse_18_c4_v21](darkhorse_18_c4_v21.md) · [darkhorse_19_c4_v15](darkhorse_19_c4_v15.md) · [darkhorse_20_c5_v15](darkhorse_20_c5_v15.md)
