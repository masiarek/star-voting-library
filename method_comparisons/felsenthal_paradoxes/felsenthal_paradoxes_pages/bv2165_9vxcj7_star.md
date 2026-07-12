# Coombs Ex.19 full — STAR: Boone wins the runoff 8–7

*Generated from [`bv2165_9vxcj7_star.yaml`](../bv2165_9vxcj7_star.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Boone

## Scenario

Race 1 of 2 in the Coombs No-Show pair, part 1 of 2 (BV2165, bvid 9vxcj7; BV-confirmed; the pair is BV2165/66). Source: Dan S. Felsenthal, "Review of Paradoxes Afflicting Various Voting Procedures Where One Out of m Candidates (m ≥ 2) Must Be Elected", University of Haifa / LSE, revised 26 May 2010; Appendix A7 (Coombs' procedure), Example 19.
The full electorate: 15 voters — 4×(Amy>Boone>Cass), 4×(Boone>Cass>Amy), 5×(Cass>Amy>Boone), 2×(Cass>Boone>Amy). Coombs (worked on the case page; no tabulator on BV or in LH): Amy is ranked last by the most voters (6) and is deleted; Boone then holds a majority — Boone wins. This STAR race (5/3/1 map): Amy 41, Boone 43, Cass 51 — Cass tops the scores, but Boone wins the automatic runoff 8–7. Part 2 (BV2166): the two Cass>Boone>Amy voters stay home, and BOTH Coombs and STAR flip to Cass, their favorite. Pairwise is a cycle (Amy>Boone 9–6, Boone>Cass 8–7, Cass>Amy 11–4) — no RR race; IRV's first elimination is a random Amy/Boone tie — no IRV race.
Live results: https://bettervoting.com/9vxcj7/results

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
1,3,5
1,3,5
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR                   = Boone
  Choose-One (Plurality) = Cass   (differs from STAR)
  Approval               = Cass   (differs from STAR)
  RCV-RR                 = Cass   (differs from STAR)
  Full round-by-round reports (generated for review):
  RCV-RR round-robin: felsenthal_paradoxes_tabulated/bv2165_9vxcj7_star_RCV-RR_tabulated.txt

[Runoff Reversal]
 - Score Round Winner(s) = (Cass)
 - Runoff Round Winner   = (Boone)
  Candidate Cass earned the highest total score, but
  Candidate Boone won the automatic runoff — not a malfunction,
  STAR working as designed: the runoff elects the finalist preferred
  by the majority (of voters with a preference).

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 15 ballots.
Count × Amy,Boone,Cass
    5 ×   3,    1,   5
    4 ×   5,    3,   1
    4 ×   1,    5,   3
    2 ×   1,    3,   5

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Cass          -- 51 -- First place
   Boone         -- 43 -- Second place
   Amy           -- 41
 Cass and Boone advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Boone         -- 8 -- First place
   Cass          -- 7
   Equal Support -- 0
 Boone wins.
   Runoff math:
     15  ballots cast
   −  0  Equal Support (no preference between the two finalists)
     ──
     15  voters with a preference  (majority = 8)
           Boone 8 (53%)  ·  Cass 7 (47%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Boone
```

<details>
<summary>Full audit — preference matrix, Condorcet, and score distribution</summary>

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |      Amy     |  * Boone    |   * Cass    |
-------------------------------------------------------------
           Amy > |     ---      | 9 -  0 -  6 | 4 -  0 - 11 |
       * Boone > |  6 -  0 -  9 |    ---      | 8 -  0 -  7 |
        * Cass > | 11 -  0 -  4 | 7 -  0 -  8 |    ---      |

[Condorcet Winner]
  No Condorcet winner (majority cycle: Amy > Boone > Cass > Amy)

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Amy        4  0  5  0  6  0  |    41   2.7
Boone      4  0  6  0  5  0  |    43   2.9
Cass       7  0  4  0  4  0  |    51   3.4
```

</details>

Everything in one file: the [`_tabulated` mirror](../felsenthal_paradoxes_tabulated/bv2165_9vxcj7_star_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/felsenthal_paradoxes/bv2165_9vxcj7_star.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Methods disagree on this election](../../divergence_review/cases/CYCLE_OR_THREE_WAY/bv2165_9vxcj7_star.md) — its entry in the divergence review ledger
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README.md)
- [Ties & tie-breaking (topic hub)](../../../00_start_here/topics/ties/README.md)
- [Runoff reversal (worked set)](../../../01_STAR/runoff_overturns_leader/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [bv2144_mxfmhm_plurality](bv2144_mxfmhm_plurality.md) · [bv2144_mxfmhm_star](bv2144_mxfmhm_star.md) · [bv2145_6fj2kg_irv](bv2145_6fj2kg_irv.md) · [bv2145_6fj2kg_ranked_robin](bv2145_6fj2kg_ranked_robin.md) · [bv2145_6fj2kg_star](bv2145_6fj2kg_star.md) · [bv2146_krk2px_irv](bv2146_krk2px_irv.md) · [bv2146_krk2px_ranked_robin](bv2146_krk2px_ranked_robin.md) · [bv2146_krk2px_star](bv2146_krk2px_star.md) · [bv2147_9gdrqg_irv](bv2147_9gdrqg_irv.md) · [bv2147_9gdrqg_star](bv2147_9gdrqg_star.md) · [bv2148_h87k6v_irv](bv2148_h87k6v_irv.md) · [bv2148_h87k6v_star](bv2148_h87k6v_star.md) · [bv2149_byk9v2_irv](bv2149_byk9v2_irv.md) · [bv2149_byk9v2_star](bv2149_byk9v2_star.md) · [bv2150_dxg8pb_irv](bv2150_dxg8pb_irv.md) · [bv2150_dxg8pb_ranked_robin](bv2150_dxg8pb_ranked_robin.md) · [bv2150_dxg8pb_star](bv2150_dxg8pb_star.md) · [bv2151_97hbpw_irv](bv2151_97hbpw_irv.md) · [bv2151_97hbpw_ranked_robin](bv2151_97hbpw_ranked_robin.md) · [bv2151_97hbpw_star](bv2151_97hbpw_star.md) · [bv2152_r6ctvy_approval](bv2152_r6ctvy_approval.md) · [bv2152_r6ctvy_ranked_robin](bv2152_r6ctvy_ranked_robin.md) · [bv2153_pcttmr_approval](bv2153_pcttmr_approval.md) · [bv2153_pcttmr_irv](bv2153_pcttmr_irv.md) · [bv2153_pcttmr_ranked_robin](bv2153_pcttmr_ranked_robin.md) · [bv2154_wq6yv7_approval](bv2154_wq6yv7_approval.md) · [bv2154_wq6yv7_irv](bv2154_wq6yv7_irv.md) · [bv2154_wq6yv7_ranked_robin](bv2154_wq6yv7_ranked_robin.md) · [bv2160_r6qc8h_plurality](bv2160_r6qc8h_plurality.md) · [bv2160_r6qc8h_star](bv2160_r6qc8h_star.md) · [bv2161_q3h4fk_plurality](bv2161_q3h4fk_plurality.md) · [bv2161_q3h4fk_star](bv2161_q3h4fk_star.md) · [bv2162_4htk44_irv](bv2162_4htk44_irv.md) · [bv2162_4htk44_ranked_robin](bv2162_4htk44_ranked_robin.md) · [bv2162_4htk44_star](bv2162_4htk44_star.md) · [bv2163_74j6vv_irv](bv2163_74j6vv_irv.md) · [bv2163_74j6vv_ranked_robin](bv2163_74j6vv_ranked_robin.md) · [bv2163_74j6vv_star](bv2163_74j6vv_star.md) · [bv2164_xbqq8t_plurality](bv2164_xbqq8t_plurality.md) · [bv2164_xbqq8t_ranked_robin](bv2164_xbqq8t_ranked_robin.md) · [bv2164_xbqq8t_star](bv2164_xbqq8t_star.md) · [bv2165_9vxcj7_plurality](bv2165_9vxcj7_plurality.md) · [bv2166_b7b8dv_plurality](bv2166_b7b8dv_plurality.md) · [bv2166_b7b8dv_star](bv2166_b7b8dv_star.md) · [bv2167_f3dxq9_plurality](bv2167_f3dxq9_plurality.md) · [bv2167_f3dxq9_star](bv2167_f3dxq9_star.md) · [felsenthal_ex6_pareto_approval](felsenthal_ex6_pareto_approval.md) · [felsenthal_ex6_ranked_robin](felsenthal_ex6_ranked_robin.md)
