---
search:
  exclude: true
---

# Same matrix, different plurality — electorate P2: Ranked Robin

*Generated from [`same_matrix_p2_ranked_robin.yaml`](../same_matrix_p2_ranked_robin.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../../05_Ranked_Robin/01_Learn/README.md) · **1 seat** · **Expected winner:** Ben

## Scenario

One of three 12-ballot electorates (P2) that produce the *identical* pairwise
table: Ben beats Ada 7-5, Ada ties Cal 6-6, Ben beats Cal 7-5. Every method that
reads only the pairwise matrix — Ranked Robin, Minimax, Ranked Pairs, Kemeny — and
Borda too, must return the same answer on all three. Ben, here. The companion
Plurality file on this same electorate returns Ben, and the three electorates
give three different plurality winners. That is what it means for plurality to sit
outside the pairwise matrix (Fishburn C3).

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
2:Ada>Ben>Cal
2:Cal>Ben>Ada
3:Ben>Ada>Cal
2:Ben>Cal>Ada
1:Ada>Cal>Ben
2:Cal>Ada>Ben
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
--- Ranked Robin (RCV-RR / Copeland) Method (single winner) ---
 Tabulating 12 ballots (ranked ballots).

Ballots:
     2 × Ada > Ben > Cal
     2 × Cal > Ben > Ada
     3 × Ben > Ada > Cal
     2 × Ben > Cal > Ada
     1 × Ada > Cal > Ben
     2 × Cal > Ada > Ben

Round-Robin — every pair, head-to-head (For – Against):
   Ben  beats Ada   7 – 5
   Ada  ties  Cal   6 – 6
   Ben  beats Cal   7 – 5

--- Pairwise (Round-Robin) Matrix ---
Head-to-head / pairwise comparison — the Ranked Robin tally
Legend: For - Equal Support - Against   (row vs column)
        |    Ada    |   Ben    |   Cal    |
-------------------------------------------
  Ada > |    ---    |5 - 0 - 7 |6 - 0 - 6 |
  Ben > | 7 - 0 - 5 |   ---    |7 - 0 - 5 |
  Cal > | 6 - 0 - 6 |5 - 0 - 7 |   ---    |

Win–loss record — Copeland score = wins + ½·ties (highest score wins; ties broken by the Ranked Robin degrees, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  Ben        2–0–0         2      +4  Ada, Cal
    2  Ada        0–1–1       0.5      -2  —
    3  Cal        0–1–1       0.5      -2  —

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
   Outside (2):        Ada, Cal
   One member ⇒ Ben is the Condorcet winner, beating every rival head-to-head.
   Ranked Robin (RCV-RR) winner Ben is INSIDE the Smith set. ✓
      Guaranteed: Ranked Robin (Copeland) is Smith-efficient — every member of
      the set outscores every outsider, so the top of the win–loss table is
      always inside the set, however the tie among them is then broken.
   More: 07_Concepts/topics/smith_set.md
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/same_matrix_p2_ranked_robin_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/same_matrix_different_plurality/cases/same_matrix_p2_ranked_robin.yaml
```

## See also

- [Ties & tie-breaking (topic hub)](../../../../07_Concepts/topics/ties/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [same_matrix_p1_plurality](same_matrix_p1_plurality.md) · [same_matrix_p1_ranked_robin](same_matrix_p1_ranked_robin.md) · [same_matrix_p2_plurality](same_matrix_p2_plurality.md) · [same_matrix_p3_plurality](same_matrix_p3_plurality.md) · [same_matrix_p3_ranked_robin](same_matrix_p3_ranked_robin.md)
