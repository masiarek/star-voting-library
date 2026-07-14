# Felsenthal Ex.5 — Approval: the Condorcet winner loses the approval count

*Generated from [`bv2152_r6ctvy_approval.yaml`](../bv2152_r6ctvy_approval.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Approval Voting](../../../00_start_here/Approval_Voting) · **1 seat** · **Expected winner:** Anna

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/r6ctvy) · **[results ↗](https://bettervoting.com/r6ctvy/results)** (election `r6ctvy`).

## Scenario

Race 1 of 2 in the Felsenthal & Maoz Approval-paradox election (BV2152, bvid r6ctvy; BV-confirmed). Source: Dan S. Felsenthal, "Review of Paradoxes Afflicting Various Voting Procedures Where One Out of m Candidates (m ≥ 2) Must Be Elected", University of Haifa / LSE, revised 26 May 2010; Appendix A3, Example 5 — due to Felsenthal & Maoz (1988: 123, Example 2).
47 voters, rankings 18×(Anna>Bert>Carla), 6×(Bert>Carla>Anna), 8×(Bert>Anna>Carla), 2×(Carla>Anna>Bert), 13×(Carla>Bert>Anna). Bert is the Condorcet winner (beats Anna 27–20, Carla 32–15; social ordering Bert>Anna>Carla). But each voter approves only the candidates the text marks in parentheses — 18×{Anna}, 6×{Bert,Carla}, 8×{Bert,Anna}, 2×{Carla,Anna}, 13×{Carla} — and the approval totals are Anna 28, Bert 14, Carla 21: APPROVAL ELECTS ANNA. The Condorcet winner paradox under Approval: where a voter draws the approval cutoff decides the election, and the pairwise favorite can fall below it.
Live results: https://bettervoting.com/r6ctvy/results

## Ballots

Row 1 = candidate names; each later row is one voter's approvals (`1` = approve, `0`/blank = not approved).

```text
Anna,Bert,Carla
1,0,0
1,0,0
1,0,0
1,0,0
1,0,0
1,0,0
1,0,0
1,0,0
1,0,0
1,0,0
1,0,0
1,0,0
1,0,0
1,0,0
1,0,0
1,0,0
1,0,0
1,0,0
0,1,1
0,1,1
0,1,1
0,1,1
0,1,1
0,1,1
1,1,0
1,1,0
1,1,0
1,1,0
1,1,0
1,1,0
1,1,0
1,1,0
1,0,1
1,0,1
0,0,1
0,0,1
0,0,1
0,0,1
0,0,1
0,0,1
0,0,1
0,0,1
0,0,1
0,0,1
0,0,1
0,0,1
0,0,1
```

## What the engine says

Full report from the [`_tabulated` mirror](../felsenthal_paradoxes_tabulated/bv2152_r6ctvy_approval_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Approval Voting (single winner) ---
 Tabulating 47 ballots (any non-zero score = approval).

Ballots:
   columns = Anna, Bert, Carla      (1 = approve; 0 / blank / marker = not approved)
    18 × 1,0,0
     6 × 0,1,1
     8 × 1,1,0
     2 × 1,0,1
    13 × 0,0,1

   Anna  -- 28 (60%) -- Elected
   Carla -- 21 (45%)
   Bert  -- 14 (30%)

[Approval Distribution] (how many candidates each ballot approved)
   63 approvals across 47 ballots — average 1.3 of 3 (range 1–2).
     approved 1: 31 ballots
     approved 2: 16 ballots

[Co-Approval Matrix]
 Of the voters who approved the ROW candidate, the % who ALSO approved the COLUMN candidate.
          |  Anna  | Carla  |  Bert  |
   -----------------------------------
   Anna   |   --   |   7%   |  29%   |
   Carla  |  10%   |   --   |  29%   |
   Bert   |  57%   |  43%   |   --   |

Winner — Approval Voting (single winner)
  Anna
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/felsenthal_paradoxes/bv2152_r6ctvy_approval.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [bv2144_mxfmhm_plurality](bv2144_mxfmhm_plurality.md) · [bv2144_mxfmhm_star](bv2144_mxfmhm_star.md) · [bv2145_6fj2kg_irv](bv2145_6fj2kg_irv.md) · [bv2145_6fj2kg_ranked_robin](bv2145_6fj2kg_ranked_robin.md) · [bv2145_6fj2kg_star](bv2145_6fj2kg_star.md) · [bv2146_krk2px_irv](bv2146_krk2px_irv.md) · [bv2146_krk2px_ranked_robin](bv2146_krk2px_ranked_robin.md) · [bv2146_krk2px_star](bv2146_krk2px_star.md) · [bv2147_9gdrqg_irv](bv2147_9gdrqg_irv.md) · [bv2147_9gdrqg_star](bv2147_9gdrqg_star.md) · [bv2148_h87k6v_irv](bv2148_h87k6v_irv.md) · [bv2148_h87k6v_star](bv2148_h87k6v_star.md) · [bv2149_byk9v2_irv](bv2149_byk9v2_irv.md) · [bv2149_byk9v2_star](bv2149_byk9v2_star.md) · [bv2150_dxg8pb_irv](bv2150_dxg8pb_irv.md) · [bv2150_dxg8pb_ranked_robin](bv2150_dxg8pb_ranked_robin.md) · [bv2150_dxg8pb_star](bv2150_dxg8pb_star.md) · [bv2151_97hbpw_irv](bv2151_97hbpw_irv.md) · [bv2151_97hbpw_ranked_robin](bv2151_97hbpw_ranked_robin.md) · [bv2151_97hbpw_star](bv2151_97hbpw_star.md) · [bv2152_r6ctvy_ranked_robin](bv2152_r6ctvy_ranked_robin.md) · [bv2153_pcttmr_approval](bv2153_pcttmr_approval.md) · [bv2153_pcttmr_irv](bv2153_pcttmr_irv.md) · [bv2153_pcttmr_ranked_robin](bv2153_pcttmr_ranked_robin.md) · [bv2154_wq6yv7_approval](bv2154_wq6yv7_approval.md) · [bv2154_wq6yv7_irv](bv2154_wq6yv7_irv.md) · [bv2154_wq6yv7_ranked_robin](bv2154_wq6yv7_ranked_robin.md) · [bv2160_r6qc8h_plurality](bv2160_r6qc8h_plurality.md) · [bv2160_r6qc8h_star](bv2160_r6qc8h_star.md) · [bv2161_q3h4fk_plurality](bv2161_q3h4fk_plurality.md) · [bv2161_q3h4fk_star](bv2161_q3h4fk_star.md) · [bv2162_4htk44_irv](bv2162_4htk44_irv.md) · [bv2162_4htk44_ranked_robin](bv2162_4htk44_ranked_robin.md) · [bv2162_4htk44_star](bv2162_4htk44_star.md) · [bv2163_74j6vv_irv](bv2163_74j6vv_irv.md) · [bv2163_74j6vv_ranked_robin](bv2163_74j6vv_ranked_robin.md) · [bv2163_74j6vv_star](bv2163_74j6vv_star.md) · [bv2164_xbqq8t_plurality](bv2164_xbqq8t_plurality.md) · [bv2164_xbqq8t_ranked_robin](bv2164_xbqq8t_ranked_robin.md) · [bv2164_xbqq8t_star](bv2164_xbqq8t_star.md) · [bv2165_9vxcj7_plurality](bv2165_9vxcj7_plurality.md) · [bv2165_9vxcj7_star](bv2165_9vxcj7_star.md) · [bv2166_b7b8dv_plurality](bv2166_b7b8dv_plurality.md) · [bv2166_b7b8dv_star](bv2166_b7b8dv_star.md) · [bv2167_f3dxq9_plurality](bv2167_f3dxq9_plurality.md) · [bv2167_f3dxq9_star](bv2167_f3dxq9_star.md) · [felsenthal_ex6_pareto_approval](felsenthal_ex6_pareto_approval.md) · [felsenthal_ex6_ranked_robin](felsenthal_ex6_ranked_robin.md)
