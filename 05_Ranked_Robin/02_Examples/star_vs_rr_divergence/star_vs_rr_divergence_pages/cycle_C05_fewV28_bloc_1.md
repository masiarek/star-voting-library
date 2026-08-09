---
search:
  exclude: true
---

# STAR vs RR divergence -- 5 cands, 28 voters, cycle (STAR A, RR C)

*Generated from [`cycle_C05_fewV28_bloc_1.yaml`](../cycle_C05_fewV28_bloc_1.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../../01_STAR/01_Learn/README.md) · **1 seat** · **Expected winner:** A

## Scenario

Auto-generated STAR-vs-Ranked-Robin divergence. 5 candidates, 28 voters, grouped (a few voter factions/blocs). STAR elects A; Ranked Robin elects C. CAUSE = CONDORCET CYCLE: no candidate beats all others, so there is no 'right' winner. RR falls back on Copeland/margin (C); STAR runs its two score-leaders off (A). See the [Divergence from STAR] block below for RCV-IRV, Approval and Plurality on the same ballots.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:A,B,C,D,E
7:0,5,1,3,1
7:5,0,2,0,4
7:5,0,2,0,4
7:0,1,5,3,1
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
[Divergence from STAR]
  STAR   = A
  RCV-RR = C   (differs from STAR)
  Full round-by-round reports (generated for review):
  RCV-RR round-robin: star_vs_rr_divergence_tabulated/cycle_C05_fewV28_bloc_1_RCV-RR_tabulated.txt

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 28 ballots.
Count × A,B,C,D,E
   14 × 5,0,2,0,4
    7 × 0,5,1,3,1
    7 × 0,1,5,3,1

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   A             -- 70 -- Tied for first place
   C             -- 70 -- Tied for first place
   E             -- 70 -- Tied for first place
   B             -- 42
   D             -- 42
 There's a three-way tie for first.

[STAR Voting: Scoring Round: First tiebreaker]
 The two candidates preferred in the most head-to-head matchups advance.
   A             -- 28 -- First place
   E             -- 28 -- Second place
   C             -- 21
   Equal Support --  0
 A and E advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   A             -- 14 -- Tied for first place
   E             -- 14 -- Tied for first place
   Equal Support --  0
 There's a two-way tie for first.

[STAR Voting: Automatic Runoff Round: First tiebreaker]
 The highest-scoring candidate wins.
   A             -- 70 -- Tied for first place
   E             -- 70 -- Tied for first place
 There's still a two-way tie for first.

[STAR Voting: Automatic Runoff Round: Second tiebreaker]
 The candidate with the most votes of score 5 wins.
   A             -- 14 -- First place
   E             --  0
 A wins.

[STAR Voting: Winner — STAR Voting Method (single winner)]
 A
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
        Note: A, C and E tied at 70 in the Scoring Round, and the head-to-head
              rung advanced A and E. The * marks who advanced, not who scored
              highest.

                 |     * A      |      B      |      C      |      D      |    * E      |
-----------------------------------------------------------------------------------------
           * A > |     ---      |14 -  0 - 14 |14 -  0 - 14 |14 -  0 - 14 |14 -  0 - 14 |
             B > | 14 -  0 - 14 |    ---      | 7 -  0 - 21 | 7 - 14 -  7 | 7 -  7 - 14 |
             C > | 14 -  0 - 14 |21 -  0 -  7 |    ---      |21 -  0 -  7 | 7 -  7 - 14 |
             D > | 14 -  0 - 14 | 7 - 14 -  7 | 7 -  0 - 21 |    ---      |14 -  0 - 14 |
           * E > | 14 -  0 - 14 |14 -  7 -  7 |14 -  7 -  7 |14 -  0 - 14 |    ---      |

[Condorcet Winner]
  No strict Condorcet winner; unbeaten candidates: A, E (pairwise ties)

[Condorcet Loser]
  No strict Condorcet loser; jointly weak Condorcet losers: A, B, D (winless — pairwise ties) — A elected by STAR, Choose-One (Plurality), Approval!

[Score Distribution] (how many ballots gave each star rating)
                   Score
Candidate   5   4   3   2   1   0  | Total   Avg
A          14   0   0   0   0  14  |    70   2.5
B           7   0   0   0   7  14  |    42   1.5
C           7   0   0  14   7   0  |    70   2.5
D           0   0  14   0   0  14  |    42   1.5
E           0  14   0   0  14   0  |    70   2.5
```

Everything in one file: the [`_tabulated` mirror](../star_vs_rr_divergence_tabulated/cycle_C05_fewV28_bloc_1_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 05_Ranked_Robin/02_Examples/star_vs_rr_divergence/cycle_C05_fewV28_bloc_1.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Condorcet efficiency (topic hub)](../../../../07_Concepts/topics/condorcet/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [cycle_C03_fewV15_noise_1](cycle_C03_fewV15_noise_1.md) · [cycle_C03_fewV15_noise_2](cycle_C03_fewV15_noise_2.md) · [cycle_C03_medV45_noise_1](cycle_C03_medV45_noise_1.md) · [cycle_C03_medV45_noise_2](cycle_C03_medV45_noise_2.md) · [cycle_C05_fewV15_noise_1](cycle_C05_fewV15_noise_1.md) · [cycle_C05_fewV15_noise_2](cycle_C05_fewV15_noise_2.md) · [cycle_C05_medV45_noise_1](cycle_C05_medV45_noise_1.md) · [cycle_C05_medV45_noise_2](cycle_C05_medV45_noise_2.md) · [cycle_C07_fewV15_noise_1](cycle_C07_fewV15_noise_1.md) · [cycle_C07_fewV28_bloc_2](cycle_C07_fewV28_bloc_2.md) · [cycle_C07_largeV598_bloc_1](cycle_C07_largeV598_bloc_1.md) · [cycle_C07_medV149_bloc_2](cycle_C07_medV149_bloc_2.md) · [cycle_C10_fewV15_noise_1](cycle_C10_fewV15_noise_1.md) · [cycle_C10_fewV15_noise_2](cycle_C10_fewV15_noise_2.md) · [cycle_C10_fewV28_bloc_1](cycle_C10_fewV28_bloc_1.md) · [cycle_C10_fewV29_bloc_2](cycle_C10_fewV29_bloc_2.md) · [cycle_C10_medV148_bloc_1](cycle_C10_medV148_bloc_1.md) · [cycle_C10_medV149_bloc_2](cycle_C10_medV149_bloc_2.md) · [cycle_C10_medV45_noise_1](cycle_C10_medV45_noise_1.md) · [cycle_C10_medV45_noise_2](cycle_C10_medV45_noise_2.md) · [darkhorse_C03_fewV15_noise_1](darkhorse_C03_fewV15_noise_1.md) · [darkhorse_C05_largeV599_bloc_1](darkhorse_C05_largeV599_bloc_1.md) · [darkhorse_C07_fewV30_bloc_1](darkhorse_C07_fewV30_bloc_1.md) · [darkhorse_C07_largeV597_bloc_1](darkhorse_C07_largeV597_bloc_1.md) · [darkhorse_C07_largeV598_bloc_2](darkhorse_C07_largeV598_bloc_2.md) · [darkhorse_C07_medV147_bloc_1](darkhorse_C07_medV147_bloc_1.md) · [darkhorse_C07_medV45_noise_1](darkhorse_C07_medV45_noise_1.md) · [darkhorse_C10_largeV598_bloc_1](darkhorse_C10_largeV598_bloc_1.md) · [darkhorse_C10_largeV599_bloc_2](darkhorse_C10_largeV599_bloc_2.md)
