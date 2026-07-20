# BV parity — STAR_PR (Allocated Score): fewer voters than seats

*Generated from [`BV_Library_star_pr_voters_fewer_than_seats.yaml`](../BV_Library_star_pr_voters_fewer_than_seats.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Allocated Score (proportional STAR)](../../../../00_start_here/proportional_representation) · **3 seats** · **Expected winners:** Allison, Bill, Carmen

## Scenario

Ported from BetterVoting's tabulator unit tests (AllocatedScore.test.ts :: "Voters < Winners").
A degenerate but important edge case: 3 seats but only 2 ballots. The method still fills
every seat, electing in score order — Allison, then Bill, then Carmen — rather than erroring
or leaving seats empty. LH's `allocated` method agrees with BetterVoting.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Allison,Bill,Carmen,Doug
5,5,0,0
5,4,3,0
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
--- Allocated Score Voting Method (3 winners) ---

[Allocated Score Voting]
 Tabulating 2 ballots to fill 3 seats.
Allison,Bill,Carmen,Doug
      5,   5,     0,   0
      5,   4,     3,   0

[Allocated Score Voting: Round 1]
 The highest-scoring candidate wins a seat.
   Allison       -- 10 -- First place
   Bill          --  9
   Carmen        --  3
   Doug          --  0
 Allison wins a seat.

[Allocated Score Voting: Round 1: Ballot allocation round]
 Allocating 2/3 ballots.

[Allocated Score Voting: Round 1: Ballot allocation round: Round 1]
 Allocating 2 ballots at score 5.
 This allocation overfills the quota.  Returning fractional surplus.
 Allocating only 33.33% of these ballots.
 Keeping these ballots, but multiplying their weights by 2/3.
 2 ballots reweighted from 1 to 2/3.

[Allocated Score Voting: Round 2]
 The highest-scoring candidate wins a seat.
   Bill          -- 6 -- First place
   Carmen        -- 2
   Doug          -- 0
 Bill wins a seat.

[Allocated Score Voting: Round 2: Ballot allocation round]
 Allocating 2/3 ballots.

[Allocated Score Voting: Round 2: Ballot allocation round: Round 1]
 Allocating 1 ballot at score 10/3.
 This allocation overfills the quota.  Returning fractional surplus.
 Allocating only 66.67% of this ballot.
 Keeping this ballot, but multiplying its weight by 1/3.
 1 ballot reweighted from 2/3 to 2/9.

[Allocated Score Voting: Round 3]
 The highest-scoring candidate wins a seat.
   Carmen        -- 2 -- First place
   Doug          -- 0
 Carmen wins a seat.

[Allocated Score Voting: Winners — Allocated Score Voting Method (3 winners)]
 Allison
 Bill
 Carmen
```

<details>
<summary>Full audit — preference matrix, Condorcet, and score distribution</summary>

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                |  * Allison  |  * Bill    |   Carmen   |    Doug    |
----------------------------------------------------------------------
    * Allison > |     ---     | 1 - 1 - 0  | 2 - 0 - 0  | 2 - 0 - 0  |
       * Bill > |  0 - 1 - 1  |    ---     | 2 - 0 - 0  | 2 - 0 - 0  |
       Carmen > |  0 - 0 - 2  | 0 - 0 - 2  |    ---     | 1 - 1 - 0  |
         Doug > |  0 - 0 - 2  | 0 - 0 - 2  | 0 - 1 - 1  |    ---     |

[Condorcet Winner]
  Condorcet Winner: Allison — matches the STAR winner

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Allison    2  0  0  0  0  0  |    10   5.0
Bill       1  1  0  0  0  0  |     9   4.5
Carmen     0  0  1  0  0  1  |     3   1.5
Doug       0  0  0  0  0  2  |     0   0.0
 Hare quota is 2/3.
```

</details>

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/BV_Library_star_pr_voters_fewer_than_seats_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/BV_Library/cases/BV_Library_star_pr_voters_fewer_than_seats.yaml
```

## See also

- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [BV_Library_approval_single_winner](BV_Library_approval_single_winner.md) · [BV_Library_plurality_single_winner](BV_Library_plurality_single_winner.md) · [BV_Library_ranked_robin_single_winner](BV_Library_ranked_robin_single_winner.md) · [BV_Library_ranked_robin_ties](BV_Library_ranked_robin_ties.md) · [BV_Library_star_condorcet_winner](BV_Library_star_condorcet_winner.md) · [BV_Library_star_pr_basic_two_seats](BV_Library_star_pr_basic_two_seats.md) · [BV_Library_star_pr_fractional_surplus](BV_Library_star_pr_fractional_surplus.md) · [BV_Library_star_runnerup_tie](BV_Library_star_runnerup_tie.md) · [BV_Library_star_runoff](BV_Library_star_runoff.md) · [BV_Library_star_runoff_score_tie_five_star](BV_Library_star_runoff_score_tie_five_star.md) · [BV_Library_star_runoff_tie_score_resolves](BV_Library_star_runoff_tie_score_resolves.md)
