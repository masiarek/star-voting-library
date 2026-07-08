# Coombs Ex.17 — Choose-One: Bree on first choices

*Generated from [`bv2164_xbqq8t_plurality.yaml`](../bv2164_xbqq8t_plurality.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [plurality](../../../00_start_here) · **1 seat** · **Expected winner:** Bree

## Scenario

Race 2 of 3 in the Coombs Condorcet-failure election (BV2164, bvid xbqq8t; BV-confirmed). Source: Dan S. Felsenthal (2010), Appendix A7, Example 17 — see bv2164_xbqq8t_star.yaml for the setup.
The same 33 voters under Choose-One: first choices Arlo 11, Bree 14, Cole 4, Dana 4 → Bree (a plurality, not a majority). Choose-One happens to agree with Coombs' paper result here — both miss the Condorcet winner Arlo, whom STAR and Ranked Robin elect.
Live results: https://bettervoting.com/xbqq8t/results

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Arlo,Bree,Cole,Dana
11: 1,0,0,0
14: 0,1,0,0
# 4× Cole-first, 4× Dana-first:
0,0,1,0
0,0,1,0
0,0,1,0
0,0,1,0
0,0,0,1
0,0,0,1
0,0,0,1
0,0,0,1
```

## What the engine says

Full report from the [`_tabulated` mirror](../felsenthal_paradoxes_tabulated/bv2164_xbqq8t_plurality_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |    * Arlo    |   * Bree    |     Cole    |     Dana    |
---------------------------------------------------------------------------
        * Arlo > |     ---      |11 -  8 - 14 |11 - 18 -  4 |11 - 18 -  4 |
        * Bree > | 14 -  8 - 11 |    ---      |14 - 15 -  4 |14 - 15 -  4 |
          Cole > |  4 - 18 - 11 | 4 - 15 - 14 |    ---      | 4 - 25 -  4 |
          Dana > |  4 - 18 - 11 | 4 - 15 - 14 | 4 - 25 -  4 |    ---      |

[Condorcet Winner]
  Condorcet Winner: Bree — matches the STAR winner

[Divergence from STAR]
  STAR     = Bree
  Approval = Arlo   (differs from STAR)

--- Choose-One / Plurality Voting Method (single winner) ---
[STAR Voting]
 Tabulating 33 ballots.
Count × Arlo,Bree,Cole,Dana
   14 ×    0,   1,   0,   0
   11 ×    1,   0,   0,   0
    4 ×    0,   0,   1,   0
    4 ×    0,   0,   0,   1

[Score Distribution] (how many ballots gave each star rating)
                   Score
Candidate   5   4   3   2   1   0  | Total   Avg
Arlo        0   0   0   0  11  22  |    11   0.3
Bree        0   0   0   0  14  19  |    14   0.4
Cole        0   0   0   0   4  29  |     4   0.1
Dana        0   0   0   0   4  29  |     4   0.1

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Bree          -- 14 -- First place
   Arlo          -- 11 -- Second place
   Cole          --  4
   Dana          --  4
 Bree and Arlo advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Bree          -- 14 -- First place
   Arlo          -- 11
   Equal Support --  8
 Bree wins.
   Runoff math:
     33  ballots cast
   −  8  Equal Support (no preference between the two finalists)
     ──
     25  voters with a preference  (majority = 13)
           Bree 14 (56%)  ·  Arlo 11 (44%)

[STAR Voting: Winner — Choose-One / Plurality Voting Method (single winner)]
 Bree
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/felsenthal_paradoxes/bv2164_xbqq8t_plurality.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [bv2144_mxfmhm_plurality](bv2144_mxfmhm_plurality.md) · [bv2144_mxfmhm_star](bv2144_mxfmhm_star.md) · [bv2145_6fj2kg_irv](bv2145_6fj2kg_irv.md) · [bv2145_6fj2kg_ranked_robin](bv2145_6fj2kg_ranked_robin.md) · [bv2145_6fj2kg_star](bv2145_6fj2kg_star.md) · [bv2146_krk2px_irv](bv2146_krk2px_irv.md) · [bv2146_krk2px_ranked_robin](bv2146_krk2px_ranked_robin.md) · [bv2146_krk2px_star](bv2146_krk2px_star.md) · [bv2147_9gdrqg_irv](bv2147_9gdrqg_irv.md) · [bv2147_9gdrqg_star](bv2147_9gdrqg_star.md) · [bv2148_h87k6v_irv](bv2148_h87k6v_irv.md) · [bv2148_h87k6v_star](bv2148_h87k6v_star.md) · [bv2149_byk9v2_irv](bv2149_byk9v2_irv.md) · [bv2149_byk9v2_star](bv2149_byk9v2_star.md) · [bv2150_dxg8pb_irv](bv2150_dxg8pb_irv.md) · [bv2150_dxg8pb_ranked_robin](bv2150_dxg8pb_ranked_robin.md) · [bv2150_dxg8pb_star](bv2150_dxg8pb_star.md) · [bv2151_97hbpw_irv](bv2151_97hbpw_irv.md) · [bv2151_97hbpw_ranked_robin](bv2151_97hbpw_ranked_robin.md) · [bv2151_97hbpw_star](bv2151_97hbpw_star.md) · [bv2152_r6ctvy_approval](bv2152_r6ctvy_approval.md) · [bv2152_r6ctvy_ranked_robin](bv2152_r6ctvy_ranked_robin.md) · [bv2153_pcttmr_approval](bv2153_pcttmr_approval.md) · [bv2153_pcttmr_irv](bv2153_pcttmr_irv.md) · [bv2153_pcttmr_ranked_robin](bv2153_pcttmr_ranked_robin.md) · [bv2154_wq6yv7_approval](bv2154_wq6yv7_approval.md) · [bv2154_wq6yv7_irv](bv2154_wq6yv7_irv.md) · [bv2154_wq6yv7_ranked_robin](bv2154_wq6yv7_ranked_robin.md) · [bv2160_r6qc8h_plurality](bv2160_r6qc8h_plurality.md) · [bv2160_r6qc8h_star](bv2160_r6qc8h_star.md) · [bv2161_q3h4fk_plurality](bv2161_q3h4fk_plurality.md) · [bv2161_q3h4fk_star](bv2161_q3h4fk_star.md) · [bv2162_4htk44_irv](bv2162_4htk44_irv.md) · [bv2162_4htk44_ranked_robin](bv2162_4htk44_ranked_robin.md) · [bv2162_4htk44_star](bv2162_4htk44_star.md) · [bv2163_74j6vv_irv](bv2163_74j6vv_irv.md) · [bv2163_74j6vv_ranked_robin](bv2163_74j6vv_ranked_robin.md) · [bv2163_74j6vv_star](bv2163_74j6vv_star.md) · [bv2164_xbqq8t_ranked_robin](bv2164_xbqq8t_ranked_robin.md) · [bv2164_xbqq8t_star](bv2164_xbqq8t_star.md) · [bv2165_9vxcj7_plurality](bv2165_9vxcj7_plurality.md) · [bv2165_9vxcj7_star](bv2165_9vxcj7_star.md) · [bv2166_b7b8dv_plurality](bv2166_b7b8dv_plurality.md) · [bv2166_b7b8dv_star](bv2166_b7b8dv_star.md) · [bv2167_f3dxq9_plurality](bv2167_f3dxq9_plurality.md) · [bv2167_f3dxq9_star](bv2167_f3dxq9_star.md) · [felsenthal_ex6_pareto_approval](felsenthal_ex6_pareto_approval.md) · [felsenthal_ex6_ranked_robin](felsenthal_ex6_ranked_robin.md)
