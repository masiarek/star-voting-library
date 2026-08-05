---
search:
  exclude: true
---

# Hillinger Table 4 — three methods, three winners (EV-3 scale)

*Generated from [`hillinger_t4_ev3.yaml`](../hillinger_t4_ev3.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../../01_STAR/01_Learn) · **1 seat** · **Expected winner:** Ana

## Scenario

Claude Hillinger's own worked example, run through the engine. In "Voting and
the Cardinal Aggregation of Judgments" (Munich Discussion Paper 2004-9, §12,
Table 4) he uses this 30-voter profile to show what he calls the MIRROR
PATHOLOGY of STV/IRV: where plurality's famous defect is that an unpopular
candidate may win, IRV's is that the MOST popular candidate may be eliminated
in the very first round.

Ana is ranked first by the fewest voters (9) but is never ranked last by
anyone. She is the Condorcet winner (beats Bruno 20-10, beats Chloe 19-11) and
she wins the cardinal count. IRV eliminates her first anyway, and her ballots
transfer to Bruno.

The scores are Hillinger's EV-3 ballot shifted onto this repo's 0-5 scale:
his (-1, 0, +1) written as (0, 1, 2). He states explicitly that the choice of
origin does not affect the outcome (§5), and the matched file
hillinger_t4_affine.yaml checks that claim by rescaling to (1, 3, 5).
Score totals here reproduce his table exactly: Ana 39, Bruno 29, Chloe 22.

What the engine adds to the paper: Hillinger only reports the STV failure, but
the same 30 ballots split THREE ways. Plurality elects Chloe (11 first
choices), RCV-IRV elects Bruno, and STAR / Score / Condorcet all elect Ana.
One electorate, one set of opinions, three different winners.

Concept page: 07_Concepts/topics/cardinal_utility.md

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:Ana,Bruno,Chloe
9:2,1,0    # Ana > Bruno > Chloe
10:1,2,0   # Bruno > Ana > Chloe
11:1,0,2   # Chloe > Ana > Bruno
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
[Divergence from STAR]
  STAR                   = Ana
  Choose-One (Plurality) = Chloe   (differs from STAR)
  RCV-IRV                = Bruno   (differs from STAR)
  Note: no ballots had tied scores, so RCV-IRV vs STAR here is a genuine
        method difference, not a tie-breaking artifact.
  Note: Ranked Robin (RCV-RR) agrees with STAR, so RCV-IRV is the lone
        outlier — the classic center-squeeze signature.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: cases_tabulated/hillinger_t4_ev3_RCV-IRV_tabulated.txt

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 30 ballots.
Count × Ana,Bruno,Chloe
   11 ×   1,    0,    2
   10 ×   1,    2,    0
    9 ×   2,    1,    0

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Ana           -- 39 -- First place
   Bruno         -- 29 -- Second place
   Chloe         -- 22
 Ana and Bruno advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Ana           -- 20 -- First place
   Bruno         -- 10
   Equal Support --  0
 Ana wins.
   Runoff math:
     30  ballots cast
   −  0  Equal Support (no preference between the two finalists)
     ──
     30  voters with a preference  (majority = 16)
           Ana 20 (67%)  ·  Bruno 10 (33%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Ana
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |    * Ana     |  * Bruno    |    Chloe    |
-------------------------------------------------------------
         * Ana > |     ---      |20 -  0 - 10 |19 -  0 - 11 |
       * Bruno > | 10 -  0 - 20 |    ---      |19 -  0 - 11 |
         Chloe > | 11 -  0 - 19 |11 -  0 - 19 |    ---      |

[Condorcet Winner]
  Condorcet Winner: Ana — matches the STAR winner

[Condorcet Loser]
  Condorcet Loser: Chloe — loses every head-to-head matchup — elected by Choose-One (Plurality)!

[Score Distribution] (how many ballots gave each star rating)
                   Score
Candidate   5   4   3   2   1   0  | Total   Avg
Ana         0   0   0   9  21   0  |    39   1.3
Bruno       0   0   0  10   9  11  |    29   1.0
Chloe       0   0   0  11   0  19  |    22   0.7
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/hillinger_t4_ev3_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/hillinger_evaluative_voting/cases/hillinger_t4_ev3.yaml
```

## See also

- [Methods disagree on this election](../../../divergence_review/cases/IRV_OUTLIER_RR_WITH_STAR/hillinger_t4_ev3.md) — its entry in the divergence review ledger
- [Condorcet efficiency (topic hub)](../../../../07_Concepts/topics/condorcet/README.md)
- [Vote splitting (worked set)](../../../split_voting/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [hillinger_t4_affine](hillinger_t4_affine.md)
