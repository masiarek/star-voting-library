---
search:
  exclude: true
---

# FL 2026 poll — 2026 FL Attorney General

*Generated from [`bxj8pxc_attorney_general.yaml`](../bxj8pxc_attorney_general.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../../01_Learn/README.md) · **1 seat** · **Expected winner:** Rodriguez (DEM)

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/xj8pxc) · **[results ↗](https://bettervoting.com/xj8pxc/results)** (election `xj8pxc`).

## Scenario

**2026 FL Attorney General** — four candidates, two per party. Both finalists are Democrats again, and the runoff margin is 5-3 — 13 of the 21 tallied ballots express no preference between them.

Scoring round: Rodriguez (DEM) 50 · Lewis (DEM) 46 · Uthmeier (REP)* 38 · Leskovich (REP) 21.
Automatic Runoff: Rodriguez (DEM) 5 vs Lewis (DEM) 3, with 13 of the
21 tallied ballots showing Equal Support for both finalists.

25 ballots were cast in the poll; 4 left this race blank (21 tallied).
Markers: `&` = the BetterVoting `null` (candidate left unscored) — it tabulates as 0,
and a ballot that is `&` all the way across is an abstention in this race.
Party tags are the candidates' own ballot labels; `*` marks the incumbent.

Frozen from the live poll on 2026-08-22 (the poll stays open to 2026-11-11, so the
live page will keep moving — this file is the snapshot LH is checked against).

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

Markers on these ballots: `-` blank · `~` race abstention · `&` candidate abstention · `?` spoiled · `%` spoiled+reissued — all tabulate as 0 (reported honestly).

```text
Lewis (DEM),Rodriguez (DEM),Leskovich (REP),Uthmeier (REP)*
5,&,&,&   # b-d67ygqqb
&,&,&,&   # b-7qr6fp6d
&,&,5,&   # b-dh7xj93b
5,5,&,&   # b-qkyw76rq
&,&,&,5   # b-cqcfrhgf
&,&,&,&   # b-6mwmcfmd
&,&,&,5   # b-8kq29hv8
5,5,0,0   # b-xfftm9yb
4,5,0,0   # b-gyvqdrry
0,0,0,0   # b-6ywyq88y
0,0,0,0   # b-9v7q4dvt
5,5,0,0   # b-6c2y3d3p
&,&,&,5   # b-3xdd4ptb
&,5,0,0   # b-9ry7jmwv
0,0,4,4   # b-rqd88v3w
4,5,0,0   # b-bk8xd8fw
5,5,1,0   # b-8bfw9dyf
0,5,&,&   # b-gffckf36
0,0,5,5   # b-6hfy233k
&,&,&,5   # b-ypm6vddm
&,&,&,5   # b-pfvxtxmh
5,3,1,0   # b-fhgbkw3x
4,5,0,0   # b-mybbty26
4,2,0,0   # b-xc3yfg8c
0,0,5,4   # b-vjpmvx6c
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
[Divergence from STAR]
  STAR                   = Rodriguez (DEM)
  Choose-One (Plurality) = Lewis (DEM)   (differs from STAR)
  RCV-IRV                = Lewis (DEM)   (differs from STAR)
  Approval               = Lewis (DEM)   (differs from STAR)
  Note: 6 of 25 ballots (24%) had equal non-zero scores, so their ranks were
        decided by candidate priority order. The RCV-IRV result may be an
        artifact of score-to-rank tie-breaking rather than a deep
        difference.
  Note: Ranked Robin (RCV-RR) agrees with STAR, so RCV-IRV is the lone
        outlier — the classic center-squeeze signature.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: cases_tabulated/bxj8pxc_attorney_general_RCV-IRV_tabulated.txt

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 25 ballots. Note: 2 of 25 ballots are marked as abstentions.
Count × Lewis (DEM),Rodriguez (DEM),Leskovich (REP),Uthmeier (REP)*
    5 ×           &,              &,              &,              5
    3 ×           4,              5,              0,              0
    2 ×           &,              &,              &,              &
    2 ×           5,              5,              0,              0
    2 ×           0,              0,              0,              0
    1 ×           5,              &,              &,              &
    1 ×           &,              &,              5,              &
    1 ×           5,              5,              &,              &
    1 ×           &,              5,              0,              0
    1 ×           0,              0,              4,              4
    1 ×           5,              5,              1,              0
    1 ×           0,              5,              &,              &
    1 ×           0,              0,              5,              5
    1 ×           5,              3,              1,              0
    1 ×           4,              2,              0,              0
    1 ×           0,              0,              5,              4

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Rodriguez (DEM) -- 50 -- First place
   Lewis (DEM)     -- 46 -- Second place
   Uthmeier (REP)* -- 38
   Leskovich (REP) -- 21
 Rodriguez (DEM) and Lewis (DEM) advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Rodriguez (DEM) -- 5 -- First place
   Lewis (DEM)     -- 3
   Equal Support   -- 17
 Rodriguez (DEM) wins.
   Runoff math:
     25  ballots cast
   − 17  Equal Support (no preference between the two finalists)
     ──
      8  voters with a preference  (majority = 5)
           Rodriguez (DEM) 5 (62%)  ·  Lewis (DEM) 3 (38%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Rodriguez (DEM)
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                        |    * Lewis (DEM)    | * Rodriguez (DEM)  |   Leskovich (REP)  |   Uthmeier (REP)*  |
--------------------------------------------------------------------------------------------------------------
        * Lewis (DEM) > |         ---         |    3 - 17 -  5     |   10 - 11 -  4     |   10 -  7 -  8     |
    * Rodriguez (DEM) > |     5 - 17 -  3     |        ---         |   11 - 10 -  4     |   11 -  6 -  8     |
      Leskovich (REP) > |     4 - 11 - 10     |    4 - 10 - 11     |        ---         |    4 - 16 -  5     |
      Uthmeier (REP)* > |     8 -  7 - 10     |    8 -  6 - 11     |    5 - 16 -  4     |        ---         |

[Condorcet Winner]
  Condorcet Winner: Rodriguez (DEM) — matches the STAR winner

[Condorcet Loser]
  Condorcet Loser: Leskovich (REP) — loses every head-to-head matchup

[Score Distribution] (how many ballots gave each star rating)
                         Score
Candidate         5   4   3   2   1   0  Abs  | Total  Avg all  Avg rated
Lewis (DEM)       6   4   0   0   0   6    9  |    46      1.8        2.9
Rodriguez (DEM)   9   0   1   1   0   5    9  |    50      2.0        3.1
Leskovich (REP)   3   1   0   0   2   9   10  |    21      0.8        1.4
Uthmeier (REP)*   6   2   0   0   0  11    6  |    38      1.5        2.0
  Avg all   = Total / all ballots — a blank counts as 0, so this is the Total the Scoring Round ranks on, per ballot.
  Avg rated = Total / the ballots that scored this candidate (Abs excluded) — support among voters who had an opinion.
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/bxj8pxc_attorney_general_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/04_Real_Elections/florida_2026_star_poll/cases/bxj8pxc_attorney_general.yaml
```

## See also

- [Methods disagree on this election](../../../../../method_comparisons/divergence_review/cases/IRV_DIFFERS_ARTIFACT/bxj8pxc_attorney_general.md) — its entry in the divergence review ledger
- [Runoff reversal (worked set)](../../../../02_Examples/runoff_overturns_leader/README.md)
- [Ballot & terminology basics](../../../../../07_Concepts/topics/ballot_and_terminology_basics.md)
- [Glossary](../../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [bxj8pxc_agriculture](bxj8pxc_agriculture.md) · [bxj8pxc_cfo](bxj8pxc_cfo.md) · [bxj8pxc_senate](bxj8pxc_senate.md)
