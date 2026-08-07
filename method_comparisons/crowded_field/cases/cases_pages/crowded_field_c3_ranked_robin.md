---
search:
  exclude: true
---

# Crowded field, rung 3 — 3 candidates, 65 voters, counted by Ranked Robin

*Generated from [`crowded_field_c3_ranked_robin.yaml`](../crowded_field_c3_ranked_robin.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../../05_Ranked_Robin/01_Learn/README.md) · **1 seat** · **Expected winner:** Diego

**Official tie-break (lot) order:** Ana > Diego > Greta — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

RUNG 1, counted by Ranked Robin. Diego beats Ana 49–16 and Greta 50–15: a clean
Condorcet winner and a Smith set of one. Agrees with crowded_field_c3_star.yaml and
with every other method at this rung.

Same 65 voters and the same fixed candidate positions as crowded_field_c3_star.yaml;
this file hands them a ranked ballot instead of a 0–5 one.

Construction: build_ladder.py in this folder. 65 voters in seven blocs at 0, 4, 8, 12,
16, 20, 24 (sizes 6, 10, 13, 9, 12, 8, 7); candidates fixed at Ana 1 · Bruno 6 ·
Clara 9 · Diego 11 · Elsa 14 · Felix 16 · Greta 22; utility = minus distance; scores =
each bloc's own min-max scaling onto 0–5. Nothing is tuned, and no count at any rung is
settled by a tie-break.

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
6:Ana>Diego>Greta    # bloc at 0
10:Ana>Diego>Greta    # bloc at 4
13:Diego>Ana>Greta    # bloc at 8
9:Diego>Greta>Ana    # bloc at 12
12:Diego>Greta>Ana    # bloc at 16
8:Greta>Diego>Ana    # bloc at 20
7:Greta>Diego>Ana    # bloc at 24
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
--- Ranked Robin (RCV-RR / Copeland) Method (single winner) ---
 Tabulating 65 ballots (ranked ballots).

Ballots:
    16 × Ana > Diego > Greta
    13 × Diego > Ana > Greta
    21 × Diego > Greta > Ana
    15 × Greta > Diego > Ana

Round-Robin — every pair, head-to-head (For – Against):
   Diego  beats Ana     49 – 16
   Greta  beats Ana     36 – 29
   Diego  beats Greta   50 – 15

--- Pairwise (Round-Robin) Matrix ---
Head-to-head / pairwise comparison — the Ranked Robin tally
Legend: For - Equal Support - Against   (row vs column)
          |     Ana      |   Diego     |   Greta     |
------------------------------------------------------
    Ana > |     ---      |16 -  0 - 49 |29 -  0 - 36 |
  Diego > | 49 -  0 - 16 |    ---      |50 -  0 - 15 |
  Greta > | 36 -  0 - 29 |15 -  0 - 50 |    ---      |

Win–loss record — Copeland score = wins + ½·ties (highest score wins; ties broken by total margin, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  Diego      2–0–0         2     +68  Greta, Ana
    2  Greta      1–1–0         1     -28  Ana
    3  Ana        0–2–0         0     -40  —

Winner — Ranked Robin (RCV-RR): Diego
   beats every opponent head-to-head — the Condorcet winner.
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Smith Set (the generalized Condorcet winner) ---
The smallest group whose every member beats every candidate outside it —
the honest answer to "who is even in contention?".
   Smith set (1 of 3): Diego
   Outside (2):        Ana, Greta
   One member ⇒ Diego is the Condorcet winner, beating every rival head-to-head.
   Ranked Robin (RCV-RR) winner Diego is INSIDE the Smith set. ✓
      Guaranteed: Ranked Robin (Copeland) is Smith-efficient — every member of
      the set outscores every outsider, so the top of the win–loss table is
      always inside the set, however the tie among them is then broken.
   More: 07_Concepts/topics/smith_set.md
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/crowded_field_c3_ranked_robin_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/crowded_field/cases/crowded_field_c3_ranked_robin.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../07_Concepts/topics/condorcet/README.md)
- [Ties & tie-breaking (topic hub)](../../../../07_Concepts/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [crowded_field_c3_approval](crowded_field_c3_approval.md) · [crowded_field_c3_irv](crowded_field_c3_irv.md) · [crowded_field_c3_star](crowded_field_c3_star.md) · [crowded_field_c5_approval](crowded_field_c5_approval.md) · [crowded_field_c5_irv](crowded_field_c5_irv.md) · [crowded_field_c5_ranked_robin](crowded_field_c5_ranked_robin.md) · [crowded_field_c5_star](crowded_field_c5_star.md) · [crowded_field_c7_approval](crowded_field_c7_approval.md) · [crowded_field_c7_irv](crowded_field_c7_irv.md) · [crowded_field_c7_ranked_robin](crowded_field_c7_ranked_robin.md) · [crowded_field_c7_star](crowded_field_c7_star.md)
