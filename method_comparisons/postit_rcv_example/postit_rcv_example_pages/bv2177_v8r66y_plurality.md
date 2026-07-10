# The Post-it election, seven ways — Choose-One: Purple on 7 first choices

*Generated from [`bv2177_v8r66y_plurality.yaml`](../bv2177_v8r66y_plurality.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [plurality](../../../00_start_here) · **1 seat** · **Expected winner:** Purple

## Scenario

One of seven races in the Post-it seven-ways election (BV2177, bvid v8r66y;
BV-confirmed) — the BV2176 electorate from Equal Vote's video "Updated: How
does RCV work? — With Post-its!" (https://youtu.be/Vte4nly_Neg), run through
every method BetterVoting supports. This race keeps only each voter's first
choice: Purple 7, Green 6, Blue 4, Pink 3 — Purple wins with 35% of the
vote, seeing nothing of the 13 voters who put Purple last-or-unranked.
Identical to RCV-IRV's round 1 (and RCV-IRV lands on Purple here too, so on
this electorate the "instant runoff" changed nothing about the winner —
only about the margin story). See the fairness lesson page:
postit_video_fair_and_balanced.md.

Live results: https://bettervoting.com/v8r66y/results
Companion races: BV2176's bv2176_p8dp28_star.yaml / _irv.yaml /
_ranked_robin.yaml (identical ballots to the BV2177 STAR/IRV/RR/STV races)
and bv2177_v8r66y_approval.yaml.
Overview page: bv2177_v8r66y_seven_methods.md

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Purple,Green,Blue,Pink
1,0,0,0
1,0,0,0
1,0,0,0
1,0,0,0
1,0,0,0
1,0,0,0
1,0,0,0
0,1,0,0
0,1,0,0
0,1,0,0
0,1,0,0
0,1,0,0
0,1,0,0
0,0,1,0
0,0,1,0
0,0,1,0
0,0,1,0
0,0,0,1
0,0,0,1
0,0,0,1
```

## What the engine says

Full report from the [`_tabulated` mirror](../postit_rcv_example_tabulated/bv2177_v8r66y_plurality_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |   * Purple   |  * Green    |     Blue    |     Pink    |
---------------------------------------------------------------------------
      * Purple > |     ---      | 7 -  7 -  6 | 7 -  9 -  4 | 7 - 10 -  3 |
       * Green > |  6 -  7 -  7 |    ---      | 6 - 10 -  4 | 6 - 11 -  3 |
          Blue > |  4 -  9 -  7 | 4 - 10 -  6 |    ---      | 4 - 13 -  3 |
          Pink > |  3 - 10 -  7 | 3 - 11 -  6 | 3 - 13 -  4 |    ---      |

[Condorcet Winner]
  Condorcet Winner: Purple — matches the STAR winner

--- Choose-One / Plurality Voting Method (single winner) ---
[STAR Voting]
 Tabulating 20 ballots.
Count × Purple,Green,Blue,Pink
    7 ×      1,    0,   0,   0
    6 ×      0,    1,   0,   0
    4 ×      0,    0,   1,   0
    3 ×      0,    0,   0,   1

[Score Distribution] (how many ballots gave each star rating)
                   Score
Candidate   5   4   3   2   1   0  | Total   Avg
Purple      0   0   0   0   7  13  |     7   0.4
Green       0   0   0   0   6  14  |     6   0.3
Blue        0   0   0   0   4  16  |     4   0.2
Pink        0   0   0   0   3  17  |     3   0.2

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Purple        -- 7 -- First place
   Green         -- 6 -- Second place
   Blue          -- 4
   Pink          -- 3
 Purple and Green advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Purple        -- 7 -- First place
   Green         -- 6
   Equal Support -- 7
 Purple wins.
   Runoff math:
     20  ballots cast
   −  7  Equal Support (no preference between the two finalists)
     ──
     13  voters with a preference  (majority = 7)
           Purple 7 (54%)  ·  Green 6 (46%)

[STAR Voting: Winner — Choose-One / Plurality Voting Method (single winner)]
 Purple
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/postit_rcv_example/bv2177_v8r66y_plurality.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Runoff reversal (worked set)](../../../01_STAR/runoff_overturns_leader/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [bv2176_p8dp28_irv](bv2176_p8dp28_irv.md) · [bv2176_p8dp28_ranked_robin](bv2176_p8dp28_ranked_robin.md) · [bv2176_p8dp28_star](bv2176_p8dp28_star.md) · [bv2177_v8r66y_approval](bv2177_v8r66y_approval.md) · [bv2178_8kg698_irv](bv2178_8kg698_irv.md) · [bv2178_8kg698_ranked_robin](bv2178_8kg698_ranked_robin.md) · [bv2178_8kg698_star](bv2178_8kg698_star.md)
