---
search:
  exclude: true
---

# Left, Centre, Right — Bloc STAR fills the council

*Generated from [`blocs_bloc_c9_b10.yaml`](../blocs_bloc_c9_b10.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Bloc STAR (multi-winner, majoritarian)](../../../../03_STAR_PR/01_Learn/README.md) · **3 seats**

## Scenario

Ten voters split into three camps — six on the left, two in the centre, two on the right — choosing three seats from nine candidates, three per camp. Every voter scores their own camp highly, the neighbouring camp modestly, and the far camp at zero. Identical ballots to blocs_pr_c9_b10.yaml; only the count differs. This is the majoritarian half: with every ballot at full weight for every seat, the largest camp decides all three.

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
  RCV-RR round-robin: cases_tabulated/blocs_bloc_c9_b10_RCV-RR_tabulated.txt

--- Bloc STAR Voting Method (3 winners) ---

[Bloc STAR]
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

[Bloc STAR: Round 1: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   L1            -- 32 -- First place
   L2            -- 32 -- Second place
   L3            -- 30
   C1            -- 24
   C2            -- 23
   C3            -- 21
   R1            -- 14
   R2            -- 12
   R3            -- 12
 L1 and L2 advance.

[Bloc STAR: Round 1: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   L1            -- 2 -- Tied for first place
   L2            -- 2 -- Tied for first place
   Equal Support -- 6
 There's a two-way tie for first.

[Bloc STAR: Round 1: Automatic Runoff Round: First tiebreaker]
 The highest-scoring candidate wins.
   L1            -- 32 -- Tied for first place
   L2            -- 32 -- Tied for first place
 There's still a two-way tie for first.

[Bloc STAR: Round 1: Automatic Runoff Round: Second tiebreaker]
 The candidate with the most votes of score 5 wins.
   L1            -- 5 -- First place
   L2            -- 4
 L1 wins.

──────────────────────────────────────────────────

[Bloc STAR: Round 2: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   L2            -- 32 -- First place
   L3            -- 30 -- Second place
   C1            -- 24
   C2            -- 23
   C3            -- 21
   R1            -- 14
   R2            -- 12
   R3            -- 12
 L2 and L3 advance.

[Bloc STAR: Round 2: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   L2            -- 4 -- First place
   L3            -- 2
   Equal Support -- 4
 L2 wins.
   Runoff math:
     10  ballots cast
   −  4  Equal Support (no preference between the two finalists)
     ──
      6  voters with a preference  (majority = 4)
           L2 4 (67%)  ·  L3 2 (33%)

──────────────────────────────────────────────────

[Bloc STAR: Round 3: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   L3            -- 30 -- First place
   C1            -- 24 -- Second place
   C2            -- 23
   C3            -- 21
   R1            -- 14
   R2            -- 12
   R3            -- 12
 L3 and C1 advance.

[Bloc STAR: Round 3: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   L3            -- 6 -- First place
   C1            -- 4
   Equal Support -- 0
 L3 wins.
   Runoff math:
     10  ballots cast
   −  0  Equal Support (no preference between the two finalists)
     ──
     10  voters with a preference  (majority = 6)
           L3 6 (60%)  ·  C1 4 (40%)

[Bloc STAR: Winners — Bloc STAR Voting Method (3 winners)]
 L1
 L2
 L3
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Preference Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        Informational only — not part of the 3-winner count below,
        so no Top-2 finalists are marked.
               |      L1    |     L2    |     L3    |     C1    |     C2    |     C3    |     R1    |     R2    |     R3    |
-----------------------------------------------------------------------------------------------------------------------------
          L1 > |    ---     |2 - 6 - 2  |4 - 4 - 2  |6 - 0 - 4  |6 - 0 - 4  |6 - 0 - 4  |6 - 1 - 3  |6 - 2 - 2  |7 - 0 - 3  |
          L2 > | 2 - 6 - 2  |   ---     |4 - 4 - 2  |6 - 0 - 4  |6 - 0 - 4  |6 - 0 - 4  |6 - 2 - 2  |7 - 1 - 2  |7 - 1 - 2  |
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
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/blocs_bloc_c9_b10_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/bloc_vs_pr/cases/blocs_bloc_c9_b10.yaml
```

## See also

- [Vote splitting (worked set)](../../../split_voting/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [blocs_pr_c9_b10](blocs_pr_c9_b10.md) · [min_bloc_c3_b2](min_bloc_c3_b2.md) · [min_pr_c3_b2](min_pr_c3_b2.md)
