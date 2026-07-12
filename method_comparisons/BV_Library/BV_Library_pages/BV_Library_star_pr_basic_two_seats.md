# BV parity — STAR_PR (Allocated Score): basic two-seat allocation

*Generated from [`BV_Library_star_pr_basic_two_seats.yaml`](../BV_Library_star_pr_basic_two_seats.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Allocated Score (proportional STAR)](../../../00_start_here/proportional_representation) · **2 seats** · **Expected winners:** Allison, Doug

## Scenario

Ported from BetterVoting's tabulator unit tests (AllocatedScore.test.ts :: "Basic Example").
Two seats, two main blocs. Allison wins the first seat with the highest score (25); one
Hare quota of her supporters is then spent, dropping Bill's remaining weight to zero and
reducing Carmen's, which lets Doug win the second seat.

This is the core Allocated Score mechanic: elect the top scorer, then allocate up to a
quota of the ballots that supported them before the next round. LH's `allocated` method
reproduces BetterVoting's committee {Allison, Doug}.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Allison,Bill,Carmen,Doug
5,5,1,0
5,5,1,0
5,5,1,0
5,5,1,0
5,4,4,0
0,0,0,3
0,0,4,5
0,0,4,5
0,0,4,5
0,0,4,5
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
--- Allocated Score Voting Method (2 winners) ---

[Allocated Score Voting]
 Tabulating 10 ballots to fill 2 seats.
Count × Allison,Bill,Carmen,Doug
    4 ×       5,   5,     1,   0
    4 ×       0,   0,     4,   5
    1 ×       5,   4,     4,   0
    1 ×       0,   0,     0,   3

[Allocated Score Voting: Round 1]
 The highest-scoring candidate wins a seat.
   Allison       -- 25 -- First place
   Bill          -- 24
   Carmen        -- 24
   Doug          -- 23
 Allison wins a seat.

[Allocated Score Voting: Round 1: Ballot allocation round]
 Allocating 5 ballots.

[Allocated Score Voting: Round 1: Ballot allocation round: Round 1]
 Allocating 5 ballots at score 5.

[Allocated Score Voting: Round 2]
 Tabulating 5 remaining ballots.
Count × Allison,Bill,Carmen,Doug
    4 ×       5,   5,     1,   0
    4 ×       0,   0,     4,   5
    1 ×       5,   4,     4,   0
    1 ×       0,   0,     0,   3

[Allocated Score Voting: Winners — Allocated Score Voting Method (2 winners)]
 Allison
 Doug
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
    * Allison > |     ---     | 1 - 9 - 0  | 5 - 1 - 4  | 5 - 0 - 5  |
       * Bill > |  0 - 9 - 1  |    ---     | 4 - 2 - 4  | 5 - 0 - 5  |
       Carmen > |  4 - 1 - 5  | 4 - 2 - 4  |    ---     | 5 - 0 - 5  |
         Doug > |  5 - 0 - 5  | 5 - 0 - 5  | 5 - 0 - 5  |    ---     |

[Condorcet Winner]
  No strict Condorcet winner; unbeaten candidates: Allison, Doug (pairwise ties)

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Allison    5  0  0  0  0  5  |    25   2.5
Bill       4  1  0  0  0  5  |    24   2.4
Carmen     0  5  0  0  4  1  |    24   2.4
Doug       4  0  1  0  0  5  |    23   2.3
 Hare quota is 5.

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Allison    5  0  0  0  0  5  |    25   2.5
Bill       4  1  0  0  0  5  |    24   2.4
Carmen     0  5  0  0  4  1  |    24   2.4
Doug       4  0  1  0  0  5  |    23   2.3
 The highest-scoring candidate wins a seat.
   Doug          -- 23 -- First place
   Carmen        -- 16
   Bill          --  0
 Doug wins a seat.
```

</details>

Everything in one file: the [`_tabulated` mirror](../BV_Library_tabulated/BV_Library_star_pr_basic_two_seats_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/BV_Library/BV_Library_star_pr_basic_two_seats.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [BV_Library_approval_single_winner](BV_Library_approval_single_winner.md) · [BV_Library_plurality_single_winner](BV_Library_plurality_single_winner.md) · [BV_Library_ranked_robin_single_winner](BV_Library_ranked_robin_single_winner.md) · [BV_Library_ranked_robin_ties](BV_Library_ranked_robin_ties.md) · [BV_Library_star_condorcet_winner](BV_Library_star_condorcet_winner.md) · [BV_Library_star_pr_fractional_surplus](BV_Library_star_pr_fractional_surplus.md) · [BV_Library_star_pr_voters_fewer_than_seats](BV_Library_star_pr_voters_fewer_than_seats.md) · [BV_Library_star_runnerup_tie](BV_Library_star_runnerup_tie.md) · [BV_Library_star_runoff](BV_Library_star_runoff.md) · [BV_Library_star_runoff_score_tie_five_star](BV_Library_star_runoff_score_tie_five_star.md) · [BV_Library_star_runoff_tie_score_resolves](BV_Library_star_runoff_tie_score_resolves.md)
