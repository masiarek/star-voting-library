# STAR vs Ranked Robin divergence — cycle_03_c5_v21 (STAR E, RR A)

*Generated from [`cycle_03_c5_v21.yaml`](../cycle_03_c5_v21.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** E

## Scenario

Auto-generated STAR-vs-Ranked-Robin divergence sample (cycle). 5 candidates, 21 voters, noise model. STAR elects E; Ranked Robin elects A; no Condorcet winner (cycle). See the [Divergence from STAR] block below for RCV-IRV, Approval and Plurality on the same ballots.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:A,B,C,D,E
1:5,0,5,3,4
1:1,0,0,0,5
1:2,2,5,0,5
1:1,2,5,4,0
1:0,5,1,4,0
1:3,2,0,5,1
1:4,1,0,5,3
1:0,2,5,0,2
1:0,3,2,1,5
1:2,3,0,5,3
1:4,2,0,5,4
1:1,0,5,0,0
1:5,4,3,0,2
1:2,4,0,5,5
1:0,0,0,5,5
1:2,5,3,0,2
1:4,5,1,2,0
1:0,4,1,4,5
1:5,5,0,4,5
1:5,4,1,1,0
1:5,0,0,3,2
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR                   = E
  Choose-One (Plurality) = D   (differs from STAR)
  RCV-IRV                = A   (differs from STAR)
  Approval               = D   (differs from STAR)
  RCV-RR                 = A   (differs from STAR)
  Note: 11 of 21 ballots (52%) had equal non-zero scores, so their ranks
        were decided by candidate priority order. The RCV-IRV result may be
        an artifact of score-to-rank tie-breaking rather than a deep
        difference.
  Note: Ranked Robin (RCV-RR) sides with RCV-IRV, so STAR is the outlier
        here — STAR need not elect the Condorcet candidate.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: star_vs_rr_divergence_tabulated/cycle_03_c5_v21_RCV-IRV_tabulated.txt
  RCV-RR round-robin: star_vs_rr_divergence_tabulated/cycle_03_c5_v21_RCV-RR_tabulated.txt

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 21 ballots.
A,B,C,D,E
5,0,5,3,4
1,0,0,0,5
2,2,5,0,5
1,2,5,4,0
0,5,1,4,0
3,2,0,5,1
4,1,0,5,3
0,2,5,0,2
0,3,2,1,5
2,3,0,5,3
4,2,0,5,4
1,0,5,0,0
5,4,3,0,2
2,4,0,5,5
0,0,0,5,5
2,5,3,0,2
4,5,1,2,0
0,4,1,4,5
5,5,0,4,5
5,4,1,1,0
5,0,0,3,2

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   E             -- 58 -- First place
   D             -- 56 -- Second place
   B             -- 53
   A             -- 51
   C             -- 37
 E and D advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   D             -- 9 -- Tied for first place
   E             -- 9 -- Tied for first place
   Equal Support -- 3
 There's a two-way tie for first.

[STAR Voting: Automatic Runoff Round: First tiebreaker]
 The highest-scoring candidate wins.
   E             -- 58 -- First place
   D             -- 56
 E wins.

[STAR Voting: Winner — STAR Voting Method (single winner)]
 E
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |       A      |      B      |      C      |    * D      |    * E      |
-----------------------------------------------------------------------------------------
             A > |     ---      | 9 -  3 -  9 |11 -  2 -  8 |10 -  1 - 10 | 9 -  4 -  8 |
             B > |  9 -  3 -  9 |    ---      |13 -  3 -  5 | 9 -  3 -  9 | 7 -  4 - 10 |
             C > |  8 -  2 - 11 | 5 -  3 - 13 |    ---      | 8 -  2 - 11 | 9 -  1 - 11 |
           * D > | 10 -  1 - 10 | 9 -  3 -  9 |11 -  2 -  8 |    ---      | 9 -  3 -  9 |
           * E > |  8 -  4 -  9 |10 -  4 -  7 |11 -  1 -  9 | 9 -  3 -  9 |    ---      |

[Condorcet Winner]
  No strict Condorcet winner; unbeaten candidates: A, D (pairwise ties)

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
A          5  3  1  4  3  5  |    51   2.4
B          4  4  2  5  1  5  |    53   2.5
C          5  0  2  1  4  9  |    37   1.8
D          6  4  2  1  2  6  |    56   2.7
E          7  2  2  4  1  5  |    58   2.8
```

Everything in one file: the [`_tabulated` mirror](../star_vs_rr_divergence_tabulated/cycle_03_c5_v21_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 05_Ranked_Robin/star_vs_rr_divergence/cycle_03_c5_v21.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [cycle_01_c5_v21](cycle_01_c5_v21.md) · [cycle_02_c5_v15](cycle_02_c5_v15.md) · [cycle_04_c5_v21](cycle_04_c5_v21.md) · [cycle_05_c5_v15](cycle_05_c5_v15.md) · [cycle_06_c4_v21](cycle_06_c4_v21.md) · [cycle_07_c4_v21](cycle_07_c4_v21.md) · [cycle_09_c3_v21](cycle_09_c3_v21.md) · [cycle_10_c4_v15](cycle_10_c4_v15.md) · [cycle_11_c4_v21](cycle_11_c4_v21.md) · [cycle_12_c3_v15](cycle_12_c3_v15.md) · [cycle_13_c5_v21](cycle_13_c5_v21.md) · [cycle_14_c3_v21](cycle_14_c3_v21.md) · [cycle_15_c5_v21](cycle_15_c5_v21.md) · [cycle_16_c3_v15](cycle_16_c3_v15.md) · [darkhorse_01_c5_v21](darkhorse_01_c5_v21.md) · [darkhorse_02_c4_v15](darkhorse_02_c4_v15.md) · [darkhorse_03_c5_v15](darkhorse_03_c5_v15.md) · [darkhorse_04_c4_v21](darkhorse_04_c4_v21.md) · [darkhorse_05_c5_v21](darkhorse_05_c5_v21.md) · [darkhorse_06_c4_v15](darkhorse_06_c4_v15.md) · [darkhorse_08_c5_v21](darkhorse_08_c5_v21.md) · [darkhorse_10_c5_v21](darkhorse_10_c5_v21.md) · [darkhorse_11_c5_v21](darkhorse_11_c5_v21.md) · [darkhorse_12_c5_v21](darkhorse_12_c5_v21.md) · [darkhorse_15_c5_v21](darkhorse_15_c5_v21.md) · [darkhorse_16_c4_v15](darkhorse_16_c4_v15.md) · [darkhorse_18_c4_v21](darkhorse_18_c4_v21.md) · [darkhorse_19_c4_v15](darkhorse_19_c4_v15.md) · [darkhorse_20_c5_v15](darkhorse_20_c5_v15.md)
