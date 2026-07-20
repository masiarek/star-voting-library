# The same overturn at scale — 67% to 33%

*Generated from [`01b_c3_b9_overturn-holds-at-scale.yaml`](../01b_c3_b9_overturn-holds-at-scale.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Brownie

## Scenario

Same election as 01a, just more voters — proof the three-person version wasn't a
fluke. Three Almond superfans (5 stars) against six who prefer Brownie. Almond
still leads the scoring round (39 to 33), and Brownie still wins the automatic
runoff — now 6-3, a clean 67% to 33%. The pattern doesn't depend on small numbers.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Almond, Brownie, Cocoa
     5,       1,     0
     5,       1,     0
     5,       1,     0
     4,       5,     0
     4,       5,     0
     4,       5,     0
     4,       5,     0
     4,       5,     0
     4,       5,     0
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR     = Brownie
  Approval = Almond   (differs from STAR)

[Runoff Reversal]
 - Score Round Winner(s) = (Almond)
 - Runoff Round Winner   = (Brownie)
  Candidate Almond earned the highest total score, but
  Candidate Brownie won the automatic runoff — not a malfunction,
  STAR working as designed: the runoff elects the finalist preferred
  by the majority (of voters with a preference).

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 9 ballots.
Count × Almond,Brownie,Cocoa
    6 ×      4,      5,    0
    3 ×      5,      1,    0

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Almond        -- 39 -- First place
   Brownie       -- 33 -- Second place
   Cocoa         --  0
 Almond and Brownie advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Brownie       -- 6 -- First place
   Almond        -- 3
   Equal Support -- 0
 Brownie wins.
   Runoff math:
     9  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     9  voters with a preference  (majority = 5)
           Brownie 6 (67%)  ·  Almond 3 (33%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Brownie
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                |  * Almond   | * Brownie  |    Cocoa   |
---------------------------------------------------------
     * Almond > |     ---     | 3 - 0 - 6  | 9 - 0 - 0  |
    * Brownie > |  6 - 0 - 3  |    ---     | 9 - 0 - 0  |
        Cocoa > |  0 - 0 - 9  | 0 - 0 - 9  |    ---     |

[Condorcet Winner]
  Condorcet Winner: Brownie — matches the STAR winner

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Almond     3  6  0  0  0  0  |    39   4.3
Brownie    6  0  0  0  3  0  |    33   3.7
Cocoa      0  0  0  0  0  9  |     0   0.0
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/01b_c3_b9_overturn-holds-at-scale_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/runoff_overturns_leader/cases/01b_c3_b9_overturn-holds-at-scale.yaml
```

## See also

- [Methods disagree on this election](../../../../method_comparisons/divergence_review/cases/APPROVAL_OR_MINOR/01b_c3_b9_overturn-holds-at-scale.md) — its entry in the divergence review ledger
- [Runoff reversal (worked set)](../../README.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [01a_c3_b3_more-stars-fewer-voters](01a_c3_b3_more-stars-fewer-voters.md) · [02_c5_b5_leader-overturned](02_c5_b5_leader-overturned.md) · [03_c7_b3_ice-cream-live](03_c7_b3_ice-cream-live.md) · [04_c4_b3_runoff-confirms-leader](04_c4_b3_runoff-confirms-leader.md) · [05_c3_b5_low-scores-bv1265](05_c3_b5_low-scores-bv1265.md) · [reversal_convincing_c3_b100](reversal_convincing_c3_b100.md) · [reversal_jarring_c3_b100](reversal_jarring_c3_b100.md)
