# Pineapple progression (2/3) — 25% wins Choose-One, but Cheese is the real choice

*Generated from [`pineapple_25pct.yaml`](../pineapple_25pct.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Cheese

## Scenario

Rung 2 of the pineapple progression. Add a fourth topping and Choose-One gets
worse: with the fan clubs split four ways, Pineapple now wins on just 25% — a
quarter of the table picking the pizza the other three-quarters didn't ask for.
Cheese is still everybody's happy second, still the Condorcet winner, and STAR /
Ranked Robin / Approval still elect it. Same story, more toppings, smaller mandate.
Lesson: README.md

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:Pineapple,Anchovy,Mushroom,Olive,Cheese
25:5,0,0,0,4
23:0,5,0,0,4
23:0,0,5,0,4
23:0,0,0,5,4
6:0,0,0,0,5
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
  RCV-IRV rounds: minority_winner_progression_tabulated/pineapple_25pct_RCV-IRV_tabulated.txt

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 100 ballots.
Count × Pineapple,Anchovy,Mushroom,Olive,Cheese
   25 ×         5,      0,       0,    0,     4
   23 ×         0,      5,       0,    0,     4
   23 ×         0,      0,       5,    0,     4
   23 ×         0,      0,       0,    5,     4
    6 ×         0,      0,       0,    0,     5

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Cheese        -- 406 -- First place
   Pineapple     -- 125 -- Second place
   Anchovy       -- 115
   Mushroom      -- 115
   Olive         -- 115
 Cheese and Pineapple advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Cheese        -- 75 -- First place
   Pineapple     -- 25
   Equal Support --  0
 Cheese wins.
   Runoff math:
     100  ballots cast
   −   0  Equal Support (no preference between the two finalists)
     ───
     100  voters with a preference  (majority = 51)
           Cheese 75 (75%)  ·  Pineapple 25 (25%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Cheese
```

<details>
<summary>Full audit — preference matrix, Condorcet, and score distribution</summary>

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                  |  * Pineapple  |    Anchovy   |   Mushroom   |     Olive    |  * Cheese    |
-----------------------------------------------------------------------------------------------
    * Pineapple > |      ---      |25 - 52 - 23  |25 - 52 - 23  |25 - 52 - 23  |25 -  0 - 75  |
        Anchovy > | 23 - 52 - 25  |     ---      |23 - 54 - 23  |23 - 54 - 23  |23 -  0 - 77  |
       Mushroom > | 23 - 52 - 25  |23 - 54 - 23  |     ---      |23 - 54 - 23  |23 -  0 - 77  |
          Olive > | 23 - 52 - 25  |23 - 54 - 23  |23 - 54 - 23  |     ---      |23 -  0 - 77  |
       * Cheese > | 75 -  0 - 25  |77 -  0 - 23  |77 -  0 - 23  |77 -  0 - 23  |     ---      |

[Condorcet Winner]
  Condorcet Winner: Cheese — matches the STAR winner

[Score Distribution] (how many ballots gave each star rating)
                   Score
Candidate   5   4   3   2   1   0  | Total   Avg
Pineapple  25   0   0   0   0  75  |   125   1.3
Anchovy    23   0   0   0   0  77  |   115   1.2
Mushroom   23   0   0   0   0  77  |   115   1.2
Olive      23   0   0   0   0  77  |   115   1.2
Cheese      6  94   0   0   0   0  |   406   4.1
```

</details>

Everything in one file: the [`_tabulated` mirror](../minority_winner_progression_tabulated/pineapple_25pct_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/minority_winner_progression/pineapple_25pct.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README.md)
- [Vote splitting (worked set)](../../split_voting/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [pineapple_11pct](pineapple_11pct.md) · [pineapple_34pct](pineapple_34pct.md)
