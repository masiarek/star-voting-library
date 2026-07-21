# STAR vs RR divergence -- 10 cands, 149 voters, cycle (STAR I, RR H)

*Generated from [`cycle_C10_medV149_bloc_2.yaml`](../cycle_C10_medV149_bloc_2.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** I

## Scenario

Auto-generated STAR-vs-Ranked-Robin divergence. 10 candidates, 149 voters, grouped (a few voter factions/blocs). STAR elects I; Ranked Robin elects H. CAUSE = CONDORCET CYCLE: no candidate beats all others (A>C>J>A), so there is no 'right' winner. RR falls back on Copeland/margin (H); STAR runs its two score-leaders off (I). See the [Divergence from STAR] block below for RCV-IRV, Approval and Plurality on the same ballots.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:A,B,C,D,E,F,G,H,I,J
61:3,1,5,0,4,5,5,5,4,4
50:5,1,1,4,0,1,2,2,2,1
38:4,3,3,1,2,0,1,3,5,4
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR                   = I
  Choose-One (Plurality) = C   (differs from STAR)
  RCV-IRV                = A   (differs from STAR)
  Approval               = A   (differs from STAR)
  RCV-RR                 = H   (differs from STAR)
  Note: 149 of 149 ballots (100%) had equal non-zero scores, so their ranks
        were decided by candidate priority order. The RCV-IRV result may be
        an artifact of score-to-rank tie-breaking rather than a deep
        difference.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: star_vs_rr_divergence_tabulated/cycle_C10_medV149_bloc_2_RCV-IRV_tabulated.txt
  RCV-RR round-robin: star_vs_rr_divergence_tabulated/cycle_C10_medV149_bloc_2_RCV-RR_tabulated.txt

[Runoff Reversal]
 - Score Round Winner(s) = (A)
 - Runoff Round Winner   = (I)
  Candidate A earned the highest total score, but
  Candidate I won the automatic runoff — not a malfunction,
  STAR working as designed: the runoff elects the finalist preferred
  by the majority (of voters with a preference).

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 149 ballots.
Count x A,B,C,D,E,F,G,H,I,J
   61 x 3,1,5,0,4,5,5,5,4,4
   50 x 5,1,1,4,0,1,2,2,2,1
   38 x 4,3,3,1,2,0,1,3,5,4

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   A             -- 585 -- First place
   I             -- 534 -- Second place
   H             -- 519
   C             -- 469
   J             -- 446
   G             -- 443
   F             -- 355
   E             -- 320
   D             -- 238
   B             -- 225
 A and I advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   I             -- 99 -- First place
   A             -- 50
   Equal Support --  0
 I wins.
   Runoff math:
     149  ballots cast
   −   0  Equal Support (no preference between the two finalists)
     ───
     149  voters with a preference  (majority = 75)
           I 99 (66%)  ·  A 50 (34%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 I
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                    |       * A       |        B       |        C       |        D       |        E       |        F       |        G       |        H       |      * I       |        J       |
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
              * A > |       ---       |149 -   0 -   0 | 88 -   0 -  61 |149 -   0 -   0 | 88 -   0 -  61 | 88 -   0 -  61 | 88 -   0 -  61 | 88 -   0 -  61 | 50 -   0 -  99 | 50 -  38 -  61 |
                B > |   0 -   0 - 149 |      ---       |  0 -  88 -  61 | 99 -   0 -  50 | 88 -   0 -  61 | 38 -  50 -  61 | 38 -   0 - 111 |  0 -  38 - 111 |  0 -   0 - 149 |  0 -  50 -  99 |
                C > |  61 -   0 -  88 | 61 -  88 -   0 |      ---       | 99 -   0 -  50 |149 -   0 -   0 | 38 - 111 -   0 | 38 -  61 -  50 |  0 -  99 -  50 | 61 -   0 -  88 | 61 -  50 -  38 |
                D > |   0 -   0 - 149 | 50 -   0 -  99 | 50 -   0 -  99 |      ---       | 50 -   0 -  99 | 88 -   0 -  61 | 50 -  38 -  61 | 50 -   0 -  99 | 50 -   0 -  99 | 50 -   0 -  99 |
                E > |  61 -   0 -  88 | 61 -   0 -  88 |  0 -   0 - 149 | 99 -   0 -  50 |      ---       | 38 -   0 - 111 | 38 -   0 - 111 |  0 -   0 - 149 |  0 -  61 -  88 |  0 -  61 -  88 |
                F > |  61 -   0 -  88 | 61 -  50 -  38 |  0 - 111 -  38 | 61 -   0 -  88 |111 -   0 -  38 |      ---       |  0 -  61 -  88 |  0 -  61 -  88 | 61 -   0 -  88 | 61 -  50 -  38 |
                G > |  61 -   0 -  88 |111 -   0 -  38 | 50 -  61 -  38 | 61 -  38 -  50 |111 -   0 -  38 | 88 -  61 -   0 |      ---       |  0 - 111 -  38 | 61 -  50 -  38 |111 -   0 -  38 |
                H > |  61 -   0 -  88 |111 -  38 -   0 | 50 -  99 -   0 | 99 -   0 -  50 |149 -   0 -   0 | 88 -  61 -   0 | 38 - 111 -   0 |      ---       | 61 -  50 -  38 |111 -   0 -  38 |
              * I > |  99 -   0 -  50 |149 -   0 -   0 | 88 -   0 -  61 | 99 -   0 -  50 | 88 -  61 -   0 | 88 -   0 -  61 | 38 -  50 -  61 | 38 -  50 -  61 |      ---       | 88 -  61 -   0 |
                J > |  61 -  38 -  50 | 99 -  50 -   0 | 38 -  50 -  61 | 99 -   0 -  50 | 88 -  61 -   0 | 38 -  50 -  61 | 38 -   0 - 111 | 38 -   0 - 111 |  0 -  61 -  88 |      ---       |

[Condorcet Winner]
  No Condorcet winner (majority cycle: B > D > F > B)

[Score Distribution] (how many ballots gave each star rating)
                      Score
Candidate    5    4    3    2    1    0  | Total   Avg
A           50   38   61    0    0    0  |   585   3.9
B            0    0   38    0  111    0  |   225   1.5
C           61    0   38    0   50    0  |   469   3.1
D            0   50    0    0   38   61  |   238   1.6
E            0   61    0   38    0   50  |   320   2.1
F           61    0    0    0   50   38  |   355   2.4
G           61    0    0   50   38    0  |   443   3.0
H           61    0   38   50    0    0  |   519   3.5
I           38   61    0   50    0    0  |   534   3.6
J            0   99    0    0   50    0  |   446   3.0
```

Everything in one file: the [`_tabulated` mirror](../star_vs_rr_divergence_tabulated/cycle_C10_medV149_bloc_2_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 05_Ranked_Robin/star_vs_rr_divergence/cycle_C10_medV149_bloc_2.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [cycle_C03_fewV15_noise_1](cycle_C03_fewV15_noise_1.md) · [cycle_C03_fewV15_noise_2](cycle_C03_fewV15_noise_2.md) · [cycle_C03_medV45_noise_1](cycle_C03_medV45_noise_1.md) · [cycle_C03_medV45_noise_2](cycle_C03_medV45_noise_2.md) · [cycle_C05_fewV15_noise_1](cycle_C05_fewV15_noise_1.md) · [cycle_C05_fewV15_noise_2](cycle_C05_fewV15_noise_2.md) · [cycle_C05_fewV28_bloc_1](cycle_C05_fewV28_bloc_1.md) · [cycle_C05_medV45_noise_1](cycle_C05_medV45_noise_1.md) · [cycle_C05_medV45_noise_2](cycle_C05_medV45_noise_2.md) · [cycle_C07_fewV15_noise_1](cycle_C07_fewV15_noise_1.md) · [cycle_C07_fewV28_bloc_2](cycle_C07_fewV28_bloc_2.md) · [cycle_C07_largeV598_bloc_1](cycle_C07_largeV598_bloc_1.md) · [cycle_C07_medV149_bloc_2](cycle_C07_medV149_bloc_2.md) · [cycle_C10_fewV15_noise_1](cycle_C10_fewV15_noise_1.md) · [cycle_C10_fewV15_noise_2](cycle_C10_fewV15_noise_2.md) · [cycle_C10_fewV28_bloc_1](cycle_C10_fewV28_bloc_1.md) · [cycle_C10_fewV29_bloc_2](cycle_C10_fewV29_bloc_2.md) · [cycle_C10_medV148_bloc_1](cycle_C10_medV148_bloc_1.md) · [cycle_C10_medV45_noise_1](cycle_C10_medV45_noise_1.md) · [cycle_C10_medV45_noise_2](cycle_C10_medV45_noise_2.md) · [darkhorse_C03_fewV15_noise_1](darkhorse_C03_fewV15_noise_1.md) · [darkhorse_C05_largeV599_bloc_1](darkhorse_C05_largeV599_bloc_1.md) · [darkhorse_C07_fewV30_bloc_1](darkhorse_C07_fewV30_bloc_1.md) · [darkhorse_C07_largeV597_bloc_1](darkhorse_C07_largeV597_bloc_1.md) · [darkhorse_C07_largeV598_bloc_2](darkhorse_C07_largeV598_bloc_2.md) · [darkhorse_C07_medV147_bloc_1](darkhorse_C07_medV147_bloc_1.md) · [darkhorse_C07_medV45_noise_1](darkhorse_C07_medV45_noise_1.md) · [darkhorse_C10_largeV598_bloc_1](darkhorse_C10_largeV598_bloc_1.md) · [darkhorse_C10_largeV599_bloc_2](darkhorse_C10_largeV599_bloc_2.md)
