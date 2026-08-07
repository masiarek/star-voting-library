---
search:
  exclude: true
---

# Left, Centre, Right — Proportional STAR fills the council

*Generated from [`blocs_pr_c9_b10.yaml`](../blocs_pr_c9_b10.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Allocated Score (proportional STAR)](../../../../03_STAR_PR/01_Learn/README.md) · **3 seats**

## Scenario

Ten voters split into three camps — six on the left, two in the centre, two on the right — choosing three seats from nine candidates, three per camp. Every voter scores their own camp highly, the neighbouring camp modestly, and the far camp at zero. Identical ballots to blocs_bloc_c9_b10.yaml; only the count differs. This is the proportional half: each seat is decided by the voters who do not yet have a representative.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
L1,L2,L3,C1,C2,C3,R1,R2,R3
5,5,4,2,2,1,0,0,0   # Left voter 1
5,4,5,2,1,2,0,0,0   # Left voter 2
5,5,4,1,2,2,0,0,0   # Left voter 3
4,5,5,2,2,1,0,0,0   # Left voter 4
5,4,5,2,2,1,0,0,0   # Left voter 5
5,5,4,2,1,2,0,0,0   # Left voter 6
2,2,1,5,5,4,2,2,1   # Centre voter 1
1,2,2,5,4,5,2,1,2   # Centre voter 2
0,0,0,2,2,1,5,5,4   # Right voter 1
0,0,0,1,2,2,5,4,5   # Right voter 2
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
[Divergence from STAR]
  STAR   = L1
  RCV-RR = L2   (differs from STAR)
  Full round-by-round reports (generated for review):
  RCV-RR round-robin: cases_tabulated/blocs_pr_c9_b10_RCV-RR_tabulated.txt

--- Allocated Score Voting Method (3 winners) ---

[Allocated Score Voting]
 Tabulating 10 ballots to fill 3 seats.
L1,L2,L3,C1,C2,C3,R1,R2,R3
 5, 5, 4, 2, 2, 1, 0, 0, 0
 5, 4, 5, 2, 1, 2, 0, 0, 0
 5, 5, 4, 1, 2, 2, 0, 0, 0
 4, 5, 5, 2, 2, 1, 0, 0, 0
 5, 4, 5, 2, 2, 1, 0, 0, 0
 5, 5, 4, 2, 1, 2, 0, 0, 0
 2, 2, 1, 5, 5, 4, 2, 2, 1
 1, 2, 2, 5, 4, 5, 2, 1, 2
 0, 0, 0, 2, 2, 1, 5, 5, 4
 0, 0, 0, 1, 2, 2, 5, 4, 5

[Allocated Score Voting: Round 1]
 The highest-scoring candidate wins a seat.
   L1            -- 32 -- Tied for first place
   L2            -- 32 -- Tied for first place
   L3            -- 30
   C1            -- 24
   C2            -- 23
   C3            -- 21
   R1            -- 14
   R2            -- 12
   R3            -- 12
 There's a two-way tie for first.

*** No official tie-breaking lot numbers were provided.
    Ties are resolved using a fallback order: CSV column order.
    Lot-number priority order: ['L1', 'L2', 'L3', 'C1', 'C2', 'C3', 'R1', 'R2', 'R3']

[Tiebreaker: Lot Number Priority]
  Tie among: ['L1', 'L2']
  Resolved: ['L1'] (selected by lot-number priority).

[Lot-decided tie — rare]
  ⚠ The ballots did not break this tie: the deterministic rungs
    (pairwise / score, then five-star) all came back equal, so the
    pre-published LOT order chose among the tied candidates — the
    result here was set by lot, not by the votes. Usually the
    "dead rung": no tied candidate held a score-5 vote (five-star
    counts fives, not fours). Verify the tied candidates' 5-counts.

[Allocated Score Voting: Round 1: Ballot allocation round]
 Allocating 3+1/3 ballots.

[Allocated Score Voting: Round 1: Ballot allocation round: Round 1]
 Allocating 5 ballots at score 5.
 This allocation overfills the quota.  Returning fractional surplus.
 Allocating only 66.67% of these ballots.
 Keeping these ballots, but multiplying their weights by 1/3.
 5 ballots reweighted from 1 to 1/3.

[Allocated Score Voting: Round 2]
 The highest-scoring candidate wins a seat.
   C1            -- 18     -- First place
   C2            -- 17+2/3
   L2            -- 16+2/3
   C3            -- 15+2/3
   L3            -- 15+1/3
   R1            -- 14
   R2            -- 12
   R3            -- 12
 C1 wins a seat.

[Allocated Score Voting: Round 2: Ballot allocation round]
 Allocating 3+1/3 ballots.

[Allocated Score Voting: Round 2: Ballot allocation round: Round 1]
 Allocating 2 ballots at score 5.

[Allocated Score Voting: Round 2: Ballot allocation round: Round 2]
 Remaining allocation quota is 4/3.
 Allocating 2 ballots at score 2.
 This allocation overfills the remaining quota.  Returning fractional surplus.
 Allocating only 66.67% of these ballots.
 Keeping these ballots, but multiplying their weights by 1/3.
 2 ballots reweighted from 1 to 1/3.

[Allocated Score Voting: Round 3]
 Tabulating 8 remaining ballots.
