# STAR vs RR divergence -- 7 cands, 597 voters, darkhorse (STAR D, RR E)

*Generated from [`darkhorse_C07_largeV597_bloc_1.yaml`](../darkhorse_C07_largeV597_bloc_1.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** D

## Scenario

Auto-generated STAR-vs-Ranked-Robin divergence. 7 candidates, 597 voters, grouped (a few voter factions/blocs). STAR elects D; Ranked Robin elects E. CAUSE = DARK HORSE: E is the Condorcet winner (beats every rival head-to-head) but only #3 of 7 by score total (2230 vs leader D 2523) -- a broadly-liked, low-intensity compromise that misses STAR's score finalists (D, C). STAR elects runoff winner D; RR elects the Condorcet winner E. Preference-vs-support: RR rewards ORDER, STAR rewards SUPPORT strength. See the [Divergence from STAR] block below for RCV-IRV, Approval and Plurality on the same ballots.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:A,B,C,D,E,F,G
204:3,5,4,4,5,1,0
168:0,0,4,5,2,1,3
158:4,5,4,4,5,2,0
42:0,1,4,5,2,0,2
25:3,0,1,1,0,5,1
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR                   = D
  Choose-One (Plurality) = B   (differs from STAR)
  RCV-IRV                = B   (differs from STAR)
  Approval               = C   (differs from STAR)
  RCV-RR (Condorcet)     = E   (differs from STAR)
  Note: 429 of 597 ballots (72%) had equal non-zero scores, so their ranks
        were decided by candidate priority order. The RCV-IRV result may be
        an artifact of score-to-rank tie-breaking rather than a deep
        difference.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: star_vs_rr_divergence_tabulated/darkhorse_C07_largeV597_bloc_1_RCV-IRV_tabulated.txt
  RCV-RR round-robin: star_vs_rr_divergence_tabulated/darkhorse_C07_largeV597_bloc_1_RCV-RR_tabulated.txt

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 597 ballots.
Count x A,B,C,D,E,F,G
  204 x 3,5,4,4,5,1,0
  168 x 0,0,4,5,2,1,3
  158 x 4,5,4,4,5,2,0
   42 x 0,1,4,5,2,0,2
   25 x 3,0,1,1,0,5,1

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   D             -- 2523 -- First place
   C             -- 2313 -- Second place
   E             -- 2230
   B             -- 1852
   A             -- 1319
   F             --  813
   G             --  613
 D and C advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   D             -- 210 -- First place
   C             --   0
   Equal Support -- 387
 D wins.
   Runoff math:
     597  ballots cast
   − 387  Equal Support (no preference between the two finalists)
     ───
     210  voters with a preference  (majority = 106)
           D 210 (100%)  ·  C 0 (0%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 D
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                    |         A       |        B       |      * C       |      * D       |        E       |        F       |        G       |
---------------------------------------------------------------------------------------------------------------------------------------------
                A > |       ---       | 25 - 168 - 404 | 25 - 158 - 414 | 25 - 158 - 414 | 25 -   0 - 572 |362 -  42 - 193 |387 -   0 - 210 |
                B > | 404 - 168 -  25 |      ---       |362 -   0 - 235 |362 -   0 - 235 |  0 - 387 - 210 |404 -   0 - 193 |362 -   0 - 235 |
              * C > | 414 - 158 -  25 |235 -   0 - 362 |      ---       |  0 - 387 - 210 |235 -   0 - 362 |572 -   0 -  25 |572 -  25 -   0 |
              * D > | 414 - 158 -  25 |235 -   0 - 362 |210 - 387 -   0 |      ---       |235 -   0 - 362 |572 -   0 -  25 |572 -  25 -   0 |
                E > | 572 -   0 -  25 |210 - 387 -   0 |362 -   0 - 235 |362 -   0 - 235 |      ---       |572 -   0 -  25 |362 -  42 - 193 |
                F > | 193 -  42 - 362 |193 -   0 - 404 | 25 -   0 - 572 | 25 -   0 - 572 | 25 -   0 - 572 |      ---       |387 -   0 - 210 |
                G > | 210 -   0 - 387 |235 -   0 - 362 |  0 -  25 - 572 |  0 -  25 - 572 |193 -  42 - 362 |210 -   0 - 387 |      ---       |

[Condorcet Winner]
  Condorcet Winner: E — STAR elected D instead (E was eliminated in the scoring round)

[Score Distribution] (how many ballots gave each star rating)
                      Score
Candidate    5    4    3    2    1    0  | Total   Avg
A            0  158  229    0    0  210  |  1319   2.2
B          362    0    0    0   42  193  |  1852   3.1
C            0  572    0    0   25    0  |  2313   3.9
D          210  362    0    0   25    0  |  2523   4.2
E          362    0    0  210    0   25  |  2230   3.7
F           25    0    0  158  372   42  |   813   1.4
G            0    0  168   42   25  362  |   613   1.0
```

Everything in one file: the [`_tabulated` mirror](../star_vs_rr_divergence_tabulated/darkhorse_C07_largeV597_bloc_1_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 05_Ranked_Robin/star_vs_rr_divergence/darkhorse_C07_largeV597_bloc_1.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README.md)
- [Runoff reversal (worked set)](../../../01_STAR/runoff_overturns_leader/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [cycle_C03_fewV15_noise_1](cycle_C03_fewV15_noise_1.md) · [cycle_C03_fewV15_noise_2](cycle_C03_fewV15_noise_2.md) · [cycle_C03_medV45_noise_1](cycle_C03_medV45_noise_1.md) · [cycle_C03_medV45_noise_2](cycle_C03_medV45_noise_2.md) · [cycle_C05_fewV15_noise_1](cycle_C05_fewV15_noise_1.md) · [cycle_C05_fewV15_noise_2](cycle_C05_fewV15_noise_2.md) · [cycle_C05_fewV28_bloc_1](cycle_C05_fewV28_bloc_1.md) · [cycle_C05_medV45_noise_1](cycle_C05_medV45_noise_1.md) · [cycle_C05_medV45_noise_2](cycle_C05_medV45_noise_2.md) · [cycle_C07_fewV15_noise_1](cycle_C07_fewV15_noise_1.md) · [cycle_C07_fewV28_bloc_2](cycle_C07_fewV28_bloc_2.md) · [cycle_C07_largeV598_bloc_1](cycle_C07_largeV598_bloc_1.md) · [cycle_C07_medV149_bloc_2](cycle_C07_medV149_bloc_2.md) · [cycle_C10_fewV15_noise_1](cycle_C10_fewV15_noise_1.md) · [cycle_C10_fewV15_noise_2](cycle_C10_fewV15_noise_2.md) · [cycle_C10_fewV28_bloc_1](cycle_C10_fewV28_bloc_1.md) · [cycle_C10_fewV29_bloc_2](cycle_C10_fewV29_bloc_2.md) · [cycle_C10_medV148_bloc_1](cycle_C10_medV148_bloc_1.md) · [cycle_C10_medV149_bloc_2](cycle_C10_medV149_bloc_2.md) · [cycle_C10_medV45_noise_1](cycle_C10_medV45_noise_1.md) · [cycle_C10_medV45_noise_2](cycle_C10_medV45_noise_2.md) · [darkhorse_C03_fewV15_noise_1](darkhorse_C03_fewV15_noise_1.md) · [darkhorse_C05_largeV599_bloc_1](darkhorse_C05_largeV599_bloc_1.md) · [darkhorse_C07_fewV30_bloc_1](darkhorse_C07_fewV30_bloc_1.md) · [darkhorse_C07_largeV598_bloc_2](darkhorse_C07_largeV598_bloc_2.md) · [darkhorse_C07_medV147_bloc_1](darkhorse_C07_medV147_bloc_1.md) · [darkhorse_C07_medV45_noise_1](darkhorse_C07_medV45_noise_1.md) · [darkhorse_C10_largeV598_bloc_1](darkhorse_C10_largeV598_bloc_1.md) · [darkhorse_C10_largeV599_bloc_2](darkhorse_C10_largeV599_bloc_2.md)
