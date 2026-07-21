# STAR vs Ranked Robin divergence — cycle_01_c5_v21 (STAR D, RR C)

*Generated from [`cycle_01_c5_v21.yaml`](../cycle_01_c5_v21.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** D

## Scenario

Auto-generated STAR-vs-Ranked-Robin divergence sample (cycle). 5 candidates, 21 voters, noise model. STAR elects D; Ranked Robin elects C; no Condorcet winner (cycle). See the [Divergence from STAR] block below for RCV-IRV, Approval and Plurality on the same ballots.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:A,B,C,D,E
1:0,0,1,5,0
1:0,5,0,3,4
1:5,1,0,4,0
1:4,1,0,5,4
1:0,1,4,0,5
1:0,5,1,5,1
1:0,2,5,3,4
1:4,5,1,4,0
1:1,3,0,2,5
1:0,5,5,4,1
1:3,0,5,3,1
1:2,2,5,3,0
1:0,5,1,2,4
1:2,5,5,0,4
1:5,3,0,0,4
1:5,0,2,1,5
1:0,0,5,1,1
1:5,5,3,0,0
1:2,0,0,4,5
1:3,0,5,3,2
1:5,5,2,2,0
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR                   = D
  Choose-One (Plurality) = B   (differs from STAR)
  RCV-IRV                = B   (differs from STAR)
  RCV-RR                 = C   (differs from STAR)
  Note: 12 of 21 ballots (57%) had equal non-zero scores, so their ranks
        were decided by candidate priority order. The RCV-IRV result may be
        an artifact of score-to-rank tie-breaking rather than a deep
        difference.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: star_vs_rr_divergence_tabulated/cycle_01_c5_v21_RCV-IRV_tabulated.txt
  RCV-RR round-robin: star_vs_rr_divergence_tabulated/cycle_01_c5_v21_RCV-RR_tabulated.txt

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 21 ballots.
A,B,C,D,E
0,0,1,5,0
0,5,0,3,4
5,1,0,4,0
4,1,0,5,4
0,1,4,0,5
0,5,1,5,1
0,2,5,3,4
4,5,1,4,0
1,3,0,2,5
0,5,5,4,1
3,0,5,3,1
2,2,5,3,0
0,5,1,2,4
2,5,5,0,4
5,3,0,0,4
5,0,2,1,5
0,0,5,1,1
5,5,3,0,0
2,0,0,4,5
3,0,5,3,2
5,5,2,2,0

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   D             -- 54 -- First place
   B             -- 53 -- Second place
   C             -- 50
   E             -- 50
   A             -- 46
 D and B advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   B             -- 10 -- Tied for first place
   D             -- 10 -- Tied for first place
   Equal Support --  1
 There's a two-way tie for first.

[STAR Voting: Automatic Runoff Round: First tiebreaker]
 The highest-scoring candidate wins.
   D             -- 54 -- First place
   B             -- 53
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
                 |       A      |    * B      |      C      |    * D      |      E      |
-----------------------------------------------------------------------------------------
             A > |     ---      | 7 -  5 -  9 | 9 -  1 - 11 | 6 -  4 - 11 | 8 -  3 - 10 |
           * B > |  9 -  5 -  7 |    ---      |10 -  3 -  8 |10 -  1 - 10 |10 -  1 - 10 |
             C > | 11 -  1 -  9 | 8 -  3 - 10 |    ---      |10 -  2 -  9 |11 -  2 -  8 |
           * D > | 11 -  4 -  6 |10 -  1 - 10 | 9 -  2 - 10 |    ---      |10 -  2 -  9 |
             E > | 10 -  3 -  8 |10 -  1 - 10 | 8 -  2 - 11 | 9 -  2 - 10 |    ---      |

[Condorcet Winner]
  No strict Condorcet winner; weak Condorcet winner: B — STAR elected D instead

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
A          5  2  2  3  1  8  |    46   2.2
B          8  0  2  2  3  6  |    53   2.5
C          7  1  1  2  4  6  |    50   2.4
D          3  4  5  3  2  4  |    54   2.6
E          4  6  0  1  4  6  |    50   2.4
```

Everything in one file: the [`_tabulated` mirror](../star_vs_rr_divergence_tabulated/cycle_01_c5_v21_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 05_Ranked_Robin/star_vs_rr_divergence/cycle_01_c5_v21.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [cycle_02_c5_v15](cycle_02_c5_v15.md) · [cycle_03_c5_v21](cycle_03_c5_v21.md) · [cycle_04_c5_v21](cycle_04_c5_v21.md) · [cycle_05_c5_v15](cycle_05_c5_v15.md) · [cycle_06_c4_v21](cycle_06_c4_v21.md) · [cycle_07_c4_v21](cycle_07_c4_v21.md) · [cycle_09_c3_v21](cycle_09_c3_v21.md) · [cycle_10_c4_v15](cycle_10_c4_v15.md) · [cycle_11_c4_v21](cycle_11_c4_v21.md) · [cycle_12_c3_v15](cycle_12_c3_v15.md) · [cycle_13_c5_v21](cycle_13_c5_v21.md) · [cycle_14_c3_v21](cycle_14_c3_v21.md) · [cycle_15_c5_v21](cycle_15_c5_v21.md) · [cycle_16_c3_v15](cycle_16_c3_v15.md) · [darkhorse_01_c5_v21](darkhorse_01_c5_v21.md) · [darkhorse_02_c4_v15](darkhorse_02_c4_v15.md) · [darkhorse_03_c5_v15](darkhorse_03_c5_v15.md) · [darkhorse_04_c4_v21](darkhorse_04_c4_v21.md) · [darkhorse_05_c5_v21](darkhorse_05_c5_v21.md) · [darkhorse_06_c4_v15](darkhorse_06_c4_v15.md) · [darkhorse_08_c5_v21](darkhorse_08_c5_v21.md) · [darkhorse_10_c5_v21](darkhorse_10_c5_v21.md) · [darkhorse_11_c5_v21](darkhorse_11_c5_v21.md) · [darkhorse_12_c5_v21](darkhorse_12_c5_v21.md) · [darkhorse_15_c5_v21](darkhorse_15_c5_v21.md) · [darkhorse_16_c4_v15](darkhorse_16_c4_v15.md) · [darkhorse_18_c4_v21](darkhorse_18_c4_v21.md) · [darkhorse_19_c4_v15](darkhorse_19_c4_v15.md) · [darkhorse_20_c5_v15](darkhorse_20_c5_v15.md)
