---
search:
  exclude: true
---

# Crowded field, rung 7 — 7 candidates, 65 voters, counted by Ranked Robin

*Generated from [`crowded_field_c7_ranked_robin.yaml`](../crowded_field_c7_ranked_robin.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../../05_Ranked_Robin/01_Learn/README.md) · **1 seat** · **Expected winner:** Diego

**Official tie-break (lot) order:** Ana > Bruno > Clara > Diego > Elsa > Felix > Greta — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

RUNG 3, counted by Ranked Robin — the control for the whole ladder.

Diego beats all SIX rivals head-to-head. The electorate's answer has not budged since
rung 1, and Ranked Robin returns it, because a ranked ballot at seven candidates can
still say which of Clara and Diego a voter prefers: **Diego beats Clara 36–29** right
here in the round-robin. The 0–5 score ballot in crowded_field_c7_star.yaml largely
cannot — 25 of 65 voters score the two identically there, and Clara takes the runoff
23–17 out of what is left.

So this file is the control, and it carries the caveat that goes with being one: it
reads a full-resolution ranking while the STAR file reads six rungs. Part of the gap
between the two at this rung is ballot expressiveness rather than tabulation rule. A
real 0–5 STAR election really does have only six rungs, so the cost still lands on
STAR — but it is not the automatic runoff that caused it. The folder README works
through both halves of that.

Same 65 voters and the same fixed candidate positions as crowded_field_c7_star.yaml;
this file hands them a ranked ballot instead of a 0–5 one.

Construction: build_ladder.py in this folder. 65 voters in seven blocs at 0, 4, 8, 12,
16, 20, 24 (sizes 6, 10, 13, 9, 12, 8, 7); candidates fixed at Ana 1 · Bruno 6 ·
Clara 9 · Diego 11 · Elsa 14 · Felix 16 · Greta 22; utility = minus distance; scores =
each bloc's own min-max scaling onto 0–5. Nothing is tuned, and no count at any rung is
settled by a tie-break.

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
6:Ana>Bruno>Clara>Diego>Elsa>Felix>Greta    # bloc at 0
10:Bruno>Ana>Clara>Diego>Elsa>Felix>Greta    # bloc at 4
13:Clara>Bruno>Diego>Elsa>Ana>Felix>Greta    # bloc at 8
9:Diego>Elsa>Clara>Felix>Bruno>Greta>Ana    # bloc at 12
12:Felix>Elsa>Diego>Greta>Clara>Bruno>Ana    # bloc at 16
8:Greta>Felix>Elsa>Diego>Clara>Bruno>Ana    # bloc at 20
7:Greta>Felix>Elsa>Diego>Clara>Bruno>Ana    # bloc at 24
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
--- Ranked Robin (RCV-RR / Copeland) Method (single winner) ---
 Tabulating 65 ballots (ranked ballots).

Ballots:
     6 × Ana > Bruno > Clara > Diego > Elsa > Felix > Greta
    10 × Bruno > Ana > Clara > Diego > Elsa > Felix > Greta
    13 × Clara > Bruno > Diego > Elsa > Ana > Felix > Greta
     9 × Diego > Elsa > Clara > Felix > Bruno > Greta > Ana
    12 × Felix > Elsa > Diego > Greta > Clara > Bruno > Ana
    15 × Greta > Felix > Elsa > Diego > Clara > Bruno > Ana

Round-Robin — every pair, head-to-head (For – Against):
   Bruno  beats Ana     59 –  6
   Clara  beats Ana     49 – 16
   Diego  beats Ana     49 – 16
   Elsa   beats Ana     49 – 16
   Felix  beats Ana     36 – 29
   Greta  beats Ana     36 – 29
   Clara  beats Bruno   49 – 16
   Diego  beats Bruno   36 – 29
   Elsa   beats Bruno   36 – 29
   Felix  beats Bruno   36 – 29
   Bruno  beats Greta   38 – 27
   Diego  beats Clara   36 – 29
   Elsa   beats Clara   36 – 29
   Clara  beats Felix   38 – 27
   Clara  beats Greta   38 – 27
   Diego  beats Elsa    38 – 27
   Diego  beats Felix   38 – 27
   Diego  beats Greta   50 – 15
   Elsa   beats Felix   38 – 27
   Elsa   beats Greta   50 – 15
   Felix  beats Greta   50 – 15

