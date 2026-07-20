# Pineapple progression (3/3) — 11% wins Choose-One, but Cheese is the real choice

*Generated from [`pineapple_11pct.yaml`](../pineapple_11pct.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Cheese

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/h34pp9) · **[results ↗](https://bettervoting.com/h34pp9/results)** (election `h34pp9`).

## Scenario

Rung 3 — the absurd one. Ten niche toppings on the menu now, each with its own
little fan club, and Choose-One crowns Pineapple on ELEVEN percent: eleven diners
out of a hundred decide the whole pizza, and the other 89 wanted something else.
Yet nothing has really changed — plain Cheese is still everyone's easy second, the
Condorcet winner, and STAR / Ranked Robin / Approval still find it. The more crowded
the menu, the sillier Choose-One's winner looks — and the more it matters that a
method read the whole ballot. Lesson: README.md

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:Pineapple,Anchovy,Mushroom,Olive,Sausage,Spinach,Jalapeno,Onion,Pepper,Basil,Cheese
11:5,0,0,0,0,0,0,0,0,0,4
10:0,5,0,0,0,0,0,0,0,0,4
10:0,0,5,0,0,0,0,0,0,0,4
10:0,0,0,5,0,0,0,0,0,0,4
10:0,0,0,0,5,0,0,0,0,0,4
10:0,0,0,0,0,5,0,0,0,0,4
10:0,0,0,0,0,0,5,0,0,0,4
10:0,0,0,0,0,0,0,5,0,0,4
10:0,0,0,0,0,0,0,0,5,0,4
9:0,0,0,0,0,0,0,0,0,5,4
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR                   = Cheese
  Choose-One (Plurality) = Pineapple   (differs from STAR)
  RCV-IRV                = Pineapple   (differs from STAR)
  Note: no ballots had tied scores, so RCV-IRV vs STAR here is a genuine
        method difference, not a tie-breaking artifact.
  Note: Ranked Robin (RCV-RR) agrees with STAR, so RCV-IRV is the lone
        outlier — the classic center-squeeze signature.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: cases_tabulated/pineapple_11pct_RCV-IRV_tabulated.txt

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 100 ballots.
Count × Pineapple,Anchovy,Mushroom,Olive,Sausage,Spinach,Jalapeno,Onion,Pepper,Basil,Cheese
   11 ×         5,      0,       0,    0,      0,      0,       0,    0,     0,    0,     4
   10 ×         0,      5,       0,    0,      0,      0,       0,    0,     0,    0,     4
   10 ×         0,      0,       5,    0,      0,      0,       0,    0,     0,    0,     4
   10 ×         0,      0,       0,    5,      0,      0,       0,    0,     0,    0,     4
   10 ×         0,      0,       0,    0,      5,      0,       0,    0,     0,    0,     4
   10 ×         0,      0,       0,    0,      0,      5,       0,    0,     0,    0,     4
   10 ×         0,      0,       0,    0,      0,      0,       5,    0,     0,    0,     4
   10 ×         0,      0,       0,    0,      0,      0,       0,    5,     0,    0,     4
   10 ×         0,      0,       0,    0,      0,      0,       0,    0,     5,    0,     4
    9 ×         0,      0,       0,    0,      0,      0,       0,    0,     0,    5,     4

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Cheese        -- 400 -- First place
   Pineapple     --  55 -- Second place
   Anchovy       --  50
   Jalapeno      --  50
   Mushroom      --  50
   Olive         --  50
   Onion         --  50
   Pepper        --  50
   Sausage       --  50
   Spinach       --  50
   Basil         --  45
 Cheese and Pineapple advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Cheese        -- 89 -- First place
   Pineapple     -- 11
   Equal Support --  0
 Cheese wins.
   Runoff math:
     100  ballots cast
   −   0  Equal Support (no preference between the two finalists)
     ───
     100  voters with a preference  (majority = 51)
           Cheese 89 (89%)  ·  Pineapple 11 (11%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Cheese
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                  |  * Pineapple  |    Anchovy   |   Mushroom   |     Olive    |    Sausage   |    Spinach   |   Jalapeno   |     Onion    |    Pepper    |     Basil    |  * Cheese    |
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    * Pineapple > |      ---      |11 - 79 - 10  |11 - 79 - 10  |11 - 79 - 10  |11 - 79 - 10  |11 - 79 - 10  |11 - 79 - 10  |11 - 79 - 10  |11 - 79 - 10  |11 - 80 -  9  |11 -  0 - 89  |
        Anchovy > | 10 - 79 - 11  |     ---      |10 - 80 - 10  |10 - 80 - 10  |10 - 80 - 10  |10 - 80 - 10  |10 - 80 - 10  |10 - 80 - 10  |10 - 80 - 10  |10 - 81 -  9  |10 -  0 - 90  |
       Mushroom > | 10 - 79 - 11  |10 - 80 - 10  |     ---      |10 - 80 - 10  |10 - 80 - 10  |10 - 80 - 10  |10 - 80 - 10  |10 - 80 - 10  |10 - 80 - 10  |10 - 81 -  9  |10 -  0 - 90  |
          Olive > | 10 - 79 - 11  |10 - 80 - 10  |10 - 80 - 10  |     ---      |10 - 80 - 10  |10 - 80 - 10  |10 - 80 - 10  |10 - 80 - 10  |10 - 80 - 10  |10 - 81 -  9  |10 -  0 - 90  |
        Sausage > | 10 - 79 - 11  |10 - 80 - 10  |10 - 80 - 10  |10 - 80 - 10  |     ---      |10 - 80 - 10  |10 - 80 - 10  |10 - 80 - 10  |10 - 80 - 10  |10 - 81 -  9  |10 -  0 - 90  |
        Spinach > | 10 - 79 - 11  |10 - 80 - 10  |10 - 80 - 10  |10 - 80 - 10  |10 - 80 - 10  |     ---      |10 - 80 - 10  |10 - 80 - 10  |10 - 80 - 10  |10 - 81 -  9  |10 -  0 - 90  |
       Jalapeno > | 10 - 79 - 11  |10 - 80 - 10  |10 - 80 - 10  |10 - 80 - 10  |10 - 80 - 10  |10 - 80 - 10  |     ---      |10 - 80 - 10  |10 - 80 - 10  |10 - 81 -  9  |10 -  0 - 90  |
          Onion > | 10 - 79 - 11  |10 - 80 - 10  |10 - 80 - 10  |10 - 80 - 10  |10 - 80 - 10  |10 - 80 - 10  |10 - 80 - 10  |     ---      |10 - 80 - 10  |10 - 81 -  9  |10 -  0 - 90  |
         Pepper > | 10 - 79 - 11  |10 - 80 - 10  |10 - 80 - 10  |10 - 80 - 10  |10 - 80 - 10  |10 - 80 - 10  |10 - 80 - 10  |10 - 80 - 10  |     ---      |10 - 81 -  9  |10 -  0 - 90  |
          Basil > |  9 - 80 - 11  | 9 - 81 - 10  | 9 - 81 - 10  | 9 - 81 - 10  | 9 - 81 - 10  | 9 - 81 - 10  | 9 - 81 - 10  | 9 - 81 - 10  | 9 - 81 - 10  |     ---      | 9 -  0 - 91  |
       * Cheese > | 89 -  0 - 11  |90 -  0 - 10  |90 -  0 - 10  |90 -  0 - 10  |90 -  0 - 10  |90 -  0 - 10  |90 -  0 - 10  |90 -  0 - 10  |90 -  0 - 10  |91 -  0 -  9  |     ---      |

[Condorcet Winner]
  Condorcet Winner: Cheese — matches the STAR winner

[Score Distribution] (how many ballots gave each star rating)
                      Score
Candidate    5    4    3    2    1    0  | Total   Avg
Pineapple   11    0    0    0    0   89  |    55   0.6
Anchovy     10    0    0    0    0   90  |    50   0.5
Mushroom    10    0    0    0    0   90  |    50   0.5
Olive       10    0    0    0    0   90  |    50   0.5
Sausage     10    0    0    0    0   90  |    50   0.5
Spinach     10    0    0    0    0   90  |    50   0.5
Jalapeno    10    0    0    0    0   90  |    50   0.5
Onion       10    0    0    0    0   90  |    50   0.5
Pepper      10    0    0    0    0   90  |    50   0.5
Basil        9    0    0    0    0   91  |    45   0.5
Cheese       0  100    0    0    0    0  |   400   4.0
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/pineapple_11pct_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/minority_winner_progression/cases/pineapple_11pct.yaml
```

## See also

- [Methods disagree on this election](../../../divergence_review/cases/IRV_OUTLIER_RR_WITH_STAR/pineapple_11pct.md) — its entry in the divergence review ledger
- [Condorcet efficiency (topic hub)](../../../../00_start_here/topics/condorcet/README.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [pineapple_25pct](pineapple_25pct.md) · [pineapple_34pct](pineapple_34pct.md)
