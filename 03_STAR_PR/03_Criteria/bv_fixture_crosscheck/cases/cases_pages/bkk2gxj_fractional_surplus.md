---
search:
  exclude: true
---

# BV fixture — fractional surplus

*Generated from [`bkk2gxj_fractional_surplus.yaml`](../bkk2gxj_fractional_surplus.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Allocated Score (proportional STAR)](../../../../01_Learn/README.md) · **2 seats** · **Expected winners:** Allison, Doug

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/kk2gxj) · **[results ↗](https://bettervoting.com/kk2gxj/results)** (election `kk2gxj`).

## Scenario

BetterVoting's own unit-test fixture for Allocated Score ("Fractional surplus" in packages/backend/src/Tabulators/AllocatedScore.test.ts), cast as a real BetterVoting election and re-counted here. Allison has eight top-level supporters but a seat costs only six voters, so the whole quota is drawn from inside her 5-star group and each of those ballots keeps 1 - 6/8 = 0.25 of its weight for the second seat. This is the case that shows fractional surplus doing its job: voters who scored the winner identically are spent identically.

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

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
--- Allocated Score Voting Method (2 winners) ---

[Allocated Score Voting]
 Tabulating 12 ballots to fill 2 seats.
Count × Allison,Bill,Carmen,Doug
    7 ×       5,   5,     1,   0
    3 ×       0,   0,     4,   5
    1 ×       5,   4,     4,   0
    1 ×       0,   0,     0,   3

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
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

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

[Condorcet Loser]
  Condorcet Loser: Doug — loses every head-to-head matchup

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Allison    8  0  0  0  0  4  |    40   3.3
Bill       7  1  0  0  0  4  |    39   3.3
Carmen     0  4  0  0  7  1  |    23   1.9
Doug       3  0  1  0  0  8  |    18   1.5
 Hare quota is 6.
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/bkk2gxj_fractional_surplus_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 03_STAR_PR/03_Criteria/bv_fixture_crosscheck/cases/bkk2gxj_fractional_surplus.yaml
```

## See also

- [Glossary](../../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [bhk27tk_fewer_voters_than_seats](bhk27tk_fewer_voters_than_seats.md)
