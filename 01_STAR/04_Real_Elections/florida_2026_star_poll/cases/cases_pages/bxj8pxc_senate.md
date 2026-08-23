---
search:
  exclude: true
---

# FL 2026 poll — 2026 U.S. Senate special election

*Generated from [`bxj8pxc_senate.yaml`](../bxj8pxc_senate.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../../01_Learn/README.md) · **1 seat** · **Expected winner:** Nixon (DEM)

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/xj8pxc) · **[results ↗](https://bettervoting.com/xj8pxc/results)** (election `xj8pxc`).

## Scenario

**2026 U.S. Senate special election** — the seven-way U.S. Senate special-election field — the race the poll was built around. Two Democrats take both runoff slots, and **15 of the 22 tallied ballots score them equally**, so the runoff is decided by 7 voters out of 25 ballots cast.

Scoring round: Nixon (DEM) 57 · Vindman (DEM) 47 · Moody (REP)* 37 · Gillespie (NPA) 23 · Rivera (REP) 16 · Gleason (REP) 8 · Perry (REP) 7.
Automatic Runoff: Nixon (DEM) 6 vs Vindman (DEM) 1, with 15 of the
22 tallied ballots showing Equal Support for both finalists.

25 ballots were cast in the poll; 3 left this race blank (22 tallied).
Markers: `&` = the BetterVoting `null` (candidate left unscored) — it tabulates as 0,
and a ballot that is `&` all the way across is an abstention in this race.
Party tags are the candidates' own ballot labels; `*` marks the incumbent.

Frozen from the live poll on 2026-08-22 (the poll stays open to 2026-11-11, so the
live page will keep moving — this file is the snapshot LH is checked against).

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

Markers on these ballots: `-` blank · `~` race abstention · `&` candidate abstention · `?` spoiled · `%` spoiled+reissued — all tabulate as 0 (reported honestly).

```text
Moody (REP)*,Nixon (DEM),Vindman (DEM),Gillespie (NPA),Gleason (REP),Perry (REP),Rivera (REP)
&,&,&,5,&,&,&   # b-d67ygqqb
&,&,&,&,&,&,&   # b-7qr6fp6d
&,5,&,&,&,&,&   # b-dh7xj93b
&,5,5,&,&,&,&   # b-qkyw76rq
5,&,&,&,&,&,&   # b-cqcfrhgf
&,&,&,&,&,&,&   # b-6mwmcfmd
&,&,&,&,&,&,5   # b-8kq29hv8
0,5,5,4,0,0,0   # b-xfftm9yb
0,5,5,3,0,0,0   # b-gyvqdrry
0,0,0,0,0,0,0   # b-6ywyq88y
&,5,3,0,0,0,0   # b-9v7q4dvt
0,4,4,1,0,0,0   # b-6c2y3d3p
5,&,&,&,&,&,&   # b-3xdd4ptb
0,5,0,0,0,0,0   # b-9ry7jmwv
5,0,0,0,0,0,0   # b-rqd88v3w
0,5,4,1,0,0,0   # b-bk8xd8fw
0,5,5,4,1,1,1   # b-8bfw9dyf
0,&,5,&,&,&,&   # b-gffckf36
5,0,0,0,0,0,5   # b-6hfy233k
5,&,&,&,&,&,&   # b-ypm6vddm
5,&,&,&,&,&,&   # b-pfvxtxmh
2,5,4,3,2,1,0   # b-fhgbkw3x
0,5,4,1,0,0,0   # b-mybbty26
0,3,3,1,0,0,0   # b-xc3yfg8c
5,0,0,0,5,5,5   # b-vjpmvx6c
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 25 ballots. Note: 2 of 25 ballots are marked as abstentions.
Count × Moody (REP)*,Nixon (DEM),Vindman (DEM),Gillespie (NPA),Gleason (REP),Perry (REP),Rivera (REP)
    4 ×            5,          &,            &,              &,            &,          &,           &
    2 ×            &,          &,            &,              &,            &,          &,           &
    2 ×            0,          5,            4,              1,            0,          0,           0
    1 ×            &,          &,            &,              5,            &,          &,           &
    1 ×            &,          5,            &,              &,            &,          &,           &
    1 ×            &,          5,            5,              &,            &,          &,           &
    1 ×            &,          &,            &,              &,            &,          &,           5
    1 ×            0,          5,            5,              4,            0,          0,           0
    1 ×            0,          5,            5,              3,            0,          0,           0
    1 ×            0,          0,            0,              0,            0,          0,           0
    1 ×            &,          5,            3,              0,            0,          0,           0
    1 ×            0,          4,            4,              1,            0,          0,           0
    1 ×            0,          5,            0,              0,            0,          0,           0
    1 ×            5,          0,            0,              0,            0,          0,           0
    1 ×            0,          5,            5,              4,            1,          1,           1
    1 ×            0,          &,            5,              &,            &,          &,           &
    1 ×            5,          0,            0,              0,            0,          0,           5
    1 ×            2,          5,            4,              3,            2,          1,           0
    1 ×            0,          3,            3,              1,            0,          0,           0
    1 ×            5,          0,            0,              0,            5,          5,           5

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Nixon (DEM)     -- 57 -- First place
   Vindman (DEM)   -- 47 -- Second place
   Moody (REP)*    -- 37
   Gillespie (NPA) -- 23
   Rivera (REP)    -- 16
   Gleason (REP)   --  8
   Perry (REP)     --  7
 Nixon (DEM) and Vindman (DEM) advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Nixon (DEM)     -- 6 -- First place
   Vindman (DEM)   -- 1
   Equal Support   -- 18
 Nixon (DEM) wins.
   Runoff math:
     25  ballots cast
   − 18  Equal Support (no preference between the two finalists)
     ──
      7  voters with a preference  (majority = 4)
           Nixon (DEM) 6 (86%)  ·  Vindman (DEM) 1 (14%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Nixon (DEM)
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                        |     Moody (REP)*    |   * Nixon (DEM)    |  * Vindman (DEM)   |   Gillespie (NPA)  |    Gleason (REP)   |     Perry (REP)    |    Rivera (REP)    |
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
         Moody (REP)* > |         ---         |    7 -  6 - 12     |    7 -  7 - 11     |    7 -  9 -  9     |    6 - 18 -  1     |    7 - 17 -  1     |    6 - 17 -  2     |
        * Nixon (DEM) > |    12 -  6 -  7     |        ---         |    6 - 18 -  1     |   12 - 12 -  1     |   12 - 12 -  1     |   12 - 12 -  1     |   12 - 10 -  3     |
      * Vindman (DEM) > |    11 -  7 -  7     |    1 - 18 -  6     |        ---         |   11 - 13 -  1     |   11 - 13 -  1     |   11 - 13 -  1     |   11 - 11 -  3     |
      Gillespie (NPA) > |     9 -  9 -  7     |    1 - 12 - 12     |    1 - 13 - 11     |        ---         |    9 - 15 -  1     |    9 - 15 -  1     |    9 - 13 -  3     |
        Gleason (REP) > |     1 - 18 -  6     |    1 - 12 - 12     |    1 - 13 - 11     |    1 - 15 -  9     |        ---         |    1 - 24 -  0     |    1 - 22 -  2     |
          Perry (REP) > |     1 - 17 -  7     |    1 - 12 - 12     |    1 - 13 - 11     |    1 - 15 -  9     |    0 - 24 -  1     |        ---         |    1 - 22 -  2     |
         Rivera (REP) > |     2 - 17 -  6     |    3 - 10 - 12     |    3 - 11 - 11     |    3 - 13 -  9     |    2 - 22 -  1     |    2 - 22 -  1     |        ---         |

[Condorcet Winner]
  Condorcet Winner: Nixon (DEM) — matches the STAR winner

[Condorcet Loser]
  Condorcet Loser: Perry (REP) — loses every head-to-head matchup

[Score Distribution] (how many ballots gave each star rating)
                         Score
Candidate         5   4   3   2   1   0  Abs  | Total  Avg all  Avg rated
Moody (REP)*      7   0   0   1   0  10    7  |    37      1.5        2.1
Nixon (DEM)      10   1   1   0   0   4    9  |    57      2.3        3.6
Vindman (DEM)     5   4   2   0   0   5    9  |    47      1.9        2.9
Gillespie (NPA)   1   2   2   0   4   6   10  |    23      0.9        1.5
Gleason (REP)     1   0   0   1   1  11   11  |     8      0.3        0.6
Perry (REP)       1   0   0   0   2  11   11  |     7      0.3        0.5
Rivera (REP)      3   0   0   0   1  11   10  |    16      0.6        1.1
  Avg all   = Total / all ballots — a blank counts as 0, so this is the Total the Scoring Round ranks on, per ballot.
  Avg rated = Total / the ballots that scored this candidate (Abs excluded) — support among voters who had an opinion.
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/bxj8pxc_senate_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/04_Real_Elections/florida_2026_star_poll/cases/bxj8pxc_senate.yaml
```

## See also

- [Runoff reversal (worked set)](../../../../02_Examples/runoff_overturns_leader/README.md)
- [Ballot & terminology basics](../../../../../07_Concepts/topics/ballot_and_terminology_basics.md)
- [Glossary](../../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [bxj8pxc_agriculture](bxj8pxc_agriculture.md) · [bxj8pxc_attorney_general](bxj8pxc_attorney_general.md) · [bxj8pxc_cfo](bxj8pxc_cfo.md)
