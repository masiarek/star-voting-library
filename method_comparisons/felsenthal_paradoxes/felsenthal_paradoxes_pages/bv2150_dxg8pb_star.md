# Felsenthal Ex.4 full electorate — STAR: elects the Condorcet winner Beth

*Generated from [`bv2150_dxg8pb_star.yaml`](../bv2150_dxg8pb_star.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Beth

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/dxg8pb) · **[results ↗](https://bettervoting.com/dxg8pb/results)** (election `dxg8pb`).

## Scenario

Race 3 of 3 in the No-Show-paradox pair, part 1 of 2 (BV2150, bvid dxg8pb; BV-confirmed). Source: Dan S. Felsenthal (2010), Appendix A2, Example 4 — see bv2150_dxg8pb_irv.yaml for the setup.
The same 11 voters with ranks mapped to 0–5 scores (5/3/1). Scores: Andy 29, Beth 37, Carl 33 — Beth and Carl advance, Beth wins the automatic runoff 7–4. STAR elects the Condorcet winner that the runoff procedure (the IRV race) deleted in round one.
Live results: https://bettervoting.com/dxg8pb/results

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Andy,Beth,Carl
5,3,1
5,3,1
5,3,1
5,3,1
1,5,3
1,5,3
1,5,3
3,1,5
1,3,5
1,3,5
1,3,5
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR                   = Beth
  Choose-One (Plurality) = Andy   (differs from STAR)
  RCV-IRV                = Carl   (differs from STAR)
  Note: no ballots had tied scores, so RCV-IRV vs STAR here is a genuine
        method difference, not a tie-breaking artifact.
  Note: Ranked Robin (RCV-RR) agrees with STAR, so RCV-IRV is the lone
        outlier — the classic center-squeeze signature.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: felsenthal_paradoxes_tabulated/bv2150_dxg8pb_star_RCV-IRV_tabulated.txt

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 11 ballots.
Count × Andy,Beth,Carl
    4 ×    5,   3,   1
    3 ×    1,   5,   3
    3 ×    1,   3,   5
    1 ×    3,   1,   5

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Beth          -- 37 -- First place
   Carl          -- 33 -- Second place
   Andy          -- 29
 Beth and Carl advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Beth          -- 7 -- First place
   Carl          -- 4
   Equal Support -- 0
 Beth wins.
   Runoff math:
     11  ballots cast
   −  0  Equal Support (no preference between the two finalists)
     ──
     11  voters with a preference  (majority = 6)
           Beth 7 (64%)  ·  Carl 4 (36%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Beth
```

<details>
<summary>Full audit — preference matrix, Condorcet, and score distribution</summary>

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |     Andy   |  * Beth   |  * Carl   |
-----------------------------------------------------
        Andy > |    ---     |5 - 0 - 6  |4 - 0 - 7  |
      * Beth > | 6 - 0 - 5  |   ---     |7 - 0 - 4  |
      * Carl > | 7 - 0 - 4  |4 - 0 - 7  |   ---     |

[Condorcet Winner]
  Condorcet Winner: Beth — matches the STAR winner

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Andy       4  0  1  0  6  0  |    29   2.6
Beth       3  0  7  0  1  0  |    37   3.4
Carl       4  0  3  0  4  0  |    33   3.0
```

</details>

Everything in one file: the [`_tabulated` mirror](../felsenthal_paradoxes_tabulated/bv2150_dxg8pb_star_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/felsenthal_paradoxes/bv2150_dxg8pb_star.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Methods disagree on this election](../../divergence_review/cases/IRV_OUTLIER_RR_WITH_STAR/bv2150_dxg8pb_star.md) — its entry in the divergence review ledger
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README.md)
- [Runoff reversal (worked set)](../../../01_STAR/runoff_overturns_leader/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [bv2144_mxfmhm_plurality](bv2144_mxfmhm_plurality.md) · [bv2144_mxfmhm_star](bv2144_mxfmhm_star.md) · [bv2145_6fj2kg_irv](bv2145_6fj2kg_irv.md) · [bv2145_6fj2kg_ranked_robin](bv2145_6fj2kg_ranked_robin.md) · [bv2145_6fj2kg_star](bv2145_6fj2kg_star.md) · [bv2146_krk2px_irv](bv2146_krk2px_irv.md) · [bv2146_krk2px_ranked_robin](bv2146_krk2px_ranked_robin.md) · [bv2146_krk2px_star](bv2146_krk2px_star.md) · [bv2147_9gdrqg_irv](bv2147_9gdrqg_irv.md) · [bv2147_9gdrqg_star](bv2147_9gdrqg_star.md) · [bv2148_h87k6v_irv](bv2148_h87k6v_irv.md) · [bv2148_h87k6v_star](bv2148_h87k6v_star.md) · [bv2149_byk9v2_irv](bv2149_byk9v2_irv.md) · [bv2149_byk9v2_star](bv2149_byk9v2_star.md) · [bv2150_dxg8pb_irv](bv2150_dxg8pb_irv.md) · [bv2150_dxg8pb_ranked_robin](bv2150_dxg8pb_ranked_robin.md) · [bv2151_97hbpw_irv](bv2151_97hbpw_irv.md) · [bv2151_97hbpw_ranked_robin](bv2151_97hbpw_ranked_robin.md) · [bv2151_97hbpw_star](bv2151_97hbpw_star.md) · [bv2152_r6ctvy_approval](bv2152_r6ctvy_approval.md) · [bv2152_r6ctvy_ranked_robin](bv2152_r6ctvy_ranked_robin.md) · [bv2153_pcttmr_approval](bv2153_pcttmr_approval.md) · [bv2153_pcttmr_irv](bv2153_pcttmr_irv.md) · [bv2153_pcttmr_ranked_robin](bv2153_pcttmr_ranked_robin.md) · [bv2154_wq6yv7_approval](bv2154_wq6yv7_approval.md) · [bv2154_wq6yv7_irv](bv2154_wq6yv7_irv.md) · [bv2154_wq6yv7_ranked_robin](bv2154_wq6yv7_ranked_robin.md) · [bv2160_r6qc8h_plurality](bv2160_r6qc8h_plurality.md) · [bv2160_r6qc8h_star](bv2160_r6qc8h_star.md) · [bv2161_q3h4fk_plurality](bv2161_q3h4fk_plurality.md) · [bv2161_q3h4fk_star](bv2161_q3h4fk_star.md) · [bv2162_4htk44_irv](bv2162_4htk44_irv.md) · [bv2162_4htk44_ranked_robin](bv2162_4htk44_ranked_robin.md) · [bv2162_4htk44_star](bv2162_4htk44_star.md) · [bv2163_74j6vv_irv](bv2163_74j6vv_irv.md) · [bv2163_74j6vv_ranked_robin](bv2163_74j6vv_ranked_robin.md) · [bv2163_74j6vv_star](bv2163_74j6vv_star.md) · [bv2164_xbqq8t_plurality](bv2164_xbqq8t_plurality.md) · [bv2164_xbqq8t_ranked_robin](bv2164_xbqq8t_ranked_robin.md) · [bv2164_xbqq8t_star](bv2164_xbqq8t_star.md) · [bv2165_9vxcj7_plurality](bv2165_9vxcj7_plurality.md) · [bv2165_9vxcj7_star](bv2165_9vxcj7_star.md) · [bv2166_b7b8dv_plurality](bv2166_b7b8dv_plurality.md) · [bv2166_b7b8dv_star](bv2166_b7b8dv_star.md) · [bv2167_f3dxq9_plurality](bv2167_f3dxq9_plurality.md) · [bv2167_f3dxq9_star](bv2167_f3dxq9_star.md) · [felsenthal_ex6_pareto_approval](felsenthal_ex6_pareto_approval.md) · [felsenthal_ex6_ranked_robin](felsenthal_ex6_ranked_robin.md)
