# STAR vs Ranked Robin divergence — cycle_02_c5_v15 (STAR D, RR C)

*Generated from [`cycle_02_c5_v15.yaml`](../cycle_02_c5_v15.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** D

## Scenario

Auto-generated STAR-vs-Ranked-Robin divergence sample (cycle). 5 candidates, 15 voters, faction2d model. STAR elects D; Ranked Robin elects C; no Condorcet winner (cycle). See the [Divergence from STAR] block below for RCV-IRV, Approval and Plurality on the same ballots.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:A,B,C,D,E
1:1,0,5,4,2
1:1,0,4,3,5
1:2,0,5,5,2
1:2,0,5,5,2
1:2,0,3,5,0
1:1,0,4,4,5
1:1,0,4,5,2
1:1,0,5,4,5
1:2,0,4,5,1
1:2,0,4,5,2
1:2,0,5,4,2
1:2,0,5,5,2
1:1,0,5,5,5
1:2,0,5,5,2
1:1,0,5,5,2
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR                   = D
  Choose-One (Plurality) = C   (differs from STAR)
  RCV-IRV                = C   (differs from STAR)
  Approval               = C   (differs from STAR)
  RCV-RR                 = C   (differs from STAR)
  Note: 10 of 15 ballots (67%) had equal non-zero scores, so their ranks
        were decided by candidate priority order. The RCV-IRV result may be
        an artifact of score-to-rank tie-breaking rather than a deep
        difference.
  Note: Ranked Robin (RCV-RR) sides with RCV-IRV, so STAR is the outlier
        here — STAR need not elect the Condorcet candidate.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: star_vs_rr_divergence_tabulated/cycle_02_c5_v15_RCV-IRV_tabulated.txt
  RCV-RR round-robin: star_vs_rr_divergence_tabulated/cycle_02_c5_v15_RCV-RR_tabulated.txt

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 15 ballots.
Count x A,B,C,D,E
    4 x 2,0,5,5,2
    1 x 1,0,5,4,2
    1 x 1,0,4,3,5
    1 x 2,0,3,5,0
    1 x 1,0,4,4,5
    1 x 1,0,4,5,2
    1 x 1,0,5,4,5
    1 x 2,0,4,5,1
    1 x 2,0,4,5,2
    1 x 2,0,5,4,2
    1 x 1,0,5,5,5
    1 x 1,0,5,5,2

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   D             -- 69 -- First place
   C             -- 68 -- Second place
   E             -- 39
   A             -- 23
   B             --  0
 D and C advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   C             -- 4 -- Tied for first place
   D             -- 4 -- Tied for first place
   Equal Support -- 7
 There's a two-way tie for first.

[STAR Voting: Automatic Runoff Round: First tiebreaker]
 The highest-scoring candidate wins.
   D             -- 69 -- First place
   C             -- 68
 D wins.

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
             A > |     ---      |15 -  0 -  0 | 0 -  0 - 15 | 0 -  0 - 15 | 2 -  6 -  7 |
             B > |  0 -  0 - 15 |    ---      | 0 -  0 - 15 | 0 -  0 - 15 | 0 -  1 - 14 |
           * C > | 15 -  0 -  0 |15 -  0 -  0 |    ---      | 4 -  7 -  4 |11 -  2 -  2 |
           * D > | 15 -  0 -  0 |15 -  0 -  0 | 4 -  7 -  4 |    ---      |11 -  1 -  3 |
             E > |  7 -  6 -  2 |14 -  1 -  0 | 2 -  2 - 11 | 3 -  1 - 11 |    ---      |

[Condorcet Winner]
  No strict Condorcet winner; unbeaten candidates: C, D (pairwise ties)

[Score Distribution] (how many ballots gave each star rating)
                   Score
Candidate   5   4   3   2   1   0  | Total   Avg
A           0   0   0   8   7   0  |    23   1.5
B           0   0   0   0   0  15  |     0   0.0
C           9   5   1   0   0   0  |    68   4.5
D          10   4   1   0   0   0  |    69   4.6
E           4   0   0   9   1   1  |    39   2.6
```

Everything in one file: the [`_tabulated` mirror](../star_vs_rr_divergence_tabulated/cycle_02_c5_v15_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 05_Ranked_Robin/star_vs_rr_divergence/cycle_02_c5_v15.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [cycle_01_c5_v21](cycle_01_c5_v21.md) · [cycle_03_c5_v21](cycle_03_c5_v21.md) · [cycle_04_c5_v21](cycle_04_c5_v21.md) · [cycle_05_c5_v15](cycle_05_c5_v15.md) · [cycle_06_c4_v21](cycle_06_c4_v21.md) · [cycle_07_c4_v21](cycle_07_c4_v21.md) · [cycle_09_c3_v21](cycle_09_c3_v21.md) · [cycle_10_c4_v15](cycle_10_c4_v15.md) · [cycle_11_c4_v21](cycle_11_c4_v21.md) · [cycle_12_c3_v15](cycle_12_c3_v15.md) · [cycle_13_c5_v21](cycle_13_c5_v21.md) · [cycle_14_c3_v21](cycle_14_c3_v21.md) · [cycle_15_c5_v21](cycle_15_c5_v21.md) · [cycle_16_c3_v15](cycle_16_c3_v15.md) · [darkhorse_01_c5_v21](darkhorse_01_c5_v21.md) · [darkhorse_02_c4_v15](darkhorse_02_c4_v15.md) · [darkhorse_03_c5_v15](darkhorse_03_c5_v15.md) · [darkhorse_04_c4_v21](darkhorse_04_c4_v21.md) · [darkhorse_05_c5_v21](darkhorse_05_c5_v21.md) · [darkhorse_06_c4_v15](darkhorse_06_c4_v15.md) · [darkhorse_08_c5_v21](darkhorse_08_c5_v21.md) · [darkhorse_10_c5_v21](darkhorse_10_c5_v21.md) · [darkhorse_11_c5_v21](darkhorse_11_c5_v21.md) · [darkhorse_12_c5_v21](darkhorse_12_c5_v21.md) · [darkhorse_15_c5_v21](darkhorse_15_c5_v21.md) · [darkhorse_16_c4_v15](darkhorse_16_c4_v15.md) · [darkhorse_18_c4_v21](darkhorse_18_c4_v21.md) · [darkhorse_19_c4_v15](darkhorse_19_c4_v15.md) · [darkhorse_20_c5_v15](darkhorse_20_c5_v15.md)
