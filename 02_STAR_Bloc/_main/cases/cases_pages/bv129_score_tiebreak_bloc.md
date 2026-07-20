# BV129 — Bloc STAR, 3 cand / 2 winners: seat 2 by the score tiebreaker

*Generated from [`bv129_score_tiebreak_bloc.yaml`](../bv129_score_tiebreak_bloc.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Bloc STAR (multi-winner, majoritarian)](../../../../00_start_here/proportional_representation) · **2 seats** · **Expected winners:** Carmen, Andre

## Scenario

The LH reference for BetterVoting test BV129 (real election btmydt). Bloc STAR,
3 candidates, 2 seats, 5 ballots. Totals: Andre=17, Blake=16, Carmen=25.
  - Seat 1: Carmen (25) and Andre (17) advance; Carmen wins the runoff 5-0.
  - Seat 2: remove Carmen -> Andre (17) and Blake (16). In the runoff they TIE
    1-1 (3 ballots are Equal Support). The tie falls to the first runoff rung,
    highest total SCORE: Andre (17) beats Blake (16), so Andre takes seat 2.
Winners: Carmen, Andre. The tie-break is deterministic (the score rung
separates them, 17 vs 16) — no lot involved.

BetterVoting agrees on the result (elected Carmen, Andre; round-1 tieBreakType
"score"). BV129's "Failed" is the method-name label, not the count: the export
reports votingMethod "STAR" rather than "Bloc STAR" (#1086, same family as #904).

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Andre,Blake,Carmen
3,3,5
4,4,5
3,1,5
4,4,5
3,4,5
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR     = Carmen
  Approval = Andre   (differs from STAR)

--- Bloc STAR Voting Method (2 winners) ---

[Bloc STAR]
 Tabulating 5 ballots to fill 2 seats.
Count × Andre,Blake,Carmen
    2 ×     4,    4,     5
    1 ×     3,    3,     5
    1 ×     3,    1,     5
    1 ×     3,    4,     5

[Bloc STAR: Round 1: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Carmen        -- 25 -- First place
   Andre         -- 17 -- Second place
   Blake         -- 16
 Carmen and Andre advance.

[Bloc STAR: Round 1: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Carmen        -- 5 -- First place
   Andre         -- 0
   Equal Support -- 0
 Carmen wins.
   Runoff math:
     5  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     5  voters with a preference  (majority = 3)
           Carmen 5 (100%)  ·  Andre 0 (0%)

──────────────────────────────────────────────────

[Bloc STAR: Round 2: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Andre         -- 17 -- First place
   Blake         -- 16 -- Second place
 Andre and Blake advance.

[Bloc STAR: Round 2: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Andre         -- 1 -- Tied for first place
   Blake         -- 1 -- Tied for first place
   Equal Support -- 3
 There's a two-way tie for first.

[Bloc STAR: Round 2: Automatic Runoff Round: First tiebreaker]
 The highest-scoring candidate wins.
   Andre         -- 17 -- First place
   Blake         -- 16
 Andre wins.

[Bloc STAR: Winners — Bloc STAR Voting Method (2 winners)]
 Carmen
 Andre
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |  * Andre   |   Blake   | * Carmen  |
-----------------------------------------------------
     * Andre > |    ---     |1 - 3 - 1  |0 - 0 - 5  |
       Blake > | 1 - 3 - 1  |   ---     |0 - 0 - 5  |
    * Carmen > | 5 - 0 - 0  |5 - 0 - 0  |   ---     |

[Condorcet Winner]
  Condorcet Winner: Carmen — matches the STAR winner

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Andre      0  2  3  0  0  0  |    17   3.4
Blake      0  3  1  0  1  0  |    16   3.2
Carmen     5  0  0  0  0  0  |    25   5.0
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/bv129_score_tiebreak_bloc_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 02_STAR_Bloc/_main/cases/bv129_score_tiebreak_bloc.yaml
```

## See also

- [Ties & tie-breaking (topic hub)](../../../../00_start_here/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)
- [Runoff reversal (worked set)](../../../../01_STAR/runoff_overturns_leader/README.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [00_c3_b3_bloc-baseline-2-seats](00_c3_b3_bloc-baseline-2-seats.md) · [01_c4_b2_bloc-star-2-seats](01_c4_b2_bloc-star-2-seats.md) · [bv130_bloc_pagination_731](bv130_bloc_pagination_731.md) · [bv130r2_dead_rung_bloc](bv130r2_dead_rung_bloc.md) · [bv131_guido_bloc](bv131_guido_bloc.md) · [bv132_verify_votes_bloc](bv132_verify_votes_bloc.md) · [bv1525_condorcet_loser_bloc](bv1525_condorcet_loser_bloc.md) · [bv1815_bloc_3c2s_basic](bv1815_bloc_3c2s_basic.md) · [bv2105_r4dqvd_ice_cream_bloc](bv2105_r4dqvd_ice_cream_bloc.md) · [bv750_tie_breaking_bloc](bv750_tie_breaking_bloc.md) · [lackner_skowron_shadow_bloc_star_c7_b12](lackner_skowron_shadow_bloc_star_c7_b12.md)
