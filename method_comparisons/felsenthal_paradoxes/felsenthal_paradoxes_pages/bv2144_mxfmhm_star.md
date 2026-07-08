# Felsenthal Ex.1 — STAR (ranks→scores): elects the Condorcet winner

*Generated from [`bv2144_mxfmhm_star.yaml`](../bv2144_mxfmhm_star.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Bo

## Scenario

Race 2 of 2 in the Felsenthal plurality-paradoxes election (BV2144, bvid mxfmhm; BV-confirmed). Source: Dan S. Felsenthal, "Review of Paradoxes Afflicting Various Voting Procedures Where One Out of m Candidates (m ≥ 2) Must Be Elected", University of Haifa / LSE, revised 26 May 2010 (Leverhulme Trust "Voting Power in Practice" workshop, Château du Baffy, Normandy); Appendix A1, Example 1.
The same 7 voters, rankings mapped to 0–5 scores with the house map (N=3: top=5, mid=3, bottom=1). Scores: Bo 25, Ana 19, Cal 19 — a scoring-round tie for the second finalist slot, broken head-to-head (Cal beats Ana 4–3, so Cal advances); Bo then wins the automatic runoff 5–2. STAR elects the Condorcet winner Bo, while Choose-One (race 1) elects Ana, the Condorcet-and-absolute loser. The tabulation, not the ballot, decides.
Live results: https://bettervoting.com/mxfmhm/results

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Ana,Bo,Cal
5,3,1
5,3,1
5,3,1
1,5,3
1,5,3
1,3,5
1,3,5
```

## What the engine says

Full report from the [`_tabulated` mirror](../felsenthal_paradoxes_tabulated/bv2144_mxfmhm_star_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |   * Ana    |   * Bo    |    Cal    |
-----------------------------------------------------
       * Ana > |    ---     |3 - 0 - 4  |3 - 0 - 4  |
        * Bo > | 4 - 0 - 3  |   ---     |5 - 0 - 2  |
         Cal > | 4 - 0 - 3  |2 - 0 - 5  |   ---     |

[Condorcet Winner]
  Condorcet Winner: Bo — matches the STAR winner

[Divergence from STAR]
  STAR                   = Bo
  Choose-One (Plurality) = Ana   (differs from STAR)

--- STAR Voting Method (single winner) ---
[STAR Voting]
 Tabulating 7 ballots.
Count × Ana,Bo,Cal
    3 ×   5, 3,  1
    2 ×   1, 5,  3
    2 ×   1, 3,  5

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Ana        3  0  0  0  4  0  |    19   2.7
Bo         2  0  5  0  0  0  |    25   3.6
Cal        2  0  2  0  3  0  |    19   2.7

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Bo            -- 25 -- First place
   Ana           -- 19 -- Tied for second place
   Cal           -- 19 -- Tied for second place
 Bo advances, but there's a two-way tie for second.

[STAR Voting: Scoring Round: First tiebreaker]
 The candidate preferred in the most head-to-head matchups advances.
   Cal           -- 4 -- Second place
   Ana           -- 3
   Equal Support -- 0
 Bo and Cal advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Bo            -- 5 -- First place
   Cal           -- 2
   Equal Support -- 0
 Bo wins.
   Runoff math:
     7  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     7  voters with a preference  (majority = 4)
           Bo 5 (71%)  ·  Cal 2 (29%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Bo
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/felsenthal_paradoxes/bv2144_mxfmhm_star.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README.md)
- [Ties & tie-breaking (topic hub)](../../../00_start_here/topics/ties/README.md)
- [Runoff reversal (worked set)](../../../01_STAR/runoff_overturns_leader/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [bv2144_mxfmhm_plurality](bv2144_mxfmhm_plurality.md) · [bv2145_6fj2kg_irv](bv2145_6fj2kg_irv.md) · [bv2145_6fj2kg_ranked_robin](bv2145_6fj2kg_ranked_robin.md) · [bv2145_6fj2kg_star](bv2145_6fj2kg_star.md) · [bv2146_krk2px_irv](bv2146_krk2px_irv.md) · [bv2146_krk2px_ranked_robin](bv2146_krk2px_ranked_robin.md) · [bv2146_krk2px_star](bv2146_krk2px_star.md) · [bv2147_9gdrqg_irv](bv2147_9gdrqg_irv.md) · [bv2147_9gdrqg_star](bv2147_9gdrqg_star.md) · [bv2148_h87k6v_irv](bv2148_h87k6v_irv.md) · [bv2148_h87k6v_star](bv2148_h87k6v_star.md) · [bv2149_byk9v2_irv](bv2149_byk9v2_irv.md) · [bv2149_byk9v2_star](bv2149_byk9v2_star.md) · [bv2150_dxg8pb_irv](bv2150_dxg8pb_irv.md) · [bv2150_dxg8pb_ranked_robin](bv2150_dxg8pb_ranked_robin.md) · [bv2150_dxg8pb_star](bv2150_dxg8pb_star.md) · [bv2151_97hbpw_irv](bv2151_97hbpw_irv.md) · [bv2151_97hbpw_ranked_robin](bv2151_97hbpw_ranked_robin.md) · [bv2151_97hbpw_star](bv2151_97hbpw_star.md) · [bv2152_r6ctvy_approval](bv2152_r6ctvy_approval.md) · [bv2152_r6ctvy_ranked_robin](bv2152_r6ctvy_ranked_robin.md) · [bv2153_pcttmr_approval](bv2153_pcttmr_approval.md) · [bv2153_pcttmr_irv](bv2153_pcttmr_irv.md) · [bv2153_pcttmr_ranked_robin](bv2153_pcttmr_ranked_robin.md) · [bv2154_wq6yv7_approval](bv2154_wq6yv7_approval.md) · [bv2154_wq6yv7_irv](bv2154_wq6yv7_irv.md) · [bv2154_wq6yv7_ranked_robin](bv2154_wq6yv7_ranked_robin.md) · [bv2160_r6qc8h_plurality](bv2160_r6qc8h_plurality.md) · [bv2160_r6qc8h_star](bv2160_r6qc8h_star.md) · [bv2161_q3h4fk_plurality](bv2161_q3h4fk_plurality.md) · [bv2161_q3h4fk_star](bv2161_q3h4fk_star.md) · [bv2162_4htk44_irv](bv2162_4htk44_irv.md) · [bv2162_4htk44_ranked_robin](bv2162_4htk44_ranked_robin.md) · [bv2162_4htk44_star](bv2162_4htk44_star.md) · [bv2163_74j6vv_irv](bv2163_74j6vv_irv.md) · [bv2163_74j6vv_ranked_robin](bv2163_74j6vv_ranked_robin.md) · [bv2163_74j6vv_star](bv2163_74j6vv_star.md) · [felsenthal_ex6_pareto_approval](felsenthal_ex6_pareto_approval.md) · [felsenthal_ex6_ranked_robin](felsenthal_ex6_ranked_robin.md)
