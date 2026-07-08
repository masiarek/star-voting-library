# Nurmi Ex.16 sincere — STAR: elects the Condorcet winner B

*Generated from [`bv2162_4htk44_star.yaml`](../bv2162_4htk44_star.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** B

## Scenario

Race 1 of 3 in the RCV-IRV truncation pair, part 1 of 2 (BV2162, bvid 4htk44; BV-confirmed; the pair is BV2162/63). Source: Dan S. Felsenthal, "Review of Paradoxes Afflicting Various Voting Procedures Where One Out of m Candidates (m ≥ 2) Must Be Elected", University of Haifa / LSE, revised 26 May 2010; Appendix A6 (instant-runoff — Felsenthal's "Alternative Vote" is the British name for RCV-IRV), Example 16, due to Nurmi (1999: 63).
103 voters, four candidates, everyone ranking all four: 33×(A>B>C>D), 29×(B>A>C>D), 24×(C>B>A>D), 17×(D>C>B>A). B is the Condorcet winner (beats A 70–33, C 62–41, D 86–17). This STAR race (ranks mapped 5/4/2/1) scores A 346, B 407, C 312, D 171 — B wins the automatic runoff 70–33. The IRV race elects A instead (a Condorcet winner failure); part 2 (BV2163) shows 17 voters improving their result by TRUNCATING.
Live results: https://bettervoting.com/4htk44/results

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
A,B,C,D
33: 5,4,2,1
29: 4,5,2,1
24: 2,4,5,1
17: 1,2,4,5
```

## What the engine says

Full report from the [`_tabulated` mirror](../felsenthal_paradoxes_tabulated/bv2162_4htk44_star_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |     * A      |    * B      |      C      |      D      |
---------------------------------------------------------------------------
           * A > |     ---      |33 -  0 - 70 |62 -  0 - 41 |86 -  0 - 17 |
           * B > | 70 -  0 - 33 |    ---      |62 -  0 - 41 |86 -  0 - 17 |
             C > | 41 -  0 - 62 |41 -  0 - 62 |    ---      |86 -  0 - 17 |
             D > | 17 -  0 - 86 |17 -  0 - 86 |17 -  0 - 86 |    ---      |

[Condorcet Winner]
  Condorcet Winner: B — matches the STAR winner

[Divergence from STAR]
  STAR                   = B
  Choose-One (Plurality) = A   (differs from STAR)
  RCV-IRV                = A   (differs from STAR)
  Note: no ballots had tied scores, so RCV-IRV vs STAR here is a genuine
        method difference, not a tie-breaking artifact.
  Note: Ranked Robin (RCV-RR) agrees with STAR, so RCV-IRV is the lone
        outlier — the classic center-squeeze signature.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: felsenthal_paradoxes_tabulated/bv2162_4htk44_star_RCV-IRV_tabulated.txt

--- STAR Voting Method (single winner) ---
[STAR Voting]
 Tabulating 103 ballots.
Count × A,B,C,D
   33 × 5,4,2,1
   29 × 4,5,2,1
   24 × 2,4,5,1
   17 × 1,2,4,5

[Score Distribution] (how many ballots gave each star rating)
                   Score
Candidate   5   4   3   2   1   0  | Total   Avg
A          33  29   0  24  17   0  |   346   3.4
B          29  57   0  17   0   0  |   407   4.0
C          24  17   0  62   0   0  |   312   3.0
D          17   0   0   0  86   0  |   171   1.7

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   B             -- 407 -- First place
   A             -- 346 -- Second place
   C             -- 312
   D             -- 171
 B and A advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   B             -- 70 -- First place
   A             -- 33
   Equal Support --  0
 B wins.
   Runoff math:
     103  ballots cast
   −   0  Equal Support (no preference between the two finalists)
     ───
     103  voters with a preference  (majority = 52)
           B 70 (68%)  ·  A 33 (32%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 B
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/felsenthal_paradoxes/bv2162_4htk44_star.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README.md)
- [Runoff reversal (worked set)](../../../01_STAR/runoff_overturns_leader/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [bv2144_mxfmhm_plurality](bv2144_mxfmhm_plurality.md) · [bv2144_mxfmhm_star](bv2144_mxfmhm_star.md) · [bv2145_6fj2kg_irv](bv2145_6fj2kg_irv.md) · [bv2145_6fj2kg_ranked_robin](bv2145_6fj2kg_ranked_robin.md) · [bv2145_6fj2kg_star](bv2145_6fj2kg_star.md) · [bv2146_krk2px_irv](bv2146_krk2px_irv.md) · [bv2146_krk2px_ranked_robin](bv2146_krk2px_ranked_robin.md) · [bv2146_krk2px_star](bv2146_krk2px_star.md) · [bv2147_9gdrqg_irv](bv2147_9gdrqg_irv.md) · [bv2147_9gdrqg_star](bv2147_9gdrqg_star.md) · [bv2148_h87k6v_irv](bv2148_h87k6v_irv.md) · [bv2148_h87k6v_star](bv2148_h87k6v_star.md) · [bv2149_byk9v2_irv](bv2149_byk9v2_irv.md) · [bv2149_byk9v2_star](bv2149_byk9v2_star.md) · [bv2150_dxg8pb_irv](bv2150_dxg8pb_irv.md) · [bv2150_dxg8pb_ranked_robin](bv2150_dxg8pb_ranked_robin.md) · [bv2150_dxg8pb_star](bv2150_dxg8pb_star.md) · [bv2151_97hbpw_irv](bv2151_97hbpw_irv.md) · [bv2151_97hbpw_ranked_robin](bv2151_97hbpw_ranked_robin.md) · [bv2151_97hbpw_star](bv2151_97hbpw_star.md) · [bv2152_r6ctvy_approval](bv2152_r6ctvy_approval.md) · [bv2152_r6ctvy_ranked_robin](bv2152_r6ctvy_ranked_robin.md) · [bv2153_pcttmr_approval](bv2153_pcttmr_approval.md) · [bv2153_pcttmr_irv](bv2153_pcttmr_irv.md) · [bv2153_pcttmr_ranked_robin](bv2153_pcttmr_ranked_robin.md) · [bv2154_wq6yv7_approval](bv2154_wq6yv7_approval.md) · [bv2154_wq6yv7_irv](bv2154_wq6yv7_irv.md) · [bv2154_wq6yv7_ranked_robin](bv2154_wq6yv7_ranked_robin.md) · [bv2160_r6qc8h_plurality](bv2160_r6qc8h_plurality.md) · [bv2160_r6qc8h_star](bv2160_r6qc8h_star.md) · [bv2161_q3h4fk_plurality](bv2161_q3h4fk_plurality.md) · [bv2161_q3h4fk_star](bv2161_q3h4fk_star.md) · [bv2162_4htk44_irv](bv2162_4htk44_irv.md) · [bv2162_4htk44_ranked_robin](bv2162_4htk44_ranked_robin.md) · [bv2163_74j6vv_irv](bv2163_74j6vv_irv.md) · [bv2163_74j6vv_ranked_robin](bv2163_74j6vv_ranked_robin.md) · [bv2163_74j6vv_star](bv2163_74j6vv_star.md) · [felsenthal_ex6_pareto_approval](felsenthal_ex6_pareto_approval.md) · [felsenthal_ex6_ranked_robin](felsenthal_ex6_ranked_robin.md)
