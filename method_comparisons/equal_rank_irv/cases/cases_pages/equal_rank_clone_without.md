---
search:
  exclude: true
---

# Equal ranks — Costa withdraws, and Split-IRV's winner flips to Alma

*Generated from [`equal_rank_clone_without.yaml`](../equal_rank_clone_without.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../../01_STAR/01_Learn/README.md) · **1 seat** · **Expected winner:** Alma

## Scenario

The clone-free half of Figure 9 from Théo Delemazure & Dominik Peters, "Generalizing Instant Runoff Voting to Allow Indifferences" (EC'24, arXiv:2404.11407). Same 45 voters, same cast, same ballots as equal_rank_clone_with.yaml with exactly one change: Costa is not running. Same cast because it is the same election with one thing changed.
With the clone gone, Split-IRV elects Alma; with the clone in the race it elects the Chen/Costa ticket. Nothing about how anyone feels changed — only how many names their top preference was spread across. That flip is Split-IRV failing independence of clones, the axiom Tideman proved ordinary strict-ballot IRV satisfies and that gives instant runoff its main claim over Choose-One voting. Approval-IRV keeps the axiom (Theorem 3.2) and elects Alma in both files.
STAR elects Alma here and in the companion file, so the clone is inert for STAR too — worth stating plainly rather than claiming: a score ballot already lets a voter rate two allies identically, so adding one changes no total that was not already recorded.
For the Approval-IRV and Split-IRV counts run tools_adam/pref_voting_tabulation_engine/approval_irv_report.py.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:Alma,Bruno,Chen
27:5,0,5    # Alma and Chen equal-first
12:3,5,0    # Bruno first, Alma second
6:3,0,5     # Chen first, Alma second
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 45 ballots.
Count × Alma,Bruno,Chen
   27 ×    5,    0,   5
   12 ×    3,    5,   0
    6 ×    3,    0,   5

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Alma          -- 189 -- First place
   Chen          -- 165 -- Second place
   Bruno         --  60
 Alma and Chen advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Alma          -- 12 -- First place
   Chen          --  6
   Equal Support -- 27
 Alma wins.
   Runoff math:
     45  ballots cast
   − 27  Equal Support (no preference between the two finalists)
     ──
     18  voters with a preference  (majority = 10)
           Alma 12 (67%)  ·  Chen 6 (33%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Alma
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |    * Alma    |    Bruno    |   * Chen    |
-------------------------------------------------------------
        * Alma > |     ---      |33 -  0 - 12 |12 - 27 -  6 |
         Bruno > | 12 -  0 - 33 |    ---      |12 -  0 - 33 |
        * Chen > |  6 - 27 - 12 |33 -  0 - 12 |    ---      |

[Condorcet Winner]
  Condorcet Winner: Alma — matches the STAR winner

[Condorcet Loser]
  Condorcet Loser: Bruno — loses every head-to-head matchup

[Score Distribution] (how many ballots gave each star rating)
                   Score
Candidate   5   4   3   2   1   0  | Total   Avg
Alma       27   0  18   0   0   0  |   189   4.2
Bruno      12   0   0   0   0  33  |    60   1.3
Chen       33   0   0   0   0  12  |   165   3.7
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/equal_rank_clone_without_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/equal_rank_irv/cases/equal_rank_clone_without.yaml
```

## See also

- [Vote splitting (worked set)](../../../split_voting/README.md)
- [Runoff reversal (worked set)](../../../../01_STAR/02_Examples/runoff_overturns_leader/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [equal_rank_clone_with](equal_rank_clone_with.md) · [equal_rank_cohesive_consecutive](equal_rank_cohesive_consecutive.md) · [equal_rank_cohesive_wide_gaps](equal_rank_cohesive_wide_gaps.md) · [equal_rank_five_voters](equal_rank_five_voters.md) · [equal_rank_majority_alternative](equal_rank_majority_alternative.md)
