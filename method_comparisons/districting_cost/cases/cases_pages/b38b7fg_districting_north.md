---
search:
  exclude: true
---

# Two chapters, one delegate — Northside chapter (5 members)

*Generated from [`b38b7fg_districting_north.yaml`](../b38b7fg_districting_north.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../../01_STAR/01_Learn/README.md) · **1 seat** · **Expected winner:** Ana

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/38b7fg) · **[results ↗](https://bettervoting.com/38b7fg/results)** (election `38b7fg` · test `BV2274`).

## Scenario

Part of the districting-cost trio. Two chapters of one club elect a single
national delegate. Ana is adored in Northside and unknown in Southside; Beto
is the mirror image; Cleo is everybody's solid second. Counted chapter by
chapter, Cleo wins NEITHER — so a delegate chosen from the chapter winners is
Ana or Beto. Counted as one electorate, Cleo wins outright, and she is also
the highest-welfare candidate (33 points to Ana's 23 and Beto's 19) and the
Condorcet winner. That gap is the distortion of distributed voting, made
countable. Companion concept page:
07_Concepts/topics/distributed_voting_distortion.md
Live on BetterVoting (Test ID BV2274): https://bettervoting.com/38b7fg/results
— ONE election carries all three counts as three races. The chapter races
hold all nine papers, with the other chapter's members leaving the contest
blank; a blank scores 0, so every total matches this file exactly.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Ana,Beto,Cleo
5,0,3
5,0,3
5,0,3
4,0,5
4,0,5
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 5 ballots.
Count × Ana,Beto,Cleo
    3 ×   5,   0,   3
    2 ×   4,   0,   5

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Ana           -- 23 -- First place
   Cleo          -- 19 -- Second place
   Beto          --  0
 Ana and Cleo advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Ana           -- 3 -- First place
   Cleo          -- 2
   Equal Support -- 0
 Ana wins.
   Runoff math:
     5  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     5  voters with a preference  (majority = 3)
           Ana 3 (60%)  ·  Cleo 2 (40%)

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
               |   * Ana    |    Beto   |  * Cleo   |
-----------------------------------------------------
       * Ana > |    ---     |5 - 0 - 0  |3 - 0 - 2  |
        Beto > | 0 - 0 - 5  |   ---     |0 - 0 - 5  |
      * Cleo > | 2 - 0 - 3  |5 - 0 - 0  |   ---     |

[Condorcet Winner]
  Condorcet Winner: Ana — matches the STAR winner

[Condorcet Loser]
  Condorcet Loser: Beto — loses every head-to-head matchup

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Ana        3  2  0  0  0  0  |    23   4.6
Beto       0  0  0  0  0  5  |     0   0.0
Cleo       2  0  3  0  0  0  |    19   3.8
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/b38b7fg_districting_north_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/districting_cost/cases/b38b7fg_districting_north.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../07_Concepts/topics/condorcet/README.md)
- [Ballot & terminology basics](../../../../07_Concepts/topics/ballot_and_terminology_basics.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [b38b7fg_districting_combined](b38b7fg_districting_combined.md) · [b38b7fg_districting_south](b38b7fg_districting_south.md)
