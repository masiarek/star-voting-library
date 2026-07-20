# Pineapple progression (1/3) — 34% wins Choose-One, but Cheese is the real choice

*Generated from [`pineapple_34pct.yaml`](../pineapple_34pct.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Cheese

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/ht2c3g) · **[results ↗](https://bettervoting.com/ht2c3g/results)** (election `ht2c3g`).

## Scenario

Rung 1 of the pineapple progression. A group shares ONE pizza. Three toppings on
the menu: Pineapple and Anchovy each have a passionate fan club; plain Cheese is
nobody's *favorite* but everybody's easy second — put it on and no one complains.
Under Choose-One (mark your one favorite), the biggest fan club wins: Pineapple
takes it with 34% — even though 65 of 99 diners would happily eat Cheese and only
34 actually want Pineapple. STAR, Ranked Robin, and Approval all read the whole
ballot and pick Cheese, the Condorcet winner (it beats every topping head-to-head).
Next rung adds a topping and the winner's share shrinks. Lesson: README.md

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:Pineapple,Anchovy,Mushroom,Cheese
34:5,0,0,4
33:0,5,0,4
32:0,0,5,4
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
  RCV-IRV rounds: cases_tabulated/pineapple_34pct_RCV-IRV_tabulated.txt

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 99 ballots.
Count × Pineapple,Anchovy,Mushroom,Cheese
   34 ×         5,      0,       0,     4
   33 ×         0,      5,       0,     4
   32 ×         0,      0,       5,     4

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Cheese        -- 396 -- First place
   Pineapple     -- 170 -- Second place
   Anchovy       -- 165
   Mushroom      -- 160
 Cheese and Pineapple advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Cheese        -- 65 -- First place
   Pineapple     -- 34
   Equal Support --  0
 Cheese wins.
   Runoff math:
     99  ballots cast
   −  0  Equal Support (no preference between the two finalists)
     ──
     99  voters with a preference  (majority = 50)
           Cheese 65 (66%)  ·  Pineapple 34 (34%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Cheese
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                  |  * Pineapple  |    Anchovy   |   Mushroom   |  * Cheese    |
--------------------------------------------------------------------------------
    * Pineapple > |      ---      |34 - 32 - 33  |34 - 33 - 32  |34 -  0 - 65  |
        Anchovy > | 33 - 32 - 34  |     ---      |33 - 34 - 32  |33 -  0 - 66  |
       Mushroom > | 32 - 33 - 34  |32 - 34 - 33  |     ---      |32 -  0 - 67  |
       * Cheese > | 65 -  0 - 34  |66 -  0 - 33  |67 -  0 - 32  |     ---      |

[Condorcet Winner]
  Condorcet Winner: Cheese — matches the STAR winner

[Score Distribution] (how many ballots gave each star rating)
                   Score
Candidate   5   4   3   2   1   0  | Total   Avg
Pineapple  34   0   0   0   0  65  |   170   1.7
Anchovy    33   0   0   0   0  66  |   165   1.7
Mushroom   32   0   0   0   0  67  |   160   1.6
Cheese      0  99   0   0   0   0  |   396   4.0
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/pineapple_34pct_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/minority_winner_progression/cases/pineapple_34pct.yaml
```

## See also

- [Methods disagree on this election](../../../divergence_review/cases/IRV_OUTLIER_RR_WITH_STAR/pineapple_34pct.md) — its entry in the divergence review ledger
- [Condorcet efficiency (topic hub)](../../../../00_start_here/topics/condorcet/README.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [pineapple_11pct](pineapple_11pct.md) · [pineapple_25pct](pineapple_25pct.md)
