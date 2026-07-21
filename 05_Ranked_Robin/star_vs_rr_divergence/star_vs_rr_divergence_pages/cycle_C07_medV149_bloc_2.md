# STAR vs RR divergence -- 7 cands, 149 voters, cycle (STAR F, RR C)

*Generated from [`cycle_C07_medV149_bloc_2.yaml`](../cycle_C07_medV149_bloc_2.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** F

## Scenario

Auto-generated STAR-vs-Ranked-Robin divergence. 7 candidates, 149 voters, grouped (a few voter factions/blocs). STAR elects F; Ranked Robin elects C. CAUSE = CONDORCET CYCLE: no candidate beats all others, so there is no 'right' winner. RR falls back on Copeland/margin (C); STAR runs its two score-leaders off (F). See the [Divergence from STAR] block below for RCV-IRV, Approval and Plurality on the same ballots.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:A,B,C,D,E,F,G
52:5,0,5,1,2,1,2
52:2,0,3,3,1,5,1
45:0,5,0,4,3,3,3
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR                   = F
  Choose-One (Plurality) = A   (differs from STAR)
  Approval               = C   (differs from STAR)
  RCV-RR                 = C   (differs from STAR)
  Full round-by-round reports (generated for review):
  RCV-RR round-robin: star_vs_rr_divergence_tabulated/cycle_C07_medV149_bloc_2_RCV-RR_tabulated.txt

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 149 ballots.
Count x A,B,C,D,E,F,G
   52 x 5,0,5,1,2,1,2
   52 x 2,0,3,3,1,5,1
   45 x 0,5,0,4,3,3,3

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   F             -- 447 -- First place
   C             -- 416 -- Second place
   D             -- 388
   A             -- 364
   E             -- 291
   G             -- 291
   B             -- 225
 F and C advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   F             -- 97 -- First place
   C             -- 52
   Equal Support --  0
 F wins.
   Runoff math:
     149  ballots cast
   −   0  Equal Support (no preference between the two finalists)
     ───
     149  voters with a preference  (majority = 75)
           F 97 (65%)  ·  C 52 (35%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 F
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                    |         A       |        B       |      * C       |        D       |        E       |      * F       |        G       |
---------------------------------------------------------------------------------------------------------------------------------------------
                A > |       ---       |104 -   0 -  45 |  0 -  97 -  52 | 52 -   0 -  97 |104 -   0 -  45 | 52 -   0 -  97 |104 -   0 -  45 |
                B > |  45 -   0 - 104 |      ---       | 45 -   0 - 104 | 45 -   0 - 104 | 45 -   0 - 104 | 45 -   0 - 104 | 45 -   0 - 104 |
              * C > |  52 -  97 -   0 |104 -   0 -  45 |      ---       | 52 -  52 -  45 |104 -   0 -  45 | 52 -   0 -  97 |104 -   0 -  45 |
                D > |  97 -   0 -  52 |104 -   0 -  45 | 45 -  52 -  52 |      ---       | 97 -   0 -  52 | 45 -  52 -  52 | 97 -   0 -  52 |
                E > |  45 -   0 - 104 |104 -   0 -  45 | 45 -   0 - 104 | 52 -   0 -  97 |      ---       | 52 -  45 -  52 |  0 - 149 -   0 |
              * F > |  97 -   0 -  52 |104 -   0 -  45 | 97 -   0 -  52 | 52 -  52 -  45 | 52 -  45 -  52 |      ---       | 52 -  45 -  52 |
                G > |  45 -   0 - 104 |104 -   0 -  45 | 45 -   0 - 104 | 52 -   0 -  97 |  0 - 149 -   0 | 52 -  45 -  52 |      ---       |

[Condorcet Winner]
  No strict Condorcet winner; weak Condorcet winner: F — matches the STAR winner

[Score Distribution] (how many ballots gave each star rating)
                      Score
Candidate    5    4    3    2    1    0  | Total   Avg
A           52    0    0   52    0   45  |   364   2.4
B           45    0    0    0    0  104  |   225   1.5
C           52    0   52    0    0   45  |   416   2.8
D            0   45   52    0   52    0  |   388   2.6
E            0    0   45   52   52    0  |   291   2.0
F           52    0   45    0   52    0  |   447   3.0
G            0    0   45   52   52    0  |   291   2.0
```

Everything in one file: the [`_tabulated` mirror](../star_vs_rr_divergence_tabulated/cycle_C07_medV149_bloc_2_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 05_Ranked_Robin/star_vs_rr_divergence/cycle_C07_medV149_bloc_2.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [cycle_C03_fewV15_noise_1](cycle_C03_fewV15_noise_1.md) · [cycle_C03_fewV15_noise_2](cycle_C03_fewV15_noise_2.md) · [cycle_C03_medV45_noise_1](cycle_C03_medV45_noise_1.md) · [cycle_C03_medV45_noise_2](cycle_C03_medV45_noise_2.md) · [cycle_C05_fewV15_noise_1](cycle_C05_fewV15_noise_1.md) · [cycle_C05_fewV15_noise_2](cycle_C05_fewV15_noise_2.md) · [cycle_C05_fewV28_bloc_1](cycle_C05_fewV28_bloc_1.md) · [cycle_C05_medV45_noise_1](cycle_C05_medV45_noise_1.md) · [cycle_C05_medV45_noise_2](cycle_C05_medV45_noise_2.md) · [cycle_C07_fewV15_noise_1](cycle_C07_fewV15_noise_1.md) · [cycle_C07_fewV28_bloc_2](cycle_C07_fewV28_bloc_2.md) · [cycle_C07_largeV598_bloc_1](cycle_C07_largeV598_bloc_1.md) · [cycle_C10_fewV15_noise_1](cycle_C10_fewV15_noise_1.md) · [cycle_C10_fewV15_noise_2](cycle_C10_fewV15_noise_2.md) · [cycle_C10_fewV28_bloc_1](cycle_C10_fewV28_bloc_1.md) · [cycle_C10_fewV29_bloc_2](cycle_C10_fewV29_bloc_2.md) · [cycle_C10_medV148_bloc_1](cycle_C10_medV148_bloc_1.md) · [cycle_C10_medV149_bloc_2](cycle_C10_medV149_bloc_2.md) · [cycle_C10_medV45_noise_1](cycle_C10_medV45_noise_1.md) · [cycle_C10_medV45_noise_2](cycle_C10_medV45_noise_2.md) · [darkhorse_C03_fewV15_noise_1](darkhorse_C03_fewV15_noise_1.md) · [darkhorse_C05_largeV599_bloc_1](darkhorse_C05_largeV599_bloc_1.md) · [darkhorse_C07_fewV30_bloc_1](darkhorse_C07_fewV30_bloc_1.md) · [darkhorse_C07_largeV597_bloc_1](darkhorse_C07_largeV597_bloc_1.md) · [darkhorse_C07_largeV598_bloc_2](darkhorse_C07_largeV598_bloc_2.md) · [darkhorse_C07_medV147_bloc_1](darkhorse_C07_medV147_bloc_1.md) · [darkhorse_C07_medV45_noise_1](darkhorse_C07_medV45_noise_1.md) · [darkhorse_C10_largeV598_bloc_1](darkhorse_C10_largeV598_bloc_1.md) · [darkhorse_C10_largeV599_bloc_2](darkhorse_C10_largeV599_bloc_2.md)
