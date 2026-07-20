# BV1815 — Bloc STAR, 3 candidates, 2 seats (seat 2 by score tiebreak)

*Generated from [`bv1815_bloc_3c2s_basic.yaml`](../bv1815_bloc_3c2s_basic.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Bloc STAR (multi-winner, majoritarian)](../../../../00_start_here/proportional_representation) · **2 seats** · **Expected winners:** A, C

## Scenario

The LH reference for BetterVoting test BV1815 (a real election, id fk38pk,
marked Passed). Labeled "basic/simple", but it quietly exercises the score
tiebreaker at the second seat.

Bloc STAR, 3 candidates, 2 seats. Totals: A=12, B=1, C=2.
  - Seat 1: A (12) and C (2) advance; A wins the runoff 3-0, taking seat 1.
  - Seat 2: remove A -> B and C. In the runoff B and C TIE 1-1 (one voter
    prefers each; one is Equal Support). The tie falls to the SCORE rung:
    C's total (2) beats B's (1), so C takes seat 2.
Winners: A, C. BetterVoting agrees (tieBreakType: "score", elected A, C) — this
case Passes; it's the Bloc analog of a runoff decided by the score tiebreaker.
(Aside: the BV export labels votingMethod "STAR" rather than "Bloc STAR" — #904.)

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
A,B,C
4,1,0
3,0,2
5,0,0
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
--- Bloc STAR Voting Method (2 winners) ---

[Bloc STAR]
 Tabulating 3 ballots to fill 2 seats.
A,B,C
4,1,0
3,0,2
5,0,0

[Bloc STAR: Round 1: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   A             -- 12 -- First place
   C             --  2 -- Second place
   B             --  1
 A and C advance.

[Bloc STAR: Round 1: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   A             -- 3 -- First place
   C             -- 0
   Equal Support -- 0
 A wins.
   Runoff math:
     3  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     3  voters with a preference  (majority = 2)
           A 3 (100%)  ·  C 0 (0%)

──────────────────────────────────────────────────

[Bloc STAR: Round 2: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   C             -- 2 -- First place
   B             -- 1 -- Second place
 C and B advance.

[Bloc STAR: Round 2: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   B             -- 1 -- Tied for first place
   C             -- 1 -- Tied for first place
   Equal Support -- 1
 There's a two-way tie for first.

[Bloc STAR: Round 2: Automatic Runoff Round: First tiebreaker]
 The highest-scoring candidate wins.
   C             -- 2 -- First place
   B             -- 1
 C wins.

[Bloc STAR: Winners — Bloc STAR Voting Method (2 winners)]
 A
 C
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |    * A     |     B     |   * C     |
-----------------------------------------------------
         * A > |    ---     |3 - 0 - 0  |3 - 0 - 0  |
           B > | 0 - 0 - 3  |   ---     |1 - 1 - 1  |
         * C > | 0 - 0 - 3  |1 - 1 - 1  |   ---     |

[Condorcet Winner]
  Condorcet Winner: A — matches the STAR winner

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
A          1  1  1  0  0  0  |    12   4.0
B          0  0  0  0  1  2  |     1   0.3
C          0  0  0  1  0  2  |     2   0.7
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/bv1815_bloc_3c2s_basic_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 02_STAR_Bloc/_main/cases/bv1815_bloc_3c2s_basic.yaml
```

## See also

- [Ties & tie-breaking (topic hub)](../../../../00_start_here/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)
- [Runoff reversal (worked set)](../../../../01_STAR/runoff_overturns_leader/README.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [00_c3_b3_bloc-baseline-2-seats](00_c3_b3_bloc-baseline-2-seats.md) · [01_c4_b2_bloc-star-2-seats](01_c4_b2_bloc-star-2-seats.md) · [bv129_score_tiebreak_bloc](bv129_score_tiebreak_bloc.md) · [bv130_bloc_pagination_731](bv130_bloc_pagination_731.md) · [bv130r2_dead_rung_bloc](bv130r2_dead_rung_bloc.md) · [bv131_guido_bloc](bv131_guido_bloc.md) · [bv132_verify_votes_bloc](bv132_verify_votes_bloc.md) · [bv1525_condorcet_loser_bloc](bv1525_condorcet_loser_bloc.md) · [bv2105_r4dqvd_ice_cream_bloc](bv2105_r4dqvd_ice_cream_bloc.md) · [bv750_tie_breaking_bloc](bv750_tie_breaking_bloc.md) · [lackner_skowron_shadow_bloc_star_c7_b12](lackner_skowron_shadow_bloc_star_c7_b12.md)
