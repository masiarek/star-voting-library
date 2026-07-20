# BV2132 — Pet poll (Plurality): the front-runner Dog wins

*Generated from [`bv2132_ykjjhy_pet_plurality.yaml`](../bv2132_ykjjhy_pet_plurality.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [plurality](../../../../00_start_here) · **1 seat** · **Expected winner:** Dog

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/ykjjhy) · **[results ↗](https://bettervoting.com/ykjjhy/results)** (election `ykjjhy`).

## Scenario

One of the four races in the BV2132 "Pet poll" (BetterVoting election ykjjhy). This is the choose-one Plurality race: each voter marks a single top pet. Dog has the most first choices (9 of 22) and wins — even though a 13-voter majority ranks Dog LAST. This is the spoiler/first-past-the-post failure: the consensus candidate Cat (the Condorcet winner) has only 6 first choices and loses. Same electorate as the Approval/STAR races (Cat wins) and the RCV-IRV race (Fish wins). BV also elects Dog. Live results: https://bettervoting.com/ykjjhy/results

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Dog,Cat,Fish
9: 1,0,0
7: 0,0,1
6: 0,1,0
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
--- Choose-One / Plurality Voting Method (single winner) ---

[STAR Voting]
 Tabulating 22 ballots.
Count × Dog,Cat,Fish
    9 ×   1,  0,   0
    7 ×   0,  0,   1
    6 ×   0,  1,   0

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Dog           -- 9 -- First place
   Fish          -- 7 -- Second place
   Cat           -- 6
 Dog and Fish advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Dog           -- 9 -- First place
   Fish          -- 7
   Equal Support -- 6
 Dog wins.
   Runoff math:
     22  ballots cast
   −  6  Equal Support (no preference between the two finalists)
     ──
     16  voters with a preference  (majority = 9)
           Dog 9 (56%)  ·  Fish 7 (44%)

[STAR Voting: Winner — Choose-One / Plurality Voting Method (single winner)]
 Dog
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |   * Dog    |    Cat    |  * Fish   |
-----------------------------------------------------
       * Dog > |    ---     |9 - 7 - 6  |9 - 6 - 7  |
         Cat > | 6 - 7 - 9  |   ---     |6 - 9 - 7  |
      * Fish > | 7 - 6 - 9  |7 - 9 - 6  |   ---     |

[Condorcet Winner]
  Condorcet Winner: Dog — matches the STAR winner

[Score Distribution] (how many ballots gave each star rating)
                   Score
Candidate   5   4   3   2   1   0  | Total   Avg
Dog         0   0   0   0   9  13  |     9   0.4
Cat         0   0   0   0   6  16  |     6   0.3
Fish        0   0   0   0   7  15  |     7   0.3
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/bv2132_ykjjhy_pet_plurality_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/pet_poll_four_methods/cases/bv2132_ykjjhy_pet_plurality.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../00_start_here/topics/condorcet/README.md)
- [Vote splitting (worked set)](../../../split_voting/README.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [bv2132_ykjjhy_pet_approval](bv2132_ykjjhy_pet_approval.md) · [bv2132_ykjjhy_pet_irv](bv2132_ykjjhy_pet_irv.md) · [bv2132_ykjjhy_pet_star](bv2132_ykjjhy_pet_star.md)
