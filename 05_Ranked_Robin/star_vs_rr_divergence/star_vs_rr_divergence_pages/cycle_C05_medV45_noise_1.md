# STAR vs RR divergence -- 5 cands, 45 voters, cycle (STAR A, RR B)

*Generated from [`cycle_C05_medV45_noise_1.yaml`](../cycle_C05_medV45_noise_1.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** A

## Scenario

Auto-generated STAR-vs-Ranked-Robin divergence. 5 candidates, 45 voters, ungrouped (independent random ballots). STAR elects A; Ranked Robin elects B. CAUSE = CONDORCET CYCLE: no candidate beats all others (A>E>B>A), so there is no 'right' winner. RR falls back on Copeland/margin (B); STAR runs its two score-leaders off (A). See the [Divergence from STAR] block below for RCV-IRV, Approval and Plurality on the same ballots.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:A,B,C,D,E
1:2,0,0,5,2
1:1,4,5,0,0
1:2,3,3,3,4
1:1,2,2,0,2
1:3,5,1,3,1
1:4,2,3,2,3
1:1,4,1,4,5
1:3,4,3,2,0
1:3,4,2,1,3
1:2,0,5,2,5
1:1,2,3,2,1
1:4,1,4,0,5
1:5,0,2,4,3
1:2,1,1,3,3
1:4,4,4,5,3
1:4,2,5,4,3
1:4,3,5,4,3
1:5,1,5,0,3
1:4,1,0,4,2
1:1,2,5,4,1
1:1,4,2,4,2
1:2,4,0,0,1
1:4,3,4,2,3
1:5,4,3,1,3
1:4,4,1,2,4
1:5,5,2,2,4
1:3,3,3,1,2
1:3,3,3,2,1
1:3,4,2,1,4
1:1,5,4,5,2
1:2,3,1,0,2
1:4,1,1,3,3
1:2,4,1,4,2
1:4,3,2,1,2
1:1,4,4,5,4
1:5,1,2,1,0
1:1,2,3,3,3
1:5,3,3,1,3
1:2,3,3,2,4
1:0,2,1,2,4
1:0,1,3,0,3
1:1,2,2,2,2
1:1,1,2,4,2
1:0,2,0,4,3
1:4,1,3,0,3
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR     = A
  Approval = E   (differs from STAR)
  RCV-RR   = B   (differs from STAR)
  Full round-by-round reports (generated for review):
  RCV-RR round-robin: star_vs_rr_divergence_tabulated/cycle_C05_medV45_noise_1_RCV-RR_tabulated.txt

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 45 ballots.
A,B,C,D,E
2,0,0,5,2
1,4,5,0,0
2,3,3,3,4
1,2,2,0,2
3,5,1,3,1
4,2,3,2,3
1,4,1,4,5
3,4,3,2,0
3,4,2,1,3
2,0,5,2,5
1,2,3,2,1
4,1,4,0,5
5,0,2,4,3
2,1,1,3,3
4,4,4,5,3
4,2,5,4,3
4,3,5,4,3
5,1,5,0,3
4,1,0,4,2
1,2,5,4,1
1,4,2,4,2
2,4,0,0,1
4,3,4,2,3
5,4,3,1,3
4,4,1,2,4
5,5,2,2,4
3,3,3,1,2
3,3,3,2,1
3,4,2,1,4
1,5,4,5,2
2,3,1,0,2
4,1,1,3,3
2,4,1,4,2
4,3,2,1,2
1,4,4,5,4
5,1,2,1,0
1,2,3,3,3
5,3,3,1,3
2,3,3,2,4
0,2,1,2,4
0,1,3,0,3
1,2,2,2,2
1,1,2,4,2
0,2,0,4,3
4,1,3,0,3

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   A             -- 119 -- First place
   E             -- 118 -- Second place
   B             -- 117
   C             -- 114
   D             -- 104
 A and E advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   A             -- 21 -- First place
   E             -- 17
   Equal Support --  7
 A wins.
   Runoff math:
     45  ballots cast
   −  7  Equal Support (no preference between the two finalists)
     ──
     38  voters with a preference  (majority = 20)
           A 21 (55%)  ·  E 17 (45%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 A
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |     * A      |      B      |      C      |      D      |    * E      |
-----------------------------------------------------------------------------------------
           * A > |     ---      |17 -  6 - 22 |19 -  9 - 17 |22 -  7 - 16 |21 -  7 - 17 |
             B > | 22 -  6 - 17 |    ---      |17 - 12 - 16 |21 - 10 - 14 |18 -  8 - 19 |
             C > | 17 -  9 - 19 |16 - 12 - 17 |    ---      |24 -  5 - 16 |13 - 14 - 18 |
             D > | 16 -  7 - 22 |14 - 10 - 21 |16 -  5 - 24 |    ---      |18 -  5 - 22 |
           * E > | 17 -  7 - 21 |19 -  8 - 18 |18 - 14 - 13 |22 -  5 - 18 |    ---      |

[Condorcet Winner]
  No Condorcet winner (majority cycle: A > E > B > A)

[Score Distribution] (how many ballots gave each star rating)
                   Score
Candidate   5   4   3   2   1   0  | Total   Avg
A           6  11   6   8  11   3  |   119   2.6
B           3  12   9   9   9   3  |   117   2.6
C           6   5  12  10   8   4  |   114   2.5
D           4  10   5  11   7   8  |   104   2.3
E           3   7  16  11   5   3  |   118   2.6
```

Everything in one file: the [`_tabulated` mirror](../star_vs_rr_divergence_tabulated/cycle_C05_medV45_noise_1_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 05_Ranked_Robin/star_vs_rr_divergence/cycle_C05_medV45_noise_1.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [cycle_C03_fewV15_noise_1](cycle_C03_fewV15_noise_1.md) · [cycle_C03_fewV15_noise_2](cycle_C03_fewV15_noise_2.md) · [cycle_C03_medV45_noise_1](cycle_C03_medV45_noise_1.md) · [cycle_C03_medV45_noise_2](cycle_C03_medV45_noise_2.md) · [cycle_C05_fewV15_noise_1](cycle_C05_fewV15_noise_1.md) · [cycle_C05_fewV15_noise_2](cycle_C05_fewV15_noise_2.md) · [cycle_C05_fewV28_bloc_1](cycle_C05_fewV28_bloc_1.md) · [cycle_C05_medV45_noise_2](cycle_C05_medV45_noise_2.md) · [cycle_C07_fewV15_noise_1](cycle_C07_fewV15_noise_1.md) · [cycle_C07_fewV28_bloc_2](cycle_C07_fewV28_bloc_2.md) · [cycle_C07_largeV598_bloc_1](cycle_C07_largeV598_bloc_1.md) · [cycle_C07_medV149_bloc_2](cycle_C07_medV149_bloc_2.md) · [cycle_C10_fewV15_noise_1](cycle_C10_fewV15_noise_1.md) · [cycle_C10_fewV15_noise_2](cycle_C10_fewV15_noise_2.md) · [cycle_C10_fewV28_bloc_1](cycle_C10_fewV28_bloc_1.md) · [cycle_C10_fewV29_bloc_2](cycle_C10_fewV29_bloc_2.md) · [cycle_C10_medV148_bloc_1](cycle_C10_medV148_bloc_1.md) · [cycle_C10_medV149_bloc_2](cycle_C10_medV149_bloc_2.md) · [cycle_C10_medV45_noise_1](cycle_C10_medV45_noise_1.md) · [cycle_C10_medV45_noise_2](cycle_C10_medV45_noise_2.md) · [darkhorse_C03_fewV15_noise_1](darkhorse_C03_fewV15_noise_1.md) · [darkhorse_C05_largeV599_bloc_1](darkhorse_C05_largeV599_bloc_1.md) · [darkhorse_C07_fewV30_bloc_1](darkhorse_C07_fewV30_bloc_1.md) · [darkhorse_C07_largeV597_bloc_1](darkhorse_C07_largeV597_bloc_1.md) · [darkhorse_C07_largeV598_bloc_2](darkhorse_C07_largeV598_bloc_2.md) · [darkhorse_C07_medV147_bloc_1](darkhorse_C07_medV147_bloc_1.md) · [darkhorse_C07_medV45_noise_1](darkhorse_C07_medV45_noise_1.md) · [darkhorse_C10_largeV598_bloc_1](darkhorse_C10_largeV598_bloc_1.md) · [darkhorse_C10_largeV599_bloc_2](darkhorse_C10_largeV599_bloc_2.md)
