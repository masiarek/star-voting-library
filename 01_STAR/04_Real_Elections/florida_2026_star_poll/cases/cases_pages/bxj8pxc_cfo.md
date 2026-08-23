---
search:
  exclude: true
---

# FL 2026 poll — 2026 FL Chief Financial Officer

*Generated from [`bxj8pxc_cfo.yaml`](../bxj8pxc_cfo.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../../01_Learn/README.md) · **1 seat** · **Expected winner:** Smith (NPA)

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/xj8pxc) · **[results ↗](https://bettervoting.com/xj8pxc/results)** (election `xj8pxc`).

## Scenario

**2026 FL Chief Financial Officer** — the thinnest race — 18 of 25 ballots tallied, 7 abstentions. An unaffiliated candidate (NPA) leads the scoring round and wins the runoff 9-5.

Scoring round: Smith (NPA) 37 · Collige (REP) 26 · Ingoglia (REP)* 23 · Gruters (REP) 21.
Automatic Runoff: Smith (NPA) 9 vs Collige (REP) 5, with 4 of the
18 tallied ballots showing Equal Support for both finalists.

25 ballots were cast in the poll; 7 left this race blank (18 tallied).
Markers: `&` = the BetterVoting `null` (candidate left unscored) — it tabulates as 0,
and a ballot that is `&` all the way across is an abstention in this race.
Party tags are the candidates' own ballot labels; `*` marks the incumbent.

Frozen from the live poll on 2026-08-22 (the poll stays open to 2026-11-11, so the
live page will keep moving — this file is the snapshot LH is checked against).

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

Markers on these ballots: `-` blank · `~` race abstention · `&` candidate abstention · `?` spoiled · `%` spoiled+reissued — all tabulate as 0 (reported honestly).

```text
Smith (NPA),Collige (REP),Gruters (REP),Ingoglia (REP)*
5,&,&,&   # b-d67ygqqb
&,&,&,&   # b-7qr6fp6d
&,5,&,&   # b-dh7xj93b
&,&,&,&   # b-qkyw76rq
&,&,&,5   # b-cqcfrhgf
&,&,&,&   # b-6mwmcfmd
&,&,5,&   # b-8kq29hv8
5,0,0,0   # b-xfftm9yb
5,0,0,0   # b-gyvqdrry
0,0,&,0   # b-6ywyq88y
0,0,0,0   # b-9v7q4dvt
5,0,0,0   # b-6c2y3d3p
&,&,&,5   # b-3xdd4ptb
0,0,0,0   # b-9ry7jmwv
0,3,3,3   # b-rqd88v3w
5,0,0,0   # b-bk8xd8fw
5,1,1,0   # b-8bfw9dyf
&,5,&,0   # b-gffckf36
0,5,5,0   # b-6hfy233k
&,&,&,5   # b-ypm6vddm
&,&,&,&   # b-pfvxtxmh
5,2,2,0   # b-fhgbkw3x
1,0,0,0   # b-mybbty26
1,0,0,0   # b-xc3yfg8c
0,5,5,5   # b-vjpmvx6c
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 25 ballots. Note: 4 of 25 ballots are marked as abstentions.
Count × Smith (NPA),Collige (REP),Gruters (REP),Ingoglia (REP)*
    4 ×           &,            &,            &,              &
    4 ×           5,            0,            0,              0
    3 ×           &,            &,            &,              5
    2 ×           0,            0,            0,              0
    2 ×           1,            0,            0,              0
    1 ×           5,            &,            &,              &
    1 ×           &,            5,            &,              &
    1 ×           &,            &,            5,              &
    1 ×           0,            0,            &,              0
    1 ×           0,            3,            3,              3
    1 ×           5,            1,            1,              0
    1 ×           &,            5,            &,              0
    1 ×           0,            5,            5,              0
    1 ×           5,            2,            2,              0
    1 ×           0,            5,            5,              5

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Smith (NPA)     -- 37 -- First place
   Collige (REP)   -- 26 -- Second place
   Ingoglia (REP)* -- 23
   Gruters (REP)   -- 21
 Smith (NPA) and Collige (REP) advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Smith (NPA)     -- 9 -- First place
   Collige (REP)   -- 5
   Equal Support   -- 11
 Smith (NPA) wins.
   Runoff math:
     25  ballots cast
   − 11  Equal Support (no preference between the two finalists)
     ──
     14  voters with a preference  (majority = 8)
           Smith (NPA) 9 (64%)  ·  Collige (REP) 5 (36%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Smith (NPA)
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                        |    * Smith (NPA)    |  * Collige (REP)   |    Gruters (REP)   |   Ingoglia (REP)*  |
--------------------------------------------------------------------------------------------------------------
        * Smith (NPA) > |         ---         |    9 - 11 -  5     |    9 - 12 -  4     |    9 - 11 -  5     |
      * Collige (REP) > |     5 - 11 -  9     |        ---         |    2 - 22 -  1     |    5 - 17 -  3     |
        Gruters (REP) > |     4 - 12 -  9     |    1 - 22 -  2     |        ---         |    4 - 18 -  3     |
      Ingoglia (REP)* > |     5 - 11 -  9     |    3 - 17 -  5     |    3 - 18 -  4     |        ---         |

[Condorcet Winner]
  Condorcet Winner: Smith (NPA) — matches the STAR winner

[Condorcet Loser]
  Condorcet Loser: Ingoglia (REP)* — loses every head-to-head matchup

[Score Distribution] (how many ballots gave each star rating)
                         Score
Candidate         5   4   3   2   1   0  Abs  | Total  Avg all  Avg rated
Smith (NPA)       7   0   0   0   2   6   10  |    37      1.5        2.5
Collige (REP)     4   0   1   1   1   9    9  |    26      1.0        1.6
Gruters (REP)     3   0   1   1   1   8   11  |    21      0.8        1.5
Ingoglia (REP)*   4   0   1   0   0  13    7  |    23      0.9        1.3
  Avg all   = Total / all ballots — a blank counts as 0, so this is the Total the Scoring Round ranks on, per ballot.
  Avg rated = Total / the ballots that scored this candidate (Abs excluded) — support among voters who had an opinion.
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/bxj8pxc_cfo_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/04_Real_Elections/florida_2026_star_poll/cases/bxj8pxc_cfo.yaml
```

## See also

- [Runoff reversal (worked set)](../../../../02_Examples/runoff_overturns_leader/README.md)
- [Ballot & terminology basics](../../../../../07_Concepts/topics/ballot_and_terminology_basics.md)
- [Glossary](../../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [bxj8pxc_agriculture](bxj8pxc_agriculture.md) · [bxj8pxc_attorney_general](bxj8pxc_attorney_general.md) · [bxj8pxc_senate](bxj8pxc_senate.md)
