---
search:
  exclude: true
---

# Free riding — the free ride (SSS)

*Generated from [`free_ride_hylland_sss.yaml`](../free_ride_hylland_sss.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Sequentially Spent Score (proportional STAR)](../../../../01_Learn/README.md) · **2 seats** · **Expected winners:** Anika, Camila

## Scenario

The free-riding ballots of free_ride_hylland_allocated.yaml, counted with Sequentially Spent Score. SSS spends score from the top down just as Allocated Score does, so it inherits the same cliff: the minority's 4-star ballots are reached later, or not at all, and the second seat moves from Bruno to Camila. SSS is not a defence against this.

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
--- Sequentially Spent Score Voting Method (2 winners) ---

[Sequentially Spent Score]
 Tabulating 20 ballots to fill 2 seats.
Count × Anika,Bruno,Camila
   12 ×     5,    4,     0
    8 ×     4,    0,     5

[Sequentially Spent Score: Round 1]
 The highest-scoring candidate wins a seat.
   Anika         -- 92 -- First place
   Bruno         -- 48
   Camila        -- 40
 Anika wins a seat.

[Sequentially Spent Score: Round 1: Ballot allocation round]
 Total score is 92, Hare score quota is 50, giving back surplus.
 Reducing each ballot's stars by their vote * 21/46.
 Reweighted 20 ballots:
    12 ballots voted 5, stars reduced from 5 to 105/46, reweighted to 21/46.
    8 ballots voted 4, stars reduced from 5 to 65/23, reweighted to 13/23.

[Sequentially Spent Score: Round 2]
 The highest-scoring candidate wins a seat.
   Camila        -- 22+14/23 -- First place
   Bruno         -- 21+21/23
 Camila wins a seat.

[Sequentially Spent Score: Winners — Sequentially Spent Score Voting Method (2 winners)]
 Anika
 Camila
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Preference Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        Informational only — not part of the 2-winner count below,
        so no Top-2 finalists are marked.
                 |     Anika    |    Bruno    |    Camila   |
-------------------------------------------------------------
         Anika > |     ---      |20 -  0 -  0 |12 -  0 -  8 |
         Bruno > |  0 -  0 - 20 |    ---      |12 -  0 -  8 |
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
 Hare score quota is 50.
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/free_ride_hylland_sss_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 03_STAR_PR/03_Criteria/free_riding/cases/free_ride_hylland_sss.yaml
```

## See also

- [Glossary](../../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [free_ride_arms_race_allocated](free_ride_arms_race_allocated.md) · [free_ride_honest_allocated](free_ride_honest_allocated.md) · [free_ride_honest_rrv](free_ride_honest_rrv.md) · [free_ride_honest_sss](free_ride_honest_sss.md) · [free_ride_hylland_allocated](free_ride_hylland_allocated.md) · [free_ride_hylland_rrv](free_ride_hylland_rrv.md) · [misjudged_queue_bury](misjudged_queue_bury.md) · [misjudged_queue_honest](misjudged_queue_honest.md) · [misjudged_queue_hylland](misjudged_queue_hylland.md)
