---
search:
  exclude: true
---

# BV2286 — Ballot B (three dogs on the paper): Ranked Robin confirms the Labrador

*Generated from [`bv2286_p2wggg_b5_three_dogs_ranked_robin.yaml`](../bv2286_p2wggg_b5_three_dogs_ranked_robin.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../../05_Ranked_Robin/01_Learn/README.md) · **1 seat** · **Expected winner:** Labrador

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/p2wggg) · **[results ↗](https://bettervoting.com/p2wggg/results)** (election `p2wggg` · test `BV2286`).

## Scenario

Race 7 of 7 in the BV2286 "Three dogs and a cat" election (BetterVoting p2wggg). The same sixty ranked ballots as race 4, counted head-to-head instead of by elimination. The Labrador wins every one of its four matchups — over the Golden Retriever 34-26, the German Shepherd 46-14, the Cat 34-26 and the Parrot 54-6 — for a 4-0-0 record and an unambiguous Condorcet winner. This race is the answer key for the whole election: it names the candidate this electorate most prefers, with no elimination order and no runoff to argue about. STAR (race 6) finds it; RCV-IRV (race 4) eliminates it in round 3; Choose-One (race 3) elects the Cat, which the Labrador beats head-to-head by the same 34-26. Live results: https://bettervoting.com/p2wggg/results

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
14:Labrador>Golden Retriever>German Shepherd>Cat>Parrot
12:Golden Retriever>Labrador>German Shepherd>Cat>Parrot
8:German Shepherd>Golden Retriever>Labrador>Parrot>Cat
20:Cat>Labrador>Golden Retriever>German Shepherd>Parrot
6:Parrot>Cat>Golden Retriever>German Shepherd>Labrador
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
--- Ranked Robin (RCV-RR / Copeland) Method (single winner) ---
 Tabulating 60 ballots (ranked ballots).

Ballots:
    14 × Labrador > Golden Retriever > German Shepherd > Cat > Parrot
    12 × Golden Retriever > Labrador > German Shepherd > Cat > Parrot
     8 × German Shepherd > Golden Retriever > Labrador > Parrot > Cat
    20 × Cat > Labrador > Golden Retriever > German Shepherd > Parrot
     6 × Parrot > Cat > Golden Retriever > German Shepherd > Labrador

Round-Robin — every pair, head-to-head (For – Against):
   Labrador          beats Golden Retriever   34 – 26
   Labrador          beats German Shepherd    46 – 14
   Labrador          beats Cat                34 – 26
   Labrador          beats Parrot             54 –  6
   Golden Retriever  beats German Shepherd    52 –  8
   Golden Retriever  beats Cat                34 – 26
   Golden Retriever  beats Parrot             54 –  6
   German Shepherd   beats Cat                34 – 26
   German Shepherd   beats Parrot             54 –  6
   Cat               beats Parrot             46 – 14

--- Pairwise (Round-Robin) Matrix ---
Head-to-head / pairwise comparison — the Ranked Robin tally
Legend: For - Equal Support - Against   (row vs column)
                     |      Labrador      | Golden Retriever  | German Shepherd   |       Cat         |      Parrot       |
---------------------------------------------------------------------------------------------------------------------------
          Labrador > |        ---         |   34 -  0 - 26    |   46 -  0 - 14    |   34 -  0 - 26    |   54 -  0 -  6    |
  Golden Retriever > |    26 -  0 - 34    |       ---         |   52 -  0 -  8    |   34 -  0 - 26    |   54 -  0 -  6    |
   German Shepherd > |    14 -  0 - 46    |    8 -  0 - 52    |       ---         |   34 -  0 - 26    |   54 -  0 -  6    |
               Cat > |    26 -  0 - 34    |   26 -  0 - 34    |   26 -  0 - 34    |       ---         |   46 -  0 - 14    |
            Parrot > |     6 -  0 - 54    |    6 -  0 - 54    |    6 -  0 - 54    |   14 -  0 - 46    |       ---         |

Win–loss record — Copeland score = wins + ½·ties (highest score wins; ties broken by the Ranked Robin degrees, then lot order):
    #  Candidate         W–L–T  Copeland  Margin  Beats
    1  Labrador          4–0–0         4     +96  Golden Retriever, German Shepherd, Cat, Parrot
    2  Golden Retriever  3–1–0         3     +92  German Shepherd, Cat, Parrot
    3  German Shepherd   2–2–0         2     -20  Cat, Parrot
    4  Cat               1–3–0         1      +8  Parrot
    5  Parrot            0–4–0         0    -176  —

Winner — Ranked Robin (RCV-RR): Labrador
   beats every opponent head-to-head — the Condorcet winner.
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Smith Set (the generalized Condorcet winner) ---
The smallest group whose every member beats every candidate outside it —
the honest answer to "who is even in contention?".
   Smith set (1 of 5): Labrador
   Outside (4):        Golden Retriever, German Shepherd, Cat, Parrot
   One member ⇒ Labrador is the Condorcet winner, beating every rival head-to-head.
   Ranked Robin (RCV-RR) winner Labrador is INSIDE the Smith set. ✓
      Guaranteed: Ranked Robin (Copeland) is Smith-efficient — every member of
      the set outscores every outsider, so the top of the win–loss table is
      always inside the set, however the tie among them is then broken.
   More: 07_Concepts/topics/smith_set.md
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/bv2286_p2wggg_b5_three_dogs_ranked_robin_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/pet_poll_breed_split/cases/bv2286_p2wggg_b5_three_dogs_ranked_robin.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../07_Concepts/topics/condorcet/README.md)
- [Runoff reversal (worked set)](../../../../01_STAR/02_Examples/runoff_overturns_leader/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [bv2286_p2wggg_a1_one_dog_plurality](bv2286_p2wggg_a1_one_dog_plurality.md) · [bv2286_p2wggg_a2_one_dog_star](bv2286_p2wggg_a2_one_dog_star.md) · [bv2286_p2wggg_b1_three_dogs_plurality](bv2286_p2wggg_b1_three_dogs_plurality.md) · [bv2286_p2wggg_b2_three_dogs_irv](bv2286_p2wggg_b2_three_dogs_irv.md) · [bv2286_p2wggg_b3_three_dogs_approval](bv2286_p2wggg_b3_three_dogs_approval.md) · [bv2286_p2wggg_b4_three_dogs_star](bv2286_p2wggg_b4_three_dogs_star.md)
