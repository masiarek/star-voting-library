---
search:
  exclude: true
---

# The smallest divergence — Proportional STAR (Allocated Score)

*Generated from [`min_pr_c3_b2.yaml`](../min_pr_c3_b2.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Allocated Score (proportional STAR)](../../../../03_STAR_PR/01_Learn/README.md) · **2 seats** · **Expected winners:** Ben, Cleo

## Scenario

Two voters, three candidates, two seats — the smallest election in which Bloc STAR and Proportional STAR (Allocated Score) fill the council differently. Identical ballots to min_bloc_c3_b2.yaml; only the count differs. Both methods agree that Ben takes the first seat. They disagree about the second, and the reason is the whole difference between the two methods: Bloc lets the voter who already got Ben pick the second seat too, while Proportional STAR considers that voter represented and hands the second seat to the voter who has nobody yet.

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
--- Allocated Score Voting Method (2 winners) ---

[Allocated Score Voting]
 Tabulating 2 ballots to fill 2 seats.
Ana,Ben,Cleo
  0,  0,   1
  2,  3,   0

[Allocated Score Voting: Round 1]
 The highest-scoring candidate wins a seat.
   Ben           -- 3 -- First place
   Ana           -- 2
   Cleo          -- 1
 Ben wins a seat.

[Allocated Score Voting: Round 1: Ballot allocation round]
 Allocating 1 ballots.

[Allocated Score Voting: Round 1: Ballot allocation round: Round 1]
 Allocating 1 ballot at score 3.

[Allocated Score Voting: Round 2]
 Tabulating 1 remaining ballots.
Ana,Ben,Cleo
  0,  0,   1
  2,  3,   0

[Allocated Score Voting: Winners — Allocated Score Voting Method (2 winners)]
 Ben
 Cleo
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
 Hare quota is 1.

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Ana        0  0  0  1  0  1  |     2   1.0
Ben        0  0  1  0  0  1  |     3   1.5
Cleo       0  0  0  0  1  1  |     1   0.5
 The highest-scoring candidate wins a seat.
   Cleo          -- 1 -- First place
   Ana           -- 0
 Cleo wins a seat.
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/min_pr_c3_b2_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/bloc_vs_pr/cases/min_pr_c3_b2.yaml
```

## See also

- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [min_bloc_c3_b2](min_bloc_c3_b2.md)
