# Coombs Ex.17 — STAR: Bree tops the scores, the Condorcet winner Arlo wins the runoff

*Generated from [`bv2164_xbqq8t_star.yaml`](../bv2164_xbqq8t_star.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Arlo

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/xbqq8t) · **[results ↗](https://bettervoting.com/xbqq8t/results)** (election `xbqq8t`).

## Scenario

Race 1 of 3 in the Coombs Condorcet-failure election (BV2164, bvid xbqq8t; BV-confirmed). Source: Dan S. Felsenthal, "Review of Paradoxes Afflicting Various Voting Procedures Where One Out of m Candidates (m ≥ 2) Must Be Elected", University of Haifa / LSE, revised 26 May 2010; Appendix A7 (Coombs' procedure: eliminate whoever is ranked LAST by the most voters), Example 17.
33 voters, four candidates: 11×(Arlo>Bree>Cole>Dana), 12×(Bree>Cole>Dana>Arlo), 2×(Bree>Arlo>Dana>Cole), 4×(Cole>Arlo>Dana>Bree), 4×(Dana>Arlo>Bree>Cole). Arlo is the Condorcet winner (beats Bree 19–14, Cole 17–16, Dana 17–16). Coombs — worked on the case page; no tabulator on BetterVoting or in the LH engine — deletes ARLO first (ranked last by 12, the most) and elects Bree. This STAR race (ranks mapped 5/4/2/1): Arlo 107, Bree 126, Cole 96, Dana 67 — Bree tops the scoring round, but Arlo wins the automatic runoff 19–14. No IRV race: its first elimination is a random Cole/Dana 4–4 tie on BV.
Live results: https://bettervoting.com/xbqq8t/results

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Arlo,Bree,Cole,Dana
11: 5,4,2,1
12: 1,5,4,2
# 2× Bree>Arlo>Dana>Cole and 4× Cole>Arlo>Dana>Bree and 4× Dana>Arlo>Bree>Cole:
4,5,1,2
4,5,1,2
4,1,5,2
4,1,5,2
4,1,5,2
4,1,5,2
4,2,1,5
4,2,1,5
4,2,1,5
4,2,1,5
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR                   = Arlo
  Choose-One (Plurality) = Bree   (differs from STAR)
  Approval               = Bree   (differs from STAR)

[Runoff Reversal]
 - Score Round Winner(s) = (Bree)
 - Runoff Round Winner   = (Arlo)
  Candidate Bree earned the highest total score, but
  Candidate Arlo won the automatic runoff — not a malfunction,
  STAR working as designed: the runoff elects the finalist preferred
  by the majority (of voters with a preference).

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 33 ballots.
Count × Arlo,Bree,Cole,Dana
   12 ×    1,   5,   4,   2
   11 ×    5,   4,   2,   1
    4 ×    4,   1,   5,   2
    4 ×    4,   2,   1,   5
    2 ×    4,   5,   1,   2

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Bree          -- 126 -- First place
   Arlo          -- 107 -- Second place
   Cole          --  96
   Dana          --  67
 Bree and Arlo advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Arlo          -- 19 -- First place
   Bree          -- 14
   Equal Support --  0
 Arlo wins.
   Runoff math:
     33  ballots cast
   −  0  Equal Support (no preference between the two finalists)
     ──
     33  voters with a preference  (majority = 17)
           Arlo 19 (58%)  ·  Bree 14 (42%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Arlo
```

<details>
<summary>Full audit — preference matrix, Condorcet, and score distribution</summary>

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |    * Arlo    |   * Bree    |     Cole    |     Dana    |
---------------------------------------------------------------------------
        * Arlo > |     ---      |19 -  0 - 14 |17 -  0 - 16 |17 -  0 - 16 |
        * Bree > | 14 -  0 - 19 |    ---      |29 -  0 -  4 |25 -  0 -  8 |
          Cole > | 16 -  0 - 17 | 4 -  0 - 29 |    ---      |27 -  0 -  6 |
          Dana > | 16 -  0 - 17 | 8 -  0 - 25 | 6 -  0 - 27 |    ---      |

[Condorcet Winner]
  Condorcet Winner: Arlo — matches the STAR winner

[Score Distribution] (how many ballots gave each star rating)
                   Score
Candidate   5   4   3   2   1   0  | Total   Avg
Arlo       11  10   0   0  12   0  |   107   3.2
Bree       14  11   0   4   4   0  |   126   3.8
Cole        4  12   0  11   6   0  |    96   2.9
Dana        4   0   0  18  11   0  |    67   2.0
```

</details>

Everything in one file: the [`_tabulated` mirror](../felsenthal_paradoxes_tabulated/bv2164_xbqq8t_star_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/felsenthal_paradoxes/bv2164_xbqq8t_star.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Methods disagree on this election](../../divergence_review/cases/APPROVAL_OR_MINOR/bv2164_xbqq8t_star.md) — its entry in the divergence review ledger
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README.md)
- [Ties & tie-breaking (topic hub)](../../../00_start_here/topics/ties/README.md)
- [Runoff reversal (worked set)](../../../01_STAR/runoff_overturns_leader/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [bv2144_mxfmhm_plurality](bv2144_mxfmhm_plurality.md) · [bv2144_mxfmhm_star](bv2144_mxfmhm_star.md) · [bv2145_6fj2kg_irv](bv2145_6fj2kg_irv.md) · [bv2145_6fj2kg_ranked_robin](bv2145_6fj2kg_ranked_robin.md) · [bv2145_6fj2kg_star](bv2145_6fj2kg_star.md) · [bv2146_krk2px_irv](bv2146_krk2px_irv.md) · [bv2146_krk2px_ranked_robin](bv2146_krk2px_ranked_robin.md) · [bv2146_krk2px_star](bv2146_krk2px_star.md) · [bv2147_9gdrqg_irv](bv2147_9gdrqg_irv.md) · [bv2147_9gdrqg_star](bv2147_9gdrqg_star.md) · [bv2148_h87k6v_irv](bv2148_h87k6v_irv.md) · [bv2148_h87k6v_star](bv2148_h87k6v_star.md) · [bv2149_byk9v2_irv](bv2149_byk9v2_irv.md) · [bv2149_byk9v2_star](bv2149_byk9v2_star.md) · [bv2150_dxg8pb_irv](bv2150_dxg8pb_irv.md) · [bv2150_dxg8pb_ranked_robin](bv2150_dxg8pb_ranked_robin.md) · [bv2150_dxg8pb_star](bv2150_dxg8pb_star.md) · [bv2151_97hbpw_irv](bv2151_97hbpw_irv.md) · [bv2151_97hbpw_ranked_robin](bv2151_97hbpw_ranked_robin.md) · [bv2151_97hbpw_star](bv2151_97hbpw_star.md) · [bv2152_r6ctvy_approval](bv2152_r6ctvy_approval.md) · [bv2152_r6ctvy_ranked_robin](bv2152_r6ctvy_ranked_robin.md) · [bv2153_pcttmr_approval](bv2153_pcttmr_approval.md) · [bv2153_pcttmr_irv](bv2153_pcttmr_irv.md) · [bv2153_pcttmr_ranked_robin](bv2153_pcttmr_ranked_robin.md) · [bv2154_wq6yv7_approval](bv2154_wq6yv7_approval.md) · [bv2154_wq6yv7_irv](bv2154_wq6yv7_irv.md) · [bv2154_wq6yv7_ranked_robin](bv2154_wq6yv7_ranked_robin.md) · [bv2160_r6qc8h_plurality](bv2160_r6qc8h_plurality.md) · [bv2160_r6qc8h_star](bv2160_r6qc8h_star.md) · [bv2161_q3h4fk_plurality](bv2161_q3h4fk_plurality.md) · [bv2161_q3h4fk_star](bv2161_q3h4fk_star.md) · [bv2162_4htk44_irv](bv2162_4htk44_irv.md) · [bv2162_4htk44_ranked_robin](bv2162_4htk44_ranked_robin.md) · [bv2162_4htk44_star](bv2162_4htk44_star.md) · [bv2163_74j6vv_irv](bv2163_74j6vv_irv.md) · [bv2163_74j6vv_ranked_robin](bv2163_74j6vv_ranked_robin.md) · [bv2163_74j6vv_star](bv2163_74j6vv_star.md) · [bv2164_xbqq8t_plurality](bv2164_xbqq8t_plurality.md) · [bv2164_xbqq8t_ranked_robin](bv2164_xbqq8t_ranked_robin.md) · [bv2165_9vxcj7_plurality](bv2165_9vxcj7_plurality.md) · [bv2165_9vxcj7_star](bv2165_9vxcj7_star.md) · [bv2166_b7b8dv_plurality](bv2166_b7b8dv_plurality.md) · [bv2166_b7b8dv_star](bv2166_b7b8dv_star.md) · [bv2167_f3dxq9_plurality](bv2167_f3dxq9_plurality.md) · [bv2167_f3dxq9_star](bv2167_f3dxq9_star.md) · [felsenthal_ex6_pareto_approval](felsenthal_ex6_pareto_approval.md) · [felsenthal_ex6_ranked_robin](felsenthal_ex6_ranked_robin.md)
