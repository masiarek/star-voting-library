---
search:
  exclude: true
---

# Misjudged queue — the free ride backfires

*Generated from [`misjudged_queue_bury.yaml`](../misjudged_queue_bury.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Allocated Score (proportional STAR)](../../../../01_Learn/README.md) · **2 seats** · **Expected winners:** Boris, Cleo

## Scenario

THE BACKFIRE. Having gained nothing at 4, the minority pushes to 0 — burying Amara completely, which under Allocated Score is the one move that guarantees exemption, since ballots scoring the winner 0 are never charged at all. It works, and it costs them the election they wanted. Without their 40 points Amara drops to 36 and LOSES seat 1 to Boris, whose supporters are then charged the quota; Cleo takes seat 2 on the minority's untouched ballots. Their honest haul was Amara, scored 5; their strategic haul is Cleo, scored 4. They are strictly worse off, and the board lost the one candidate every voter actually liked.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:Amara,Boris,Cleo
12:3,5,0
8:0,0,4
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
[Divergence from STAR]
  STAR     = Boris
  Approval = Amara   (differs from STAR)

--- Allocated Score Voting Method (2 winners) ---

[Allocated Score Voting]
 Tabulating 20 ballots to fill 2 seats.
Count × Amara,Boris,Cleo
   12 ×     3,    5,   0
    8 ×     0,    0,   4

[Allocated Score Voting: Round 1]
 The highest-scoring candidate wins a seat.
   Boris         -- 60 -- First place
   Amara         -- 36
   Cleo          -- 32
 Boris wins a seat.

[Allocated Score Voting: Round 1: Ballot allocation round]
 Allocating 10 ballots.

[Allocated Score Voting: Round 1: Ballot allocation round: Round 1]
 Allocating 12 ballots at score 5.
 This allocation overfills the quota.  Returning fractional surplus.
 Allocating only 83.33% of these ballots.
 Keeping these ballots, but multiplying their weights by 1/6.
 12 ballots reweighted from 1 to 1/6.

[Allocated Score Voting: Round 2]
 The highest-scoring candidate wins a seat.
   Cleo          -- 32 -- First place
   Amara         --  6
 Cleo wins a seat.

[Allocated Score Voting: Winners — Allocated Score Voting Method (2 winners)]
 Boris
 Cleo
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |   * Amara    |  * Boris    |     Cleo    |
-------------------------------------------------------------
       * Amara > |     ---      | 0 -  8 - 12 |12 -  0 -  8 |
       * Boris > | 12 -  8 -  0 |    ---      |12 -  0 -  8 |
          Cleo > |  8 -  0 - 12 | 8 -  0 - 12 |    ---      |

[Condorcet Winner]
  Condorcet Winner: Boris — matches the STAR winner

[Condorcet Loser]
  Condorcet Loser: Cleo — loses every head-to-head matchup

[Score Distribution] (how many ballots gave each star rating)
                   Score
Candidate   5   4   3   2   1   0  | Total   Avg
Amara       0   0  12   0   0   8  |    36   1.8
Boris      12   0   0   0   0   8  |    60   3.0
Cleo        0   8   0   0   0  12  |    32   1.6
 Hare quota is 10.
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/misjudged_queue_bury_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 03_STAR_PR/03_Criteria/free_riding/cases/misjudged_queue_bury.yaml
```

## See also

- [Glossary](../../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [free_ride_arms_race_allocated](free_ride_arms_race_allocated.md) · [free_ride_honest_allocated](free_ride_honest_allocated.md) · [free_ride_honest_rrv](free_ride_honest_rrv.md) · [free_ride_honest_sss](free_ride_honest_sss.md) · [free_ride_hylland_allocated](free_ride_hylland_allocated.md) · [free_ride_hylland_rrv](free_ride_hylland_rrv.md) · [free_ride_hylland_sss](free_ride_hylland_sss.md) · [misjudged_queue_honest](misjudged_queue_honest.md) · [misjudged_queue_hylland](misjudged_queue_hylland.md)
