# Dead rung — scoring round, dead five-star rung, cap 2

*Generated from [`dead_rung_scoring_dead_cap2.yaml`](../dead_rung_scoring_dead_cap2.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Ann

**Official tie-break (lot) order:** Ann > Ben > Cara — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

Generated dead-rung scenario (scoring round, 'dead' five-star rung). no 5 anywhere (capped at 2) -> five-star 0-0 -> the LOT picks the 2nd finalist. STAR's second rung counts only score-5 votes and never steps down to 4s; when it can't separate the tied candidates the lot decides. See 01_STAR/tie_break_dead_rung/README.md and 00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Ann,Ben,Cara
2,2,1
2,0,1
```

## What the engine says

Full report from the [`_tabulated` mirror](../tie_break_dead_rung_tabulated/dead_rung_scoring_dead_cap2_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |   * Ann    |  * Ben    |    Cara   |
-----------------------------------------------------
       * Ann > |    ---     |1 - 1 - 0  |2 - 0 - 0  |
       * Ben > | 0 - 1 - 1  |   ---     |1 - 0 - 1  |
        Cara > | 0 - 0 - 2  |1 - 0 - 1  |   ---     |

[Condorcet Winner]
  Condorcet Winner: Ann — matches the STAR winner

--- STAR Voting Method (single winner) ---
[STAR Voting]
 Tabulating 2 ballots.
Ann,Ben,Cara
  2,  2,   1
  2,  0,   1

[Score Distribution] (number of ballots giving each score)
      5  4  3  2  1  0  | Total   Avg
Ann   0  0  0  2  0  0  |     4   2.0
Ben   0  0  0  1  0  1  |     2   1.0
Cara  0  0  0  0  2  0  |     2   1.0

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Ann           -- 4 -- First place
   Ben           -- 2 -- Tied for second place
   Cara          -- 2 -- Tied for second place
 Ann advances, but there's a two-way tie for second.

[STAR Voting: Scoring Round: First tiebreaker]
 The candidate preferred in the most head-to-head matchups advances.
   Ben           -- 1 -- Tied for second place
   Cara          -- 1 -- Tied for second place
   Equal Support -- 0
 There's still a two-way tie for second.

[STAR Voting: Scoring Round: Second tiebreaker]
 The candidate with the most votes of score 5 advances.
   Ben           -- 0 -- Tied for second place
   Cara          -- 0 -- Tied for second place
 There's still a two-way tie for second.

*(Ties are resolved by choosing the tied candidate with the highest-priority official lot number.)*
    Lot-number priority order: ['Ann', 'Ben', 'Cara']

[Tiebreaker: Lot Number Priority]
  Tie among: ['Ben', 'Cara']
  Resolved: ['Ben'] (selected by lot-number priority).

[Lot-decided tie — rare]
  ⚠ The ballots did not break this tie: the deterministic rungs
    (pairwise / score, then five-star) all came back equal, so the
    pre-published LOT order chose among the tied candidates — the
    result here was set by lot, not by the votes. Usually the
    "dead rung": no tied candidate held a score-5 vote (five-star
    counts fives, not fours). Verify the tied candidates' 5-counts.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Ann           -- 1 -- First place
   Ben           -- 0
   Equal Support -- 1
 Ann wins.
   Runoff math:
     2  ballots cast
   − 1  Equal Support (no preference between the two finalists)
     ─
     1  voters with a preference  (majority = 1)
           Ann 1 (100%)  ·  Ben 0 (0%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Ann
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/tie_break_dead_rung/dead_rung_scoring_dead_cap2.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Ties & tie-breaking (topic hub)](../../../00_start_here/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [dead_rung_scoring_dead_cap3](dead_rung_scoring_dead_cap3.md) · [dead_rung_scoring_dead_cap4](dead_rung_scoring_dead_cap4.md) · [tie_break_01_scoring_five_star_breaks](tie_break_01_scoring_five_star_breaks.md) · [tie_break_02_scoring_no_fives_to_lot](tie_break_02_scoring_no_fives_to_lot.md) · [tie_break_03_runoff_no_fives_to_lot](tie_break_03_runoff_no_fives_to_lot.md) · [tie_break_04_runoff_five_star_breaks](tie_break_04_runoff_five_star_breaks.md) · [tie_break_05_scoring_five_star_vs_adversarial_lot](tie_break_05_scoring_five_star_vs_adversarial_lot.md) · [tie_break_06_scoring_dead_rung_adversarial_lot](tie_break_06_scoring_dead_rung_adversarial_lot.md) · [tie_break_07_runoff_five_star_vs_adversarial_lot](tie_break_07_runoff_five_star_vs_adversarial_lot.md) · [tie_break_08_runoff_dead_rung_adversarial_lot](tie_break_08_runoff_dead_rung_adversarial_lot.md) · [tie_break_09_five_star_tied_nonzero](tie_break_09_five_star_tied_nonzero.md)
