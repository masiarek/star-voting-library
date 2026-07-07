# Summability demo — District B, counted by Ranked Robin

*Generated from [`rr_district_B.yaml`](../rr_district_B.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../00_start_here/RCV_Ranked_Robin) · **1 seat** · **Expected winner:** B

## Scenario

District B of the two-district summability demo, counted by Ranked Robin.
Same ranked ballots as irv_district_B. B again beats both A and C head-to-head
(the Condorcet winner). Its pairwise matrix ADDS to District A's to give the
combined result (rr_combined) — no ballot pooling required.

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
6:C
4:B
3:A>B>C
```

## What the engine says

Full report from the [`_tabulated` mirror](../summability_demo_tabulated/rr_district_B_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Ranked Robin (RCV-RR / Copeland) Method (single winner) ---
 Tabulating 13 ballots (ranked ballots).

Ballots:
     6 × C
     4 × B
     3 × A > B > C

Round-Robin — every pair, head-to-head (For – Against):
   B  beats C   7 – 6
   C  beats A   6 – 3
   B  beats A   4 – 3

--- Pairwise (Round-Robin) Matrix ---
Head-to-head / pairwise comparison — the Ranked Robin tally
Legend: For - Equal Support - Against   (row vs column)
      |     C     |    B     |    A     |
-----------------------------------------
  C > |    ---    |6 - 0 - 7 |6 - 4 - 3 |
  B > | 7 - 0 - 6 |   ---    |4 - 6 - 3 |
  A > | 3 - 4 - 6 |3 - 6 - 4 |   ---    |

Win–loss record — Copeland score = wins + ½·ties (most wins wins; ties broken by total margin, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  B          2–0–0         2      +2  C, A
    2  C          1–1–0         1      +2  A
    3  A          0–2–0         0      -4  —

Winner — Ranked Robin (RCV-RR): B
   beats every opponent head-to-head — the Condorcet winner.
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/summability_demo/rr_district_B.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Summability (topic hub)](../../../00_start_here/topics/summability/README.md)
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [irv_combined](irv_combined.md) · [irv_district_A](irv_district_A.md) · [irv_district_B](irv_district_B.md) · [rr_combined](rr_combined.md) · [rr_district_A](rr_district_A.md) · [star_combined](star_combined.md) · [star_district_A](star_district_A.md) · [star_district_B](star_district_B.md)
