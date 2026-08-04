---
search:
  exclude: true
---

# Hillinger Table 4, rescaled — what 'cardinal' actually guarantees

*Generated from [`hillinger_t4_affine.yaml`](../hillinger_t4_affine.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../../01_STAR/01_Learn) · **1 seat** · **Expected winner:** Ana

## Scenario

The SAME 30 voters and the SAME opinions as hillinger_t4_ev3.yaml, with every
score put through the positive affine transformation u' = 2u + 1. Hillinger's
EV-3 marks (0, 1, 2) become (1, 3, 5).

This is the definition of a cardinal scale made runnable. A utility scale is
called CARDINAL when it is unique up to a positive affine transformation —
meaning you may slide the origin and stretch the unit freely, and every
question the scale is entitled to answer keeps the same answer. Hillinger
makes the point in §5 ("The choice of x0 does not affect the outcome") and
again in §6, where he notes that the scales of the physical sciences are
arbitrary up to a linear transformation in exactly this way — "Only, when
adding different measurements, we must use the same scale!"

So compare the two runs. The totals move: Ana 39 -> 108, Bruno 29 -> 88,
Chloe 22 -> 74 (each total is 2x the old one plus 30, one point per ballot).
Nothing that decides the election moves: the same two finalists, the same
winner, the same runoff margin, the same ordering.

The caveat is the one Hillinger flags with an exclamation mark, and it is the
live objection to every score method: the invariance holds because EVERY voter
was rescaled together. Let two voters use different scales and the sum is no
longer a rescaling of anything — it is a different election. That is the
interpersonal-comparability problem, and it is not solved by this file.

Concept page: 07_Concepts/topics/cardinal_utility.md

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:Ana,Bruno,Chloe
9:5,3,1    # Ana > Bruno > Chloe
10:3,5,1   # Bruno > Ana > Chloe
11:3,1,5   # Chloe > Ana > Bruno
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
  RCV-IRV rounds: cases_tabulated/hillinger_t4_affine_RCV-IRV_tabulated.txt

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 30 ballots.
Count × Ana,Bruno,Chloe
   11 ×   3,    1,    5
   10 ×   3,    5,    1
    9 ×   5,    3,    1

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Ana           -- 108 -- First place
   Bruno         --  88 -- Second place
   Chloe         --  74
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
Ana         9   0  21   0   0   0  |   108   3.6
Bruno      10   0   9   0  11   0  |    88   2.9
Chloe      11   0   0   0  19   0  |    74   2.5
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/hillinger_t4_affine_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/hillinger_evaluative_voting/cases/hillinger_t4_affine.yaml
```

## See also

- [Runoff reversal (worked set)](../../../../01_STAR/02_Examples/runoff_overturns_leader/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [hillinger_t4_ev3](hillinger_t4_ev3.md)
