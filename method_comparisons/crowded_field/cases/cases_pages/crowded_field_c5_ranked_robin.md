---
search:
  exclude: true
---

# Crowded field, rung 5 — 5 candidates, 65 voters, counted by Ranked Robin

*Generated from [`crowded_field_c5_ranked_robin.yaml`](../crowded_field_c5_ranked_robin.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../../05_Ranked_Robin/01_Learn/README.md) · **1 seat** · **Expected winner:** Diego

**Official tie-break (lot) order:** Ana > Bruno > Diego > Elsa > Greta — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

RUNG 2, counted by Ranked Robin. Two candidates joined; Diego still beats all four
rivals, so the Smith set is still {Diego} and the electorate's answer has not moved.
Hold this next to crowded_field_c5_star.yaml, where STAR agrees — and against
crowded_field_c5_irv.yaml, where instant runoff and Choose-One do not.

Same 65 voters and the same fixed candidate positions as crowded_field_c5_star.yaml;
this file hands them a ranked ballot instead of a 0–5 one.

Construction: build_ladder.py in this folder. 65 voters in seven blocs at 0, 4, 8, 12,
16, 20, 24 (sizes 6, 10, 13, 9, 12, 8, 7); candidates fixed at Ana 1 · Bruno 6 ·
Clara 9 · Diego 11 · Elsa 14 · Felix 16 · Greta 22; utility = minus distance; scores =
each bloc's own min-max scaling onto 0–5. Nothing is tuned, and no count at any rung is
settled by a tie-break.

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
6:Ana>Bruno>Diego>Elsa>Greta    # bloc at 0
10:Bruno>Ana>Diego>Elsa>Greta    # bloc at 4
13:Bruno>Diego>Elsa>Ana>Greta    # bloc at 8
9:Diego>Elsa>Bruno>Greta>Ana    # bloc at 12
12:Elsa>Diego>Greta>Bruno>Ana    # bloc at 16
8:Greta>Elsa>Diego>Bruno>Ana    # bloc at 20
7:Greta>Elsa>Diego>Bruno>Ana    # bloc at 24
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
--- Ranked Robin (RCV-RR / Copeland) Method (single winner) ---
 Tabulating 65 ballots (ranked ballots).

Ballots:
     6 × Ana > Bruno > Diego > Elsa > Greta
    10 × Bruno > Ana > Diego > Elsa > Greta
    13 × Bruno > Diego > Elsa > Ana > Greta
     9 × Diego > Elsa > Bruno > Greta > Ana
    12 × Elsa > Diego > Greta > Bruno > Ana
    15 × Greta > Elsa > Diego > Bruno > Ana

Round-Robin — every pair, head-to-head (For – Against):
   Bruno  beats Ana     59 –  6
   Diego  beats Ana     49 – 16
   Elsa   beats Ana     49 – 16
   Greta  beats Ana     36 – 29
   Diego  beats Bruno   36 – 29
   Elsa   beats Bruno   36 – 29
   Bruno  beats Greta   38 – 27
   Diego  beats Elsa    38 – 27
   Diego  beats Greta   50 – 15
   Elsa   beats Greta   50 – 15

--- Pairwise (Round-Robin) Matrix ---
Head-to-head / pairwise comparison — the Ranked Robin tally
Legend: For - Equal Support - Against   (row vs column)
          |     Ana      |   Bruno     |   Diego     |    Elsa     |   Greta     |
----------------------------------------------------------------------------------
    Ana > |     ---      | 6 -  0 - 59 |16 -  0 - 49 |16 -  0 - 49 |29 -  0 - 36 |
  Bruno > | 59 -  0 -  6 |    ---      |29 -  0 - 36 |29 -  0 - 36 |38 -  0 - 27 |
  Diego > | 49 -  0 - 16 |36 -  0 - 29 |    ---      |38 -  0 - 27 |50 -  0 - 15 |
   Elsa > | 49 -  0 - 16 |36 -  0 - 29 |27 -  0 - 38 |    ---      |50 -  0 - 15 |
  Greta > | 36 -  0 - 29 |27 -  0 - 38 |15 -  0 - 50 |15 -  0 - 50 |    ---      |

Win–loss record — Copeland score = wins + ½·ties (highest score wins; ties broken by total margin, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  Diego      4–0–0         4     +86  Elsa, Bruno, Greta, Ana
    2  Elsa       3–1–0         3     +64  Bruno, Greta, Ana
    3  Bruno      2–2–0         2     +50  Greta, Ana
    4  Greta      1–3–0         1     -74  Ana
    5  Ana        0–4–0         0    -126  —

Winner — Ranked Robin (RCV-RR): Diego
   beats every opponent head-to-head — the Condorcet winner.
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Smith Set (the generalized Condorcet winner) ---
The smallest group whose every member beats every candidate outside it —
the honest answer to "who is even in contention?".
   Smith set (1 of 5): Diego
   Outside (4):        Ana, Bruno, Elsa, Greta
   One member ⇒ Diego is the Condorcet winner, beating every rival head-to-head.
   Ranked Robin (RCV-RR) winner Diego is INSIDE the Smith set. ✓
      Guaranteed: Ranked Robin (Copeland) is Smith-efficient — every member of
      the set outscores every outsider, so the top of the win–loss table is
      always inside the set, however the tie among them is then broken.
   More: 07_Concepts/topics/smith_set.md
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/crowded_field_c5_ranked_robin_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/crowded_field/cases/crowded_field_c5_ranked_robin.yaml
```

## See also

- [Ties & tie-breaking (topic hub)](../../../../07_Concepts/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)
- [Runoff reversal (worked set)](../../../../01_STAR/02_Examples/runoff_overturns_leader/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [crowded_field_c3_approval](crowded_field_c3_approval.md) · [crowded_field_c3_irv](crowded_field_c3_irv.md) · [crowded_field_c3_ranked_robin](crowded_field_c3_ranked_robin.md) · [crowded_field_c3_star](crowded_field_c3_star.md) · [crowded_field_c5_approval](crowded_field_c5_approval.md) · [crowded_field_c5_irv](crowded_field_c5_irv.md) · [crowded_field_c5_star](crowded_field_c5_star.md) · [crowded_field_c7_approval](crowded_field_c7_approval.md) · [crowded_field_c7_irv](crowded_field_c7_irv.md) · [crowded_field_c7_ranked_robin](crowded_field_c7_ranked_robin.md) · [crowded_field_c7_star](crowded_field_c7_star.md)
