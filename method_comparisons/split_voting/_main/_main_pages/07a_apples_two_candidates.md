---
search:
  exclude: true
---

# Rung 1 — two candidates: nothing can split

*Generated from [`07a_apples_two_candidates.yaml`](../07a_apples_two_candidates.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [plurality](../../../../07_Concepts/README.md) · **1 seat** · **Expected winner:** Gala

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/vq78wk) · **[results ↗](https://bettervoting.com/vq78wk/results)** (election `vq78wk` · test `BV2293`).

## Scenario

Nine people pick ONE fruit for the office basket. Seven of them want an apple;
two want a banana. With only two names on the paper there is exactly one way to
say "apple", so the apple people all say it.

Gala 7, Banana 2. The apple side holds 78% and wins with 78%.

This is the baseline every later rung is measured against. With two candidates,
Choose-One, STAR, Approval, RCV-IRV and Ranked Robin ALL elect Gala, because
with two candidates every reasonable method is the same method: majority rule.
Vote splitting has not been prevented here — it is not yet possible. It becomes
possible the moment a third name appears.
Live results: https://bettervoting.com/vq78wk/results

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Gala,Banana
1,0   # apple person - would really rather have a Granny Smith
1,0   # apple person - Gala is genuinely their favourite
1,0   # apple person - would really rather have a Fuji
1,0   # apple person - would really rather have a Honeycrisp
1,0   # apple person - would really rather have a Pink Lady
1,0   # apple person - would really rather have a Red Delicious
1,0   # apple person - would really rather have a McIntosh
0,1   # banana person
0,1   # banana person
```

## What the engine says

Full report from the [`_tabulated` mirror](../_main_tabulated/07a_apples_two_candidates_tabulated.txt) (regenerated on every run; every analysis forced on):

<!-- --8<-- [start:report] -->
```text
--- Choose-One / Plurality Voting Method (single winner) ---
 Tabulating 9 ballots.

                                                           Gala  Banana 
  apple person - would really rather have a Granny Smith    X      -    
  apple person - Gala is genuinely their favourite          X      -    
  apple person - would really rather have a Fuji            X      -    
  apple person - would really rather have a Honeycrisp      X      -    
  apple person - would really rather have a Pink Lady       X      -    
  apple person - would really rather have a Red Delicious   X      -    
  apple person - would really rather have a McIntosh        X      -    
  banana person                                             -      X    
  banana person                                             -      X    

  Count the marks:  Gala 7 · Banana 2

Winner — Choose-One / Plurality Voting Method (single winner)
 Gala   (7 of 9 marks)
```
<!-- --8<-- [end:report] -->

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/split_voting/_main/07a_apples_two_candidates.yaml
```

## See also

- [Vote splitting (worked set)](../../README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [00_plurality_vs_majority](00_plurality_vs_majority.md) · [01_political_left_split](01_political_left_split.md) · [02_icecream_chocolate_split](02_icecream_chocolate_split.md) · [03_lunch_veggie_vs_meat](03_lunch_veggie_vs_meat.md) · [04_star_wars_vote_split](04_star_wars_vote_split.md) · [05a_residual_split_bullet-voting](05a_residual_split_bullet-voting.md) · [05b_residual_split_expressive-fix](05b_residual_split_expressive-fix.md) · [06_sub_majority_not_spoiled](06_sub_majority_not_spoiled.md) · [07b_apples_six_candidates](07b_apples_six_candidates.md) · [07c_apples_full_menu](07c_apples_full_menu.md) · [07d_apples_full_menu_star](07d_apples_full_menu_star.md) · [07e_apples_full_menu_approval](07e_apples_full_menu_approval.md) · [07f_apples_full_menu_irv](07f_apples_full_menu_irv.md) · [07g_apples_full_menu_ranked_robin](07g_apples_full_menu_ranked_robin.md) · [08a_smallest_spoiler_plurality](08a_smallest_spoiler_plurality.md) · [08b_smallest_spoiler_star](08b_smallest_spoiler_star.md) · [08c_smallest_spoiler_ranked_robin](08c_smallest_spoiler_ranked_robin.md) · [09a_clones_are_voters_not_labels](09a_clones_are_voters_not_labels.md) · [09b_same_ballots_grouped_by_label](09b_same_ballots_grouped_by_label.md)
