# Fishburn Ex.14 — STAR: B wins the electorate whose Borda count is truncation-unstable

*Generated from [`bv2160_r6qc8h_star.yaml`](../bv2160_r6qc8h_star.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** B

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/r6qc8h) · **[results ↗](https://bettervoting.com/r6qc8h/results)** (election `r6qc8h`).

## Scenario

Race 1 of 2 in the Borda-truncation election (BV2160, bvid r6qc8h; BV-confirmed). Source: Dan S. Felsenthal, "Review of Paradoxes Afflicting Various Voting Procedures Where One Out of m Candidates (m ≥ 2) Must Be Elected", University of Haifa / LSE, revised 26 May 2010; Appendix A5, Example 14 — adapted from Fishburn (1974: 543).
7 voters, four candidates: 3×(A>B>C>D), 1×(B>C>A>D), 1×(B>C>D>A), 2×(C>D>A>B). The Borda paradox lives on the case page (no Borda tabulator on BetterVoting or in the LH engine): Borda awards A 19, B 19, C 20, D 12 → C, but if the three A>B>C>D voters TRUNCATE C, Borda gives 16/16/14/12 — a truncation flips the winner away from C. This STAR race (ranks mapped 5/4/2/1) scores A 22, B 24, C 24, D 14: B and C take both finalist seats and B wins the automatic runoff 5–2. The pairwise preferences are a CYCLE (A>B 5–2, B>C 5–2, C>A 4–3), which is why no Ranked Robin or IRV race exists here (both would hit random ties on BetterVoting).
Live results: https://bettervoting.com/r6qc8h/results

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
A,B,C,D
5,4,2,1
5,4,2,1
5,4,2,1
2,5,4,1
1,5,4,2
2,1,5,4
2,1,5,4
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR                   = B
  Choose-One (Plurality) = A   (differs from STAR)
  RCV-IRV                = A   (differs from STAR)
  RCV-RR                 = C   (differs from STAR)
  Note: no ballots had tied scores, so RCV-IRV vs STAR here is a genuine
        method difference, not a tie-breaking artifact.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: felsenthal_paradoxes_tabulated/bv2160_r6qc8h_star_RCV-IRV_tabulated.txt
  RCV-RR round-robin: felsenthal_paradoxes_tabulated/bv2160_r6qc8h_star_RCV-RR_tabulated.txt

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 7 ballots.
Count × A,B,C,D
    3 × 5,4,2,1
    2 × 2,1,5,4
    1 × 2,5,4,1
    1 × 1,5,4,2

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   B             -- 24 -- First place
   C             -- 24 -- Second place
   A             -- 22
   D             -- 14
 B and C advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   B             -- 5 -- First place
   C             -- 2
   Equal Support -- 0
 B wins.
   Runoff math:
     7  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     7  voters with a preference  (majority = 4)
           B 5 (71%)  ·  C 2 (29%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 B
```

<details>
<summary>Full audit — preference matrix, Condorcet, and score distribution</summary>

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |      A     |   * B     |   * C     |     D     |
-----------------------------------------------------------------
           A > |    ---     |5 - 0 - 2  |3 - 0 - 4  |4 - 0 - 3  |
         * B > | 2 - 0 - 5  |   ---     |5 - 0 - 2  |5 - 0 - 2  |
         * C > | 4 - 0 - 3  |2 - 0 - 5  |   ---     |7 - 0 - 0  |
           D > | 3 - 0 - 4  |2 - 0 - 5  |0 - 0 - 7  |   ---     |

[Condorcet Winner]
  No Condorcet winner (majority cycle: A > B > C > A)

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
A          3  0  0  3  1  0  |    22   3.1
B          2  3  0  0  2  0  |    24   3.4
C          2  2  0  3  0  0  |    24   3.4
D          0  2  0  1  4  0  |    14   2.0
```

</details>

Everything in one file: the [`_tabulated` mirror](../felsenthal_paradoxes_tabulated/bv2160_r6qc8h_star_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/felsenthal_paradoxes/bv2160_r6qc8h_star.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Methods disagree on this election](../../divergence_review/cases/CYCLE_OR_THREE_WAY/bv2160_r6qc8h_star.md) — its entry in the divergence review ledger
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README.md)
- [Ties & tie-breaking (topic hub)](../../../00_start_here/topics/ties/README.md)
- [Runoff reversal (worked set)](../../../01_STAR/runoff_overturns_leader/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [bv2144_mxfmhm_plurality](bv2144_mxfmhm_plurality.md) · [bv2144_mxfmhm_star](bv2144_mxfmhm_star.md) · [bv2145_6fj2kg_irv](bv2145_6fj2kg_irv.md) · [bv2145_6fj2kg_ranked_robin](bv2145_6fj2kg_ranked_robin.md) · [bv2145_6fj2kg_star](bv2145_6fj2kg_star.md) · [bv2146_krk2px_irv](bv2146_krk2px_irv.md) · [bv2146_krk2px_ranked_robin](bv2146_krk2px_ranked_robin.md) · [bv2146_krk2px_star](bv2146_krk2px_star.md) · [bv2147_9gdrqg_irv](bv2147_9gdrqg_irv.md) · [bv2147_9gdrqg_star](bv2147_9gdrqg_star.md) · [bv2148_h87k6v_irv](bv2148_h87k6v_irv.md) · [bv2148_h87k6v_star](bv2148_h87k6v_star.md) · [bv2149_byk9v2_irv](bv2149_byk9v2_irv.md) · [bv2149_byk9v2_star](bv2149_byk9v2_star.md) · [bv2150_dxg8pb_irv](bv2150_dxg8pb_irv.md) · [bv2150_dxg8pb_ranked_robin](bv2150_dxg8pb_ranked_robin.md) · [bv2150_dxg8pb_star](bv2150_dxg8pb_star.md) · [bv2151_97hbpw_irv](bv2151_97hbpw_irv.md) · [bv2151_97hbpw_ranked_robin](bv2151_97hbpw_ranked_robin.md) · [bv2151_97hbpw_star](bv2151_97hbpw_star.md) · [bv2152_r6ctvy_approval](bv2152_r6ctvy_approval.md) · [bv2152_r6ctvy_ranked_robin](bv2152_r6ctvy_ranked_robin.md) · [bv2153_pcttmr_approval](bv2153_pcttmr_approval.md) · [bv2153_pcttmr_irv](bv2153_pcttmr_irv.md) · [bv2153_pcttmr_ranked_robin](bv2153_pcttmr_ranked_robin.md) · [bv2154_wq6yv7_approval](bv2154_wq6yv7_approval.md) · [bv2154_wq6yv7_irv](bv2154_wq6yv7_irv.md) · [bv2154_wq6yv7_ranked_robin](bv2154_wq6yv7_ranked_robin.md) · [bv2160_r6qc8h_plurality](bv2160_r6qc8h_plurality.md) · [bv2161_q3h4fk_plurality](bv2161_q3h4fk_plurality.md) · [bv2161_q3h4fk_star](bv2161_q3h4fk_star.md) · [bv2162_4htk44_irv](bv2162_4htk44_irv.md) · [bv2162_4htk44_ranked_robin](bv2162_4htk44_ranked_robin.md) · [bv2162_4htk44_star](bv2162_4htk44_star.md) · [bv2163_74j6vv_irv](bv2163_74j6vv_irv.md) · [bv2163_74j6vv_ranked_robin](bv2163_74j6vv_ranked_robin.md) · [bv2163_74j6vv_star](bv2163_74j6vv_star.md) · [bv2164_xbqq8t_plurality](bv2164_xbqq8t_plurality.md) · [bv2164_xbqq8t_ranked_robin](bv2164_xbqq8t_ranked_robin.md) · [bv2164_xbqq8t_star](bv2164_xbqq8t_star.md) · [bv2165_9vxcj7_plurality](bv2165_9vxcj7_plurality.md) · [bv2165_9vxcj7_star](bv2165_9vxcj7_star.md) · [bv2166_b7b8dv_plurality](bv2166_b7b8dv_plurality.md) · [bv2166_b7b8dv_star](bv2166_b7b8dv_star.md) · [bv2167_f3dxq9_plurality](bv2167_f3dxq9_plurality.md) · [bv2167_f3dxq9_star](bv2167_f3dxq9_star.md) · [felsenthal_ex6_pareto_approval](felsenthal_ex6_pareto_approval.md) · [felsenthal_ex6_ranked_robin](felsenthal_ex6_ranked_robin.md)
