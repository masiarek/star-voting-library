---
search:
  exclude: true
---

# BV2286 — Ballot B (three dogs on the paper): RCV-IRV elects the Golden Retriever

*Generated from [`bv2286_p2wggg_b2_three_dogs_irv.yaml`](../bv2286_p2wggg_b2_three_dogs_irv.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [RCV-IRV (Instant Runoff)](../../../../06_Other/RCV_IRV/concepts/README.md) · **1 seat** · **Expected winner:** Golden Retriever

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/p2wggg) · **[results ↗](https://bettervoting.com/p2wggg/results)** (election `p2wggg` · test `BV2286`).

## Scenario

Race 4 of 7 in the BV2286 "Three dogs and a cat" election (BetterVoting p2wggg). The same sixty voters, ranked. A ranked ballot lets a dog voter say "any dog before the cat", so the three-way split does not hand the seat to the cat the way Choose-One did in race 3 — IRV keeps it on the dog side. It does not, however, find the candidate this electorate most prefers: Parrot goes first, then the German Shepherd, and in round 3 the LABRADOR is eliminated on 14 first choices — one round before it would have won. Its ballots transfer to the Golden Retriever, which takes the final round 34-26 over the Cat. The Labrador beats every rival head-to-head (see the Ranked Robin race), so this is the familiar shape: IRV eliminates on first choices, and a candidate can be everyone's acceptable second while holding too few firsts to survive. Live results: https://bettervoting.com/p2wggg/results

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
--- RCV / Instant-Runoff Voting (single winner) ---
  BV2286 — Ballot B (three dogs on the paper): RCV-IRV elects the Golden Retriever
 Tabulating 60 ballots (ranked ballots).

ROUND 1
Candidate           Votes  Status
----------------  -------  --------
Cat                    20  Hopeful
Labrador               14  Hopeful
Golden Retriever       12  Hopeful
German Shepherd         8  Hopeful
Parrot                  6  Rejected

ROUND 2
Candidate           Votes  Status
----------------  -------  --------
Cat                    26  Hopeful
Labrador               14  Hopeful
Golden Retriever       12  Hopeful
German Shepherd         8  Rejected
Parrot                  0  Rejected

ROUND 3
Candidate           Votes  Status
----------------  -------  --------
Cat                    26  Hopeful
Golden Retriever       20  Hopeful
Labrador               14  Rejected
German Shepherd         0  Rejected
Parrot                  0  Rejected

FINAL RESULT
Candidate           Votes  Status
----------------  -------  --------
Golden Retriever       34  Elected
Cat                    26  Rejected
Labrador                0  Rejected
German Shepherd         0  Rejected
Parrot                  0  Rejected


Winner(s) — RCV / Instant-Runoff Voting (single winner)
  Golden Retriever

--- Transfers and inactive ballots (what the round tables leave out) ---
The tables above give each candidate's round total but not where a
transferred vote came FROM, nor how many ballots stopped counting.
Both are recomputed from the ballots, using the eliminations the
count above actually made.

ROUND 1 — 60 of 60 ballots still active; majority = 31
   Parrot eliminated with 6:
      → Cat                       6

ROUND 2 — 60 of 60 ballots still active; majority = 31
   German Shepherd eliminated with 8:
      → Golden Retriever          8

ROUND 3 — 60 of 60 ballots still active; majority = 31
   Labrador eliminated with 14:
      → Golden Retriever         14

FINAL ROUND — 60 of 60 ballots still active; majority = 31
   Golden Retriever         34  (56.7% of the still-active)  ← elected
   Cat                      26  (43.3% of the still-active)
   Never exhausted, never transferred:
      26 ballots held by Cat carried a lower ranking that was never read
      (the count stopped here, so those preferences did nothing).

Inactive ballots at the final round: 0 of 60 (0.0%).
   Golden Retriever's 34 is a majority of the 60 still active AND of all 60 cast (56.7%).
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Smith Set (the generalized Condorcet winner) ---
The smallest group whose every member beats every candidate outside it —
the honest answer to "who is even in contention?".
   Smith set (1 of 5): Labrador
   Outside (4):        Golden, Retriever, German, Shepherd, Cat, Parrot
   One member ⇒ Labrador is the Condorcet winner, beating every rival head-to-head.
   More: 07_Concepts/topics/smith_set.md
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/bv2286_p2wggg_b2_three_dogs_irv_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/pet_poll_breed_split/cases/bv2286_p2wggg_b2_three_dogs_irv.yaml
```

## See also

- [Vote splitting (worked set)](../../../split_voting/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [bv2286_p2wggg_a1_one_dog_plurality](bv2286_p2wggg_a1_one_dog_plurality.md) · [bv2286_p2wggg_a2_one_dog_star](bv2286_p2wggg_a2_one_dog_star.md) · [bv2286_p2wggg_b1_three_dogs_plurality](bv2286_p2wggg_b1_three_dogs_plurality.md) · [bv2286_p2wggg_b3_three_dogs_approval](bv2286_p2wggg_b3_three_dogs_approval.md) · [bv2286_p2wggg_b4_three_dogs_star](bv2286_p2wggg_b4_three_dogs_star.md) · [bv2286_p2wggg_b5_three_dogs_ranked_robin](bv2286_p2wggg_b5_three_dogs_ranked_robin.md)
