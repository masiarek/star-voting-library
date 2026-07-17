# No Condorcet winner (top-two tie) — STAR breaks it by score (BV830, vb3xv2)

*Generated from [`bv830_vb3xv2_no_condorcet_tie_score.yaml`](../bv830_vb3xv2_no_condorcet_tie_score.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** B

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/vb3xv2) · **[results ↗](https://bettervoting.com/vb3xv2/results)** (election `vb3xv2`).

## Scenario

A STAR edge case where the head-to-head standard runs out of data and the
score rung finishes the job. Three voters score three candidates A, B, C:
(0,0,1), (0,2,2), (0,5,0). Scoring round: B totals 7 and C totals 3, so B and
C advance (A gets 0). Automatic runoff: the two finalists tie 1-1-1 head-to-head
— voter 1 prefers C, voter 3 prefers B, voter 2 scores them equally — so neither
beats the other and there is NO strict Condorcet winner. This is a top-two
pairwise tie, not a rock-paper-scissors cycle (the fork says so: "unbeaten
candidates: B, C (pairwise ties)"). STAR breaks the deadlock at the FIRST runoff
rung, the score total: B (7) outscores C (3), so B wins. Lot never reached —
LH and BetterVoting agree deterministically. The lesson: within a Condorcet tie
the ordinal (head-to-head) method is silent, and STAR's score intensity is the
stronger tiebreak. Live results: https://bettervoting.com/vb3xv2/results
Lesson: bv830_vb3xv2_no_condorcet_tie_score.md

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
A, B, C
0, 0, 1
0, 2, 2
0, 5, 0
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 3 ballots.
A,B,C
0,0,1
0,2,2
0,5,0

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   B             -- 7 -- First place
   C             -- 3 -- Second place
   A             -- 0
 B and C advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   B             -- 1 -- Tied for first place
   C             -- 1 -- Tied for first place
   Equal Support -- 1
 There's a two-way tie for first.

[STAR Voting: Automatic Runoff Round: First tiebreaker]
 The highest-scoring candidate wins.
   B             -- 7 -- First place
   C             -- 3
 B wins.

[STAR Voting: Winner — STAR Voting Method (single winner)]
 B
```

<details>
<summary>Full audit — preference matrix, Condorcet, and score distribution</summary>

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |      A     |   * B     |   * C     |
-----------------------------------------------------
           A > |    ---     |0 - 1 - 2  |0 - 1 - 2  |
         * B > | 2 - 1 - 0  |   ---     |1 - 1 - 1  |
         * C > | 2 - 1 - 0  |1 - 1 - 1  |   ---     |

[Condorcet Winner]
  No strict Condorcet winner; unbeaten candidates: B, C (pairwise ties)

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
A          0  0  0  0  0  3  |     0   0.0
B          1  0  0  1  0  1  |     7   2.3
C          0  0  0  1  1  1  |     3   1.0
```

</details>

Everything in one file: the [`_tabulated` mirror](../tie_break_ladder_tabulated/bv830_vb3xv2_no_condorcet_tie_score_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/tie_break_ladder/bv830_vb3xv2_no_condorcet_tie_score.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README.md)
- [Ties & tie-breaking (topic hub)](../../../00_start_here/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)
- [Runoff reversal (worked set)](../../runoff_overturns_leader/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [bv2180_fp62p2_ice_cream_ladder](bv2180_fp62p2_ice_cream_ladder.md)
