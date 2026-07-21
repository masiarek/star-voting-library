# STAR vs RR divergence -- 5 cands, 15 voters, cycle (STAR B, RR E)

*Generated from [`cycle_C05_fewV15_noise_1.yaml`](../cycle_C05_fewV15_noise_1.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** B

## Scenario

Auto-generated STAR-vs-Ranked-Robin divergence. 5 candidates, 15 voters, ungrouped (independent random ballots). STAR elects B; Ranked Robin elects E. CAUSE = CONDORCET CYCLE: no candidate beats all others, so there is no 'right' winner. RR falls back on Copeland/margin (E); STAR runs its two score-leaders off (B). See the [Divergence from STAR] block below for RCV-IRV, Approval and Plurality on the same ballots.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:A,B,C,D,E
1:5,3,1,1,5
1:1,1,1,3,4
1:4,4,1,4,2
1:3,4,2,2,3
1:2,5,2,4,2
1:0,4,1,0,1
1:3,2,1,1,3
1:2,0,3,2,2
1:3,1,5,3,0
1:2,1,3,1,4
1:3,2,2,3,1
1:1,1,3,0,5
1:1,2,5,2,3
1:4,5,3,2,3
1:0,2,1,1,1
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR     = B
  RCV-IRV  = A   (differs from STAR)
  Approval = E   (differs from STAR)
  RCV-RR   = E   (differs from STAR)
  Note: 15 of 15 ballots (100%) had equal non-zero scores, so their ranks
        were decided by candidate priority order. The RCV-IRV result may be
        an artifact of score-to-rank tie-breaking rather than a deep
        difference.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: star_vs_rr_divergence_tabulated/cycle_C05_fewV15_noise_1_RCV-IRV_tabulated.txt
  RCV-RR round-robin: star_vs_rr_divergence_tabulated/cycle_C05_fewV15_noise_1_RCV-RR_tabulated.txt

[Runoff Reversal]
 - Score Round Winner(s) = (E)
 - Runoff Round Winner   = (B)
  Candidate E earned the highest total score, but
  Candidate B won the automatic runoff — not a malfunction,
  STAR working as designed: the runoff elects the finalist preferred
  by the majority (of voters with a preference).

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 15 ballots.
A,B,C,D,E
5,3,1,1,5
1,1,1,3,4
4,4,1,4,2
3,4,2,2,3
2,5,2,4,2
0,4,1,0,1
3,2,1,1,3
2,0,3,2,2
3,1,5,3,0
2,1,3,1,4
3,2,2,3,1
1,1,3,0,5
1,2,5,2,3
4,5,3,2,3
0,2,1,1,1

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   E             -- 39 -- First place
   B             -- 37 -- Second place
   A             -- 34
   C             -- 34
   D             -- 29
 E and B advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   B             -- 8 -- First place
   E             -- 7
   Equal Support -- 0
 B wins.
   Runoff math:
     15  ballots cast
   −  0  Equal Support (no preference between the two finalists)
     ──
     15  voters with a preference  (majority = 8)
           B 8 (53%)  ·  E 7 (47%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 B
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |      A     |   * B     |     C     |     D     |   * E     |
-----------------------------------------------------------------------------
           A > |    ---     |6 - 3 - 6  |6 - 2 - 7  |6 - 5 - 4  |4 - 5 - 6  |
         * B > | 6 - 3 - 6  |   ---     |8 - 2 - 5  |8 - 3 - 4  |8 - 0 - 7  |
           C > | 7 - 2 - 6  |5 - 2 - 8  |   ---     |7 - 4 - 4  |4 - 4 - 7  |
           D > | 4 - 5 - 6  |4 - 3 - 8  |4 - 4 - 7  |   ---     |4 - 2 - 9  |
         * E > | 6 - 5 - 4  |7 - 0 - 8  |7 - 4 - 4  |9 - 2 - 4  |   ---     |

[Condorcet Winner]
  No strict Condorcet winner; weak Condorcet winner: B — matches the STAR winner

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
A          1  2  4  3  3  2  |    34   2.3
B          2  3  1  4  4  1  |    37   2.5
C          2  0  4  3  6  0  |    34   2.3
D          0  2  3  4  4  2  |    29   1.9
E          2  2  4  3  3  1  |    39   2.6
```

Everything in one file: the [`_tabulated` mirror](../star_vs_rr_divergence_tabulated/cycle_C05_fewV15_noise_1_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 05_Ranked_Robin/star_vs_rr_divergence/cycle_C05_fewV15_noise_1.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [cycle_C03_fewV15_noise_1](cycle_C03_fewV15_noise_1.md) · [cycle_C03_fewV15_noise_2](cycle_C03_fewV15_noise_2.md) · [cycle_C03_medV45_noise_1](cycle_C03_medV45_noise_1.md) · [cycle_C03_medV45_noise_2](cycle_C03_medV45_noise_2.md) · [cycle_C05_fewV15_noise_2](cycle_C05_fewV15_noise_2.md) · [cycle_C05_fewV28_bloc_1](cycle_C05_fewV28_bloc_1.md) · [cycle_C05_medV45_noise_1](cycle_C05_medV45_noise_1.md) · [cycle_C05_medV45_noise_2](cycle_C05_medV45_noise_2.md) · [cycle_C07_fewV15_noise_1](cycle_C07_fewV15_noise_1.md) · [cycle_C07_fewV28_bloc_2](cycle_C07_fewV28_bloc_2.md) · [cycle_C07_largeV598_bloc_1](cycle_C07_largeV598_bloc_1.md) · [cycle_C07_medV149_bloc_2](cycle_C07_medV149_bloc_2.md) · [cycle_C10_fewV15_noise_1](cycle_C10_fewV15_noise_1.md) · [cycle_C10_fewV15_noise_2](cycle_C10_fewV15_noise_2.md) · [cycle_C10_fewV28_bloc_1](cycle_C10_fewV28_bloc_1.md) · [cycle_C10_fewV29_bloc_2](cycle_C10_fewV29_bloc_2.md) · [cycle_C10_medV148_bloc_1](cycle_C10_medV148_bloc_1.md) · [cycle_C10_medV149_bloc_2](cycle_C10_medV149_bloc_2.md) · [cycle_C10_medV45_noise_1](cycle_C10_medV45_noise_1.md) · [cycle_C10_medV45_noise_2](cycle_C10_medV45_noise_2.md) · [darkhorse_C03_fewV15_noise_1](darkhorse_C03_fewV15_noise_1.md) · [darkhorse_C05_largeV599_bloc_1](darkhorse_C05_largeV599_bloc_1.md) · [darkhorse_C07_fewV30_bloc_1](darkhorse_C07_fewV30_bloc_1.md) · [darkhorse_C07_largeV597_bloc_1](darkhorse_C07_largeV597_bloc_1.md) · [darkhorse_C07_largeV598_bloc_2](darkhorse_C07_largeV598_bloc_2.md) · [darkhorse_C07_medV147_bloc_1](darkhorse_C07_medV147_bloc_1.md) · [darkhorse_C07_medV45_noise_1](darkhorse_C07_medV45_noise_1.md) · [darkhorse_C10_largeV598_bloc_1](darkhorse_C10_largeV598_bloc_1.md) · [darkhorse_C10_largeV599_bloc_2](darkhorse_C10_largeV599_bloc_2.md)
