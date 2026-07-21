# STAR vs RR divergence -- 5 cands, 599 voters, darkhorse (STAR A, RR E)

*Generated from [`darkhorse_C05_largeV599_bloc_1.yaml`](../darkhorse_C05_largeV599_bloc_1.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** A

## Scenario

Auto-generated STAR-vs-Ranked-Robin divergence. 5 candidates, 599 voters, grouped (a few voter factions/blocs). STAR elects A; Ranked Robin elects E. CAUSE = DARK HORSE: E is the Condorcet winner (beats every rival head-to-head) but only #4 of 5 by score total (1379 vs leader A 1550) -- a broadly-liked, low-intensity compromise that misses STAR's score finalists (A, B). STAR elects runoff winner A; RR elects the Condorcet winner E. Preference-vs-support: RR rewards ORDER, STAR rewards SUPPORT strength. See the [Divergence from STAR] block below for RCV-IRV, Approval and Plurality on the same ballots.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:A,B,C,D,E
257:0,5,3,4,1
230:5,0,1,0,3
80:3,2,5,0,5
32:5,0,0,1,1
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR               = A
  RCV-RR (Condorcet) = E   (differs from STAR)
  Full round-by-round reports (generated for review):
  RCV-RR round-robin: star_vs_rr_divergence_tabulated/darkhorse_C05_largeV599_bloc_1_RCV-RR_tabulated.txt

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 599 ballots.
Count x A,B,C,D,E
  257 x 0,5,3,4,1
  230 x 5,0,1,0,3
   80 x 3,2,5,0,5
   32 x 5,0,0,1,1

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   A             -- 1550 -- First place
   B             -- 1445 -- Second place
   C             -- 1401
   E             -- 1379
   D             -- 1060
 A and B advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   A             -- 342 -- First place
   B             -- 257
   Equal Support --   0
 A wins.
   Runoff math:
     599  ballots cast
   −   0  Equal Support (no preference between the two finalists)
     ───
     599  voters with a preference  (majority = 300)
           A 342 (57%)  ·  B 257 (43%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 A
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                    |       * A       |      * B       |        C       |        D       |        E       |
-----------------------------------------------------------------------------------------------------------
              * A > |       ---       |342 -   0 - 257 |262 -   0 - 337 |342 -   0 - 257 |262 -   0 - 337 |
              * B > | 257 -   0 - 342 |      ---       |257 -  32 - 310 |337 - 230 -  32 |257 -   0 - 342 |
                C > | 337 -   0 - 262 |310 -  32 - 257 |      ---       |310 -   0 - 289 |257 -  80 - 262 |
                D > | 257 -   0 - 342 | 32 - 230 - 337 |289 -   0 - 310 |      ---       |257 -  32 - 310 |
                E > | 337 -   0 - 262 |342 -   0 - 257 |262 -  80 - 257 |310 -  32 - 257 |      ---       |

[Condorcet Winner]
  Condorcet Winner: E — STAR elected A instead (E was eliminated in the scoring round)

[Score Distribution] (how many ballots gave each star rating)
                      Score
Candidate    5    4    3    2    1    0  | Total   Avg
A          262    0   80    0    0  257  |  1550   2.6
B          257    0    0   80    0  262  |  1445   2.4
C           80    0  257    0  230   32  |  1401   2.3
D            0  257    0    0   32  310  |  1060   1.8
E           80    0  230    0  289    0  |  1379   2.3
```

Everything in one file: the [`_tabulated` mirror](../star_vs_rr_divergence_tabulated/darkhorse_C05_largeV599_bloc_1_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 05_Ranked_Robin/star_vs_rr_divergence/darkhorse_C05_largeV599_bloc_1.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README.md)
- [Runoff reversal (worked set)](../../../01_STAR/runoff_overturns_leader/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [cycle_C03_fewV15_noise_1](cycle_C03_fewV15_noise_1.md) · [cycle_C03_fewV15_noise_2](cycle_C03_fewV15_noise_2.md) · [cycle_C03_medV45_noise_1](cycle_C03_medV45_noise_1.md) · [cycle_C03_medV45_noise_2](cycle_C03_medV45_noise_2.md) · [cycle_C05_fewV15_noise_1](cycle_C05_fewV15_noise_1.md) · [cycle_C05_fewV15_noise_2](cycle_C05_fewV15_noise_2.md) · [cycle_C05_fewV28_bloc_1](cycle_C05_fewV28_bloc_1.md) · [cycle_C05_medV45_noise_1](cycle_C05_medV45_noise_1.md) · [cycle_C05_medV45_noise_2](cycle_C05_medV45_noise_2.md) · [cycle_C07_fewV15_noise_1](cycle_C07_fewV15_noise_1.md) · [cycle_C07_fewV28_bloc_2](cycle_C07_fewV28_bloc_2.md) · [cycle_C07_largeV598_bloc_1](cycle_C07_largeV598_bloc_1.md) · [cycle_C07_medV149_bloc_2](cycle_C07_medV149_bloc_2.md) · [cycle_C10_fewV15_noise_1](cycle_C10_fewV15_noise_1.md) · [cycle_C10_fewV15_noise_2](cycle_C10_fewV15_noise_2.md) · [cycle_C10_fewV28_bloc_1](cycle_C10_fewV28_bloc_1.md) · [cycle_C10_fewV29_bloc_2](cycle_C10_fewV29_bloc_2.md) · [cycle_C10_medV148_bloc_1](cycle_C10_medV148_bloc_1.md) · [cycle_C10_medV149_bloc_2](cycle_C10_medV149_bloc_2.md) · [cycle_C10_medV45_noise_1](cycle_C10_medV45_noise_1.md) · [cycle_C10_medV45_noise_2](cycle_C10_medV45_noise_2.md) · [darkhorse_C03_fewV15_noise_1](darkhorse_C03_fewV15_noise_1.md) · [darkhorse_C07_fewV30_bloc_1](darkhorse_C07_fewV30_bloc_1.md) · [darkhorse_C07_largeV597_bloc_1](darkhorse_C07_largeV597_bloc_1.md) · [darkhorse_C07_largeV598_bloc_2](darkhorse_C07_largeV598_bloc_2.md) · [darkhorse_C07_medV147_bloc_1](darkhorse_C07_medV147_bloc_1.md) · [darkhorse_C07_medV45_noise_1](darkhorse_C07_medV45_noise_1.md) · [darkhorse_C10_largeV598_bloc_1](darkhorse_C10_largeV598_bloc_1.md) · [darkhorse_C10_largeV599_bloc_2](darkhorse_C10_largeV599_bloc_2.md)
