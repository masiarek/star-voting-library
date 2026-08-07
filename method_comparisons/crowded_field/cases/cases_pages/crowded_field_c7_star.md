---
search:
  exclude: true
---

# Crowded field, rung 7 — 7 candidates, 65 voters, counted by STAR

*Generated from [`crowded_field_c7_star.yaml`](../crowded_field_c7_star.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../../01_STAR/01_Learn/README.md) · **1 seat** · **Expected winner:** Clara

**Official tie-break (lot) order:** Ana > Bruno > Clara > Diego > Elsa > Felix > Greta — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

RUNG 3 — seven candidates, and the score ballot runs out of room.

Clara (9) and Felix (16) join, one on each side again, both closer in than the last
pair. Diego STILL beats every one of the other six head-to-head — six wins out of six,
the Condorcet winner for the third rung running, and Ranked Robin returns him
(crowded_field_c7_ranked_robin.yaml).

STAR does not. Clara, standing two steps from Diego, edges him in the scoring round
225 to 219. Both reach the runoff — so this is NOT the top-two rule discarding anyone,
the mechanism people usually reach for — and Clara wins it 23–17, with **25 of the 65
voters expressing no preference at all** between the two. That is the lesson in one
line: seven candidates on a six-rung ballot (0–5) leaves little room to separate two
candidates standing near each other, so a preference that is perfectly real on the
spectrum is not on the paper.

Read the pairwise matrix against the score totals. Diego wins every column and loses
the election. On the ranked ballots of the same voters he beats Clara 36–29
(crowded_field_c7_ranked_robin.yaml); on this 0–5 ballot that margin has been rounded
away.

One warning about this file's [Divergence from STAR] block: it converts scores to ranks
to guess at RCV-IRV and Choose-One, and the engine's own note says how many ballots
carry tied scores. Take those two results from crowded_field_c7_irv.yaml instead, where
the ballots are real rankings.

