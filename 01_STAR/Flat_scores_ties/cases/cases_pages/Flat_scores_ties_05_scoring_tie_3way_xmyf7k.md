# Flat scores 05 — scoring-round 3-way tie (BV555, xmyf7k)

*Generated from [`Flat_scores_ties_05_scoring_tie_3way_xmyf7k.yaml`](../Flat_scores_ties_05_scoring_tie_3way_xmyf7k.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** A

## Scenario

A 3-way scoring-round tie (A, B, C all at 10) where every score-based tiebreaker
stays tied, so the winner turns on the TERMINAL tiebreak — and that is where LH and
BetterVoting part ways: LH uses a pre-published lot order (deterministic -> A, B
advance, A wins); BV uses a random shuffle (that run: C, A -> C). Same ballots, but
BV's result is NOT reproducible, so this case is LH-ONLY / not freezable (no
_bv_export.json — a random BV winner can't be frozen). The logic divergence is
working-as-intended, not a bug: BV's ties protocol deliberately skips head-to-head
for 3+ way ties (confirmed on #1379, closing WAI); LH's extra head-to-head-among-tied
rung is a no-op here anyway. What stays open is transparency — surfacing BV's
tie-break steps in the results/JSON export — now tracked in #1432 (builds on the
JSON-v2 export in PR #1419). Precedent: the Ranked Robin analog, rr_tiebreak_lh_vs_bv.md.
Level 201/301. Lesson: Flat_scores_ties_05_scoring_tie_3way_xmyf7k.md
BV: https://bettervoting.com/xmyf7k/results

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
A, B, C, D, E
5, 5, 5, 4, 4
5, 5, 5, 4, 4
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 2 ballots.
Count × A,B,C,D,E
    2 × 5,5,5,4,4

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   A             -- 10 -- Tied for first place
   B             -- 10 -- Tied for first place
   C             -- 10 -- Tied for first place
   D             --  8
   E             --  8
 There's a three-way tie for first.

[STAR Voting: Scoring Round: First tiebreaker]
 The two candidates preferred in the most head-to-head matchups advance.
   A             -- 0 -- Tied for first place
   B             -- 0 -- Tied for first place
   C             -- 0 -- Tied for first place
   Equal Support -- 2
 There's still a three-way tie for first.

[STAR Voting: Scoring Round: Second tiebreaker]
 The two candidates with the most votes of score 5 advance.
   A             -- 2 -- Tied for first place
   B             -- 2 -- Tied for first place
   C             -- 2 -- Tied for first place
 There's still a three-way tie for first.

*(Ties are resolved by choosing the tied candidate with the highest-priority official lot number.)*
    Lot-number priority order: ['A', 'B', 'C', 'D', 'E']

[Tiebreaker: Lot Number Priority]
  Tie among: ['A', 'B', 'C']
  Resolved: ['A', 'B'] (selected by lot-number priority).

[Lot-decided tie — rare]
  ⚠ The ballots did not break this tie: the deterministic rungs
    (pairwise / score, then five-star) all came back equal, so the
    pre-published LOT order chose among the tied candidates — the
    result here was set by lot, not by the votes. Usually the
    "dead rung": no tied candidate held a score-5 vote (five-star
    counts fives, not fours). Verify the tied candidates' 5-counts.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   A             -- 0 -- Tied for first place
   B             -- 0 -- Tied for first place
   Equal Support -- 2
 There's a two-way tie for first.

[STAR Voting: Automatic Runoff Round: First tiebreaker]
 The highest-scoring candidate wins.
   A             -- 10 -- Tied for first place
   B             -- 10 -- Tied for first place
 There's still a two-way tie for first.

[STAR Voting: Automatic Runoff Round: Second tiebreaker]
 The candidate with the most votes of score 5 wins.
   A             -- 2 -- Tied for first place
   B             -- 2 -- Tied for first place
 There's still a two-way tie for first.

[Tiebreaker: Lot Number Priority]
  Tie among: ['A', 'B']
  Resolved: ['A'] (selected by lot-number priority).

[Lot-decided tie — rare]
  ⚠ The ballots did not break this tie: the deterministic rungs
    (pairwise / score, then five-star) all came back equal, so the
    pre-published LOT order chose among the tied candidates — the
    result here was set by lot, not by the votes. Usually the
    "dead rung": no tied candidate held a score-5 vote (five-star
    counts fives, not fours). Verify the tied candidates' 5-counts.

[STAR Voting: Winner — STAR Voting Method (single winner)]
 A
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |    * A     |   * B     |     C     |     D     |     E     |
-----------------------------------------------------------------------------
         * A > |    ---     |0 - 2 - 0  |0 - 2 - 0  |2 - 0 - 0  |2 - 0 - 0  |
         * B > | 0 - 2 - 0  |   ---     |0 - 2 - 0  |2 - 0 - 0  |2 - 0 - 0  |
           C > | 0 - 2 - 0  |0 - 2 - 0  |   ---     |2 - 0 - 0  |2 - 0 - 0  |
           D > | 0 - 0 - 2  |0 - 0 - 2  |0 - 0 - 2  |   ---     |0 - 2 - 0  |
           E > | 0 - 0 - 2  |0 - 0 - 2  |0 - 0 - 2  |0 - 2 - 0  |   ---     |

[Condorcet Winner]
  No strict Condorcet winner; unbeaten candidates: A, B, C (pairwise ties)

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
A          2  0  0  0  0  0  |    10   5.0
B          2  0  0  0  0  0  |    10   5.0
C          2  0  0  0  0  0  |    10   5.0
D          0  2  0  0  0  0  |     8   4.0
E          0  2  0  0  0  0  |     8   4.0
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/Flat_scores_ties_05_scoring_tie_3way_xmyf7k_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/Flat_scores_ties/cases/Flat_scores_ties_05_scoring_tie_3way_xmyf7k.yaml
```

## See also

- [Ties & tie-breaking (topic hub)](../../../../00_start_here/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [Flat_scores_ties_01_baseline_clean](Flat_scores_ties_01_baseline_clean.md) · [Flat_scores_ties_02_runoff_tie_2cand](Flat_scores_ties_02_runoff_tie_2cand.md) · [Flat_scores_ties_03_runoff_tie_split](Flat_scores_ties_03_runoff_tie_split.md) · [Flat_scores_ties_04_scoring_tie_2way](Flat_scores_ties_04_scoring_tie_2way.md) · [Flat_scores_ties_06_scoring_tie_4way](Flat_scores_ties_06_scoring_tie_4way.md) · [Flat_scores_ties_07_fully_flat](Flat_scores_ties_07_fully_flat.md) · [Flat_scores_ties_08_all_flat_zero_count](Flat_scores_ties_08_all_flat_zero_count.md)
