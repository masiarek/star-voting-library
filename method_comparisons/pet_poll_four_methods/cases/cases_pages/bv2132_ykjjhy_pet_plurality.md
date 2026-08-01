---
search:
  exclude: true
---

# BV2132 — Pet poll (Plurality): the front-runner Dog wins

*Generated from [`bv2132_ykjjhy_pet_plurality.yaml`](../bv2132_ykjjhy_pet_plurality.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [plurality](../../../../07_Concepts) · **1 seat** · **Expected winner:** Dog

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/ykjjhy) · **[results ↗](https://bettervoting.com/ykjjhy/results)** (election `ykjjhy`).

## Scenario

One of the four races in the BV2132 "Pet poll" (BetterVoting election ykjjhy). This is the choose-one Plurality race: each voter marks a single top pet. Dog has the most first choices (9 of 22) and wins — even though a 13-voter majority ranks Dog LAST. This is the spoiler/first-past-the-post failure: the consensus candidate Cat (the Condorcet winner) has only 6 first choices and loses. Same electorate as the Approval/STAR races (Cat wins) and the RCV-IRV race (Fish wins). BV also elects Dog. Live results: https://bettervoting.com/ykjjhy/results

## Parameters (from the YAML)

```yaml
voting_method: Plurality
num_winners: 1
expected_winners:
- Dog
bv_election_id: ykjjhy
bv_test_id: BV2132
```

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Dog,Cat,Fish
9: 1,0,0
7: 0,0,1
6: 0,1,0
```

## What the engine says

Full report from the [`_tabulated` mirror](../cases_tabulated/bv2132_ykjjhy_pet_plurality_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Choose-One / Plurality Voting Method (single winner) ---
 Tabulating 22 ballots.

                    Dog    Cat    Fish 
  9 ×                X      -      -   
  7 ×                -      -      X   
  6 ×                -      X      -   

  Count the marks:  Dog 9 · Fish 7 · Cat 6

Winner — Choose-One / Plurality Voting Method (single winner)
 Dog   (9 of 22 marks)
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/pet_poll_four_methods/cases/bv2132_ykjjhy_pet_plurality.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../07_Concepts/topics/condorcet/README.md)
- [Vote splitting (worked set)](../../../split_voting/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [bv2132_ykjjhy_pet_approval](bv2132_ykjjhy_pet_approval.md) · [bv2132_ykjjhy_pet_irv](bv2132_ykjjhy_pet_irv.md) · [bv2132_ykjjhy_pet_star](bv2132_ykjjhy_pet_star.md)
