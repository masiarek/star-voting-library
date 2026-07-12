# The BV recipe (the "crazy" scenario)

*Generated from [`Ballot Data - The BV recipe (the _crazy_ scenario)-jfk7pd_published_order.yaml`](../Ballot Data - The BV recipe (the _crazy_ scenario)-jfk7pd_published_order.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat**

## Scenario

BV id - jfk7pd

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Ada, Ben
  4,   0
  0,   4
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 2 ballots.
Ada,Ben
  4,  0
  0,  4

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Ada           -- 4 -- First place
   Ben           -- 4 -- Second place
 Ada and Ben advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Ada           -- 1 -- Tied for first place
   Ben           -- 1 -- Tied for first place
   Equal Support -- 0
 There's a two-way tie for first.

[STAR Voting: Automatic Runoff Round: First tiebreaker]
 The highest-scoring candidate wins.
   Ada           -- 4 -- Tied for first place
   Ben           -- 4 -- Tied for first place
 There's still a two-way tie for first.

[STAR Voting: Automatic Runoff Round: Second tiebreaker]
 The candidate with the most votes of score 5 wins.
   Ada           -- 0 -- Tied for first place
   Ben           -- 0 -- Tied for first place
 There's still a two-way tie for first.

*(Ties are resolved by choosing the tied candidate with the highest-priority official lot number.)*
    Lot-number priority order: ['Ada', 'Ben']

[Tiebreaker: Lot Number Priority]
  Tie among: ['Ada', 'Ben']
  Resolved: ['Ada'] (selected by lot-number priority).

[Lot-decided tie — rare]
  ⚠ The ballots did not break this tie: the deterministic rungs
    (pairwise / score, then five-star) all came back equal, so the
    pre-published LOT order chose among the tied candidates — the
    result here was set by lot, not by the votes. Usually the
    "dead rung": no tied candidate held a score-5 vote (five-star
    counts fives, not fours). Verify the tied candidates' 5-counts.

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Ada
```

<details>
<summary>▸ Full audit — preference matrix, Condorcet, and score distribution</summary>

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |   * Ada    |  * Ben    |
-----------------------------------------
       * Ada > |    ---     |1 - 0 - 1  |
       * Ben > | 1 - 0 - 1  |   ---     |

[Condorcet Winner]
  No strict Condorcet winner; unbeaten candidates: Ada, Ben (pairwise ties)

[Score Distribution] (number of ballots giving each score)
     5  4  3  2  1  0  | Total   Avg
Ada  0  1  0  0  0  1  |     4   2.0
Ben  0  1  0  0  0  1  |     4   2.0
```

</details>

Everything in one file: the [`_tabulated` mirror](../_demo_dropbox_tabulated/Ballot Data - The BV recipe (the _crazy_ scenario)-jfk7pd_published_order_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 06_Other/_demo_dropbox/Ballot Data - The BV recipe (the _crazy_ scenario)-jfk7pd_published_order.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [Ballot Data - The BV recipe (the _crazy_ scenario)-jfk7pd_bv_order](Ballot Data - The BV recipe (the _crazy_ scenario)-jfk7pd_bv_order.md)
