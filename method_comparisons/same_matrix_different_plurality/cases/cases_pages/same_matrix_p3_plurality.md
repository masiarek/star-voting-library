---
search:
  exclude: true
---

# Same matrix, different plurality — electorate P3: Choose-One

*Generated from [`same_matrix_p3_plurality.yaml`](../same_matrix_p3_plurality.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [plurality](../../../../07_Concepts) · **1 seat** · **Expected winner:** Cal

## Scenario

The same electorate P3, voting Choose-One: each voter marks only their first
choice, so the ballot keeps the top of the ranking and discards the rest. Tally:
Cal 5, Ben 4, Ada 3 — winner Cal. The Ranked Robin file on this same electorate
elects Ben, and all three electorates in this folder share one pairwise table
while their plurality winners differ. Plurality's winner is not a function of
the pairwise matrix.

## Parameters (from the YAML)

```yaml
voting_method: Plurality
num_winners: 1
expected_winners: [Cal]
```

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:Ada,Ben,Cal
3:1,0,0
5:0,0,1
4:0,1,0
```

## What the engine says

Full report from the [`_tabulated` mirror](../cases_tabulated/same_matrix_p3_plurality_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Choose-One / Plurality Voting Method (single winner) ---
 Tabulating 12 ballots.

                    Ada    Ben    Cal  
  3 ×                X      -      -   
  5 ×                -      -      X   
  4 ×                -      X      -   

  Count the marks:  Cal 5 · Ben 4 · Ada 3

Winner — Choose-One / Plurality Voting Method (single winner)
 Cal   (5 of 12 marks)
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/same_matrix_different_plurality/cases/same_matrix_p3_plurality.yaml
```

## See also

- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [same_matrix_p1_plurality](same_matrix_p1_plurality.md) · [same_matrix_p1_ranked_robin](same_matrix_p1_ranked_robin.md) · [same_matrix_p2_plurality](same_matrix_p2_plurality.md) · [same_matrix_p2_ranked_robin](same_matrix_p2_ranked_robin.md) · [same_matrix_p3_ranked_robin](same_matrix_p3_ranked_robin.md)
