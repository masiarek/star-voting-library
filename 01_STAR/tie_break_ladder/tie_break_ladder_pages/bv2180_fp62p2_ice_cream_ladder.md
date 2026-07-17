# Ice cream ladder — a STAR tie in both rounds, settled without the lot (BV2180, fp62p2)

*Generated from [`bv2180_fp62p2_ice_cream_ladder.yaml`](../bv2180_fp62p2_ice_cream_ladder.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Strawberry

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/fp62p2) · **[results ↗](https://bettervoting.com/fp62p2/results)** (election `fp62p2`).

## Scenario

The worked example behind the STAR tie-breaking doc (the two-round, two-ladder
tiebreak), now a live BetterVoting election. Two voters, six flavors. Scoring
round: Strawberry leads at 7; Chocolate, Chocolate Chip and Vanilla tie for the
second finalist slot at 5 each. Pairwise can't separate the three (all 2), so
the FIVE-STAR rung decides — only Chocolate Chip earned a 5, so it advances with
Strawberry. The automatic runoff then ties 1-1 head-to-head, and the SCORE rung
breaks it: Strawberry 7 beats Chocolate Chip 5. Winner: Strawberry. The lesson:
STAR settles ties in BOTH rounds by DETERMINISTIC rungs (five-star, then score) —
the pre-published lot order is never consulted, so LH and BetterVoting agree and
the result is fully reproducible (unlike the 3-way dead heat in BV555/xmyf7k,
which reaches the random floor). Live results: https://bettervoting.com/fp62p2/results
Lesson: bv2180_fp62p2_ice_cream_ladder.md

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

Markers on these ballots: `-` blank · `~` race abstention · `&` candidate abstention · `?` spoiled · `%` spoiled+reissued — all tabulate as 0 (reported honestly).

```text
Chocolate, Chocolate Chip, Fudge Brownie, Vanilla, Strawberry, Mango
4, 5, 4, 1, 2, -
1, 0, 0, 4, 5, 4
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR                   = Strawberry
  Choose-One (Plurality) = Chocolate Chip   (differs from STAR)
  Approval               = Chocolate   (differs from STAR)

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 2 ballots.
Chocolate,Chocolate Chip,Fudge Brownie,Vanilla,Strawberry,Mango
        4,             5,            4,      1,         2,    -
        1,             0,            0,      4,         5,    4
  ('-' = left blank / abstained; '0' = scored zero — both count as 0 stars.)

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Strawberry     -- 7 -- First place
   Chocolate      -- 5 -- Tied for second place
   Chocolate Chip -- 5 -- Tied for second place
   Vanilla        -- 5 -- Tied for second place
   Fudge Brownie  -- 4
   Mango          -- 4
 Strawberry advances, but there's a three-way tie for second.

[STAR Voting: Scoring Round: First tiebreaker]
 The candidate preferred in the most head-to-head matchups advances.
   Chocolate      -- 2 -- Tied for second place
   Chocolate Chip -- 2 -- Tied for second place
   Vanilla        -- 2 -- Tied for second place
   Equal Support  -- 0
 There's still a three-way tie for second.

[STAR Voting: Scoring Round: Second tiebreaker]
 The candidate with the most votes of score 5 advances.
   Chocolate Chip -- 1 -- Second place
   Chocolate      -- 0
   Vanilla        -- 0
 Strawberry and Chocolate Chip advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Chocolate Chip -- 1 -- Tied for first place
   Strawberry     -- 1 -- Tied for first place
   Equal Support  -- 0
 There's a two-way tie for first.

[STAR Voting: Automatic Runoff Round: First tiebreaker]
 The highest-scoring candidate wins.
   Strawberry     -- 7 -- First place
   Chocolate Chip -- 5
 Strawberry wins.

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Strawberry
```

<details>
<summary>Full audit — preference matrix, Condorcet, and score distribution</summary>

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                       |    * Chocolate     |   Chocolate Chip  |   Fudge Brownie   |      Vanilla      |   * Strawberry    |       Mango       |
-------------------------------------------------------------------------------------------------------------------------------------------------
         * Chocolate > |        ---         |    1 - 0 - 1      |    1 - 1 - 0      |    1 - 0 - 1      |    1 - 0 - 1      |    1 - 0 - 1      |
      Chocolate Chip > |     1 - 0 - 1      |       ---         |    1 - 1 - 0      |    1 - 0 - 1      |    1 - 0 - 1      |    1 - 0 - 1      |
       Fudge Brownie > |     0 - 1 - 1      |    0 - 1 - 1      |       ---         |    1 - 0 - 1      |    1 - 0 - 1      |    1 - 0 - 1      |
             Vanilla > |     1 - 0 - 1      |    1 - 0 - 1      |    1 - 0 - 1      |       ---         |    0 - 0 - 2      |    1 - 1 - 0      |
        * Strawberry > |     1 - 0 - 1      |    1 - 0 - 1      |    1 - 0 - 1      |    2 - 0 - 0      |       ---         |    2 - 0 - 0      |
               Mango > |     1 - 0 - 1      |    1 - 0 - 1      |    1 - 0 - 1      |    0 - 1 - 1      |    0 - 0 - 2      |       ---         |

[Condorcet Winner]
  No strict Condorcet winner; unbeaten candidates: Chocolate, Chocolate Chip, Strawberry (pairwise ties)

[Score Distribution] (how many ballots gave each star rating)
                     Score
Candidate       5  4  3  2  1  0  Abs  | Total   Avg
Chocolate       0  1  0  0  1  0    0  |     5   2.5
Chocolate Chip  1  0  0  0  0  1    0  |     5   2.5
Fudge Brownie   0  1  0  0  0  1    0  |     4   2.0
Vanilla         0  1  0  0  1  0    0  |     5   2.5
Strawberry      1  0  0  1  0  0    0  |     7   3.5
Mango           0  1  0  0  0  0    1  |     4   4.0
```

</details>

Everything in one file: the [`_tabulated` mirror](../tie_break_ladder_tabulated/bv2180_fp62p2_ice_cream_ladder_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/tie_break_ladder/bv2180_fp62p2_ice_cream_ladder.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Methods disagree on this election](../../../method_comparisons/divergence_review/cases/APPROVAL_OR_MINOR/bv2180_fp62p2_ice_cream_ladder.md) — its entry in the divergence review ledger
- [Ties & tie-breaking (topic hub)](../../../00_start_here/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)
- [Runoff reversal (worked set)](../../runoff_overturns_leader/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [bv830_vb3xv2_no_condorcet_tie_score](bv830_vb3xv2_no_condorcet_tie_score.md)
