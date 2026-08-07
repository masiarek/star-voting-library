---
search:
  exclude: true
---

# The smallest divergence — Bloc STAR

*Generated from [`min_bloc_c3_b2.yaml`](../min_bloc_c3_b2.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Bloc STAR (multi-winner, majoritarian)](../../../../03_STAR_PR/01_Learn/README.md) · **2 seats** · **Expected winners:** Ana, Ben

## Scenario

Two voters, three candidates, two seats — the smallest election in which Bloc STAR and Proportional STAR (Allocated Score) fill the council differently. Identical ballots to min_pr_c3_b2.yaml; only the count differs. Both methods agree that Ben takes the first seat. They disagree about the second, and the reason is the whole difference between the two methods: Bloc lets the voter who already got Ben pick the second seat too, while Proportional STAR considers that voter represented and hands the second seat to the voter who has nobody yet.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Ana,Ben,Cleo
0,0,1   # Voter 1 — likes only Cleo, and only mildly
2,3,0   # Voter 2 — prefers Ben, then Ana
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
--- Bloc STAR Voting Method (2 winners) ---

[Bloc STAR]
 Tabulating 2 ballots to fill 2 seats.
Ana,Ben,Cleo
  0,  0,   1
  2,  3,   0

[Bloc STAR: Round 1: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Ben           -- 3 -- First place
   Ana           -- 2 -- Second place
   Cleo          -- 1
 Ben and Ana advance.

[Bloc STAR: Round 1: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Ben           -- 1 -- First place
   Ana           -- 0
   Equal Support -- 1
 Ben wins.
   Runoff math:
     2  ballots cast
   − 1  Equal Support (no preference between the two finalists)
     ─
     1  voters with a preference  (majority = 1)
           Ben 1 (100%)  ·  Ana 0 (0%)

──────────────────────────────────────────────────

[Bloc STAR: Round 2: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Ana           -- 2 -- First place
   Cleo          -- 1 -- Second place
 Ana and Cleo advance.

[Bloc STAR: Round 2: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Ana           -- 1 -- Tied for first place
   Cleo          -- 1 -- Tied for first place
   Equal Support -- 0
 There's a two-way tie for first.

[Bloc STAR: Round 2: Automatic Runoff Round: First tiebreaker]
 The highest-scoring candidate wins.
   Ana           -- 2 -- First place
   Cleo          -- 1
 Ana wins.

[Bloc STAR: Winners — Bloc STAR Voting Method (2 winners)]
 Ben
 Ana
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |   * Ana    |  * Ben    |    Cleo   |
-----------------------------------------------------
       * Ana > |    ---     |0 - 1 - 1  |1 - 0 - 1  |
       * Ben > | 1 - 1 - 0  |   ---     |1 - 0 - 1  |
        Cleo > | 1 - 0 - 1  |1 - 0 - 1  |   ---     |

[Condorcet Winner]
  No strict Condorcet winner; unbeaten candidates: Ben, Cleo (pairwise ties)

[Condorcet Loser]
  No strict Condorcet loser; jointly weak Condorcet losers: Ana, Cleo (winless — pairwise ties)

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Ana        0  0  0  1  0  1  |     2   1.0
Ben        0  0  1  0  0  1  |     3   1.5
Cleo       0  0  0  0  1  1  |     1   0.5
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/min_bloc_c3_b2_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/bloc_vs_pr/cases/min_bloc_c3_b2.yaml
```

## See also

- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [min_pr_c3_b2](min_pr_c3_b2.md)
