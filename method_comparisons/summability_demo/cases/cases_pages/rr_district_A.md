---
search:
  exclude: true
---

# Summability demo — District A, counted by Ranked Robin

*Generated from [`rr_district_A.yaml`](../rr_district_A.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../../05_Ranked_Robin/01_Learn/README.md) · **1 seat** · **Expected winner:** B

## Scenario

District A of the two-district summability demo, counted by Ranked Robin
(RCV-RR / Copeland) instead of IRV. Same ranked ballots as irv_district_A.
The summable artifact is the pairwise (For–Against–Equal) matrix: B beats both
A and C, so B is the Condorcet winner here. Combine with rr_district_B by
ADDING the matrices cell-by-cell (see rr_combined) — the sum recovers the true
winner without pooling ballots, the summability property IRV's count lacks.

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
6:A
4:B
3:C>B>A
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
--- Ranked Robin (RCV-RR / Copeland) Method (single winner) ---
 Tabulating 13 ballots (ranked ballots).

Ballots:
     6 × A
     4 × B
     3 × C > B > A

Round-Robin — every pair, head-to-head (For – Against):
   B  beats A   7 – 6
   A  beats C   6 – 3
   B  beats C   4 – 3

--- Pairwise (Round-Robin) Matrix ---
Head-to-head / pairwise comparison — the Ranked Robin tally
Legend: For - Equal Support - Against   (row vs column)
      |     A     |    B     |    C     |
-----------------------------------------
  A > |    ---    |6 - 0 - 7 |6 - 4 - 3 |
  B > | 7 - 0 - 6 |   ---    |4 - 6 - 3 |
  C > | 3 - 4 - 6 |3 - 6 - 4 |   ---    |

Win–loss record — Copeland score = wins + ½·ties (highest score wins; ties broken by the Ranked Robin degrees, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  B          2–0–0         2      +2  A, C
    2  A          1–1–0         1      +2  C
    3  C          0–2–0         0      -4  —

Winner — Ranked Robin (RCV-RR): B
   beats every opponent head-to-head — the Condorcet winner.
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Smith Set (the generalized Condorcet winner) ---
The smallest group whose every member beats every candidate outside it —
the honest answer to "who is even in contention?".
   Smith set (1 of 3): B
   Outside (2):        A, C
   One member ⇒ B is the Condorcet winner, beating every rival head-to-head.
   Ranked Robin (RCV-RR) winner B is INSIDE the Smith set. ✓
      Guaranteed: Ranked Robin (Copeland) is Smith-efficient — every member of
      the set outscores every outsider, so the top of the win–loss table is
      always inside the set, however the tie among them is then broken.
   More: 07_Concepts/topics/smith_set.md
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/rr_district_A_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/summability_demo/cases/rr_district_A.yaml
```

## See also

- [Summability (topic hub)](../../../../07_Concepts/topics/summability/README.md)
- [Condorcet efficiency (topic hub)](../../../../07_Concepts/topics/condorcet/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [irv_combined](irv_combined.md) · [irv_district_A](irv_district_A.md) · [irv_district_B](irv_district_B.md) · [rr_combined](rr_combined.md) · [rr_district_B](rr_district_B.md) · [star_combined](star_combined.md) · [star_district_A](star_district_A.md) · [star_district_B](star_district_B.md)
