---
search:
  exclude: true
---

# Bloc STAR — a seat-1 lot decides who wins seat 2 (lot A: Nadia first)

*Generated from [`bloc_lot_path_dependence_a_c3_b5.yaml`](../bloc_lot_path_dependence_a_c3_b5.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Bloc STAR (multi-winner, majoritarian)](../../../../03_STAR_PR/01_Learn/README.md) · **2 seats** · **Expected winners:** Nadia, Priya

**Official tie-break (lot) order:** Nadia > Omar > Priya — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

Three candidates for a two-seat arts council, five ballots. Nadia and Omar
tie at 15 points; Priya trails at 12, so Nadia and Omar are the seat-1
finalists. Their runoff is a dead heat (2 - 2, with 1 Equal Support), and
every deterministic rung ties behind it: score 15 - 15, five-star 3 - 3.
The five-star rung is LIVE here (both hold three 5s) and still cannot
separate them, so seat 1 falls to the published lot.

This file pins the lot to [Nadia, Omar, Priya], so Nadia takes seat 1. Omar
then meets Priya for seat 2 and LOSES that runoff 2 - 1 (two ballots score
them both 5). Winners: Nadia, Priya.

The companion file bloc_lot_path_dependence_b_c3_b5.yaml is the identical
election with the lot reversed: Omar takes seat 1, Nadia then meets Priya
and BEATS her 3 - 2. Winners: Omar, Nadia.

The point is that the two runs differ in WHO WINS, not merely in the order
the seats were filled. Priya is on the council in one and absent from the
other, and no ballot changed. Bloc STAR is sequential - each seat is decided
in the field the previous seat left behind - so a tie broken at seat 1
propagates into every later seat. In a top-N method (Bloc Approval, SNTV,
Bloc Ranked Robin) a tie can only ever swap the last seat.

Why the two head-to-heads differ: Omar and Priya are scored 5/5 by the two
ballots that would otherwise separate them, so Omar wins only 1 of the 3
decided ballots; Nadia and Priya are never tied on any ballot, and Nadia
takes 3 of 5. Same pair of near-identical candidates, opposite results
against the same third one.

LH-only (no BetterVoting election): the winner turns on the lot, and only
LH's published lot_numbers let a reader derive the result from the file.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Nadia,Omar,Priya
5,0,1
5,0,1
5,5,0
0,5,5
0,5,5
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
--- Bloc STAR Voting Method (2 winners) ---

[Bloc STAR]
 Tabulating 5 ballots to fill 2 seats.
Count × Nadia,Omar,Priya
    2 ×     5,   0,    1
    2 ×     0,   5,    5
    1 ×     5,   5,    0

