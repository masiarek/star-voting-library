# Borda SCC Ex.15 — STAR: C wins (and stays won when a loser exits)

*Generated from [`bv2161_q3h4fk_star.yaml`](../bv2161_q3h4fk_star.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** C

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/q3h4fk) · **[results ↗](https://bettervoting.com/q3h4fk/results)** (election `q3h4fk`).

## Scenario

Race 1 of 2 in the Borda-SCC election (BV2161, bvid q3h4fk; BV-confirmed). Source: Dan S. Felsenthal, "Review of Paradoxes Afflicting Various Voting Procedures Where One Out of m Candidates (m ≥ 2) Must Be Elected", University of Haifa / LSE, revised 26 May 2010; Appendix A5, Example 15.
7 voters, three candidates: 2×(A>C>B), 2×(B>A>C), 3×(C>B>A). NOTE: the paper prints the third bloc as C>A>B, but its own Borda totals (6/7/8, summing to 21) are only consistent with C>B>A — this case uses the arithmetic-consistent profile. The Borda paradox lives on the case page: Borda elects C (8 points), but if B — a LOSING candidate — drops out, Borda on the remaining pair elects A 4–3: SCC violated. This STAR race (5/3/1 map) scores A 19, B 21, C 23; C beats B 5–2 in the runoff — STAR agrees with Borda's initial pick. Honest note: if B exits, A beats C head-to-head 4–3, so a two-candidate contest elects A under ANY method, STAR included — on a cyclic profile (B>A 5–2, A>C 4–3, C>B 5–2) every method's winner is exit-sensitive; Felsenthal's charge is that Borda's POINT COUNT did the flipping. The cycle is also why no Ranked Robin or IRV race exists here (random ties on BV).
Live results: https://bettervoting.com/q3h4fk/results

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
A,B,C
5,1,3
5,1,3
3,5,1
3,5,1
1,3,5
1,3,5
1,3,5
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR     = C
  Approval = B   (differs from STAR)

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 7 ballots.
Count × A,B,C
    3 × 1,3,5
    2 × 5,1,3
    2 × 3,5,1

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   C             -- 23 -- First place
   B             -- 21 -- Second place
   A             -- 19
 C and B advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   C             -- 5 -- First place
   B             -- 2
   Equal Support -- 0
 C wins.
   Runoff math:
     7  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     7  voters with a preference  (majority = 4)
           C 5 (71%)  ·  B 2 (29%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 C
```

<details>
<summary>Full audit — preference matrix, Condorcet, and score distribution</summary>

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |      A     |   * B     |   * C     |
-----------------------------------------------------
           A > |    ---     |2 - 0 - 5  |4 - 0 - 3  |
         * B > | 5 - 0 - 2  |   ---     |2 - 0 - 5  |
         * C > | 3 - 0 - 4  |5 - 0 - 2  |   ---     |

[Condorcet Winner]
  No Condorcet winner (majority cycle: A > C > B > A)

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
A          2  0  2  0  3  0  |    19   2.7
B          2  0  3  0  2  0  |    21   3.0
C          3  0  2  0  2  0  |    23   3.3
```

</details>

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/bv2161_q3h4fk_star_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/felsenthal_paradoxes/cases/bv2161_q3h4fk_star.yaml
```

## See also

- [Methods disagree on this election](../../../divergence_review/cases/APPROVAL_OR_MINOR/bv2161_q3h4fk_star.md) — its entry in the divergence review ledger
- [Condorcet efficiency (topic hub)](../../../../00_start_here/topics/condorcet/README.md)
- [Ties & tie-breaking (topic hub)](../../../../00_start_here/topics/ties/README.md)
- [Runoff reversal (worked set)](../../../../01_STAR/runoff_overturns_leader/README.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [bv2144_mxfmhm_plurality](bv2144_mxfmhm_plurality.md) · [bv2144_mxfmhm_star](bv2144_mxfmhm_star.md) · [bv2145_6fj2kg_irv](bv2145_6fj2kg_irv.md) · [bv2145_6fj2kg_ranked_robin](bv2145_6fj2kg_ranked_robin.md) · [bv2145_6fj2kg_star](bv2145_6fj2kg_star.md) · [bv2146_krk2px_irv](bv2146_krk2px_irv.md) · [bv2146_krk2px_ranked_robin](bv2146_krk2px_ranked_robin.md) · [bv2146_krk2px_star](bv2146_krk2px_star.md) · [bv2147_9gdrqg_irv](bv2147_9gdrqg_irv.md) · [bv2147_9gdrqg_star](bv2147_9gdrqg_star.md) · [bv2148_h87k6v_irv](bv2148_h87k6v_irv.md) · [bv2148_h87k6v_star](bv2148_h87k6v_star.md) · [bv2149_byk9v2_irv](bv2149_byk9v2_irv.md) · [bv2149_byk9v2_star](bv2149_byk9v2_star.md) · [bv2150_dxg8pb_irv](bv2150_dxg8pb_irv.md) · [bv2150_dxg8pb_ranked_robin](bv2150_dxg8pb_ranked_robin.md) · [bv2150_dxg8pb_star](bv2150_dxg8pb_star.md) · [bv2151_97hbpw_irv](bv2151_97hbpw_irv.md) · [bv2151_97hbpw_ranked_robin](bv2151_97hbpw_ranked_robin.md) · [bv2151_97hbpw_star](bv2151_97hbpw_star.md) · [bv2152_r6ctvy_approval](bv2152_r6ctvy_approval.md) · [bv2152_r6ctvy_ranked_robin](bv2152_r6ctvy_ranked_robin.md) · [bv2153_pcttmr_approval](bv2153_pcttmr_approval.md) · [bv2153_pcttmr_irv](bv2153_pcttmr_irv.md) · [bv2153_pcttmr_ranked_robin](bv2153_pcttmr_ranked_robin.md) · [bv2154_wq6yv7_approval](bv2154_wq6yv7_approval.md) · [bv2154_wq6yv7_irv](bv2154_wq6yv7_irv.md) · [bv2154_wq6yv7_ranked_robin](bv2154_wq6yv7_ranked_robin.md) · [bv2160_r6qc8h_plurality](bv2160_r6qc8h_plurality.md) · [bv2160_r6qc8h_star](bv2160_r6qc8h_star.md) · [bv2161_q3h4fk_plurality](bv2161_q3h4fk_plurality.md) · [bv2162_4htk44_irv](bv2162_4htk44_irv.md) · [bv2162_4htk44_ranked_robin](bv2162_4htk44_ranked_robin.md) · [bv2162_4htk44_star](bv2162_4htk44_star.md) · [bv2163_74j6vv_irv](bv2163_74j6vv_irv.md) · [bv2163_74j6vv_ranked_robin](bv2163_74j6vv_ranked_robin.md) · [bv2163_74j6vv_star](bv2163_74j6vv_star.md) · [bv2164_xbqq8t_plurality](bv2164_xbqq8t_plurality.md) · [bv2164_xbqq8t_ranked_robin](bv2164_xbqq8t_ranked_robin.md) · [bv2164_xbqq8t_star](bv2164_xbqq8t_star.md) · [bv2165_9vxcj7_plurality](bv2165_9vxcj7_plurality.md) · [bv2165_9vxcj7_star](bv2165_9vxcj7_star.md) · [bv2166_b7b8dv_plurality](bv2166_b7b8dv_plurality.md) · [bv2166_b7b8dv_star](bv2166_b7b8dv_star.md) · [bv2167_f3dxq9_plurality](bv2167_f3dxq9_plurality.md) · [bv2167_f3dxq9_star](bv2167_f3dxq9_star.md) · [felsenthal_ex6_pareto_approval](felsenthal_ex6_pareto_approval.md) · [felsenthal_ex6_ranked_robin](felsenthal_ex6_ranked_robin.md)
