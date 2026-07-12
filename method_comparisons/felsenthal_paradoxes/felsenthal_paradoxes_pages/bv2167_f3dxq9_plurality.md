# Minimax Ex.29 — Choose-One: agrees with Minimax, elects the absolute loser D

*Generated from [`bv2167_f3dxq9_plurality.yaml`](../bv2167_f3dxq9_plurality.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [plurality](../../../00_start_here) · **1 seat** · **Expected winner:** D

## Scenario

Race 2 of 2 in the Minimax-elects-the-absolute-loser election (BV2167, bvid f3dxq9; BV-confirmed). Source: Dan S. Felsenthal (2010), Appendix A10, Example 29 — see bv2167_f3dxq9_star.yaml for the setup.
The same 11 voters under Choose-One: first choices D 5, C 3, A 2, B 1 → D — the candidate who loses every head-to-head 5–6 and whom a majority (6 of 11) rank dead last. Choose-One and Minimax (worked on the case page) agree on the absolute loser, for opposite reasons: Choose-One sees only D's five committed fans; Minimax sees only that D's defeats are narrow.
Live results: https://bettervoting.com/f3dxq9/results

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
A,B,C,D
0,0,0,1
0,0,0,1
0,0,0,1
0,0,0,1
0,0,0,1
0,0,1,0
0,0,1,0
0,0,1,0
0,1,0,0
1,0,0,0
1,0,0,0
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR     = D
  Approval = A   (differs from STAR)

--- Choose-One / Plurality Voting Method (single winner) ---

[STAR Voting]
 Tabulating 11 ballots.
Count × A,B,C,D
    5 × 0,0,0,1
    3 × 0,0,1,0
    2 × 1,0,0,0
    1 × 0,1,0,0

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   D             -- 5 -- First place
   C             -- 3 -- Second place
   A             -- 2
   B             -- 1
 D and C advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   D             -- 5 -- First place
   C             -- 3
   Equal Support -- 3
 D wins.
   Runoff math:
     11  ballots cast
   −  3  Equal Support (no preference between the two finalists)
     ──
      8  voters with a preference  (majority = 5)
           D 5 (62%)  ·  C 3 (38%)

[STAR Voting: Winner — Choose-One / Plurality Voting Method (single winner)]
 D
```

<details>
<summary>Full audit — preference matrix, Condorcet, and score distribution</summary>

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |      A     |     B     |   * C     |   * D     |
-----------------------------------------------------------------
           A > |    ---     |2 - 8 - 1  |2 - 6 - 3  |2 - 4 - 5  |
           B > | 1 - 8 - 2  |   ---     |1 - 7 - 3  |1 - 5 - 5  |
         * C > | 3 - 6 - 2  |3 - 7 - 1  |   ---     |3 - 3 - 5  |
         * D > | 5 - 4 - 2  |5 - 5 - 1  |5 - 3 - 3  |   ---     |

[Condorcet Winner]
  Condorcet Winner: D — matches the STAR winner

[Score Distribution] (how many ballots gave each star rating)
                   Score
Candidate   5   4   3   2   1   0  | Total   Avg
A           0   0   0   0   2   9  |     2   0.2
B           0   0   0   0   1  10  |     1   0.1
C           0   0   0   0   3   8  |     3   0.3
D           0   0   0   0   5   6  |     5   0.5
```

</details>

Everything in one file: the [`_tabulated` mirror](../felsenthal_paradoxes_tabulated/bv2167_f3dxq9_plurality_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/felsenthal_paradoxes/bv2167_f3dxq9_plurality.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [bv2144_mxfmhm_plurality](bv2144_mxfmhm_plurality.md) · [bv2144_mxfmhm_star](bv2144_mxfmhm_star.md) · [bv2145_6fj2kg_irv](bv2145_6fj2kg_irv.md) · [bv2145_6fj2kg_ranked_robin](bv2145_6fj2kg_ranked_robin.md) · [bv2145_6fj2kg_star](bv2145_6fj2kg_star.md) · [bv2146_krk2px_irv](bv2146_krk2px_irv.md) · [bv2146_krk2px_ranked_robin](bv2146_krk2px_ranked_robin.md) · [bv2146_krk2px_star](bv2146_krk2px_star.md) · [bv2147_9gdrqg_irv](bv2147_9gdrqg_irv.md) · [bv2147_9gdrqg_star](bv2147_9gdrqg_star.md) · [bv2148_h87k6v_irv](bv2148_h87k6v_irv.md) · [bv2148_h87k6v_star](bv2148_h87k6v_star.md) · [bv2149_byk9v2_irv](bv2149_byk9v2_irv.md) · [bv2149_byk9v2_star](bv2149_byk9v2_star.md) · [bv2150_dxg8pb_irv](bv2150_dxg8pb_irv.md) · [bv2150_dxg8pb_ranked_robin](bv2150_dxg8pb_ranked_robin.md) · [bv2150_dxg8pb_star](bv2150_dxg8pb_star.md) · [bv2151_97hbpw_irv](bv2151_97hbpw_irv.md) · [bv2151_97hbpw_ranked_robin](bv2151_97hbpw_ranked_robin.md) · [bv2151_97hbpw_star](bv2151_97hbpw_star.md) · [bv2152_r6ctvy_approval](bv2152_r6ctvy_approval.md) · [bv2152_r6ctvy_ranked_robin](bv2152_r6ctvy_ranked_robin.md) · [bv2153_pcttmr_approval](bv2153_pcttmr_approval.md) · [bv2153_pcttmr_irv](bv2153_pcttmr_irv.md) · [bv2153_pcttmr_ranked_robin](bv2153_pcttmr_ranked_robin.md) · [bv2154_wq6yv7_approval](bv2154_wq6yv7_approval.md) · [bv2154_wq6yv7_irv](bv2154_wq6yv7_irv.md) · [bv2154_wq6yv7_ranked_robin](bv2154_wq6yv7_ranked_robin.md) · [bv2160_r6qc8h_plurality](bv2160_r6qc8h_plurality.md) · [bv2160_r6qc8h_star](bv2160_r6qc8h_star.md) · [bv2161_q3h4fk_plurality](bv2161_q3h4fk_plurality.md) · [bv2161_q3h4fk_star](bv2161_q3h4fk_star.md) · [bv2162_4htk44_irv](bv2162_4htk44_irv.md) · [bv2162_4htk44_ranked_robin](bv2162_4htk44_ranked_robin.md) · [bv2162_4htk44_star](bv2162_4htk44_star.md) · [bv2163_74j6vv_irv](bv2163_74j6vv_irv.md) · [bv2163_74j6vv_ranked_robin](bv2163_74j6vv_ranked_robin.md) · [bv2163_74j6vv_star](bv2163_74j6vv_star.md) · [bv2164_xbqq8t_plurality](bv2164_xbqq8t_plurality.md) · [bv2164_xbqq8t_ranked_robin](bv2164_xbqq8t_ranked_robin.md) · [bv2164_xbqq8t_star](bv2164_xbqq8t_star.md) · [bv2165_9vxcj7_plurality](bv2165_9vxcj7_plurality.md) · [bv2165_9vxcj7_star](bv2165_9vxcj7_star.md) · [bv2166_b7b8dv_plurality](bv2166_b7b8dv_plurality.md) · [bv2166_b7b8dv_star](bv2166_b7b8dv_star.md) · [bv2167_f3dxq9_star](bv2167_f3dxq9_star.md) · [felsenthal_ex6_pareto_approval](felsenthal_ex6_pareto_approval.md) · [felsenthal_ex6_ranked_robin](felsenthal_ex6_ranked_robin.md)
