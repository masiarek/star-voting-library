---
search:
  exclude: true
---

# Co-op board — 0–5 score ballot, sss

*Generated from [`coop_board_scores_sss.yaml`](../coop_board_scores_sss.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Sequentially Spent Score (proportional STAR)](../../../../03_STAR_PR/01_Learn/README.md) · **3 seats** · **Expected winners:** Ben, Chris, Dana

## Scenario

Nine co-op members elect a three-seat board. This file is the SCORE half of
a matched pair: the same nine people, the same opinions, recorded once on a
0-5 ballot and once as Yes/No approvals (approve iff score >= 3, in
coop_board_approval.yaml).

Both halves are counted PROPORTIONALLY -- Allocated Score and SSS here,
seq-Phragmen / PAV / seqPAV on the approval file -- so the seat-filling
philosophy is held constant and any difference is attributable to the
BALLOT rather than to majoritarian-vs-proportional.

Score totals: Chris 36, Ben 24, Dana 23, Ella 22, Amy 18.
Both score tabulations elect  ->  Ben, Chris, Dana
All three approval rules elect ->  Chris, Dana, Ella

Ben and Ella swap, and the reason is the threshold. Ben is nobody's
favourite and everybody's acceptable: his scores are 1,2,4,3,2,2,2,5,3 --
a total of 24 with NOT ONE ZERO. Ella's are 4,0,3,4,5,0,2,4,0 -- a lower
total of 22, but five of them clear the 3-star line and three voters give
her nothing at all. Approval counts them 4 to 5 and seats Ella; the score
ballot counts them 24 to 22 and seats Ben.

An approval ballot cannot see a floor. Everything below the threshold --
Ben's steady 2s from the whole room -- is erased, and a bare 3 counts
exactly as much as a 5.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Amy,Ben,Chris,Dana,Ella
5,1,3,3,4      # Member 1
2,2,4,3,0      # Member 2
0,4,4,2,3      # Member 3
1,3,4,4,4      # Member 4
5,2,5,2,5      # Member 5
1,2,4,0,0      # Member 6
1,2,5,4,2      # Member 7
2,5,4,0,4      # Member 8
1,3,3,5,0      # Member 9
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
--- Sequentially Spent Score Voting Method (3 winners) ---

[Sequentially Spent Score]
 Tabulating 9 ballots to fill 3 seats.
Amy,Ben,Chris,Dana,Ella
  5,  1,    3,   3,   4
  2,  2,    4,   3,   0
  0,  4,    4,   2,   3
  1,  3,    4,   4,   4
  5,  2,    5,   2,   5
  1,  2,    4,   0,   0
  1,  2,    5,   4,   2
  2,  5,    4,   0,   4
  1,  3,    3,   5,   0

[Sequentially Spent Score: Round 1]
 The highest-scoring candidate wins a seat.
   Chris         -- 36 -- First place
   Ben           -- 24
   Dana          -- 23
   Ella          -- 22
   Amy           -- 18
 Chris wins a seat.

[Sequentially Spent Score: Round 1: Ballot allocation round]
 Total score is 36, Hare score quota is 15, giving back surplus.
 Reducing each ballot's stars by their vote * 7/12.
 Reweighted 9 ballots:
    5 ballots voted 4, stars reduced from 5 to 10/3, reweighted to 2/3.
    2 ballots voted 5, stars reduced from 5 to 35/12, reweighted to 7/12.
    2 ballots voted 3, stars reduced from 5 to 15/4, reweighted to 3/4.

[Sequentially Spent Score: Round 2]
 The highest-scoring candidate wins a seat.
   Ben           -- 16      -- First place
   Dana          -- 15+1/2
   Ella          -- 14+5/12
   Amy           -- 12
 Ben wins a seat.

[Sequentially Spent Score: Round 2: Ballot allocation round]
 Total score is 16, Hare score quota is 15, giving back surplus.
 Reducing each ballot's stars by their vote * 1/16.
 Reweighted 9 ballots:
    2 ballots voted 4/3, stars reduced from 10/3 to 25/12, reweighted to 5/12.
    2 ballots voted 7/6, stars reduced from 35/12 to 175/96, reweighted to 35/96.
    1 ballot voted 10/3, stars reduced from 10/3 to 5/24, reweighted to 1/24.
    1 ballot voted 8/3, stars reduced from 10/3 to 5/6, reweighted to 1/6.
    1 ballot voted 9/4, stars reduced from 15/4 to 105/64, reweighted to 21/64.
    1 ballot voted 2, stars reduced from 10/3 to 35/24, reweighted to 7/24.
    1 ballot voted 3/4, stars reduced from 15/4 to 195/64, reweighted to 39/64.

[Sequentially Spent Score: Round 3]
 The highest-scoring candidate wins a seat.
   Dana          -- 8+13/32 -- First place
   Amy           -- 7+ 3/16
   Ella          -- 6+79/96
 Dana wins a seat.

[Sequentially Spent Score: Winners — Sequentially Spent Score Voting Method (3 winners)]
 Ben
 Chris
 Dana
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Preference Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        Informational only — not part of the 3-winner count below,
        so no Top-2 finalists are marked.
               |     Amy    |    Ben    |   Chris   |    Dana   |    Ella   |
-----------------------------------------------------------------------------
         Amy > |    ---     |2 - 1 - 6  |1 - 1 - 7  |4 - 0 - 5  |4 - 1 - 4  |
         Ben > | 6 - 1 - 2  |   ---     |1 - 2 - 6  |3 - 1 - 5  |5 - 1 - 3  |
       Chris > | 7 - 1 - 1  |6 - 2 - 1  |   ---     |6 - 2 - 1  |5 - 3 - 1  |
        Dana > | 5 - 0 - 4  |5 - 1 - 3  |1 - 2 - 6  |   ---     |3 - 2 - 4  |
        Ella > | 4 - 1 - 4  |3 - 1 - 5  |1 - 3 - 5  |4 - 2 - 3  |   ---     |

[Condorcet Winner]
  Condorcet Winner: Chris — matches the STAR winner

[Condorcet Loser]
  No strict Condorcet loser; weak Condorcet loser: Amy (never wins a matchup)

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Amy        2  0  0  2  4  1  |    18   2.0
Ben        1  1  2  4  1  0  |    24   2.7
Chris      2  5  2  0  0  0  |    36   4.0
Dana       1  2  2  2  0  2  |    23   2.6
Ella       1  3  1  1  0  3  |    22   2.4
 Hare score quota is 15.
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/coop_board_scores_sss_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/proportional_ballots/cases/coop_board_scores_sss.yaml
```

## See also

- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [coop_board_approval](coop_board_approval.md) · [coop_board_scores_allocated](coop_board_scores_allocated.md)
