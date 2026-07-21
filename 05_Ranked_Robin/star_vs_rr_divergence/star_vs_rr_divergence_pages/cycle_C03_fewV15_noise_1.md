# STAR vs RR divergence -- 3 cands, 15 voters, cycle (STAR A, RR B)

*Generated from [`cycle_C03_fewV15_noise_1.yaml`](../cycle_C03_fewV15_noise_1.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** A

## Scenario

Auto-generated STAR-vs-Ranked-Robin divergence. 3 candidates, 15 voters, ungrouped (independent random ballots). STAR elects A; Ranked Robin elects B. CAUSE = CONDORCET CYCLE: no candidate beats all others, so there is no 'right' winner. RR falls back on Copeland/margin (B); STAR runs its two score-leaders off (A). See the [Divergence from STAR] block below for RCV-IRV, Approval and Plurality on the same ballots.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:A,B,C
2:1,5,1
1:1,3,2
1:4,1,5
1:3,2,1
1:0,1,1
1:1,2,2
1:2,4,0
1:5,2,5
1:4,0,4
1:5,5,1
1:3,1,0
1:3,4,3
1:5,3,4
1:4,3,4
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR   = A
  RCV-RR = B   (differs from STAR)
  Full round-by-round reports (generated for review):
  RCV-RR round-robin: star_vs_rr_divergence_tabulated/cycle_C03_fewV15_noise_1_RCV-RR_tabulated.txt

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 15 ballots.
Count x A,B,C
    2 x 1,5,1
    1 x 1,3,2
    1 x 4,1,5
    1 x 3,2,1
    1 x 0,1,1
    1 x 1,2,2
    1 x 2,4,0
    1 x 5,2,5
    1 x 4,0,4
    1 x 5,5,1
    1 x 3,1,0
    1 x 3,4,3
    1 x 5,3,4
    1 x 4,3,4

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   A             -- 42 -- First place
   B             -- 41 -- Second place
   C             -- 34
 A and B advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   A             -- 7 -- Tied for first place
   B             -- 7 -- Tied for first place
   Equal Support -- 1
 There's a two-way tie for first.

[STAR Voting: Automatic Runoff Round: First tiebreaker]
 The highest-scoring candidate wins.
   A             -- 42 -- First place
   B             -- 41
 A wins.

[STAR Voting: Winner — STAR Voting Method (single winner)]
 A
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |    * A     |   * B     |     C     |
-----------------------------------------------------
         * A > |    ---     |7 - 1 - 7  |5 - 6 - 4  |
         * B > | 7 - 1 - 7  |   ---     |8 - 2 - 5  |
           C > | 4 - 6 - 5  |5 - 2 - 8  |   ---     |

[Condorcet Winner]
  No strict Condorcet winner; unbeaten candidates: A, B (pairwise ties)

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
A          3  3  3  1  4  1  |    42   2.8
B          3  2  3  3  3  1  |    41   2.7
C          2  3  1  2  5  2  |    34   2.3
```

Everything in one file: the [`_tabulated` mirror](../star_vs_rr_divergence_tabulated/cycle_C03_fewV15_noise_1_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 05_Ranked_Robin/star_vs_rr_divergence/cycle_C03_fewV15_noise_1.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [cycle_C03_fewV15_noise_2](cycle_C03_fewV15_noise_2.md) · [cycle_C03_medV45_noise_1](cycle_C03_medV45_noise_1.md) · [cycle_C03_medV45_noise_2](cycle_C03_medV45_noise_2.md) · [cycle_C05_fewV15_noise_1](cycle_C05_fewV15_noise_1.md) · [cycle_C05_fewV15_noise_2](cycle_C05_fewV15_noise_2.md) · [cycle_C05_fewV28_bloc_1](cycle_C05_fewV28_bloc_1.md) · [cycle_C05_medV45_noise_1](cycle_C05_medV45_noise_1.md) · [cycle_C05_medV45_noise_2](cycle_C05_medV45_noise_2.md) · [cycle_C07_fewV15_noise_1](cycle_C07_fewV15_noise_1.md) · [cycle_C07_fewV28_bloc_2](cycle_C07_fewV28_bloc_2.md) · [cycle_C07_largeV598_bloc_1](cycle_C07_largeV598_bloc_1.md) · [cycle_C07_medV149_bloc_2](cycle_C07_medV149_bloc_2.md) · [cycle_C10_fewV15_noise_1](cycle_C10_fewV15_noise_1.md) · [cycle_C10_fewV15_noise_2](cycle_C10_fewV15_noise_2.md) · [cycle_C10_fewV28_bloc_1](cycle_C10_fewV28_bloc_1.md) · [cycle_C10_fewV29_bloc_2](cycle_C10_fewV29_bloc_2.md) · [cycle_C10_medV148_bloc_1](cycle_C10_medV148_bloc_1.md) · [cycle_C10_medV149_bloc_2](cycle_C10_medV149_bloc_2.md) · [cycle_C10_medV45_noise_1](cycle_C10_medV45_noise_1.md) · [cycle_C10_medV45_noise_2](cycle_C10_medV45_noise_2.md) · [darkhorse_C03_fewV15_noise_1](darkhorse_C03_fewV15_noise_1.md) · [darkhorse_C05_largeV599_bloc_1](darkhorse_C05_largeV599_bloc_1.md) · [darkhorse_C07_fewV30_bloc_1](darkhorse_C07_fewV30_bloc_1.md) · [darkhorse_C07_largeV597_bloc_1](darkhorse_C07_largeV597_bloc_1.md) · [darkhorse_C07_largeV598_bloc_2](darkhorse_C07_largeV598_bloc_2.md) · [darkhorse_C07_medV147_bloc_1](darkhorse_C07_medV147_bloc_1.md) · [darkhorse_C07_medV45_noise_1](darkhorse_C07_medV45_noise_1.md) · [darkhorse_C10_largeV598_bloc_1](darkhorse_C10_largeV598_bloc_1.md) · [darkhorse_C10_largeV599_bloc_2](darkhorse_C10_largeV599_bloc_2.md)
