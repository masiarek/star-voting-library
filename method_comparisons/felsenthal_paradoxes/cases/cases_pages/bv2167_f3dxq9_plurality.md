# Minimax Ex.29 — Choose-One: agrees with Minimax, elects the absolute loser D

*Generated from [`bv2167_f3dxq9_plurality.yaml`](../bv2167_f3dxq9_plurality.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [plurality](../../../../07_Concepts) · **1 seat** · **Expected winner:** D

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/f3dxq9) · **[results ↗](https://bettervoting.com/f3dxq9/results)** (election `f3dxq9`).

## Scenario

Race 2 of 2 in the Minimax-elects-the-absolute-loser election (BV2167, bvid f3dxq9; BV-confirmed). Source: Dan S. Felsenthal (2010), Appendix A10, Example 29 — see bv2167_f3dxq9_star.yaml for the setup.
The same 11 voters under Choose-One: first choices D 5, C 3, A 2, B 1 → D — the candidate who loses every head-to-head 5–6 and whom a majority (6 of 11) rank dead last. Choose-One and Minimax (worked on the case page) agree on the absolute loser, for opposite reasons: Choose-One sees only D's five committed fans; Minimax sees only that D's defeats are narrow.
Live results: https://bettervoting.com/f3dxq9/results

## Parameters (from the YAML)

```yaml
voting_method: Plurality
num_winners: 1
expected_winners:
- D
bv_election_id: f3dxq9
bv_test_id: BV2167
```

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

Full report from the [`_tabulated` mirror](../cases_tabulated/bv2167_f3dxq9_plurality_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Choose-One / Plurality Voting Method (single winner) ---
 Tabulating 11 ballots.

                     A      B      C      D   
                     -      -      -      X   
                     -      -      -      X   
                     -      -      -      X   
                     -      -      -      X   
                     -      -      -      X   
                     -      -      X      -   
                     -      -      X      -   
                     -      -      X      -   
                     -      X      -      -   
                     X      -      -      -   
                     X      -      -      -   

  Count the marks:  D 5 · C 3 · A 2 · B 1

Winner — Choose-One / Plurality Voting Method (single winner)
 D   (5 of 11 marks)
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/felsenthal_paradoxes/cases/bv2167_f3dxq9_plurality.yaml
```

## See also

- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [bv2144_mxfmhm_plurality](bv2144_mxfmhm_plurality.md) · [bv2144_mxfmhm_star](bv2144_mxfmhm_star.md) · [bv2145_6fj2kg_irv](bv2145_6fj2kg_irv.md) · [bv2145_6fj2kg_ranked_robin](bv2145_6fj2kg_ranked_robin.md) · [bv2145_6fj2kg_star](bv2145_6fj2kg_star.md) · [bv2146_krk2px_irv](bv2146_krk2px_irv.md) · [bv2146_krk2px_ranked_robin](bv2146_krk2px_ranked_robin.md) · [bv2146_krk2px_star](bv2146_krk2px_star.md) · [bv2147_9gdrqg_irv](bv2147_9gdrqg_irv.md) · [bv2147_9gdrqg_star](bv2147_9gdrqg_star.md) · [bv2148_h87k6v_irv](bv2148_h87k6v_irv.md) · [bv2148_h87k6v_star](bv2148_h87k6v_star.md) · [bv2149_byk9v2_irv](bv2149_byk9v2_irv.md) · [bv2149_byk9v2_star](bv2149_byk9v2_star.md) · [bv2150_dxg8pb_irv](bv2150_dxg8pb_irv.md) · [bv2150_dxg8pb_ranked_robin](bv2150_dxg8pb_ranked_robin.md) · [bv2150_dxg8pb_star](bv2150_dxg8pb_star.md) · [bv2151_97hbpw_irv](bv2151_97hbpw_irv.md) · [bv2151_97hbpw_ranked_robin](bv2151_97hbpw_ranked_robin.md) · [bv2151_97hbpw_star](bv2151_97hbpw_star.md) · [bv2152_r6ctvy_approval](bv2152_r6ctvy_approval.md) · [bv2152_r6ctvy_ranked_robin](bv2152_r6ctvy_ranked_robin.md) · [bv2153_pcttmr_approval](bv2153_pcttmr_approval.md) · [bv2153_pcttmr_irv](bv2153_pcttmr_irv.md) · [bv2153_pcttmr_ranked_robin](bv2153_pcttmr_ranked_robin.md) · [bv2154_wq6yv7_approval](bv2154_wq6yv7_approval.md) · [bv2154_wq6yv7_irv](bv2154_wq6yv7_irv.md) · [bv2154_wq6yv7_ranked_robin](bv2154_wq6yv7_ranked_robin.md) · [bv2160_r6qc8h_plurality](bv2160_r6qc8h_plurality.md) · [bv2160_r6qc8h_star](bv2160_r6qc8h_star.md) · [bv2161_q3h4fk_plurality](bv2161_q3h4fk_plurality.md) · [bv2161_q3h4fk_star](bv2161_q3h4fk_star.md) · [bv2162_4htk44_irv](bv2162_4htk44_irv.md) · [bv2162_4htk44_ranked_robin](bv2162_4htk44_ranked_robin.md) · [bv2162_4htk44_star](bv2162_4htk44_star.md) · [bv2163_74j6vv_irv](bv2163_74j6vv_irv.md) · [bv2163_74j6vv_ranked_robin](bv2163_74j6vv_ranked_robin.md) · [bv2163_74j6vv_star](bv2163_74j6vv_star.md) · [bv2164_xbqq8t_plurality](bv2164_xbqq8t_plurality.md) · [bv2164_xbqq8t_ranked_robin](bv2164_xbqq8t_ranked_robin.md) · [bv2164_xbqq8t_star](bv2164_xbqq8t_star.md) · [bv2165_9vxcj7_plurality](bv2165_9vxcj7_plurality.md) · [bv2165_9vxcj7_star](bv2165_9vxcj7_star.md) · [bv2166_b7b8dv_plurality](bv2166_b7b8dv_plurality.md) · [bv2166_b7b8dv_star](bv2166_b7b8dv_star.md) · [bv2167_f3dxq9_star](bv2167_f3dxq9_star.md) · [felsenthal_ex6_pareto_approval](felsenthal_ex6_pareto_approval.md) · [felsenthal_ex6_ranked_robin](felsenthal_ex6_ranked_robin.md)
