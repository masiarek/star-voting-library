# Fishburn Ex.14 — Choose-One: A wins on first choices

*Generated from [`bv2160_r6qc8h_plurality.yaml`](../bv2160_r6qc8h_plurality.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [plurality](../../../00_start_here) · **1 seat** · **Expected winner:** A

## Scenario

Race 2 of 2 in the Borda-truncation election (BV2160, bvid r6qc8h; BV-confirmed). Source: Dan S. Felsenthal (2010), Appendix A5, Example 14, adapted from Fishburn (1974: 543) — see bv2160_r6qc8h_star.yaml for the setup.
The same 7 voters under Choose-One: first choices A 3, B 2, C 2 → A. So this tiny cyclic electorate splits three ways across counts: Plurality → A, STAR → B, Borda (on paper) → C — and Borda's C evaporates into an A/B tie if three voters merely truncate. The tabulation, not the ballot, decides.
Live results: https://bettervoting.com/r6qc8h/results

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
A,B,C,D
1,0,0,0
1,0,0,0
1,0,0,0
0,1,0,0
0,1,0,0
0,0,1,0
0,0,1,0
```

## What the engine says

Full report from the [`_tabulated` mirror](../felsenthal_paradoxes_tabulated/bv2160_r6qc8h_plurality_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |    * A     |   * B     |     C     |     D     |
-----------------------------------------------------------------
         * A > |    ---     |3 - 2 - 2  |3 - 2 - 2  |3 - 4 - 0  |
         * B > | 2 - 2 - 3  |   ---     |2 - 3 - 2  |2 - 5 - 0  |
           C > | 2 - 2 - 3  |2 - 3 - 2  |   ---     |2 - 5 - 0  |
           D > | 0 - 4 - 3  |0 - 5 - 2  |0 - 5 - 2  |   ---     |

[Condorcet Winner]
  Condorcet Winner: A — matches the STAR winner

--- Choose-One / Plurality Voting Method (single winner) ---
[STAR Voting]
 Tabulating 7 ballots.
Count × A,B,C,D
    3 × 1,0,0,0
    2 × 0,1,0,0
    2 × 0,0,1,0

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
A          0  0  0  0  3  4  |     3   0.4
B          0  0  0  0  2  5  |     2   0.3
C          0  0  0  0  2  5  |     2   0.3
D          0  0  0  0  0  7  |     0   0.0

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   A             -- 3 -- First place
   B             -- 2 -- Tied for second place
   C             -- 2 -- Tied for second place
   D             -- 0
 A advances, but there's a two-way tie for second.

[STAR Voting: Scoring Round: First tiebreaker]
 The candidate preferred in the most head-to-head matchups advances.
   B             -- 2 -- Tied for second place
   C             -- 2 -- Tied for second place
   Equal Support -- 3
 There's still a two-way tie for second.

[STAR Voting: Scoring Round: Second tiebreaker]
 The candidate with the most votes of score 5 advances.
   B             -- 0 -- Tied for second place
   C             -- 0 -- Tied for second place
 There's still a two-way tie for second.

*** No official tie-breaking lot numbers were provided.
    Ties are resolved using a fallback order: CSV column order.
    Lot-number priority order: ['A', 'B', 'C', 'D']

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

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   A             -- 3 -- First place
   B             -- 2
   Equal Support -- 2
 A wins.
   Runoff math:
     7  ballots cast
   − 2  Equal Support (no preference between the two finalists)
     ─
     5  voters with a preference  (majority = 3)
           A 3 (60%)  ·  B 2 (40%)

[STAR Voting: Winner — Choose-One / Plurality Voting Method (single winner)]
 A
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/felsenthal_paradoxes/bv2160_r6qc8h_plurality.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Ties & tie-breaking (topic hub)](../../../00_start_here/topics/ties/README.md)
- [Vote splitting (worked set)](../../split_voting/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [bv2144_mxfmhm_plurality](bv2144_mxfmhm_plurality.md) · [bv2144_mxfmhm_star](bv2144_mxfmhm_star.md) · [bv2145_6fj2kg_irv](bv2145_6fj2kg_irv.md) · [bv2145_6fj2kg_ranked_robin](bv2145_6fj2kg_ranked_robin.md) · [bv2145_6fj2kg_star](bv2145_6fj2kg_star.md) · [bv2146_krk2px_irv](bv2146_krk2px_irv.md) · [bv2146_krk2px_ranked_robin](bv2146_krk2px_ranked_robin.md) · [bv2146_krk2px_star](bv2146_krk2px_star.md) · [bv2147_9gdrqg_irv](bv2147_9gdrqg_irv.md) · [bv2147_9gdrqg_star](bv2147_9gdrqg_star.md) · [bv2148_h87k6v_irv](bv2148_h87k6v_irv.md) · [bv2148_h87k6v_star](bv2148_h87k6v_star.md) · [bv2149_byk9v2_irv](bv2149_byk9v2_irv.md) · [bv2149_byk9v2_star](bv2149_byk9v2_star.md) · [bv2150_dxg8pb_irv](bv2150_dxg8pb_irv.md) · [bv2150_dxg8pb_ranked_robin](bv2150_dxg8pb_ranked_robin.md) · [bv2150_dxg8pb_star](bv2150_dxg8pb_star.md) · [bv2151_97hbpw_irv](bv2151_97hbpw_irv.md) · [bv2151_97hbpw_ranked_robin](bv2151_97hbpw_ranked_robin.md) · [bv2151_97hbpw_star](bv2151_97hbpw_star.md) · [bv2152_r6ctvy_approval](bv2152_r6ctvy_approval.md) · [bv2152_r6ctvy_ranked_robin](bv2152_r6ctvy_ranked_robin.md) · [bv2153_pcttmr_approval](bv2153_pcttmr_approval.md) · [bv2153_pcttmr_irv](bv2153_pcttmr_irv.md) · [bv2153_pcttmr_ranked_robin](bv2153_pcttmr_ranked_robin.md) · [bv2154_wq6yv7_approval](bv2154_wq6yv7_approval.md) · [bv2154_wq6yv7_irv](bv2154_wq6yv7_irv.md) · [bv2154_wq6yv7_ranked_robin](bv2154_wq6yv7_ranked_robin.md) · [bv2160_r6qc8h_star](bv2160_r6qc8h_star.md) · [bv2161_q3h4fk_plurality](bv2161_q3h4fk_plurality.md) · [bv2161_q3h4fk_star](bv2161_q3h4fk_star.md) · [bv2162_4htk44_irv](bv2162_4htk44_irv.md) · [bv2162_4htk44_ranked_robin](bv2162_4htk44_ranked_robin.md) · [bv2162_4htk44_star](bv2162_4htk44_star.md) · [bv2163_74j6vv_irv](bv2163_74j6vv_irv.md) · [bv2163_74j6vv_ranked_robin](bv2163_74j6vv_ranked_robin.md) · [bv2163_74j6vv_star](bv2163_74j6vv_star.md) · [felsenthal_ex6_pareto_approval](felsenthal_ex6_pareto_approval.md) · [felsenthal_ex6_ranked_robin](felsenthal_ex6_ranked_robin.md)
