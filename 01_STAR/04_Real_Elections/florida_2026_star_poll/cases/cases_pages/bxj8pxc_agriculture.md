---
search:
  exclude: true
---

# FL 2026 poll — 2026 FL Commissioner of Agriculture and Consumer Services

*Generated from [`bxj8pxc_agriculture.yaml`](../bxj8pxc_agriculture.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../../01_Learn/README.md) · **1 seat** · **Expected winner:** Matt The Welder (REP)

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/xj8pxc) · **[results ↗](https://bettervoting.com/xj8pxc/results)** (election `xj8pxc`).

## Scenario

**2026 FL Commissioner of Agriculture and Consumer Services** — the one race a Republican wins, and by the widest margin in the poll: **Matt The Welder** leads the scoring round 79-39 and takes the runoff 15-8. It is also the only race every one of the 25 ballots voted in.

Scoring round: Matt The Welder (REP) 79 · Romagnano (DEM) 39 · Simpson (REP)* 23 · Gibson (NPA) 20 · Olle Jr (REP) 7.
Automatic Runoff: Matt The Welder (REP) 15 vs Romagnano (DEM) 8, with 2 of the
25 tallied ballots showing Equal Support for both finalists.

25 ballots were cast in the poll; 0 left this race blank (25 tallied).
Markers: `&` = the BetterVoting `null` (candidate left unscored) — it tabulates as 0,
and a ballot that is `&` all the way across is an abstention in this race.
Party tags are the candidates' own ballot labels; `*` marks the incumbent.

Frozen from the live poll on 2026-08-22 (the poll stays open to 2026-11-11, so the
live page will keep moving — this file is the snapshot LH is checked against).

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

Markers on these ballots: `-` blank · `~` race abstention · `&` candidate abstention · `?` spoiled · `%` spoiled+reissued — all tabulate as 0 (reported honestly).

```text
Romagnano (DEM),Gibson (NPA),Olle Jr (REP),Simpson (REP)*,Matt The Welder (REP)
&,&,&,&,5   # b-d67ygqqb
1,1,1,0,5   # b-7qr6fp6d
&,&,&,&,5   # b-dh7xj93b
&,&,&,&,5   # b-qkyw76rq
&,&,&,&,5   # b-cqcfrhgf
&,&,&,&,5   # b-6mwmcfmd
&,&,&,&,5   # b-8kq29hv8
5,4,0,0,0   # b-xfftm9yb
5,3,0,0,0   # b-gyvqdrry
0,0,0,0,5   # b-6ywyq88y
0,0,0,0,5   # b-9v7q4dvt
5,1,0,0,0   # b-6c2y3d3p
&,&,&,5,&   # b-3xdd4ptb
0,0,0,4,5   # b-9ry7jmwv
0,0,0,5,0   # b-rqd88v3w
4,1,0,&,0   # b-bk8xd8fw
5,4,1,1,0   # b-8bfw9dyf
&,&,&,0,5   # b-gffckf36
0,0,0,0,5   # b-6hfy233k
&,&,&,&,5   # b-ypm6vddm
&,&,&,&,5   # b-pfvxtxmh
5,4,0,3,4   # b-fhgbkw3x
5,1,0,0,0   # b-mybbty26
4,1,0,0,0   # b-xc3yfg8c
0,0,5,5,5   # b-vjpmvx6c
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 25 ballots.
Count × Romagnano (DEM),Gibson (NPA),Olle Jr (REP),Simpson (REP)*,Matt The Welder (REP)
    8 ×               &,           &,            &,             &,                    5
    3 ×               0,           0,            0,             0,                    5
    2 ×               5,           1,            0,             0,                    0
    1 ×               1,           1,            1,             0,                    5
    1 ×               5,           4,            0,             0,                    0
    1 ×               5,           3,            0,             0,                    0
    1 ×               &,           &,            &,             5,                    &
    1 ×               0,           0,            0,             4,                    5
    1 ×               0,           0,            0,             5,                    0
    1 ×               4,           1,            0,             &,                    0
    1 ×               5,           4,            1,             1,                    0
    1 ×               &,           &,            &,             0,                    5
    1 ×               5,           4,            0,             3,                    4
    1 ×               4,           1,            0,             0,                    0
    1 ×               0,           0,            5,             5,                    5

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Matt The Welder (REP) -- 79 -- First place
   Romagnano (DEM)       -- 39 -- Second place
   Simpson (REP)*        -- 23
   Gibson (NPA)          -- 20
   Olle Jr (REP)         --  7
 Matt The Welder (REP) and Romagnano (DEM) advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Matt The Welder (REP) -- 15 -- First place
   Romagnano (DEM)       --  8
   Equal Support         --  2
 Matt The Welder (REP) wins.
   Runoff math:
     25  ballots cast
   −  2  Equal Support (no preference between the two finalists)
     ──
     23  voters with a preference  (majority = 12)
           Matt The Welder (REP) 15 (65%)  ·  Romagnano (DEM) 8 (35%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Matt The Welder (REP)
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                              |     * Romagnano (DEM)     |       Gibson (NPA)       |       Olle Jr (REP)      |      Simpson (REP)*      | * Matt The Welder (REP)  |
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
          * Romagnano (DEM) > |            ---            |       8 - 17 -  0        |       8 - 16 -  1        |       9 - 12 -  4        |       8 -  2 - 15        |
               Gibson (NPA) > |        0 - 17 -  8        |           ---            |       8 - 16 -  1        |       9 - 12 -  4        |       7 -  3 - 15        |
              Olle Jr (REP) > |        1 - 16 -  8        |       1 - 16 -  8        |           ---            |       1 - 20 -  4        |       1 -  9 - 15        |
             Simpson (REP)* > |        4 - 12 -  9        |       4 - 12 -  9        |       4 - 20 -  1        |           ---            |       3 -  7 - 15        |
    * Matt The Welder (REP) > |       15 -  2 -  8        |      15 -  3 -  7        |      15 -  9 -  1        |      15 -  7 -  3        |           ---            |

[Condorcet Winner]
  Condorcet Winner: Matt The Welder (REP) — matches the STAR winner

[Condorcet Loser]
  Condorcet Loser: Olle Jr (REP) — loses every head-to-head matchup

[Score Distribution] (how many ballots gave each star rating)
                               Score
Candidate               5   4   3   2   1   0  Abs  | Total  Avg all  Avg rated
Romagnano (DEM)         6   2   0   0   1   6   10  |    39      1.6        2.6
Gibson (NPA)            0   3   1   0   5   6   10  |    20      0.8        1.3
Olle Jr (REP)           1   0   0   0   2  12   10  |     7      0.3        0.5
Simpson (REP)*          3   1   1   0   1  10    9  |    23      0.9        1.4
Matt The Welder (REP)  15   1   0   0   0   8    1  |    79      3.2        3.3
  Avg all   = Total / all ballots — a blank counts as 0, so this is the Total the Scoring Round ranks on, per ballot.
  Avg rated = Total / the ballots that scored this candidate (Abs excluded) — support among voters who had an opinion.
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/bxj8pxc_agriculture_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/04_Real_Elections/florida_2026_star_poll/cases/bxj8pxc_agriculture.yaml
```

## See also

- [Runoff reversal (worked set)](../../../../02_Examples/runoff_overturns_leader/README.md)
- [Ballot & terminology basics](../../../../../07_Concepts/topics/ballot_and_terminology_basics.md)
- [Glossary](../../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [bxj8pxc_attorney_general](bxj8pxc_attorney_general.md) · [bxj8pxc_cfo](bxj8pxc_cfo.md) · [bxj8pxc_senate](bxj8pxc_senate.md)
