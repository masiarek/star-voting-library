# Fishburn Ex.14 — Choose-One: A wins on first choices

*Generated from [`bv2160_r6qc8h_plurality.yaml`](../bv2160_r6qc8h_plurality.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [plurality](../../../../00_start_here) · **1 seat** · **Expected winner:** A

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/r6qc8h) · **[results ↗](https://bettervoting.com/r6qc8h/results)** (election `r6qc8h`).

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

Full report from the [`_tabulated` mirror](../cases_tabulated/bv2160_r6qc8h_plurality_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Choose-One / Plurality Voting Method (single winner) ---
 Tabulating 7 ballots.

                     A      B      C      D   
                     X      -      -      -   
                     X      -      -      -   
                     X      -      -      -   
                     -      X      -      -   
                     -      X      -      -   
                     -      -      X      -   
                     -      -      X      -   

  Count the marks:  A 3 · B 2 · C 2 · D 0

Winner — Choose-One / Plurality Voting Method (single winner)
 A   (3 of 7 marks)
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/felsenthal_paradoxes/cases/bv2160_r6qc8h_plurality.yaml
```

## See also

- [Ties & tie-breaking (topic hub)](../../../../00_start_here/topics/ties/README.md)
- [Vote splitting (worked set)](../../../split_voting/README.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [bv2144_mxfmhm_plurality](bv2144_mxfmhm_plurality.md) · [bv2144_mxfmhm_star](bv2144_mxfmhm_star.md) · [bv2145_6fj2kg_irv](bv2145_6fj2kg_irv.md) · [bv2145_6fj2kg_ranked_robin](bv2145_6fj2kg_ranked_robin.md) · [bv2145_6fj2kg_star](bv2145_6fj2kg_star.md) · [bv2146_krk2px_irv](bv2146_krk2px_irv.md) · [bv2146_krk2px_ranked_robin](bv2146_krk2px_ranked_robin.md) · [bv2146_krk2px_star](bv2146_krk2px_star.md) · [bv2147_9gdrqg_irv](bv2147_9gdrqg_irv.md) · [bv2147_9gdrqg_star](bv2147_9gdrqg_star.md) · [bv2148_h87k6v_irv](bv2148_h87k6v_irv.md) · [bv2148_h87k6v_star](bv2148_h87k6v_star.md) · [bv2149_byk9v2_irv](bv2149_byk9v2_irv.md) · [bv2149_byk9v2_star](bv2149_byk9v2_star.md) · [bv2150_dxg8pb_irv](bv2150_dxg8pb_irv.md) · [bv2150_dxg8pb_ranked_robin](bv2150_dxg8pb_ranked_robin.md) · [bv2150_dxg8pb_star](bv2150_dxg8pb_star.md) · [bv2151_97hbpw_irv](bv2151_97hbpw_irv.md) · [bv2151_97hbpw_ranked_robin](bv2151_97hbpw_ranked_robin.md) · [bv2151_97hbpw_star](bv2151_97hbpw_star.md) · [bv2152_r6ctvy_approval](bv2152_r6ctvy_approval.md) · [bv2152_r6ctvy_ranked_robin](bv2152_r6ctvy_ranked_robin.md) · [bv2153_pcttmr_approval](bv2153_pcttmr_approval.md) · [bv2153_pcttmr_irv](bv2153_pcttmr_irv.md) · [bv2153_pcttmr_ranked_robin](bv2153_pcttmr_ranked_robin.md) · [bv2154_wq6yv7_approval](bv2154_wq6yv7_approval.md) · [bv2154_wq6yv7_irv](bv2154_wq6yv7_irv.md) · [bv2154_wq6yv7_ranked_robin](bv2154_wq6yv7_ranked_robin.md) · [bv2160_r6qc8h_star](bv2160_r6qc8h_star.md) · [bv2161_q3h4fk_plurality](bv2161_q3h4fk_plurality.md) · [bv2161_q3h4fk_star](bv2161_q3h4fk_star.md) · [bv2162_4htk44_irv](bv2162_4htk44_irv.md) · [bv2162_4htk44_ranked_robin](bv2162_4htk44_ranked_robin.md) · [bv2162_4htk44_star](bv2162_4htk44_star.md) · [bv2163_74j6vv_irv](bv2163_74j6vv_irv.md) · [bv2163_74j6vv_ranked_robin](bv2163_74j6vv_ranked_robin.md) · [bv2163_74j6vv_star](bv2163_74j6vv_star.md) · [bv2164_xbqq8t_plurality](bv2164_xbqq8t_plurality.md) · [bv2164_xbqq8t_ranked_robin](bv2164_xbqq8t_ranked_robin.md) · [bv2164_xbqq8t_star](bv2164_xbqq8t_star.md) · [bv2165_9vxcj7_plurality](bv2165_9vxcj7_plurality.md) · [bv2165_9vxcj7_star](bv2165_9vxcj7_star.md) · [bv2166_b7b8dv_plurality](bv2166_b7b8dv_plurality.md) · [bv2166_b7b8dv_star](bv2166_b7b8dv_star.md) · [bv2167_f3dxq9_plurality](bv2167_f3dxq9_plurality.md) · [bv2167_f3dxq9_star](bv2167_f3dxq9_star.md) · [felsenthal_ex6_pareto_approval](felsenthal_ex6_pareto_approval.md) · [felsenthal_ex6_ranked_robin](felsenthal_ex6_ranked_robin.md)
