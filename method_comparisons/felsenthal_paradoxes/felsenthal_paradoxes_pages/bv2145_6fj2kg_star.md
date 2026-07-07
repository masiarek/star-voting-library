# Felsenthal Ex.2 — STAR (ranks→scores): elects the Condorcet winner

*Generated from [`bv2145_6fj2kg_star.yaml`](../bv2145_6fj2kg_star.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Ada

## Scenario

Race 3 of 3 in the Felsenthal runoff-paradoxes election, part 1 of 2 (BV2145, bvid 6fj2kg; BV-confirmed). Source: Dan S. Felsenthal (2010), Appendix A2, Example 2 — see bv2145_6fj2kg_irv.yaml for the full citation and setup.
The same 17 voters with ranks mapped to 0–5 scores (house map, N=3: top=5, mid=3, bottom=1). Scores: Ada 53, Ben 51, Cleo 49 — Ada and Ben advance, and Ada wins the automatic runoff 9–8. STAR elects the Condorcet winner that the runoff procedure (the IRV race) eliminated first.
Live results: https://bettervoting.com/6fj2kg/results

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
1,3,5
1,3,5
```

## What the engine says

Full report from the [`_tabulated` mirror](../felsenthal_paradoxes_tabulated/bv2145_6fj2kg_star_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |   * Ada    |  * Ben    |    Cleo   |
-----------------------------------------------------
       * Ada > |    ---     |9 - 0 - 8  |9 - 0 - 8  |
       * Ben > | 8 - 0 - 9  |   ---     |9 - 0 - 8  |
        Cleo > | 8 - 0 - 9  |8 - 0 - 9  |   ---     |

[Condorcet Winner]
  Condorcet Winner: Ada — matches the STAR winner

[Divergence from STAR]
  STAR                   = Ada
  Choose-One (Plurality) = Ben   (differs from STAR)
  RCV-IRV                = Ben   (differs from STAR)
  Note: no ballots had tied scores, so RCV-IRV vs STAR here is a genuine
        method difference, not a tie-breaking artifact.
  Note: Ranked Robin (RCV-RR) agrees with STAR, so RCV-IRV is the lone
        outlier — the classic center-squeeze signature.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: felsenthal_paradoxes_tabulated/bv2145_6fj2kg_star_RCV-IRV_tabulated.txt

--- STAR Voting Method (single winner) ---
[STAR Voting]
 Tabulating 17 ballots.
Count × Ada,Ben,Cleo
    4 ×   3,  5,   1
    4 ×   3,  1,   5
    3 ×   5,  3,   1
    2 ×   5,  1,   3
    2 ×   1,  5,   3
    2 ×   1,  3,   5

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Ada        5  0  8  0  4  0  |    53   3.1
Ben        6  0  5  0  6  0  |    51   3.0
Cleo       6  0  4  0  7  0  |    49   2.9

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Ada           -- 53 -- First place
   Ben           -- 51 -- Second place
   Cleo          -- 49
 Ada and Ben advance.

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

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/felsenthal_paradoxes/bv2145_6fj2kg_star.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Methods disagree on this election](../../divergence_review/cases/IRV_OUTLIER_RR_WITH_STAR/bv2145_6fj2kg_star.md) — its entry in the divergence review ledger
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README.md)
- [Runoff reversal (worked set)](../../../01_STAR/runoff_overturns_leader/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [bv2144_mxfmhm_plurality](bv2144_mxfmhm_plurality.md) · [bv2144_mxfmhm_star](bv2144_mxfmhm_star.md) · [bv2145_6fj2kg_irv](bv2145_6fj2kg_irv.md) · [bv2145_6fj2kg_ranked_robin](bv2145_6fj2kg_ranked_robin.md) · [bv2146_krk2px_irv](bv2146_krk2px_irv.md) · [bv2146_krk2px_ranked_robin](bv2146_krk2px_ranked_robin.md) · [bv2146_krk2px_star](bv2146_krk2px_star.md) · [bv2147_9gdrqg_irv](bv2147_9gdrqg_irv.md) · [bv2147_9gdrqg_star](bv2147_9gdrqg_star.md) · [bv2148_h87k6v_irv](bv2148_h87k6v_irv.md) · [bv2148_h87k6v_star](bv2148_h87k6v_star.md) · [bv2149_byk9v2_irv](bv2149_byk9v2_irv.md) · [bv2149_byk9v2_star](bv2149_byk9v2_star.md) · [bv2150_dxg8pb_irv](bv2150_dxg8pb_irv.md) · [bv2150_dxg8pb_ranked_robin](bv2150_dxg8pb_ranked_robin.md) · [bv2150_dxg8pb_star](bv2150_dxg8pb_star.md) · [bv2151_97hbpw_irv](bv2151_97hbpw_irv.md) · [bv2151_97hbpw_ranked_robin](bv2151_97hbpw_ranked_robin.md) · [bv2151_97hbpw_star](bv2151_97hbpw_star.md) · [bv2152_r6ctvy_approval](bv2152_r6ctvy_approval.md) · [bv2152_r6ctvy_ranked_robin](bv2152_r6ctvy_ranked_robin.md) · [bv2153_pcttmr_approval](bv2153_pcttmr_approval.md) · [bv2153_pcttmr_irv](bv2153_pcttmr_irv.md) · [bv2153_pcttmr_ranked_robin](bv2153_pcttmr_ranked_robin.md) · [bv2154_wq6yv7_approval](bv2154_wq6yv7_approval.md) · [bv2154_wq6yv7_irv](bv2154_wq6yv7_irv.md) · [bv2154_wq6yv7_ranked_robin](bv2154_wq6yv7_ranked_robin.md) · [felsenthal_ex6_pareto_approval](felsenthal_ex6_pareto_approval.md) · [felsenthal_ex6_ranked_robin](felsenthal_ex6_ranked_robin.md)
