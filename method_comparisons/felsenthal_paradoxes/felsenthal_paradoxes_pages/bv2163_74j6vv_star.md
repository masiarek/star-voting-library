# Nurmi Ex.16 truncated — STAR: unmoved, still B

*Generated from [`bv2163_74j6vv_star.yaml`](../bv2163_74j6vv_star.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** B

## Scenario

Race 1 of 3 in the RCV-IRV truncation pair, part 2 of 2 (BV2163, bvid 74j6vv; BV-confirmed). Source: Dan S. Felsenthal (2010), Appendix A6, Example 16, due to Nurmi (1999: 63) — see bv2163_74j6vv_irv.yaml for the setup.
The same electorate with the 17 truncated ballots scoring only D (everything else 0): A 329, B 373, C 244, D 171 — B still wins the automatic runoff. STAR elects the Condorcet winner B with full ballots (BV2162: 346/407/312/171) and with truncated ones: no truncation incentive on this profile, while the IRV race's winner flips A → B on the same change.
Live results: https://bettervoting.com/74j6vv/results

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
A,B,C,D
33: 5,4,2,1
29: 4,5,2,1
24: 2,4,5,1
17: 0,0,0,5
```

## What the engine says

Full report from the [`_tabulated` mirror](../felsenthal_paradoxes_tabulated/bv2163_74j6vv_star_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |     * A      |    * B      |      C      |      D      |
---------------------------------------------------------------------------
           * A > |     ---      |33 - 17 - 53 |62 - 17 - 24 |86 -  0 - 17 |
           * B > | 53 - 17 - 33 |    ---      |62 - 17 - 24 |86 -  0 - 17 |
             C > | 24 - 17 - 62 |24 - 17 - 62 |    ---      |86 -  0 - 17 |
             D > | 17 -  0 - 86 |17 -  0 - 86 |17 -  0 - 86 |    ---      |

[Condorcet Winner]
  Condorcet Winner: B — matches the STAR winner

[Divergence from STAR]
  STAR                   = B
  Choose-One (Plurality) = A   (differs from STAR)

--- STAR Voting Method (single winner) ---
[STAR Voting]
 Tabulating 103 ballots.
Count × A,B,C,D
   33 × 5,4,2,1
   29 × 4,5,2,1
   24 × 2,4,5,1
   17 × 0,0,0,5

[Score Distribution] (how many ballots gave each star rating)
                   Score
Candidate   5   4   3   2   1   0  | Total   Avg
A          33  29   0  24   0  17  |   329   3.2
B          29  57   0   0   0  17  |   373   3.6
C          24   0   0  62   0  17  |   244   2.4
D          17   0   0   0  86   0  |   171   1.7

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   B             -- 373 -- First place
   A             -- 329 -- Second place
   C             -- 244
   D             -- 171
 B and A advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   B             -- 53 -- First place
   A             -- 33
   Equal Support -- 17
 B wins.
   Runoff math:
     103  ballots cast
   −  17  Equal Support (no preference between the two finalists)
     ───
      86  voters with a preference  (majority = 44)
           B 53 (62%)  ·  A 33 (38%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 B
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/felsenthal_paradoxes/bv2163_74j6vv_star.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README.md)
- [Runoff reversal (worked set)](../../../01_STAR/runoff_overturns_leader/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [bv2144_mxfmhm_plurality](bv2144_mxfmhm_plurality.md) · [bv2144_mxfmhm_star](bv2144_mxfmhm_star.md) · [bv2145_6fj2kg_irv](bv2145_6fj2kg_irv.md) · [bv2145_6fj2kg_ranked_robin](bv2145_6fj2kg_ranked_robin.md) · [bv2145_6fj2kg_star](bv2145_6fj2kg_star.md) · [bv2146_krk2px_irv](bv2146_krk2px_irv.md) · [bv2146_krk2px_ranked_robin](bv2146_krk2px_ranked_robin.md) · [bv2146_krk2px_star](bv2146_krk2px_star.md) · [bv2147_9gdrqg_irv](bv2147_9gdrqg_irv.md) · [bv2147_9gdrqg_star](bv2147_9gdrqg_star.md) · [bv2148_h87k6v_irv](bv2148_h87k6v_irv.md) · [bv2148_h87k6v_star](bv2148_h87k6v_star.md) · [bv2149_byk9v2_irv](bv2149_byk9v2_irv.md) · [bv2149_byk9v2_star](bv2149_byk9v2_star.md) · [bv2150_dxg8pb_irv](bv2150_dxg8pb_irv.md) · [bv2150_dxg8pb_ranked_robin](bv2150_dxg8pb_ranked_robin.md) · [bv2150_dxg8pb_star](bv2150_dxg8pb_star.md) · [bv2151_97hbpw_irv](bv2151_97hbpw_irv.md) · [bv2151_97hbpw_ranked_robin](bv2151_97hbpw_ranked_robin.md) · [bv2151_97hbpw_star](bv2151_97hbpw_star.md) · [bv2152_r6ctvy_approval](bv2152_r6ctvy_approval.md) · [bv2152_r6ctvy_ranked_robin](bv2152_r6ctvy_ranked_robin.md) · [bv2153_pcttmr_approval](bv2153_pcttmr_approval.md) · [bv2153_pcttmr_irv](bv2153_pcttmr_irv.md) · [bv2153_pcttmr_ranked_robin](bv2153_pcttmr_ranked_robin.md) · [bv2154_wq6yv7_approval](bv2154_wq6yv7_approval.md) · [bv2154_wq6yv7_irv](bv2154_wq6yv7_irv.md) · [bv2154_wq6yv7_ranked_robin](bv2154_wq6yv7_ranked_robin.md) · [bv2160_r6qc8h_plurality](bv2160_r6qc8h_plurality.md) · [bv2160_r6qc8h_star](bv2160_r6qc8h_star.md) · [bv2161_q3h4fk_plurality](bv2161_q3h4fk_plurality.md) · [bv2161_q3h4fk_star](bv2161_q3h4fk_star.md) · [bv2162_4htk44_irv](bv2162_4htk44_irv.md) · [bv2162_4htk44_ranked_robin](bv2162_4htk44_ranked_robin.md) · [bv2162_4htk44_star](bv2162_4htk44_star.md) · [bv2163_74j6vv_irv](bv2163_74j6vv_irv.md) · [bv2163_74j6vv_ranked_robin](bv2163_74j6vv_ranked_robin.md) · [bv2164_xbqq8t_plurality](bv2164_xbqq8t_plurality.md) · [bv2164_xbqq8t_ranked_robin](bv2164_xbqq8t_ranked_robin.md) · [bv2164_xbqq8t_star](bv2164_xbqq8t_star.md) · [bv2165_9vxcj7_plurality](bv2165_9vxcj7_plurality.md) · [bv2165_9vxcj7_star](bv2165_9vxcj7_star.md) · [bv2166_b7b8dv_plurality](bv2166_b7b8dv_plurality.md) · [bv2166_b7b8dv_star](bv2166_b7b8dv_star.md) · [bv2167_f3dxq9_plurality](bv2167_f3dxq9_plurality.md) · [bv2167_f3dxq9_star](bv2167_f3dxq9_star.md) · [felsenthal_ex6_pareto_approval](felsenthal_ex6_pareto_approval.md) · [felsenthal_ex6_ranked_robin](felsenthal_ex6_ranked_robin.md)
