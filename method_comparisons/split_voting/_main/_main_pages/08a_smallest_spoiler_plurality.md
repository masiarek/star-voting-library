---
search:
  exclude: true
---

# The smallest spoiler — seven friends, three flavours, and a minority winner

*Generated from [`08a_smallest_spoiler_plurality.yaml`](../08a_smallest_spoiler_plurality.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [plurality](../../../../07_Concepts/README.md) · **1 seat** · **Expected winner:** Vanilla

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/9cff2d) · **[results ↗](https://bettervoting.com/9cff2d/results)** (election `9cff2d` · test `BV2296`).

## Scenario

The smallest election in which two similar candidates can cost their own side
the win. Seven friends pick ONE tub of ice cream. Four of them want chocolate,
three want vanilla — and the chocolate four are divided over WHICH chocolate.

Choose-One: Vanilla 3, Milk Chocolate 2, Dark Chocolate 2. Vanilla wins with
3 of 7 (43%) — and all four chocolate lovers ranked Vanilla DEAD LAST.

Why seven is the floor for this shape: with two similar candidates, the rival
needs more marks than either of them individually and fewer than both together.
The cheapest arithmetic that does it is 2 + 2 versus 3. Fewer voters than this
and either the chocolate side stops being a majority or one chocolate out-polls
the vanilla.

(Allow THREE similar candidates and the floor drops to five voters: 1 + 1 + 1
against 2, a 40% winner. Fewer voters, more candidates — see the fruit-basket
ladder, where seven apples and a banana bring it down to 22% on nine ballots.)
Live results: https://bettervoting.com/9cff2d/results

## Parameters (from the YAML)

```yaml
blocs:
  Chocolate: [Milk Chocolate, Dark Chocolate]
```

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Milk Chocolate,Dark Chocolate,Vanilla
1,0,0   # milk chocolate, and dark would be fine too
1,0,0   # milk chocolate, and dark would be fine too
0,1,0   # dark chocolate, and milk would be fine too
0,1,0   # dark chocolate, and milk would be fine too
0,0,1   # vanilla
0,0,1   # vanilla
0,0,1   # vanilla
```

## What the engine says

Full report from the [`_tabulated` mirror](../_main_tabulated/08a_smallest_spoiler_plurality_tabulated.txt) (regenerated on every run; every analysis forced on):

<!-- --8<-- [start:report] -->
```text
--- Choose-One / Plurality Voting Method (single winner) ---
 Tabulating 7 ballots.

                                             Milk Chocolate  Dark Chocolate  Vanilla 
  milk chocolate, and dark would be fine too       X               -            -    
  milk chocolate, and dark would be fine too       X               -            -    
  dark chocolate, and milk would be fine too       -               X            -    
  dark chocolate, and milk would be fine too       -               X            -    
  vanilla                                          -               -            X    
  vanilla                                          -               -            X    
  vanilla                                          -               -            X    

  Count the marks:  Vanilla 3 · Milk Chocolate 2 · Dark Chocolate 2

Winner — Choose-One / Plurality Voting Method (single winner)
 Vanilla   (3 of 7 marks)
```
<!-- --8<-- [end:report] -->

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/split_voting/_main/08a_smallest_spoiler_plurality.yaml
```

## See also

- [Vote splitting (worked set)](../../README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [00_plurality_vs_majority](00_plurality_vs_majority.md) · [01_political_left_split](01_political_left_split.md) · [02_icecream_chocolate_split](02_icecream_chocolate_split.md) · [03_lunch_veggie_vs_meat](03_lunch_veggie_vs_meat.md) · [04_star_wars_vote_split](04_star_wars_vote_split.md) · [05a_residual_split_bullet-voting](05a_residual_split_bullet-voting.md) · [05b_residual_split_expressive-fix](05b_residual_split_expressive-fix.md) · [06_sub_majority_not_spoiled](06_sub_majority_not_spoiled.md) · [07a_apples_two_candidates](07a_apples_two_candidates.md) · [07b_apples_six_candidates](07b_apples_six_candidates.md) · [07c_apples_full_menu](07c_apples_full_menu.md) · [07d_apples_full_menu_star](07d_apples_full_menu_star.md) · [07e_apples_full_menu_approval](07e_apples_full_menu_approval.md) · [07f_apples_full_menu_irv](07f_apples_full_menu_irv.md) · [07g_apples_full_menu_ranked_robin](07g_apples_full_menu_ranked_robin.md) · [08b_smallest_spoiler_star](08b_smallest_spoiler_star.md) · [08c_smallest_spoiler_ranked_robin](08c_smallest_spoiler_ranked_robin.md) · [09a_clones_are_voters_not_labels](09a_clones_are_voters_not_labels.md) · [09b_same_ballots_grouped_by_label](09b_same_ballots_grouped_by_label.md)
