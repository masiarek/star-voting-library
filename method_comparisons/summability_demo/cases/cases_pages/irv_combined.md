---
search:
  exclude: true
---

# Summability demo — RCV-IRV combined A+B (B eliminated; not summable)

*Generated from [`irv_combined.yaml`](../irv_combined.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [RCV-IRV (Instant Runoff)](../../../../06_Other/RCV_IRV/concepts/README.md) · **1 seat** · **Expected winner:** A

## Scenario

Districts A + B merged, counted by RCV-IRV. B won BOTH districts — but in
the combined electorate B has the fewest first choices (8 vs 9 and 9), is
eliminated first, and both B-bullet blocs exhaust. The race then ends in a
GENUINE 9-9 tie between A and C; the engine's seeded coin flip elects A (see
the note at expected_winners). No district subtotal can produce this result:
IRV needs every ballot in one pile. Compare the star_* trio, where
subtotals simply add.

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

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
--- RCV / Instant-Runoff Voting (single winner) ---
  Summability demo — RCV-IRV combined A+B (B eliminated; not summable)
 Tabulating 26 ballots (ranked ballots).

ROUND 1
Candidate      Votes  Status
-----------  -------  --------
A                  9  Hopeful
C                  9  Hopeful
B                  8  Rejected

FINAL RESULT
Candidate      Votes  Status
-----------  -------  --------
A                  9  Elected
C                  9  Rejected
B                  0  Rejected
Blank Votes        8  Rejected


Winner(s) — RCV / Instant-Runoff Voting (single winner)
  A
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
   RCV-IRV winner A is OUTSIDE the Smith set. ✗
      Every member of the set (B) beats A head-to-head, yet
      RCV-IRV elected A anyway. RCV-IRV is not Smith-efficient (nor
      Condorcet-efficient) — this is the shape a center squeeze leaves behind.
   More: 07_Concepts/topics/smith_set.md
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/irv_combined_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/summability_demo/cases/irv_combined.yaml
```

## See also

- [Summability (topic hub)](../../../../07_Concepts/topics/summability/README.md)
- [Ties & tie-breaking (topic hub)](../../../../07_Concepts/topics/ties/README.md)
- [Exhausted ballots (conversation)](../../../../06_Other/RCV_IRV/concepts/exhausted_ballots_301.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [irv_district_A](irv_district_A.md) · [irv_district_B](irv_district_B.md) · [rr_combined](rr_combined.md) · [rr_district_A](rr_district_A.md) · [rr_district_B](rr_district_B.md) · [star_combined](star_combined.md) · [star_district_A](star_district_A.md) · [star_district_B](star_district_B.md)
