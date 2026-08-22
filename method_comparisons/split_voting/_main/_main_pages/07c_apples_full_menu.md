---
search:
  exclude: true
---

# Rung 3 — eight candidates: the banana wins on 22%

*Generated from [`07c_apples_full_menu.yaml`](../07c_apples_full_menu.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [plurality](../../../../07_Concepts/README.md) · **1 seat** · **Expected winner:** Banana

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/vq78wk) · **[results ↗](https://bettervoting.com/vq78wk/results)** (election `vq78wk` · test `BV2293`).

## Scenario

The SAME nine people again. Two more apple varieties join the list — Pink Lady
and McIntosh — and they are the true favourites of the last two voters who were
still marking Gala. Both peel away.

Now every apple holds exactly ONE mark and Banana holds two. Banana wins with
2 of 9 — twenty-two percent — while seven of the nine people (78%) came in
wanting an apple. Nobody changed their mind between this rung and the last one.
Nobody voted strategically. Two candidates joined the ballot.

Look at where the two newcomers finished: Pink Lady and McIntosh got one vote
each. Neither could win. TOGETHER they changed who did — and the word matters:
add either one alone to rung 2 and the race deadlocks at Gala 2, Banana 2
rather than flipping, so it takes the pair. That is exactly what the word
SPOILER means — not a candidate who wins unfairly, but one who cannot win and
alters the result anyway. (It is also why the ladder skips seven names: that
rung is the 2-2 dead heat.)

And Banana is not merely a minority winner. It is the CONDORCET LOSER — every
single apple beats it head-to-head. Choose-One elected the one candidate this
electorate would reject in any pairing you care to run.

The general rule, visible across rungs 1-3: the rival takes the lead the moment
no single member of the split side holds more first choices than the rival
does. Under Choose-One, adding candidates cannot help the side doing the
adding. (State the method — it is not a universal law. A Borda ballot rewards
running clones, which is the mirror-image failure called teaming.)
Live results: https://bettervoting.com/vq78wk/results

## Parameters (from the YAML)

```yaml
blocs:
  Apples: [Granny Smith, Gala, Fuji, Honeycrisp, Pink Lady, Red Delicious, McIntosh]
```

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Granny Smith,Gala,Fuji,Honeycrisp,Pink Lady,Red Delicious,McIntosh,Banana
1,0,0,0,0,0,0,0   # Granny Smith
0,1,0,0,0,0,0,0   # Gala
0,0,1,0,0,0,0,0   # Fuji
0,0,0,1,0,0,0,0   # Honeycrisp
0,0,0,0,1,0,0,0   # Pink Lady - was marking Gala at rung 2
0,0,0,0,0,1,0,0   # Red Delicious
0,0,0,0,0,0,1,0   # McIntosh - was marking Gala at rung 2
0,0,0,0,0,0,0,1   # banana person
0,0,0,0,0,0,0,1   # banana person
```

## What the engine says

Full report from the [`_tabulated` mirror](../_main_tabulated/07c_apples_full_menu_tabulated.txt) (regenerated on every run; every analysis forced on):

<!-- --8<-- [start:report] -->
```text
--- Choose-One / Plurality Voting Method (single winner) ---
 Tabulating 9 ballots.

                                         Granny Smith   Gala   Fuji  Honeycrisp  Pink Lady  Red Delicious  McIntosh  Banana 
  Granny Smith                                X          -      -        -           -            -           -        -    
  Gala                                        -          X      -        -           -            -           -        -    
  Fuji                                        -          -      X        -           -            -           -        -    
  Honeycrisp                                  -          -      -        X           -            -           -        -    
  Pink Lady - was marking Gala at rung 2      -          -      -        -           X            -           -        -    
  Red Delicious                               -          -      -        -           -            X           -        -    
  McIntosh - was marking Gala at rung 2       -          -      -        -           -            -           X        -    
  banana person                               -          -      -        -           -            -           -        X    
  banana person                               -          -      -        -           -            -           -        X    

  Count the marks:  Banana 2 · Granny Smith 1 · Gala 1 · Fuji 1 · Honeycrisp 1 · Pink Lady 1 · Red Delicious 1 · McIntosh 1

Winner — Choose-One / Plurality Voting Method (single winner)
 Banana   (2 of 9 marks)
```
<!-- --8<-- [end:report] -->

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/split_voting/_main/07c_apples_full_menu.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../07_Concepts/topics/condorcet/README.md)
- [Vote splitting (worked set)](../../README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [00_plurality_vs_majority](00_plurality_vs_majority.md) · [01_political_left_split](01_political_left_split.md) · [02_icecream_chocolate_split](02_icecream_chocolate_split.md) · [03_lunch_veggie_vs_meat](03_lunch_veggie_vs_meat.md) · [04_star_wars_vote_split](04_star_wars_vote_split.md) · [05a_residual_split_bullet-voting](05a_residual_split_bullet-voting.md) · [05b_residual_split_expressive-fix](05b_residual_split_expressive-fix.md) · [06_sub_majority_not_spoiled](06_sub_majority_not_spoiled.md) · [07a_apples_two_candidates](07a_apples_two_candidates.md) · [07b_apples_six_candidates](07b_apples_six_candidates.md) · [07d_apples_full_menu_star](07d_apples_full_menu_star.md) · [07e_apples_full_menu_approval](07e_apples_full_menu_approval.md) · [07f_apples_full_menu_irv](07f_apples_full_menu_irv.md) · [07g_apples_full_menu_ranked_robin](07g_apples_full_menu_ranked_robin.md) · [08a_smallest_spoiler_plurality](08a_smallest_spoiler_plurality.md) · [08b_smallest_spoiler_star](08b_smallest_spoiler_star.md) · [08c_smallest_spoiler_ranked_robin](08c_smallest_spoiler_ranked_robin.md) · [09a_clones_are_voters_not_labels](09a_clones_are_voters_not_labels.md) · [09b_same_ballots_grouped_by_label](09b_same_ballots_grouped_by_label.md)
