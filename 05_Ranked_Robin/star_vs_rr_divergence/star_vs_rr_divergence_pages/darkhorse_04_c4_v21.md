# STAR vs Ranked Robin divergence — darkhorse_04_c4_v21 (STAR D, RR A)

*Generated from [`darkhorse_04_c4_v21.yaml`](../darkhorse_04_c4_v21.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** D

## Scenario

Auto-generated STAR-vs-Ranked-Robin divergence sample (darkhorse). 4 candidates, 21 voters, spatial2d model. STAR elects D; Ranked Robin elects A; Condorcet winner A. See the [Divergence from STAR] block below for RCV-IRV, Approval and Plurality on the same ballots.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:A,B,C,D
1:5,3,0,4
1:5,3,0,4
1:5,4,0,5
1:5,3,0,5
1:0,5,3,2
1:3,5,0,4
1:5,3,0,4
1:3,5,0,5
1:0,5,5,2
1:5,4,0,4
1:5,3,0,4
1:5,2,0,5
1:0,5,0,2
1:5,4,0,4
1:5,2,0,4
1:5,5,0,5
1:5,2,0,4
1:5,3,0,4
1:0,3,5,3
1:3,5,0,4
1:0,5,4,0
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR                   = D
  Choose-One (Plurality) = A   (differs from STAR)
  RCV-IRV                = A   (differs from STAR)
  Approval               = B   (differs from STAR)
  RCV-RR (Condorcet)     = A   (differs from STAR)
  Note: 9 of 21 ballots (43%) had equal non-zero scores, so their ranks were
        decided by candidate priority order. The RCV-IRV result may be an
        artifact of score-to-rank tie-breaking rather than a deep
        difference.
  Note: Ranked Robin (RCV-RR) sides with RCV-IRV, so STAR is the outlier
        here — STAR need not elect the Condorcet candidate.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: star_vs_rr_divergence_tabulated/darkhorse_04_c4_v21_RCV-IRV_tabulated.txt
  RCV-RR round-robin: star_vs_rr_divergence_tabulated/darkhorse_04_c4_v21_RCV-RR_tabulated.txt

[Runoff Reversal]
 - Score Round Winner(s) = (B)
 - Runoff Round Winner   = (D)
  Candidate B earned the highest total score, but
  Candidate D won the automatic runoff — not a malfunction,
  STAR working as designed: the runoff elects the finalist preferred
  by the majority (of voters with a preference).

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 21 ballots.
Count x A,B,C,D
    5 x 5,3,0,4
    2 x 3,5,0,4
    2 x 5,4,0,4
    2 x 5,2,0,4
    1 x 5,4,0,5
    1 x 5,3,0,5
    1 x 0,5,3,2
    1 x 3,5,0,5
    1 x 0,5,5,2
    1 x 5,2,0,5
    1 x 0,5,0,2
    1 x 5,5,0,5
    1 x 0,3,5,3
    1 x 0,5,4,0

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   B             -- 79 -- First place
   D             -- 78 -- Second place
   A             -- 74
   C             -- 17
 B and D advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   D             -- 10 -- First place
   B             --  6
   Equal Support --  5
 D wins.
   Runoff math:
     21  ballots cast
   −  5  Equal Support (no preference between the two finalists)
     ──
     16  voters with a preference  (majority = 9)
           D 10 (62%)  ·  B 6 (38%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 D
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |       A      |    * B      |      C      |    * D      |
---------------------------------------------------------------------------
             A > |     ---      |12 -  1 -  8 |16 -  1 -  4 | 9 -  5 -  7 |
           * B > |  8 -  1 - 12 |    ---      |19 -  1 -  1 | 6 -  5 - 10 |
             C > |  4 -  1 - 16 | 1 -  1 - 19 |    ---      | 4 -  0 - 17 |
           * D > |  7 -  5 -  9 |10 -  5 -  6 |17 -  0 -  4 |    ---      |

[Condorcet Winner]
  Condorcet Winner: A — STAR elected D instead (A was eliminated in the scoring round)

[Score Distribution] (how many ballots gave each star rating)
                   Score
Candidate   5   4   3   2   1   0  | Total   Avg
A          13   0   3   0   0   5  |    74   3.5
B           8   3   7   3   0   0  |    79   3.8
C           2   1   1   0   0  17  |    17   0.8
D           5  11   1   3   0   1  |    78   3.7
```

Everything in one file: the [`_tabulated` mirror](../star_vs_rr_divergence_tabulated/darkhorse_04_c4_v21_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 05_Ranked_Robin/star_vs_rr_divergence/darkhorse_04_c4_v21.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [cycle_01_c5_v21](cycle_01_c5_v21.md) · [cycle_02_c5_v15](cycle_02_c5_v15.md) · [cycle_03_c5_v21](cycle_03_c5_v21.md) · [cycle_04_c5_v21](cycle_04_c5_v21.md) · [cycle_05_c5_v15](cycle_05_c5_v15.md) · [cycle_06_c4_v21](cycle_06_c4_v21.md) · [cycle_07_c4_v21](cycle_07_c4_v21.md) · [cycle_09_c3_v21](cycle_09_c3_v21.md) · [cycle_10_c4_v15](cycle_10_c4_v15.md) · [cycle_11_c4_v21](cycle_11_c4_v21.md) · [cycle_12_c3_v15](cycle_12_c3_v15.md) · [cycle_13_c5_v21](cycle_13_c5_v21.md) · [cycle_14_c3_v21](cycle_14_c3_v21.md) · [cycle_15_c5_v21](cycle_15_c5_v21.md) · [cycle_16_c3_v15](cycle_16_c3_v15.md) · [darkhorse_01_c5_v21](darkhorse_01_c5_v21.md) · [darkhorse_02_c4_v15](darkhorse_02_c4_v15.md) · [darkhorse_03_c5_v15](darkhorse_03_c5_v15.md) · [darkhorse_05_c5_v21](darkhorse_05_c5_v21.md) · [darkhorse_06_c4_v15](darkhorse_06_c4_v15.md) · [darkhorse_08_c5_v21](darkhorse_08_c5_v21.md) · [darkhorse_10_c5_v21](darkhorse_10_c5_v21.md) · [darkhorse_11_c5_v21](darkhorse_11_c5_v21.md) · [darkhorse_12_c5_v21](darkhorse_12_c5_v21.md) · [darkhorse_15_c5_v21](darkhorse_15_c5_v21.md) · [darkhorse_16_c4_v15](darkhorse_16_c4_v15.md) · [darkhorse_18_c4_v21](darkhorse_18_c4_v21.md) · [darkhorse_19_c4_v15](darkhorse_19_c4_v15.md) · [darkhorse_20_c5_v15](darkhorse_20_c5_v15.md)
