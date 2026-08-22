---
search:
  exclude: true
---

# The smallest spoiler, head-to-head — the majority Choose-One threw away

*Generated from [`08c_smallest_spoiler_ranked_robin.yaml`](../08c_smallest_spoiler_ranked_robin.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../../05_Ranked_Robin/01_Learn/README.md) · **1 seat** · **Expected winner:** Milk Chocolate

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/9cff2d) · **[results ↗](https://bettervoting.com/9cff2d/results)** (election `9cff2d` · test `BV2296`).

## Scenario

The same seven friends as 08a and 08b, counted pair by pair. This is the
cleanest statement of what Choose-One discarded.

Milk Chocolate beats Dark Chocolate 5-2 and beats Vanilla 4-3 — the Condorcet
winner. Dark Chocolate also beats Vanilla 4-3. So a majority of these seven
friends preferred EITHER chocolate to the vanilla that won the Choose-One
count. Vanilla did not merely win with a minority; it won against a candidate
a majority preferred to it, and there were two such candidates.

No rounds, no eliminations, no runoff to explain — just every pair counted.
Cross-checked against pref_voting's independent Copeland implementation.
Live results: https://bettervoting.com/9cff2d/results

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
1:Milk Chocolate>Dark Chocolate>Vanilla
1:Milk Chocolate>Dark Chocolate>Vanilla
1:Dark Chocolate>Milk Chocolate>Vanilla
1:Dark Chocolate>Milk Chocolate>Vanilla
1:Vanilla>Milk Chocolate>Dark Chocolate
1:Vanilla>Milk Chocolate>Dark Chocolate
1:Vanilla>Milk Chocolate>Dark Chocolate
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
--- Ranked Robin (RCV-RR / Copeland) Method (single winner) ---
 Tabulating 7 ballots (ranked ballots).

Ballots:
     2 × Milk Chocolate > Dark Chocolate > Vanilla
     2 × Dark Chocolate > Milk Chocolate > Vanilla
     3 × Vanilla > Milk Chocolate > Dark Chocolate

Round-Robin — every pair, head-to-head (For – Against):
   Milk Chocolate  beats Dark Chocolate   5 – 2
   Milk Chocolate  beats Vanilla          4 – 3
   Dark Chocolate  beats Vanilla          4 – 3

--- Pairwise (Round-Robin) Matrix ---
Head-to-head / pairwise comparison — the Ranked Robin tally
Legend: For - Equal Support - Against   (row vs column)
                   |  Milk Chocolate  | Dark Chocolate  |    Vanilla      |
---------------------------------------------------------------------------
  Milk Chocolate > |       ---        |   5 - 0 - 2     |   4 - 0 - 3     |
  Dark Chocolate > |    2 - 0 - 5     |      ---        |   4 - 0 - 3     |
         Vanilla > |    3 - 0 - 4     |   3 - 0 - 4     |      ---        |

Win–loss record — Copeland score = wins + ½·ties (highest score wins; ties broken by the Ranked Robin degrees, then lot order):
    #  Candidate       W–L–T  Copeland  Margin  Beats
    1  Milk Chocolate  2–0–0         2      +4  Dark Chocolate, Vanilla
    2  Dark Chocolate  1–1–0         1      -2  Vanilla
    3  Vanilla         0–2–0         0      -2  —

Winner — Ranked Robin (RCV-RR): Milk Chocolate
   beats every opponent head-to-head — the Condorcet winner.
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Smith Set (the generalized Condorcet winner) ---
The smallest group whose every member beats every candidate outside it —
the honest answer to "who is even in contention?".
   Smith set (1 of 3): Milk Chocolate
   Outside (2):        Dark Chocolate, Vanilla
   One member ⇒ Milk Chocolate is the Condorcet winner, beating every rival head-to-head.
   Ranked Robin (RCV-RR) winner Milk Chocolate is INSIDE the Smith set. ✓
      Guaranteed: Ranked Robin (Copeland) is Smith-efficient — every member of
      the set outscores every outsider, so the top of the win–loss table is
      always inside the set, however the tie among them is then broken.
   More: 07_Concepts/topics/smith_set.md
```

Everything in one file: the [`_tabulated` mirror](../_main_tabulated/08c_smallest_spoiler_ranked_robin_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/split_voting/_main/08c_smallest_spoiler_ranked_robin.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../07_Concepts/topics/condorcet/README.md)
- [Vote splitting (worked set)](../../README.md)
- [Runoff reversal (worked set)](../../../../01_STAR/02_Examples/runoff_overturns_leader/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [00_plurality_vs_majority](00_plurality_vs_majority.md) · [01_political_left_split](01_political_left_split.md) · [02_icecream_chocolate_split](02_icecream_chocolate_split.md) · [03_lunch_veggie_vs_meat](03_lunch_veggie_vs_meat.md) · [04_star_wars_vote_split](04_star_wars_vote_split.md) · [05a_residual_split_bullet-voting](05a_residual_split_bullet-voting.md) · [05b_residual_split_expressive-fix](05b_residual_split_expressive-fix.md) · [06_sub_majority_not_spoiled](06_sub_majority_not_spoiled.md) · [07a_apples_two_candidates](07a_apples_two_candidates.md) · [07b_apples_six_candidates](07b_apples_six_candidates.md) · [07c_apples_full_menu](07c_apples_full_menu.md) · [07d_apples_full_menu_star](07d_apples_full_menu_star.md) · [07e_apples_full_menu_approval](07e_apples_full_menu_approval.md) · [07f_apples_full_menu_irv](07f_apples_full_menu_irv.md) · [07g_apples_full_menu_ranked_robin](07g_apples_full_menu_ranked_robin.md) · [08a_smallest_spoiler_plurality](08a_smallest_spoiler_plurality.md) · [08b_smallest_spoiler_star](08b_smallest_spoiler_star.md) · [09a_clones_are_voters_not_labels](09a_clones_are_voters_not_labels.md) · [09b_same_ballots_grouped_by_label](09b_same_ballots_grouped_by_label.md)
