# BV parity — STAR_PR (Allocated Score): fractional surplus reweighting

*Generated from [`BV_Library_star_pr_fractional_surplus.yaml`](../BV_Library_star_pr_fractional_surplus.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Allocated Score (proportional STAR)](../../../00_start_here/proportional_representation) · **2 seats** · **Expected winners:** Allison, Doug

## Scenario

Ported from BetterVoting's tabulator unit tests (AllocatedScore.test.ts :: "Fractional surplus").
Allison has 8 top-level supporters but the Hare quota is only 6, so her surplus is spread
fractionally: each of her supporters' ballots is reweighted to (1 − 6/8) = 0.25 rather than
fully spent. That leftover weight keeps her bloc partly active, but Doug still takes the
second seat. Represents the fractional-surplus family of BetterVoting's AllocatedScore tests
(the "single vote" and "lower split" variants elect the same committee, {Allison, Doug}).
LH's `allocated` method matches BetterVoting.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Allison,Bill,Carmen,Doug
5,5,1,0
5,5,1,0
5,5,1,0
5,5,1,0
5,5,1,0
5,5,1,0
5,5,1,0
5,4,4,0
0,0,0,3
0,0,4,5
0,0,4,5
0,0,4,5
```

## What the engine says

Full report from the [`_tabulated` mirror](../BV_Library_tabulated/BV_Library_star_pr_fractional_surplus_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |  * Allison   |   * Bill    |    Carmen   |     Doug    |
---------------------------------------------------------------------------
     * Allison > |     ---      | 1 - 11 -  0 | 8 -  1 -  3 | 8 -  0 -  4 |
        * Bill > |  0 - 11 -  1 |    ---      | 7 -  2 -  3 | 8 -  0 -  4 |
        Carmen > |  3 -  1 -  8 | 3 -  2 -  7 |    ---      | 8 -  0 -  4 |
          Doug > |  4 -  0 -  8 | 4 -  0 -  8 | 4 -  0 -  8 |    ---      |

[Condorcet Winner]
  Condorcet Winner: Allison — matches the STAR winner

--- Allocated Score Voting Method (2 winners) ---
[Allocated Score Voting]
 Tabulating 12 ballots to fill 2 seats.
Count × Allison,Bill,Carmen,Doug
    7 ×       5,   5,     1,   0
    3 ×       0,   0,     4,   5
    1 ×       5,   4,     4,   0
    1 ×       0,   0,     0,   3

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Allison    8  0  0  0  0  4  |    40   3.3
Bill       7  1  0  0  0  4  |    39   3.3
Carmen     0  4  0  0  7  1  |    23   1.9
Doug       3  0  1  0  0  8  |    18   1.5
 Hare quota is 6.

[Allocated Score Voting: Round 1]
 The highest-scoring candidate wins a seat.
   Allison       -- 40 -- First place
   Bill          -- 39
   Carmen        -- 23
   Doug          -- 18
 Allison wins a seat.

[Allocated Score Voting: Round 1: Ballot allocation round]
 Allocating 6 ballots.

[Allocated Score Voting: Round 1: Ballot allocation round: Round 1]
 Allocating 8 ballots at score 5.
 This allocation overfills the quota.  Returning fractional surplus.
 Allocating only 75.00% of these ballots.
 Keeping these ballots, but multiplying their weights by 1/4.
 8 ballots reweighted from 1 to 1/4.

[Allocated Score Voting: Round 2]
 The highest-scoring candidate wins a seat.
   Doug          -- 18     -- First place
   Carmen        -- 14+3/4
   Bill          --  9+3/4
 Doug wins a seat.

[Allocated Score Voting: Winners — Allocated Score Voting Method (2 winners)]
 Allison
 Doug
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/BV_Library/BV_Library_star_pr_fractional_surplus.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Vote splitting (worked set)](../../split_voting/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [BV_Library_approval_single_winner](BV_Library_approval_single_winner.md) · [BV_Library_plurality_single_winner](BV_Library_plurality_single_winner.md) · [BV_Library_ranked_robin_single_winner](BV_Library_ranked_robin_single_winner.md) · [BV_Library_ranked_robin_ties](BV_Library_ranked_robin_ties.md) · [BV_Library_star_condorcet_winner](BV_Library_star_condorcet_winner.md) · [BV_Library_star_pr_basic_two_seats](BV_Library_star_pr_basic_two_seats.md) · [BV_Library_star_pr_voters_fewer_than_seats](BV_Library_star_pr_voters_fewer_than_seats.md) · [BV_Library_star_runnerup_tie](BV_Library_star_runnerup_tie.md) · [BV_Library_star_runoff](BV_Library_star_runoff.md) · [BV_Library_star_runoff_score_tie_five_star](BV_Library_star_runoff_score_tie_five_star.md) · [BV_Library_star_runoff_tie_score_resolves](BV_Library_star_runoff_tie_score_resolves.md)
