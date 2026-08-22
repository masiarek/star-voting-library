---
search:
  exclude: true
---

# BV2286 — Ballot A (one dog on the paper): Choose-One elects Dog outright

*Generated from [`bv2286_p2wggg_a1_one_dog_plurality.yaml`](../bv2286_p2wggg_a1_one_dog_plurality.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [plurality](../../../../07_Concepts/README.md) · **1 seat** · **Expected winner:** Dog

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/p2wggg) · **[results ↗](https://bettervoting.com/p2wggg/results)** (election `p2wggg` · test `BV2286`).

## Scenario

Race 1 of 7 in the BV2286 "Three dogs and a cat" election (BetterVoting p2wggg). This is the shape a typical best-pet poll uses, and the shape Equal.Vote's own meta_pets uses: ONE name per animal family. Sixty pet owners — 34 dog people (57%), 20 cat people, 6 parrot people. Each voter gets one mark, and the dog side has exactly one name to put it on, so Dog wins with 34 of 60 — an outright majority. There is no vote splitting here and there cannot be: splitting needs two or more similar candidates drawing from one pool of voters, and this ballot offers the dog side a single name. Compare race 3 (bv2286_p2wggg_b1_three_dogs_plurality), where the SAME sixty voters face the same question with three dog breeds on the paper and Choose-One elects the Cat. Live results: https://bettervoting.com/p2wggg/results

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:Dog,Cat,Parrot
14:1,0,0   # Labrador-first dog people — one dog on the ballot, so all one mark
12:1,0,0   # Golden-Retriever-first dog people
8:1,0,0    # German-Shepherd-first dog people
20:0,1,0   # cat people
6:0,0,1    # parrot people
```

## What the engine says

Full report from the [`_tabulated` mirror](../cases_tabulated/bv2286_p2wggg_a1_one_dog_plurality_tabulated.txt) (regenerated on every run; every analysis forced on):

<!-- --8<-- [start:report] -->
```text
--- Choose-One / Plurality Voting Method (single winner) ---
 Tabulating 60 ballots.

                    Dog    Cat   Parrot 
  34 ×               X      -      -    
  20 ×               -      X      -    
  6 ×                -      -      X    

  Count the marks:  Dog 34 · Cat 20 · Parrot 6

Winner — Choose-One / Plurality Voting Method (single winner)
 Dog   (34 of 60 marks)
```
<!-- --8<-- [end:report] -->

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/pet_poll_breed_split/cases/bv2286_p2wggg_a1_one_dog_plurality.yaml
```

## See also

- [Vote splitting (worked set)](../../../split_voting/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [bv2286_p2wggg_a2_one_dog_star](bv2286_p2wggg_a2_one_dog_star.md) · [bv2286_p2wggg_b1_three_dogs_plurality](bv2286_p2wggg_b1_three_dogs_plurality.md) · [bv2286_p2wggg_b2_three_dogs_irv](bv2286_p2wggg_b2_three_dogs_irv.md) · [bv2286_p2wggg_b3_three_dogs_approval](bv2286_p2wggg_b3_three_dogs_approval.md) · [bv2286_p2wggg_b4_three_dogs_star](bv2286_p2wggg_b4_three_dogs_star.md) · [bv2286_p2wggg_b5_three_dogs_ranked_robin](bv2286_p2wggg_b5_three_dogs_ranked_robin.md)
