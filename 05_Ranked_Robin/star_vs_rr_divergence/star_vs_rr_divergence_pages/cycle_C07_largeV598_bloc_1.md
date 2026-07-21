# STAR vs RR divergence -- 7 cands, 598 voters, cycle (STAR C, RR E)

*Generated from [`cycle_C07_largeV598_bloc_1.yaml`](../cycle_C07_largeV598_bloc_1.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** C

## Scenario

Auto-generated STAR-vs-Ranked-Robin divergence. 7 candidates, 598 voters, grouped (a few voter factions/blocs). STAR elects C; Ranked Robin elects E. CAUSE = CONDORCET CYCLE: no candidate beats all others (B>C>E>B), so there is no 'right' winner. RR falls back on Copeland/margin (E); STAR runs its two score-leaders off (C). See the [Divergence from STAR] block below for RCV-IRV, Approval and Plurality on the same ballots.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:A,B,C,D,E,F,G
215:5,3,5,0,4,3,1
177:3,5,4,2,4,4,0
146:3,4,3,2,4,5,0
60:3,2,3,0,4,5,3
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR                   = C
  Choose-One (Plurality) = A   (differs from STAR)
  RCV-IRV                = F   (differs from STAR)
  Approval               = A   (differs from STAR)
  RCV-RR                 = E   (differs from STAR)
  Note: 598 of 598 ballots (100%) had equal non-zero scores, so their ranks
        were decided by candidate priority order. The RCV-IRV result may be
        an artifact of score-to-rank tie-breaking rather than a deep
        difference.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: star_vs_rr_divergence_tabulated/cycle_C07_largeV598_bloc_1_RCV-IRV_tabulated.txt
  RCV-RR round-robin: star_vs_rr_divergence_tabulated/cycle_C07_largeV598_bloc_1_RCV-RR_tabulated.txt

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 598 ballots.
Count x A,B,C,D,E,F,G
  215 x 5,3,5,0,4,3,1
  177 x 3,5,4,2,4,4,0
  146 x 3,4,3,2,4,5,0
   60 x 3,2,3,0,4,5,3

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   C             -- 2401 -- First place
   E             -- 2392 -- Second place
   F             -- 2383
   B             -- 2234
   A             -- 2224
   D             --  646
   G             --  395
 C and E advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   C             -- 215 -- First place
   E             -- 206
   Equal Support -- 177
 C wins.
   Runoff math:
     598  ballots cast
   − 177  Equal Support (no preference between the two finalists)
     ───
     421  voters with a preference  (majority = 211)
           C 215 (51%)  ·  E 206 (49%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 C
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                    |         A       |        B       |      * C       |        D       |      * E       |        F       |        G       |
---------------------------------------------------------------------------------------------------------------------------------------------
                A > |       ---       |275 -   0 - 323 |  0 - 421 - 177 |598 -   0 -   0 |215 -   0 - 383 |215 -   0 - 383 |538 -  60 -   0 |
                B > | 323 -   0 - 275 |      ---       |323 -   0 - 275 |598 -   0 -   0 |177 - 146 - 275 |177 - 215 - 206 |538 -   0 -  60 |
              * C > | 177 - 421 -   0 |275 -   0 - 323 |      ---       |598 -   0 -   0 |215 - 177 - 206 |215 - 177 - 206 |538 -  60 -   0 |
                D > |   0 -   0 - 598 |  0 -   0 - 598 |  0 -   0 - 598 |      ---       |  0 -   0 - 598 |  0 -   0 - 598 |323 -   0 - 275 |
              * E > | 383 -   0 - 215 |275 - 146 - 177 |206 - 177 - 215 |598 -   0 -   0 |      ---       |215 - 177 - 206 |598 -   0 -   0 |
                F > | 383 -   0 - 215 |206 - 215 - 177 |206 - 177 - 215 |598 -   0 -   0 |206 - 177 - 215 |      ---       |598 -   0 -   0 |
                G > |   0 -  60 - 538 | 60 -   0 - 538 |  0 -  60 - 538 |275 -   0 - 323 |  0 -   0 - 598 |  0 -   0 - 598 |      ---       |

[Condorcet Winner]
  No Condorcet winner (majority cycle: B > C > E > B)

[Score Distribution] (how many ballots gave each star rating)
                      Score
Candidate    5    4    3    2    1    0  | Total   Avg
A          215    0  383    0    0    0  |  2224   3.7
B          177  146  215   60    0    0  |  2234   3.7
C          215  177  206    0    0    0  |  2401   4.0
D            0    0    0  323    0  275  |   646   1.1
E            0  598    0    0    0    0  |  2392   4.0
F          206  177  215    0    0    0  |  2383   4.0
G            0    0   60    0  215  323  |   395   0.7
```

Everything in one file: the [`_tabulated` mirror](../star_vs_rr_divergence_tabulated/cycle_C07_largeV598_bloc_1_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 05_Ranked_Robin/star_vs_rr_divergence/cycle_C07_largeV598_bloc_1.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [cycle_C03_fewV15_noise_1](cycle_C03_fewV15_noise_1.md) · [cycle_C03_fewV15_noise_2](cycle_C03_fewV15_noise_2.md) · [cycle_C03_medV45_noise_1](cycle_C03_medV45_noise_1.md) · [cycle_C03_medV45_noise_2](cycle_C03_medV45_noise_2.md) · [cycle_C05_fewV15_noise_1](cycle_C05_fewV15_noise_1.md) · [cycle_C05_fewV15_noise_2](cycle_C05_fewV15_noise_2.md) · [cycle_C05_fewV28_bloc_1](cycle_C05_fewV28_bloc_1.md) · [cycle_C05_medV45_noise_1](cycle_C05_medV45_noise_1.md) · [cycle_C05_medV45_noise_2](cycle_C05_medV45_noise_2.md) · [cycle_C07_fewV15_noise_1](cycle_C07_fewV15_noise_1.md) · [cycle_C07_fewV28_bloc_2](cycle_C07_fewV28_bloc_2.md) · [cycle_C07_medV149_bloc_2](cycle_C07_medV149_bloc_2.md) · [cycle_C10_fewV15_noise_1](cycle_C10_fewV15_noise_1.md) · [cycle_C10_fewV15_noise_2](cycle_C10_fewV15_noise_2.md) · [cycle_C10_fewV28_bloc_1](cycle_C10_fewV28_bloc_1.md) · [cycle_C10_fewV29_bloc_2](cycle_C10_fewV29_bloc_2.md) · [cycle_C10_medV148_bloc_1](cycle_C10_medV148_bloc_1.md) · [cycle_C10_medV149_bloc_2](cycle_C10_medV149_bloc_2.md) · [cycle_C10_medV45_noise_1](cycle_C10_medV45_noise_1.md) · [cycle_C10_medV45_noise_2](cycle_C10_medV45_noise_2.md) · [darkhorse_C03_fewV15_noise_1](darkhorse_C03_fewV15_noise_1.md) · [darkhorse_C05_largeV599_bloc_1](darkhorse_C05_largeV599_bloc_1.md) · [darkhorse_C07_fewV30_bloc_1](darkhorse_C07_fewV30_bloc_1.md) · [darkhorse_C07_largeV597_bloc_1](darkhorse_C07_largeV597_bloc_1.md) · [darkhorse_C07_largeV598_bloc_2](darkhorse_C07_largeV598_bloc_2.md) · [darkhorse_C07_medV147_bloc_1](darkhorse_C07_medV147_bloc_1.md) · [darkhorse_C07_medV45_noise_1](darkhorse_C07_medV45_noise_1.md) · [darkhorse_C10_largeV598_bloc_1](darkhorse_C10_largeV598_bloc_1.md) · [darkhorse_C10_largeV599_bloc_2](darkhorse_C10_largeV599_bloc_2.md)
