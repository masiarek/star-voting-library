# Shadow STAR-PR (RRV) — Lackner & Skowron's running example (k=4) — matches PAV

*Generated from [`lackner_skowron_shadow_star_pr_rrv_c7_b12.yaml`](../lackner_skowron_shadow_star_pr_rrv_c7_b12.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Reweighted Range Voting (proportional STAR)](../../../00_start_here/proportional_representation) · **4 seats** · **Expected winners:** A, B, C, F

**Official tie-break (lot) order:** A > B > C > D > E > F > G — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

Lackner & Skowron's Example 2.1 (k=4 steering committee, 7 candidates, 12
ballots), approval profile read as STAR ballots (approved = 5, else 0),
tabulated with Reweighted Range Voting (RRV) — one of STAR's proportional
variants.

Unlike the other STAR-family rules on this profile (Bloc STAR, Allocated Score,
and SSS all seat A,B,C,D), RRV seats A,B,C,F — the SAME committee the book's
PAV elects (Example 2.4). Seating F gives the two {*,F} voters representation
the majoritarian committee denies them; the 4th seat (D vs F) is exactly where
loosely- vs fully-proportional rules diverge.

Companions: majoritarian shadow (Bloc STAR) and the Allocated Score shadow both
give A,B,C,D — see lackner_skowron_shadow_star_pr_c7_b12.yaml and
../../02_STAR_Bloc/_main/lackner_skowron_shadow_bloc_star_c7_b12.yaml. Approval
original: ../../04_Approval/multiwinner/approval_bloc_4seats_c7_b12_lackner_skowron.yaml.

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
--- Reweighted Range Voting Method (4 winners) ---

[Reweighted Range Voting]
 Tabulating 12 ballots to fill 4 seats.
Count × A,B,C,D,E,F,G
    3 × 5,5,0,0,0,0,0
    3 × 5,0,5,0,0,0,0
    2 × 5,0,0,5,0,0,0
    1 × 0,5,5,0,0,5,0
    1 × 0,0,0,0,5,0,0
    1 × 0,0,0,0,0,5,0
    1 × 0,0,0,0,0,0,5

[Reweighted Range Voting: Round 1: Score round]
 The highest-scoring candidate wins a seat.
   A             -- 40 -- First place
   B             -- 20
   C             -- 20
   D             -- 10
   F             -- 10
   E             --  5
   G             --  5
 A wins a seat.

[Reweighted Range Voting: Round 1: Reweighing Ballots]
 8 ballots reweighted from 1 to 1/2.

[Reweighted Range Voting: Round 2: Score round]
 The highest-scoring candidate wins a seat.
   B             -- 12+1/2 -- Tied for first place
   C             -- 12+1/2 -- Tied for first place
   F             -- 10
   D             --  5
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

[Reweighted Range Voting: Round 2: Reweighing Ballots]
 Reweighted 4 ballots:
   3 ballots reweighted from 1/2 to 1/3.
   1 ballot reweighted from 1 to 1/2.

[Reweighted Range Voting: Round 3: Score round]
 The highest-scoring candidate wins a seat.
   C             -- 10     -- First place
   F             --  7+1/2
   D             --  5
   E             --  5
   G             --  5
 C wins a seat.

[Reweighted Range Voting: Round 3: Reweighing Ballots]
 4 ballots reweighted from 1/2 to 1/3.

[Reweighted Range Voting: Round 4: Score round]
 The highest-scoring candidate wins a seat.
   F             -- 6+2/3 -- First place
   D             -- 5
   E             -- 5
   G             -- 5
 F wins a seat.

[Reweighted Range Voting: Winners — Reweighted Range Voting Method (4 winners)]
 A
 B
 C
 F
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

Everything in one file: the [`_tabulated` mirror](../_main_tabulated/lackner_skowron_shadow_star_pr_rrv_c7_b12_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 03_STAR_PR/_main/lackner_skowron_shadow_star_pr_rrv_c7_b12.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [02a_c5_b63_proportional-allocated-score](02a_c5_b63_proportional-allocated-score.md) · [02b_c5_b63_proportional-sss](02b_c5_b63_proportional-sss.md) · [02c_c5_b63_proportional-rrv](02c_c5_b63_proportional-rrv.md) · [03b_star_pr_3seats](03b_star_pr_3seats.md) · [bv2130_bvhchj_party_plurality](bv2130_bvhchj_party_plurality.md) · [bv2130_presidential_board_star_pr](bv2130_presidential_board_star_pr.md) · [lackner_skowron_shadow_star_pr_c7_b12](lackner_skowron_shadow_star_pr_c7_b12.md) · [rrv_sample_c15_b13_three-parties](rrv_sample_c15_b13_three-parties.md)
