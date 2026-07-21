# STAR vs RR divergence -- 3 cands, 45 voters, cycle (STAR A, RR B)

*Generated from [`cycle_C03_medV45_noise_1.yaml`](../cycle_C03_medV45_noise_1.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** A

## Scenario

Auto-generated STAR-vs-Ranked-Robin divergence. 3 candidates, 45 voters, ungrouped (independent random ballots). STAR elects A; Ranked Robin elects B. CAUSE = CONDORCET CYCLE: no candidate beats all others (A>B>C>A), so there is no 'right' winner. RR falls back on Copeland/margin (B); STAR runs its two score-leaders off (A). See the [Divergence from STAR] block below for RCV-IRV, Approval and Plurality on the same ballots.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:A,B,C
2:3,5,3
2:2,5,3
2:4,4,1
2:0,3,4
1:2,3,2
1:5,3,0
1:4,3,1
1:3,4,4
1:1,4,5
1:4,4,5
1:1,3,2
1:5,4,2
1:1,0,1
1:5,2,4
1:1,1,0
1:1,3,1
1:4,4,2
1:2,4,4
1:5,4,3
1:2,0,4
1:3,1,5
1:3,0,4
1:4,4,0
1:0,4,1
1:5,4,1
1:3,0,1
1:2,2,3
1:4,2,5
1:4,0,2
1:4,5,3
1:5,3,1
1:1,1,3
1:4,1,4
1:3,2,1
1:4,3,4
1:2,1,3
1:2,4,3
1:0,3,3
1:4,4,3
1:4,3,2
1:0,2,1
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR     = A
  Approval = B   (differs from STAR)
  RCV-RR   = B   (differs from STAR)
  Full round-by-round reports (generated for review):
  RCV-RR round-robin: star_vs_rr_divergence_tabulated/cycle_C03_medV45_noise_1_RCV-RR_tabulated.txt

[Runoff Reversal]
 - Score Round Winner(s) = (B)
 - Runoff Round Winner   = (A)
  Candidate B earned the highest total score, but
  Candidate A won the automatic runoff — not a malfunction,
  STAR working as designed: the runoff elects the finalist preferred
  by the majority (of voters with a preference).

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 45 ballots.
Count x A,B,C
    2 x 3,5,3
    2 x 2,5,3
    2 x 4,4,1
    2 x 0,3,4
    1 x 2,3,2
    1 x 5,3,0
    1 x 4,3,1
    1 x 3,4,4
    1 x 1,4,5
    1 x 4,4,5
    1 x 1,3,2
    1 x 5,4,2
    1 x 1,0,1
    1 x 5,2,4
    1 x 1,1,0
    1 x 1,3,1
    1 x 4,4,2
    1 x 2,4,4
    1 x 5,4,3
    1 x 2,0,4
    1 x 3,1,5
    1 x 3,0,4
    1 x 4,4,0
    1 x 0,4,1
    1 x 5,4,1
    1 x 3,0,1
    1 x 2,2,3
    1 x 4,2,5
    1 x 4,0,2
    1 x 4,5,3
    1 x 5,3,1
    1 x 1,1,3
    1 x 4,1,4
    1 x 3,2,1
    1 x 4,3,4
    1 x 2,1,3
    1 x 2,4,3
    1 x 0,3,3
    1 x 4,4,3
    1 x 4,3,2
    1 x 0,2,1

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   B             -- 129 -- First place
   A             -- 125 -- Second place
   C             -- 115
 B and A advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   A             -- 19 -- First place
   B             -- 17
   Equal Support --  9
 A wins.
   Runoff math:
     45  ballots cast
   −  9  Equal Support (no preference between the two finalists)
     ──
     36  voters with a preference  (majority = 19)
           A 19 (53%)  ·  B 17 (47%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 A
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |     * A      |    * B      |      C      |
-------------------------------------------------------------
           * A > |     ---      |19 -  9 - 17 |18 -  7 - 20 |
           * B > | 17 -  9 - 19 |    ---      |25 -  3 - 17 |
             C > | 20 -  7 - 18 |17 -  3 - 25 |    ---      |

[Condorcet Winner]
  No Condorcet winner (majority cycle: A > B > C > A)

[Score Distribution] (how many ballots gave each star rating)
                   Score
Candidate   5   4   3   2   1   0  | Total   Avg
A           6  13   7   8   6   5  |   125   2.8
B           5  14  11   5   5   5  |   129   2.9
C           4   9  12   6  11   3  |   115   2.6
```

Everything in one file: the [`_tabulated` mirror](../star_vs_rr_divergence_tabulated/cycle_C03_medV45_noise_1_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 05_Ranked_Robin/star_vs_rr_divergence/cycle_C03_medV45_noise_1.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [cycle_C03_fewV15_noise_1](cycle_C03_fewV15_noise_1.md) · [cycle_C03_fewV15_noise_2](cycle_C03_fewV15_noise_2.md) · [cycle_C03_medV45_noise_2](cycle_C03_medV45_noise_2.md) · [cycle_C05_fewV15_noise_1](cycle_C05_fewV15_noise_1.md) · [cycle_C05_fewV15_noise_2](cycle_C05_fewV15_noise_2.md) · [cycle_C05_fewV28_bloc_1](cycle_C05_fewV28_bloc_1.md) · [cycle_C05_medV45_noise_1](cycle_C05_medV45_noise_1.md) · [cycle_C05_medV45_noise_2](cycle_C05_medV45_noise_2.md) · [cycle_C07_fewV15_noise_1](cycle_C07_fewV15_noise_1.md) · [cycle_C07_fewV28_bloc_2](cycle_C07_fewV28_bloc_2.md) · [cycle_C07_largeV598_bloc_1](cycle_C07_largeV598_bloc_1.md) · [cycle_C07_medV149_bloc_2](cycle_C07_medV149_bloc_2.md) · [cycle_C10_fewV15_noise_1](cycle_C10_fewV15_noise_1.md) · [cycle_C10_fewV15_noise_2](cycle_C10_fewV15_noise_2.md) · [cycle_C10_fewV28_bloc_1](cycle_C10_fewV28_bloc_1.md) · [cycle_C10_fewV29_bloc_2](cycle_C10_fewV29_bloc_2.md) · [cycle_C10_medV148_bloc_1](cycle_C10_medV148_bloc_1.md) · [cycle_C10_medV149_bloc_2](cycle_C10_medV149_bloc_2.md) · [cycle_C10_medV45_noise_1](cycle_C10_medV45_noise_1.md) · [cycle_C10_medV45_noise_2](cycle_C10_medV45_noise_2.md) · [darkhorse_C03_fewV15_noise_1](darkhorse_C03_fewV15_noise_1.md) · [darkhorse_C05_largeV599_bloc_1](darkhorse_C05_largeV599_bloc_1.md) · [darkhorse_C07_fewV30_bloc_1](darkhorse_C07_fewV30_bloc_1.md) · [darkhorse_C07_largeV597_bloc_1](darkhorse_C07_largeV597_bloc_1.md) · [darkhorse_C07_largeV598_bloc_2](darkhorse_C07_largeV598_bloc_2.md) · [darkhorse_C07_medV147_bloc_1](darkhorse_C07_medV147_bloc_1.md) · [darkhorse_C07_medV45_noise_1](darkhorse_C07_medV45_noise_1.md) · [darkhorse_C10_largeV598_bloc_1](darkhorse_C10_largeV598_bloc_1.md) · [darkhorse_C10_largeV599_bloc_2](darkhorse_C10_largeV599_bloc_2.md)
