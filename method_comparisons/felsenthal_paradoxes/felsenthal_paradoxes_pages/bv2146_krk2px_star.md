# Felsenthal Ex.2 after the raise — STAR: unmoved, still Ada

*Generated from [`bv2146_krk2px_star.yaml`](../bv2146_krk2px_star.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Ada

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/krk2px) · **[results ↗](https://bettervoting.com/krk2px/results)** (election `krk2px`).

## Scenario

Race 3 of 3 in the Felsenthal runoff-paradoxes election, part 2 of 2 (BV2146, bvid krk2px; BV-confirmed). Source: Dan S. Felsenthal (2010), Appendix A2, Example 2 (continued) — see bv2146_krk2px_irv.yaml for the setup.
The same 17 voters after the raise, ranks mapped 5/3/1. Ben's two raised ballots move him 51 → 55 and Cleo 49 → 45; Ada stays 53. Finalists are now Ben and Ada — and Ada still wins the automatic runoff 9–8, exactly as in BV2145. Giving Ben more support changed STAR's finalist pair but not its winner: no more-is-less here, while the same raise flips the IRV race.
Live results: https://bettervoting.com/krk2px/results

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Ada,Ben,Cleo
5,3,1
5,3,1
5,3,1
5,1,3
5,1,3
3,5,1
3,5,1
3,5,1
3,5,1
1,5,3
1,5,3
3,1,5
3,1,5
3,1,5
3,1,5
1,5,3
1,5,3
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR                   = Ada
  Choose-One (Plurality) = Ben   (differs from STAR)

[Runoff Reversal]
 - Score Round Winner(s) = (Ben)
 - Runoff Round Winner   = (Ada)
  Candidate Ben earned the highest total score, but
  Candidate Ada won the automatic runoff — not a malfunction,
  STAR working as designed: the runoff elects the finalist preferred
  by the majority (of voters with a preference).

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 17 ballots.
Count × Ada,Ben,Cleo
    4 ×   3,  5,   1
    4 ×   1,  5,   3
    4 ×   3,  1,   5
    3 ×   5,  3,   1
    2 ×   5,  1,   3

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Ben           -- 55 -- First place
   Ada           -- 53 -- Second place
   Cleo          -- 45
 Ben and Ada advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Ada           -- 9 -- First place
   Ben           -- 8
   Equal Support -- 0
 Ada wins.
   Runoff math:
     17  ballots cast
   −  0  Equal Support (no preference between the two finalists)
     ──
     17  voters with a preference  (majority = 9)
           Ada 9 (53%)  ·  Ben 8 (47%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Ada
```

<details>
<summary>Full audit — preference matrix, Condorcet, and score distribution</summary>

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |    * Ada     |   * Ben     |     Cleo    |
-------------------------------------------------------------
         * Ada > |     ---      | 9 -  0 -  8 | 9 -  0 -  8 |
         * Ben > |  8 -  0 -  9 |    ---      |11 -  0 -  6 |
          Cleo > |  8 -  0 -  9 | 6 -  0 - 11 |    ---      |

[Condorcet Winner]
  Condorcet Winner: Ada — matches the STAR winner

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Ada        5  0  8  0  4  0  |    53   3.1
Ben        8  0  3  0  6  0  |    55   3.2
Cleo       4  0  6  0  7  0  |    45   2.6
```

</details>

Everything in one file: the [`_tabulated` mirror](../felsenthal_paradoxes_tabulated/bv2146_krk2px_star_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/felsenthal_paradoxes/bv2146_krk2px_star.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Runoff reversal (worked set)](../../../01_STAR/runoff_overturns_leader/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [bv2144_mxfmhm_plurality](bv2144_mxfmhm_plurality.md) · [bv2144_mxfmhm_star](bv2144_mxfmhm_star.md) · [bv2145_6fj2kg_irv](bv2145_6fj2kg_irv.md) · [bv2145_6fj2kg_ranked_robin](bv2145_6fj2kg_ranked_robin.md) · [bv2145_6fj2kg_star](bv2145_6fj2kg_star.md) · [bv2146_krk2px_irv](bv2146_krk2px_irv.md) · [bv2146_krk2px_ranked_robin](bv2146_krk2px_ranked_robin.md) · [bv2147_9gdrqg_irv](bv2147_9gdrqg_irv.md) · [bv2147_9gdrqg_star](bv2147_9gdrqg_star.md) · [bv2148_h87k6v_irv](bv2148_h87k6v_irv.md) · [bv2148_h87k6v_star](bv2148_h87k6v_star.md) · [bv2149_byk9v2_irv](bv2149_byk9v2_irv.md) · [bv2149_byk9v2_star](bv2149_byk9v2_star.md) · [bv2150_dxg8pb_irv](bv2150_dxg8pb_irv.md) · [bv2150_dxg8pb_ranked_robin](bv2150_dxg8pb_ranked_robin.md) · [bv2150_dxg8pb_star](bv2150_dxg8pb_star.md) · [bv2151_97hbpw_irv](bv2151_97hbpw_irv.md) · [bv2151_97hbpw_ranked_robin](bv2151_97hbpw_ranked_robin.md) · [bv2151_97hbpw_star](bv2151_97hbpw_star.md) · [bv2152_r6ctvy_approval](bv2152_r6ctvy_approval.md) · [bv2152_r6ctvy_ranked_robin](bv2152_r6ctvy_ranked_robin.md) · [bv2153_pcttmr_approval](bv2153_pcttmr_approval.md) · [bv2153_pcttmr_irv](bv2153_pcttmr_irv.md) · [bv2153_pcttmr_ranked_robin](bv2153_pcttmr_ranked_robin.md) · [bv2154_wq6yv7_approval](bv2154_wq6yv7_approval.md) · [bv2154_wq6yv7_irv](bv2154_wq6yv7_irv.md) · [bv2154_wq6yv7_ranked_robin](bv2154_wq6yv7_ranked_robin.md) · [bv2160_r6qc8h_plurality](bv2160_r6qc8h_plurality.md) · [bv2160_r6qc8h_star](bv2160_r6qc8h_star.md) · [bv2161_q3h4fk_plurality](bv2161_q3h4fk_plurality.md) · [bv2161_q3h4fk_star](bv2161_q3h4fk_star.md) · [bv2162_4htk44_irv](bv2162_4htk44_irv.md) · [bv2162_4htk44_ranked_robin](bv2162_4htk44_ranked_robin.md) · [bv2162_4htk44_star](bv2162_4htk44_star.md) · [bv2163_74j6vv_irv](bv2163_74j6vv_irv.md) · [bv2163_74j6vv_ranked_robin](bv2163_74j6vv_ranked_robin.md) · [bv2163_74j6vv_star](bv2163_74j6vv_star.md) · [bv2164_xbqq8t_plurality](bv2164_xbqq8t_plurality.md) · [bv2164_xbqq8t_ranked_robin](bv2164_xbqq8t_ranked_robin.md) · [bv2164_xbqq8t_star](bv2164_xbqq8t_star.md) · [bv2165_9vxcj7_plurality](bv2165_9vxcj7_plurality.md) · [bv2165_9vxcj7_star](bv2165_9vxcj7_star.md) · [bv2166_b7b8dv_plurality](bv2166_b7b8dv_plurality.md) · [bv2166_b7b8dv_star](bv2166_b7b8dv_star.md) · [bv2167_f3dxq9_plurality](bv2167_f3dxq9_plurality.md) · [bv2167_f3dxq9_star](bv2167_f3dxq9_star.md) · [felsenthal_ex6_pareto_approval](felsenthal_ex6_pareto_approval.md) · [felsenthal_ex6_ranked_robin](felsenthal_ex6_ranked_robin.md)
