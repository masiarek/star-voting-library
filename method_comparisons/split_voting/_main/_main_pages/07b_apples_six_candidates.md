---
search:
  exclude: true
---

# Rung 2 — six candidates: the vote splits, and it costs nothing

*Generated from [`07b_apples_six_candidates.yaml`](../07b_apples_six_candidates.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [plurality](../../../../07_Concepts/README.md) · **1 seat** · **Expected winner:** Gala

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/vq78wk) · **[results ↗](https://bettervoting.com/vq78wk/results)** (election `vq78wk` · test `BV2293`).

## Scenario

The SAME nine people, the same opinions, four more apple varieties on the list.
Each apple person now marks whichever of the available apples they like best.

Gala 3, Banana 2, and one each for Granny Smith, Fuji, Honeycrisp and Red
Delicious. Gala wins with 3 of 9 — 33%, well under half.

Read the warning signs and this looks alarming: the winner has a third of the
vote, and the candidates who lost hold twice as much between them. Read the
result and nothing went wrong at all. The apple vote IS splitting — five ways —
and the apple side still wins, because Gala's pile is still bigger than
Banana's.

This rung is the one most explanations skip, and it is the reason "the winner
got under 50%" is a screening flag rather than a finding. Splitting is not the
same as being spoiled. What matters is not whether a side divides, but whether
it divides FAR ENOUGH that its largest piece drops below the rival's.
Live results: https://bettervoting.com/vq78wk/results

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Granny Smith,Gala,Fuji,Honeycrisp,Red Delicious,Banana
1,0,0,0,0,0   # Granny Smith is on the list now, so that is the mark
0,1,0,0,0,0   # Gala really is this voter's favourite
0,0,1,0,0,0   # Fuji is on the list now
0,0,0,1,0,0   # Honeycrisp is on the list now
0,1,0,0,0,0   # would prefer a Pink Lady - not on the list, so Gala
0,0,0,0,1,0   # Red Delicious is on the list now
0,1,0,0,0,0   # would prefer a McIntosh - not on the list, so Gala
0,0,0,0,0,1   # banana person
0,0,0,0,0,1   # banana person
```

## What the engine says

Full report from the [`_tabulated` mirror](../_main_tabulated/07b_apples_six_candidates_tabulated.txt) (regenerated on every run; every analysis forced on):

<!-- --8<-- [start:report] -->
```text
--- Choose-One / Plurality Voting Method (single winner) ---
 Tabulating 9 ballots.

                                                       Granny Smith   Gala   Fuji  Honeycrisp  Red Delicious  Banana 
  Granny Smith is on the list now, so that is the mark      X          -      -        -             -          -    
  Gala really is this voter's favourite                     -          X      -        -             -          -    
  Fuji is on the list now                                   -          -      X        -             -          -    
  Honeycrisp is on the list now                             -          -      -        X             -          -    
  would prefer a Pink Lady - not on the list, so Gala       -          X      -        -             -          -    
  Red Delicious is on the list now                          -          -      -        -             X          -    
  would prefer a McIntosh - not on the list, so Gala        -          X      -        -             -          -    
  banana person                                             -          -      -        -             -          X    
  banana person                                             -          -      -        -             -          X    

  Count the marks:  Gala 3 · Banana 2 · Granny Smith 1 · Fuji 1 · Honeycrisp 1 · Red Delicious 1

Winner — Choose-One / Plurality Voting Method (single winner)
 Gala   (3 of 9 marks)
```
<!-- --8<-- [end:report] -->

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/split_voting/_main/07b_apples_six_candidates.yaml
```

## See also

- [Vote splitting (worked set)](../../README.md)
- [Ballot & terminology basics](../../../../07_Concepts/topics/ballot_and_terminology_basics.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [00_plurality_vs_majority](00_plurality_vs_majority.md) · [01_political_left_split](01_political_left_split.md) · [02_icecream_chocolate_split](02_icecream_chocolate_split.md) · [03_lunch_veggie_vs_meat](03_lunch_veggie_vs_meat.md) · [04_star_wars_vote_split](04_star_wars_vote_split.md) · [05a_residual_split_bullet-voting](05a_residual_split_bullet-voting.md) · [05b_residual_split_expressive-fix](05b_residual_split_expressive-fix.md) · [06_sub_majority_not_spoiled](06_sub_majority_not_spoiled.md) · [07a_apples_two_candidates](07a_apples_two_candidates.md) · [07c_apples_full_menu](07c_apples_full_menu.md) · [07d_apples_full_menu_star](07d_apples_full_menu_star.md) · [07e_apples_full_menu_approval](07e_apples_full_menu_approval.md) · [07f_apples_full_menu_irv](07f_apples_full_menu_irv.md) · [07g_apples_full_menu_ranked_robin](07g_apples_full_menu_ranked_robin.md) · [08a_smallest_spoiler_plurality](08a_smallest_spoiler_plurality.md) · [08b_smallest_spoiler_star](08b_smallest_spoiler_star.md) · [08c_smallest_spoiler_ranked_robin](08c_smallest_spoiler_ranked_robin.md) · [09a_clones_are_voters_not_labels](09a_clones_are_voters_not_labels.md) · [09b_same_ballots_grouped_by_label](09b_same_ballots_grouped_by_label.md)
