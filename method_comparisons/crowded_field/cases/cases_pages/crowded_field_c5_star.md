---
search:
  exclude: true
---

# Crowded field, rung 5 — 5 candidates, 65 voters, counted by STAR

*Generated from [`crowded_field_c5_star.yaml`](../crowded_field_c5_star.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../../01_STAR/01_Learn/README.md) · **1 seat** · **Expected winner:** Diego

**Official tie-break (lot) order:** Ana > Bruno > Diego > Elsa > Greta — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

RUNG 2 — the same 65 voters, the same opinions, two more names on the paper.

Bruno (6) and Elsa (14) join, one on each side of Diego. Nobody has changed their mind:
Diego still beats all four rivals head-to-head, so he is still the Condorcet winner,
and STAR still elects him — 244 in the scoring round to Elsa's 220, then the runoff
38–27.

The choose-one family has already broken, in two different directions. Choose-One now
elects Bruno, whose 23 first choices beat Diego's 9 — and Diego's collapse from 34 to 9
is arithmetic, not persuasion: Bruno and Elsa now stand between him and the voters who
previously had nobody closer. RCV-IRV elects Elsa. Both results are in
crowded_field_c5_irv.yaml, which counts them on real ranked ballots.

Score and Approval are still with STAR here. They break at the next rung.

Construction: build_ladder.py in this folder. 65 voters in seven blocs at 0, 4, 8, 12,
16, 20, 24 (sizes 6, 10, 13, 9, 12, 8, 7); candidates fixed at Ana 1 · Bruno 6 ·
Clara 9 · Diego 11 · Elsa 14 · Felix 16 · Greta 22; utility = minus distance; scores =
each bloc's own min-max scaling onto 0–5. Nothing is tuned, and no count at any rung is
settled by a tie-break.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:Ana,Bruno,Diego,Elsa,Greta
6:5,4,3,2,0    # bloc at 0
10:5,5,3,2,0    # bloc at 4
13:3,5,5,3,0    # bloc at 8
9:0,2,5,4,0    # bloc at 12
12:0,2,4,5,3    # bloc at 16
8:0,1,3,4,5    # bloc at 20
7:0,1,2,3,5    # bloc at 24
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
[Divergence from STAR]
  STAR                   = Diego
  Choose-One (Plurality) = Ana   (differs from STAR)
  RCV-IRV                = Elsa   (differs from STAR)
  Note: 23 of 65 ballots (35%) had equal non-zero scores, so their ranks
        were decided by candidate priority order. The RCV-IRV result may be
        an artifact of score-to-rank tie-breaking rather than a deep
        difference.
  Note: Ranked Robin (RCV-RR) agrees with STAR, so RCV-IRV is the lone
        outlier — the classic center-squeeze signature.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: cases_tabulated/crowded_field_c5_star_RCV-IRV_tabulated.txt

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 65 ballots.
Count × Ana,Bruno,Diego,Elsa,Greta
   13 ×   3,    5,    5,   3,    0
   12 ×   0,    2,    4,   5,    3
   10 ×   5,    5,    3,   2,    0
    9 ×   0,    2,    5,   4,    0
    8 ×   0,    1,    3,   4,    5
    7 ×   0,    1,    2,   3,    5
    6 ×   5,    4,    3,   2,    0

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Diego         -- 244 -- First place
   Elsa          -- 220 -- Second place
   Bruno         -- 196
   Ana           -- 119
   Greta         -- 111
 Diego and Elsa advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Diego         -- 38 -- First place
   Elsa          -- 27
   Equal Support --  0
 Diego wins.
   Runoff math:
     65  ballots cast
   −  0  Equal Support (no preference between the two finalists)
     ──
     65  voters with a preference  (majority = 33)
           Diego 38 (58%)  ·  Elsa 27 (42%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Diego
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |      Ana     |    Bruno    |  * Diego    |   * Elsa    |    Greta    |
-----------------------------------------------------------------------------------------
           Ana > |     ---      | 6 - 10 - 49 |16 -  0 - 49 |16 - 13 - 36 |29 -  9 - 27 |
         Bruno > | 49 - 10 -  6 |    ---      |16 - 13 - 36 |29 -  0 - 36 |38 -  0 - 27 |
       * Diego > | 49 -  0 - 16 |36 - 13 - 16 |    ---      |38 -  0 - 27 |50 -  0 - 15 |
        * Elsa > | 36 - 13 - 16 |36 -  0 - 29 |27 -  0 - 38 |    ---      |50 -  0 - 15 |
         Greta > | 27 -  9 - 29 |27 -  0 - 38 |15 -  0 - 50 |15 -  0 - 50 |    ---      |

[Condorcet Winner]
  Condorcet Winner: Diego — matches the STAR winner

[Condorcet Loser]
  Condorcet Loser: Greta — loses every head-to-head matchup

[Score Distribution] (how many ballots gave each star rating)
                   Score
Candidate   5   4   3   2   1   0  | Total   Avg
Ana        16   0  13   0   0  36  |   119   1.8
Bruno      23   6   0  21  15   0  |   196   3.0
Diego      22  12  24   7   0   0  |   244   3.8
Elsa       12  17  20  16   0   0  |   220   3.4
Greta      15   0  12   0   0  38  |   111   1.7
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/crowded_field_c5_star_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/crowded_field/cases/crowded_field_c5_star.yaml
```

## See also

- [Methods disagree on this election](../../../divergence_review/cases/IRV_DIFFERS_ARTIFACT/crowded_field_c5_star.md) — its entry in the divergence review ledger
- [Condorcet efficiency (topic hub)](../../../../07_Concepts/topics/condorcet/README.md)
- [Ties & tie-breaking (topic hub)](../../../../07_Concepts/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)
- [Runoff reversal (worked set)](../../../../01_STAR/02_Examples/runoff_overturns_leader/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [crowded_field_c3_approval](crowded_field_c3_approval.md) · [crowded_field_c3_irv](crowded_field_c3_irv.md) · [crowded_field_c3_ranked_robin](crowded_field_c3_ranked_robin.md) · [crowded_field_c3_star](crowded_field_c3_star.md) · [crowded_field_c5_approval](crowded_field_c5_approval.md) · [crowded_field_c5_irv](crowded_field_c5_irv.md) · [crowded_field_c5_ranked_robin](crowded_field_c5_ranked_robin.md) · [crowded_field_c7_approval](crowded_field_c7_approval.md) · [crowded_field_c7_irv](crowded_field_c7_irv.md) · [crowded_field_c7_ranked_robin](crowded_field_c7_ranked_robin.md) · [crowded_field_c7_star](crowded_field_c7_star.md)
