---
search:
  exclude: true
---

# Misjudged queue — honest baseline

*Generated from [`misjudged_queue_honest.yaml`](../misjudged_queue_honest.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Allocated Score (proportional STAR)](../../../../01_Learn/README.md) · **2 seats** · **Expected winners:** Amara, Boris

## Scenario

HONEST BASELINE for the backfire pair. A different election: the 8-voter minority scores Amara 5 and Cleo 4; the 12-voter majority is only lukewarm on Amara (3) and wants Boris (5). Amara wins seat 1 with 76. The quota is charged from the top down, and the top score group is the MINORITY's own 5-star ballots — all 8 are spent in full before the majority is touched at all. Seat 2 goes to Boris. The minority's honest haul is Amara, whom they scored 5. Compare misjudged_queue_hylland.yaml and misjudged_queue_bury.yaml.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:Amara,Boris,Cleo
12:3,5,0
8:5,0,4
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
[Divergence from STAR]
  STAR     = Boris
  Approval = Amara   (differs from STAR)

[Runoff Reversal]
 - Score Round Winner(s) = (Amara)
 - Runoff Round Winner   = (Boris)
  Candidate Amara earned the highest total score, but
  Candidate Boris won the automatic runoff — not a malfunction,
  STAR working as designed: the runoff elects the finalist preferred
  by the majority (of voters with a preference).

--- Allocated Score Voting Method (2 winners) ---

[Allocated Score Voting]
 Tabulating 20 ballots to fill 2 seats.
Count × Amara,Boris,Cleo
   12 ×     3,    5,   0
    8 ×     5,    0,   4

[Allocated Score Voting: Round 1]
 The highest-scoring candidate wins a seat.
   Amara         -- 76 -- First place
   Boris         -- 60
   Cleo          -- 32
 Amara wins a seat.

[Allocated Score Voting: Round 1: Ballot allocation round]
 Allocating 10 ballots.

[Allocated Score Voting: Round 1: Ballot allocation round: Round 1]
 Allocating 8 ballots at score 5.

[Allocated Score Voting: Round 1: Ballot allocation round: Round 2]
 Remaining allocation quota is 2.
 Allocating 12 ballots at score 3.
 This allocation overfills the remaining quota.  Returning fractional surplus.
 Allocating only 16.67% of these ballots.
 Keeping these ballots, but multiplying their weights by 5/6.
 12 ballots reweighted from 1 to 5/6.

[Allocated Score Voting: Round 2]
 Tabulating 12 remaining ballots.
Count × Amara,Boris,Cleo
   12 ×     3,    5,   0
    8 ×     5,    0,   4

[Allocated Score Voting: Winners — Allocated Score Voting Method (2 winners)]
 Amara
 Boris
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
       * Amara > |     ---      | 8 -  0 - 12 |20 -  0 -  0 |
       * Boris > | 12 -  0 -  8 |    ---      |12 -  0 -  8 |
          Cleo > |  0 -  0 - 20 | 8 -  0 - 12 |    ---      |

[Condorcet Winner]
  Condorcet Winner: Boris — matches the STAR winner

[Condorcet Loser]
  Condorcet Loser: Cleo — loses every head-to-head matchup

[Score Distribution] (how many ballots gave each star rating)
                   Score
Candidate   5   4   3   2   1   0  | Total   Avg
Amara       8   0  12   0   0   0  |    76   3.8
Boris      12   0   0   0   0   8  |    60   3.0
Cleo        0   8   0   0   0  12  |    32   1.6
 Hare quota is 10.

[Score Distribution] (how many ballots gave each star rating)
                   Score
Candidate   5   4   3   2   1   0  | Total   Avg
Amara       8   0  12   0   0   0  |    76   3.8
Boris      12   0   0   0   0   8  |    60   3.0
Cleo        0   8   0   0   0  12  |    32   1.6
 The highest-scoring candidate wins a seat.
   Boris         -- 50 -- First place
   Cleo          --  0
 Boris wins a seat.
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/misjudged_queue_honest_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 03_STAR_PR/03_Criteria/free_riding/cases/misjudged_queue_honest.yaml
```

## See also

- [Glossary](../../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [free_ride_arms_race_allocated](free_ride_arms_race_allocated.md) · [free_ride_honest_allocated](free_ride_honest_allocated.md) · [free_ride_honest_rrv](free_ride_honest_rrv.md) · [free_ride_honest_sss](free_ride_honest_sss.md) · [free_ride_hylland_allocated](free_ride_hylland_allocated.md) · [free_ride_hylland_rrv](free_ride_hylland_rrv.md) · [free_ride_hylland_sss](free_ride_hylland_sss.md) · [misjudged_queue_bury](misjudged_queue_bury.md) · [misjudged_queue_hylland](misjudged_queue_hylland.md)
