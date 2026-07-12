# Three-way dead-rung tie — published order C,A,B elects C

*Generated from [`three_way_dead_rung_C.yaml`](../three_way_dead_rung_C.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** C

**Official tie-break (lot) order:** C > A > B — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

The SAME rotationally-symmetric three-candidate dead-rung tie as
three_way_dead_rung_A.yaml (A 4/0/0, B 0/4/0, C 0/0/4 — totals 4-4-4, all
pairwise 1-1, no 5s so the five-star rung is dead). Only the lot order changes:
here it is [C, A, B], so C wins. Same ballots as _A (elects A) and _B (elects
B): three candidates, three possible winners, chosen entirely by the lot order.
A random tie-break would pick one at 1-in-3; a published lot fixes it. See the
lesson md and BV #1063.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
A,B,C
4,0,0
0,4,0
0,0,4
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR    = C
  RCV-IRV = B   (differs from STAR)
  Note: no ballots had tied scores, so RCV-IRV vs STAR here is a genuine
        method difference, not a tie-breaking artifact.
  Note: Ranked Robin (RCV-RR) agrees with STAR, so RCV-IRV is the lone
        outlier — the classic center-squeeze signature.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: three_way_dead_rung_tie_tabulated/three_way_dead_rung_C_RCV-IRV_tabulated.txt

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 3 ballots.
A,B,C
4,0,0
0,4,0
0,0,4

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   A             -- 4 -- Tied for first place
   B             -- 4 -- Tied for first place
   C             -- 4 -- Tied for first place
 There's a three-way tie for first.

[STAR Voting: Scoring Round: First tiebreaker]
 The two candidates preferred in the most head-to-head matchups advance.
   A             -- 2 -- Tied for first place
   B             -- 2 -- Tied for first place
   C             -- 2 -- Tied for first place
   Equal Support -- 0
 There's still a three-way tie for first.

[STAR Voting: Scoring Round: Second tiebreaker]
 The two candidates with the most votes of score 5 advance.
   A             -- 0 -- Tied for first place
   B             -- 0 -- Tied for first place
   C             -- 0 -- Tied for first place
 There's still a three-way tie for first.

*(Ties are resolved by choosing the tied candidate with the highest-priority official lot number.)*
    Lot-number priority order: ['C', 'A', 'B']

[Tiebreaker: Lot Number Priority]
  Tie among: ['A', 'B', 'C']
  Resolved: ['C', 'A'] (selected by lot-number priority).

[Lot-decided tie — rare]
  ⚠ The ballots did not break this tie: the deterministic rungs
    (pairwise / score, then five-star) all came back equal, so the
    pre-published LOT order chose among the tied candidates — the
    result here was set by lot, not by the votes. Usually the
    "dead rung": no tied candidate held a score-5 vote (five-star
    counts fives, not fours). Verify the tied candidates' 5-counts.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   A             -- 1 -- Tied for first place
   C             -- 1 -- Tied for first place
   Equal Support -- 1
 There's a two-way tie for first.

[STAR Voting: Automatic Runoff Round: First tiebreaker]
 The highest-scoring candidate wins.
   A             -- 4 -- Tied for first place
   C             -- 4 -- Tied for first place
 There's still a two-way tie for first.

[STAR Voting: Automatic Runoff Round: Second tiebreaker]
 The candidate with the most votes of score 5 wins.
   A             -- 0 -- Tied for first place
   C             -- 0 -- Tied for first place
 There's still a two-way tie for first.

[Tiebreaker: Lot Number Priority]
  Tie among: ['A', 'C']
  Resolved: ['C'] (selected by lot-number priority).

[Lot-decided tie — rare]
  ⚠ The ballots did not break this tie: the deterministic rungs
    (pairwise / score, then five-star) all came back equal, so the
    pre-published LOT order chose among the tied candidates — the
    result here was set by lot, not by the votes. Usually the
    "dead rung": no tied candidate held a score-5 vote (five-star
    counts fives, not fours). Verify the tied candidates' 5-counts.

[STAR Voting: Winner — STAR Voting Method (single winner)]
 C
```

<details>
<summary>▸ Full audit — preference matrix, Condorcet, and score distribution</summary>

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |    * A     |     B     |   * C     |
-----------------------------------------------------
         * A > |    ---     |1 - 1 - 1  |1 - 1 - 1  |
           B > | 1 - 1 - 1  |   ---     |1 - 1 - 1  |
         * C > | 1 - 1 - 1  |1 - 1 - 1  |   ---     |

[Condorcet Winner]
  No strict Condorcet winner; unbeaten candidates: A, B, C (pairwise ties)

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
A          0  1  0  0  0  2  |     4   1.3
B          0  1  0  0  0  2  |     4   1.3
C          0  1  0  0  0  2  |     4   1.3
```

</details>

Everything in one file: the [`_tabulated` mirror](../three_way_dead_rung_tie_tabulated/three_way_dead_rung_C_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/tie_break_dead_rung/three_way_dead_rung_tie/three_way_dead_rung_C.yaml
```

## See also

- [Ties & tie-breaking (topic hub)](../../../../00_start_here/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [three_way_dead_rung_A](three_way_dead_rung_A.md) · [three_way_dead_rung_B](three_way_dead_rung_B.md)
