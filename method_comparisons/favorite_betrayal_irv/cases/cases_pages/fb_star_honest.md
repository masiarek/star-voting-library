# Favorite betrayal — the fix: STAR & Ranked Robin elect Center from the HONEST ballots

*Generated from [`fb_star_honest.yaml`](../fb_star_honest.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Center

## Scenario

The same electorate as fb_irv_honest / fb_irv_betray, scored honestly (favorite 5,
compromise 3, worst 0). No strategy: the Left voters give Left 5, Center 3, Right 0.
STAR elects CENTER — the Condorcet winner — with no betrayal required (scoring round
Center 120, Right 80; runoff Center 21-13). The [Divergence from STAR] block confirms
the contrast on these very ballots: STAR = Center, Ranked Robin = Center, but
RCV-IRV = Right. That is the whole lesson: under RCV-IRV the Left voters had to rank
their favorite second to get a good outcome (fb_irv_betray); under STAR and Ranked
Robin they simply vote their honest preferences and the compromise wins. Honesty is
the best ballot. Concept: favorite_betrayal_voting_301.md.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:Left,Center,Right
12:5,3,0   # Left > Center > Right   (honest — favorite 5, compromise 3, worst 0)
4:3,5,0    # Center > Left > Right
5:0,5,3    # Center > Right > Left
13:0,3,5   # Right > Center > Left
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR                   = Center
  Choose-One (Plurality) = Right   (differs from STAR)
  RCV-IRV                = Right   (differs from STAR)
  Note: no ballots had tied scores, so RCV-IRV vs STAR here is a genuine
        method difference, not a tie-breaking artifact.
  Note: Ranked Robin (RCV-RR) agrees with STAR, so RCV-IRV is the lone
        outlier — the classic center-squeeze signature.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: cases_tabulated/fb_star_honest_RCV-IRV_tabulated.txt

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 34 ballots.
Count × Left,Center,Right
   13 ×    0,     3,    5
   12 ×    5,     3,    0
    5 ×    0,     5,    3
    4 ×    3,     5,    0

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Center        -- 120 -- First place
   Right         --  80 -- Second place
   Left          --  72
 Center and Right advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Center        -- 21 -- First place
   Right         -- 13
   Equal Support --  0
 Center wins.
   Runoff math:
     34  ballots cast
   −  0  Equal Support (no preference between the two finalists)
     ──
     34  voters with a preference  (majority = 18)
           Center 21 (62%)  ·  Right 13 (38%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Center
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |      Left    |  * Center   |  * Right    |
-------------------------------------------------------------
          Left > |     ---      |12 -  0 - 22 |16 -  0 - 18 |
      * Center > | 22 -  0 - 12 |    ---      |21 -  0 - 13 |
       * Right > | 18 -  0 - 16 |13 -  0 - 21 |    ---      |

[Condorcet Winner]
  Condorcet Winner: Center — matches the STAR winner

[Score Distribution] (how many ballots gave each star rating)
                   Score
Candidate   5   4   3   2   1   0  | Total   Avg
Left       12   0   4   0   0  18  |    72   2.1
Center      9   0  25   0   0   0  |   120   3.5
Right      13   0   5   0   0  16  |    80   2.4
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/fb_star_honest_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/favorite_betrayal_irv/cases/fb_star_honest.yaml
```

## See also

- [Methods disagree on this election](../../../divergence_review/cases/IRV_OUTLIER_RR_WITH_STAR/fb_star_honest.md) — its entry in the divergence review ledger
- [Condorcet efficiency (topic hub)](../../../../00_start_here/topics/condorcet/README.md)
- [Runoff reversal (worked set)](../../../../01_STAR/runoff_overturns_leader/README.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [fb_irv_betray](fb_irv_betray.md) · [fb_irv_honest](fb_irv_honest.md)
