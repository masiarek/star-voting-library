---
search:
  exclude: true
---

# 3 candidates / 2 seats, Bloc STAR — tie at every rung (484mbm)

*Generated from [`b484mbm_tie_every_rung.yaml`](../b484mbm_tie_every_rung.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Bloc STAR (multi-winner, majoritarian)](../../../../03_STAR_PR/01_Learn/README.md) · **2 seats** · **Expected winners:** Blythe, Arden

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/484mbm) · **[results ↗](https://bettervoting.com/484mbm/results)** (election `484mbm`).

**Official tie-break (lot) order:** Blythe > Arden > Corin — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

The smallest election that ties all the way down. Three voters, three
candidates, two seats; the ballots rotate, so each voter's 3 / 4 / 5 lands on a
different candidate (Arden > Blythe > Corin > Arden, rock-paper-scissors).

Every deterministic rung comes back level. Scores: 12 = 12 = 12. Pairwise: each
candidate is preferred on 3 of the 9 matchup-ballots, and each wins exactly one
head-to-head 2-1, so the cycle ties on either reading. Five-star: one score-5
vote each. Nothing in the ballots separates the three, so the two seats are
filled entirely by whatever tie-breaking policy was published before the count.

That makes it a clean divergence probe, and the two engines take different
paths to the same pair. BetterVoting SKIPS the pairwise rung whenever more than
two candidates are tied (log `pairwise_too_many_candidates`), falls through
five-star, and settles seat 1 with its seeded random draw
perm = [Blythe, Arden, Corin] -> Blythe, then Arden. The LH engine DOES compute
the pairwise rung, finds it tied 3-3-3, and only then reaches its own
tiebreaker. Pinning lot_numbers to BV's perm reproduces BV exactly.

Also a live repro of the tieBreakType reporting gap already seen on BV130-r2:
round 0 carries `tieBreakType: "random"` and the logs name both draws, but the
top-level `tieBreakType` is `"none"` and `tied` is `[]` — so the summary a
reader sees does not say a seat was decided by lot.

Backs the .starvote input-format page, which runs the same election through
Larry Hastings' own CLI with the tiebreaker switched off, where it refuses to
pick anyone at all:
07_Concepts/tabulation_engines/LH_starvote/starvote_file_format.md

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Arden,Blythe,Corin
3,4,5
5,3,4
4,5,3
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
--- Bloc STAR Voting Method (2 winners) ---

[Bloc STAR]
 Tabulating 3 ballots to fill 2 seats.
Arden,Blythe,Corin
    3,     4,    5
    5,     3,    4
    4,     5,    3

[Bloc STAR: Round 1: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Arden         -- 12 -- Tied for first place
   Blythe        -- 12 -- Tied for first place
   Corin         -- 12 -- Tied for first place
 There's a three-way tie for first.

[Bloc STAR: Round 1: Scoring Round: First tiebreaker]
 The two candidates preferred in the most head-to-head matchups advance.
   Arden         -- 3 -- Tied for first place
   Blythe        -- 3 -- Tied for first place
   Corin         -- 3 -- Tied for first place
   Equal Support -- 0
 There's still a three-way tie for first.

[Bloc STAR: Round 1: Scoring Round: Second tiebreaker]
 The two candidates with the most votes of score 5 advance.
   Arden         -- 1 -- Tied for first place
   Blythe        -- 1 -- Tied for first place
   Corin         -- 1 -- Tied for first place
 There's still a three-way tie for first.

*(Ties are resolved by choosing the tied candidate with the highest-priority official lot number.)*
    Lot-number priority order: ['Blythe', 'Arden', 'Corin']

[Tiebreaker: Lot Number Priority]
  Tie among: ['Arden', 'Blythe', 'Corin']
  Resolved: ['Blythe', 'Arden'] (selected by lot-number priority).

[Lot-decided tie — rare]
  ⚠ The ballots did not break this tie: the deterministic rungs
    (pairwise / score, then five-star) all came back equal, so the
    pre-published LOT order chose among the tied candidates — the
    result here was set by lot, not by the votes. Usually the
    "dead rung": no tied candidate held a score-5 vote (five-star
    counts fives, not fours). Verify the tied candidates' 5-counts.

[Bloc STAR: Round 1: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Blythe        -- 2 -- First place
   Arden         -- 1
   Equal Support -- 0
 Blythe wins.
   Runoff math:
     3  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     3  voters with a preference  (majority = 2)
           Blythe 2 (67%)  ·  Arden 1 (33%)

──────────────────────────────────────────────────

[Bloc STAR: Round 2: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Arden         -- 12 -- First place
   Corin         -- 12 -- Second place
 Arden and Corin advance.

[Bloc STAR: Round 2: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Arden         -- 2 -- First place
   Corin         -- 1
   Equal Support -- 0
 Arden wins.
   Runoff math:
     3  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     3  voters with a preference  (majority = 2)
           Arden 2 (67%)  ·  Corin 1 (33%)

[Bloc STAR: Winners — Bloc STAR Voting Method (2 winners)]
 Blythe
 Arden
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |  * Arden   | * Blythe  |   Corin   |
-----------------------------------------------------
     * Arden > |    ---     |1 - 0 - 2  |2 - 0 - 1  |
    * Blythe > | 2 - 0 - 1  |   ---     |1 - 0 - 2  |
       Corin > | 1 - 0 - 2  |2 - 0 - 1  |   ---     |

[Condorcet Winner]
  No Condorcet winner (majority cycle: Arden > Corin > Blythe > Arden)

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Arden      1  1  1  0  0  0  |    12   4.0
Blythe     1  1  1  0  0  0  |    12   4.0
Corin      1  1  1  0  0  0  |    12   4.0
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/b484mbm_tie_every_rung_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 02_STAR_Bloc/02_Examples/cases/b484mbm_tie_every_rung.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../07_Concepts/topics/condorcet/README.md)
- [Ties & tie-breaking (topic hub)](../../../../07_Concepts/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [00_c3_b3_bloc-baseline-2-seats](00_c3_b3_bloc-baseline-2-seats.md) · [01_c4_b2_bloc-star-2-seats](01_c4_b2_bloc-star-2-seats.md) · [bloc_lot_path_dependence_a_c3_b5](bloc_lot_path_dependence_a_c3_b5.md) · [bloc_lot_path_dependence_b_c3_b5](bloc_lot_path_dependence_b_c3_b5.md) · [bv129_score_tiebreak_bloc](bv129_score_tiebreak_bloc.md) · [bv130_bloc_pagination_731](bv130_bloc_pagination_731.md) · [bv130r2_dead_rung_bloc](bv130r2_dead_rung_bloc.md) · [bv131_guido_bloc](bv131_guido_bloc.md) · [bv132_verify_votes_bloc](bv132_verify_votes_bloc.md) · [bv1525_condorcet_loser_bloc](bv1525_condorcet_loser_bloc.md) · [bv1815_bloc_3c2s_basic](bv1815_bloc_3c2s_basic.md) · [bv1835_8h3yrx_score_leader_no_seat](bv1835_8h3yrx_score_leader_no_seat.md) · [bv2105_r4dqvd_ice_cream_bloc](bv2105_r4dqvd_ice_cream_bloc.md) · [bv2105r2_w3vvff_ice_cream_recheck](bv2105r2_w3vvff_ice_cream_recheck.md) · [bv2269_t488h9_race_nobody_can_lose](bv2269_t488h9_race_nobody_can_lose.md) · [bv750_tie_breaking_bloc](bv750_tie_breaking_bloc.md) · [lackner_skowron_shadow_bloc_star_c7_b12](lackner_skowron_shadow_bloc_star_c7_b12.md) · [race_nobody_can_lose_two_seat_control](race_nobody_can_lose_two_seat_control.md)
