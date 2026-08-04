---
search:
  exclude: true
---

# A 41% winner that nothing spoiled — sub-majority is not the same as split

*Generated from [`06_sub_majority_not_spoiled.yaml`](../06_sub_majority_not_spoiled.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../../01_STAR/01_Learn) · **1 seat** · **Expected winner:** Aspen

## Scenario

The counter-example to the "winner under 50% = vote split election" test.

44 residents pick the tree for the new Main Street: Aspen, Birch, Cedar.
Under Choose-One the first choices are Aspen 18 (41%), Birch 14, Cedar 12.
The winner is well under half, and the two losers combined (26) are a
majority — so by the usual screening rule this race counts as a "vote split
election."

But read the whole ballot and nothing was split at all. Aspen leads the
scoring round (180), wins the automatic runoff over Birch 30-14, beats BOTH
rivals head-to-head (the Condorcet winner), and also wins under RCV-IRV once
Cedar's ballots transfer. Every method agrees: Aspen is the majority's
genuine choice, who simply led a three-way field without clearing 50% of
FIRST choices.

The lesson: a sub-majority plurality winner means the race was EXPOSED to
vote splitting, not that vote splitting changed the outcome. Telling the two
apart needs preference data — exactly what a one-mark ballot never collects.
Compare 01_political_left_split.yaml, where the same 41%-ish arithmetic DOES
hide a flipped result.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:Aspen,Birch,Cedar
18:5,4,0   # Aspen first, Birch a close second
14:3,5,1   # Birch first, Aspen acceptable
12:4,0,5   # Cedar first, Aspen the clear second
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 44 ballots.
Count × Aspen,Birch,Cedar
   18 ×     5,    4,    0
   14 ×     3,    5,    1
   12 ×     4,    0,    5

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Aspen         -- 180 -- First place
   Birch         -- 142 -- Second place
   Cedar         --  74
 Aspen and Birch advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Aspen         -- 30 -- First place
   Birch         -- 14
   Equal Support --  0
 Aspen wins.
   Runoff math:
     44  ballots cast
   −  0  Equal Support (no preference between the two finalists)
     ──
     44  voters with a preference  (majority = 23)
           Aspen 30 (68%)  ·  Birch 14 (32%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Aspen
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |   * Aspen    |  * Birch    |    Cedar    |
-------------------------------------------------------------
       * Aspen > |     ---      |30 -  0 - 14 |32 -  0 - 12 |
       * Birch > | 14 -  0 - 30 |    ---      |32 -  0 - 12 |
         Cedar > | 12 -  0 - 32 |12 -  0 - 32 |    ---      |

[Condorcet Winner]
  Condorcet Winner: Aspen — matches the STAR winner

[Condorcet Loser]
  Condorcet Loser: Cedar — loses every head-to-head matchup

[Score Distribution] (how many ballots gave each star rating)
                   Score
Candidate   5   4   3   2   1   0  | Total   Avg
Aspen      18  12  14   0   0   0  |   180   4.1
Birch      14  18   0   0   0  12  |   142   3.2
Cedar      12   0   0   0  14  18  |    74   1.7
```

Everything in one file: the [`_tabulated` mirror](../_main_tabulated/06_sub_majority_not_spoiled_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/split_voting/_main/06_sub_majority_not_spoiled.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../07_Concepts/topics/condorcet/README.md)
- [Vote splitting (worked set)](../../README.md)
- [Runoff reversal (worked set)](../../../../01_STAR/02_Examples/runoff_overturns_leader/README.md)
- [Ballot & terminology basics](../../../../07_Concepts/topics/ballot_and_terminology_basics.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [00_plurality_vs_majority](00_plurality_vs_majority.md) · [01_political_left_split](01_political_left_split.md) · [02_icecream_chocolate_split](02_icecream_chocolate_split.md) · [03_lunch_veggie_vs_meat](03_lunch_veggie_vs_meat.md) · [04_star_wars_vote_split](04_star_wars_vote_split.md) · [05a_residual_split_bullet-voting](05a_residual_split_bullet-voting.md) · [05b_residual_split_expressive-fix](05b_residual_split_expressive-fix.md)
