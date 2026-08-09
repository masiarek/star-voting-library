---
search:
  exclude: true
---

# Free riding — honest baseline (SSS)

*Generated from [`free_ride_honest_sss.yaml`](../free_ride_honest_sss.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Sequentially Spent Score (proportional STAR)](../../../../01_Learn/README.md) · **2 seats** · **Expected winners:** Anika, Bruno

## Scenario

The honest ballots of free_ride_honest_allocated.yaml, counted with Sequentially Spent Score instead. SSS reaches the same result — Anika and Bruno — so the free ride in free_ride_hylland_sss.yaml is a genuine change of outcome and not an artefact of the tabulation.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:Anika,Bruno,Camila
12:5,4,0
8:5,0,5
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
    8 ×     5,    0,     5

[Sequentially Spent Score: Round 1]
 The highest-scoring candidate wins a seat.
   Anika         -- 100 -- First place
   Bruno         --  48
   Camila        --  40
 Anika wins a seat.

[Sequentially Spent Score: Round 1: Ballot allocation round]
 Total score is 100, Hare score quota is 50, giving back surplus.
 Reducing each ballot's stars by their vote * 1/2.
 20 ballots voted 5, stars reduced from 5 to 5/2, reweighted to 1/2.

[Sequentially Spent Score: Round 2]
 The highest-scoring candidate wins a seat.
   Bruno         -- 24 -- First place
   Camila        -- 20
 Bruno wins a seat.

[Sequentially Spent Score: Winners — Sequentially Spent Score Voting Method (2 winners)]
 Anika
 Bruno
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
         Anika > |     ---      |20 -  0 -  0 |12 -  8 -  0 |
         Bruno > |  0 -  0 - 20 |    ---      |12 -  0 -  8 |
        Camila > |  0 -  8 - 12 | 8 -  0 - 12 |    ---      |

[Condorcet Winner]
  Condorcet Winner: Anika — matches the STAR winner

[Condorcet Loser]
  Condorcet Loser: Camila — loses every head-to-head matchup

[Score Distribution] (how many ballots gave each star rating)
                   Score
Candidate   5   4   3   2   1   0  | Total   Avg
Anika      20   0   0   0   0   0  |   100   5.0
Bruno       0  12   0   0   0   8  |    48   2.4
Camila      8   0   0   0   0  12  |    40   2.0
 Hare score quota is 50.
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/free_ride_honest_sss_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 03_STAR_PR/03_Criteria/free_riding/cases/free_ride_honest_sss.yaml
```

## See also

- [Glossary](../../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [free_ride_arms_race_allocated](free_ride_arms_race_allocated.md) · [free_ride_honest_allocated](free_ride_honest_allocated.md) · [free_ride_honest_rrv](free_ride_honest_rrv.md) · [free_ride_hylland_allocated](free_ride_hylland_allocated.md) · [free_ride_hylland_rrv](free_ride_hylland_rrv.md) · [free_ride_hylland_sss](free_ride_hylland_sss.md) · [misjudged_queue_bury](misjudged_queue_bury.md) · [misjudged_queue_honest](misjudged_queue_honest.md) · [misjudged_queue_hylland](misjudged_queue_hylland.md)
