# Coombs Ex.19 no-show — Choose-One: still Cass, unmoved

*Generated from [`bv2166_b7b8dv_plurality.yaml`](../bv2166_b7b8dv_plurality.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [plurality](../../../00_start_here) · **1 seat** · **Expected winner:** Cass

## Scenario

Race 2 of 2 in the Coombs No-Show pair, part 2 of 2 (BV2166, bvid b7b8dv; BV-confirmed). Source: Dan S. Felsenthal (2010), Appendix A7, Example 19 (continued) — see bv2166_b7b8dv_star.yaml for the setup.
The 13 remaining voters under Choose-One: first choices Amy 4, Boone 4, Cass 5 → Cass, exactly as with all 15 (BV2165). The first-choice count never wavers; the no-show flips live in Coombs' elimination (on paper) and STAR's runoff (live).
Live results: https://bettervoting.com/b7b8dv/results

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Amy,Boone,Cass
1,0,0
1,0,0
1,0,0
1,0,0
0,1,0
0,1,0
0,1,0
0,1,0
0,0,1
0,0,1
0,0,1
0,0,1
0,0,1
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR     = Cass
  Approval = Amy   (differs from STAR)

--- Choose-One / Plurality Voting Method (single winner) ---

[STAR Voting]
 Tabulating 13 ballots.
Count × Amy,Boone,Cass
    5 ×   0,    0,   1
    4 ×   1,    0,   0
    4 ×   0,    1,   0

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Cass          -- 5 -- First place
   Amy           -- 4 -- Tied for second place
   Boone         -- 4 -- Tied for second place
 Cass advances, but there's a two-way tie for second.

[STAR Voting: Scoring Round: First tiebreaker]
 The candidate preferred in the most head-to-head matchups advances.
   Amy           -- 4 -- Tied for second place
   Boone         -- 4 -- Tied for second place
   Equal Support -- 5
 There's still a two-way tie for second.

[STAR Voting: Scoring Round: Second tiebreaker]
 The candidate with the most votes of score 5 advances.
   Amy           -- 0 -- Tied for second place
   Boone         -- 0 -- Tied for second place
 There's still a two-way tie for second.

*** No official tie-breaking lot numbers were provided.
    Ties are resolved using a fallback order: CSV column order.
    Lot-number priority order: ['Amy', 'Boone', 'Cass']

[Tiebreaker: Lot Number Priority]
  Tie among: ['Amy', 'Boone']
  Resolved: ['Amy'] (selected by lot-number priority).

[Lot-decided tie — rare]
  ⚠ The ballots did not break this tie: the deterministic rungs
    (pairwise / score, then five-star) all came back equal, so the
    pre-published LOT order chose among the tied candidates — the
    result here was set by lot, not by the votes. Usually the
    "dead rung": no tied candidate held a score-5 vote (five-star
    counts fives, not fours). Verify the tied candidates' 5-counts.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Cass          -- 5 -- First place
   Amy           -- 4
   Equal Support -- 4
 Cass wins.
   Runoff math:
     13  ballots cast
   −  4  Equal Support (no preference between the two finalists)
     ──
      9  voters with a preference  (majority = 5)
           Cass 5 (56%)  ·  Amy 4 (44%)

[STAR Voting: Winner — Choose-One / Plurality Voting Method (single winner)]
 Cass
```

<details>
<summary>Full audit — preference matrix, Condorcet, and score distribution</summary>

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |   * Amy    |   Boone   |  * Cass   |
-----------------------------------------------------
       * Amy > |    ---     |4 - 5 - 4  |4 - 4 - 5  |
       Boone > | 4 - 5 - 4  |   ---     |4 - 4 - 5  |
      * Cass > | 5 - 4 - 4  |5 - 4 - 4  |   ---     |

[Condorcet Winner]
  Condorcet Winner: Cass — matches the STAR winner

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Amy        0  0  0  0  4  9  |     4   0.3
Boone      0  0  0  0  4  9  |     4   0.3
Cass       0  0  0  0  5  8  |     5   0.4
```

</details>

Everything in one file: the [`_tabulated` mirror](../felsenthal_paradoxes_tabulated/bv2166_b7b8dv_plurality_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/felsenthal_paradoxes/bv2166_b7b8dv_plurality.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Runoff reversal (worked set)](../../../01_STAR/runoff_overturns_leader/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [bv2144_mxfmhm_plurality](bv2144_mxfmhm_plurality.md) · [bv2144_mxfmhm_star](bv2144_mxfmhm_star.md) · [bv2145_6fj2kg_irv](bv2145_6fj2kg_irv.md) · [bv2145_6fj2kg_ranked_robin](bv2145_6fj2kg_ranked_robin.md) · [bv2145_6fj2kg_star](bv2145_6fj2kg_star.md) · [bv2146_krk2px_irv](bv2146_krk2px_irv.md) · [bv2146_krk2px_ranked_robin](bv2146_krk2px_ranked_robin.md) · [bv2146_krk2px_star](bv2146_krk2px_star.md) · [bv2147_9gdrqg_irv](bv2147_9gdrqg_irv.md) · [bv2147_9gdrqg_star](bv2147_9gdrqg_star.md) · [bv2148_h87k6v_irv](bv2148_h87k6v_irv.md) · [bv2148_h87k6v_star](bv2148_h87k6v_star.md) · [bv2149_byk9v2_irv](bv2149_byk9v2_irv.md) · [bv2149_byk9v2_star](bv2149_byk9v2_star.md) · [bv2150_dxg8pb_irv](bv2150_dxg8pb_irv.md) · [bv2150_dxg8pb_ranked_robin](bv2150_dxg8pb_ranked_robin.md) · [bv2150_dxg8pb_star](bv2150_dxg8pb_star.md) · [bv2151_97hbpw_irv](bv2151_97hbpw_irv.md) · [bv2151_97hbpw_ranked_robin](bv2151_97hbpw_ranked_robin.md) · [bv2151_97hbpw_star](bv2151_97hbpw_star.md) · [bv2152_r6ctvy_approval](bv2152_r6ctvy_approval.md) · [bv2152_r6ctvy_ranked_robin](bv2152_r6ctvy_ranked_robin.md) · [bv2153_pcttmr_approval](bv2153_pcttmr_approval.md) · [bv2153_pcttmr_irv](bv2153_pcttmr_irv.md) · [bv2153_pcttmr_ranked_robin](bv2153_pcttmr_ranked_robin.md) · [bv2154_wq6yv7_approval](bv2154_wq6yv7_approval.md) · [bv2154_wq6yv7_irv](bv2154_wq6yv7_irv.md) · [bv2154_wq6yv7_ranked_robin](bv2154_wq6yv7_ranked_robin.md) · [bv2160_r6qc8h_plurality](bv2160_r6qc8h_plurality.md) · [bv2160_r6qc8h_star](bv2160_r6qc8h_star.md) · [bv2161_q3h4fk_plurality](bv2161_q3h4fk_plurality.md) · [bv2161_q3h4fk_star](bv2161_q3h4fk_star.md) · [bv2162_4htk44_irv](bv2162_4htk44_irv.md) · [bv2162_4htk44_ranked_robin](bv2162_4htk44_ranked_robin.md) · [bv2162_4htk44_star](bv2162_4htk44_star.md) · [bv2163_74j6vv_irv](bv2163_74j6vv_irv.md) · [bv2163_74j6vv_ranked_robin](bv2163_74j6vv_ranked_robin.md) · [bv2163_74j6vv_star](bv2163_74j6vv_star.md) · [bv2164_xbqq8t_plurality](bv2164_xbqq8t_plurality.md) · [bv2164_xbqq8t_ranked_robin](bv2164_xbqq8t_ranked_robin.md) · [bv2164_xbqq8t_star](bv2164_xbqq8t_star.md) · [bv2165_9vxcj7_plurality](bv2165_9vxcj7_plurality.md) · [bv2165_9vxcj7_star](bv2165_9vxcj7_star.md) · [bv2166_b7b8dv_star](bv2166_b7b8dv_star.md) · [bv2167_f3dxq9_plurality](bv2167_f3dxq9_plurality.md) · [bv2167_f3dxq9_star](bv2167_f3dxq9_star.md) · [felsenthal_ex6_pareto_approval](felsenthal_ex6_pareto_approval.md) · [felsenthal_ex6_ranked_robin](felsenthal_ex6_ranked_robin.md)
