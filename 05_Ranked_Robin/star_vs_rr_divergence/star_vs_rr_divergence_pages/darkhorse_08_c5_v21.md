# STAR vs Ranked Robin divergence — darkhorse_08_c5_v21 (STAR C, RR D)

*Generated from [`darkhorse_08_c5_v21.yaml`](../darkhorse_08_c5_v21.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** C

## Scenario

Auto-generated STAR-vs-Ranked-Robin divergence sample (darkhorse). 5 candidates, 21 voters, faction2d model. STAR elects C; Ranked Robin elects D; Condorcet winner D. See the [Divergence from STAR] block below for RCV-IRV, Approval and Plurality on the same ballots.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:A,B,C,D,E
1:3,5,2,0,4
1:1,0,4,5,1
1:0,3,1,0,5
1:5,1,0,2,2
1:1,5,2,0,5
1:1,0,3,5,3
1:4,0,3,5,1
1:2,0,5,5,3
1:2,0,3,5,1
1:1,4,2,0,5
1:1,5,1,0,4
1:3,5,0,1,4
1:3,0,4,5,1
1:1,5,2,0,4
1:3,0,5,2,2
1:3,0,4,5,1
1:2,0,3,5,2
1:0,1,5,3,3
1:0,3,2,0,5
1:5,1,2,2,0
1:2,0,3,5,1
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR                   = C
  Choose-One (Plurality) = D   (differs from STAR)
  RCV-IRV                = D   (differs from STAR)
  RCV-RR (Condorcet)     = D   (differs from STAR)
  Note: 10 of 21 ballots (48%) had equal non-zero scores, so their ranks
        were decided by candidate priority order. The RCV-IRV result may be
        an artifact of score-to-rank tie-breaking rather than a deep
        difference.
  Note: Ranked Robin (RCV-RR) sides with RCV-IRV, so STAR is the outlier
        here — STAR need not elect the Condorcet candidate.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: star_vs_rr_divergence_tabulated/darkhorse_08_c5_v21_RCV-IRV_tabulated.txt
  RCV-RR round-robin: star_vs_rr_divergence_tabulated/darkhorse_08_c5_v21_RCV-RR_tabulated.txt

[Runoff Reversal]
 - Score Round Winner(s) = (E)
 - Runoff Round Winner   = (C)
  Candidate E earned the highest total score, but
  Candidate C won the automatic runoff — not a malfunction,
  STAR working as designed: the runoff elects the finalist preferred
  by the majority (of voters with a preference).

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 21 ballots.
Count x A,B,C,D,E
    2 x 2,0,3,5,1
    2 x 3,0,4,5,1
    1 x 3,5,2,0,4
    1 x 1,0,4,5,1
    1 x 0,3,1,0,5
    1 x 5,1,0,2,2
    1 x 1,5,2,0,5
    1 x 1,0,3,5,3
    1 x 4,0,3,5,1
    1 x 2,0,5,5,3
    1 x 1,4,2,0,5
    1 x 1,5,1,0,4
    1 x 3,5,0,1,4
    1 x 1,5,2,0,4
    1 x 3,0,5,2,2
    1 x 2,0,3,5,2
    1 x 0,1,5,3,3
    1 x 0,3,2,0,5
    1 x 5,1,2,2,0

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   E             -- 57 -- First place
   C             -- 56 -- Second place
   D             -- 55
   A             -- 43
   B             -- 38
 E and C advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   C             -- 11 -- First place
   E             --  9
   Equal Support --  1
 C wins.
   Runoff math:
     21  ballots cast
   −  1  Equal Support (no preference between the two finalists)
     ──
     20  voters with a preference  (majority = 11)
           C 11 (55%)  ·  E 9 (45%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 C
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |       A      |      B      |    * C      |      D      |    * E      |
-----------------------------------------------------------------------------------------
             A > |     ---      |12 -  0 -  9 | 5 -  1 - 15 | 9 -  2 - 10 | 8 -  2 - 11 |
             B > |  9 -  0 - 12 |    ---      | 9 -  0 - 12 | 8 -  0 - 13 | 5 -  1 - 15 |
           * C > | 15 -  1 -  5 |12 -  0 -  9 |    ---      | 9 -  2 - 10 |11 -  1 -  9 |
             D > | 10 -  2 -  9 |13 -  0 -  8 |10 -  2 -  9 |    ---      |10 -  3 -  8 |
           * E > | 11 -  2 -  8 |15 -  1 -  5 | 9 -  1 - 11 | 8 -  3 - 10 |    ---      |

[Condorcet Winner]
  Condorcet Winner: D — STAR elected C instead (D was eliminated in the scoring round)

[Score Distribution] (how many ballots gave each star rating)
                   Score
Candidate   5   4   3   2   1   0  | Total   Avg
A           2   1   5   4   6   3  |    43   2.0
B           5   1   2   0   3  10  |    38   1.8
C           3   3   5   6   2   2  |    56   2.7
D           9   0   1   3   1   7  |    55   2.6
E           4   4   3   3   6   1  |    57   2.7
```

Everything in one file: the [`_tabulated` mirror](../star_vs_rr_divergence_tabulated/darkhorse_08_c5_v21_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 05_Ranked_Robin/star_vs_rr_divergence/darkhorse_08_c5_v21.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [cycle_01_c5_v21](cycle_01_c5_v21.md) · [cycle_02_c5_v15](cycle_02_c5_v15.md) · [cycle_03_c5_v21](cycle_03_c5_v21.md) · [cycle_04_c5_v21](cycle_04_c5_v21.md) · [cycle_05_c5_v15](cycle_05_c5_v15.md) · [cycle_06_c4_v21](cycle_06_c4_v21.md) · [cycle_07_c4_v21](cycle_07_c4_v21.md) · [cycle_09_c3_v21](cycle_09_c3_v21.md) · [cycle_10_c4_v15](cycle_10_c4_v15.md) · [cycle_11_c4_v21](cycle_11_c4_v21.md) · [cycle_12_c3_v15](cycle_12_c3_v15.md) · [cycle_13_c5_v21](cycle_13_c5_v21.md) · [cycle_14_c3_v21](cycle_14_c3_v21.md) · [cycle_15_c5_v21](cycle_15_c5_v21.md) · [cycle_16_c3_v15](cycle_16_c3_v15.md) · [darkhorse_01_c5_v21](darkhorse_01_c5_v21.md) · [darkhorse_02_c4_v15](darkhorse_02_c4_v15.md) · [darkhorse_03_c5_v15](darkhorse_03_c5_v15.md) · [darkhorse_04_c4_v21](darkhorse_04_c4_v21.md) · [darkhorse_05_c5_v21](darkhorse_05_c5_v21.md) · [darkhorse_06_c4_v15](darkhorse_06_c4_v15.md) · [darkhorse_10_c5_v21](darkhorse_10_c5_v21.md) · [darkhorse_11_c5_v21](darkhorse_11_c5_v21.md) · [darkhorse_12_c5_v21](darkhorse_12_c5_v21.md) · [darkhorse_15_c5_v21](darkhorse_15_c5_v21.md) · [darkhorse_16_c4_v15](darkhorse_16_c4_v15.md) · [darkhorse_18_c4_v21](darkhorse_18_c4_v21.md) · [darkhorse_19_c4_v15](darkhorse_19_c4_v15.md) · [darkhorse_20_c5_v15](darkhorse_20_c5_v15.md)
