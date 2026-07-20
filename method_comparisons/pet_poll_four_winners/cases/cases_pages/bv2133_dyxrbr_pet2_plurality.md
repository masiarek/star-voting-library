# BV2133 — Pet poll II (Plurality): the front-runner Dog wins

*Generated from [`bv2133_dyxrbr_pet2_plurality.yaml`](../bv2133_dyxrbr_pet2_plurality.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [plurality](../../../../00_start_here) · **1 seat** · **Expected winner:** Dog

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/dyxrbr) · **[results ↗](https://bettervoting.com/dyxrbr/results)** (election `dyxrbr`).

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

The count, step by step — the rounds and how the winner is reached:

```text
--- Choose-One / Plurality Voting Method (single winner) ---

[STAR Voting]
 Tabulating 32 ballots.
Count × Dog,Cat,Fish,Bird
   13 ×   1,  0,   0,   0
   10 ×   0,  0,   1,   0
    9 ×   0,  0,   0,   1

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Dog           -- 13 -- First place
   Fish          -- 10 -- Second place
   Bird          --  9
   Cat           --  0
 Dog and Fish advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Dog           -- 13 -- First place
   Fish          -- 10
   Equal Support --  9
 Dog wins.
   Runoff math:
     32  ballots cast
   −  9  Equal Support (no preference between the two finalists)
     ──
     23  voters with a preference  (majority = 12)
           Dog 13 (57%)  ·  Fish 10 (43%)

[STAR Voting: Winner — Choose-One / Plurality Voting Method (single winner)]
 Dog
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |    * Dog     |     Cat     |   * Fish    |     Bird    |
---------------------------------------------------------------------------
         * Dog > |     ---      |13 - 19 -  0 |13 -  9 - 10 |13 - 10 -  9 |
           Cat > |  0 - 19 - 13 |    ---      | 0 - 22 - 10 | 0 - 23 -  9 |
        * Fish > | 10 -  9 - 13 |10 - 22 -  0 |    ---      |10 - 13 -  9 |
          Bird > |  9 - 10 - 13 | 9 - 23 -  0 | 9 - 13 - 10 |    ---      |

[Condorcet Winner]
  Condorcet Winner: Dog — matches the STAR winner

[Score Distribution] (how many ballots gave each star rating)
                   Score
Candidate   5   4   3   2   1   0  | Total   Avg
Dog         0   0   0   0  13  19  |    13   0.4
Cat         0   0   0   0   0  32  |     0   0.0
Fish        0   0   0   0  10  22  |    10   0.3
Bird        0   0   0   0   9  23  |     9   0.3
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/bv2133_dyxrbr_pet2_plurality_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/pet_poll_four_winners/cases/bv2133_dyxrbr_pet2_plurality.yaml
```

## See also

- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [bv2133_dyxrbr_pet2_approval](bv2133_dyxrbr_pet2_approval.md) · [bv2133_dyxrbr_pet2_irv](bv2133_dyxrbr_pet2_irv.md) · [bv2133_dyxrbr_pet2_star](bv2133_dyxrbr_pet2_star.md)
