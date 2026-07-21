# STAR vs RR divergence -- 10 cands, 28 voters, cycle (STAR C, RR F)

*Generated from [`cycle_C10_fewV28_bloc_1.yaml`](../cycle_C10_fewV28_bloc_1.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** C

## Scenario

Auto-generated STAR-vs-Ranked-Robin divergence. 10 candidates, 28 voters, grouped (a few voter factions/blocs). STAR elects C; Ranked Robin elects F. CAUSE = CONDORCET CYCLE: no candidate beats all others, so there is no 'right' winner. RR falls back on Copeland/margin (F); STAR runs its two score-leaders off (C). See the [Divergence from STAR] block below for RCV-IRV, Approval and Plurality on the same ballots.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:A,B,C,D,E,F,G,H,I,J
7:0,1,3,3,4,3,5,3,2,3
7:0,1,4,4,5,5,4,5,3,4
7:2,2,5,5,3,5,0,3,3,3
7:4,4,5,5,3,4,0,4,4,4
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR   = C
  RCV-RR = F   (differs from STAR)
  Full round-by-round reports (generated for review):
  RCV-RR round-robin: star_vs_rr_divergence_tabulated/cycle_C10_fewV28_bloc_1_RCV-RR_tabulated.txt

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 28 ballots.
Count x A,B,C,D,E,F,G,H,I,J
    7 x 0,1,3,3,4,3,5,3,2,3
    7 x 0,1,4,4,5,5,4,5,3,4
    7 x 2,2,5,5,3,5,0,3,3,3
    7 x 4,4,5,5,3,4,0,4,4,4

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   C             -- 119 -- Tied for first place
   D             -- 119 -- Tied for first place
   F             -- 119 -- Tied for first place
   E             -- 105
   H             -- 105
   J             --  98
   I             --  84
   G             --  63
   B             --  56
   A             --  42
 There's a three-way tie for first.

[STAR Voting: Scoring Round: First tiebreaker]
 The two candidates preferred in the most head-to-head matchups advance.
   F             -- 14 -- First place
   C             --  7 -- Tied for second place
   D             --  7 -- Tied for second place
   Equal Support -- 14
 F advances, but there's still a two-way tie for second.

[STAR Voting: Scoring Round: Second tiebreaker]
 The candidate with the most votes of score 5 advances.
   C             -- 14 -- Tied for second place
   D             -- 14 -- Tied for second place
 There's still a two-way tie for second.

*** No official tie-breaking lot numbers were provided.
    Ties are resolved using a fallback order: CSV column order.
    Lot-number priority order: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

[Tiebreaker: Lot Number Priority]
  Tie among: ['C', 'D']
  Resolved: ['C'] (selected by lot-number priority).

[Lot-decided tie — rare]
  ⚠ The ballots did not break this tie: the deterministic rungs
    (pairwise / score, then five-star) all came back equal, so the
    pre-published LOT order chose among the tied candidates — the
    result here was set by lot, not by the votes. Usually the
    "dead rung": no tied candidate held a score-5 vote (five-star
    counts fives, not fours). Verify the tied candidates' 5-counts.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   C             -- 7 -- Tied for first place
   F             -- 7 -- Tied for first place
   Equal Support -- 14
 There's a two-way tie for first.

[STAR Voting: Automatic Runoff Round: First tiebreaker]
 The highest-scoring candidate wins.
   C             -- 119 -- Tied for first place
   F             -- 119 -- Tied for first place
 There's still a two-way tie for first.

[STAR Voting: Automatic Runoff Round: Second tiebreaker]
 The candidate with the most votes of score 5 wins.
   C             -- 14 -- Tied for first place
   F             -- 14 -- Tied for first place
 There's still a two-way tie for first.

[Tiebreaker: Lot Number Priority]
  Tie among: ['C', 'F']
  Resolved: ['C'] (selected by lot-number priority).

[Lot-decided tie — rare]
  ⚠ The ballots did not break this tie: the deterministic rungs
    (pairwise / score, then five-star) all came back equal, so the
    pre-published LOT order chose among the tied candidates — the
    result here was set by lot, not by the votes. Usually the
    "dead rung": no tied candidate held a score-5 vote (five-star
    counts fives, not fours). Verify the tied candidates' 5-counts.

[STAR Voting: Winner — STAR Voting Method (single winner)]
 C
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |       A      |      B      |    * C      |    * D      |      E      |      F      |      G      |      H      |      I      |      J      |
---------------------------------------------------------------------------------------------------------------------------------------------------------------
             A > |     ---      | 0 - 14 - 14 | 0 -  0 - 28 | 0 -  0 - 28 | 7 -  0 - 21 | 0 -  7 - 21 |14 -  0 - 14 | 0 -  7 - 21 | 0 -  7 - 21 | 0 -  7 - 21 |
             B > | 14 - 14 -  0 |    ---      | 0 -  0 - 28 | 0 -  0 - 28 | 7 -  0 - 21 | 0 -  7 - 21 |14 -  0 - 14 | 0 -  7 - 21 | 0 -  7 - 21 | 0 -  7 - 21 |
           * C > | 28 -  0 -  0 |28 -  0 -  0 |    ---      | 0 - 28 -  0 |14 -  0 - 14 | 7 - 14 -  7 |14 -  7 -  7 |14 -  7 -  7 |28 -  0 -  0 |14 - 14 -  0 |
           * D > | 28 -  0 -  0 |28 -  0 -  0 | 0 - 28 -  0 |    ---      |14 -  0 - 14 | 7 - 14 -  7 |14 -  7 -  7 |14 -  7 -  7 |28 -  0 -  0 |14 - 14 -  0 |
             E > | 21 -  0 -  7 |21 -  0 -  7 |14 -  0 - 14 |14 -  0 - 14 |    ---      | 7 -  7 - 14 |21 -  0 -  7 | 7 - 14 -  7 |14 -  7 -  7 |14 -  7 -  7 |
             F > | 21 -  7 -  0 |21 -  7 -  0 | 7 - 14 -  7 | 7 - 14 -  7 |14 -  7 -  7 |    ---      |21 -  0 -  7 | 7 - 21 -  0 |21 -  7 -  0 |14 - 14 -  0 |
             G > | 14 -  0 - 14 |14 -  0 - 14 | 7 -  7 - 14 | 7 -  7 - 14 | 7 -  0 - 21 | 7 -  0 - 21 |    ---      | 7 -  0 - 21 |14 -  0 - 14 | 7 -  7 - 14 |
             H > | 21 -  7 -  0 |21 -  7 -  0 | 7 -  7 - 14 | 7 -  7 - 14 | 7 - 14 -  7 | 0 - 21 -  7 |21 -  0 -  7 |    ---      |14 - 14 -  0 | 7 - 21 -  0 |
             I > | 21 -  7 -  0 |21 -  7 -  0 | 0 -  0 - 28 | 0 -  0 - 28 | 7 -  7 - 14 | 0 -  7 - 21 |14 -  0 - 14 | 0 - 14 - 14 |    ---      | 0 - 14 - 14 |
             J > | 21 -  7 -  0 |21 -  7 -  0 | 0 - 14 - 14 | 0 - 14 - 14 | 7 -  7 - 14 | 0 - 14 - 14 |14 -  7 -  7 | 0 - 21 -  7 |14 - 14 -  0 |    ---      |

[Condorcet Winner]
  No strict Condorcet winner; unbeaten candidates: C, D, F (pairwise ties)

[Score Distribution] (how many ballots gave each star rating)
                   Score
Candidate   5   4   3   2   1   0  | Total   Avg
A           0   7   0   7   0  14  |    42   1.5
B           0   7   0   7  14   0  |    56   2.0
C          14   7   7   0   0   0  |   119   4.3
D          14   7   7   0   0   0  |   119   4.3
E           7   7  14   0   0   0  |   105   3.8
F          14   7   7   0   0   0  |   119   4.3
G           7   7   0   0   0  14  |    63   2.3
H           7   7  14   0   0   0  |   105   3.8
I           0   7  14   7   0   0  |    84   3.0
J           0  14  14   0   0   0  |    98   3.5
```

Everything in one file: the [`_tabulated` mirror](../star_vs_rr_divergence_tabulated/cycle_C10_fewV28_bloc_1_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 05_Ranked_Robin/star_vs_rr_divergence/cycle_C10_fewV28_bloc_1.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [cycle_C03_fewV15_noise_1](cycle_C03_fewV15_noise_1.md) · [cycle_C03_fewV15_noise_2](cycle_C03_fewV15_noise_2.md) · [cycle_C03_medV45_noise_1](cycle_C03_medV45_noise_1.md) · [cycle_C03_medV45_noise_2](cycle_C03_medV45_noise_2.md) · [cycle_C05_fewV15_noise_1](cycle_C05_fewV15_noise_1.md) · [cycle_C05_fewV15_noise_2](cycle_C05_fewV15_noise_2.md) · [cycle_C05_fewV28_bloc_1](cycle_C05_fewV28_bloc_1.md) · [cycle_C05_medV45_noise_1](cycle_C05_medV45_noise_1.md) · [cycle_C05_medV45_noise_2](cycle_C05_medV45_noise_2.md) · [cycle_C07_fewV15_noise_1](cycle_C07_fewV15_noise_1.md) · [cycle_C07_fewV28_bloc_2](cycle_C07_fewV28_bloc_2.md) · [cycle_C07_largeV598_bloc_1](cycle_C07_largeV598_bloc_1.md) · [cycle_C07_medV149_bloc_2](cycle_C07_medV149_bloc_2.md) · [cycle_C10_fewV15_noise_1](cycle_C10_fewV15_noise_1.md) · [cycle_C10_fewV15_noise_2](cycle_C10_fewV15_noise_2.md) · [cycle_C10_fewV29_bloc_2](cycle_C10_fewV29_bloc_2.md) · [cycle_C10_medV148_bloc_1](cycle_C10_medV148_bloc_1.md) · [cycle_C10_medV149_bloc_2](cycle_C10_medV149_bloc_2.md) · [cycle_C10_medV45_noise_1](cycle_C10_medV45_noise_1.md) · [cycle_C10_medV45_noise_2](cycle_C10_medV45_noise_2.md) · [darkhorse_C03_fewV15_noise_1](darkhorse_C03_fewV15_noise_1.md) · [darkhorse_C05_largeV599_bloc_1](darkhorse_C05_largeV599_bloc_1.md) · [darkhorse_C07_fewV30_bloc_1](darkhorse_C07_fewV30_bloc_1.md) · [darkhorse_C07_largeV597_bloc_1](darkhorse_C07_largeV597_bloc_1.md) · [darkhorse_C07_largeV598_bloc_2](darkhorse_C07_largeV598_bloc_2.md) · [darkhorse_C07_medV147_bloc_1](darkhorse_C07_medV147_bloc_1.md) · [darkhorse_C07_medV45_noise_1](darkhorse_C07_medV45_noise_1.md) · [darkhorse_C10_largeV598_bloc_1](darkhorse_C10_largeV598_bloc_1.md) · [darkhorse_C10_largeV599_bloc_2](darkhorse_C10_largeV599_bloc_2.md)
