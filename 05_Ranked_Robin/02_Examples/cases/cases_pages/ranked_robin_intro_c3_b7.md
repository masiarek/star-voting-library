---
search:
  exclude: true
---

# Ranked Robin (RCV-RR) — the smallest round-robin that shows the report

*Generated from [`ranked_robin_intro_c3_b7.yaml`](../ranked_robin_intro_c3_b7.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../01_Learn) · **1 seat** · **Expected winner:** Ben

## Scenario

The three-candidate, seven-ballot election the Ranked Robin lesson opens with —
small enough that every pairwise comparison fits on one screen.

Ada leads on first choices (3 of 7) and finishes LAST. Ben never leads the first
count, yet beats Ada 4-3 and Cara 5-2, so he takes the round-robin 2-0 and is the
Condorcet winner. Cara beats Ada 4-3 and loses to Ben: 1-1.

Copeland scores (wins + 1/2*ties): Ben 2, Cara 1, Ada 0.

This case exists so the lesson can EMBED the report instead of pasting it — the
page shows exactly what the engine prints today, and the test suite notices if
that ever stops being true.

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
3:Ada>Ben>Cara
2:Ben>Cara>Ada
2:Cara>Ben>Ada
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
--- Ranked Robin (RCV-RR / Copeland) Method (single winner) ---
 Tabulating 7 ballots (ranked ballots).

Ballots:
     3 × Ada > Ben > Cara
     2 × Ben > Cara > Ada
     2 × Cara > Ben > Ada

Round-Robin — every pair, head-to-head (For – Against):
   Ben   beats Ada    4 – 3
   Cara  beats Ada    4 – 3
   Ben   beats Cara   5 – 2

--- Pairwise (Round-Robin) Matrix ---
Head-to-head / pairwise comparison — the Ranked Robin tally
Legend: For - Equal Support - Against   (row vs column)
         |    Ada    |   Ben    |  Cara    |
--------------------------------------------
   Ada > |    ---    |3 - 0 - 4 |3 - 0 - 4 |
   Ben > | 4 - 0 - 3 |   ---    |5 - 0 - 2 |
  Cara > | 4 - 0 - 3 |2 - 0 - 5 |   ---    |

Win–loss record — Copeland score = wins + ½·ties (highest score wins; ties broken by total margin, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  Ben        2–0–0         2      +4  Cara, Ada
    2  Cara       1–1–0         1      -2  Ada
    3  Ada        0–2–0         0      -2  —

Winner — Ranked Robin (RCV-RR): Ben
   beats every opponent head-to-head — the Condorcet winner.
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Smith Set (the generalized Condorcet winner) ---
The smallest group whose every member beats every candidate outside it —
the honest answer to "who is even in contention?".
   Smith set (1 of 3): Ben
   Outside (2):        Ada, Cara
   One member ⇒ Ben is the Condorcet winner, beating every rival head-to-head.
   Ranked Robin (RCV-RR) winner Ben is INSIDE the Smith set. ✓
      Guaranteed: Ranked Robin (Copeland) is Smith-efficient — every member of
      the set outscores every outsider, so the top of the win–loss table is
      always inside the set, however the tie among them is then broken.
   More: 07_Concepts/topics/smith_set.md
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/ranked_robin_intro_c3_b7_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 05_Ranked_Robin/02_Examples/cases/ranked_robin_intro_c3_b7.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../07_Concepts/topics/condorcet/README.md)
- [Ties & tie-breaking (topic hub)](../../../../07_Concepts/topics/ties/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [ranked_robin_consensus_center](ranked_robin_consensus_center.md) · [rr_blank_is_last_c4_b3](rr_blank_is_last_c4_b3.md)
