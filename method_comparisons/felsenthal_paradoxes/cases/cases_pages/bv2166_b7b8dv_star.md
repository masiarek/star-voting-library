# Coombs Ex.19 no-show — STAR: the two abstainers get their favorite (STAR flips too)

*Generated from [`bv2166_b7b8dv_star.yaml`](../bv2166_b7b8dv_star.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Cass

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/b7b8dv) · **[results ↗](https://bettervoting.com/b7b8dv/results)** (election `b7b8dv`).

## Scenario

Race 1 of 2 in the Coombs No-Show pair, part 2 of 2 (BV2166, bvid b7b8dv; BV-confirmed; the pair is BV2165/66). Source: Dan S. Felsenthal, "Review of Paradoxes Afflicting Various Voting Procedures Where One Out of m Candidates (m ≥ 2) Must Be Elected", University of Haifa / LSE, revised 26 May 2010; Appendix A7 (Coombs' procedure), Example 19 (continued).
Ceteris paribus, the two Cass>Boone>Amy voters do NOT participate: 13 voters — 4×(Amy>Boone>Cass), 4×(Boone>Cass>Amy), 5×(Cass>Amy>Boone). Coombs (on the case page): now BOONE is ranked last by the most voters (5) and is deleted; Cass — the abstainers' TOP preference — wins: Felsenthal's No-Show paradox (same flip via truncation). HONEST BONUS, live: STAR flips here too. With all 15 ballots STAR elects Boone (BV2165: 41/43/51, runoff 8–7); on these 13 it scores Amy 39, Boone 37, Cass 41 and CASS beats Amy 9–4 in the runoff. The absent pair's sincere ballots (scoring Boone 3) had helped Boone reach and win the runoff — staying home gets them their favorite: a genuine STAR participation failure on this profile. The mechanism is STAR's runoff stage (which costs it Moulin-style participation guarantees); score-only methods cannot do this. First live score-family entry in the no-show group — the honest-limits pledge in action.
Live results: https://bettervoting.com/b7b8dv/results

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Amy,Boone,Cass
5,3,1
5,3,1
5,3,1
5,3,1
1,5,3
1,5,3
1,5,3
1,5,3
3,1,5
3,1,5
3,1,5
3,1,5
3,1,5
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR     = Cass
  Approval = Amy   (differs from STAR)

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 13 ballots.
Count × Amy,Boone,Cass
    5 ×   3,    1,   5
    4 ×   5,    3,   1
    4 ×   1,    5,   3

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Cass          -- 41 -- First place
   Amy           -- 39 -- Second place
   Boone         -- 37
 Cass and Amy advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Cass          -- 9 -- First place
   Amy           -- 4
   Equal Support -- 0
 Cass wins.
   Runoff math:
     13  ballots cast
   −  0  Equal Support (no preference between the two finalists)
     ──
     13  voters with a preference  (majority = 7)
           Cass 9 (69%)  ·  Amy 4 (31%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Cass
```

<details>
<summary>Full audit — preference matrix, Condorcet, and score distribution</summary>

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |   * Amy    |   Boone   |  * Cass   |
-----------------------------------------------------
       * Amy > |    ---     |9 - 0 - 4  |4 - 0 - 9  |
       Boone > | 4 - 0 - 9  |   ---     |8 - 0 - 5  |
      * Cass > | 9 - 0 - 4  |5 - 0 - 8  |   ---     |

[Condorcet Winner]
  No Condorcet winner (majority cycle: Amy > Boone > Cass > Amy)

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Amy        4  0  5  0  4  0  |    39   3.0
Boone      4  0  4  0  5  0  |    37   2.8
Cass       5  0  4  0  4  0  |    41   3.2
```

</details>

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/bv2166_b7b8dv_star_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/felsenthal_paradoxes/cases/bv2166_b7b8dv_star.yaml
```

## See also

- [Methods disagree on this election](../../../divergence_review/cases/APPROVAL_OR_MINOR/bv2166_b7b8dv_star.md) — its entry in the divergence review ledger
- [Runoff reversal (worked set)](../../../../01_STAR/runoff_overturns_leader/README.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [bv2144_mxfmhm_plurality](bv2144_mxfmhm_plurality.md) · [bv2144_mxfmhm_star](bv2144_mxfmhm_star.md) · [bv2145_6fj2kg_irv](bv2145_6fj2kg_irv.md) · [bv2145_6fj2kg_ranked_robin](bv2145_6fj2kg_ranked_robin.md) · [bv2145_6fj2kg_star](bv2145_6fj2kg_star.md) · [bv2146_krk2px_irv](bv2146_krk2px_irv.md) · [bv2146_krk2px_ranked_robin](bv2146_krk2px_ranked_robin.md) · [bv2146_krk2px_star](bv2146_krk2px_star.md) · [bv2147_9gdrqg_irv](bv2147_9gdrqg_irv.md) · [bv2147_9gdrqg_star](bv2147_9gdrqg_star.md) · [bv2148_h87k6v_irv](bv2148_h87k6v_irv.md) · [bv2148_h87k6v_star](bv2148_h87k6v_star.md) · [bv2149_byk9v2_irv](bv2149_byk9v2_irv.md) · [bv2149_byk9v2_star](bv2149_byk9v2_star.md) · [bv2150_dxg8pb_irv](bv2150_dxg8pb_irv.md) · [bv2150_dxg8pb_ranked_robin](bv2150_dxg8pb_ranked_robin.md) · [bv2150_dxg8pb_star](bv2150_dxg8pb_star.md) · [bv2151_97hbpw_irv](bv2151_97hbpw_irv.md) · [bv2151_97hbpw_ranked_robin](bv2151_97hbpw_ranked_robin.md) · [bv2151_97hbpw_star](bv2151_97hbpw_star.md) · [bv2152_r6ctvy_approval](bv2152_r6ctvy_approval.md) · [bv2152_r6ctvy_ranked_robin](bv2152_r6ctvy_ranked_robin.md) · [bv2153_pcttmr_approval](bv2153_pcttmr_approval.md) · [bv2153_pcttmr_irv](bv2153_pcttmr_irv.md) · [bv2153_pcttmr_ranked_robin](bv2153_pcttmr_ranked_robin.md) · [bv2154_wq6yv7_approval](bv2154_wq6yv7_approval.md) · [bv2154_wq6yv7_irv](bv2154_wq6yv7_irv.md) · [bv2154_wq6yv7_ranked_robin](bv2154_wq6yv7_ranked_robin.md) · [bv2160_r6qc8h_plurality](bv2160_r6qc8h_plurality.md) · [bv2160_r6qc8h_star](bv2160_r6qc8h_star.md) · [bv2161_q3h4fk_plurality](bv2161_q3h4fk_plurality.md) · [bv2161_q3h4fk_star](bv2161_q3h4fk_star.md) · [bv2162_4htk44_irv](bv2162_4htk44_irv.md) · [bv2162_4htk44_ranked_robin](bv2162_4htk44_ranked_robin.md) · [bv2162_4htk44_star](bv2162_4htk44_star.md) · [bv2163_74j6vv_irv](bv2163_74j6vv_irv.md) · [bv2163_74j6vv_ranked_robin](bv2163_74j6vv_ranked_robin.md) · [bv2163_74j6vv_star](bv2163_74j6vv_star.md) · [bv2164_xbqq8t_plurality](bv2164_xbqq8t_plurality.md) · [bv2164_xbqq8t_ranked_robin](bv2164_xbqq8t_ranked_robin.md) · [bv2164_xbqq8t_star](bv2164_xbqq8t_star.md) · [bv2165_9vxcj7_plurality](bv2165_9vxcj7_plurality.md) · [bv2165_9vxcj7_star](bv2165_9vxcj7_star.md) · [bv2166_b7b8dv_plurality](bv2166_b7b8dv_plurality.md) · [bv2167_f3dxq9_plurality](bv2167_f3dxq9_plurality.md) · [bv2167_f3dxq9_star](bv2167_f3dxq9_star.md) · [felsenthal_ex6_pareto_approval](felsenthal_ex6_pareto_approval.md) · [felsenthal_ex6_ranked_robin](felsenthal_ex6_ranked_robin.md)
