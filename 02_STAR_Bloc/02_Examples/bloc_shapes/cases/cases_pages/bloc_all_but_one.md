---
search:
  exclude: true
---

# Bloc STAR — five seats, six candidates: the election that only excludes

*Generated from [`bloc_all_but_one.yaml`](../bloc_all_but_one.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Bloc STAR (multi-winner, majoritarian)](../../../../01_Learn/README.md) · **5 seats** · **Expected winners:** Ana, Cleo, Bram, Dov, Esme

## Scenario

Seven voters fill FIVE seats from six candidates. When almost everyone wins,
the count stops being about who is chosen and becomes about who is left out —
and the methods stop disagreeing.

Scores: Ana 22, Cleo 21, Dov 20, Bram 19, Esme 12, Finn 11.

  - Seat 1: finalists Ana and Cleo; Ana wins the runoff 4-3.
  - Seat 2: finalists Cleo and Dov. The runoff is a 3-3 TIE (one voter
    expresses no preference), broken by the FIRST TIEBREAKER — highest score —
    which favours Cleo 21 to 20.
  - Seat 3: finalists Dov and Bram; Bram wins 4-3.
  - Seat 4: finalists Dov and Esme; Dov wins.
  - Seat 5: finalists Esme and Finn; Esme wins.

Council: Ana, Cleo, Bram, Dov, Esme. Finn is the only candidate excluded.

Bloc STAR, Allocated Score, Sequentially Spent Score and Reweighted Range all
elect the SAME five candidates here — they differ only in the order the seats
are filled. That is the structural reason: with five of six seats filled, there
is no room left for proportionality to reallocate anything. The closer the
seat count gets to the candidate count, the less the choice of method can
matter, until at seats = candidates it cannot matter at all.

This case also carries a second job, for the engine rather than the reader. The
round-2 runoff tie is resolved by a DETERMINISTIC rung (score) inside a bloc
round, and the machine-readable contract does not see it: the printed report
shows "Round 2: Automatic Runoff Round: First tiebreaker" while
`--json` reports `tiebreaks: []` at schema 1.2.0. That is the known blind spot
named in CLAUDE.md — the rungs below the lot inside a Bloc/PR round run in
starvote's own counting functions and report nothing back. Keep this file as
the fixture that fails first when someone closes that gap.

The tie decides the ORDER of seats 2 and 4 only; Cleo and Dov are both elected
either way, so the winner SET does not depend on it.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Ana,Bram,Cleo,Dov,Esme,Finn
5,4,3,2,1,0
4,5,2,3,0,1
3,2,5,4,1,0
0,1,2,3,4,5
5,3,4,2,0,1
1,0,2,3,5,4
4,4,3,3,1,0
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
--- Bloc STAR Voting Method (5 winners) ---

[Bloc STAR]
 Tabulating 7 ballots to fill 5 seats.
Ana,Bram,Cleo,Dov,Esme,Finn
  5,   4,   3,  2,   1,   0
  4,   5,   2,  3,   0,   1
  3,   2,   5,  4,   1,   0
  0,   1,   2,  3,   4,   5
  5,   3,   4,  2,   0,   1
  1,   0,   2,  3,   5,   4
  4,   4,   3,  3,   1,   0

