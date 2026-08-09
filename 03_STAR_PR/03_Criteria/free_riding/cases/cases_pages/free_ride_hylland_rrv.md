---
search:
  exclude: true
---

# Free riding — the free ride fails (RRV)

*Generated from [`free_ride_hylland_rrv.yaml`](../free_ride_hylland_rrv.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Reweighted Range Voting (proportional STAR)](../../../../01_Learn/README.md) · **2 seats** · **Expected winners:** Anika, Bruno

## Scenario

THE CONTROL THAT DOES NOT BREAK. The free-riding ballots of free_ride_hylland_allocated.yaml, counted with Reweighted Range Voting — and here the strategy FAILS. RRV's weight is a smooth function of the score you gave, 1/(1 + score/max), so dropping Anika from 5 to 4 moves a free rider from 1/2 to 5/9 rather than from 1/2 to 1. Camila climbs from 20 to 22.22 and still loses to Bruno's 24. Bruno keeps the seat that the quota methods handed to Camila. RRV is a divisor method with no score groups and therefore no cliff to jump.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:Anika,Bruno,Camila
12:5,4,0
8:4,0,5
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
--- Reweighted Range Voting Method (2 winners) ---

[Reweighted Range Voting]
 Tabulating 20 ballots to fill 2 seats.
Count × Anika,Bruno,Camila
   12 ×     5,    4,     0
    8 ×     4,    0,     5

[Reweighted Range Voting: Round 1: Score round]
 The highest-scoring candidate wins a seat.
   Anika         -- 92 -- First place
   Bruno         -- 48
   Camila        -- 40
 Anika wins a seat.

[Reweighted Range Voting: Round 1: Reweighing Ballots]
 Reweighted 20 ballots:
   12 ballots reweighted from 1 to 1/2.
   8 ballots reweighted from 1 to 5/9.

[Reweighted Range Voting: Round 2: Score round]
 The highest-scoring candidate wins a seat.
   Bruno         -- 24     -- First place
   Camila        -- 22+2/9
 Bruno wins a seat.

[Reweighted Range Voting: Winners — Reweighted Range Voting Method (2 winners)]
 Anika
 Bruno
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |   * Anika    |  * Bruno    |    Camila   |
-------------------------------------------------------------
       * Anika > |     ---      |20 -  0 -  0 |12 -  0 -  8 |
       * Bruno > |  0 -  0 - 20 |    ---      |12 -  0 -  8 |
        Camila > |  8 -  0 - 12 | 8 -  0 - 12 |    ---      |

[Condorcet Winner]
  Condorcet Winner: Anika — matches the STAR winner

[Condorcet Loser]
  Condorcet Loser: Camila — loses every head-to-head matchup

[Score Distribution] (how many ballots gave each star rating)
                   Score
Candidate   5   4   3   2   1   0  | Total   Avg
Anika      12   8   0   0   0   0  |    92   4.6
Bruno       0  12   0   0   0   8  |    48   2.4
Camila      8   0   0   0   0  12  |    40   2.0
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/free_ride_hylland_rrv_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 03_STAR_PR/03_Criteria/free_riding/cases/free_ride_hylland_rrv.yaml
```

## See also

- [Glossary](../../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [free_ride_arms_race_allocated](free_ride_arms_race_allocated.md) · [free_ride_honest_allocated](free_ride_honest_allocated.md) · [free_ride_honest_rrv](free_ride_honest_rrv.md) · [free_ride_honest_sss](free_ride_honest_sss.md) · [free_ride_hylland_allocated](free_ride_hylland_allocated.md) · [free_ride_hylland_sss](free_ride_hylland_sss.md) · [misjudged_queue_bury](misjudged_queue_bury.md) · [misjudged_queue_honest](misjudged_queue_honest.md) · [misjudged_queue_hylland](misjudged_queue_hylland.md)
