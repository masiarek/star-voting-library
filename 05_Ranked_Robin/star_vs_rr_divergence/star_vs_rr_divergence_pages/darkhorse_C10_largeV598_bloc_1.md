# STAR vs RR divergence -- 10 cands, 598 voters, darkhorse (STAR G, RR F)

*Generated from [`darkhorse_C10_largeV598_bloc_1.yaml`](../darkhorse_C10_largeV598_bloc_1.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** G

## Scenario

Auto-generated STAR-vs-Ranked-Robin divergence. 10 candidates, 598 voters, grouped (a few voter factions/blocs). STAR elects G; Ranked Robin elects F. CAUSE = DARK HORSE: F is the Condorcet winner (beats every rival head-to-head) but only #9 of 10 by score total (1647 vs leader G 1929) -- a broadly-liked, low-intensity compromise that misses STAR's score finalists (G, C). STAR elects runoff winner G; RR elects the Condorcet winner F. Preference-vs-support: RR rewards ORDER, STAR rewards SUPPORT strength. See the [Divergence from STAR] block below for RCV-IRV, Approval and Plurality on the same ballots.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:A,B,C,D,E,F,G,H,I,J
288:2,4,2,3,4,5,4,2,0,2
219:5,2,5,2,1,0,2,5,4,4
66:1,1,1,5,5,2,4,1,0,3
25:4,5,5,3,2,3,3,4,0,3
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR                   = G
  Choose-One (Plurality) = F   (differs from STAR)
  RCV-IRV                = F   (differs from STAR)
  Approval               = D   (differs from STAR)
  RCV-RR (Condorcet)     = F   (differs from STAR)
  Note: 598 of 598 ballots (100%) had equal non-zero scores, so their ranks
        were decided by candidate priority order. The RCV-IRV result may be
        an artifact of score-to-rank tie-breaking rather than a deep
        difference.
  Note: Ranked Robin (RCV-RR) sides with RCV-IRV, so STAR is the outlier
        here — STAR need not elect the Condorcet candidate.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: star_vs_rr_divergence_tabulated/darkhorse_C10_largeV598_bloc_1_RCV-IRV_tabulated.txt
  RCV-RR round-robin: star_vs_rr_divergence_tabulated/darkhorse_C10_largeV598_bloc_1_RCV-RR_tabulated.txt

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 598 ballots.
Count x A,B,C,D,E,F,G,H,I,J
  288 x 2,4,2,3,4,5,4,2,0,2
  219 x 5,2,5,2,1,0,2,5,4,4
   66 x 1,1,1,5,5,2,4,1,0,3
   25 x 4,5,5,3,2,3,3,4,0,3

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   G             -- 1929 -- First place
   C             -- 1862 -- Second place
   A             -- 1837
   H             -- 1837
   B             -- 1781
   E             -- 1751
   J             -- 1725
   D             -- 1707
   F             -- 1647
   I             --  876
 G and C advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   G             -- 354 -- First place
   C             -- 244
   Equal Support --   0
 G wins.
   Runoff math:
     598  ballots cast
   −   0  Equal Support (no preference between the two finalists)
     ───
     598  voters with a preference  (majority = 300)
           G 354 (59%)  ·  C 244 (41%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 G
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                    |         A       |        B       |      * C       |        D       |        E       |        F       |      * G       |        H       |        I       |        J       |
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                A > |       ---       |219 -  66 - 313 |  0 - 573 -  25 |244 -   0 - 354 |244 -   0 - 354 |244 -   0 - 354 |244 -   0 - 354 |  0 - 598 -   0 |598 -   0 -   0 |244 - 288 -  66 |
                B > | 313 -  66 - 219 |      ---       |288 -  91 - 219 |313 - 219 -  66 |244 - 288 -  66 |244 -   0 - 354 | 25 - 507 -  66 |313 -  66 - 219 |379 -   0 - 219 |313 -   0 - 285 |
              * C > |  25 - 573 -   0 |219 -  91 - 288 |      ---       |244 -   0 - 354 |244 -   0 - 354 |244 -   0 - 354 |244 -   0 - 354 | 25 - 573 -   0 |598 -   0 -   0 |244 - 288 -  66 |
                D > | 354 -   0 - 244 | 66 - 219 - 313 |354 -   0 - 244 |      ---       |244 -  66 - 288 |285 -  25 - 288 | 66 - 244 - 288 |354 -   0 - 244 |379 -   0 - 219 |354 -  25 - 219 |
                E > | 354 -   0 - 244 | 66 - 288 - 244 |354 -   0 - 244 |288 -  66 - 244 |      ---       |285 -   0 - 313 | 66 - 288 - 244 |354 -   0 - 244 |379 -   0 - 219 |354 -   0 - 244 |
                F > | 354 -   0 - 244 |354 -   0 - 244 |354 -   0 - 244 |288 -  25 - 285 |313 -   0 - 285 |      ---       |288 -  25 - 285 |354 -   0 - 244 |379 -   0 - 219 |288 -  25 - 285 |
              * G > | 354 -   0 - 244 | 66 - 507 -  25 |354 -   0 - 244 |288 - 244 -  66 |244 - 288 -  66 |285 -  25 - 288 |      ---       |354 -   0 - 244 |379 -   0 - 219 |354 -  25 - 219 |
                H > |   0 - 598 -   0 |219 -  66 - 313 |  0 - 573 -  25 |244 -   0 - 354 |244 -   0 - 354 |244 -   0 - 354 |244 -   0 - 354 |      ---       |598 -   0 -   0 |244 - 288 -  66 |
                I > |   0 -   0 - 598 |219 -   0 - 379 |  0 -   0 - 598 |219 -   0 - 379 |219 -   0 - 379 |219 -   0 - 379 |219 -   0 - 379 |  0 -   0 - 598 |      ---       |  0 - 219 - 379 |
                J > |  66 - 288 - 244 |285 -   0 - 313 | 66 - 288 - 244 |219 -  25 - 354 |244 -   0 - 354 |285 -  25 - 288 |219 -  25 - 354 | 66 - 288 - 244 |379 - 219 -   0 |      ---       |

[Condorcet Winner]
  Condorcet Winner: F — STAR elected G instead (F was eliminated in the scoring round)

[Score Distribution] (how many ballots gave each star rating)
                      Score
Candidate    5    4    3    2    1    0  | Total   Avg
A          219   25    0  288   66    0  |  1837   3.1
B           25  288    0  219   66    0  |  1781   3.0
C          244    0    0  288   66    0  |  1862   3.1
D           66    0  313  219    0    0  |  1707   2.9
E           66  288    0   25  219    0  |  1751   2.9
F          288    0   25   66    0  219  |  1647   2.8
G            0  354   25  219    0    0  |  1929   3.2
H          219   25    0  288   66    0  |  1837   3.1
I            0  219    0    0    0  379  |   876   1.5
J            0  219   91  288    0    0  |  1725   2.9
```

Everything in one file: the [`_tabulated` mirror](../star_vs_rr_divergence_tabulated/darkhorse_C10_largeV598_bloc_1_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 05_Ranked_Robin/star_vs_rr_divergence/darkhorse_C10_largeV598_bloc_1.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README.md)
- [Runoff reversal (worked set)](../../../01_STAR/runoff_overturns_leader/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [cycle_C03_fewV15_noise_1](cycle_C03_fewV15_noise_1.md) · [cycle_C03_fewV15_noise_2](cycle_C03_fewV15_noise_2.md) · [cycle_C03_medV45_noise_1](cycle_C03_medV45_noise_1.md) · [cycle_C03_medV45_noise_2](cycle_C03_medV45_noise_2.md) · [cycle_C05_fewV15_noise_1](cycle_C05_fewV15_noise_1.md) · [cycle_C05_fewV15_noise_2](cycle_C05_fewV15_noise_2.md) · [cycle_C05_fewV28_bloc_1](cycle_C05_fewV28_bloc_1.md) · [cycle_C05_medV45_noise_1](cycle_C05_medV45_noise_1.md) · [cycle_C05_medV45_noise_2](cycle_C05_medV45_noise_2.md) · [cycle_C07_fewV15_noise_1](cycle_C07_fewV15_noise_1.md) · [cycle_C07_fewV28_bloc_2](cycle_C07_fewV28_bloc_2.md) · [cycle_C07_largeV598_bloc_1](cycle_C07_largeV598_bloc_1.md) · [cycle_C07_medV149_bloc_2](cycle_C07_medV149_bloc_2.md) · [cycle_C10_fewV15_noise_1](cycle_C10_fewV15_noise_1.md) · [cycle_C10_fewV15_noise_2](cycle_C10_fewV15_noise_2.md) · [cycle_C10_fewV28_bloc_1](cycle_C10_fewV28_bloc_1.md) · [cycle_C10_fewV29_bloc_2](cycle_C10_fewV29_bloc_2.md) · [cycle_C10_medV148_bloc_1](cycle_C10_medV148_bloc_1.md) · [cycle_C10_medV149_bloc_2](cycle_C10_medV149_bloc_2.md) · [cycle_C10_medV45_noise_1](cycle_C10_medV45_noise_1.md) · [cycle_C10_medV45_noise_2](cycle_C10_medV45_noise_2.md) · [darkhorse_C03_fewV15_noise_1](darkhorse_C03_fewV15_noise_1.md) · [darkhorse_C05_largeV599_bloc_1](darkhorse_C05_largeV599_bloc_1.md) · [darkhorse_C07_fewV30_bloc_1](darkhorse_C07_fewV30_bloc_1.md) · [darkhorse_C07_largeV597_bloc_1](darkhorse_C07_largeV597_bloc_1.md) · [darkhorse_C07_largeV598_bloc_2](darkhorse_C07_largeV598_bloc_2.md) · [darkhorse_C07_medV147_bloc_1](darkhorse_C07_medV147_bloc_1.md) · [darkhorse_C07_medV45_noise_1](darkhorse_C07_medV45_noise_1.md) · [darkhorse_C10_largeV599_bloc_2](darkhorse_C10_largeV599_bloc_2.md)
