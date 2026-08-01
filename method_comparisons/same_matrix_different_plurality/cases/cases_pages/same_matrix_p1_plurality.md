# Same matrix, different plurality — electorate P1: Choose-One

*Generated from [`same_matrix_p1_plurality.yaml`](../same_matrix_p1_plurality.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [plurality](../../../../07_Concepts) · **1 seat** · **Expected winner:** Ada

## Scenario

The same electorate P1, voting Choose-One: each voter marks only their first
choice, so the ballot keeps the top of the ranking and discards the rest. Tally:
Ada 5, Cal 4, Ben 3 — winner Ada. The Ranked Robin file on this same electorate
elects Ben, and all three electorates in this folder share one pairwise table
while their plurality winners differ. Plurality's winner is not a function of
the pairwise matrix.

## Parameters (from the YAML)

```yaml
voting_method: Plurality
num_winners: 1
expected_winners:
- Ada
```

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:Ada,Ben,Cal
4:1,0,0
1:1,0,0
4:0,0,1
3:0,1,0
```

## What the engine says

Full report from the [`_tabulated` mirror](../cases_tabulated/same_matrix_p1_plurality_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Choose-One / Plurality Voting Method (single winner) ---
 Tabulating 12 ballots.

                    Ada    Ben    Cal  
  5 ×                X      -      -   
  4 ×                -      -      X   
  3 ×                -      X      -   

  Count the marks:  Ada 5 · Cal 4 · Ben 3

Winner — Choose-One / Plurality Voting Method (single winner)
 Ada   (5 of 12 marks)
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/same_matrix_different_plurality/cases/same_matrix_p1_plurality.yaml
```

## See also

- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [same_matrix_p1_ranked_robin](same_matrix_p1_ranked_robin.md) · [same_matrix_p2_plurality](same_matrix_p2_plurality.md) · [same_matrix_p2_ranked_robin](same_matrix_p2_ranked_robin.md) · [same_matrix_p3_plurality](same_matrix_p3_plurality.md) · [same_matrix_p3_ranked_robin](same_matrix_p3_ranked_robin.md)
