# STAR vs RR divergence -- 3 cands, 45 voters, cycle (STAR B, RR C)

*Generated from [`cycle_C03_medV45_noise_2.yaml`](../cycle_C03_medV45_noise_2.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** B

## Scenario

Auto-generated STAR-vs-Ranked-Robin divergence. 3 candidates, 45 voters, ungrouped (independent random ballots). STAR elects B; Ranked Robin elects C. CAUSE = CONDORCET CYCLE: no candidate beats all others, so there is no 'right' winner. RR falls back on Copeland/margin (C); STAR runs its two score-leaders off (B). See the [Divergence from STAR] block below for RCV-IRV, Approval and Plurality on the same ballots.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:A,B,C
3:1,1,1
2:4,1,4
2:0,4,3
2:5,5,3
1:3,2,2
1:3,0,1
1:0,2,2
1:1,4,3
1:2,0,4
1:1,1,3
1:4,0,5
1:2,5,1
1:2,1,5
1:1,1,4
1:3,4,3
1:3,2,4
1:4,5,1
1:2,4,3
1:0,4,4
1:3,2,1
1:4,0,0
1:3,2,0
1:5,0,1
1:3,3,4
1:1,2,1
1:1,3,2
1:3,1,1
1:4,2,2
1:1,0,4
1:3,5,2
1:2,1,2
1:2,4,4
1:1,4,0
1:2,5,3
1:0,1,2
1:1,0,3
1:4,4,4
1:0,4,0
1:0,4,2
1:4,1,3
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR                   = B
  Choose-One (Plurality) = A   (differs from STAR)
  RCV-IRV                = A   (differs from STAR)
  Approval               = C   (differs from STAR)
  RCV-RR                 = C   (differs from STAR)
  Note: 20 of 45 ballots (44%) had equal non-zero scores, so their ranks
        were decided by candidate priority order. The RCV-IRV result may be
        an artifact of score-to-rank tie-breaking rather than a deep
        difference.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: star_vs_rr_divergence_tabulated/cycle_C03_medV45_noise_2_RCV-IRV_tabulated.txt
  RCV-RR round-robin: star_vs_rr_divergence_tabulated/cycle_C03_medV45_noise_2_RCV-RR_tabulated.txt

[Runoff Reversal]
 - Score Round Winner(s) = (C)
 - Runoff Round Winner   = (B)
  Candidate C earned the highest total score, but
  Candidate B won the automatic runoff — not a malfunction,
  STAR working as designed: the runoff elects the finalist preferred
  by the majority (of voters with a preference).

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 45 ballots.
Count x A,B,C
    3 x 1,1,1
    2 x 4,1,4
    2 x 0,4,3
    2 x 5,5,3
    1 x 3,2,2
    1 x 3,0,1
    1 x 0,2,2
    1 x 1,4,3
    1 x 2,0,4
    1 x 1,1,3
    1 x 4,0,5
    1 x 2,5,1
    1 x 2,1,5
    1 x 1,1,4
    1 x 3,4,3
    1 x 3,2,4
    1 x 4,5,1
    1 x 2,4,3
    1 x 0,4,4
    1 x 3,2,1
    1 x 4,0,0
    1 x 3,2,0
    1 x 5,0,1
    1 x 3,3,4
    1 x 1,2,1
    1 x 1,3,2
    1 x 3,1,1
    1 x 4,2,2
    1 x 1,0,4
    1 x 3,5,2
    1 x 2,1,2
    1 x 2,4,4
    1 x 1,4,0
    1 x 2,5,3
    1 x 0,1,2
    1 x 1,0,3
    1 x 4,4,4
    1 x 0,4,0
    1 x 0,4,2
    1 x 4,1,3

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   C             -- 109 -- First place
   B             -- 106 -- Second place
   A             --  99
 C and B advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   B             -- 18 -- First place
   C             -- 16
   Equal Support -- 11
 B wins.
   Runoff math:
     45  ballots cast
   − 11  Equal Support (no preference between the two finalists)
     ──
     34  voters with a preference  (majority = 18)
           B 18 (53%)  ·  C 16 (47%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 B
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |       A      |    * B      |    * C      |
-------------------------------------------------------------
             A > |     ---      |18 -  9 - 18 |15 - 10 - 20 |
           * B > | 18 -  9 - 18 |    ---      |18 - 11 - 16 |
           * C > | 20 - 10 - 15 |16 - 11 - 18 |    ---      |

[Condorcet Winner]
  No strict Condorcet winner; weak Condorcet winner: B — matches the STAR winner

[Score Distribution] (how many ballots gave each star rating)
                   Score
Candidate   5   4   3   2   1   0  | Total   Avg
A           3   8   9   7  11   7  |    99   2.2
B           6  11   2   7  12   7  |   106   2.4
C           2  10  11   8  10   4  |   109   2.4
```

Everything in one file: the [`_tabulated` mirror](../star_vs_rr_divergence_tabulated/cycle_C03_medV45_noise_2_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 05_Ranked_Robin/star_vs_rr_divergence/cycle_C03_medV45_noise_2.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [cycle_C03_fewV15_noise_1](cycle_C03_fewV15_noise_1.md) · [cycle_C03_fewV15_noise_2](cycle_C03_fewV15_noise_2.md) · [cycle_C03_medV45_noise_1](cycle_C03_medV45_noise_1.md) · [cycle_C05_fewV15_noise_1](cycle_C05_fewV15_noise_1.md) · [cycle_C05_fewV15_noise_2](cycle_C05_fewV15_noise_2.md) · [cycle_C05_fewV28_bloc_1](cycle_C05_fewV28_bloc_1.md) · [cycle_C05_medV45_noise_1](cycle_C05_medV45_noise_1.md) · [cycle_C05_medV45_noise_2](cycle_C05_medV45_noise_2.md) · [cycle_C07_fewV15_noise_1](cycle_C07_fewV15_noise_1.md) · [cycle_C07_fewV28_bloc_2](cycle_C07_fewV28_bloc_2.md) · [cycle_C07_largeV598_bloc_1](cycle_C07_largeV598_bloc_1.md) · [cycle_C07_medV149_bloc_2](cycle_C07_medV149_bloc_2.md) · [cycle_C10_fewV15_noise_1](cycle_C10_fewV15_noise_1.md) · [cycle_C10_fewV15_noise_2](cycle_C10_fewV15_noise_2.md) · [cycle_C10_fewV28_bloc_1](cycle_C10_fewV28_bloc_1.md) · [cycle_C10_fewV29_bloc_2](cycle_C10_fewV29_bloc_2.md) · [cycle_C10_medV148_bloc_1](cycle_C10_medV148_bloc_1.md) · [cycle_C10_medV149_bloc_2](cycle_C10_medV149_bloc_2.md) · [cycle_C10_medV45_noise_1](cycle_C10_medV45_noise_1.md) · [cycle_C10_medV45_noise_2](cycle_C10_medV45_noise_2.md) · [darkhorse_C03_fewV15_noise_1](darkhorse_C03_fewV15_noise_1.md) · [darkhorse_C05_largeV599_bloc_1](darkhorse_C05_largeV599_bloc_1.md) · [darkhorse_C07_fewV30_bloc_1](darkhorse_C07_fewV30_bloc_1.md) · [darkhorse_C07_largeV597_bloc_1](darkhorse_C07_largeV597_bloc_1.md) · [darkhorse_C07_largeV598_bloc_2](darkhorse_C07_largeV598_bloc_2.md) · [darkhorse_C07_medV147_bloc_1](darkhorse_C07_medV147_bloc_1.md) · [darkhorse_C07_medV45_noise_1](darkhorse_C07_medV45_noise_1.md) · [darkhorse_C10_largeV598_bloc_1](darkhorse_C10_largeV598_bloc_1.md) · [darkhorse_C10_largeV599_bloc_2](darkhorse_C10_largeV599_bloc_2.md)
