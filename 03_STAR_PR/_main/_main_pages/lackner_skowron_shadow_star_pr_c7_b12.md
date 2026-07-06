# Shadow STAR-PR (Allocated Score) — Lackner & Skowron's running example (k=4)

*Generated from [`lackner_skowron_shadow_star_pr_c7_b12.yaml`](../lackner_skowron_shadow_star_pr_c7_b12.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Allocated Score (proportional STAR)](../../../00_start_here/proportional_representation) · **4 seats** · **Expected winners:** A, B, C, D

**Official tie-break (lot) order:** A > B > C > D > E > F > G — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

The PROPORTIONAL shadow STAR of Lackner & Skowron's Example 2.1 (k=4
steering committee, 7 candidates, 12 ballots). Same approval profile, read as
STAR ballots (approved = 5, else 0), but tabulated with Proportional STAR
(Allocated Score / STAR-PR) instead of the majoritarian Bloc STAR.

This is the STAR-family parallel to the book's PAV: after a faction helps elect
a candidate, its ballots are spent/reweighted, so later seats go to
under-represented voters. Where Bloc STAR / AV seat A, B, C, D (the big
A-approving bloc takes 3 of 4 seats and D fills the 4th), the proportional rule
is expected to seat someone for the small factions instead — compare against
PAV's {A,B,C,F} in the book (Example 2.4).

Approval original: 04_Approval/multiwinner/approval_bloc_4seats_c7_b12_lackner_skowron.yaml
Majoritarian shadow (Bloc STAR): 02_STAR_Bloc/_main/lackner_skowron_shadow_bloc_star_c7_b12.yaml

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

Full report from the [`_tabulated` mirror](../_main_tabulated/lackner_skowron_shadow_star_pr_c7_b12_tabulated.txt) (regenerated on every run; every analysis forced on):

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

--- Allocated Score Voting Method (4 winners) ---
[Allocated Score Voting]
 Tabulating 12 ballots to fill 4 seats.
Count × A,B,C,D,E,F,G
    3 × 5,5,0,0,0,0,0
    3 × 5,0,5,0,0,0,0
    2 × 5,0,0,5,0,0,0
    1 × 0,5,5,0,0,5,0
    1 × 0,0,0,0,5,0,0
    1 × 0,0,0,0,0,5,0
    1 × 0,0,0,0,0,0,5

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
 Hare quota is 3.

[Allocated Score Voting: Round 1]
 The highest-scoring candidate wins a seat.
   A             -- 40 -- First place
   B             -- 20
   C             -- 20
   D             -- 10
   F             -- 10
   E             --  5
   G             --  5
 A wins a seat.

[Allocated Score Voting: Round 1: Ballot allocation round]
 Allocating 3 ballots.

[Allocated Score Voting: Round 1: Ballot allocation round: Round 1]
 Allocating 8 ballots at score 5.
 This allocation overfills the quota.  Returning fractional surplus.
 Allocating only 37.50% of these ballots.
 Keeping these ballots, but multiplying their weights by 5/8.
 8 ballots reweighted from 1 to 5/8.

[Allocated Score Voting: Round 2]
 The highest-scoring candidate wins a seat.
   B             -- 14+3/8 -- Tied for first place
   C             -- 14+3/8 -- Tied for first place
   F             -- 10
   D             --  6+1/4
   E             --  5
   G             --  5
 There's a two-way tie for first.

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

[Allocated Score Voting: Round 2: Ballot allocation round]
 Allocating 3 ballots.

[Allocated Score Voting: Round 2: Ballot allocation round: Round 1]
 Allocating 1 ballot at score 5.

[Allocated Score Voting: Round 2: Ballot allocation round: Round 2]
 Remaining allocation quota is 2.
 Allocating 3 ballots at score 25/8.
 This allocation overfills the remaining quota.  Returning fractional surplus.
 Allocating only 66.67% of these ballots.
 Keeping these ballots, but multiplying their weights by 1/3.
 3 ballots reweighted from 5/8 to 5/24.

[Allocated Score Voting: Round 3]
 Tabulating 11 remaining ballots.
Count × A,B,C,D,E,F,G
    3 × 5,5,0,0,0,0,0
    3 × 5,0,5,0,0,0,0
    2 × 5,0,0,5,0,0,0
    1 × 0,5,5,0,0,5,0
    1 × 0,0,0,0,5,0,0
    1 × 0,0,0,0,0,5,0
    1 × 0,0,0,0,0,0,5

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
 The highest-scoring candidate wins a seat.
   C             -- 9+3/8 -- First place
   D             -- 6+1/4
   E             -- 5
   F             -- 5
   G             -- 5
 C wins a seat.

[Allocated Score Voting: Round 3: Ballot allocation round]
 Allocating 3 ballots.

[Allocated Score Voting: Round 3: Ballot allocation round: Round 1]
 Allocating 3 ballots at score 25/8.

[Allocated Score Voting: Round 4]
 Tabulating 8 remaining ballots.
Count × A,B,C,D,E,F,G
    3 × 5,5,0,0,0,0,0
    3 × 5,0,5,0,0,0,0
    2 × 5,0,0,5,0,0,0
    1 × 0,5,5,0,0,5,0
    1 × 0,0,0,0,5,0,0
    1 × 0,0,0,0,0,5,0
    1 × 0,0,0,0,0,0,5

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
 The highest-scoring candidate wins a seat.
   D             -- 6+1/4 -- First place
   E             -- 5
   F             -- 5
   G             -- 5
 D wins a seat.

[Allocated Score Voting: Winners — Allocated Score Voting Method (4 winners)]
 A
 B
 C
 D
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 03_STAR_PR/_main/lackner_skowron_shadow_star_pr_c7_b12.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [02a_c5_b63_proportional-allocated-score](02a_c5_b63_proportional-allocated-score.md) · [02b_c5_b63_proportional-sss](02b_c5_b63_proportional-sss.md) · [02c_c5_b63_proportional-rrv](02c_c5_b63_proportional-rrv.md) · [03b_star_pr_3seats](03b_star_pr_3seats.md) · [bv2130_presidential_board_star_pr](bv2130_presidential_board_star_pr.md) · [lackner_skowron_shadow_star_pr_rrv_c7_b12](lackner_skowron_shadow_star_pr_rrv_c7_b12.md) · [rrv_sample_c15_b13_three-parties](rrv_sample_c15_b13_three-parties.md)
