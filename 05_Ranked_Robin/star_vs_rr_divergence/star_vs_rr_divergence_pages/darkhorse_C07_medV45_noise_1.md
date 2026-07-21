# STAR vs RR divergence -- 7 cands, 45 voters, darkhorse (STAR E, RR A)

*Generated from [`darkhorse_C07_medV45_noise_1.yaml`](../darkhorse_C07_medV45_noise_1.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** E

## Scenario

Auto-generated STAR-vs-Ranked-Robin divergence. 7 candidates, 45 voters, ungrouped (independent random ballots). STAR elects E; Ranked Robin elects A. CAUSE = DARK HORSE: A is the Condorcet winner (beats every rival head-to-head) but only #3 of 7 by score total (111 vs leader E 122) -- a broadly-liked, low-intensity compromise that misses STAR's score finalists (E, G). STAR elects runoff winner E; RR elects the Condorcet winner A. Preference-vs-support: RR rewards ORDER, STAR rewards SUPPORT strength. See the [Divergence from STAR] block below for RCV-IRV, Approval and Plurality on the same ballots.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:A,B,C,D,E,F,G
1:3,1,3,5,3,0,3
1:5,1,0,0,0,2,2
1:3,2,4,4,2,2,2
1:4,1,0,2,2,1,1
1:2,2,2,2,1,4,1
1:2,1,3,1,1,4,4
1:3,1,1,3,5,3,3
1:4,3,1,1,1,5,3
1:1,4,0,2,3,4,3
1:4,0,3,4,2,1,5
1:3,1,4,3,4,2,1
1:4,3,2,3,3,1,2
1:0,5,1,4,3,0,4
1:1,2,4,5,4,5,4
1:0,3,4,3,4,2,5
1:5,1,1,2,0,2,3
1:0,4,4,0,4,1,4
1:5,1,2,5,2,4,2
1:1,0,2,3,3,4,1
1:3,4,3,1,3,1,5
1:5,1,4,1,4,2,4
1:2,3,3,0,2,0,2
1:0,0,3,2,3,1,1
1:4,1,2,1,3,2,4
1:3,4,1,4,2,0,2
1:4,1,0,2,3,4,2
1:2,4,4,5,0,5,3
1:2,5,1,3,1,3,0
1:2,1,1,1,4,3,1
1:1,0,1,1,1,1,0
1:0,1,1,2,4,3,4
1:2,0,4,2,5,4,4
1:3,4,1,2,2,2,0
1:4,1,3,2,2,0,4
1:1,4,0,2,4,1,3
1:1,0,5,1,3,4,2
1:1,0,5,5,1,1,3
1:4,4,2,3,2,4,1
1:1,3,1,4,3,1,4
1:1,1,1,1,5,3,3
1:4,1,2,1,4,2,1
1:5,0,4,2,4,3,3
1:0,1,0,1,3,0,0
1:4,2,3,4,5,3,4
1:2,3,1,0,2,3,2
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR                   = E
  Choose-One (Plurality) = A   (differs from STAR)
  RCV-IRV                = A   (differs from STAR)
  RCV-RR (Condorcet)     = A   (differs from STAR)
  Note: 45 of 45 ballots (100%) had equal non-zero scores, so their ranks
        were decided by candidate priority order. The RCV-IRV result may be
        an artifact of score-to-rank tie-breaking rather than a deep
        difference.
  Note: Ranked Robin (RCV-RR) sides with RCV-IRV, so STAR is the outlier
        here — STAR need not elect the Condorcet candidate.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: star_vs_rr_divergence_tabulated/darkhorse_C07_medV45_noise_1_RCV-IRV_tabulated.txt
  RCV-RR round-robin: star_vs_rr_divergence_tabulated/darkhorse_C07_medV45_noise_1_RCV-RR_tabulated.txt

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 45 ballots.
A,B,C,D,E,F,G
3,1,3,5,3,0,3
5,1,0,0,0,2,2
3,2,4,4,2,2,2
4,1,0,2,2,1,1
2,2,2,2,1,4,1
2,1,3,1,1,4,4
3,1,1,3,5,3,3
4,3,1,1,1,5,3
1,4,0,2,3,4,3
4,0,3,4,2,1,5
3,1,4,3,4,2,1
4,3,2,3,3,1,2
0,5,1,4,3,0,4
1,2,4,5,4,5,4
0,3,4,3,4,2,5
5,1,1,2,0,2,3
0,4,4,0,4,1,4
5,1,2,5,2,4,2
1,0,2,3,3,4,1
3,4,3,1,3,1,5
5,1,4,1,4,2,4
2,3,3,0,2,0,2
0,0,3,2,3,1,1
4,1,2,1,3,2,4
3,4,1,4,2,0,2
4,1,0,2,3,4,2
2,4,4,5,0,5,3
2,5,1,3,1,3,0
2,1,1,1,4,3,1
1,0,1,1,1,1,0
0,1,1,2,4,3,4
2,0,4,2,5,4,4
3,4,1,2,2,2,0
4,1,3,2,2,0,4
1,4,0,2,4,1,3
1,0,5,1,3,4,2
1,0,5,5,1,1,3
4,4,2,3,2,4,1
1,3,1,4,3,1,4
1,1,1,1,5,3,3
4,1,2,1,4,2,1
5,0,4,2,4,3,3
0,1,0,1,3,0,0
4,2,3,4,5,3,4
2,3,1,0,2,3,2

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   E             -- 122 -- First place
   G             -- 115 -- Second place
   A             -- 111
   D             -- 105
   F             -- 103
   C             --  97
   B             --  85
 E and G advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   E             -- 20 -- First place
   G             -- 13
   Equal Support -- 12
 E wins.
   Runoff math:
     45  ballots cast
   − 12  Equal Support (no preference between the two finalists)
     ──
     33  voters with a preference  (majority = 17)
           E 20 (61%)  ·  G 13 (39%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 E
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |       A      |      B      |      C      |      D      |    * E      |      F      |    * G      |
---------------------------------------------------------------------------------------------------------------------
             A > |     ---      |25 -  4 - 16 |23 -  7 - 15 |18 - 11 - 16 |20 -  7 - 18 |19 -  9 - 17 |19 -  9 - 17 |
             B > | 16 -  4 - 25 |    ---      |16 -  9 - 20 |12 - 11 - 22 |14 -  6 - 25 |14 -  5 - 26 |13 -  8 - 24 |
             C > | 15 -  7 - 23 |20 -  9 - 16 |    ---      |15 -  8 - 22 |10 - 15 - 20 |17 -  7 - 21 |15 -  9 - 21 |
             D > | 16 - 11 - 18 |22 - 11 - 12 |22 -  8 - 15 |    ---      |14 -  9 - 22 |17 -  9 - 19 |18 -  7 - 20 |
           * E > | 18 -  7 - 20 |25 -  6 - 14 |20 - 15 - 10 |22 -  9 - 14 |    ---      |26 -  4 - 15 |20 - 12 - 13 |
             F > | 17 -  9 - 19 |26 -  5 - 14 |21 -  7 - 17 |19 -  9 - 17 |15 -  4 - 26 |    ---      |17 - 10 - 18 |
           * G > | 17 -  9 - 19 |24 -  8 - 13 |21 -  9 - 15 |20 -  7 - 18 |13 - 12 - 20 |18 - 10 - 17 |    ---      |

[Condorcet Winner]
  Condorcet Winner: A — STAR elected E instead (A was eliminated in the scoring round)

[Score Distribution] (how many ballots gave each star rating)
                   Score
Candidate   5   4   3   2   1   0  | Total   Avg
A           5  10   7   8   9   6  |   111   2.5
B           2   8   6   4  17   8  |    85   1.9
C           2   9   8   7  13   6  |    97   2.2
D           5   6   7  12  11   4  |   105   2.3
E           4  10  12  10   6   3  |   122   2.7
F           3   9   8   9  10   6  |   103   2.3
G           3  11  10   9   8   4  |   115   2.6
```

Everything in one file: the [`_tabulated` mirror](../star_vs_rr_divergence_tabulated/darkhorse_C07_medV45_noise_1_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 05_Ranked_Robin/star_vs_rr_divergence/darkhorse_C07_medV45_noise_1.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README.md)
- [Runoff reversal (worked set)](../../../01_STAR/runoff_overturns_leader/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [cycle_C03_fewV15_noise_1](cycle_C03_fewV15_noise_1.md) · [cycle_C03_fewV15_noise_2](cycle_C03_fewV15_noise_2.md) · [cycle_C03_medV45_noise_1](cycle_C03_medV45_noise_1.md) · [cycle_C03_medV45_noise_2](cycle_C03_medV45_noise_2.md) · [cycle_C05_fewV15_noise_1](cycle_C05_fewV15_noise_1.md) · [cycle_C05_fewV15_noise_2](cycle_C05_fewV15_noise_2.md) · [cycle_C05_fewV28_bloc_1](cycle_C05_fewV28_bloc_1.md) · [cycle_C05_medV45_noise_1](cycle_C05_medV45_noise_1.md) · [cycle_C05_medV45_noise_2](cycle_C05_medV45_noise_2.md) · [cycle_C07_fewV15_noise_1](cycle_C07_fewV15_noise_1.md) · [cycle_C07_fewV28_bloc_2](cycle_C07_fewV28_bloc_2.md) · [cycle_C07_largeV598_bloc_1](cycle_C07_largeV598_bloc_1.md) · [cycle_C07_medV149_bloc_2](cycle_C07_medV149_bloc_2.md) · [cycle_C10_fewV15_noise_1](cycle_C10_fewV15_noise_1.md) · [cycle_C10_fewV15_noise_2](cycle_C10_fewV15_noise_2.md) · [cycle_C10_fewV28_bloc_1](cycle_C10_fewV28_bloc_1.md) · [cycle_C10_fewV29_bloc_2](cycle_C10_fewV29_bloc_2.md) · [cycle_C10_medV148_bloc_1](cycle_C10_medV148_bloc_1.md) · [cycle_C10_medV149_bloc_2](cycle_C10_medV149_bloc_2.md) · [cycle_C10_medV45_noise_1](cycle_C10_medV45_noise_1.md) · [cycle_C10_medV45_noise_2](cycle_C10_medV45_noise_2.md) · [darkhorse_C03_fewV15_noise_1](darkhorse_C03_fewV15_noise_1.md) · [darkhorse_C05_largeV599_bloc_1](darkhorse_C05_largeV599_bloc_1.md) · [darkhorse_C07_fewV30_bloc_1](darkhorse_C07_fewV30_bloc_1.md) · [darkhorse_C07_largeV597_bloc_1](darkhorse_C07_largeV597_bloc_1.md) · [darkhorse_C07_largeV598_bloc_2](darkhorse_C07_largeV598_bloc_2.md) · [darkhorse_C07_medV147_bloc_1](darkhorse_C07_medV147_bloc_1.md) · [darkhorse_C10_largeV598_bloc_1](darkhorse_C10_largeV598_bloc_1.md) · [darkhorse_C10_largeV599_bloc_2](darkhorse_C10_largeV599_bloc_2.md)
