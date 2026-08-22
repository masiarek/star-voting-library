---
search:
  exclude: true
---

# Equal ranks — Costa joins Chen's ticket, and Split-IRV hands them the win

*Generated from [`equal_rank_clone_with.yaml`](../equal_rank_clone_with.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../../01_STAR/01_Learn/README.md) · **1 seat** · **Expected winner:** Alma

## Scenario

Figure 9 of Théo Delemazure & Dominik Peters, "Generalizing Instant Runoff Voting to Allow Indifferences" (EC'24, arXiv:2404.11407): the profile on which Split-IRV fails independence of clones. The paper's counts are tripled so every bloc clears the house minimum of 6; scaling every weight by the same factor leaves every winner unchanged.
Chen and Costa are perfect clones — every voter rates them identically, which is what "clone" means, and why they share an initial here. The matched file equal_rank_clone_without.yaml is the SAME election with Costa withdrawn, so the pair reads as one election with one thing changed.
Split-IRV, round 1 with Costa running: Bruno 12, Chen 12, Costa 12, Alma 9. The 27 voters who rate Alma, Chen and Costa equal-first split their one point three ways, which leaves Alma the lowest and eliminates her immediately; the clone pair goes on to win. Withdraw Costa and those same 27 voters split two ways instead: Chen 19.5, Alma 13.5, Bruno 12, so BRUNO goes out first and Alma wins the final pairing. Adding a clone of a loser changed the winner: that is exactly the spoiler effect independence of clones forbids, and Split-IRV is the generalization actually deployed in the field — the John Muir Trust and the London Mathematical Society have used it for trustee and council elections since the late 1990s.
Approval-IRV is clone-independent (Theorem 3.2) and elects Alma in both files. So does STAR: the extra identical ballot column adds nothing to the scoring round that was not already there, which is the same reason Approval-IRV survives the test.
One honest wrinkle the file shows rather than hides: perfect clones cast IDENTICAL ballots, so Chen and Costa post identical score totals and STAR's second finalist slot is a genuine tie. The runoff is unaffected — Alma beats either of them on the same ballots — but the tiebreaker banner in the report is real, not a defect in the case.
For the Approval-IRV and Split-IRV counts run tools_adam/pref_voting_tabulation_engine/approval_irv_report.py; --drop Costa reproduces the companion file's count from this one.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:Alma,Bruno,Chen,Costa
27:5,0,5,5    # Alma and the whole Chen/Costa ticket equal-first
12:3,5,0,0    # Bruno first, Alma second, the ticket last
6:3,0,5,5     # the ticket first, Alma second, Bruno last
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 45 ballots.
Count × Alma,Bruno,Chen,Costa
   27 ×    5,    0,   5,    5
   12 ×    3,    5,   0,    0
    6 ×    3,    0,   5,    5

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Alma          -- 189 -- First place
   Chen          -- 165 -- Tied for second place
   Costa         -- 165 -- Tied for second place
   Bruno         --  60
 Alma advances, but there's a two-way tie for second.

[STAR Voting: Scoring Round: First tiebreaker]
 The candidate preferred in the most head-to-head matchups advances.
   Chen          -- 0 -- Tied for second place
   Costa         -- 0 -- Tied for second place
   Equal Support -- 45
 There's still a two-way tie for second.

[STAR Voting: Scoring Round: Second tiebreaker]
 The candidate with the most votes of score 5 advances.
   Chen          -- 33 -- Tied for second place
   Costa         -- 33 -- Tied for second place
 There's still a two-way tie for second.

*** No official tie-breaking lot numbers were provided.
    Ties are resolved using a fallback order: CSV column order.
    Lot-number priority order: ['Alma', 'Bruno', 'Chen', 'Costa']

[Tiebreaker: Lot Number Priority]
  Tie among: ['Chen', 'Costa']
  Resolved: ['Chen'] (selected by lot-number priority).

[Lot-decided tie — rare]
  ⚠ The ballots did not break this tie: the deterministic rungs
    (pairwise / score, then five-star) all came back equal, so the
    pre-published LOT order chose among the tied candidates — the
    result here was set by lot, not by the votes. Usually the
    "dead rung": no tied candidate held a score-5 vote (five-star
    counts fives, not fours). Verify the tied candidates' 5-counts.

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
        Note: Chen and Costa tied at 165 in the Scoring Round, and the lot
              rung (the ballots could not separate them) advanced Chen. The *
              marks who advanced, not who scored highest.

                 |    * Alma    |    Bruno    |   * Chen    |    Costa    |
---------------------------------------------------------------------------
        * Alma > |     ---      |33 -  0 - 12 |12 - 27 -  6 |12 - 27 -  6 |
         Bruno > | 12 -  0 - 33 |    ---      |12 -  0 - 33 |12 -  0 - 33 |
        * Chen > |  6 - 27 - 12 |33 -  0 - 12 |    ---      | 0 - 45 -  0 |
         Costa > |  6 - 27 - 12 |33 -  0 - 12 | 0 - 45 -  0 |    ---      |

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
Costa      33   0   0   0   0  12  |   165   3.7
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/equal_rank_clone_with_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/equal_rank_irv/cases/equal_rank_clone_with.yaml
```

## See also

- [Ties & tie-breaking (topic hub)](../../../../07_Concepts/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)
- [Vote splitting (worked set)](../../../split_voting/README.md)
- [Runoff reversal (worked set)](../../../../01_STAR/02_Examples/runoff_overturns_leader/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [equal_rank_clone_without](equal_rank_clone_without.md) · [equal_rank_cohesive_consecutive](equal_rank_cohesive_consecutive.md) · [equal_rank_cohesive_wide_gaps](equal_rank_cohesive_wide_gaps.md) · [equal_rank_five_voters](equal_rank_five_voters.md) · [equal_rank_majority_alternative](equal_rank_majority_alternative.md)
