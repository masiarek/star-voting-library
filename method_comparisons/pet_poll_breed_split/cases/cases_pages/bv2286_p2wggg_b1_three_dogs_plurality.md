---
search:
  exclude: true
---

# BV2286 — Ballot B (three dogs on the paper): Choose-One elects the CAT on 33%

*Generated from [`bv2286_p2wggg_b1_three_dogs_plurality.yaml`](../bv2286_p2wggg_b1_three_dogs_plurality.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [plurality](../../../../07_Concepts/README.md) · **1 seat** · **Expected winner:** Cat

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/p2wggg) · **[results ↗](https://bettervoting.com/p2wggg/results)** (election `p2wggg` · test `BV2286`).

## Scenario

Race 3 of 7 in the BV2286 "Three dogs and a cat" election (BetterVoting p2wggg), and the point of the whole set. The SAME sixty voters as races 1-2, with the same opinions, face the same question — but the dog side's internal disagreement is now written onto the paper as three breeds. Each voter still gets one mark, so the 34 dog people (57% of the room) spread theirs over three names: Labrador 14, Golden Retriever 12, German Shepherd 8. The 20 cat people are undivided. Cat wins with 20 of 60 marks — 33% — while a 57% majority of the room are dog people. Nobody changed their mind between race 2 and race 3; only the number of names the dog side had did. That is vote splitting, and it is a property of the CANDIDATE LIST, not of the topic and not of how anyone voted. Every other counting rule in this election holds the seat on the dog side. Live results: https://bettervoting.com/p2wggg/results

## Parameters (from the YAML)

```yaml
blocs:
  Dogs: [Labrador, Golden Retriever, German Shepherd]
```

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:Labrador,Golden Retriever,German Shepherd,Cat,Parrot
14:1,0,0,0,0   # dog people who lead with the Labrador
12:0,1,0,0,0   # dog people who lead with the Golden Retriever
8:0,0,1,0,0    # dog people who lead with the German Shepherd
20:0,0,0,1,0   # cat people — undivided
6:0,0,0,0,1    # parrot people
```

## What the engine says

Full report from the [`_tabulated` mirror](../cases_tabulated/bv2286_p2wggg_b1_three_dogs_plurality_tabulated.txt) (regenerated on every run; every analysis forced on):

<!-- --8<-- [start:report] -->
```text
--- Choose-One / Plurality Voting Method (single winner) ---
 Tabulating 60 ballots.

                   Labrador  Golden Retriever  German Shepherd   Cat   Parrot 
  14 ×                X             -                 -           -      -    
  12 ×                -             X                 -           -      -    
  8 ×                 -             -                 X           -      -    
  20 ×                -             -                 -           X      -    
  6 ×                 -             -                 -           -      X    

  Count the marks:  Cat 20 · Labrador 14 · Golden Retriever 12 · German Shepherd 8 · Parrot 6

Winner — Choose-One / Plurality Voting Method (single winner)
 Cat   (20 of 60 marks)
```
<!-- --8<-- [end:report] -->

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/pet_poll_breed_split/cases/bv2286_p2wggg_b1_three_dogs_plurality.yaml
```

## See also

- [Vote splitting (worked set)](../../../split_voting/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [bv2286_p2wggg_a1_one_dog_plurality](bv2286_p2wggg_a1_one_dog_plurality.md) · [bv2286_p2wggg_a2_one_dog_star](bv2286_p2wggg_a2_one_dog_star.md) · [bv2286_p2wggg_b2_three_dogs_irv](bv2286_p2wggg_b2_three_dogs_irv.md) · [bv2286_p2wggg_b3_three_dogs_approval](bv2286_p2wggg_b3_three_dogs_approval.md) · [bv2286_p2wggg_b4_three_dogs_star](bv2286_p2wggg_b4_three_dogs_star.md) · [bv2286_p2wggg_b5_three_dogs_ranked_robin](bv2286_p2wggg_b5_three_dogs_ranked_robin.md)
