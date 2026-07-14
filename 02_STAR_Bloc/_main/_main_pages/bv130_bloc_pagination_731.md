# BV130 — 6 candidates / 3 winners, Bloc STAR (original; star-server#731)

*Generated from [`bv130_bloc_pagination_731.yaml`](../bv130_bloc_pagination_731.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Bloc STAR (multi-winner, majoritarian)](../../../00_start_here/proportional_representation) · **3 seats** · **Expected winners:** Someone I Like, Santa Claus, The Lesser Evil

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/yhxy7q) · **[results ↗](https://bettervoting.com/yhxy7q/results)** (election `yhxy7q`).

## Scenario

The LH reference for BetterVoting test BV130 (the ORIGINAL, not the r2 retest).
6 candidates, 3 seats, 9 ballots. This case backs sheet row BV130 and the
star-server#731 report — a REPORTING/UI issue: Bloc STAR results are shown as
browser "tabs" (one per round) and should use numbered pages instead. The
tabulation itself is correct and has a clean, tie-free result, so the LH engine
simply confirms the winners; the bug is purely how BetterVoting displays the
three rounds, not the math.

Winners (both engines): Someone I Like, Santa Claus, The Lesser Evil.

NOTE: do not confuse this with BV130-r2 (election 9ff9jk), a separate 4-ballot
retest built around a dead-rung lot tie — see bv130r2_dead_rung_bloc.md.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Johnny Cash,Elvis Presley,Santa Claus,The Lesser Evil,Someone I Like,Apocalypse Now
0,2,4,3,5,0
0,2,4,3,5,0
0,2,4,3,5,0
2,1,3,4,3,2
2,1,3,4,3,2
2,1,3,4,3,2
2,1,3,4,3,2
1,1,5,2,5,0
1,1,5,2,5,0
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR                   = Someone I Like
  Choose-One (Plurality) = The Lesser Evil   (differs from STAR)
  Approval               = Santa Claus   (differs from STAR)

--- Bloc STAR Voting Method (3 winners) ---

[Bloc STAR]
 Tabulating 9 ballots to fill 3 seats.
Count × Johnny Cash,Elvis Presley,Santa Claus,The Lesser Evil,Someone I Like,Apocalypse Now
    4 ×           2,            1,          3,              4,             3,             2
    3 ×           0,            2,          4,              3,             5,             0
    2 ×           1,            1,          5,              2,             5,             0

[Bloc STAR: Round 1: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Someone I Like  -- 37 -- First place
   Santa Claus     -- 34 -- Second place
   The Lesser Evil -- 29
   Elvis Presley   -- 12
   Johnny Cash     -- 10
   Apocalypse Now  --  8
 Someone I Like and Santa Claus advance.

[Bloc STAR: Round 1: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Someone I Like  -- 3 -- First place
   Santa Claus     -- 0
   Equal Support   -- 6
 Someone I Like wins.
   Runoff math:
     9  ballots cast
   − 6  Equal Support (no preference between the two finalists)
     ─
     3  voters with a preference  (majority = 2)
           Someone I Like 3 (100%)  ·  Santa Claus 0 (0%)

──────────────────────────────────────────────────

[Bloc STAR: Round 2: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Santa Claus     -- 34 -- First place
   The Lesser Evil -- 29 -- Second place
   Elvis Presley   -- 12
   Johnny Cash     -- 10
   Apocalypse Now  --  8
 Santa Claus and The Lesser Evil advance.

[Bloc STAR: Round 2: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Santa Claus     -- 5 -- First place
   The Lesser Evil -- 4
   Equal Support   -- 0
 Santa Claus wins.
   Runoff math:
     9  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     9  voters with a preference  (majority = 5)
           Santa Claus 5 (56%)  ·  The Lesser Evil 4 (44%)

──────────────────────────────────────────────────

[Bloc STAR: Round 3: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   The Lesser Evil -- 29 -- First place
   Elvis Presley   -- 12 -- Second place
   Johnny Cash     -- 10
   Apocalypse Now  --  8
 The Lesser Evil and Elvis Presley advance.

[Bloc STAR: Round 3: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   The Lesser Evil -- 9 -- First place
   Elvis Presley   -- 0
   Equal Support   -- 0
 The Lesser Evil wins.
   Runoff math:
     9  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     9  voters with a preference  (majority = 5)
           The Lesser Evil 9 (100%)  ·  Elvis Presley 0 (0%)

[Bloc STAR: Winners — Bloc STAR Voting Method (3 winners)]
 Someone I Like
 Santa Claus
 The Lesser Evil
```

<details>
<summary>Full audit — preference matrix, Condorcet, and score distribution</summary>

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                        |      Johnny Cash    |    Elvis Presley   |   * Santa Claus    |   The Lesser Evil  | * Someone I Like   |   Apocalypse Now   |
--------------------------------------------------------------------------------------------------------------------------------------------------------
          Johnny Cash > |         ---         |     4 - 2 - 3      |     0 - 0 - 9      |     0 - 0 - 9      |     0 - 0 - 9      |     2 - 7 - 0      |
        Elvis Presley > |      3 - 2 - 4      |        ---         |     0 - 0 - 9      |     0 - 0 - 9      |     0 - 0 - 9      |     5 - 0 - 4      |
        * Santa Claus > |      9 - 0 - 0      |     9 - 0 - 0      |        ---         |     5 - 0 - 4      |     0 - 6 - 3      |     9 - 0 - 0      |
      The Lesser Evil > |      9 - 0 - 0      |     9 - 0 - 0      |     4 - 0 - 5      |        ---         |     4 - 0 - 5      |     9 - 0 - 0      |
     * Someone I Like > |      9 - 0 - 0      |     9 - 0 - 0      |     3 - 6 - 0      |     5 - 0 - 4      |        ---         |     9 - 0 - 0      |
       Apocalypse Now > |      0 - 7 - 2      |     4 - 0 - 5      |     0 - 0 - 9      |     0 - 0 - 9      |     0 - 0 - 9      |        ---         |

[Condorcet Winner]
  Condorcet Winner: Someone I Like — matches the STAR winner

[Score Distribution] (how many ballots gave each star rating)
                      Score
Candidate        5  4  3  2  1  0  | Total   Avg
Johnny Cash      0  0  0  4  2  3  |    10   1.1
Elvis Presley    0  0  0  3  6  0  |    12   1.3
Santa Claus      2  3  4  0  0  0  |    34   3.8
The Lesser Evil  0  4  3  2  0  0  |    29   3.2
Someone I Like   5  0  4  0  0  0  |    37   4.1
Apocalypse Now   0  0  0  4  0  5  |     8   0.9
```

</details>

Everything in one file: the [`_tabulated` mirror](../_main_tabulated/bv130_bloc_pagination_731_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 02_STAR_Bloc/_main/bv130_bloc_pagination_731.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Ties & tie-breaking (topic hub)](../../../00_start_here/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [00_c3_b3_bloc-baseline-2-seats](00_c3_b3_bloc-baseline-2-seats.md) · [01_c4_b2_bloc-star-2-seats](01_c4_b2_bloc-star-2-seats.md) · [bv129_score_tiebreak_bloc](bv129_score_tiebreak_bloc.md) · [bv130r2_dead_rung_bloc](bv130r2_dead_rung_bloc.md) · [bv131_guido_bloc](bv131_guido_bloc.md) · [bv132_verify_votes_bloc](bv132_verify_votes_bloc.md) · [bv1525_condorcet_loser_bloc](bv1525_condorcet_loser_bloc.md) · [bv1815_bloc_3c2s_basic](bv1815_bloc_3c2s_basic.md) · [bv2105_r4dqvd_ice_cream_bloc](bv2105_r4dqvd_ice_cream_bloc.md) · [bv750_tie_breaking_bloc](bv750_tie_breaking_bloc.md) · [lackner_skowron_shadow_bloc_star_c7_b12](lackner_skowron_shadow_bloc_star_c7_b12.md)
