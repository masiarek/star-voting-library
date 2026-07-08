# Coombs Ex.17 — Ranked Robin: the Condorcet winner Arlo

*Generated from [`bv2164_xbqq8t_ranked_robin.yaml`](../bv2164_xbqq8t_ranked_robin.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../00_start_here/RCV_Ranked_Robin) · **1 seat** · **Expected winner:** Arlo

## Scenario

Race 3 of 3 in the Coombs Condorcet-failure election (BV2164, bvid xbqq8t; BV-confirmed). Source: Dan S. Felsenthal (2010), Appendix A7, Example 17 — see bv2164_xbqq8t_star.yaml for the setup.
The same 33 rankings counted by Ranked Robin (Copeland): Arlo wins every head-to-head (Bree 19–14, Cole 17–16, Dana 17–16) — the Condorcet winner, elected directly. The irony this case teaches: Coombs deletes candidates for being ranked LAST by many, and Arlo — everyone's pairwise favorite — is also the most-frequent last choice (12 ballots), so Coombs deletes the Condorcet winner FIRST. Felsenthal conjectures four candidates are the minimum for this failure.
Live results: https://bettervoting.com/xbqq8t/results

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
11:Arlo>Bree>Cole>Dana
12:Bree>Cole>Dana>Arlo
2:Bree>Arlo>Dana>Cole
4:Cole>Arlo>Dana>Bree
4:Dana>Arlo>Bree>Cole
```

## What the engine says

Full report from the [`_tabulated` mirror](../felsenthal_paradoxes_tabulated/bv2164_xbqq8t_ranked_robin_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Ranked Robin (RCV-RR / Copeland) Method (single winner) ---
 Tabulating 33 ballots (ranked ballots).

Ballots:
    11 × Arlo > Bree > Cole > Dana
    12 × Bree > Cole > Dana > Arlo
     2 × Bree > Arlo > Dana > Cole
     4 × Cole > Arlo > Dana > Bree
     4 × Dana > Arlo > Bree > Cole

Round-Robin — every pair, head-to-head (For – Against):
   Arlo  beats Bree   19 – 14
   Arlo  beats Cole   17 – 16
   Arlo  beats Dana   17 – 16
   Bree  beats Cole   29 –  4
   Bree  beats Dana   25 –  8
   Cole  beats Dana   27 –  6

--- Pairwise (Round-Robin) Matrix ---
Head-to-head / pairwise comparison — the Ranked Robin tally
Legend: For - Equal Support - Against   (row vs column)
         |     Arlo     |    Bree     |    Cole     |    Dana     |
-------------------------------------------------------------------
  Arlo > |     ---      |19 -  0 - 14 |17 -  0 - 16 |17 -  0 - 16 |
  Bree > | 14 -  0 - 19 |    ---      |29 -  0 -  4 |25 -  0 -  8 |
  Cole > | 16 -  0 - 17 | 4 -  0 - 29 |    ---      |27 -  0 -  6 |
  Dana > | 16 -  0 - 17 | 8 -  0 - 25 | 6 -  0 - 27 |    ---      |

Win–loss record — Copeland score = wins + ½·ties (most wins wins; ties broken by total margin, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  Arlo       3–0–0         3      +7  Bree, Cole, Dana
    2  Bree       2–1–0         2     +37  Cole, Dana
    3  Cole       1–2–0         1      -5  Dana
    4  Dana       0–3–0         0     -39  —

Winner — Ranked Robin (RCV-RR): Arlo
   beats every opponent head-to-head — the Condorcet winner.
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/felsenthal_paradoxes/bv2164_xbqq8t_ranked_robin.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [bv2144_mxfmhm_plurality](bv2144_mxfmhm_plurality.md) · [bv2144_mxfmhm_star](bv2144_mxfmhm_star.md) · [bv2145_6fj2kg_irv](bv2145_6fj2kg_irv.md) · [bv2145_6fj2kg_ranked_robin](bv2145_6fj2kg_ranked_robin.md) · [bv2145_6fj2kg_star](bv2145_6fj2kg_star.md) · [bv2146_krk2px_irv](bv2146_krk2px_irv.md) · [bv2146_krk2px_ranked_robin](bv2146_krk2px_ranked_robin.md) · [bv2146_krk2px_star](bv2146_krk2px_star.md) · [bv2147_9gdrqg_irv](bv2147_9gdrqg_irv.md) · [bv2147_9gdrqg_star](bv2147_9gdrqg_star.md) · [bv2148_h87k6v_irv](bv2148_h87k6v_irv.md) · [bv2148_h87k6v_star](bv2148_h87k6v_star.md) · [bv2149_byk9v2_irv](bv2149_byk9v2_irv.md) · [bv2149_byk9v2_star](bv2149_byk9v2_star.md) · [bv2150_dxg8pb_irv](bv2150_dxg8pb_irv.md) · [bv2150_dxg8pb_ranked_robin](bv2150_dxg8pb_ranked_robin.md) · [bv2150_dxg8pb_star](bv2150_dxg8pb_star.md) · [bv2151_97hbpw_irv](bv2151_97hbpw_irv.md) · [bv2151_97hbpw_ranked_robin](bv2151_97hbpw_ranked_robin.md) · [bv2151_97hbpw_star](bv2151_97hbpw_star.md) · [bv2152_r6ctvy_approval](bv2152_r6ctvy_approval.md) · [bv2152_r6ctvy_ranked_robin](bv2152_r6ctvy_ranked_robin.md) · [bv2153_pcttmr_approval](bv2153_pcttmr_approval.md) · [bv2153_pcttmr_irv](bv2153_pcttmr_irv.md) · [bv2153_pcttmr_ranked_robin](bv2153_pcttmr_ranked_robin.md) · [bv2154_wq6yv7_approval](bv2154_wq6yv7_approval.md) · [bv2154_wq6yv7_irv](bv2154_wq6yv7_irv.md) · [bv2154_wq6yv7_ranked_robin](bv2154_wq6yv7_ranked_robin.md) · [bv2160_r6qc8h_plurality](bv2160_r6qc8h_plurality.md) · [bv2160_r6qc8h_star](bv2160_r6qc8h_star.md) · [bv2161_q3h4fk_plurality](bv2161_q3h4fk_plurality.md) · [bv2161_q3h4fk_star](bv2161_q3h4fk_star.md) · [bv2162_4htk44_irv](bv2162_4htk44_irv.md) · [bv2162_4htk44_ranked_robin](bv2162_4htk44_ranked_robin.md) · [bv2162_4htk44_star](bv2162_4htk44_star.md) · [bv2163_74j6vv_irv](bv2163_74j6vv_irv.md) · [bv2163_74j6vv_ranked_robin](bv2163_74j6vv_ranked_robin.md) · [bv2163_74j6vv_star](bv2163_74j6vv_star.md) · [bv2164_xbqq8t_plurality](bv2164_xbqq8t_plurality.md) · [bv2164_xbqq8t_star](bv2164_xbqq8t_star.md) · [bv2165_9vxcj7_plurality](bv2165_9vxcj7_plurality.md) · [bv2165_9vxcj7_star](bv2165_9vxcj7_star.md) · [bv2166_b7b8dv_plurality](bv2166_b7b8dv_plurality.md) · [bv2166_b7b8dv_star](bv2166_b7b8dv_star.md) · [bv2167_f3dxq9_plurality](bv2167_f3dxq9_plurality.md) · [bv2167_f3dxq9_star](bv2167_f3dxq9_star.md) · [felsenthal_ex6_pareto_approval](felsenthal_ex6_pareto_approval.md) · [felsenthal_ex6_ranked_robin](felsenthal_ex6_ranked_robin.md)
