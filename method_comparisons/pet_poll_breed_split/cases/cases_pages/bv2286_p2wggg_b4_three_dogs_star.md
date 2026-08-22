---
search:
  exclude: true
---

# BV2286 — Ballot B (three dogs on the paper): STAR elects the Labrador

*Generated from [`bv2286_p2wggg_b4_three_dogs_star.yaml`](../bv2286_p2wggg_b4_three_dogs_star.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../../01_STAR/01_Learn/README.md) · **1 seat** · **Expected winner:** Labrador

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/p2wggg) · **[results ↗](https://bettervoting.com/p2wggg/results)** (election `p2wggg` · test `BV2286`).

## Scenario

Race 6 of 7 in the BV2286 "Three dogs and a cat" election (BetterVoting p2wggg). The same sixty voters, scoring every candidate 0-5. A dog voter can give all three breeds a high score, so the split that cost the dog side the seat in race 3 never happens: the three dogs take the top three places in the Scoring Round (Labrador 188, Golden Retriever 180, German Shepherd 150) with the Cat fourth on 144. The two leaders advance and the Automatic Runoff goes to the Labrador 34-26, with no Equal Support — every ballot expressed a preference between the two finalists. The Labrador is also the Condorcet winner, beating every rival head-to-head including the Cat 34-26 (confirmed in race 7). Note what the runoff did that the scoring round alone could not: it asked which finalist more voters actually PREFER, rather than which collected the most generous scores. Live results: https://bettervoting.com/p2wggg/results

## Parameters (from the YAML)

```yaml
blocs:
  Dogs: [Labrador, Golden Retriever, German Shepherd]
```

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:Labrador,Golden Retriever,German Shepherd,Cat,Parrot
14:5,4,3,1,0   # Labrador camp — but any dog beats the cat
12:4,5,3,1,0   # Golden camp
8:3,4,5,0,1    # Shepherd camp
20:2,1,1,5,1   # cat people — the Labrador is the tolerable dog
6:1,2,2,3,5    # parrot people
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
[Divergence from STAR]
  STAR                   = Labrador
  Choose-One (Plurality) = Cat   (differs from STAR)
  RCV-IRV                = Golden Retriever   (differs from STAR)
  Note: 26 of 60 ballots (43%) had equal non-zero scores, so their ranks
        were decided by candidate priority order. The RCV-IRV result may be
        an artifact of score-to-rank tie-breaking rather than a deep
        difference.
  Note: Ranked Robin (RCV-RR) agrees with STAR, so RCV-IRV is the lone
        outlier — the classic center-squeeze signature.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: cases_tabulated/bv2286_p2wggg_b4_three_dogs_star_RCV-IRV_tabulated.txt

[Vote-splitting check]
  Choose-One first choices: Cat 20, Labrador 14, Golden Retriever 12, German Shepherd 8, Parrot 6
  Plurality winner: Cat (20, 33.3%)
  Bloc 'Dogs' = Labrador, Golden Retriever, German Shepherd: combined 34 (56.7%); winner Cat is OUTSIDE it.
  => VOTE SPLITTING: the 'Dogs' bloc is an outright majority (34 vs Cat's
     20) but split across 3 candidates, so Cat won Choose-One. STAR elected
     Labrador.

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 60 ballots.
Count × Labrador,Golden Retriever,German Shepherd,Cat,Parrot
   20 ×        2,               1,              1,  5,     1
   14 ×        5,               4,              3,  1,     0
   12 ×        4,               5,              3,  1,     0
    8 ×        3,               4,              5,  0,     1
    6 ×        1,               2,              2,  3,     5

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Labrador         -- 188 -- First place
   Golden Retriever -- 180 -- Second place
   German Shepherd  -- 150
   Cat              -- 144
   Parrot           --  58
 Labrador and Golden Retriever advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Labrador         -- 34 -- First place
   Golden Retriever -- 26
   Equal Support    --  0
 Labrador wins.
   Runoff math:
     60  ballots cast
   −  0  Equal Support (no preference between the two finalists)
     ──
     60  voters with a preference  (majority = 31)
           Labrador 34 (57%)  ·  Golden Retriever 26 (43%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Labrador
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                         |      * Labrador      | * Golden Retriever  |   German Shepherd   |         Cat         |        Parrot       |
-----------------------------------------------------------------------------------------------------------------------------------------
            * Labrador > |         ---          |    34 -  0 - 26     |    46 -  0 - 14     |    34 -  0 - 26     |    54 -  0 -  6     |
    * Golden Retriever > |     26 -  0 - 34     |        ---          |    26 - 26 -  8     |    34 -  0 - 26     |    34 - 20 -  6     |
       German Shepherd > |     14 -  0 - 46     |     8 - 26 - 26     |        ---          |    34 -  0 - 26     |    34 - 20 -  6     |
                   Cat > |     26 -  0 - 34     |    26 -  0 - 34     |    26 -  0 - 34     |        ---          |    46 -  0 - 14     |
                Parrot > |      6 -  0 - 54     |     6 - 20 - 34     |     6 - 20 - 34     |    14 -  0 - 46     |        ---          |

[Condorcet Winner]
  Condorcet Winner: Labrador — matches the STAR winner

[Condorcet Loser]
  Condorcet Loser: Parrot — loses every head-to-head matchup

[Score Distribution] (how many ballots gave each star rating)
                          Score
Candidate          5   4   3   2   1   0  | Total   Avg
Labrador          14  12   8  20   6   0  |   188   3.1
Golden Retriever  12  22   0   6  20   0  |   180   3.0
German Shepherd    8   0  26   6  20   0  |   150   2.5
Cat               20   0   6   0  26   8  |   144   2.4
Parrot             6   0   0   0  28  26  |    58   1.0
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/bv2286_p2wggg_b4_three_dogs_star_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/pet_poll_breed_split/cases/bv2286_p2wggg_b4_three_dogs_star.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../07_Concepts/topics/condorcet/README.md)
- [Vote splitting (worked set)](../../../split_voting/README.md)
- [Runoff reversal (worked set)](../../../../01_STAR/02_Examples/runoff_overturns_leader/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [bv2286_p2wggg_a1_one_dog_plurality](bv2286_p2wggg_a1_one_dog_plurality.md) · [bv2286_p2wggg_a2_one_dog_star](bv2286_p2wggg_a2_one_dog_star.md) · [bv2286_p2wggg_b1_three_dogs_plurality](bv2286_p2wggg_b1_three_dogs_plurality.md) · [bv2286_p2wggg_b2_three_dogs_irv](bv2286_p2wggg_b2_three_dogs_irv.md) · [bv2286_p2wggg_b3_three_dogs_approval](bv2286_p2wggg_b3_three_dogs_approval.md) · [bv2286_p2wggg_b5_three_dogs_ranked_robin](bv2286_p2wggg_b5_three_dogs_ranked_robin.md)
