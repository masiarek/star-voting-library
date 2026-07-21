# STAR vs RR divergence -- 7 cands, 15 voters, cycle (STAR D, RR A)

*Generated from [`cycle_C07_fewV15_noise_1.yaml`](../cycle_C07_fewV15_noise_1.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** D

## Scenario

Auto-generated STAR-vs-Ranked-Robin divergence. 7 candidates, 15 voters, ungrouped (independent random ballots). STAR elects D; Ranked Robin elects A. CAUSE = CONDORCET CYCLE: no candidate beats all others (B>E>C>B), so there is no 'right' winner. RR falls back on Copeland/margin (A); STAR runs its two score-leaders off (D). See the [Divergence from STAR] block below for RCV-IRV, Approval and Plurality on the same ballots.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:A,B,C,D,E,F,G
1:3,3,4,2,4,4,1
1:2,2,3,3,4,2,4
1:2,2,3,2,2,0,3
1:3,1,2,3,4,1,5
1:5,2,4,3,1,2,3
1:4,4,2,1,3,4,0
1:0,4,4,3,2,5,1
1:3,5,3,3,3,1,2
1:3,3,4,2,1,0,1
1:3,2,1,3,2,2,1
1:0,4,0,3,1,1,4
1:3,4,1,5,4,3,4
1:3,0,1,3,1,5,1
1:2,1,1,1,1,1,2
1:4,0,2,5,1,1,3
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR                   = D
  Choose-One (Plurality) = A   (differs from STAR)
  RCV-IRV                = A   (differs from STAR)
  Approval               = A   (differs from STAR)
  RCV-RR                 = A   (differs from STAR)
  Note: 15 of 15 ballots (100%) had equal non-zero scores, so their ranks
        were decided by candidate priority order. The RCV-IRV result may be
        an artifact of score-to-rank tie-breaking rather than a deep
        difference.
  Note: Ranked Robin (RCV-RR) sides with RCV-IRV, so STAR is the outlier
        here — STAR need not elect the Condorcet candidate.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: star_vs_rr_divergence_tabulated/cycle_C07_fewV15_noise_1_RCV-IRV_tabulated.txt
  RCV-RR round-robin: star_vs_rr_divergence_tabulated/cycle_C07_fewV15_noise_1_RCV-RR_tabulated.txt

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 15 ballots.
A,B,C,D,E,F,G
3,3,4,2,4,4,1
2,2,3,3,4,2,4
2,2,3,2,2,0,3
3,1,2,3,4,1,5
5,2,4,3,1,2,3
4,4,2,1,3,4,0
0,4,4,3,2,5,1
3,5,3,3,3,1,2
3,3,4,2,1,0,1
3,2,1,3,2,2,1
0,4,0,3,1,1,4
3,4,1,5,4,3,4
3,0,1,3,1,5,1
2,1,1,1,1,1,2
4,0,2,5,1,1,3

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   D             -- 42 -- First place
   A             -- 40 -- Second place
   B             -- 37
   C             -- 35
   G             -- 35
   E             -- 34
   F             -- 32
 D and A advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   A             -- 5 -- Tied for first place
   D             -- 5 -- Tied for first place
   Equal Support -- 5
 There's a two-way tie for first.

[STAR Voting: Automatic Runoff Round: First tiebreaker]
 The highest-scoring candidate wins.
   D             -- 42 -- First place
   A             -- 40
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
                 |     * A      |      B      |      C      |    * D      |      E      |      F      |      G      |
---------------------------------------------------------------------------------------------------------------------
           * A > |     ---      | 6 -  5 -  4 | 8 -  2 -  5 | 5 -  5 -  5 | 7 -  2 -  6 | 8 -  3 -  4 | 8 -  1 -  6 |
             B > |  4 -  5 -  6 |    ---      | 5 -  2 -  8 | 6 -  2 -  7 | 6 -  4 -  5 | 5 -  6 -  4 | 6 -  2 -  7 |
             C > |  5 -  2 -  8 | 8 -  2 -  5 |    ---      | 6 -  3 -  6 | 5 -  4 -  6 | 7 -  2 -  6 | 6 -  3 -  6 |
           * D > |  5 -  5 -  5 | 7 -  2 -  6 | 6 -  3 -  6 |    ---      | 8 -  3 -  4 |10 -  1 -  4 | 9 -  1 -  5 |
             E > |  6 -  2 -  7 | 5 -  4 -  6 | 6 -  4 -  5 | 4 -  3 -  8 |    ---      | 6 -  5 -  4 | 5 -  4 -  6 |
             F > |  4 -  3 -  8 | 4 -  6 -  5 | 6 -  2 -  7 | 4 -  1 - 10 | 4 -  5 -  6 |    ---      | 5 -  0 - 10 |
             G > |  6 -  1 -  8 | 7 -  2 -  6 | 6 -  3 -  6 | 5 -  1 -  9 | 6 -  4 -  5 |10 -  0 -  5 |    ---      |

[Condorcet Winner]
  No strict Condorcet winner; unbeaten candidates: A, D (pairwise ties)

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
A          1  2  7  3  0  2  |    40   2.7
B          1  4  2  4  2  2  |    37   2.5
C          0  4  3  3  4  1  |    35   2.3
D          2  0  8  3  2  0  |    42   2.8
E          0  4  2  3  6  0  |    34   2.3
F          2  2  1  3  5  2  |    32   2.1
G          1  3  3  2  5  1  |    35   2.3
```

Everything in one file: the [`_tabulated` mirror](../star_vs_rr_divergence_tabulated/cycle_C07_fewV15_noise_1_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 05_Ranked_Robin/star_vs_rr_divergence/cycle_C07_fewV15_noise_1.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [cycle_C03_fewV15_noise_1](cycle_C03_fewV15_noise_1.md) · [cycle_C03_fewV15_noise_2](cycle_C03_fewV15_noise_2.md) · [cycle_C03_medV45_noise_1](cycle_C03_medV45_noise_1.md) · [cycle_C03_medV45_noise_2](cycle_C03_medV45_noise_2.md) · [cycle_C05_fewV15_noise_1](cycle_C05_fewV15_noise_1.md) · [cycle_C05_fewV15_noise_2](cycle_C05_fewV15_noise_2.md) · [cycle_C05_fewV28_bloc_1](cycle_C05_fewV28_bloc_1.md) · [cycle_C05_medV45_noise_1](cycle_C05_medV45_noise_1.md) · [cycle_C05_medV45_noise_2](cycle_C05_medV45_noise_2.md) · [cycle_C07_fewV28_bloc_2](cycle_C07_fewV28_bloc_2.md) · [cycle_C07_largeV598_bloc_1](cycle_C07_largeV598_bloc_1.md) · [cycle_C07_medV149_bloc_2](cycle_C07_medV149_bloc_2.md) · [cycle_C10_fewV15_noise_1](cycle_C10_fewV15_noise_1.md) · [cycle_C10_fewV15_noise_2](cycle_C10_fewV15_noise_2.md) · [cycle_C10_fewV28_bloc_1](cycle_C10_fewV28_bloc_1.md) · [cycle_C10_fewV29_bloc_2](cycle_C10_fewV29_bloc_2.md) · [cycle_C10_medV148_bloc_1](cycle_C10_medV148_bloc_1.md) · [cycle_C10_medV149_bloc_2](cycle_C10_medV149_bloc_2.md) · [cycle_C10_medV45_noise_1](cycle_C10_medV45_noise_1.md) · [cycle_C10_medV45_noise_2](cycle_C10_medV45_noise_2.md) · [darkhorse_C03_fewV15_noise_1](darkhorse_C03_fewV15_noise_1.md) · [darkhorse_C05_largeV599_bloc_1](darkhorse_C05_largeV599_bloc_1.md) · [darkhorse_C07_fewV30_bloc_1](darkhorse_C07_fewV30_bloc_1.md) · [darkhorse_C07_largeV597_bloc_1](darkhorse_C07_largeV597_bloc_1.md) · [darkhorse_C07_largeV598_bloc_2](darkhorse_C07_largeV598_bloc_2.md) · [darkhorse_C07_medV147_bloc_1](darkhorse_C07_medV147_bloc_1.md) · [darkhorse_C07_medV45_noise_1](darkhorse_C07_medV45_noise_1.md) · [darkhorse_C10_largeV598_bloc_1](darkhorse_C10_largeV598_bloc_1.md) · [darkhorse_C10_largeV599_bloc_2](darkhorse_C10_largeV599_bloc_2.md)
