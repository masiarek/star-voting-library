---
search:
  exclude: true
---

# Co-op board — 0–5 score ballot, allocated

*Generated from [`coop_board_scores_allocated.yaml`](../coop_board_scores_allocated.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Allocated Score (proportional STAR)](../../../../03_STAR_PR/01_Learn/README.md) · **3 seats** · **Expected winners:** Ben, Chris, Dana

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
--- Allocated Score Voting Method (3 winners) ---

[Allocated Score Voting]
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

[Allocated Score Voting: Round 1]
 The highest-scoring candidate wins a seat.
   Chris         -- 36 -- First place
   Ben           -- 24
   Dana          -- 23
   Ella          -- 22
   Amy           -- 18
 Chris wins a seat.

[Allocated Score Voting: Round 1: Ballot allocation round]
 Allocating 3 ballots.

[Allocated Score Voting: Round 1: Ballot allocation round: Round 1]
 Allocating 2 ballots at score 5.

[Allocated Score Voting: Round 1: Ballot allocation round: Round 2]
 Remaining allocation quota is 1.
 Allocating 5 ballots at score 4.
 This allocation overfills the remaining quota.  Returning fractional surplus.
 Allocating only 20.00% of these ballots.
 Keeping these ballots, but multiplying their weights by 4/5.
 5 ballots reweighted from 1 to 4/5.

[Allocated Score Voting: Round 2]
 Tabulating 7 remaining ballots.
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

[Allocated Score Voting: Round 2: Ballot allocation round]
 Allocating 3 ballots.

[Allocated Score Voting: Round 2: Ballot allocation round: Round 1]
 Allocating 1 ballot at score 4.

[Allocated Score Voting: Round 2: Ballot allocation round: Round 2]
 Remaining allocation quota is 2.
 Allocating 1 ballot at score 16/5.

[Allocated Score Voting: Round 2: Ballot allocation round: Round 3]
 Remaining allocation quota is 1.
 Allocating 1 ballot at score 3.

[Allocated Score Voting: Round 3]
 Tabulating 4 remaining ballots.
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

[Allocated Score Voting: Winners — Allocated Score Voting Method (3 winners)]
 Ben
 Chris
 Dana
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |     Amy    |  * Ben    | * Chris   |    Dana   |    Ella   |
-----------------------------------------------------------------------------
         Amy > |    ---     |2 - 1 - 6  |1 - 1 - 7  |4 - 0 - 5  |4 - 1 - 4  |
       * Ben > | 6 - 1 - 2  |   ---     |1 - 2 - 6  |3 - 1 - 5  |5 - 1 - 3  |
     * Chris > | 7 - 1 - 1  |6 - 2 - 1  |   ---     |6 - 2 - 1  |5 - 3 - 1  |
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
 Hare quota is 3.

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Amy        2  0  0  2  4  1  |    18   2.0
Ben        1  1  2  4  1  0  |    24   2.7
Chris      2  5  2  0  0  0  |    36   4.0
Dana       1  2  2  2  0  2  |    23   2.6
Ella       1  3  1  1  0  3  |    22   2.4
 The highest-scoring candidate wins a seat.
   Ben           -- 16+4/5 -- First place
   Dana          -- 15+1/5
   Ella          -- 12+4/5
   Amy           -- 10+4/5
 Ben wins a seat.

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Amy        2  0  0  2  4  1  |    18   2.0
Ben        1  1  2  4  1  0  |    24   2.7
Chris      2  5  2  0  0  0  |    36   4.0
Dana       1  2  2  2  0  2  |    23   2.6
Ella       1  3  1  1  0  3  |    22   2.4
 The highest-scoring candidate wins a seat.
   Dana          -- 8+3/5 -- First place
   Amy           -- 8+1/5
   Ella          -- 7+1/5
 Dana wins a seat.
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/coop_board_scores_allocated_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/proportional_ballots/cases/coop_board_scores_allocated.yaml
```

## See also

- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [coop_board_approval](coop_board_approval.md) · [coop_board_scores_sss](coop_board_scores_sss.md)
