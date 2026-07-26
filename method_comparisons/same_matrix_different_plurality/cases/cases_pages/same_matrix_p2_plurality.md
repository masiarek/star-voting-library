# Same matrix, different plurality — electorate P2: Choose-One

*Generated from [`same_matrix_p2_plurality.yaml`](../same_matrix_p2_plurality.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [plurality](../../../../00_start_here) · **1 seat** · **Expected winner:** Ben

## Scenario

The same electorate P2, voting Choose-One: each voter marks only their first
choice, so the ballot keeps the top of the ranking and discards the rest. Tally:
Ben 5, Cal 4, Ada 3 — winner Ben. The Ranked Robin file on this same electorate
elects Ben, and all three electorates in this folder share one pairwise table
while their plurality winners differ. Plurality's winner is not a function of
the pairwise matrix.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:Ada,Ben,Cal
3:1,0,0
4:0,0,1
5:0,1,0
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR     = Ben
  Approval = Ada   (differs from STAR)

--- Choose-One / Plurality Voting Method (single winner) ---

[STAR Voting]
 Tabulating 12 ballots.
Count × Ada,Ben,Cal
    5 ×   0,  1,  0
    4 ×   0,  0,  1
    3 ×   1,  0,  0

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Ben           -- 5 -- First place
   Cal           -- 4 -- Second place
   Ada           -- 3
 Ben and Cal advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Ben           -- 5 -- First place
   Cal           -- 4
   Equal Support -- 3
 Ben wins.
   Runoff math:
     12  ballots cast
   −  3  Equal Support (no preference between the two finalists)
     ──
      9  voters with a preference  (majority = 5)
           Ben 5 (56%)  ·  Cal 4 (44%)

[STAR Voting: Winner — Choose-One / Plurality Voting Method (single winner)]
 Ben
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |     Ada    |  * Ben    |  * Cal    |
-----------------------------------------------------
         Ada > |    ---     |3 - 4 - 5  |3 - 5 - 4  |
       * Ben > | 5 - 4 - 3  |   ---     |5 - 3 - 4  |
       * Cal > | 4 - 5 - 3  |4 - 3 - 5  |   ---     |

[Condorcet Winner]
  Condorcet Winner: Ben — matches the STAR winner

[Condorcet Loser]
  Condorcet Loser: Ada — loses every head-to-head matchup — elected by Approval!

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Ada        0  0  0  0  3  9  |     3   0.3
Ben        0  0  0  0  5  7  |     5   0.4
Cal        0  0  0  0  4  8  |     4   0.3
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/same_matrix_p2_plurality_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/same_matrix_different_plurality/cases/same_matrix_p2_plurality.yaml
```

## See also

- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [same_matrix_p1_plurality](same_matrix_p1_plurality.md) · [same_matrix_p1_ranked_robin](same_matrix_p1_ranked_robin.md) · [same_matrix_p2_ranked_robin](same_matrix_p2_ranked_robin.md) · [same_matrix_p3_plurality](same_matrix_p3_plurality.md) · [same_matrix_p3_ranked_robin](same_matrix_p3_ranked_robin.md)
