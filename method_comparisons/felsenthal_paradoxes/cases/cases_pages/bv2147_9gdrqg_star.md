# Felsenthal Ex.3 District I — STAR: also Bruno

*Generated from [`bv2147_9gdrqg_star.yaml`](../bv2147_9gdrqg_star.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Bruno

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/9gdrqg) · **[results ↗](https://bettervoting.com/9gdrqg/results)** (election `9gdrqg`).

## Scenario

Race 2 of 2 in District I of the Felsenthal Reinforcement-paradox trio (BV2147, bvid 9gdrqg; BV-confirmed). Source: Dan S. Felsenthal (2010), Appendix A2, Example 3 — see bv2147_9gdrqg_irv.yaml for the setup.
The same 17 ballots with ranks mapped to 0–5 scores (5/3/1). Scores: Alma 47, Bruno 51, Cora 55 — Cora and Bruno advance, Bruno wins the automatic runoff 10–7. Same winner as the runoff procedure in this district; the reinforcement contrast appears at the combined stage (BV2149), where STAR stays with Bruno and the runoff procedure flips to Alma.
Live results: https://bettervoting.com/9gdrqg/results

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Alma,Bruno,Cora
5,3,1
5,3,1
5,3,1
5,3,1
3,5,1
1,5,3
1,5,3
1,5,3
1,5,3
1,5,3
3,1,5
3,1,5
3,1,5
3,1,5
3,1,5
3,1,5
1,3,5
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR                   = Bruno
  Choose-One (Plurality) = Cora   (differs from STAR)
  Approval               = Cora   (differs from STAR)
  RCV-RR                 = Cora   (differs from STAR)
  Full round-by-round reports (generated for review):
  RCV-RR round-robin: cases_tabulated/bv2147_9gdrqg_star_RCV-RR_tabulated.txt

[Runoff Reversal]
 - Score Round Winner(s) = (Cora)
 - Runoff Round Winner   = (Bruno)
  Candidate Cora earned the highest total score, but
  Candidate Bruno won the automatic runoff — not a malfunction,
  STAR working as designed: the runoff elects the finalist preferred
  by the majority (of voters with a preference).

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 17 ballots.
Count × Alma,Bruno,Cora
    6 ×    3,    1,   5
    5 ×    1,    5,   3
    4 ×    5,    3,   1
    1 ×    3,    5,   1
    1 ×    1,    3,   5

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Cora          -- 55 -- First place
   Bruno         -- 51 -- Second place
   Alma          -- 47
 Cora and Bruno advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Bruno         -- 10 -- First place
   Cora          --  7
   Equal Support --  0
 Bruno wins.
   Runoff math:
     17  ballots cast
   −  0  Equal Support (no preference between the two finalists)
     ──
     17  voters with a preference  (majority = 9)
           Bruno 10 (59%)  ·  Cora 7 (41%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Bruno
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |      Alma    |  * Bruno    |   * Cora    |
-------------------------------------------------------------
          Alma > |     ---      |10 -  0 -  7 | 5 -  0 - 12 |
       * Bruno > |  7 -  0 - 10 |    ---      |10 -  0 -  7 |
        * Cora > | 12 -  0 -  5 | 7 -  0 - 10 |    ---      |

[Condorcet Winner]
  No Condorcet winner (majority cycle: Alma > Bruno > Cora > Alma)

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Alma       4  0  7  0  6  0  |    47   2.8
Bruno      6  0  5  0  6  0  |    51   3.0
Cora       7  0  5  0  5  0  |    55   3.2
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/bv2147_9gdrqg_star_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/felsenthal_paradoxes/cases/bv2147_9gdrqg_star.yaml
```

## See also

- [Methods disagree on this election](../../../divergence_review/cases/CYCLE_OR_THREE_WAY/bv2147_9gdrqg_star.md) — its entry in the divergence review ledger
- [Runoff reversal (worked set)](../../../../01_STAR/runoff_overturns_leader/README.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [bv2144_mxfmhm_plurality](bv2144_mxfmhm_plurality.md) · [bv2144_mxfmhm_star](bv2144_mxfmhm_star.md) · [bv2145_6fj2kg_irv](bv2145_6fj2kg_irv.md) · [bv2145_6fj2kg_ranked_robin](bv2145_6fj2kg_ranked_robin.md) · [bv2145_6fj2kg_star](bv2145_6fj2kg_star.md) · [bv2146_krk2px_irv](bv2146_krk2px_irv.md) · [bv2146_krk2px_ranked_robin](bv2146_krk2px_ranked_robin.md) · [bv2146_krk2px_star](bv2146_krk2px_star.md) · [bv2147_9gdrqg_irv](bv2147_9gdrqg_irv.md) · [bv2148_h87k6v_irv](bv2148_h87k6v_irv.md) · [bv2148_h87k6v_star](bv2148_h87k6v_star.md) · [bv2149_byk9v2_irv](bv2149_byk9v2_irv.md) · [bv2149_byk9v2_star](bv2149_byk9v2_star.md) · [bv2150_dxg8pb_irv](bv2150_dxg8pb_irv.md) · [bv2150_dxg8pb_ranked_robin](bv2150_dxg8pb_ranked_robin.md) · [bv2150_dxg8pb_star](bv2150_dxg8pb_star.md) · [bv2151_97hbpw_irv](bv2151_97hbpw_irv.md) · [bv2151_97hbpw_ranked_robin](bv2151_97hbpw_ranked_robin.md) · [bv2151_97hbpw_star](bv2151_97hbpw_star.md) · [bv2152_r6ctvy_approval](bv2152_r6ctvy_approval.md) · [bv2152_r6ctvy_ranked_robin](bv2152_r6ctvy_ranked_robin.md) · [bv2153_pcttmr_approval](bv2153_pcttmr_approval.md) · [bv2153_pcttmr_irv](bv2153_pcttmr_irv.md) · [bv2153_pcttmr_ranked_robin](bv2153_pcttmr_ranked_robin.md) · [bv2154_wq6yv7_approval](bv2154_wq6yv7_approval.md) · [bv2154_wq6yv7_irv](bv2154_wq6yv7_irv.md) · [bv2154_wq6yv7_ranked_robin](bv2154_wq6yv7_ranked_robin.md) · [bv2160_r6qc8h_plurality](bv2160_r6qc8h_plurality.md) · [bv2160_r6qc8h_star](bv2160_r6qc8h_star.md) · [bv2161_q3h4fk_plurality](bv2161_q3h4fk_plurality.md) · [bv2161_q3h4fk_star](bv2161_q3h4fk_star.md) · [bv2162_4htk44_irv](bv2162_4htk44_irv.md) · [bv2162_4htk44_ranked_robin](bv2162_4htk44_ranked_robin.md) · [bv2162_4htk44_star](bv2162_4htk44_star.md) · [bv2163_74j6vv_irv](bv2163_74j6vv_irv.md) · [bv2163_74j6vv_ranked_robin](bv2163_74j6vv_ranked_robin.md) · [bv2163_74j6vv_star](bv2163_74j6vv_star.md) · [bv2164_xbqq8t_plurality](bv2164_xbqq8t_plurality.md) · [bv2164_xbqq8t_ranked_robin](bv2164_xbqq8t_ranked_robin.md) · [bv2164_xbqq8t_star](bv2164_xbqq8t_star.md) · [bv2165_9vxcj7_plurality](bv2165_9vxcj7_plurality.md) · [bv2165_9vxcj7_star](bv2165_9vxcj7_star.md) · [bv2166_b7b8dv_plurality](bv2166_b7b8dv_plurality.md) · [bv2166_b7b8dv_star](bv2166_b7b8dv_star.md) · [bv2167_f3dxq9_plurality](bv2167_f3dxq9_plurality.md) · [bv2167_f3dxq9_star](bv2167_f3dxq9_star.md) · [felsenthal_ex6_pareto_approval](felsenthal_ex6_pareto_approval.md) · [felsenthal_ex6_ranked_robin](felsenthal_ex6_ranked_robin.md)
