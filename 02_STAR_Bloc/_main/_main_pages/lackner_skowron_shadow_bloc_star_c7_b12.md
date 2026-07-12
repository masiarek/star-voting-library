# Shadow STAR (Bloc) — Lackner & Skowron's running example (k=4)

*Generated from [`lackner_skowron_shadow_bloc_star_c7_b12.yaml`](../lackner_skowron_shadow_bloc_star_c7_b12.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Bloc STAR (multi-winner, majoritarian)](../../../00_start_here/proportional_representation) · **4 seats** · **Expected winners:** A, B, C, D

**Official tie-break (lot) order:** A > B > C > D > E > F > G — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

A "shadow STAR" of Lackner & Skowron's Example 2.1 (the k=4 steering-committee
approval profile, 7 candidates, 12 ballots) — see the approval original at
04_Approval/multiwinner/approval_bloc_4seats_c7_b12_lackner_skowron.yaml.

The approval ballots are read as STAR ballots: an APPROVED candidate scores 5,
an unapproved one scores 0. This asks "what committee would Bloc STAR pick from
the very same voters, if approve/not-approve were the only two scores used?"

Bloc STAR is majoritarian (like Bloc Approval / AV), so it favors the big
A-approving bloc. Compare with the proportional STAR analog (STAR-PR /
Allocated Score) at 03_STAR_PR/_main/lackner_skowron_shadow_star_pr_c7_b12.yaml,
which is the STAR-family parallel to the book's PAV. lot_numbers [A..G] pins any
ties to alphabetical priority (matching the approval file's D-over-F choice).

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
A,B,C,D,E,F,G
5,5,0,0,0,0,0
5,5,0,0,0,0,0
5,5,0,0,0,0,0
5,0,5,0,0,0,0
5,0,5,0,0,0,0
5,0,5,0,0,0,0
5,0,0,5,0,0,0
5,0,0,5,0,0,0
0,5,5,0,0,5,0
0,0,0,0,5,0,0
0,0,0,0,0,5,0
0,0,0,0,0,0,5
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
--- Bloc STAR Voting Method (4 winners) ---

[Bloc STAR]
 Tabulating 12 ballots to fill 4 seats.
Count × A,B,C,D,E,F,G
    3 × 5,5,0,0,0,0,0
    3 × 5,0,5,0,0,0,0
    2 × 5,0,0,5,0,0,0
    1 × 0,5,5,0,0,5,0
    1 × 0,0,0,0,5,0,0
    1 × 0,0,0,0,0,5,0
    1 × 0,0,0,0,0,0,5

[Bloc STAR: Round 1: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   A             -- 40 -- First place
   B             -- 20 -- Tied for second place
   C             -- 20 -- Tied for second place
   D             -- 10
   F             -- 10
   E             --  5
   G             --  5
 A advances, but there's a two-way tie for second.

[Bloc STAR: Round 1: Scoring Round: First tiebreaker]
 The candidate preferred in the most head-to-head matchups advances.
   B             -- 3 -- Tied for second place
   C             -- 3 -- Tied for second place
   Equal Support -- 6
 There's still a two-way tie for second.

[Bloc STAR: Round 1: Scoring Round: Second tiebreaker]
 The candidate with the most votes of score 5 advances.
   B             -- 4 -- Tied for second place
   C             -- 4 -- Tied for second place
 There's still a two-way tie for second.

*(Ties are resolved by choosing the tied candidate with the highest-priority official lot number.)*
    Lot-number priority order: ['A', 'B', 'C', 'D', 'E', 'F', 'G']

[Tiebreaker: Lot Number Priority]
  Tie among: ['B', 'C']
  Resolved: ['B'] (selected by lot-number priority).

[Lot-decided tie — rare]
  ⚠ The ballots did not break this tie: the deterministic rungs
    (pairwise / score, then five-star) all came back equal, so the
    pre-published LOT order chose among the tied candidates — the
    result here was set by lot, not by the votes. Usually the
    "dead rung": no tied candidate held a score-5 vote (five-star
    counts fives, not fours). Verify the tied candidates' 5-counts.

[Bloc STAR: Round 1: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   A             -- 5 -- First place
   B             -- 1
   Equal Support -- 6
 A wins.
   Runoff math:
     12  ballots cast
   −  6  Equal Support (no preference between the two finalists)
     ──
      6  voters with a preference  (majority = 4)
           A 5 (83%)  ·  B 1 (17%)

──────────────────────────────────────────────────

[Bloc STAR: Round 2: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   B             -- 20 -- First place
   C             -- 20 -- Second place
   D             -- 10
   F             -- 10
   E             --  5
   G             --  5
 B and C advance.

[Bloc STAR: Round 2: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   B             -- 3 -- Tied for first place
   C             -- 3 -- Tied for first place
   Equal Support -- 6
 There's a two-way tie for first.

[Bloc STAR: Round 2: Automatic Runoff Round: First tiebreaker]
 The highest-scoring candidate wins.
   B             -- 20 -- Tied for first place
   C             -- 20 -- Tied for first place
 There's still a two-way tie for first.

[Bloc STAR: Round 2: Automatic Runoff Round: Second tiebreaker]
 The candidate with the most votes of score 5 wins.
   B             -- 4 -- Tied for first place
   C             -- 4 -- Tied for first place
 There's still a two-way tie for first.

[Tiebreaker: Lot Number Priority]
  Tie among: ['B', 'C']
  Resolved: ['B'] (selected by lot-number priority).

[Lot-decided tie — rare]
  ⚠ The ballots did not break this tie: the deterministic rungs
    (pairwise / score, then five-star) all came back equal, so the
    pre-published LOT order chose among the tied candidates — the
    result here was set by lot, not by the votes. Usually the
    "dead rung": no tied candidate held a score-5 vote (five-star
    counts fives, not fours). Verify the tied candidates' 5-counts.

──────────────────────────────────────────────────

[Bloc STAR: Round 3: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   C             -- 20 -- First place
   D             -- 10 -- Tied for second place
   F             -- 10 -- Tied for second place
   E             --  5
   G             --  5
 C advances, but there's a two-way tie for second.

[Bloc STAR: Round 3: Scoring Round: First tiebreaker]
 The candidate preferred in the most head-to-head matchups advances.
   D             -- 2 -- Tied for second place
   F             -- 2 -- Tied for second place
   Equal Support -- 8
 There's still a two-way tie for second.

[Bloc STAR: Round 3: Scoring Round: Second tiebreaker]
 The candidate with the most votes of score 5 advances.
   D             -- 2 -- Tied for second place
   F             -- 2 -- Tied for second place
 There's still a two-way tie for second.

[Tiebreaker: Lot Number Priority]
  Tie among: ['D', 'F']
  Resolved: ['D'] (selected by lot-number priority).

[Lot-decided tie — rare]
  ⚠ The ballots did not break this tie: the deterministic rungs
    (pairwise / score, then five-star) all came back equal, so the
    pre-published LOT order chose among the tied candidates — the
    result here was set by lot, not by the votes. Usually the
    "dead rung": no tied candidate held a score-5 vote (five-star
    counts fives, not fours). Verify the tied candidates' 5-counts.

[Bloc STAR: Round 3: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   C             -- 4 -- First place
   D             -- 2
   Equal Support -- 6
 C wins.
   Runoff math:
     12  ballots cast
   −  6  Equal Support (no preference between the two finalists)
     ──
      6  voters with a preference  (majority = 4)
           C 4 (67%)  ·  D 2 (33%)

──────────────────────────────────────────────────

[Bloc STAR: Round 4: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   D             -- 10 -- First place
   F             -- 10 -- Second place
   E             --  5
   G             --  5
 D and F advance.

[Bloc STAR: Round 4: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   D             -- 2 -- Tied for first place
   F             -- 2 -- Tied for first place
   Equal Support -- 8
 There's a two-way tie for first.

[Bloc STAR: Round 4: Automatic Runoff Round: First tiebreaker]
 The highest-scoring candidate wins.
   D             -- 10 -- Tied for first place
   F             -- 10 -- Tied for first place
 There's still a two-way tie for first.

[Bloc STAR: Round 4: Automatic Runoff Round: Second tiebreaker]
 The candidate with the most votes of score 5 wins.
   D             -- 2 -- Tied for first place
   F             -- 2 -- Tied for first place
 There's still a two-way tie for first.

[Tiebreaker: Lot Number Priority]
  Tie among: ['D', 'F']
  Resolved: ['D'] (selected by lot-number priority).

[Lot-decided tie — rare]
  ⚠ The ballots did not break this tie: the deterministic rungs
    (pairwise / score, then five-star) all came back equal, so the
    pre-published LOT order chose among the tied candidates — the
    result here was set by lot, not by the votes. Usually the
    "dead rung": no tied candidate held a score-5 vote (five-star
    counts fives, not fours). Verify the tied candidates' 5-counts.

[Bloc STAR: Winners — Bloc STAR Voting Method (4 winners)]
 A
 B
 C
 D
```

<details>
<summary>▸ Full audit — preference matrix, Condorcet, and score distribution</summary>

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |     * A      |    * B      |      C      |      D      |      E      |      F      |      G      |
---------------------------------------------------------------------------------------------------------------------
           * A > |     ---      | 5 -  6 -  1 | 5 -  6 -  1 | 6 -  6 -  0 | 8 -  3 -  1 | 8 -  2 -  2 | 8 -  3 -  1 |
           * B > |  1 -  6 -  5 |    ---      | 3 -  6 -  3 | 4 -  6 -  2 | 4 -  7 -  1 | 3 -  8 -  1 | 4 -  7 -  1 |
             C > |  1 -  6 -  5 | 3 -  6 -  3 |    ---      | 4 -  6 -  2 | 4 -  7 -  1 | 3 -  8 -  1 | 4 -  7 -  1 |
             D > |  0 -  6 -  6 | 2 -  6 -  4 | 2 -  6 -  4 |    ---      | 2 -  9 -  1 | 2 -  8 -  2 | 2 -  9 -  1 |
             E > |  1 -  3 -  8 | 1 -  7 -  4 | 1 -  7 -  4 | 1 -  9 -  2 |    ---      | 1 -  9 -  2 | 1 - 10 -  1 |
             F > |  2 -  2 -  8 | 1 -  8 -  3 | 1 -  8 -  3 | 2 -  8 -  2 | 2 -  9 -  1 |    ---      | 2 -  9 -  1 |
             G > |  1 -  3 -  8 | 1 -  7 -  4 | 1 -  7 -  4 | 1 -  9 -  2 | 1 - 10 -  1 | 1 -  9 -  2 |    ---      |

[Condorcet Winner]
  Condorcet Winner: A — matches the STAR winner

[Score Distribution] (how many ballots gave each star rating)
                   Score
Candidate   5   4   3   2   1   0  | Total   Avg
A           8   0   0   0   0   4  |    40   3.3
B           4   0   0   0   0   8  |    20   1.7
C           4   0   0   0   0   8  |    20   1.7
D           2   0   0   0   0  10  |    10   0.8
E           1   0   0   0   0  11  |     5   0.4
F           2   0   0   0   0  10  |    10   0.8
G           1   0   0   0   0  11  |     5   0.4
```

</details>

Everything in one file: the [`_tabulated` mirror](../_main_tabulated/lackner_skowron_shadow_bloc_star_c7_b12_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 02_STAR_Bloc/_main/lackner_skowron_shadow_bloc_star_c7_b12.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Ties & tie-breaking (topic hub)](../../../00_start_here/topics/ties/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [00_c3_b3_bloc-baseline-2-seats](00_c3_b3_bloc-baseline-2-seats.md) · [01_c4_b2_bloc-star-2-seats](01_c4_b2_bloc-star-2-seats.md) · [bv129_score_tiebreak_bloc](bv129_score_tiebreak_bloc.md) · [bv130_bloc_pagination_731](bv130_bloc_pagination_731.md) · [bv130r2_dead_rung_bloc](bv130r2_dead_rung_bloc.md) · [bv131_guido_bloc](bv131_guido_bloc.md) · [bv132_verify_votes_bloc](bv132_verify_votes_bloc.md) · [bv1525_condorcet_loser_bloc](bv1525_condorcet_loser_bloc.md) · [bv1815_bloc_3c2s_basic](bv1815_bloc_3c2s_basic.md) · [bv2105_r4dqvd_ice_cream_bloc](bv2105_r4dqvd_ice_cream_bloc.md) · [bv750_tie_breaking_bloc](bv750_tie_breaking_bloc.md)
