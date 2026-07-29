# P3 manipulated — two voters bury their 4th choice and STAR elects their favourite

*Generated from [`p3_manip_star.yaml`](../p3_manip_star.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../../01_STAR/concepts) · **1 seat** · **Expected winner:** Edinburgh

## Scenario

STAR's turn to fail, on the same profile and cheaply. The two sincere Edinburgh>Cork>Athens>Dublin>Bergen voters score their 4th choice Dublin a 0 instead of a 2 — one number each, on one candidate, with their own favourite still a 5 and no favourite betrayal anywhere. Dublin's total drops 23 to 19, which knocks Dublin out of the finalists entirely; the runoff becomes Edinburgh vs Cork and Edinburgh wins 5-2. The two manipulators have replaced Dublin with Edinburgh, their FAVOURITE. This is burial, and it is the honest counterweight to the Copeland and Borda manipulations on this page: Gibbard-Satterthwaite guarantees every reasonable method is manipulable, and that includes both methods this library advocates.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Athens,Bergen,Cork,Dublin,Edinburgh
2:3,0,4,0,5
3:0,3,2,5,4
2:5,4,3,2,0
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR                   = Edinburgh
  Choose-One (Plurality) = Dublin   (differs from STAR)
  RCV-IRV                = Dublin   (differs from STAR)
  Approval               = Bergen   (differs from STAR)
  Note: no ballots had tied scores, so RCV-IRV vs STAR here is a genuine
        method difference, not a tie-breaking artifact.
  Note: Ranked Robin (RCV-RR) agrees with STAR, so RCV-IRV is the lone
        outlier — the classic center-squeeze signature.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: cases_tabulated/p3_manip_star_RCV-IRV_tabulated.txt

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 7 ballots.
Count × Athens,Bergen,Cork,Dublin,Edinburgh
    3 ×      0,     3,   2,     5,        4
    2 ×      3,     0,   4,     0,        5
    2 ×      5,     4,   3,     2,        0

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Edinburgh     -- 22 -- First place
   Cork          -- 20 -- Second place
   Dublin        -- 19
   Bergen        -- 17
   Athens        -- 16
 Edinburgh and Cork advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Edinburgh     -- 5 -- First place
   Cork          -- 2
   Equal Support -- 0
 Edinburgh wins.
   Runoff math:
     7  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     7  voters with a preference  (majority = 4)
           Edinburgh 5 (71%)  ·  Cork 2 (29%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Edinburgh
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                  |     Athens    |    Bergen    |   * Cork     |    Dublin    | * Edinburgh  |
-----------------------------------------------------------------------------------------------
         Athens > |      ---      |  4 - 0 - 3   |  2 - 0 - 5   |  4 - 0 - 3   |  2 - 0 - 5   |
         Bergen > |   3 - 0 - 4   |     ---      |  5 - 0 - 2   |  2 - 2 - 3   |  2 - 0 - 5   |
         * Cork > |   5 - 0 - 2   |  2 - 0 - 5   |     ---      |  4 - 0 - 3   |  2 - 0 - 5   |
         Dublin > |   3 - 0 - 4   |  3 - 2 - 2   |  3 - 0 - 4   |     ---      |  5 - 0 - 2   |
    * Edinburgh > |   5 - 0 - 2   |  5 - 0 - 2   |  5 - 0 - 2   |  2 - 0 - 5   |     ---      |

[Condorcet Winner]
  No Condorcet winner (majority cycle: Athens > Bergen > Cork > Athens)

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Athens     2  0  2  0  0  3  |    16   2.3
Bergen     0  2  3  0  0  2  |    17   2.4
Cork       0  2  2  3  0  0  |    20   2.9
Dublin     3  0  0  2  0  2  |    19   2.7
Edinburgh  2  3  0  0  0  2  |    22   3.1
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/p3_manip_star_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/manipulability_p3/cases/p3_manip_star.yaml
```

## See also

- [Methods disagree on this election](../../../divergence_review/cases/CYCLE_OR_THREE_WAY/p3_manip_star.md) — its entry in the divergence review ledger
- [Runoff reversal (worked set)](../../../../01_STAR/runoff_overturns_leader/README.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [p3_manip_compromise_rr](p3_manip_compromise_rr.md) · [p3_manip_reversal_rr](p3_manip_reversal_rr.md) · [p3_sincere_ranked_robin](p3_sincere_ranked_robin.md) · [p3_sincere_star](p3_sincere_star.md)