[Bloc STAR: Round 1: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Ana           -- 22 -- First place
   Cleo          -- 21 -- Second place
   Dov           -- 20
   Bram          -- 19
   Esme          -- 12
   Finn          -- 11
 Ana and Cleo advance.

[Bloc STAR: Round 1: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Ana           -- 4 -- First place
   Cleo          -- 3
   Equal Support -- 0
 Ana wins.
   Runoff math:
     7  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     7  voters with a preference  (majority = 4)
           Ana 4 (57%)  ·  Cleo 3 (43%)

──────────────────────────────────────────────────

[Bloc STAR: Round 2: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Cleo          -- 21 -- First place
   Dov           -- 20 -- Second place
   Bram          -- 19
   Esme          -- 12
   Finn          -- 11
 Cleo and Dov advance.

[Bloc STAR: Round 2: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Cleo          -- 3 -- Tied for first place
   Dov           -- 3 -- Tied for first place
   Equal Support -- 1
 There's a two-way tie for first.

[Bloc STAR: Round 2: Automatic Runoff Round: First tiebreaker]
 The highest-scoring candidate wins.
   Cleo          -- 21 -- First place
   Dov           -- 20
 Cleo wins.

──────────────────────────────────────────────────

[Bloc STAR: Round 3: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Dov           -- 20 -- First place
   Bram          -- 19 -- Second place
   Esme          -- 12
   Finn          -- 11
 Dov and Bram advance.

[Bloc STAR: Round 3: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Bram          -- 4 -- First place
   Dov           -- 3
   Equal Support -- 0
 Bram wins.
   Runoff math:
     7  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     7  voters with a preference  (majority = 4)
           Bram 4 (57%)  ·  Dov 3 (43%)

──────────────────────────────────────────────────

[Bloc STAR: Round 4: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Dov           -- 20 -- First place
   Esme          -- 12 -- Second place
   Finn          -- 11
 Dov and Esme advance.

[Bloc STAR: Round 4: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Dov           -- 5 -- First place
   Esme          -- 2
   Equal Support -- 0
 Dov wins.
   Runoff math:
     7  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     7  voters with a preference  (majority = 4)
           Dov 5 (71%)  ·  Esme 2 (29%)

──────────────────────────────────────────────────

[Bloc STAR: Round 5: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Esme          -- 12 -- First place
   Finn          -- 11 -- Second place
 Esme and Finn advance.

[Bloc STAR: Round 5: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Esme          -- 4 -- First place
   Finn          -- 3
   Equal Support -- 0
 Esme wins.
   Runoff math:
     7  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     7  voters with a preference  (majority = 4)
           Esme 4 (57%)  ·  Finn 3 (43%)

[Bloc STAR: Winners — Bloc STAR Voting Method (5 winners)]
 Ana
 Cleo
 Bram
 Dov
 Esme
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Preference Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        Informational only — not part of the 5-winner count below,
        so no Top-2 finalists are marked.
               |     Ana    |    Bram   |    Cleo   |    Dov    |    Esme   |    Finn   |
-----------------------------------------------------------------------------------------
         Ana > |    ---     |4 - 1 - 2  |4 - 0 - 3  |4 - 0 - 3  |5 - 0 - 2  |5 - 0 - 2  |
        Bram > | 2 - 1 - 4  |   ---     |3 - 0 - 4  |4 - 0 - 3  |5 - 0 - 2  |5 - 0 - 2  |
        Cleo > | 3 - 0 - 4  |4 - 0 - 3  |   ---     |3 - 1 - 3  |5 - 0 - 2  |5 - 0 - 2  |
         Dov > | 3 - 0 - 4  |3 - 0 - 4  |3 - 1 - 3  |   ---     |5 - 0 - 2  |5 - 0 - 2  |
        Esme > | 2 - 0 - 5  |2 - 0 - 5  |2 - 0 - 5  |2 - 0 - 5  |   ---     |4 - 0 - 3  |
        Finn > | 2 - 0 - 5  |2 - 0 - 5  |2 - 0 - 5  |2 - 0 - 5  |3 - 0 - 4  |   ---     |

[Condorcet Winner]
  Condorcet Winner: Ana — matches the STAR winner

[Condorcet Loser]
  Condorcet Loser: Finn — loses every head-to-head matchup

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Ana        2  2  1  0  1  1  |    22   3.1
Bram       1  2  1  1  1  1  |    19   2.7
Cleo       1  1  2  3  0  0  |    21   3.0
Dov        0  1  4  2  0  0  |    20   2.9
Esme       1  1  0  0  3  2  |    12   1.7
Finn       1  1  0  0  2  3  |    11   1.6
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/bloc_all_but_one_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 02_STAR_Bloc/02_Examples/bloc_shapes/cases/bloc_all_but_one.yaml
```

## See also

- [Ties & tie-breaking (topic hub)](../../../../../07_Concepts/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)
- [Runoff reversal (worked set)](../../../../../01_STAR/02_Examples/runoff_overturns_leader/README.md)
- [Glossary](../../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [bloc_condorcet_winner_no_seat](bloc_condorcet_winner_no_seat.md) · [bloc_divided_majority](bloc_divided_majority.md) · [bloc_equal_support_seat](bloc_equal_support_seat.md) · [bloc_finalist_wins_nothing](bloc_finalist_wins_nothing.md) · [bloc_harborview_council](bloc_harborview_council.md) · [bloc_no_majority_bridge](bloc_no_majority_bridge.md) · [bloc_one_voter_council](bloc_one_voter_council.md) · [bloc_score_leader_shut_out](bloc_score_leader_shut_out.md) · [bloc_widest_field](bloc_widest_field.md)
