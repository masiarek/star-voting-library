# STAR vs RR divergence -- 10 cands, 45 voters, cycle (STAR A, RR I)

*Generated from [`cycle_C10_medV45_noise_2.yaml`](../cycle_C10_medV45_noise_2.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** A

## Scenario

Auto-generated STAR-vs-Ranked-Robin divergence. 10 candidates, 45 voters, ungrouped (independent random ballots). STAR elects A; Ranked Robin elects I. CAUSE = CONDORCET CYCLE: no candidate beats all others (D>F>H>D), so there is no 'right' winner. RR falls back on Copeland/margin (I); STAR runs its two score-leaders off (A). See the [Divergence from STAR] block below for RCV-IRV, Approval and Plurality on the same ballots.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:A,B,C,D,E,F,G,H,I,J
1:0,2,2,2,4,1,2,1,2,4
1:3,3,2,1,4,2,2,5,5,4
1:3,3,5,4,1,1,0,3,3,2
1:5,1,3,1,3,4,1,3,2,3
1:5,4,4,0,3,5,2,2,4,3
1:3,1,2,3,5,3,1,2,5,5
1:2,5,5,1,1,4,4,3,4,1
1:4,4,2,4,1,0,4,0,3,2
1:2,2,5,5,2,1,3,1,3,3
1:3,3,5,0,5,2,1,2,5,4
1:4,0,1,3,3,1,3,1,2,4
1:1,2,4,2,0,2,5,5,3,2
1:1,4,3,2,2,0,3,2,1,2
1:0,2,4,3,5,1,3,1,2,2
1:3,3,0,3,5,4,3,2,1,2
1:4,1,5,4,2,0,5,4,3,2
1:0,1,4,3,5,1,2,4,3,5
1:3,2,0,1,1,5,2,2,3,5
1:5,4,0,0,2,0,2,2,2,1
1:5,4,3,4,4,2,2,2,3,5
1:3,0,4,0,0,3,5,1,1,1
1:1,3,3,5,3,4,2,3,4,2
1:3,4,0,1,3,4,5,4,1,4
1:1,0,3,1,3,1,3,5,2,4
1:1,2,2,2,5,2,1,4,2,2
1:4,3,1,2,0,2,4,3,5,1
1:2,2,2,2,2,4,4,3,5,1
1:4,4,3,4,3,1,4,4,1,2
1:5,2,3,0,2,4,3,0,1,5
1:3,0,1,5,4,1,4,1,2,4
1:2,1,2,5,1,2,2,1,3,2
1:4,2,1,2,3,5,3,2,4,1
1:2,1,4,1,2,4,4,2,2,1
1:5,1,4,1,4,3,3,0,4,2
1:4,0,0,3,0,3,5,5,1,1
1:1,2,2,4,1,3,4,1,2,1
1:2,0,3,5,4,3,2,1,0,0
1:1,5,4,2,3,4,1,3,4,3
1:3,5,1,2,2,4,3,4,2,1
1:4,0,3,2,2,0,2,3,1,1
1:0,0,4,1,2,2,4,2,4,3
1:5,4,3,5,0,2,1,1,4,4
1:2,0,3,4,5,2,1,1,4,5
1:3,3,0,5,3,4,2,2,0,1
1:3,2,4,3,3,0,1,5,4,5
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR   = A
  RCV-RR = I   (differs from STAR)
  Full round-by-round reports (generated for review):
  RCV-RR round-robin: star_vs_rr_divergence_tabulated/cycle_C10_medV45_noise_2_RCV-RR_tabulated.txt

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 45 ballots.
A,B,C,D,E,F,G,H,I,J
0,2,2,2,4,1,2,1,2,4
3,3,2,1,4,2,2,5,5,4
3,3,5,4,1,1,0,3,3,2
5,1,3,1,3,4,1,3,2,3
5,4,4,0,3,5,2,2,4,3
3,1,2,3,5,3,1,2,5,5
2,5,5,1,1,4,4,3,4,1
4,4,2,4,1,0,4,0,3,2
2,2,5,5,2,1,3,1,3,3
3,3,5,0,5,2,1,2,5,4
4,0,1,3,3,1,3,1,2,4
1,2,4,2,0,2,5,5,3,2
1,4,3,2,2,0,3,2,1,2
0,2,4,3,5,1,3,1,2,2
3,3,0,3,5,4,3,2,1,2
4,1,5,4,2,0,5,4,3,2
0,1,4,3,5,1,2,4,3,5
3,2,0,1,1,5,2,2,3,5
5,4,0,0,2,0,2,2,2,1
5,4,3,4,4,2,2,2,3,5
3,0,4,0,0,3,5,1,1,1
1,3,3,5,3,4,2,3,4,2
3,4,0,1,3,4,5,4,1,4
1,0,3,1,3,1,3,5,2,4
1,2,2,2,5,2,1,4,2,2
4,3,1,2,0,2,4,3,5,1
2,2,2,2,2,4,4,3,5,1
4,4,3,4,3,1,4,4,1,2
5,2,3,0,2,4,3,0,1,5
3,0,1,5,4,1,4,1,2,4
2,1,2,5,1,2,2,1,3,2
4,2,1,2,3,5,3,2,4,1
2,1,4,1,2,4,4,2,2,1
5,1,4,1,4,3,3,0,4,2
4,0,0,3,0,3,5,5,1,1
1,2,2,4,1,3,4,1,2,1
2,0,3,5,4,3,2,1,0,0
1,5,4,2,3,4,1,3,4,3
3,5,1,2,2,4,3,4,2,1
4,0,3,2,2,0,2,3,1,1
0,0,4,1,2,2,4,2,4,3
5,4,3,5,0,2,1,1,4,4
2,0,3,4,5,2,1,1,4,5
3,3,0,5,3,4,2,2,0,1
3,2,4,3,3,0,1,5,4,5

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   A             -- 124 -- First place
   G             -- 123 -- Second place
   I             -- 122
   C             -- 119
   E             -- 118
   J             -- 118
   D             -- 113
   H             -- 108
   F             -- 106
   B             --  97
 A and G advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   A             -- 18 -- Tied for first place
   G             -- 18 -- Tied for first place
   Equal Support --  9
 There's a two-way tie for first.

[STAR Voting: Automatic Runoff Round: First tiebreaker]
 The highest-scoring candidate wins.
   A             -- 124 -- First place
   G             -- 123
 A wins.

[STAR Voting: Winner — STAR Voting Method (single winner)]
 A
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |     * A      |      B      |      C      |      D      |      E      |      F      |    * G      |      H      |      I      |      J      |
---------------------------------------------------------------------------------------------------------------------------------------------------------------
           * A > |     ---      |23 - 10 - 12 |22 -  2 - 21 |19 -  9 - 17 |22 -  7 - 16 |20 -  6 - 19 |18 -  9 - 18 |23 -  5 - 17 |20 -  5 - 20 |21 -  5 - 19 |
             B > | 12 - 10 - 23 |    ---      |15 -  8 - 22 |12 - 13 - 20 |15 -  9 - 21 |18 -  5 - 22 |15 -  7 - 23 |18 -  8 - 19 |12 -  8 - 25 |16 -  7 - 22 |
             C > | 21 -  2 - 22 |22 -  8 - 15 |    ---      |20 -  5 - 20 |19 -  8 - 18 |21 -  9 - 15 |19 -  9 - 17 |22 -  7 - 16 |16 - 11 - 18 |20 -  7 - 18 |
             D > | 17 -  9 - 19 |20 - 13 - 12 |20 -  5 - 20 |    ---      |15 - 10 - 20 |21 -  7 - 17 |15 -  9 - 21 |18 -  5 - 22 |19 -  6 - 20 |20 -  5 - 20 |
             E > | 16 -  7 - 22 |21 -  9 - 15 |18 -  8 - 19 |20 - 10 - 15 |    ---      |23 -  2 - 20 |19 -  6 - 20 |19 -  9 - 17 |18 -  6 - 21 |15 - 13 - 17 |
             F > | 19 -  6 - 20 |22 -  5 - 18 |15 -  9 - 21 |17 -  7 - 21 |20 -  2 - 23 |    ---      |17 -  7 - 21 |20 - 11 - 14 |14 -  5 - 26 |17 -  5 - 23 |
           * G > | 18 -  9 - 18 |23 -  7 - 15 |17 -  9 - 19 |21 -  9 - 15 |20 -  6 - 19 |21 -  7 - 17 |    ---      |22 - 10 - 13 |20 -  5 - 20 |23 -  4 - 18 |
             H > | 17 -  5 - 23 |19 -  8 - 18 |16 -  7 - 22 |22 -  5 - 18 |17 -  9 - 19 |14 - 11 - 20 |13 - 10 - 22 |    ---      |16 -  5 - 24 |19 -  8 - 18 |
             I > | 20 -  5 - 20 |25 -  8 - 12 |18 - 11 - 16 |20 -  6 - 19 |21 -  6 - 18 |26 -  5 - 14 |20 -  5 - 20 |24 -  5 - 16 |    ---      |20 -  9 - 16 |
             J > | 19 -  5 - 21 |22 -  7 - 16 |18 -  7 - 20 |20 -  5 - 20 |17 - 13 - 15 |23 -  5 - 17 |18 -  4 - 23 |18 -  8 - 19 |16 -  9 - 20 |    ---      |

[Condorcet Winner]
  No strict Condorcet winner; unbeaten candidates: A, I (pairwise ties)

[Score Distribution] (how many ballots gave each star rating)
                   Score
Candidate   5   4   3   2   1   0  | Total   Avg
A           7   8  12   7   7   4  |   124   2.8
B           3   8   7  11   7   9  |    97   2.2
C           5  10  11   8   5   6  |   119   2.6
D           7   7   7  10   9   5  |   113   2.5
E           7   6  11  10   6   5  |   118   2.6
F           3  11   6  10   9   6  |   106   2.4
G           5   9  10  12   8   1  |   123   2.7
H           5   6   8  12  11   3  |   108   2.4
I           5  10   9  11   8   2  |   122   2.7
J           7   8   5  12  12   1  |   118   2.6
```

Everything in one file: the [`_tabulated` mirror](../star_vs_rr_divergence_tabulated/cycle_C10_medV45_noise_2_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 05_Ranked_Robin/star_vs_rr_divergence/cycle_C10_medV45_noise_2.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [cycle_C03_fewV15_noise_1](cycle_C03_fewV15_noise_1.md) · [cycle_C03_fewV15_noise_2](cycle_C03_fewV15_noise_2.md) · [cycle_C03_medV45_noise_1](cycle_C03_medV45_noise_1.md) · [cycle_C03_medV45_noise_2](cycle_C03_medV45_noise_2.md) · [cycle_C05_fewV15_noise_1](cycle_C05_fewV15_noise_1.md) · [cycle_C05_fewV15_noise_2](cycle_C05_fewV15_noise_2.md) · [cycle_C05_fewV28_bloc_1](cycle_C05_fewV28_bloc_1.md) · [cycle_C05_medV45_noise_1](cycle_C05_medV45_noise_1.md) · [cycle_C05_medV45_noise_2](cycle_C05_medV45_noise_2.md) · [cycle_C07_fewV15_noise_1](cycle_C07_fewV15_noise_1.md) · [cycle_C07_fewV28_bloc_2](cycle_C07_fewV28_bloc_2.md) · [cycle_C07_largeV598_bloc_1](cycle_C07_largeV598_bloc_1.md) · [cycle_C07_medV149_bloc_2](cycle_C07_medV149_bloc_2.md) · [cycle_C10_fewV15_noise_1](cycle_C10_fewV15_noise_1.md) · [cycle_C10_fewV15_noise_2](cycle_C10_fewV15_noise_2.md) · [cycle_C10_fewV28_bloc_1](cycle_C10_fewV28_bloc_1.md) · [cycle_C10_fewV29_bloc_2](cycle_C10_fewV29_bloc_2.md) · [cycle_C10_medV148_bloc_1](cycle_C10_medV148_bloc_1.md) · [cycle_C10_medV149_bloc_2](cycle_C10_medV149_bloc_2.md) · [cycle_C10_medV45_noise_1](cycle_C10_medV45_noise_1.md) · [darkhorse_C03_fewV15_noise_1](darkhorse_C03_fewV15_noise_1.md) · [darkhorse_C05_largeV599_bloc_1](darkhorse_C05_largeV599_bloc_1.md) · [darkhorse_C07_fewV30_bloc_1](darkhorse_C07_fewV30_bloc_1.md) · [darkhorse_C07_largeV597_bloc_1](darkhorse_C07_largeV597_bloc_1.md) · [darkhorse_C07_largeV598_bloc_2](darkhorse_C07_largeV598_bloc_2.md) · [darkhorse_C07_medV147_bloc_1](darkhorse_C07_medV147_bloc_1.md) · [darkhorse_C07_medV45_noise_1](darkhorse_C07_medV45_noise_1.md) · [darkhorse_C10_largeV598_bloc_1](darkhorse_C10_largeV598_bloc_1.md) · [darkhorse_C10_largeV599_bloc_2](darkhorse_C10_largeV599_bloc_2.md)
