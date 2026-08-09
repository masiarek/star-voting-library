---
search:
  exclude: true
---

# Free riding — both sides ride, nobody gains

*Generated from [`free_ride_arms_race_allocated.yaml`](../free_ride_arms_race_allocated.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Allocated Score (proportional STAR)](../../../../01_Learn/README.md) · **2 seats** · **Expected winners:** Anika, Bruno

## Scenario

THE STRATEGY CANCELS ITSELF. Both blocs free ride: all 20 voters now score Anika 4 rather than 5. She still wins seat 1, and every ballot is once again in the same score group — so the quota is charged to everyone equally, exactly as it was under honest voting, and Bruno takes the second seat 24 to 20. The free ride pays only while the OTHER side does not attempt it. Its gain is positional, not absolute, which is the main reason it is self-limiting in practice.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:Anika,Bruno,Camila
12:4,4,0
8:4,0,5
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
--- Allocated Score Voting Method (2 winners) ---

[Allocated Score Voting]
 Tabulating 20 ballots to fill 2 seats.
Count × Anika,Bruno,Camila
   12 ×     4,    4,     0
    8 ×     4,    0,     5

[Allocated Score Voting: Round 1]
 The highest-scoring candidate wins a seat.
   Anika         -- 80 -- First place
   Bruno         -- 48
   Camila        -- 40
 Anika wins a seat.

[Allocated Score Voting: Round 1: Ballot allocation round]
 Allocating 10 ballots.

[Allocated Score Voting: Round 1: Ballot allocation round: Round 1]
 Allocating 20 ballots at score 4.
 This allocation overfills the quota.  Returning fractional surplus.
 Allocating only 50.00% of these ballots.
 Keeping these ballots, but multiplying their weights by 1/2.
 20 ballots reweighted from 1 to 1/2.

[Allocated Score Voting: Round 2]
 The highest-scoring candidate wins a seat.
   Bruno         -- 24 -- First place
   Camila        -- 20
 Bruno wins a seat.

[Allocated Score Voting: Winners — Allocated Score Voting Method (2 winners)]
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
       * Anika > |     ---      | 8 - 12 -  0 |12 -  0 -  8 |
       * Bruno > |  0 - 12 -  8 |    ---      |12 -  0 -  8 |
        Camila > |  8 -  0 - 12 | 8 -  0 - 12 |    ---      |

[Condorcet Winner]
  Condorcet Winner: Anika — matches the STAR winner

[Condorcet Loser]
  Condorcet Loser: Camila — loses every head-to-head matchup

[Score Distribution] (how many ballots gave each star rating)
                   Score
Candidate   5   4   3   2   1   0  | Total   Avg
Anika       0  20   0   0   0   0  |    80   4.0
Bruno       0  12   0   0   0   8  |    48   2.4
Camila      8   0   0   0   0  12  |    40   2.0
 Hare quota is 10.
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/free_ride_arms_race_allocated_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 03_STAR_PR/03_Criteria/free_riding/cases/free_ride_arms_race_allocated.yaml
```

## See also

- [Glossary](../../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [free_ride_honest_allocated](free_ride_honest_allocated.md) · [free_ride_honest_rrv](free_ride_honest_rrv.md) · [free_ride_honest_sss](free_ride_honest_sss.md) · [free_ride_hylland_allocated](free_ride_hylland_allocated.md) · [free_ride_hylland_rrv](free_ride_hylland_rrv.md) · [free_ride_hylland_sss](free_ride_hylland_sss.md) · [misjudged_queue_bury](misjudged_queue_bury.md) · [misjudged_queue_honest](misjudged_queue_honest.md) · [misjudged_queue_hylland](misjudged_queue_hylland.md)
