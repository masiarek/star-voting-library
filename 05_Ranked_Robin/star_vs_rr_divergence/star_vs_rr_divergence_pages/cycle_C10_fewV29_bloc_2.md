# STAR vs RR divergence -- 10 cands, 29 voters, cycle (STAR A, RR B)

*Generated from [`cycle_C10_fewV29_bloc_2.yaml`](../cycle_C10_fewV29_bloc_2.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** A

## Scenario

Auto-generated STAR-vs-Ranked-Robin divergence. 10 candidates, 29 voters, grouped (a few voter factions/blocs). STAR elects A; Ranked Robin elects B. CAUSE = CONDORCET CYCLE: no candidate beats all others (A>I>G>A), so there is no 'right' winner. RR falls back on Copeland/margin (B); STAR runs its two score-leaders off (A). See the [Divergence from STAR] block below for RCV-IRV, Approval and Plurality on the same ballots.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:A,B,C,D,E,F,G,H,I,J
11:4,5,4,3,3,4,5,1,3,0
9:3,0,2,3,4,2,1,0,3,5
9:4,5,5,4,3,5,4,5,5,0
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR                   = C
  Choose-One (Plurality) = B   (differs from STAR)
  RCV-IRV                = B   (differs from STAR)
  Approval               = A   (differs from STAR)
  RCV-RR                 = B   (differs from STAR)
  Note: 29 of 29 ballots (100%) had equal non-zero scores, so their ranks
        were decided by candidate priority order. The RCV-IRV result may be
        an artifact of score-to-rank tie-breaking rather than a deep
        difference.
  Note: Ranked Robin (RCV-RR) sides with RCV-IRV, so STAR is the outlier
        here — STAR need not elect the Condorcet candidate.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: star_vs_rr_divergence_tabulated/cycle_C10_fewV29_bloc_2_RCV-IRV_tabulated.txt
  RCV-RR round-robin: star_vs_rr_divergence_tabulated/cycle_C10_fewV29_bloc_2_RCV-RR_tabulated.txt

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 29 ballots.
Count x A,B,C,D,E,F,G,H,I,J
   11 x 4,5,4,3,3,4,5,1,3,0
    9 x 3,0,2,3,4,2,1,0,3,5
    9 x 4,5,5,4,3,5,4,5,5,0

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   A             -- 107 -- Tied for first place
   C             -- 107 -- Tied for first place
   F             -- 107 -- Tied for first place
   I             -- 105
   B             -- 100
   G             -- 100
   D             --  96
   E             --  96
   H             --  56
   J             --  45
 There's a three-way tie for first.

[STAR Voting: Scoring Round: First tiebreaker]
 The two candidates preferred in the most head-to-head matchups advance.
   A             -- 18 -- First place
   C             --  9 -- Tied for second place
   F             --  9 -- Tied for second place
   Equal Support -- 11
 A advances, but there's still a two-way tie for second.

[STAR Voting: Scoring Round: Second tiebreaker]
 The candidate with the most votes of score 5 advances.
   C             -- 9 -- Tied for second place
   F             -- 9 -- Tied for second place
 There's still a two-way tie for second.

*** No official tie-breaking lot numbers were provided.
    Ties are resolved using a fallback order: CSV column order.
    Lot-number priority order: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

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

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   A             -- 9 -- Tied for first place
   C             -- 9 -- Tied for first place
   Equal Support -- 11
 There's a two-way tie for first.

[STAR Voting: Automatic Runoff Round: First tiebreaker]
 The highest-scoring candidate wins.
   A             -- 107 -- Tied for first place
   C             -- 107 -- Tied for first place
 There's still a two-way tie for first.

[STAR Voting: Automatic Runoff Round: Second tiebreaker]
 The candidate with the most votes of score 5 wins.
   C             -- 9 -- First place
   A             -- 0
 C wins.

[STAR Voting: Winner — STAR Voting Method (single winner)]
 C
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |     * A      |      B      |    * C      |      D      |      E      |      F      |      G      |      H      |      I      |      J      |
---------------------------------------------------------------------------------------------------------------------------------------------------------------
           * A > |     ---      | 9 -  0 - 20 | 9 - 11 -  9 |11 - 18 -  0 |20 -  0 -  9 | 9 - 11 -  9 | 9 -  9 - 11 |20 -  0 -  9 |11 -  9 -  9 |20 -  0 -  9 |
             B > | 20 -  0 -  9 |    ---      |11 -  9 -  9 |20 -  0 -  9 |20 -  0 -  9 |11 -  9 -  9 | 9 - 11 -  9 |11 - 18 -  0 |11 -  9 -  9 |20 -  0 -  9 |
           * C > |  9 - 11 -  9 | 9 -  9 - 11 |    ---      |20 -  0 -  9 |20 -  0 -  9 | 0 - 29 -  0 |18 -  0 - 11 |20 -  9 -  0 |11 -  9 -  9 |20 -  0 -  9 |
             D > |  0 - 18 - 11 | 9 -  0 - 20 | 9 -  0 - 20 |    ---      | 9 - 11 -  9 | 9 -  0 - 20 | 9 -  9 - 11 |20 -  0 -  9 | 0 - 20 -  9 |20 -  0 -  9 |
             E > |  9 -  0 - 20 | 9 -  0 - 20 | 9 -  0 - 20 | 9 - 11 -  9 |    ---      | 9 -  0 - 20 | 9 -  0 - 20 |20 -  0 -  9 | 9 - 11 -  9 |20 -  0 -  9 |
             F > |  9 - 11 -  9 | 9 -  9 - 11 | 0 - 29 -  0 |20 -  0 -  9 |20 -  0 -  9 |    ---      |18 -  0 - 11 |20 -  9 -  0 |11 -  9 -  9 |20 -  0 -  9 |
             G > | 11 -  9 -  9 | 9 - 11 -  9 |11 -  0 - 18 |11 -  9 -  9 |20 -  0 -  9 |11 -  0 - 18 |    ---      |20 -  0 -  9 |11 -  0 - 18 |20 -  0 -  9 |
             H > |  9 -  0 - 20 | 0 - 18 - 11 | 0 -  9 - 20 | 9 -  0 - 20 | 9 -  0 - 20 | 0 -  9 - 20 | 9 -  0 - 20 |    ---      | 0 -  9 - 20 |20 -  0 -  9 |
             I > |  9 -  9 - 11 | 9 -  9 - 11 | 9 -  9 - 11 | 9 - 20 -  0 | 9 - 11 -  9 | 9 -  9 - 11 |18 -  0 - 11 |20 -  9 -  0 |    ---      |20 -  0 -  9 |
             J > |  9 -  0 - 20 | 9 -  0 - 20 | 9 -  0 - 20 | 9 -  0 - 20 | 9 -  0 - 20 | 9 -  0 - 20 | 9 -  0 - 20 | 9 -  0 - 20 | 9 -  0 - 20 |    ---      |

[Condorcet Winner]
  No strict Condorcet winner; weak Condorcet winner: B — STAR elected C instead (B was eliminated in the scoring round)

[Score Distribution] (how many ballots gave each star rating)
                   Score
Candidate   5   4   3   2   1   0  | Total   Avg
A           0  20   9   0   0   0  |   107   3.7
B          20   0   0   0   0   9  |   100   3.4
C           9  11   0   9   0   0  |   107   3.7
D           0   9  20   0   0   0  |    96   3.3
E           0   9  20   0   0   0  |    96   3.3
F           9  11   0   9   0   0  |   107   3.7
G          11   9   0   0   9   0  |   100   3.4
H           9   0   0   0  11   9  |    56   1.9
I           9   0  20   0   0   0  |   105   3.6
J           9   0   0   0   0  20  |    45   1.6
```

Everything in one file: the [`_tabulated` mirror](../star_vs_rr_divergence_tabulated/cycle_C10_fewV29_bloc_2_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 05_Ranked_Robin/star_vs_rr_divergence/cycle_C10_fewV29_bloc_2.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [cycle_C03_fewV15_noise_1](cycle_C03_fewV15_noise_1.md) · [cycle_C03_fewV15_noise_2](cycle_C03_fewV15_noise_2.md) · [cycle_C03_medV45_noise_1](cycle_C03_medV45_noise_1.md) · [cycle_C03_medV45_noise_2](cycle_C03_medV45_noise_2.md) · [cycle_C05_fewV15_noise_1](cycle_C05_fewV15_noise_1.md) · [cycle_C05_fewV15_noise_2](cycle_C05_fewV15_noise_2.md) · [cycle_C05_fewV28_bloc_1](cycle_C05_fewV28_bloc_1.md) · [cycle_C05_medV45_noise_1](cycle_C05_medV45_noise_1.md) · [cycle_C05_medV45_noise_2](cycle_C05_medV45_noise_2.md) · [cycle_C07_fewV15_noise_1](cycle_C07_fewV15_noise_1.md) · [cycle_C07_fewV28_bloc_2](cycle_C07_fewV28_bloc_2.md) · [cycle_C07_largeV598_bloc_1](cycle_C07_largeV598_bloc_1.md) · [cycle_C07_medV149_bloc_2](cycle_C07_medV149_bloc_2.md) · [cycle_C10_fewV15_noise_1](cycle_C10_fewV15_noise_1.md) · [cycle_C10_fewV15_noise_2](cycle_C10_fewV15_noise_2.md) · [cycle_C10_fewV28_bloc_1](cycle_C10_fewV28_bloc_1.md) · [cycle_C10_medV148_bloc_1](cycle_C10_medV148_bloc_1.md) · [cycle_C10_medV149_bloc_2](cycle_C10_medV149_bloc_2.md) · [cycle_C10_medV45_noise_1](cycle_C10_medV45_noise_1.md) · [cycle_C10_medV45_noise_2](cycle_C10_medV45_noise_2.md) · [darkhorse_C03_fewV15_noise_1](darkhorse_C03_fewV15_noise_1.md) · [darkhorse_C05_largeV599_bloc_1](darkhorse_C05_largeV599_bloc_1.md) · [darkhorse_C07_fewV30_bloc_1](darkhorse_C07_fewV30_bloc_1.md) · [darkhorse_C07_largeV597_bloc_1](darkhorse_C07_largeV597_bloc_1.md) · [darkhorse_C07_largeV598_bloc_2](darkhorse_C07_largeV598_bloc_2.md) · [darkhorse_C07_medV147_bloc_1](darkhorse_C07_medV147_bloc_1.md) · [darkhorse_C07_medV45_noise_1](darkhorse_C07_medV45_noise_1.md) · [darkhorse_C10_largeV598_bloc_1](darkhorse_C10_largeV598_bloc_1.md) · [darkhorse_C10_largeV599_bloc_2](darkhorse_C10_largeV599_bloc_2.md)
