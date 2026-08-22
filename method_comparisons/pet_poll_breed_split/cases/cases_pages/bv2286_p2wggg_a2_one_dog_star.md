---
search:
  exclude: true
---

# BV2286 — Ballot A (one dog on the paper): STAR agrees, Dog again

*Generated from [`bv2286_p2wggg_a2_one_dog_star.yaml`](../bv2286_p2wggg_a2_one_dog_star.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../../01_STAR/01_Learn/README.md) · **1 seat** · **Expected winner:** Dog

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/p2wggg) · **[results ↗](https://bettervoting.com/p2wggg/results)** (election `p2wggg` · test `BV2286`).

## Scenario

Race 2 of 7 in the BV2286 "Three dogs and a cat" election (BetterVoting p2wggg). The same sixty voters and the same three-name ballot as race 1, scored 0-5. Scoring Round: Dog 222, Cat 144, Parrot 58. Automatic Runoff: Dog 34, Cat 26, no Equal Support. STAR returns the same winner Choose-One did, because with one name per family there is nothing for a richer ballot to rescue. This race is the control: it is what a demo poll looks like when every method agrees and the audience learns nothing about vote splitting. The lesson starts at race 3. Live results: https://bettervoting.com/p2wggg/results

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:Dog,Cat,Parrot
14:5,1,0   # Labrador-first dog people — a dog is a dog on this ballot
12:5,1,0   # Golden-Retriever-first dog people
8:5,0,1    # German-Shepherd-first dog people
20:2,5,1   # cat people — a dog is tolerable, a cat is the point
6:2,3,5    # parrot people
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 60 ballots.
Count × Dog,Cat,Parrot
   26 ×   5,  1,     0
   20 ×   2,  5,     1
    8 ×   5,  0,     1
    6 ×   2,  3,     5

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Dog           -- 222 -- First place
   Cat           -- 144 -- Second place
   Parrot        --  58
 Dog and Cat advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Dog           -- 34 -- First place
   Cat           -- 26
   Equal Support --  0
 Dog wins.
   Runoff math:
     60  ballots cast
   −  0  Equal Support (no preference between the two finalists)
     ──
     60  voters with a preference  (majority = 31)
           Dog 34 (57%)  ·  Cat 26 (43%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Dog
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |    * Dog     |   * Cat     |    Parrot   |
-------------------------------------------------------------
         * Dog > |     ---      |34 -  0 - 26 |54 -  0 -  6 |
         * Cat > | 26 -  0 - 34 |    ---      |46 -  0 - 14 |
        Parrot > |  6 -  0 - 54 |14 -  0 - 46 |    ---      |

[Condorcet Winner]
  Condorcet Winner: Dog — matches the STAR winner

[Condorcet Loser]
  Condorcet Loser: Parrot — loses every head-to-head matchup

[Score Distribution] (how many ballots gave each star rating)
                   Score
Candidate   5   4   3   2   1   0  | Total   Avg
Dog        34   0   0  26   0   0  |   222   3.7
Cat        20   0   6   0  26   8  |   144   2.4
Parrot      6   0   0   0  28  26  |    58   1.0
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/bv2286_p2wggg_a2_one_dog_star_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/pet_poll_breed_split/cases/bv2286_p2wggg_a2_one_dog_star.yaml
```

## See also

- [Vote splitting (worked set)](../../../split_voting/README.md)
- [Runoff reversal (worked set)](../../../../01_STAR/02_Examples/runoff_overturns_leader/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [bv2286_p2wggg_a1_one_dog_plurality](bv2286_p2wggg_a1_one_dog_plurality.md) · [bv2286_p2wggg_b1_three_dogs_plurality](bv2286_p2wggg_b1_three_dogs_plurality.md) · [bv2286_p2wggg_b2_three_dogs_irv](bv2286_p2wggg_b2_three_dogs_irv.md) · [bv2286_p2wggg_b3_three_dogs_approval](bv2286_p2wggg_b3_three_dogs_approval.md) · [bv2286_p2wggg_b4_three_dogs_star](bv2286_p2wggg_b4_three_dogs_star.md) · [bv2286_p2wggg_b5_three_dogs_ranked_robin](bv2286_p2wggg_b5_three_dogs_ranked_robin.md)
