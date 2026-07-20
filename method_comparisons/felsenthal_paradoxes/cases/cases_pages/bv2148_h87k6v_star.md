# Felsenthal Ex.3 District II — STAR: also Bruno

*Generated from [`bv2148_h87k6v_star.yaml`](../bv2148_h87k6v_star.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Bruno

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/h87k6v) · **[results ↗](https://bettervoting.com/h87k6v/results)** (election `h87k6v`).

## Scenario

Race 2 of 2 in District II of the Felsenthal Reinforcement-paradox trio (BV2148, bvid h87k6v; BV-confirmed). Source: Dan S. Felsenthal (2010), Appendix A2, Example 3 — see bv2148_h87k6v_irv.yaml for the setup.
The same 15 ballots with ranks mapped 5/3/1. Scores: Alma 41, Bruno 47, Cora 47 — Bruno and Cora advance (both clear of Alma; no advancement tie), and Bruno wins the automatic runoff 8–7. Same winner as the runoff procedure; the reinforcement contrast appears at the combined stage (BV2149).
Live results: https://bettervoting.com/h87k6v/results

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Alma,Bruno,Cora
5,1,3
5,1,3
5,1,3
5,1,3
5,1,3
5,1,3
1,5,3
1,5,3
1,5,3
1,5,3
1,5,3
1,5,3
1,5,3
1,5,3
3,1,5
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR     = Bruno
  Approval = Cora   (differs from STAR)

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 15 ballots.
Count × Alma,Bruno,Cora
    8 ×    1,    5,   3
    6 ×    5,    1,   3
    1 ×    3,    1,   5

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Bruno         -- 47 -- First place
   Cora          -- 47 -- Second place
   Alma          -- 41
 Bruno and Cora advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Bruno         -- 8 -- First place
   Cora          -- 7
   Equal Support -- 0
 Bruno wins.
   Runoff math:
     15  ballots cast
   −  0  Equal Support (no preference between the two finalists)
     ──
     15  voters with a preference  (majority = 8)
           Bruno 8 (53%)  ·  Cora 7 (47%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Bruno
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |     Alma   | * Bruno   |  * Cora   |
-----------------------------------------------------
        Alma > |    ---     |7 - 0 - 8  |6 - 0 - 9  |
     * Bruno > | 8 - 0 - 7  |   ---     |8 - 0 - 7  |
      * Cora > | 9 - 0 - 6  |7 - 0 - 8  |   ---     |

[Condorcet Winner]
  Condorcet Winner: Bruno — matches the STAR winner

[Score Distribution] (how many ballots gave each star rating)
                   Score
Candidate   5   4   3   2   1   0  | Total   Avg
Alma        6   0   1   0   8   0  |    41   2.7
Bruno       8   0   0   0   7   0  |    47   3.1
Cora        1   0  14   0   0   0  |    47   3.1
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/bv2148_h87k6v_star_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/felsenthal_paradoxes/cases/bv2148_h87k6v_star.yaml
```

## See also

- [Methods disagree on this election](../../../divergence_review/cases/APPROVAL_OR_MINOR/bv2148_h87k6v_star.md) — its entry in the divergence review ledger
- [Ties & tie-breaking (topic hub)](../../../../00_start_here/topics/ties/README.md)
- [Runoff reversal (worked set)](../../../../01_STAR/runoff_overturns_leader/README.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [bv2144_mxfmhm_plurality](bv2144_mxfmhm_plurality.md) · [bv2144_mxfmhm_star](bv2144_mxfmhm_star.md) · [bv2145_6fj2kg_irv](bv2145_6fj2kg_irv.md) · [bv2145_6fj2kg_ranked_robin](bv2145_6fj2kg_ranked_robin.md) · [bv2145_6fj2kg_star](bv2145_6fj2kg_star.md) · [bv2146_krk2px_irv](bv2146_krk2px_irv.md) · [bv2146_krk2px_ranked_robin](bv2146_krk2px_ranked_robin.md) · [bv2146_krk2px_star](bv2146_krk2px_star.md) · [bv2147_9gdrqg_irv](bv2147_9gdrqg_irv.md) · [bv2147_9gdrqg_star](bv2147_9gdrqg_star.md) · [bv2148_h87k6v_irv](bv2148_h87k6v_irv.md) · [bv2149_byk9v2_irv](bv2149_byk9v2_irv.md) · [bv2149_byk9v2_star](bv2149_byk9v2_star.md) · [bv2150_dxg8pb_irv](bv2150_dxg8pb_irv.md) · [bv2150_dxg8pb_ranked_robin](bv2150_dxg8pb_ranked_robin.md) · [bv2150_dxg8pb_star](bv2150_dxg8pb_star.md) · [bv2151_97hbpw_irv](bv2151_97hbpw_irv.md) · [bv2151_97hbpw_ranked_robin](bv2151_97hbpw_ranked_robin.md) · [bv2151_97hbpw_star](bv2151_97hbpw_star.md) · [bv2152_r6ctvy_approval](bv2152_r6ctvy_approval.md) · [bv2152_r6ctvy_ranked_robin](bv2152_r6ctvy_ranked_robin.md) · [bv2153_pcttmr_approval](bv2153_pcttmr_approval.md) · [bv2153_pcttmr_irv](bv2153_pcttmr_irv.md) · [bv2153_pcttmr_ranked_robin](bv2153_pcttmr_ranked_robin.md) · [bv2154_wq6yv7_approval](bv2154_wq6yv7_approval.md) · [bv2154_wq6yv7_irv](bv2154_wq6yv7_irv.md) · [bv2154_wq6yv7_ranked_robin](bv2154_wq6yv7_ranked_robin.md) · [bv2160_r6qc8h_plurality](bv2160_r6qc8h_plurality.md) · [bv2160_r6qc8h_star](bv2160_r6qc8h_star.md) · [bv2161_q3h4fk_plurality](bv2161_q3h4fk_plurality.md) · [bv2161_q3h4fk_star](bv2161_q3h4fk_star.md) · [bv2162_4htk44_irv](bv2162_4htk44_irv.md) · [bv2162_4htk44_ranked_robin](bv2162_4htk44_ranked_robin.md) · [bv2162_4htk44_star](bv2162_4htk44_star.md) · [bv2163_74j6vv_irv](bv2163_74j6vv_irv.md) · [bv2163_74j6vv_ranked_robin](bv2163_74j6vv_ranked_robin.md) · [bv2163_74j6vv_star](bv2163_74j6vv_star.md) · [bv2164_xbqq8t_plurality](bv2164_xbqq8t_plurality.md) · [bv2164_xbqq8t_ranked_robin](bv2164_xbqq8t_ranked_robin.md) · [bv2164_xbqq8t_star](bv2164_xbqq8t_star.md) · [bv2165_9vxcj7_plurality](bv2165_9vxcj7_plurality.md) · [bv2165_9vxcj7_star](bv2165_9vxcj7_star.md) · [bv2166_b7b8dv_plurality](bv2166_b7b8dv_plurality.md) · [bv2166_b7b8dv_star](bv2166_b7b8dv_star.md) · [bv2167_f3dxq9_plurality](bv2167_f3dxq9_plurality.md) · [bv2167_f3dxq9_star](bv2167_f3dxq9_star.md) · [felsenthal_ex6_pareto_approval](felsenthal_ex6_pareto_approval.md) · [felsenthal_ex6_ranked_robin](felsenthal_ex6_ranked_robin.md)
