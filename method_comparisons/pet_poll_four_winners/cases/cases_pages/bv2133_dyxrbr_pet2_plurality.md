---
search:
  exclude: true
---

# BV2133 — Pet poll II (Plurality): the front-runner Dog wins

*Generated from [`bv2133_dyxrbr_pet2_plurality.yaml`](../bv2133_dyxrbr_pet2_plurality.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [plurality](../../../../07_Concepts) · **1 seat** · **Expected winner:** Dog

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/dyxrbr) · **[results ↗](https://bettervoting.com/dyxrbr/results)** (election `dyxrbr` · test `BV2133`).

## Scenario

One of four races in the BV2133 "Pet poll II" (BetterVoting election dyxrbr). Choose-one Plurality: Dog has the most first choices (13 of 32) and wins — even though the other 19 voters rank Dog LAST. Classic first-past-the-post: a polarizing plurality beats broadly-liked rivals. Same electorate as the RCV-IRV race (Fish), Approval race (Bird) and STAR race (Cat): four methods, four winners. BV also elects Dog. Live results: https://bettervoting.com/dyxrbr/results

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Dog,Cat,Fish,Bird
9: 0,0,0,1
10: 0,0,1,0
13: 1,0,0,0
```

## What the engine says

Full report from the [`_tabulated` mirror](../cases_tabulated/bv2133_dyxrbr_pet2_plurality_tabulated.txt) (regenerated on every run; every analysis forced on):

<!-- --8<-- [start:report] -->
```text
--- Choose-One / Plurality Voting Method (single winner) ---
 Tabulating 32 ballots.

                    Dog    Cat    Fish   Bird 
  9 ×                -      -      -      X   
  10 ×               -      -      X      -   
  13 ×               X      -      -      -   

  Count the marks:  Dog 13 · Fish 10 · Bird 9 · Cat 0

Winner — Choose-One / Plurality Voting Method (single winner)
 Dog   (13 of 32 marks)
```
<!-- --8<-- [end:report] -->

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/pet_poll_four_winners/cases/bv2133_dyxrbr_pet2_plurality.yaml
```

## See also

- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [bv2133_dyxrbr_pet2_approval](bv2133_dyxrbr_pet2_approval.md) · [bv2133_dyxrbr_pet2_irv](bv2133_dyxrbr_pet2_irv.md) · [bv2133_dyxrbr_pet2_star](bv2133_dyxrbr_pet2_star.md)
