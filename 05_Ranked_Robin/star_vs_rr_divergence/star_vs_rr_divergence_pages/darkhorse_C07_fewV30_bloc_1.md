# STAR vs RR divergence -- 7 cands, 30 voters, darkhorse (STAR D, RR C)

*Generated from [`darkhorse_C07_fewV30_bloc_1.yaml`](../darkhorse_C07_fewV30_bloc_1.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** D

## Scenario

Auto-generated STAR-vs-Ranked-Robin divergence. 7 candidates, 30 voters, grouped (a few voter factions/blocs). STAR elects D; Ranked Robin elects C. CAUSE = DARK HORSE: C is the Condorcet winner (beats every rival head-to-head) but only #3 of 7 by score total (96 vs leader D 114) -- a broadly-liked, low-intensity compromise that misses STAR's score finalists (D, A). STAR elects runoff winner D; RR elects the Condorcet winner C. Preference-vs-support: RR rewards ORDER, STAR rewards SUPPORT strength. See the [Divergence from STAR] block below for RCV-IRV, Approval and Plurality on the same ballots.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:A,B,C,D,E,F,G
6:5,3,1,4,0,4,3
6:2,2,5,3,0,2,0
6:3,3,5,4,0,2,1
6:5,3,0,4,0,5,3
6:3,4,5,4,0,2,2
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR                   = D
  Choose-One (Plurality) = C   (differs from STAR)
  RCV-IRV                = C   (differs from STAR)
  RCV-RR (Condorcet)     = C   (differs from STAR)
  Note: 30 of 30 ballots (100%) had equal non-zero scores, so their ranks
        were decided by candidate priority order. The RCV-IRV result may be
        an artifact of score-to-rank tie-breaking rather than a deep
        difference.
  Note: Ranked Robin (RCV-RR) sides with RCV-IRV, so STAR is the outlier
        here — STAR need not elect the Condorcet candidate.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: star_vs_rr_divergence_tabulated/darkhorse_C07_fewV30_bloc_1_RCV-IRV_tabulated.txt
  RCV-RR round-robin: star_vs_rr_divergence_tabulated/darkhorse_C07_fewV30_bloc_1_RCV-RR_tabulated.txt

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 30 ballots.
Count x A,B,C,D,E,F,G
    6 x 5,3,1,4,0,4,3
    6 x 2,2,5,3,0,2,0
    6 x 3,3,5,4,0,2,1
    6 x 5,3,0,4,0,5,3
    6 x 3,4,5,4,0,2,2

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   D             -- 114 -- First place
   A             -- 108 -- Second place
   C             --  96
   B             --  90
   F             --  90
   G             --  54
   E             --   0
 D and A advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   D             -- 18 -- First place
   A             -- 12
   Equal Support --  0
 D wins.
   Runoff math:
     30  ballots cast
   −  0  Equal Support (no preference between the two finalists)
     ──
     30  voters with a preference  (majority = 16)
           D 18 (60%)  ·  A 12 (40%)

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
           * A > |     ---      |12 - 12 -  6 |12 -  0 - 18 |12 -  0 - 18 |30 -  0 -  0 |18 - 12 -  0 |30 -  0 -  0 |
             B > |  6 - 12 - 12 |    ---      |12 -  0 - 18 | 0 -  6 - 24 |30 -  0 -  0 |12 -  6 - 12 |18 - 12 -  0 |
             C > | 18 -  0 - 12 |18 -  0 - 12 |    ---      |18 -  0 - 12 |24 -  6 -  0 |18 -  0 - 12 |18 -  0 - 12 |
           * D > | 18 -  0 - 12 |24 -  6 -  0 |12 -  0 - 18 |    ---      |30 -  0 -  0 |18 -  6 -  6 |30 -  0 -  0 |
             E > |  0 -  0 - 30 | 0 -  0 - 30 | 0 -  6 - 24 | 0 -  0 - 30 |    ---      | 0 -  0 - 30 | 0 -  6 - 24 |
             F > |  0 - 12 - 18 |12 -  6 - 12 |12 -  0 - 18 | 6 -  6 - 18 |30 -  0 -  0 |    ---      |24 -  6 -  0 |
             G > |  0 -  0 - 30 | 0 - 12 - 18 |12 -  0 - 18 | 0 -  0 - 30 |24 -  6 -  0 | 0 -  6 - 24 |    ---      |

[Condorcet Winner]
  Condorcet Winner: C — STAR elected D instead (C was eliminated in the scoring round)

[Score Distribution] (how many ballots gave each star rating)
                   Score
Candidate   5   4   3   2   1   0  | Total   Avg
A          12   0  12   6   0   0  |   108   3.6
B           0   6  18   6   0   0  |    90   3.0
C          18   0   0   0   6   6  |    96   3.2
D           0  24   6   0   0   0  |   114   3.8
E           0   0   0   0   0  30  |     0   0.0
F           6   6   0  18   0   0  |    90   3.0
G           0   0  12   6   6   6  |    54   1.8
```

Everything in one file: the [`_tabulated` mirror](../star_vs_rr_divergence_tabulated/darkhorse_C07_fewV30_bloc_1_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 05_Ranked_Robin/star_vs_rr_divergence/darkhorse_C07_fewV30_bloc_1.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README.md)
- [Runoff reversal (worked set)](../../../01_STAR/runoff_overturns_leader/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [cycle_C03_fewV15_noise_1](cycle_C03_fewV15_noise_1.md) · [cycle_C03_fewV15_noise_2](cycle_C03_fewV15_noise_2.md) · [cycle_C03_medV45_noise_1](cycle_C03_medV45_noise_1.md) · [cycle_C03_medV45_noise_2](cycle_C03_medV45_noise_2.md) · [cycle_C05_fewV15_noise_1](cycle_C05_fewV15_noise_1.md) · [cycle_C05_fewV15_noise_2](cycle_C05_fewV15_noise_2.md) · [cycle_C05_fewV28_bloc_1](cycle_C05_fewV28_bloc_1.md) · [cycle_C05_medV45_noise_1](cycle_C05_medV45_noise_1.md) · [cycle_C05_medV45_noise_2](cycle_C05_medV45_noise_2.md) · [cycle_C07_fewV15_noise_1](cycle_C07_fewV15_noise_1.md) · [cycle_C07_fewV28_bloc_2](cycle_C07_fewV28_bloc_2.md) · [cycle_C07_largeV598_bloc_1](cycle_C07_largeV598_bloc_1.md) · [cycle_C07_medV149_bloc_2](cycle_C07_medV149_bloc_2.md) · [cycle_C10_fewV15_noise_1](cycle_C10_fewV15_noise_1.md) · [cycle_C10_fewV15_noise_2](cycle_C10_fewV15_noise_2.md) · [cycle_C10_fewV28_bloc_1](cycle_C10_fewV28_bloc_1.md) · [cycle_C10_fewV29_bloc_2](cycle_C10_fewV29_bloc_2.md) · [cycle_C10_medV148_bloc_1](cycle_C10_medV148_bloc_1.md) · [cycle_C10_medV149_bloc_2](cycle_C10_medV149_bloc_2.md) · [cycle_C10_medV45_noise_1](cycle_C10_medV45_noise_1.md) · [cycle_C10_medV45_noise_2](cycle_C10_medV45_noise_2.md) · [darkhorse_C03_fewV15_noise_1](darkhorse_C03_fewV15_noise_1.md) · [darkhorse_C05_largeV599_bloc_1](darkhorse_C05_largeV599_bloc_1.md) · [darkhorse_C07_largeV597_bloc_1](darkhorse_C07_largeV597_bloc_1.md) · [darkhorse_C07_largeV598_bloc_2](darkhorse_C07_largeV598_bloc_2.md) · [darkhorse_C07_medV147_bloc_1](darkhorse_C07_medV147_bloc_1.md) · [darkhorse_C07_medV45_noise_1](darkhorse_C07_medV45_noise_1.md) · [darkhorse_C10_largeV598_bloc_1](darkhorse_C10_largeV598_bloc_1.md) · [darkhorse_C10_largeV599_bloc_2](darkhorse_C10_largeV599_bloc_2.md)