Construction: build_ladder.py in this folder. 65 voters in seven blocs at 0, 4, 8, 12,
16, 20, 24 (sizes 6, 10, 13, 9, 12, 8, 7); candidates fixed at Ana 1 · Bruno 6 ·
Clara 9 · Diego 11 · Elsa 14 · Felix 16 · Greta 22; utility = minus distance; scores =
each bloc's own min-max scaling onto 0–5. Nothing is tuned, and no count at any rung is
settled by a tie-break.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:Ana,Bruno,Clara,Diego,Elsa,Felix,Greta
6:5,4,3,3,2,1,0    # bloc at 0
10:5,5,4,3,2,2,0    # bloc at 4
13:3,5,5,4,3,2,0    # bloc at 8
9:0,2,4,5,4,4,0    # bloc at 12
12:0,2,3,3,4,5,3    # bloc at 16
8:0,1,2,3,4,4,5    # bloc at 20
7:0,1,2,2,3,4,5    # bloc at 24
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
[Divergence from STAR]
  STAR                   = Clara
  Choose-One (Plurality) = Ana   (differs from STAR)
  RCV-IRV                = Felix   (differs from STAR)
  Approval               = Diego   (differs from STAR)
  Note: 65 of 65 ballots (100%) had equal non-zero scores, so their ranks
        were decided by candidate priority order. The RCV-IRV result may be
        an artifact of score-to-rank tie-breaking rather than a deep
        difference.
  Note: Ranked Robin (RCV-RR) agrees with STAR, so RCV-IRV is the lone
        outlier — the classic center-squeeze signature.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: cases_tabulated/crowded_field_c7_star_RCV-IRV_tabulated.txt

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 65 ballots.
Count × Ana,Bruno,Clara,Diego,Elsa,Felix,Greta
   13 ×   3,    5,    5,    4,   3,    2,    0
   12 ×   0,    2,    3,    3,   4,    5,    3
   10 ×   5,    5,    4,    3,   2,    2,    0
    9 ×   0,    2,    4,    5,   4,    4,    0
    8 ×   0,    1,    2,    3,   4,    4,    5
    7 ×   0,    1,    2,    2,   3,    4,    5
    6 ×   5,    4,    3,    3,   2,    1,    0

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Clara         -- 225 -- First place
   Diego         -- 219 -- Second place
   Elsa          -- 208
   Felix         -- 208
   Bruno         -- 196
   Ana           -- 119
   Greta         -- 111
 Clara and Diego advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Clara         -- 23 -- First place
   Diego         -- 17
   Equal Support -- 25
 Clara wins.
   Runoff math:
     65  ballots cast
   − 25  Equal Support (no preference between the two finalists)
     ──
     40  voters with a preference  (majority = 21)
           Clara 23 (57%)  ·  Diego 17 (42%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Clara
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |      Ana     |    Bruno    |  * Clara    |  * Diego    |     Elsa    |    Felix    |    Greta    |
---------------------------------------------------------------------------------------------------------------------
           Ana > |     ---      | 6 - 10 - 49 |16 -  0 - 49 |16 -  0 - 49 |16 - 13 - 36 |29 -  0 - 36 |29 -  9 - 27 |
         Bruno > | 49 - 10 -  6 |    ---      |16 - 13 - 36 |29 -  0 - 36 |29 -  0 - 36 |29 -  0 - 36 |38 -  0 - 27 |
       * Clara > | 49 -  0 - 16 |36 - 13 - 16 |    ---      |23 - 25 - 17 |29 -  9 - 27 |29 -  9 - 27 |38 - 12 - 15 |
       * Diego > | 49 -  0 - 16 |36 -  0 - 29 |17 - 25 - 23 |    ---      |38 -  0 - 27 |38 -  0 - 27 |38 - 12 - 15 |
          Elsa > | 36 - 13 - 16 |36 -  0 - 29 |27 -  9 - 29 |27 -  0 - 38 |    ---      |19 - 27 - 19 |50 -  0 - 15 |
         Felix > | 36 -  0 - 29 |36 -  0 - 29 |27 -  9 - 29 |27 -  0 - 38 |19 - 27 - 19 |    ---      |50 -  0 - 15 |
         Greta > | 27 -  9 - 29 |27 -  0 - 38 |15 - 12 - 38 |15 - 12 - 38 |15 -  0 - 50 |15 -  0 - 50 |    ---      |

[Condorcet Winner]
  Condorcet Winner: Clara — matches the STAR winner

[Condorcet Loser]
  Condorcet Loser: Greta — loses every head-to-head matchup

[Score Distribution] (how many ballots gave each star rating)
                   Score
Candidate   5   4   3   2   1   0  | Total   Avg
Ana        16   0  13   0   0  36  |   119   1.8
Bruno      23   6   0  21  15   0  |   196   3.0
Clara      13  19  18  15   0   0  |   225   3.5
Diego       9  13  36   7   0   0  |   219   3.4
Elsa        0  29  20  16   0   0  |   208   3.2
Felix      12  24   0  23   6   0  |   208   3.2
Greta      15   0  12   0   0  38  |   111   1.7
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/crowded_field_c7_star_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/crowded_field/cases/crowded_field_c7_star.yaml
```

## See also

- [Methods disagree on this election](../../../divergence_review/cases/IRV_DIFFERS_ARTIFACT/crowded_field_c7_star.md) — its entry in the divergence review ledger
- [Condorcet efficiency (topic hub)](../../../../07_Concepts/topics/condorcet/README.md)
- [Ties & tie-breaking (topic hub)](../../../../07_Concepts/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)
- [Runoff reversal (worked set)](../../../../01_STAR/02_Examples/runoff_overturns_leader/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [crowded_field_c3_approval](crowded_field_c3_approval.md) · [crowded_field_c3_irv](crowded_field_c3_irv.md) · [crowded_field_c3_ranked_robin](crowded_field_c3_ranked_robin.md) · [crowded_field_c3_star](crowded_field_c3_star.md) · [crowded_field_c5_approval](crowded_field_c5_approval.md) · [crowded_field_c5_irv](crowded_field_c5_irv.md) · [crowded_field_c5_ranked_robin](crowded_field_c5_ranked_robin.md) · [crowded_field_c5_star](crowded_field_c5_star.md) · [crowded_field_c7_approval](crowded_field_c7_approval.md) · [crowded_field_c7_irv](crowded_field_c7_irv.md) · [crowded_field_c7_ranked_robin](crowded_field_c7_ranked_robin.md)
