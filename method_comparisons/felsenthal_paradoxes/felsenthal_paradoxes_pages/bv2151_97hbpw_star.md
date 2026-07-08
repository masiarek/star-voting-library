# Felsenthal Ex.4 after two no-shows — STAR: unmoved, still Beth

*Generated from [`bv2151_97hbpw_star.yaml`](../bv2151_97hbpw_star.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Beth

## Scenario

Race 3 of 3 in the No-Show-paradox pair, part 2 of 2 (BV2151, bvid 97hbpw; BV-confirmed). Source: Dan S. Felsenthal (2010), Appendix A2, Example 4 — see bv2151_97hbpw_irv.yaml for the setup.
The same 9 voters with ranks mapped 5/3/1. Scores: Andy 19, Beth 31, Carl 31 — Beth and Carl both clear Andy and advance (no advancement tie), and Beth wins the automatic runoff 5–4. STAR elects Beth with 11 voters (BV2150: 29/37/33, runoff 7–4) and with 9: same winner either way, so the Andy voters' participation never backfired under STAR in this pair.
Live results: https://bettervoting.com/97hbpw/results

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Andy,Beth,Carl
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

Full report from the [`_tabulated` mirror](../felsenthal_paradoxes_tabulated/bv2151_97hbpw_star_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |     Andy   |  * Beth   |  * Carl   |
-----------------------------------------------------
        Andy > |    ---     |3 - 0 - 6  |2 - 0 - 7  |
      * Beth > | 6 - 0 - 3  |   ---     |5 - 0 - 4  |
      * Carl > | 7 - 0 - 2  |4 - 0 - 5  |   ---     |

[Condorcet Winner]
  Condorcet Winner: Beth — matches the STAR winner

[Divergence from STAR]
  STAR                   = Beth
  Choose-One (Plurality) = Carl   (differs from STAR)

--- STAR Voting Method (single winner) ---
[STAR Voting]
 Tabulating 9 ballots.
Count × Andy,Beth,Carl
    3 ×    1,   5,   3
    3 ×    1,   3,   5
    2 ×    5,   3,   1
    1 ×    3,   1,   5

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Andy       2  0  1  0  6  0  |    19   2.1
Beth       3  0  5  0  1  0  |    31   3.4
Carl       4  0  3  0  2  0  |    31   3.4

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Beth          -- 31 -- First place
   Carl          -- 31 -- Second place
   Andy          -- 19
 Beth and Carl advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Beth          -- 5 -- First place
   Carl          -- 4
   Equal Support -- 0
 Beth wins.
   Runoff math:
     9  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     9  voters with a preference  (majority = 5)
           Beth 5 (56%)  ·  Carl 4 (44%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Beth
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/felsenthal_paradoxes/bv2151_97hbpw_star.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Ties & tie-breaking (topic hub)](../../../00_start_here/topics/ties/README.md)
- [Runoff reversal (worked set)](../../../01_STAR/runoff_overturns_leader/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [bv2144_mxfmhm_plurality](bv2144_mxfmhm_plurality.md) · [bv2144_mxfmhm_star](bv2144_mxfmhm_star.md) · [bv2145_6fj2kg_irv](bv2145_6fj2kg_irv.md) · [bv2145_6fj2kg_ranked_robin](bv2145_6fj2kg_ranked_robin.md) · [bv2145_6fj2kg_star](bv2145_6fj2kg_star.md) · [bv2146_krk2px_irv](bv2146_krk2px_irv.md) · [bv2146_krk2px_ranked_robin](bv2146_krk2px_ranked_robin.md) · [bv2146_krk2px_star](bv2146_krk2px_star.md) · [bv2147_9gdrqg_irv](bv2147_9gdrqg_irv.md) · [bv2147_9gdrqg_star](bv2147_9gdrqg_star.md) · [bv2148_h87k6v_irv](bv2148_h87k6v_irv.md) · [bv2148_h87k6v_star](bv2148_h87k6v_star.md) · [bv2149_byk9v2_irv](bv2149_byk9v2_irv.md) · [bv2149_byk9v2_star](bv2149_byk9v2_star.md) · [bv2150_dxg8pb_irv](bv2150_dxg8pb_irv.md) · [bv2150_dxg8pb_ranked_robin](bv2150_dxg8pb_ranked_robin.md) · [bv2150_dxg8pb_star](bv2150_dxg8pb_star.md) · [bv2151_97hbpw_irv](bv2151_97hbpw_irv.md) · [bv2151_97hbpw_ranked_robin](bv2151_97hbpw_ranked_robin.md) · [bv2152_r6ctvy_approval](bv2152_r6ctvy_approval.md) · [bv2152_r6ctvy_ranked_robin](bv2152_r6ctvy_ranked_robin.md) · [bv2153_pcttmr_approval](bv2153_pcttmr_approval.md) · [bv2153_pcttmr_irv](bv2153_pcttmr_irv.md) · [bv2153_pcttmr_ranked_robin](bv2153_pcttmr_ranked_robin.md) · [bv2154_wq6yv7_approval](bv2154_wq6yv7_approval.md) · [bv2154_wq6yv7_irv](bv2154_wq6yv7_irv.md) · [bv2154_wq6yv7_ranked_robin](bv2154_wq6yv7_ranked_robin.md) · [bv2160_r6qc8h_plurality](bv2160_r6qc8h_plurality.md) · [bv2160_r6qc8h_star](bv2160_r6qc8h_star.md) · [bv2161_q3h4fk_plurality](bv2161_q3h4fk_plurality.md) · [bv2161_q3h4fk_star](bv2161_q3h4fk_star.md) · [bv2162_4htk44_irv](bv2162_4htk44_irv.md) · [bv2162_4htk44_ranked_robin](bv2162_4htk44_ranked_robin.md) · [bv2162_4htk44_star](bv2162_4htk44_star.md) · [bv2163_74j6vv_irv](bv2163_74j6vv_irv.md) · [bv2163_74j6vv_ranked_robin](bv2163_74j6vv_ranked_robin.md) · [bv2163_74j6vv_star](bv2163_74j6vv_star.md) · [bv2164_xbqq8t_plurality](bv2164_xbqq8t_plurality.md) · [bv2164_xbqq8t_ranked_robin](bv2164_xbqq8t_ranked_robin.md) · [bv2164_xbqq8t_star](bv2164_xbqq8t_star.md) · [bv2165_9vxcj7_plurality](bv2165_9vxcj7_plurality.md) · [bv2165_9vxcj7_star](bv2165_9vxcj7_star.md) · [bv2166_b7b8dv_plurality](bv2166_b7b8dv_plurality.md) · [bv2166_b7b8dv_star](bv2166_b7b8dv_star.md) · [felsenthal_ex6_pareto_approval](felsenthal_ex6_pareto_approval.md) · [felsenthal_ex6_ranked_robin](felsenthal_ex6_ranked_robin.md)
