# STAR vs RR divergence -- 7 cands, 147 voters, darkhorse (STAR F, RR D)

*Generated from [`darkhorse_C07_medV147_bloc_1.yaml`](../darkhorse_C07_medV147_bloc_1.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** F

## Scenario

Auto-generated STAR-vs-Ranked-Robin divergence. 7 candidates, 147 voters, grouped (a few voter factions/blocs). STAR elects F; Ranked Robin elects D. CAUSE = DARK HORSE: D is the Condorcet winner (beats every rival head-to-head) but only #3 of 7 by score total (445 vs leader C 461) -- a broadly-liked, low-intensity compromise that misses STAR's score finalists (C, F). STAR elects runoff winner F; RR elects the Condorcet winner D. Preference-vs-support: RR rewards ORDER, STAR rewards SUPPORT strength. See the [Divergence from STAR] block below for RCV-IRV, Approval and Plurality on the same ballots.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:A,B,C,D,E,F,G
46:2,0,3,5,4,3,0
43:2,0,4,5,5,4,0
35:5,4,2,0,0,3,3
12:0,0,4,0,2,2,5
11:1,1,3,0,1,1,5
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR                   = F
  Choose-One (Plurality) = D   (differs from STAR)
  RCV-IRV                = D   (differs from STAR)
  RCV-RR (Condorcet)     = D   (differs from STAR)
  Note: 147 of 147 ballots (100%) had equal non-zero scores, so their ranks
        were decided by candidate priority order. The RCV-IRV result may be
        an artifact of score-to-rank tie-breaking rather than a deep
        difference.
  Note: Ranked Robin (RCV-RR) sides with RCV-IRV, so STAR is the outlier
        here — STAR need not elect the Condorcet candidate.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: star_vs_rr_divergence_tabulated/darkhorse_C07_medV147_bloc_1_RCV-IRV_tabulated.txt
  RCV-RR round-robin: star_vs_rr_divergence_tabulated/darkhorse_C07_medV147_bloc_1_RCV-RR_tabulated.txt

[Runoff Reversal]
 - Score Round Winner(s) = (C)
 - Runoff Round Winner   = (F)
  Candidate C earned the highest total score, but
  Candidate F won the automatic runoff — not a malfunction,
  STAR working as designed: the runoff elects the finalist preferred
  by the majority (of voters with a preference).

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 147 ballots.
Count x A,B,C,D,E,F,G
   46 x 2,0,3,5,4,3,0
   43 x 2,0,4,5,5,4,0
   35 x 5,4,2,0,0,3,3
   12 x 0,0,4,0,2,2,5
   11 x 1,1,3,0,1,1,5

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   C             -- 461 -- First place
   F             -- 450 -- Second place
   D             -- 445
   E             -- 434
   A             -- 364
   G             -- 220
   B             -- 151
 C and F advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   F             -- 35 -- First place
   C             -- 23
   Equal Support -- 89
 F wins.
   Runoff math:
     147  ballots cast
   −  89  Equal Support (no preference between the two finalists)
     ───
      58  voters with a preference  (majority = 30)
           F 35 (60%)  ·  C 23 (40%)

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
                A > |       ---       |124 -  23 -   0 | 35 -   0 - 112 | 46 -  12 -  89 | 35 -  11 - 101 | 35 -  11 - 101 |124 -   0 -  23 |
                B > |   0 -  23 - 124 |      ---       | 35 -   0 - 112 | 46 -  12 -  89 | 35 -  11 - 101 | 35 -  11 - 101 | 35 -  89 -  23 |
              * C > | 112 -   0 -  35 |112 -   0 -  35 |      ---       | 58 -   0 -  89 | 58 -   0 -  89 | 23 -  89 -  35 | 89 -   0 -  58 |
                D > |  89 -  12 -  46 | 89 -  12 -  46 | 89 -   0 -  58 |      ---       | 46 -  78 -  23 | 89 -   0 -  58 | 89 -   0 -  58 |
                E > | 101 -  11 -  35 |101 -  11 -  35 | 89 -   0 -  58 | 23 -  78 -  46 |      ---       | 89 -  23 -  35 | 89 -   0 -  58 |
              * F > | 101 -  11 -  35 |101 -  11 -  35 | 35 -  89 -  23 | 58 -   0 -  89 | 35 -  23 -  89 |      ---       | 89 -  35 -  23 |
                G > |  23 -   0 - 124 | 23 -  89 -  35 | 58 -   0 -  89 | 58 -   0 -  89 | 58 -   0 -  89 | 23 -  35 -  89 |      ---       |

[Condorcet Winner]
  Condorcet Winner: D — STAR elected F instead (D was eliminated in the scoring round)

[Score Distribution] (how many ballots gave each star rating)
                      Score
Candidate    5    4    3    2    1    0  | Total   Avg
A           35    0    0   89   11   12  |   364   2.5
B            0   35    0    0   11  101  |   151   1.0
C            0   55   57   35    0    0  |   461   3.1
D           89    0    0    0    0   58  |   445   3.0
E           43   46    0   12   11   35  |   434   3.0
F            0   43   81   12   11    0  |   450   3.1
G           23    0   35    0    0   89  |   220   1.5
```

Everything in one file: the [`_tabulated` mirror](../star_vs_rr_divergence_tabulated/darkhorse_C07_medV147_bloc_1_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 05_Ranked_Robin/star_vs_rr_divergence/darkhorse_C07_medV147_bloc_1.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README.md)
- [Runoff reversal (worked set)](../../../01_STAR/runoff_overturns_leader/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [cycle_C03_fewV15_noise_1](cycle_C03_fewV15_noise_1.md) · [cycle_C03_fewV15_noise_2](cycle_C03_fewV15_noise_2.md) · [cycle_C03_medV45_noise_1](cycle_C03_medV45_noise_1.md) · [cycle_C03_medV45_noise_2](cycle_C03_medV45_noise_2.md) · [cycle_C05_fewV15_noise_1](cycle_C05_fewV15_noise_1.md) · [cycle_C05_fewV15_noise_2](cycle_C05_fewV15_noise_2.md) · [cycle_C05_fewV28_bloc_1](cycle_C05_fewV28_bloc_1.md) · [cycle_C05_medV45_noise_1](cycle_C05_medV45_noise_1.md) · [cycle_C05_medV45_noise_2](cycle_C05_medV45_noise_2.md) · [cycle_C07_fewV15_noise_1](cycle_C07_fewV15_noise_1.md) · [cycle_C07_fewV28_bloc_2](cycle_C07_fewV28_bloc_2.md) · [cycle_C07_largeV598_bloc_1](cycle_C07_largeV598_bloc_1.md) · [cycle_C07_medV149_bloc_2](cycle_C07_medV149_bloc_2.md) · [cycle_C10_fewV15_noise_1](cycle_C10_fewV15_noise_1.md) · [cycle_C10_fewV15_noise_2](cycle_C10_fewV15_noise_2.md) · [cycle_C10_fewV28_bloc_1](cycle_C10_fewV28_bloc_1.md) · [cycle_C10_fewV29_bloc_2](cycle_C10_fewV29_bloc_2.md) · [cycle_C10_medV148_bloc_1](cycle_C10_medV148_bloc_1.md) · [cycle_C10_medV149_bloc_2](cycle_C10_medV149_bloc_2.md) · [cycle_C10_medV45_noise_1](cycle_C10_medV45_noise_1.md) · [cycle_C10_medV45_noise_2](cycle_C10_medV45_noise_2.md) · [darkhorse_C03_fewV15_noise_1](darkhorse_C03_fewV15_noise_1.md) · [darkhorse_C05_largeV599_bloc_1](darkhorse_C05_largeV599_bloc_1.md) · [darkhorse_C07_fewV30_bloc_1](darkhorse_C07_fewV30_bloc_1.md) · [darkhorse_C07_largeV597_bloc_1](darkhorse_C07_largeV597_bloc_1.md) · [darkhorse_C07_largeV598_bloc_2](darkhorse_C07_largeV598_bloc_2.md) · [darkhorse_C07_medV45_noise_1](darkhorse_C07_medV45_noise_1.md) · [darkhorse_C10_largeV598_bloc_1](darkhorse_C10_largeV598_bloc_1.md) · [darkhorse_C10_largeV599_bloc_2](darkhorse_C10_largeV599_bloc_2.md)
