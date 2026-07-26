# Same matrix, different plurality — electorate P1: Choose-One

*Generated from [`same_matrix_p1_plurality.yaml`](../same_matrix_p1_plurality.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [plurality](../../../../00_start_here) · **1 seat** · **Expected winner:** Ada

## Scenario

The same electorate P1, voting Choose-One: each voter marks only their first
choice, so the ballot keeps the top of the ranking and discards the rest. Tally:
Ada 5, Cal 4, Ben 3 — winner Ada. The Ranked Robin file on this same electorate
elects Ben, and all three electorates in this folder share one pairwise table
while their plurality winners differ. Plurality's winner is not a function of
the pairwise matrix.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:Ada,Ben,Cal
4:1,0,0
1:1,0,0
4:0,0,1
3:0,1,0
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
--- Choose-One / Plurality Voting Method (single winner) ---

[STAR Voting]
 Tabulating 12 ballots.
Count × Ada,Ben,Cal
    5 ×   1,  0,  0
    4 ×   0,  0,  1
    3 ×   0,  1,  0

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Ada           -- 5 -- First place
   Cal           -- 4 -- Second place
   Ben           -- 3
 Ada and Cal advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Ada           -- 5 -- First place
   Cal           -- 4
   Equal Support -- 3
 Ada wins.
   Runoff math:
     12  ballots cast
   −  3  Equal Support (no preference between the two finalists)
     ──
      9  voters with a preference  (majority = 5)
           Ada 5 (56%)  ·  Cal 4 (44%)

[STAR Voting: Winner — Choose-One / Plurality Voting Method (single winner)]
 Ada
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |   * Ada    |    Ben    |  * Cal    |
-----------------------------------------------------
       * Ada > |    ---     |5 - 4 - 3  |5 - 3 - 4  |
         Ben > | 3 - 4 - 5  |   ---     |3 - 5 - 4  |
       * Cal > | 4 - 3 - 5  |4 - 5 - 3  |   ---     |

[Condorcet Winner]
  Condorcet Winner: Ada — matches the STAR winner

[Condorcet Loser]
  Condorcet Loser: Ben — loses every head-to-head matchup

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Ada        0  0  0  0  5  7  |     5   0.4
Ben        0  0  0  0  3  9  |     3   0.3
Cal        0  0  0  0  4  8  |     4   0.3
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/same_matrix_p1_plurality_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/same_matrix_different_plurality/cases/same_matrix_p1_plurality.yaml
```

## See also

- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [same_matrix_p1_ranked_robin](same_matrix_p1_ranked_robin.md) · [same_matrix_p2_plurality](same_matrix_p2_plurality.md) · [same_matrix_p2_ranked_robin](same_matrix_p2_ranked_robin.md) · [same_matrix_p3_plurality](same_matrix_p3_plurality.md) · [same_matrix_p3_ranked_robin](same_matrix_p3_ranked_robin.md)
