# STAR vs RR divergence -- 7 cands, 598 voters, darkhorse (STAR E, RR G)

*Generated from [`darkhorse_C07_largeV598_bloc_2.yaml`](../darkhorse_C07_largeV598_bloc_2.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** E

## Scenario

Auto-generated STAR-vs-Ranked-Robin divergence. 7 candidates, 598 voters, grouped (a few voter factions/blocs). STAR elects E; Ranked Robin elects G. CAUSE = DARK HORSE: G is the Condorcet winner (beats every rival head-to-head) but only #4 of 7 by score total (1910 vs leader F 2226) -- a broadly-liked, low-intensity compromise that misses STAR's score finalists (F, E). STAR elects runoff winner E; RR elects the Condorcet winner G. Preference-vs-support: RR rewards ORDER, STAR rewards SUPPORT strength. See the [Divergence from STAR] block below for RCV-IRV, Approval and Plurality on the same ballots.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:A,B,C,D,E,F,G
382:3,0,3,3,4,3,5
122:5,1,0,1,3,5,0
94:4,5,1,1,3,5,0
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR                   = E
  Choose-One (Plurality) = G   (differs from STAR)
  RCV-IRV                = G   (differs from STAR)
  Approval               = A   (differs from STAR)
  RCV-RR (Condorcet)     = G   (differs from STAR)
  Note: 598 of 598 ballots (100%) had equal non-zero scores, so their ranks
        were decided by candidate priority order. The RCV-IRV result may be
        an artifact of score-to-rank tie-breaking rather than a deep
        difference.
  Note: Ranked Robin (RCV-RR) sides with RCV-IRV, so STAR is the outlier
        here — STAR need not elect the Condorcet candidate.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: star_vs_rr_divergence_tabulated/darkhorse_C07_largeV598_bloc_2_RCV-IRV_tabulated.txt
  RCV-RR round-robin: star_vs_rr_divergence_tabulated/darkhorse_C07_largeV598_bloc_2_RCV-RR_tabulated.txt

[Runoff Reversal]
 - Score Round Winner(s) = (F)
 - Runoff Round Winner   = (E)
  Candidate F earned the highest total score, but
  Candidate E won the automatic runoff — not a malfunction,
  STAR working as designed: the runoff elects the finalist preferred
  by the majority (of voters with a preference).

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 598 ballots.
Count x A,B,C,D,E,F,G
  382 x 3,0,3,3,4,3,5
  122 x 5,1,0,1,3,5,0
   94 x 4,5,1,1,3,5,0

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   F             -- 2226 -- First place
   E             -- 2176 -- Second place
   A             -- 2132
   G             -- 1910
   D             -- 1362
   C             -- 1240
   B             --  592
 F and E advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   E             -- 382 -- First place
   F             -- 216
   Equal Support --   0
 E wins.
   Runoff math:
     598  ballots cast
   −   0  Equal Support (no preference between the two finalists)
     ───
     598  voters with a preference  (majority = 300)
           E 382 (64%)  ·  F 216 (36%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 E
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                    |         A       |        B       |        C       |        D       |      * E       |      * F       |        G       |
---------------------------------------------------------------------------------------------------------------------------------------------
                A > |       ---       |504 -   0 -  94 |216 - 382 -   0 |216 - 382 -   0 |216 -   0 - 382 |  0 - 504 -  94 |216 -   0 - 382 |
                B > |  94 -   0 - 504 |      ---       |216 -   0 - 382 | 94 - 122 - 382 | 94 -   0 - 504 |  0 -  94 - 504 |216 -   0 - 382 |
                C > |   0 - 382 - 216 |382 -   0 - 216 |      ---       |  0 - 476 - 122 |  0 -   0 - 598 |  0 - 382 - 216 | 94 - 122 - 382 |
                D > |   0 - 382 - 216 |382 - 122 -  94 |122 - 476 -   0 |      ---       |  0 -   0 - 598 |  0 - 382 - 216 |216 -   0 - 382 |
              * E > | 382 -   0 - 216 |504 -   0 -  94 |598 -   0 -   0 |598 -   0 -   0 |      ---       |382 -   0 - 216 |216 -   0 - 382 |
              * F > |  94 - 504 -   0 |504 -  94 -   0 |216 - 382 -   0 |216 - 382 -   0 |216 -   0 - 382 |      ---       |216 -   0 - 382 |
                G > | 382 -   0 - 216 |382 -   0 - 216 |382 - 122 -  94 |382 -   0 - 216 |382 -   0 - 216 |382 -   0 - 216 |      ---       |

[Condorcet Winner]
  Condorcet Winner: G — STAR elected E instead (G was eliminated in the scoring round)

[Score Distribution] (how many ballots gave each star rating)
                      Score
Candidate    5    4    3    2    1    0  | Total   Avg
A          122   94  382    0    0    0  |  2132   3.6
B           94    0    0    0  122  382  |   592   1.0
C            0    0  382    0   94  122  |  1240   2.1
D            0    0  382    0  216    0  |  1362   2.3
E            0  382  216    0    0    0  |  2176   3.6
F          216    0  382    0    0    0  |  2226   3.7
G          382    0    0    0    0  216  |  1910   3.2
```

Everything in one file: the [`_tabulated` mirror](../star_vs_rr_divergence_tabulated/darkhorse_C07_largeV598_bloc_2_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 05_Ranked_Robin/star_vs_rr_divergence/darkhorse_C07_largeV598_bloc_2.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README.md)
- [Runoff reversal (worked set)](../../../01_STAR/runoff_overturns_leader/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [cycle_C03_fewV15_noise_1](cycle_C03_fewV15_noise_1.md) · [cycle_C03_fewV15_noise_2](cycle_C03_fewV15_noise_2.md) · [cycle_C03_medV45_noise_1](cycle_C03_medV45_noise_1.md) · [cycle_C03_medV45_noise_2](cycle_C03_medV45_noise_2.md) · [cycle_C05_fewV15_noise_1](cycle_C05_fewV15_noise_1.md) · [cycle_C05_fewV15_noise_2](cycle_C05_fewV15_noise_2.md) · [cycle_C05_fewV28_bloc_1](cycle_C05_fewV28_bloc_1.md) · [cycle_C05_medV45_noise_1](cycle_C05_medV45_noise_1.md) · [cycle_C05_medV45_noise_2](cycle_C05_medV45_noise_2.md) · [cycle_C07_fewV15_noise_1](cycle_C07_fewV15_noise_1.md) · [cycle_C07_fewV28_bloc_2](cycle_C07_fewV28_bloc_2.md) · [cycle_C07_largeV598_bloc_1](cycle_C07_largeV598_bloc_1.md) · [cycle_C07_medV149_bloc_2](cycle_C07_medV149_bloc_2.md) · [cycle_C10_fewV15_noise_1](cycle_C10_fewV15_noise_1.md) · [cycle_C10_fewV15_noise_2](cycle_C10_fewV15_noise_2.md) · [cycle_C10_fewV28_bloc_1](cycle_C10_fewV28_bloc_1.md) · [cycle_C10_fewV29_bloc_2](cycle_C10_fewV29_bloc_2.md) · [cycle_C10_medV148_bloc_1](cycle_C10_medV148_bloc_1.md) · [cycle_C10_medV149_bloc_2](cycle_C10_medV149_bloc_2.md) · [cycle_C10_medV45_noise_1](cycle_C10_medV45_noise_1.md) · [cycle_C10_medV45_noise_2](cycle_C10_medV45_noise_2.md) · [darkhorse_C03_fewV15_noise_1](darkhorse_C03_fewV15_noise_1.md) · [darkhorse_C05_largeV599_bloc_1](darkhorse_C05_largeV599_bloc_1.md) · [darkhorse_C07_fewV30_bloc_1](darkhorse_C07_fewV30_bloc_1.md) · [darkhorse_C07_largeV597_bloc_1](darkhorse_C07_largeV597_bloc_1.md) · [darkhorse_C07_medV147_bloc_1](darkhorse_C07_medV147_bloc_1.md) · [darkhorse_C07_medV45_noise_1](darkhorse_C07_medV45_noise_1.md) · [darkhorse_C10_largeV598_bloc_1](darkhorse_C10_largeV598_bloc_1.md) · [darkhorse_C10_largeV599_bloc_2](darkhorse_C10_largeV599_bloc_2.md)
