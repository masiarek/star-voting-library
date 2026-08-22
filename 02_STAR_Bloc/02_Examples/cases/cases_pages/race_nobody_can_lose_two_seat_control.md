---
search:
  exclude: true
---

# A race nobody can lose — the two-seat control

*Generated from [`race_nobody_can_lose_two_seat_control.yaml`](../race_nobody_can_lose_two_seat_control.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Bloc STAR (multi-winner, majoritarian)](../../../01_Learn/README.md) · **2 seats** · **Expected winners:** Abby, Bruno

## Scenario

The control for BV2269 (bv2269_t488h9_race_nobody_can_lose.yaml): the SAME
seven ballots and the same three candidates, with one seat removed. Two
seats from three candidates is an ordinary Bloc STAR election, so the LH
engine counts it without complaint — which is what isolates the degenerate
ingredient in the other file. Nothing about these ballots is malformed; the
only thing wrong there is the seat count.

Scoring round Abby 28, Bruno 23, Celia 16. Seat 1 runoff Abby 5 - Bruno 2,
seat 2 runoff Bruno 5 - Celia 2, with every voter expressing a preference in
both. Celia, the candidate who takes the third seat by default when there is
a third seat, wins nothing here.

LH-only: this control was never minted on BetterVoting. The BV half of the
pair is the three-seat file.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Abby,Bruno,Celia
5,3,1
5,4,0
4,3,2
5,2,3
3,5,1
2,5,4
4,1,5
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
--- Bloc STAR Voting Method (2 winners) ---

[Bloc STAR]
 Tabulating 7 ballots to fill 2 seats.
Abby,Bruno,Celia
   5,    3,    1
   5,    4,    0
   4,    3,    2
   5,    2,    3
   3,    5,    1
   2,    5,    4
   4,    1,    5

[Bloc STAR: Round 1: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Abby          -- 28 -- First place
   Bruno         -- 23 -- Second place
   Celia         -- 16
 Abby and Bruno advance.

[Bloc STAR: Round 1: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Abby          -- 5 -- First place
   Bruno         -- 2
   Equal Support -- 0
 Abby wins.
   Runoff math:
     7  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     7  voters with a preference  (majority = 4)
           Abby 5 (71%)  ·  Bruno 2 (29%)

──────────────────────────────────────────────────

[Bloc STAR: Round 2: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Bruno         -- 23 -- First place
   Celia         -- 16 -- Second place
 Bruno and Celia advance.

[Bloc STAR: Round 2: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Bruno         -- 5 -- First place
   Celia         -- 2
   Equal Support -- 0
 Bruno wins.
   Runoff math:
     7  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     7  voters with a preference  (majority = 4)
           Bruno 5 (71%)  ·  Celia 2 (29%)

[Bloc STAR: Winners — Bloc STAR Voting Method (2 winners)]
 Abby
 Bruno
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Preference Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        Informational only — not part of the 2-winner count below,
        so no Top-2 finalists are marked.
               |     Abby   |   Bruno   |   Celia   |
-----------------------------------------------------
        Abby > |    ---     |5 - 0 - 2  |5 - 0 - 2  |
       Bruno > | 2 - 0 - 5  |   ---     |5 - 0 - 2  |
       Celia > | 2 - 0 - 5  |2 - 0 - 5  |   ---     |

[Condorcet Winner]
  Condorcet Winner: Abby — matches the STAR winner

[Condorcet Loser]
  Condorcet Loser: Celia — loses every head-to-head matchup

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Abby       3  2  1  1  0  0  |    28   4.0
Bruno      2  1  2  1  1  0  |    23   3.3
Celia      1  1  1  1  2  1  |    16   2.3
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/race_nobody_can_lose_two_seat_control_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 02_STAR_Bloc/02_Examples/cases/race_nobody_can_lose_two_seat_control.yaml
```

## See also

- [Runoff reversal (worked set)](../../../../01_STAR/02_Examples/runoff_overturns_leader/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [00_c3_b3_bloc-baseline-2-seats](00_c3_b3_bloc-baseline-2-seats.md) · [01_c4_b2_bloc-star-2-seats](01_c4_b2_bloc-star-2-seats.md) · [b484mbm_tie_every_rung](b484mbm_tie_every_rung.md) · [bloc_lot_path_dependence_a_c3_b5](bloc_lot_path_dependence_a_c3_b5.md) · [bloc_lot_path_dependence_b_c3_b5](bloc_lot_path_dependence_b_c3_b5.md) · [bv129_score_tiebreak_bloc](bv129_score_tiebreak_bloc.md) · [bv130_bloc_pagination_731](bv130_bloc_pagination_731.md) · [bv130r2_dead_rung_bloc](bv130r2_dead_rung_bloc.md) · [bv131_guido_bloc](bv131_guido_bloc.md) · [bv132_verify_votes_bloc](bv132_verify_votes_bloc.md) · [bv1525_condorcet_loser_bloc](bv1525_condorcet_loser_bloc.md) · [bv1815_bloc_3c2s_basic](bv1815_bloc_3c2s_basic.md) · [bv1835_8h3yrx_score_leader_no_seat](bv1835_8h3yrx_score_leader_no_seat.md) · [bv2105_r4dqvd_ice_cream_bloc](bv2105_r4dqvd_ice_cream_bloc.md) · [bv2105r2_w3vvff_ice_cream_recheck](bv2105r2_w3vvff_ice_cream_recheck.md) · [bv2269_t488h9_race_nobody_can_lose](bv2269_t488h9_race_nobody_can_lose.md) · [bv750_tie_breaking_bloc](bv750_tie_breaking_bloc.md) · [lackner_skowron_shadow_bloc_star_c7_b12](lackner_skowron_shadow_bloc_star_c7_b12.md)
