---
search:
  exclude: true
---

# The smallest spoiler, fixed — the same seven friends, scoring

*Generated from [`08b_smallest_spoiler_star.yaml`](../08b_smallest_spoiler_star.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../../01_STAR/01_Learn/README.md) · **1 seat** · **Expected winner:** Milk Chocolate

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/vjp3fj) · **[results ↗](https://bettervoting.com/vjp3fj/results)** (election `vjp3fj` · test `BV2294`).

## Scenario

The identical seven friends from 08a, scoring each flavour 0-5 instead of
marking one. Nothing about their opinions changed; the ballot simply records
what the single mark could not — that a chocolate lover likes BOTH chocolates
and does not want vanilla.

Scoring Round: Milk Chocolate 20, Dark Chocolate 18, Vanilla 15. Automatic
Runoff: Milk Chocolate 4, Vanilla 3 — the four chocolate lovers, no longer
divided against themselves.

This is the whole argument in seven ballots. Choose-One did not count the
chocolate votes wrongly. It never asked the question whose answer would have
changed the result.
Live results: https://bettervoting.com/vjp3fj/results

## Parameters (from the YAML)

```yaml
blocs:
  Chocolate: [Milk Chocolate, Dark Chocolate]
```

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Milk Chocolate,Dark Chocolate,Vanilla
5,4,0   # milk first, dark is a close second, vanilla no thanks
5,3,0   # milk first, dark is fine, vanilla no thanks
4,5,0   # dark first, milk is a close second
3,5,0   # dark first, milk is fine
0,0,5   # vanilla only
1,0,5   # vanilla, and milk chocolate at a pinch
2,1,5   # vanilla, but not fussy
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
[Divergence from STAR]
  STAR                   = Milk Chocolate
  Choose-One (Plurality) = Vanilla   (differs from STAR)

[Vote-splitting check]
  Choose-One first choices: Vanilla 3, Milk Chocolate 2, Dark Chocolate 2
  Plurality winner: Vanilla (3, 42.9%)
  Bloc 'Chocolate' = Milk Chocolate, Dark Chocolate: combined 4 (57.1%); winner Vanilla is OUTSIDE it.
  => VOTE SPLITTING: the 'Chocolate' bloc is an outright majority (4 vs
     Vanilla's 3) but split across 2 candidates, so Vanilla won Choose-One.
     STAR elected Milk Chocolate.

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 7 ballots.
Milk Chocolate,Dark Chocolate,Vanilla
             5,             4,      0
             5,             3,      0
             4,             5,      0
             3,             5,      0
             0,             0,      5
             1,             0,      5
             2,             1,      5

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Milk Chocolate -- 20 -- First place
   Dark Chocolate -- 18 -- Second place
   Vanilla        -- 15
 Milk Chocolate and Dark Chocolate advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Milk Chocolate -- 4 -- First place
   Dark Chocolate -- 2
   Equal Support  -- 1
 Milk Chocolate wins.
   Runoff math:
     7  ballots cast
   − 1  Equal Support (no preference between the two finalists)
     ─
     6  voters with a preference  (majority = 4)
           Milk Chocolate 4 (67%)  ·  Dark Chocolate 2 (33%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Milk Chocolate
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                       |  * Milk Chocolate  | * Dark Chocolate  |      Vanilla      |
-------------------------------------------------------------------------------------
    * Milk Chocolate > |        ---         |    4 - 1 - 2      |    4 - 0 - 3      |
    * Dark Chocolate > |     2 - 1 - 4      |       ---         |    4 - 0 - 3      |
             Vanilla > |     3 - 0 - 4      |    3 - 0 - 4      |       ---         |

[Condorcet Winner]
  Condorcet Winner: Milk Chocolate — matches the STAR winner

[Condorcet Loser]
  Condorcet Loser: Vanilla — loses every head-to-head matchup — elected by Choose-One (Plurality)!

[Score Distribution] (how many ballots gave each star rating)
                     Score
Candidate       5  4  3  2  1  0  | Total   Avg
Milk Chocolate  2  1  1  1  1  1  |    20   2.9
Dark Chocolate  2  1  1  0  1  2  |    18   2.6
Vanilla         3  0  0  0  0  4  |    15   2.1
```

Everything in one file: the [`_tabulated` mirror](../_main_tabulated/08b_smallest_spoiler_star_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/split_voting/_main/08b_smallest_spoiler_star.yaml
```

## See also

- [Vote splitting (worked set)](../../README.md)
- [Runoff reversal (worked set)](../../../../01_STAR/02_Examples/runoff_overturns_leader/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [00_plurality_vs_majority](00_plurality_vs_majority.md) · [01_political_left_split](01_political_left_split.md) · [02_icecream_chocolate_split](02_icecream_chocolate_split.md) · [03_lunch_veggie_vs_meat](03_lunch_veggie_vs_meat.md) · [04_star_wars_vote_split](04_star_wars_vote_split.md) · [05a_residual_split_bullet-voting](05a_residual_split_bullet-voting.md) · [05b_residual_split_expressive-fix](05b_residual_split_expressive-fix.md) · [06_sub_majority_not_spoiled](06_sub_majority_not_spoiled.md) · [07a_apples_two_candidates](07a_apples_two_candidates.md) · [07b_apples_six_candidates](07b_apples_six_candidates.md) · [07c_apples_full_menu](07c_apples_full_menu.md) · [07d_apples_full_menu_star](07d_apples_full_menu_star.md) · [07e_apples_full_menu_approval](07e_apples_full_menu_approval.md) · [07f_apples_full_menu_irv](07f_apples_full_menu_irv.md) · [08a_smallest_spoiler_plurality](08a_smallest_spoiler_plurality.md) · [09a_clones_are_voters_not_labels](09a_clones_are_voters_not_labels.md) · [09b_same_ballots_grouped_by_label](09b_same_ballots_grouped_by_label.md)