[Bloc STAR: Round 1: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Nadia         -- 15 -- First place
   Omar          -- 15 -- Second place
   Priya         -- 12
 Nadia and Omar advance.

[Bloc STAR: Round 1: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Nadia         -- 2 -- Tied for first place
   Omar          -- 2 -- Tied for first place
   Equal Support -- 1
 There's a two-way tie for first.

[Bloc STAR: Round 1: Automatic Runoff Round: First tiebreaker]
 The highest-scoring candidate wins.
   Nadia         -- 15 -- Tied for first place
   Omar          -- 15 -- Tied for first place
 There's still a two-way tie for first.

[Bloc STAR: Round 1: Automatic Runoff Round: Second tiebreaker]
 The candidate with the most votes of score 5 wins.
   Nadia         -- 3 -- Tied for first place
   Omar          -- 3 -- Tied for first place
 There's still a two-way tie for first.

*(Ties are resolved by choosing the tied candidate with the highest-priority official lot number.)*
    Lot-number priority order: ['Nadia', 'Omar', 'Priya']

[Tiebreaker: Lot Number Priority]
  Tie among: ['Nadia', 'Omar']
  Resolved: ['Nadia'] (selected by lot-number priority).

[Lot-decided tie — rare]
  ⚠ The ballots did not break this tie: the deterministic rungs
    (pairwise / score, then five-star) all came back equal, so the
    pre-published LOT order chose among the tied candidates — the
    result here was set by lot, not by the votes. Usually the
    "dead rung": no tied candidate held a score-5 vote (five-star
    counts fives, not fours). Verify the tied candidates' 5-counts.

──────────────────────────────────────────────────

[Bloc STAR: Round 2: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Omar          -- 15 -- First place
   Priya         -- 12 -- Second place
 Omar and Priya advance.

[Bloc STAR: Round 2: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Priya         -- 2 -- First place
   Omar          -- 1
   Equal Support -- 2
 Priya wins.
   Runoff math:
     5  ballots cast
   − 2  Equal Support (no preference between the two finalists)
     ─
     3  voters with a preference  (majority = 2)
           Priya 2 (67%)  ·  Omar 1 (33%)

[Bloc STAR: Winners — Bloc STAR Voting Method (2 winners)]
 Nadia
 Priya
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Preference Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        Informational only — not part of the 2-winner count below,
        so no Top-2 finalists are marked.
               |    Nadia   |    Omar   |   Priya   |
-----------------------------------------------------
       Nadia > |    ---     |2 - 1 - 2  |3 - 0 - 2  |
        Omar > | 2 - 1 - 2  |   ---     |1 - 2 - 2  |
       Priya > | 2 - 0 - 3  |2 - 2 - 1  |   ---     |

[Condorcet Winner]
  No strict Condorcet winner; weak Condorcet winner: Nadia — matches the STAR winner

[Condorcet Loser]
  No strict Condorcet loser; weak Condorcet loser: Omar (never wins a matchup)

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Nadia      3  0  0  0  0  2  |    15   3.0
Omar       3  0  0  0  0  2  |    15   3.0
Priya      2  0  0  0  2  1  |    12   2.4
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/bloc_lot_path_dependence_a_c3_b5_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 02_STAR_Bloc/02_Examples/cases/bloc_lot_path_dependence_a_c3_b5.yaml
```

## See also

- [Ties & tie-breaking (topic hub)](../../../../07_Concepts/topics/ties/README.md)
- [Runoff reversal (worked set)](../../../../01_STAR/02_Examples/runoff_overturns_leader/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [00_c3_b3_bloc-baseline-2-seats](00_c3_b3_bloc-baseline-2-seats.md) · [01_c4_b2_bloc-star-2-seats](01_c4_b2_bloc-star-2-seats.md) · [b484mbm_tie_every_rung](b484mbm_tie_every_rung.md) · [bloc_lot_path_dependence_b_c3_b5](bloc_lot_path_dependence_b_c3_b5.md) · [bv129_score_tiebreak_bloc](bv129_score_tiebreak_bloc.md) · [bv130_bloc_pagination_731](bv130_bloc_pagination_731.md) · [bv130r2_dead_rung_bloc](bv130r2_dead_rung_bloc.md) · [bv131_guido_bloc](bv131_guido_bloc.md) · [bv132_verify_votes_bloc](bv132_verify_votes_bloc.md) · [bv1525_condorcet_loser_bloc](bv1525_condorcet_loser_bloc.md) · [bv1815_bloc_3c2s_basic](bv1815_bloc_3c2s_basic.md) · [bv1835_8h3yrx_score_leader_no_seat](bv1835_8h3yrx_score_leader_no_seat.md) · [bv2105_r4dqvd_ice_cream_bloc](bv2105_r4dqvd_ice_cream_bloc.md) · [bv2105r2_w3vvff_ice_cream_recheck](bv2105r2_w3vvff_ice_cream_recheck.md) · [bv2269_t488h9_race_nobody_can_lose](bv2269_t488h9_race_nobody_can_lose.md) · [bv750_tie_breaking_bloc](bv750_tie_breaking_bloc.md) · [lackner_skowron_shadow_bloc_star_c7_b12](lackner_skowron_shadow_bloc_star_c7_b12.md) · [race_nobody_can_lose_two_seat_control](race_nobody_can_lose_two_seat_control.md)
