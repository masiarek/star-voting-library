# BV1525 — 5 candidates / 4 winners, Bloc STAR (Condorcet-loser ties for seat 1)

*Generated from [`bv1525_condorcet_loser_bloc.yaml`](../bv1525_condorcet_loser_bloc.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Bloc STAR (multi-winner, majoritarian)](../../../../00_start_here/proportional_representation) · **4 seats** · **Expected winners:** First, Second, Third, Fourth

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/dkj9dx) · **[results ↗](https://bettervoting.com/dkj9dx/results)** (election `dkj9dx`).

**Official tie-break (lot) order:** First > Condorcet Loser > Second > Third > Fourth — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

The LH reference for BetterVoting test BV1525 (4 winners, 16 ballots), which
reproduces Larry Hastings' own electowiki Bloc-STAR test election
(test_election_bloc_star_and_electowiki). Five candidates named for their
intended finish — First, Condorcet Loser, Second, Third, Fourth — 16 ballots,
4 seats.

The teaching point (electowiki): a Score co-leader can be a near-CONDORCET
LOSER — a candidate who loses every head-to-head runoff. Here "Condorcet
Loser" ties "First" for the top score (both 24) and so ties for seat 1's
runoff (pairwise 8-8, five-star 0-0). Only the LOT can separate them. With the
pre-published permutation [First, Condorcet Loser, Second, Third, Fourth],
First takes seat 1; Condorcet Loser then LOSES every subsequent runoff and
wins no seat. Winners: First, Second, Third, Fourth.

The lot matters: if Condorcet Loser had won the seat-1 coin toss, the outcome
would be Condorcet Loser, First, Second, Third — the ONLY other valid ordering.
A pre-published lot makes which of the two happens reproducible; a random draw
(as in STAR Vote 2.0) does not, and picks different winners on each run.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
First,Condorcet Loser,Second,Third,Fourth
3,0,1,1,1
3,0,1,1,1
3,0,1,1,1
3,0,1,1,1
3,0,1,1,1
3,0,1,1,1
3,0,1,1,1
3,0,1,1,1
0,4,0,0,0
0,4,0,0,0
0,4,0,0,0
0,4,0,0,0
0,4,0,0,0
0,1,3,2,1
0,1,3,2,1
0,2,5,4,3
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
--- Bloc STAR Voting Method (4 winners) ---

[Bloc STAR]
 Tabulating 16 ballots to fill 4 seats.
Count × First,Condorcet Loser,Second,Third,Fourth
    8 ×     3,              0,     1,    1,     1
    5 ×     0,              4,     0,    0,     0
    2 ×     0,              1,     3,    2,     1
    1 ×     0,              2,     5,    4,     3

[Bloc STAR: Round 1: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Condorcet Loser -- 24 -- First place
   First           -- 24 -- Second place
   Second          -- 19
   Third           -- 16
   Fourth          -- 13
 Condorcet Loser and First advance.

[Bloc STAR: Round 1: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Condorcet Loser -- 8 -- Tied for first place
   First           -- 8 -- Tied for first place
   Equal Support   -- 0
 There's a two-way tie for first.

[Bloc STAR: Round 1: Automatic Runoff Round: First tiebreaker]
 The highest-scoring candidate wins.
   Condorcet Loser -- 24 -- Tied for first place
   First           -- 24 -- Tied for first place
 There's still a two-way tie for first.

[Bloc STAR: Round 1: Automatic Runoff Round: Second tiebreaker]
 The candidate with the most votes of score 5 wins.
   Condorcet Loser -- 0 -- Tied for first place
   First           -- 0 -- Tied for first place
 There's still a two-way tie for first.

*(Ties are resolved by choosing the tied candidate with the highest-priority official lot number.)*
    Lot-number priority order: ['First', 'Condorcet Loser', 'Second', 'Third', 'Fourth']

[Tiebreaker: Lot Number Priority]
  Tie among: ['Condorcet Loser', 'First']
  Resolved: ['First'] (selected by lot-number priority).

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
   Condorcet Loser -- 24 -- First place
   Second          -- 19 -- Second place
   Third           -- 16
   Fourth          -- 13
 Condorcet Loser and Second advance.

[Bloc STAR: Round 2: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Second          -- 11 -- First place
   Condorcet Loser --  5
   Equal Support   --  0
 Second wins.
   Runoff math:
     16  ballots cast
   −  0  Equal Support (no preference between the two finalists)
     ──
     16  voters with a preference  (majority = 9)
           Second 11 (69%)  ·  Condorcet Loser 5 (31%)

──────────────────────────────────────────────────

[Bloc STAR: Round 3: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Condorcet Loser -- 24 -- First place
   Third           -- 16 -- Second place
   Fourth          -- 13
 Condorcet Loser and Third advance.

[Bloc STAR: Round 3: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Third           -- 11 -- First place
   Condorcet Loser --  5
   Equal Support   --  0
 Third wins.
   Runoff math:
     16  ballots cast
   −  0  Equal Support (no preference between the two finalists)
     ──
     16  voters with a preference  (majority = 9)
           Third 11 (69%)  ·  Condorcet Loser 5 (31%)

──────────────────────────────────────────────────

[Bloc STAR: Round 4: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Condorcet Loser -- 24 -- First place
   Fourth          -- 13 -- Second place
 Condorcet Loser and Fourth advance.

[Bloc STAR: Round 4: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Fourth          -- 9 -- First place
   Condorcet Loser -- 5
   Equal Support   -- 2
 Fourth wins.
   Runoff math:
     16  ballots cast
   −  2  Equal Support (no preference between the two finalists)
     ──
     14  voters with a preference  (majority = 8)
           Fourth 9 (64%)  ·  Condorcet Loser 5 (36%)

[Bloc STAR: Winners — Bloc STAR Voting Method (4 winners)]
 First
 Second
 Third
 Fourth
```

<details>
<summary>Full audit — preference matrix, Condorcet, and score distribution</summary>

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                        |       * First       | * Condorcet Loser  |       Second       |        Third       |       Fourth       |
-----------------------------------------------------------------------------------------------------------------------------------
              * First > |         ---         |    8 -  0 -  8     |    8 -  5 -  3     |    8 -  5 -  3     |    8 -  5 -  3     |
    * Condorcet Loser > |     8 -  0 -  8     |        ---         |    5 -  0 - 11     |    5 -  0 - 11     |    5 -  2 -  9     |
               Second > |     3 -  5 -  8     |   11 -  0 -  5     |        ---         |    3 - 13 -  0     |    3 - 13 -  0     |
                Third > |     3 -  5 -  8     |   11 -  0 -  5     |    0 - 13 -  3     |        ---         |    3 - 13 -  0     |
               Fourth > |     3 -  5 -  8     |    9 -  2 -  5     |    0 - 13 -  3     |    0 - 13 -  3     |        ---         |

[Condorcet Winner]
  No strict Condorcet winner; weak Condorcet winner: First — matches the STAR winner

[Score Distribution] (how many ballots gave each star rating)
                         Score
Candidate         5   4   3   2   1   0  | Total   Avg
First             0   0   8   0   0   8  |    24   1.5
Condorcet Loser   0   5   0   1   2   8  |    24   1.5
Second            1   0   2   0   8   5  |    19   1.2
Third             0   1   0   2   8   5  |    16   1.0
Fourth            0   0   1   0  10   5  |    13   0.8
```

</details>

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/bv1525_condorcet_loser_bloc_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 02_STAR_Bloc/_main/cases/bv1525_condorcet_loser_bloc.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../00_start_here/topics/condorcet/README.md)
- [Ties & tie-breaking (topic hub)](../../../../00_start_here/topics/ties/README.md)
- [Runoff reversal (worked set)](../../../../01_STAR/runoff_overturns_leader/README.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [00_c3_b3_bloc-baseline-2-seats](00_c3_b3_bloc-baseline-2-seats.md) · [01_c4_b2_bloc-star-2-seats](01_c4_b2_bloc-star-2-seats.md) · [bv129_score_tiebreak_bloc](bv129_score_tiebreak_bloc.md) · [bv130_bloc_pagination_731](bv130_bloc_pagination_731.md) · [bv130r2_dead_rung_bloc](bv130r2_dead_rung_bloc.md) · [bv131_guido_bloc](bv131_guido_bloc.md) · [bv132_verify_votes_bloc](bv132_verify_votes_bloc.md) · [bv1815_bloc_3c2s_basic](bv1815_bloc_3c2s_basic.md) · [bv2105_r4dqvd_ice_cream_bloc](bv2105_r4dqvd_ice_cream_bloc.md) · [bv750_tie_breaking_bloc](bv750_tie_breaking_bloc.md) · [lackner_skowron_shadow_bloc_star_c7_b12](lackner_skowron_shadow_bloc_star_c7_b12.md)