L1,L2,L3,C1,C2,C3,R1,R2,R3
 5, 5, 4, 2, 2, 1, 0, 0, 0
 5, 4, 5, 2, 1, 2, 0, 0, 0
 5, 5, 4, 1, 2, 2, 0, 0, 0
 4, 5, 5, 2, 2, 1, 0, 0, 0
 5, 4, 5, 2, 2, 1, 0, 0, 0
 5, 5, 4, 2, 1, 2, 0, 0, 0
 2, 2, 1, 5, 5, 4, 2, 2, 1
 1, 2, 2, 5, 4, 5, 2, 1, 2
 0, 0, 0, 2, 2, 1, 5, 5, 4
 0, 0, 0, 1, 2, 2, 5, 4, 5

[Allocated Score Voting: Winners — Allocated Score Voting Method (3 winners)]
 C1
 L1
 L2
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |    * L1    |   * L2    |     L3    |     C1    |     C2    |     C3    |     R1    |     R2    |     R3    |
-----------------------------------------------------------------------------------------------------------------------------
        * L1 > |    ---     |2 - 6 - 2  |4 - 4 - 2  |6 - 0 - 4  |6 - 0 - 4  |6 - 0 - 4  |6 - 1 - 3  |6 - 2 - 2  |7 - 0 - 3  |
        * L2 > | 2 - 6 - 2  |   ---     |4 - 4 - 2  |6 - 0 - 4  |6 - 0 - 4  |6 - 0 - 4  |6 - 2 - 2  |7 - 1 - 2  |7 - 1 - 2  |
          L3 > | 2 - 4 - 4  |2 - 4 - 4  |   ---     |6 - 0 - 4  |6 - 0 - 4  |6 - 0 - 4  |6 - 1 - 3  |7 - 0 - 3  |6 - 2 - 2  |
          C1 > | 4 - 0 - 6  |4 - 0 - 6  |4 - 0 - 6  |   ---     |3 - 5 - 2  |5 - 3 - 2  |8 - 0 - 2  |8 - 0 - 2  |8 - 0 - 2  |
          C2 > | 4 - 0 - 6  |4 - 0 - 6  |4 - 0 - 6  |2 - 5 - 3  |   ---     |5 - 2 - 3  |8 - 0 - 2  |8 - 0 - 2  |8 - 0 - 2  |
          C3 > | 4 - 0 - 6  |4 - 0 - 6  |4 - 0 - 6  |2 - 3 - 5  |3 - 2 - 5  |   ---     |8 - 0 - 2  |8 - 0 - 2  |8 - 0 - 2  |
          R1 > | 3 - 1 - 6  |2 - 2 - 6  |3 - 1 - 6  |2 - 0 - 8  |2 - 0 - 8  |2 - 0 - 8  |   ---     |2 - 8 - 0  |2 - 8 - 0  |
          R2 > | 2 - 2 - 6  |2 - 1 - 7  |3 - 0 - 7  |2 - 0 - 8  |2 - 0 - 8  |2 - 0 - 8  |0 - 8 - 2  |   ---     |2 - 6 - 2  |
          R3 > | 3 - 0 - 7  |2 - 1 - 7  |2 - 2 - 6  |2 - 0 - 8  |2 - 0 - 8  |2 - 0 - 8  |0 - 8 - 2  |2 - 6 - 2  |   ---     |

[Condorcet Winner]
  No strict Condorcet winner; unbeaten candidates: L1, L2 (pairwise ties)

[Condorcet Loser]
  No strict Condorcet loser; jointly weak Condorcet losers: R2, R3 (winless — pairwise ties)

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
L1         5  1  0  1  1  2  |    32   3.2
L2         4  2  0  2  0  2  |    32   3.2
L3         3  3  0  1  1  2  |    30   3.0
C1         2  0  0  6  2  0  |    24   2.4
C2         1  1  0  6  2  0  |    23   2.3
C3         1  1  0  4  4  0  |    21   2.1
R1         2  0  0  2  0  6  |    14   1.4
R2         1  1  0  1  1  6  |    12   1.2
R3         1  1  0  1  1  6  |    12   1.2
 Hare quota is 10/3.

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
L1         5  1  0  1  1  2  |    32   3.2
L2         4  2  0  2  0  2  |    32   3.2
L3         3  3  0  1  1  2  |    30   3.0
C1         2  0  0  6  2  0  |    24   2.4
C2         1  1  0  6  2  0  |    23   2.3
C3         1  1  0  4  4  0  |    21   2.1
R1         2  0  0  2  0  6  |    14   1.4
R2         1  1  0  1  1  6  |    12   1.2
R3         1  1  0  1  1  6  |    12   1.2
 The highest-scoring candidate wins a seat.
   L2            -- 9+1/3 -- First place
   L3            -- 9
   R1            -- 6+2/3
   R3            -- 6+1/3
   C2            -- 6
   R2            -- 5+2/3
   C3            -- 5+1/3
 L2 wins a seat.
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/blocs_pr_c9_b10_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/bloc_vs_pr/cases/blocs_pr_c9_b10.yaml
```

## See also

- [Vote splitting (worked set)](../../../split_voting/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [blocs_bloc_c9_b10](blocs_bloc_c9_b10.md) · [min_bloc_c3_b2](min_bloc_c3_b2.md) · [min_pr_c3_b2](min_pr_c3_b2.md)