--- Pairwise (Round-Robin) Matrix ---
Head-to-head / pairwise comparison — the Ranked Robin tally
Legend: For - Equal Support - Against   (row vs column)
          |     Ana      |   Bruno     |   Clara     |   Diego     |    Elsa     |   Felix     |   Greta     |
--------------------------------------------------------------------------------------------------------------
    Ana > |     ---      | 6 -  0 - 59 |16 -  0 - 49 |16 -  0 - 49 |16 -  0 - 49 |29 -  0 - 36 |29 -  0 - 36 |
  Bruno > | 59 -  0 -  6 |    ---      |16 -  0 - 49 |29 -  0 - 36 |29 -  0 - 36 |29 -  0 - 36 |38 -  0 - 27 |
  Clara > | 49 -  0 - 16 |49 -  0 - 16 |    ---      |29 -  0 - 36 |29 -  0 - 36 |38 -  0 - 27 |38 -  0 - 27 |
  Diego > | 49 -  0 - 16 |36 -  0 - 29 |36 -  0 - 29 |    ---      |38 -  0 - 27 |38 -  0 - 27 |50 -  0 - 15 |
   Elsa > | 49 -  0 - 16 |36 -  0 - 29 |36 -  0 - 29 |27 -  0 - 38 |    ---      |38 -  0 - 27 |50 -  0 - 15 |
  Felix > | 36 -  0 - 29 |36 -  0 - 29 |27 -  0 - 38 |27 -  0 - 38 |27 -  0 - 38 |    ---      |50 -  0 - 15 |
  Greta > | 36 -  0 - 29 |27 -  0 - 38 |27 -  0 - 38 |15 -  0 - 50 |15 -  0 - 50 |15 -  0 - 50 |    ---      |

Win–loss record — Copeland score = wins + ½·ties (highest score wins; ties broken by the Ranked Robin degrees, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  Diego      6–0–0         6    +104  Elsa, Clara, Felix, Bruno, Greta, Ana
    2  Elsa       5–1–0         5     +82  Clara, Felix, Bruno, Greta, Ana
    3  Clara      4–2–0         4     +74  Felix, Bruno, Greta, Ana
    4  Felix      3–3–0         3     +16  Bruno, Greta, Ana
    5  Bruno      2–4–0         2     +10  Greta, Ana
    6  Greta      1–5–0         1    -120  Ana
    7  Ana        0–6–0         0    -166  —

Winner — Ranked Robin (RCV-RR): Diego
   beats every opponent head-to-head — the Condorcet winner.
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Smith Set (the generalized Condorcet winner) ---
The smallest group whose every member beats every candidate outside it —
the honest answer to "who is even in contention?".
   Smith set (1 of 7): Diego
   Outside (6):        Ana, Bruno, Clara, Elsa, Felix, Greta
   One member ⇒ Diego is the Condorcet winner, beating every rival head-to-head.
   Ranked Robin (RCV-RR) winner Diego is INSIDE the Smith set. ✓
      Guaranteed: Ranked Robin (Copeland) is Smith-efficient — every member of
      the set outscores every outsider, so the top of the win–loss table is
      always inside the set, however the tie among them is then broken.
   More: 07_Concepts/topics/smith_set.md
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/crowded_field_c7_ranked_robin_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/crowded_field/cases/crowded_field_c7_ranked_robin.yaml
```

## See also

- [Ties & tie-breaking (topic hub)](../../../../07_Concepts/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)
- [Runoff reversal (worked set)](../../../../01_STAR/02_Examples/runoff_overturns_leader/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [crowded_field_c3_approval](crowded_field_c3_approval.md) · [crowded_field_c3_irv](crowded_field_c3_irv.md) · [crowded_field_c3_ranked_robin](crowded_field_c3_ranked_robin.md) · [crowded_field_c3_star](crowded_field_c3_star.md) · [crowded_field_c5_approval](crowded_field_c5_approval.md) · [crowded_field_c5_irv](crowded_field_c5_irv.md) · [crowded_field_c5_ranked_robin](crowded_field_c5_ranked_robin.md) · [crowded_field_c5_star](crowded_field_c5_star.md) · [crowded_field_c7_approval](crowded_field_c7_approval.md) · [crowded_field_c7_irv](crowded_field_c7_irv.md) · [crowded_field_c7_star](crowded_field_c7_star.md)
