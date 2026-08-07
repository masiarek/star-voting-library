---
search:
  exclude: true
---

# Crowded field, rung 3 — 3 candidates, 65 voters, counted by STAR

*Generated from [`crowded_field_c3_star.yaml`](../crowded_field_c3_star.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../../01_STAR/01_Learn/README.md) · **1 seat** · **Expected winner:** Diego

**Official tie-break (lot) order:** Ana > Diego > Greta — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

RUNG 1 of the crowded-field ladder — three candidates, and all six methods agree.

Diego stands at 11 on a 0–24 spectrum, near the middle of where the voters are. He
beats both rivals head-to-head, so he is the Condorcet winner; he leads the scoring
round 266 to Greta's 123 and Ana's 119, and takes the runoff 50–15 with nobody
undecided. He even holds an outright majority of first choices, 34 of 65.

Ranked Robin, Score, Approval, RCV-IRV and Choose-One elect him too. That is the point
of this rung: with a small field there is nothing to argue about, so any disagreement
further up the ladder was caused by the candidates who joined — the voters never move.

Construction: build_ladder.py in this folder. 65 voters in seven blocs at 0, 4, 8, 12,
16, 20, 24 (sizes 6, 10, 13, 9, 12, 8, 7); candidates fixed at Ana 1 · Bruno 6 ·
Clara 9 · Diego 11 · Elsa 14 · Felix 16 · Greta 22; utility = minus distance; scores =
each bloc's own min-max scaling onto 0–5. Nothing is tuned, and no count at any rung is
settled by a tie-break.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:Ana,Diego,Greta
6:5,3,0    # bloc at 0
10:5,4,0    # bloc at 4
13:3,5,0    # bloc at 8
9:0,5,0    # bloc at 12
12:0,5,4    # bloc at 16
8:0,3,5    # bloc at 20
7:0,2,5    # bloc at 24
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 65 ballots.
Count × Ana,Diego,Greta
   13 ×   3,    5,    0
   12 ×   0,    5,    4
   10 ×   5,    4,    0
    9 ×   0,    5,    0
    8 ×   0,    3,    5
    7 ×   0,    2,    5
    6 ×   5,    3,    0

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Diego         -- 266 -- First place
   Greta         -- 123 -- Second place
   Ana           -- 119
 Diego and Greta advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Diego         -- 50 -- First place
   Greta         -- 15
   Equal Support --  0
 Diego wins.
   Runoff math:
     65  ballots cast
   −  0  Equal Support (no preference between the two finalists)
     ──
     65  voters with a preference  (majority = 33)
           Diego 50 (77%)  ·  Greta 15 (23%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Diego
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |      Ana     |  * Diego    |  * Greta    |
-------------------------------------------------------------
           Ana > |     ---      |16 -  0 - 49 |29 -  9 - 27 |
       * Diego > | 49 -  0 - 16 |    ---      |50 -  0 - 15 |
       * Greta > | 27 -  9 - 29 |15 -  0 - 50 |    ---      |

[Condorcet Winner]
  Condorcet Winner: Diego — matches the STAR winner

[Condorcet Loser]
  Condorcet Loser: Greta — loses every head-to-head matchup

[Score Distribution] (how many ballots gave each star rating)
                   Score
Candidate   5   4   3   2   1   0  | Total   Avg
Ana        16   0  13   0   0  36  |   119   1.8
Diego      34  10  14   7   0   0  |   266   4.1
Greta      15  12   0   0   0  38  |   123   1.9
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/crowded_field_c3_star_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/crowded_field/cases/crowded_field_c3_star.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../07_Concepts/topics/condorcet/README.md)
- [Ties & tie-breaking (topic hub)](../../../../07_Concepts/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)
- [Runoff reversal (worked set)](../../../../01_STAR/02_Examples/runoff_overturns_leader/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [crowded_field_c3_approval](crowded_field_c3_approval.md) · [crowded_field_c3_irv](crowded_field_c3_irv.md) · [crowded_field_c3_ranked_robin](crowded_field_c3_ranked_robin.md) · [crowded_field_c5_approval](crowded_field_c5_approval.md) · [crowded_field_c5_irv](crowded_field_c5_irv.md) · [crowded_field_c5_ranked_robin](crowded_field_c5_ranked_robin.md) · [crowded_field_c5_star](crowded_field_c5_star.md) · [crowded_field_c7_approval](crowded_field_c7_approval.md) · [crowded_field_c7_irv](crowded_field_c7_irv.md) · [crowded_field_c7_ranked_robin](crowded_field_c7_ranked_robin.md) · [crowded_field_c7_star](crowded_field_c7_star.md)
