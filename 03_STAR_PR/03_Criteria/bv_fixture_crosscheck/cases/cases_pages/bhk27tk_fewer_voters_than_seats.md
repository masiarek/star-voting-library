---
search:
  exclude: true
---

# BV fixture — fewer voters than seats

*Generated from [`bhk27tk_fewer_voters_than_seats.yaml`](../bhk27tk_fewer_voters_than_seats.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Allocated Score (proportional STAR)](../../../../01_Learn/README.md) · **3 seats** · **Expected winners:** Allison, Bill, Carmen

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/hk27tk) · **[results ↗](https://bettervoting.com/hk27tk/results)** (election `hk27tk`).

## Scenario

BetterVoting's own unit-test fixture for Allocated Score ("Voters < Winners" in packages/backend/src/Tabulators/AllocatedScore.test.ts), cast as a real BetterVoting election and re-counted here. Two voters, three seats: a degenerate election that exists to prove the tabulator does something sane when the quota is smaller than a single ballot rather than dividing by zero or looping. Both engines seat Allison, Bill and Carmen.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Allison,Bill,Carmen,Doug
5,5,0,0
5,4,3,0
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
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
 These ballots carry a remaining weight of 2/3.

[Allocated Score Voting: Round 3]
 Tabulating 1 remaining ballots.
Allison,Bill,Carmen,Doug
      5,   5,     0,   0
      5,   4,     3,   0

[Allocated Score Voting: Winners — Allocated Score Voting Method (3 winners)]
 Allison
 Bill
 Carmen
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Preference Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        Informational only — not part of the 3-winner count below,
        so no Top-2 finalists are marked.
                |    Allison  |    Bill    |   Carmen   |    Doug    |
----------------------------------------------------------------------
      Allison > |     ---     | 1 - 1 - 0  | 2 - 0 - 0  | 2 - 0 - 0  |
         Bill > |  0 - 1 - 1  |    ---     | 2 - 0 - 0  | 2 - 0 - 0  |
       Carmen > |  0 - 0 - 2  | 0 - 0 - 2  |    ---     | 1 - 1 - 0  |
         Doug > |  0 - 0 - 2  | 0 - 0 - 2  | 0 - 1 - 1  |    ---     |

[Condorcet Winner]
  Condorcet Winner: Allison — matches the STAR winner

[Condorcet Loser]
  Condorcet Loser: Doug — loses every head-to-head matchup

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Allison    2  0  0  0  0  0  |    10   5.0
Bill       1  1  0  0  0  0  |     9   4.5
Carmen     0  0  1  0  0  1  |     3   1.5
Doug       0  0  0  0  0  2  |     0   0.0
 Hare quota is 2/3.

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Allison    2  0  0  0  0  0  |    10   5.0
Bill       1  1  0  0  0  0  |     9   4.5
Carmen     0  0  1  0  0  1  |     3   1.5
Doug       0  0  0  0  0  2  |     0   0.0
 The highest-scoring candidate wins a seat.
   Carmen        -- 2 -- First place
   Doug          -- 0
 Carmen wins a seat.
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/bhk27tk_fewer_voters_than_seats_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 03_STAR_PR/03_Criteria/bv_fixture_crosscheck/cases/bhk27tk_fewer_voters_than_seats.yaml
```

## See also

- [Glossary](../../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [bkk2gxj_fractional_surplus](bkk2gxj_fractional_surplus.md)
