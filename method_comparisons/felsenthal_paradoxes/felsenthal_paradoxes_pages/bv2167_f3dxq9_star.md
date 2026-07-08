# Minimax Ex.29 — STAR: elects B, a top-cycle member, not the universal loser

*Generated from [`bv2167_f3dxq9_star.yaml`](../bv2167_f3dxq9_star.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** B

## Scenario

Race 1 of 2 in the Minimax-elects-the-absolute-loser election (BV2167, bvid f3dxq9; BV-confirmed). Source: Dan S. Felsenthal, "Review of Paradoxes Afflicting Various Voting Procedures Where One Out of m Candidates (m ≥ 2) Must Be Elected", University of Haifa / LSE, revised 26 May 2010; Appendix A10 (the Condorcet / Minimax / Simpson-Kramer procedure), Example 29.
11 voters, four candidates: 2×(D>A>C>B), 3×(D>B>A>C), 3×(C>B>A>D), 1×(B>A>C>D), 2×(A>C>B>D). A, B, C form a top cycle (B>A 7–4, A>C 8–3, C>B 7–4); D loses every matchup 5–6 — the Condorcet loser AND absolute loser (6 of 11 rank D last). Minimax — worked on the case page; no tabulator on BV or in LH — elects D, whose worst loss (6) is the smallest (A/B/C: 7/7/8). This STAR race (ranks mapped 5/4/2/1): A 34, B 35, C 32, D 31 — B and A advance, B wins the automatic runoff 7–4. No RR race (the A/B/C Copeland tie → BV random) and no IRV race (random transfer tie).
Live results: https://bettervoting.com/f3dxq9/results

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
A,B,C,D
4,1,2,5
4,1,2,5
2,4,1,5
2,4,1,5
2,4,1,5
2,4,5,1
2,4,5,1
2,4,5,1
4,5,2,1
5,2,4,1
5,2,4,1
```

## What the engine says

Full report from the [`_tabulated` mirror](../felsenthal_paradoxes_tabulated/bv2167_f3dxq9_star_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |    * A     |   * B     |     C     |     D     |
-----------------------------------------------------------------
         * A > |    ---     |4 - 0 - 7  |8 - 0 - 3  |6 - 0 - 5  |
         * B > | 7 - 0 - 4  |   ---     |4 - 0 - 7  |6 - 0 - 5  |
           C > | 3 - 0 - 8  |7 - 0 - 4  |   ---     |6 - 0 - 5  |
           D > | 5 - 0 - 6  |5 - 0 - 6  |5 - 0 - 6  |   ---     |

[Condorcet Winner]
  No Condorcet winner (majority cycle: A > C > B > A)

[Divergence from STAR]
  STAR                   = B
  Choose-One (Plurality) = D   (differs from STAR)
  RCV-IRV                = C   (differs from STAR)
  RCV-RR                 = A   (differs from STAR)
  Note: no ballots had tied scores, so RCV-IRV vs STAR here is a genuine
        method difference, not a tie-breaking artifact.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: felsenthal_paradoxes_tabulated/bv2167_f3dxq9_star_RCV-IRV_tabulated.txt
  RCV-RR round-robin: felsenthal_paradoxes_tabulated/bv2167_f3dxq9_star_RCV-RR_tabulated.txt

--- STAR Voting Method (single winner) ---
[STAR Voting]
 Tabulating 11 ballots.
Count × A,B,C,D
    3 × 2,4,1,5
    3 × 2,4,5,1
    2 × 4,1,2,5
    2 × 5,2,4,1
    1 × 4,5,2,1

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
A          2  3  0  6  0  0  |    34   3.1
B          1  6  0  2  2  0  |    35   3.2
C          3  2  0  3  3  0  |    32   2.9
D          5  0  0  0  6  0  |    31   2.8

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   B             -- 35 -- First place
   A             -- 34 -- Second place
   C             -- 32
   D             -- 31
 B and A advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   B             -- 7 -- First place
   A             -- 4
   Equal Support -- 0
 B wins.
   Runoff math:
     11  ballots cast
   −  0  Equal Support (no preference between the two finalists)
     ──
     11  voters with a preference  (majority = 6)
           B 7 (64%)  ·  A 4 (36%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 B
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/felsenthal_paradoxes/bv2167_f3dxq9_star.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README.md)
- [Ties & tie-breaking (topic hub)](../../../00_start_here/topics/ties/README.md)
- [Runoff reversal (worked set)](../../../01_STAR/runoff_overturns_leader/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [bv2144_mxfmhm_plurality](bv2144_mxfmhm_plurality.md) · [bv2144_mxfmhm_star](bv2144_mxfmhm_star.md) · [bv2145_6fj2kg_irv](bv2145_6fj2kg_irv.md) · [bv2145_6fj2kg_ranked_robin](bv2145_6fj2kg_ranked_robin.md) · [bv2145_6fj2kg_star](bv2145_6fj2kg_star.md) · [bv2146_krk2px_irv](bv2146_krk2px_irv.md) · [bv2146_krk2px_ranked_robin](bv2146_krk2px_ranked_robin.md) · [bv2146_krk2px_star](bv2146_krk2px_star.md) · [bv2147_9gdrqg_irv](bv2147_9gdrqg_irv.md) · [bv2147_9gdrqg_star](bv2147_9gdrqg_star.md) · [bv2148_h87k6v_irv](bv2148_h87k6v_irv.md) · [bv2148_h87k6v_star](bv2148_h87k6v_star.md) · [bv2149_byk9v2_irv](bv2149_byk9v2_irv.md) · [bv2149_byk9v2_star](bv2149_byk9v2_star.md) · [bv2150_dxg8pb_irv](bv2150_dxg8pb_irv.md) · [bv2150_dxg8pb_ranked_robin](bv2150_dxg8pb_ranked_robin.md) · [bv2150_dxg8pb_star](bv2150_dxg8pb_star.md) · [bv2151_97hbpw_irv](bv2151_97hbpw_irv.md) · [bv2151_97hbpw_ranked_robin](bv2151_97hbpw_ranked_robin.md) · [bv2151_97hbpw_star](bv2151_97hbpw_star.md) · [bv2152_r6ctvy_approval](bv2152_r6ctvy_approval.md) · [bv2152_r6ctvy_ranked_robin](bv2152_r6ctvy_ranked_robin.md) · [bv2153_pcttmr_approval](bv2153_pcttmr_approval.md) · [bv2153_pcttmr_irv](bv2153_pcttmr_irv.md) · [bv2153_pcttmr_ranked_robin](bv2153_pcttmr_ranked_robin.md) · [bv2154_wq6yv7_approval](bv2154_wq6yv7_approval.md) · [bv2154_wq6yv7_irv](bv2154_wq6yv7_irv.md) · [bv2154_wq6yv7_ranked_robin](bv2154_wq6yv7_ranked_robin.md) · [bv2160_r6qc8h_plurality](bv2160_r6qc8h_plurality.md) · [bv2160_r6qc8h_star](bv2160_r6qc8h_star.md) · [bv2161_q3h4fk_plurality](bv2161_q3h4fk_plurality.md) · [bv2161_q3h4fk_star](bv2161_q3h4fk_star.md) · [bv2162_4htk44_irv](bv2162_4htk44_irv.md) · [bv2162_4htk44_ranked_robin](bv2162_4htk44_ranked_robin.md) · [bv2162_4htk44_star](bv2162_4htk44_star.md) · [bv2163_74j6vv_irv](bv2163_74j6vv_irv.md) · [bv2163_74j6vv_ranked_robin](bv2163_74j6vv_ranked_robin.md) · [bv2163_74j6vv_star](bv2163_74j6vv_star.md) · [bv2164_xbqq8t_plurality](bv2164_xbqq8t_plurality.md) · [bv2164_xbqq8t_ranked_robin](bv2164_xbqq8t_ranked_robin.md) · [bv2164_xbqq8t_star](bv2164_xbqq8t_star.md) · [bv2165_9vxcj7_plurality](bv2165_9vxcj7_plurality.md) · [bv2165_9vxcj7_star](bv2165_9vxcj7_star.md) · [bv2166_b7b8dv_plurality](bv2166_b7b8dv_plurality.md) · [bv2166_b7b8dv_star](bv2166_b7b8dv_star.md) · [bv2167_f3dxq9_plurality](bv2167_f3dxq9_plurality.md) · [felsenthal_ex6_pareto_approval](felsenthal_ex6_pareto_approval.md) · [felsenthal_ex6_ranked_robin](felsenthal_ex6_ranked_robin.md)
