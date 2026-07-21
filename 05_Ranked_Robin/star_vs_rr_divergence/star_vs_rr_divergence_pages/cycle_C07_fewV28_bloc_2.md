# STAR vs RR divergence -- 7 cands, 28 voters, cycle (STAR D, RR A)

*Generated from [`cycle_C07_fewV28_bloc_2.yaml`](../cycle_C07_fewV28_bloc_2.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** D

## Scenario

Auto-generated STAR-vs-Ranked-Robin divergence. 7 candidates, 28 voters, grouped (a few voter factions/blocs). STAR elects D; Ranked Robin elects A. CAUSE = CONDORCET CYCLE: no candidate beats all others, so there is no 'right' winner. RR falls back on Copeland/margin (A); STAR runs its two score-leaders off (D). See the [Divergence from STAR] block below for RCV-IRV, Approval and Plurality on the same ballots.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:A,B,C,D,E,F,G
7:1,0,4,5,0,0,0
7:3,4,3,2,0,5,4
7:3,0,4,5,2,0,1
7:5,0,2,2,2,1,3
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR     = D
  Approval = A   (differs from STAR)
  RCV-RR   = A   (differs from STAR)
  Full round-by-round reports (generated for review):
  RCV-RR round-robin: star_vs_rr_divergence_tabulated/cycle_C07_fewV28_bloc_2_RCV-RR_tabulated.txt

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 28 ballots.
Count x A,B,C,D,E,F,G
    7 x 1,0,4,5,0,0,0
    7 x 3,4,3,2,0,5,4
    7 x 3,0,4,5,2,0,1
    7 x 5,0,2,2,2,1,3

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   D             -- 98 -- First place
   C             -- 91 -- Second place
   A             -- 84
   G             -- 56
   F             -- 42
   B             -- 28
   E             -- 28
 D and C advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   D             -- 14 -- First place
   C             --  7
   Equal Support --  7
 D wins.
   Runoff math:
     28  ballots cast
   −  7  Equal Support (no preference between the two finalists)
     ──
     21  voters with a preference  (majority = 11)
           D 14 (67%)  ·  C 7 (33%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 D
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |       A      |      B      |    * C      |    * D      |      E      |      F      |      G      |
---------------------------------------------------------------------------------------------------------------------
             A > |     ---      |21 -  0 -  7 | 7 -  7 - 14 |14 -  0 - 14 |28 -  0 -  0 |21 -  0 -  7 |21 -  0 -  7 |
             B > |  7 -  0 - 21 |    ---      | 7 -  0 - 21 | 7 -  0 - 21 | 7 -  7 - 14 | 0 - 14 - 14 | 0 - 14 - 14 |
           * C > | 14 -  7 -  7 |21 -  0 -  7 |    ---      | 7 -  7 - 14 |21 -  7 -  0 |21 -  0 -  7 |14 -  0 - 14 |
           * D > | 14 -  0 - 14 |21 -  0 -  7 |14 -  7 -  7 |    ---      |21 -  7 -  0 |21 -  0 -  7 |14 -  0 - 14 |
             E > |  0 -  0 - 28 |14 -  7 -  7 | 0 -  7 - 21 | 0 -  7 - 21 |    ---      |14 -  7 -  7 | 7 -  7 - 14 |
             F > |  7 -  0 - 21 |14 - 14 -  0 | 7 -  0 - 21 | 7 -  0 - 21 | 7 -  7 - 14 |    ---      | 7 -  7 - 14 |
             G > |  7 -  0 - 21 |14 - 14 -  0 |14 -  0 - 14 |14 -  0 - 14 |14 -  7 -  7 |14 -  7 -  7 |    ---      |

[Condorcet Winner]
  No strict Condorcet winner; weak Condorcet winner: D — matches the STAR winner

[Score Distribution] (how many ballots gave each star rating)
                   Score
Candidate   5   4   3   2   1   0  | Total   Avg
A           7   0  14   0   7   0  |    84   3.0
B           0   7   0   0   0  21  |    28   1.0
C           0  14   7   7   0   0  |    91   3.3
D          14   0   0  14   0   0  |    98   3.5
E           0   0   0  14   0  14  |    28   1.0
F           7   0   0   0   7  14  |    42   1.5
G           0   7   7   0   7   7  |    56   2.0
```

Everything in one file: the [`_tabulated` mirror](../star_vs_rr_divergence_tabulated/cycle_C07_fewV28_bloc_2_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 05_Ranked_Robin/star_vs_rr_divergence/cycle_C07_fewV28_bloc_2.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [cycle_C03_fewV15_noise_1](cycle_C03_fewV15_noise_1.md) · [cycle_C03_fewV15_noise_2](cycle_C03_fewV15_noise_2.md) · [cycle_C03_medV45_noise_1](cycle_C03_medV45_noise_1.md) · [cycle_C03_medV45_noise_2](cycle_C03_medV45_noise_2.md) · [cycle_C05_fewV15_noise_1](cycle_C05_fewV15_noise_1.md) · [cycle_C05_fewV15_noise_2](cycle_C05_fewV15_noise_2.md) · [cycle_C05_fewV28_bloc_1](cycle_C05_fewV28_bloc_1.md) · [cycle_C05_medV45_noise_1](cycle_C05_medV45_noise_1.md) · [cycle_C05_medV45_noise_2](cycle_C05_medV45_noise_2.md) · [cycle_C07_fewV15_noise_1](cycle_C07_fewV15_noise_1.md) · [cycle_C07_largeV598_bloc_1](cycle_C07_largeV598_bloc_1.md) · [cycle_C07_medV149_bloc_2](cycle_C07_medV149_bloc_2.md) · [cycle_C10_fewV15_noise_1](cycle_C10_fewV15_noise_1.md) · [cycle_C10_fewV15_noise_2](cycle_C10_fewV15_noise_2.md) · [cycle_C10_fewV28_bloc_1](cycle_C10_fewV28_bloc_1.md) · [cycle_C10_fewV29_bloc_2](cycle_C10_fewV29_bloc_2.md) · [cycle_C10_medV148_bloc_1](cycle_C10_medV148_bloc_1.md) · [cycle_C10_medV149_bloc_2](cycle_C10_medV149_bloc_2.md) · [cycle_C10_medV45_noise_1](cycle_C10_medV45_noise_1.md) · [cycle_C10_medV45_noise_2](cycle_C10_medV45_noise_2.md) · [darkhorse_C03_fewV15_noise_1](darkhorse_C03_fewV15_noise_1.md) · [darkhorse_C05_largeV599_bloc_1](darkhorse_C05_largeV599_bloc_1.md) · [darkhorse_C07_fewV30_bloc_1](darkhorse_C07_fewV30_bloc_1.md) · [darkhorse_C07_largeV597_bloc_1](darkhorse_C07_largeV597_bloc_1.md) · [darkhorse_C07_largeV598_bloc_2](darkhorse_C07_largeV598_bloc_2.md) · [darkhorse_C07_medV147_bloc_1](darkhorse_C07_medV147_bloc_1.md) · [darkhorse_C07_medV45_noise_1](darkhorse_C07_medV45_noise_1.md) · [darkhorse_C10_largeV598_bloc_1](darkhorse_C10_largeV598_bloc_1.md) · [darkhorse_C10_largeV599_bloc_2](darkhorse_C10_largeV599_bloc_2.md)
