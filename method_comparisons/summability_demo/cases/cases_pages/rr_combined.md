# Summability demo — Combined (A+B), counted by Ranked Robin

*Generated from [`rr_combined.yaml`](../rr_combined.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../../00_start_here/RCV_Ranked_Robin) · **1 seat** · **Expected winner:** B

## Scenario

The two districts merged, counted by Ranked Robin. These are the SAME ranked
ballots IRV could not combine (under IRV, B wins both districts yet is
eliminated when merged — see irv_combined). Ranked Robin's pairwise matrix is
summable: District A's matrix + District B's matrix EQUALS this combined matrix
cell-by-cell, and from it B beats A (11–9) and C (11–9) → B is the Condorcet
winner. The candidate who won both districts wins the merge, reached by adding
precinct tables, never pooling ballots.

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
6:A
4:B
3:C>B>A
6:C
4:B
3:A>B>C
```

## What the engine says

Full report from the [`_tabulated` mirror](../cases_tabulated/rr_combined_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Ranked Robin (RCV-RR / Copeland) Method (single winner) ---
 Tabulating 26 ballots (ranked ballots).

Ballots:
     6 × A
     8 × B
     3 × C > B > A
     6 × C
     3 × A > B > C

Round-Robin — every pair, head-to-head (For – Against):
   B  beats A   11 –  9
   A  ties  C    9 –  9
   B  beats C   11 –  9

--- Pairwise (Round-Robin) Matrix ---
Head-to-head / pairwise comparison — the Ranked Robin tally
Legend: For - Equal Support - Against   (row vs column)
      |      A       |     B       |     C       |
--------------------------------------------------
  A > |     ---      | 9 -  6 - 11 | 9 -  8 -  9 |
  B > | 11 -  6 -  9 |    ---      |11 -  6 -  9 |
  C > |  9 -  8 -  9 | 9 -  6 - 11 |    ---      |

Win–loss record — Copeland score = wins + ½·ties (most wins wins; ties broken by total margin, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  B          2–0–0         2      +4  A, C
    2  A          0–1–1       0.5      -2  —
    3  C          0–1–1       0.5      -2  —

Winner — Ranked Robin (RCV-RR): B
   beats every opponent head-to-head — the Condorcet winner.
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/summability_demo/cases/rr_combined.yaml
```

## See also

- [Summability (topic hub)](../../../../00_start_here/topics/summability/README.md)
- [Condorcet efficiency (topic hub)](../../../../00_start_here/topics/condorcet/README.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [irv_combined](irv_combined.md) · [irv_district_A](irv_district_A.md) · [irv_district_B](irv_district_B.md) · [rr_district_A](rr_district_A.md) · [rr_district_B](rr_district_B.md) · [star_combined](star_combined.md) · [star_district_A](star_district_A.md) · [star_district_B](star_district_B.md)
