---
search:
  exclude: true
---

# Tied for the second finalist — the head-to-head rung settles it (BV2276, qhjyr2)

*Generated from [`bv2276_qhjyr2_second_finalist_tie.yaml`](../bv2276_qhjyr2_second_finalist_tie.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../../01_Learn/README.md) · **1 seat** · **Expected winner:** Ana

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/qhjyr2) · **[results ↗](https://bettervoting.com/qhjyr2/results)** (election `qhjyr2` · test `BV2276`).

## Scenario

Five voters, four candidates. Scoring round: Ana leads at 15, but Ben and Cora
BOTH finish on 14 — so the scoring round names only ONE finalist outright and the
second runoff slot has to be settled another way. STAR's ladder settles it on its
FIRST deterministic rung, the head-to-head: Cora is preferred to Ben on three of
the five ballots to Ben's two, so Cora advances and the runoff is Ana vs Cora.
No five-star rung, no lot, no random — re-run the count and the pair never moves.
The automatic runoff then goes Ana 2, Cora 1, with 2 of the 5 voters rating the
two finalists EQUALLY (one gives both 3 stars, one gives both 5), so Equal Support
ties the winner as the largest group on the chart. Ana wins.
The lesson: a tie for a FINALIST SLOT sounds alarming and usually isn't — it has an
ordinary, deterministic answer that doesn't depend on candidate order or on who
happened to be listed second. Contrast BV2180/fp62p2, where pairwise CAN'T separate
three tied candidates and the five-star rung takes over.
This election also serves as the regression fixture for BetterVoting reporting issue
#1484 (https://github.com/Equal-Vote/bettervoting/issues/1484): on the live results
page the charts and Tabulation Steps correctly name Cora, while the Scores Table
highlight and the Runoff Table name BEN — the second-highest SCORER rather than the
candidate the tiebreak advanced — and Equal Support collapses from 2 to 0.
Live results: https://bettervoting.com/qhjyr2/results
Lesson: bv2276_qhjyr2_second_finalist_tie.md

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Ana, Ben, Cora, Dev
5, 3, 5, 0
3, 1, 3, 0
5, 4, 2, 1
1, 4, 0, 5
1, 2, 4, 5
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 5 ballots.
Ana,Ben,Cora,Dev
  5,  3,   5,  0
  3,  1,   3,  0
  5,  4,   2,  1
  1,  4,   0,  5
  1,  2,   4,  5

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Ana           -- 15 -- First place
   Ben           -- 14 -- Tied for second place
   Cora          -- 14 -- Tied for second place
   Dev           -- 11
 Ana advances, but there's a two-way tie for second.

[STAR Voting: Scoring Round: First tiebreaker]
 The candidate preferred in the most head-to-head matchups advances.
   Cora          -- 3 -- Second place
   Ben           -- 2
   Equal Support -- 0
 Ana and Cora advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Ana           -- 2 -- First place
   Cora          -- 1
   Equal Support -- 2
 Ana wins.
   Runoff math:
     5  ballots cast
   − 2  Equal Support (no preference between the two finalists)
     ─
     3  voters with a preference  (majority = 2)
           Ana 2 (67%)  ·  Cora 1 (33%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Ana
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |   * Ana    |  * Ben    |    Cora   |    Dev    |
-----------------------------------------------------------------
       * Ana > |    ---     |3 - 0 - 2  |2 - 2 - 1  |3 - 0 - 2  |
       * Ben > | 2 - 0 - 3  |   ---     |2 - 0 - 3  |3 - 0 - 2  |
        Cora > | 1 - 2 - 2  |3 - 0 - 2  |   ---     |3 - 0 - 2  |
         Dev > | 2 - 0 - 3  |2 - 0 - 3  |2 - 0 - 3  |   ---     |

[Condorcet Winner]
  Condorcet Winner: Ana — matches the STAR winner

[Condorcet Loser]
  Condorcet Loser: Dev — loses every head-to-head matchup

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Ana        2  0  1  0  2  0  |    15   3.0
Ben        0  2  1  1  1  0  |    14   2.8
Cora       1  1  1  1  0  1  |    14   2.8
Dev        2  0  0  0  1  2  |    11   2.2
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/bv2276_qhjyr2_second_finalist_tie_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/03_Criteria/tie_break_ladder/cases/bv2276_qhjyr2_second_finalist_tie.yaml
```

## See also

- [Ties & tie-breaking (topic hub)](../../../../../07_Concepts/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../../01_Learn/Tie_Breaking_STAR/tie_breaking.md)
- [Runoff reversal (worked set)](../../../../02_Examples/runoff_overturns_leader/README.md)
- [Glossary](../../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [bv2180_fp62p2_ice_cream_ladder](bv2180_fp62p2_ice_cream_ladder.md) · [bv830_vb3xv2_no_condorcet_tie_score](bv830_vb3xv2_no_condorcet_tie_score.md)
