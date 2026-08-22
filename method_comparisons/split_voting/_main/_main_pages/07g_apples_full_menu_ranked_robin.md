---
search:
  exclude: true
---

# Rung 4 — the same nine voters, head-to-head: Ranked Robin confirms Gala

*Generated from [`07g_apples_full_menu_ranked_robin.yaml`](../07g_apples_full_menu_ranked_robin.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../../05_Ranked_Robin/01_Learn/README.md) · **1 seat** · **Expected winner:** Gala

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/vq78wk) · **[results ↗](https://bettervoting.com/vq78wk/results)** (election `vq78wk` · test `BV2293`).

## Scenario

The same nine ranked ballots as rung 4's RCV-IRV race, counted head-to-head
instead of by elimination — and the answer key for the whole ladder.

Gala wins all seven of its matchups: it is the Condorcet winner, the candidate
this electorate prefers to every alternative. At the other end, BANANA LOSES
ALL SEVEN — it is the Condorcet loser. Choose-One elected the one candidate
that loses every pairing you can run.

This race also settles what rung 4's IRV file deliberately leaves open. There,
seven candidates start tied on one first choice each, so the elimination order
is decided by tie-breaking; here nothing is. No eliminations, no rounds, no lot
— just every pair counted.

Cross-checked three ways per house rule: this engine, BetterVoting's own
RankedRobin tabulator, and pref_voting's independent Copeland implementation
(unique leader, AGREE).
Live results: https://bettervoting.com/vq78wk/results

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
1:Granny Smith>Gala>Fuji>McIntosh>Honeycrisp>Pink Lady>Red Delicious>Banana
1:Gala>Granny Smith>Fuji>Honeycrisp>Pink Lady>McIntosh>Red Delicious>Banana
1:Fuji>Gala>Granny Smith>Honeycrisp>Pink Lady>McIntosh>Red Delicious>Banana
1:Honeycrisp>Gala>Granny Smith>McIntosh>Fuji>Pink Lady>Red Delicious>Banana
1:Pink Lady>Gala>Granny Smith>Fuji>Honeycrisp>Red Delicious>McIntosh>Banana
1:Red Delicious>Gala>Granny Smith>Fuji>Banana>Honeycrisp>Pink Lady>McIntosh
1:McIntosh>Gala>Granny Smith>Honeycrisp>Fuji>Pink Lady>Red Delicious>Banana
1:Banana>Granny Smith>Red Delicious>Gala>Fuji>Honeycrisp>Pink Lady>McIntosh
1:Banana>Granny Smith>Gala>Fuji>Honeycrisp>Pink Lady>Red Delicious>McIntosh
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
--- Ranked Robin (RCV-RR / Copeland) Method (single winner) ---
 Tabulating 9 ballots (ranked ballots).

Ballots:
     1 × Granny Smith > Gala > Fuji > McIntosh > Honeycrisp > Pink Lady > Red Delicious > Banana
     1 × Gala > Granny Smith > Fuji > Honeycrisp > Pink Lady > McIntosh > Red Delicious > Banana
     1 × Fuji > Gala > Granny Smith > Honeycrisp > Pink Lady > McIntosh > Red Delicious > Banana
     1 × Honeycrisp > Gala > Granny Smith > McIntosh > Fuji > Pink Lady > Red Delicious > Banana
     1 × Pink Lady > Gala > Granny Smith > Fuji > Honeycrisp > Red Delicious > McIntosh > Banana
     1 × Red Delicious > Gala > Granny Smith > Fuji > Banana > Honeycrisp > Pink Lady > McIntosh
     1 × McIntosh > Gala > Granny Smith > Honeycrisp > Fuji > Pink Lady > Red Delicious > Banana
     1 × Banana > Granny Smith > Red Delicious > Gala > Fuji > Honeycrisp > Pink Lady > McIntosh
     1 × Banana > Granny Smith > Gala > Fuji > Honeycrisp > Pink Lady > Red Delicious > McIntosh

Round-Robin — every pair, head-to-head (For – Against):
   Gala           beats Granny Smith    6 – 3
   Granny Smith   beats Fuji            8 – 1
   Granny Smith   beats McIntosh        8 – 1
   Granny Smith   beats Honeycrisp      8 – 1
   Granny Smith   beats Pink Lady       8 – 1
   Granny Smith   beats Red Delicious   8 – 1
   Granny Smith   beats Banana          7 – 2
   Gala           beats Fuji            8 – 1
   Gala           beats McIntosh        8 – 1
   Gala           beats Honeycrisp      8 – 1
   Gala           beats Pink Lady       8 – 1
   Gala           beats Red Delicious   7 – 2
   Gala           beats Banana          7 – 2
   Fuji           beats McIntosh        7 – 2
   Fuji           beats Honeycrisp      7 – 2
   Fuji           beats Pink Lady       8 – 1
   Fuji           beats Red Delicious   7 – 2
   Fuji           beats Banana          7 – 2
   Honeycrisp     beats McIntosh        7 – 2
   Pink Lady      beats McIntosh        6 – 3
   McIntosh       beats Red Delicious   5 – 4
   McIntosh       beats Banana          6 – 3
   Honeycrisp     beats Pink Lady       8 – 1
   Honeycrisp     beats Red Delicious   7 – 2
   Honeycrisp     beats Banana          6 – 3
   Pink Lady      beats Red Delicious   7 – 2
   Pink Lady      beats Banana          6 – 3
   Red Delicious  beats Banana          7 – 2

--- Pairwise (Round-Robin) Matrix ---
Head-to-head / pairwise comparison — the Ranked Robin tally
Legend: For - Equal Support - Against   (row vs column)
                  |  Granny Smith   |     Gala       |     Fuji       |   McIntosh     |  Honeycrisp    |   Pink Lady    | Red Delicious  |    Banana      |
------------------------------------------------------------------------------------------------------------------------------------------------------------
   Granny Smith > |       ---       |   3 - 0 - 6    |   8 - 0 - 1    |   8 - 0 - 1    |   8 - 0 - 1    |   8 - 0 - 1    |   8 - 0 - 1    |   7 - 0 - 2    |
           Gala > |    6 - 0 - 3    |      ---       |   8 - 0 - 1    |   8 - 0 - 1    |   8 - 0 - 1    |   8 - 0 - 1    |   7 - 0 - 2    |   7 - 0 - 2    |
           Fuji > |    1 - 0 - 8    |   1 - 0 - 8    |      ---       |   7 - 0 - 2    |   7 - 0 - 2    |   8 - 0 - 1    |   7 - 0 - 2    |   7 - 0 - 2    |
       McIntosh > |    1 - 0 - 8    |   1 - 0 - 8    |   2 - 0 - 7    |      ---       |   2 - 0 - 7    |   3 - 0 - 6    |   5 - 0 - 4    |   6 - 0 - 3    |
     Honeycrisp > |    1 - 0 - 8    |   1 - 0 - 8    |   2 - 0 - 7    |   7 - 0 - 2    |      ---       |   8 - 0 - 1    |   7 - 0 - 2    |   6 - 0 - 3    |
      Pink Lady > |    1 - 0 - 8    |   1 - 0 - 8    |   1 - 0 - 8    |   6 - 0 - 3    |   1 - 0 - 8    |      ---       |   7 - 0 - 2    |   6 - 0 - 3    |
  Red Delicious > |    1 - 0 - 8    |   2 - 0 - 7    |   2 - 0 - 7    |   4 - 0 - 5    |   2 - 0 - 7    |   2 - 0 - 7    |      ---       |   7 - 0 - 2    |
         Banana > |    2 - 0 - 7    |   2 - 0 - 7    |   2 - 0 - 7    |   3 - 0 - 6    |   3 - 0 - 6    |   3 - 0 - 6    |   2 - 0 - 7    |      ---       |

Win–loss record — Copeland score = wins + ½·ties (highest score wins; ties broken by the Ranked Robin degrees, then lot order):
    #  Candidate      W–L–T  Copeland  Margin  Beats
    1  Gala           7–0–0         7     +41  Granny Smith, Fuji, Honeycrisp, Pink Lady, McIntosh, Red Delicious, Banana
    2  Granny Smith   6–1–0         6     +37  Fuji, Honeycrisp, Pink Lady, McIntosh, Red Delicious, Banana
    3  Fuji           5–2–0         5     +13  Honeycrisp, Pink Lady, McIntosh, Red Delicious, Banana
    4  Honeycrisp     4–3–0         4      +1  Pink Lady, McIntosh, Red Delicious, Banana
    5  Pink Lady      3–4–0         3     -17  McIntosh, Red Delicious, Banana
    6  McIntosh       2–5–0         2     -23  Red Delicious, Banana
    7  Red Delicious  1–6–0         1     -23  Banana
    8  Banana         0–7–0         0     -29  —

Winner — Ranked Robin (RCV-RR): Gala
   beats every opponent head-to-head — the Condorcet winner.
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Smith Set (the generalized Condorcet winner) ---
The smallest group whose every member beats every candidate outside it —
the honest answer to "who is even in contention?".
   Smith set (1 of 8): Gala
   Outside (7):        Granny Smith, Fuji, McIntosh, Honeycrisp, Pink Lady, Red Delicious, Banana
   One member ⇒ Gala is the Condorcet winner, beating every rival head-to-head.
   Ranked Robin (RCV-RR) winner Gala is INSIDE the Smith set. ✓
      Guaranteed: Ranked Robin (Copeland) is Smith-efficient — every member of
      the set outscores every outsider, so the top of the win–loss table is
      always inside the set, however the tie among them is then broken.
   More: 07_Concepts/topics/smith_set.md
```

Everything in one file: the [`_tabulated` mirror](../_main_tabulated/07g_apples_full_menu_ranked_robin_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/split_voting/_main/07g_apples_full_menu_ranked_robin.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../07_Concepts/topics/condorcet/README.md)
- [Ties & tie-breaking (topic hub)](../../../../07_Concepts/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [00_plurality_vs_majority](00_plurality_vs_majority.md) · [01_political_left_split](01_political_left_split.md) · [02_icecream_chocolate_split](02_icecream_chocolate_split.md) · [03_lunch_veggie_vs_meat](03_lunch_veggie_vs_meat.md) · [04_star_wars_vote_split](04_star_wars_vote_split.md) · [05a_residual_split_bullet-voting](05a_residual_split_bullet-voting.md) · [05b_residual_split_expressive-fix](05b_residual_split_expressive-fix.md) · [06_sub_majority_not_spoiled](06_sub_majority_not_spoiled.md) · [07a_apples_two_candidates](07a_apples_two_candidates.md) · [07b_apples_six_candidates](07b_apples_six_candidates.md) · [07c_apples_full_menu](07c_apples_full_menu.md) · [07d_apples_full_menu_star](07d_apples_full_menu_star.md) · [07e_apples_full_menu_approval](07e_apples_full_menu_approval.md) · [07f_apples_full_menu_irv](07f_apples_full_menu_irv.md) · [08a_smallest_spoiler_plurality](08a_smallest_spoiler_plurality.md) · [08b_smallest_spoiler_star](08b_smallest_spoiler_star.md) · [08c_smallest_spoiler_ranked_robin](08c_smallest_spoiler_ranked_robin.md) · [09a_clones_are_voters_not_labels](09a_clones_are_voters_not_labels.md) · [09b_same_ballots_grouped_by_label](09b_same_ballots_grouped_by_label.md)
