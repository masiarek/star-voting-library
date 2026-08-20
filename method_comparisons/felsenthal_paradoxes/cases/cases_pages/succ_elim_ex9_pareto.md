---
search:
  exclude: true
---

# Successive elimination Ex.9 — the agenda elects B, whom every voter ranks below A

*Generated from [`succ_elim_ex9_pareto.yaml`](../succ_elim_ex9_pareto.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../../05_Ranked_Robin/01_Learn/README.md) · **1 seat** · **Expected winner:** D

## Scenario

Felsenthal's flagship successive-elimination example, and the densest case in the whole appendix: one 11-voter profile that yields four different paradoxes depending on which single datum you vary. Source: Dan S. Felsenthal, "Review of Paradoxes Afflicting Various Voting Procedures Where One Out of m Candidates (m ≥ 2) Must Be Elected", University of Haifa / LSE, revised 26 May 2010; Appendix A4, Example 9.
11 voters, four candidates: 3×(A>B>C>D), 2×(C>A>B>D), 1×(C>D>A>B), 5×(D>A>B>C). The majority preference cycles (B>C>D>A>B), which is the precondition for everything below.
PARETO. Under the agenda D vs A, winner vs C, winner vs B: D beats A 6:5, C beats D 6:5, B beats C 8:3 — B is elected. But all 11 voters rank A above B, unanimously and without exception. A Pareto-dominated candidate wins.
PATH INDEPENDENCE. Same ballots, agenda A vs B, winner vs C, winner vs D: A beats B 11:0, A beats C 8:3, then D beats A 6:5 — D wins. Under a cycle the agenda-setter picks the winner, not the electorate.
SCC. Delete D, who wins nothing under the first agenda: A beats C 8:3 and then B 11:0, so A wins. A non-winner's mere presence decided the election.
NO-SHOW is the companion file succ_elim_ex9_noshow.yaml, where two of the D-first voters stay home and get A, whom they prefer to B.
Labels are Felsenthal's own, capitalized; this is an academic reproduction meant to be read beside the paper's table, not a scenario with a cast.
Successive elimination exists in neither the LH engine nor BetterVoting — it is a parliamentary procedure, not a ballot-box method — so this file is tabulated as Ranked Robin, which reads the same pairwise matrix the agenda consumes one pair at a time. Ranked Robin ties A and D at 2 wins each and separates them the way the method says to — the finalists' own head-to-head, its 1st Degree — which D wins 6:5. So Ranked Robin elects D: not the Pareto-dominated B the first agenda produces, and not the A the third agenda produces, but the winner of the second. (Before 2026-08-19 the engine used total margin over the whole field here and reported A; that is Ranked Robin's 2nd Degree, reachable only when the finalists are level against each other — see 05_Ranked_Robin/03_Criteria/rr_tiebreaks/degrees_of_ties.md.) Run the procedure itself with tools_adam/pref_voting_tabulation_engine/successive_elimination_report.py, whose --agenda and --drop flags reproduce all four readings above.

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
3:A>B>C>D
2:C>A>B>D
1:C>D>A>B
5:D>A>B>C
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
--- Ranked Robin (RCV-RR / Copeland) Method (single winner) ---
 Tabulating 11 ballots (ranked ballots).

Ballots:
     3 × A > B > C > D
     2 × C > A > B > D
     1 × C > D > A > B
     5 × D > A > B > C

Round-Robin — every pair, head-to-head (For – Against):
   A  beats B   11 –  0
   A  beats C    8 –  3
   D  beats A    6 –  5
   B  beats C    8 –  3
   D  beats B    6 –  5
   C  beats D    6 –  5

--- Pairwise (Round-Robin) Matrix ---
Head-to-head / pairwise comparison — the Ranked Robin tally
Legend: For - Equal Support - Against   (row vs column)
      |      A       |     B       |     C       |     D       |
----------------------------------------------------------------
  A > |     ---      |11 -  0 -  0 | 8 -  0 -  3 | 5 -  0 -  6 |
  B > |  0 -  0 - 11 |    ---      | 8 -  0 -  3 | 5 -  0 -  6 |
  C > |  3 -  0 -  8 | 3 -  0 -  8 |    ---      | 6 -  0 -  5 |
  D > |  6 -  0 -  5 | 6 -  0 -  5 | 5 -  0 -  6 |    ---      |

Win–loss record — Copeland score = wins + ½·ties (highest score wins; ties broken by the Ranked Robin degrees, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  vs finalists  Beats
    1  D          2–1–0         2      +1            +1  A, B
    2  A          2–1–0         2     +15            -1  B, C
    3  B          1–2–0         1      -7             —  C
    4  C          1–2–0         1      -9             —  D

Winner — Ranked Robin (RCV-RR): D
   *** 2 candidates tie for the most wins (A, D) — tied on the tally, not a cycle (some of them beat others head-to-head, but no loop closes). Resolved by the 1st Degree tiebreaker: D has the greatest sum of win margins over the other finalists (+1).
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Smith Set (the generalized Condorcet winner) ---
The smallest group whose every member beats every candidate outside it —
the honest answer to "who is even in contention?".
   Smith set (4 of 4): A, D, B, C
   Outside (0):        —
   More than one member ⇒ NO Condorcet winner: the top of the tournament is a
   cycle, so the strongest "candidate" is a set, not a person. Which member of
   the set should win is exactly what Minimax / Ranked Pairs / Schulze disagree
   about — see 05_Ranked_Robin/01_Learn/cycle_resolution.md.
   Note: the Copeland leaders (A, D) are only part of the set — the
   win–loss table's top block understates how wide the contention is.
   Ranked Robin (RCV-RR) winner D is INSIDE the Smith set. ✓
      Guaranteed: Ranked Robin (Copeland) is Smith-efficient — every member of
      the set outscores every outsider, so the top of the win–loss table is
      always inside the set, however the tie among them is then broken.
   More: 07_Concepts/topics/smith_set.md
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/succ_elim_ex9_pareto_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/felsenthal_paradoxes/cases/succ_elim_ex9_pareto.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../07_Concepts/topics/condorcet/README.md)
- [Ties & tie-breaking (topic hub)](../../../../07_Concepts/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [bv2144_mxfmhm_plurality](bv2144_mxfmhm_plurality.md) · [bv2144_mxfmhm_star](bv2144_mxfmhm_star.md) · [bv2145_6fj2kg_irv](bv2145_6fj2kg_irv.md) · [bv2145_6fj2kg_ranked_robin](bv2145_6fj2kg_ranked_robin.md) · [bv2145_6fj2kg_star](bv2145_6fj2kg_star.md) · [bv2146_krk2px_irv](bv2146_krk2px_irv.md) · [bv2146_krk2px_ranked_robin](bv2146_krk2px_ranked_robin.md) · [bv2146_krk2px_star](bv2146_krk2px_star.md) · [bv2147_9gdrqg_irv](bv2147_9gdrqg_irv.md) · [bv2147_9gdrqg_star](bv2147_9gdrqg_star.md) · [bv2148_h87k6v_irv](bv2148_h87k6v_irv.md) · [bv2148_h87k6v_star](bv2148_h87k6v_star.md) · [bv2149_byk9v2_irv](bv2149_byk9v2_irv.md) · [bv2149_byk9v2_star](bv2149_byk9v2_star.md) · [bv2150_dxg8pb_irv](bv2150_dxg8pb_irv.md) · [bv2150_dxg8pb_ranked_robin](bv2150_dxg8pb_ranked_robin.md) · [bv2150_dxg8pb_star](bv2150_dxg8pb_star.md) · [bv2151_97hbpw_irv](bv2151_97hbpw_irv.md) · [bv2151_97hbpw_ranked_robin](bv2151_97hbpw_ranked_robin.md) · [bv2151_97hbpw_star](bv2151_97hbpw_star.md) · [bv2152_r6ctvy_approval](bv2152_r6ctvy_approval.md) · [bv2152_r6ctvy_ranked_robin](bv2152_r6ctvy_ranked_robin.md) · [bv2153_pcttmr_approval](bv2153_pcttmr_approval.md) · [bv2153_pcttmr_irv](bv2153_pcttmr_irv.md) · [bv2153_pcttmr_ranked_robin](bv2153_pcttmr_ranked_robin.md) · [bv2154_wq6yv7_approval](bv2154_wq6yv7_approval.md) · [bv2154_wq6yv7_irv](bv2154_wq6yv7_irv.md) · [bv2154_wq6yv7_ranked_robin](bv2154_wq6yv7_ranked_robin.md) · [bv2160_r6qc8h_plurality](bv2160_r6qc8h_plurality.md) · [bv2160_r6qc8h_star](bv2160_r6qc8h_star.md) · [bv2161_q3h4fk_plurality](bv2161_q3h4fk_plurality.md) · [bv2161_q3h4fk_star](bv2161_q3h4fk_star.md) · [bv2162_4htk44_irv](bv2162_4htk44_irv.md) · [bv2162_4htk44_ranked_robin](bv2162_4htk44_ranked_robin.md) · [bv2162_4htk44_star](bv2162_4htk44_star.md) · [bv2163_74j6vv_irv](bv2163_74j6vv_irv.md) · [bv2163_74j6vv_ranked_robin](bv2163_74j6vv_ranked_robin.md) · [bv2163_74j6vv_star](bv2163_74j6vv_star.md) · [bv2164_xbqq8t_plurality](bv2164_xbqq8t_plurality.md) · [bv2164_xbqq8t_ranked_robin](bv2164_xbqq8t_ranked_robin.md) · [bv2164_xbqq8t_star](bv2164_xbqq8t_star.md) · [bv2165_9vxcj7_plurality](bv2165_9vxcj7_plurality.md) · [bv2165_9vxcj7_star](bv2165_9vxcj7_star.md) · [bv2166_b7b8dv_plurality](bv2166_b7b8dv_plurality.md) · [bv2166_b7b8dv_star](bv2166_b7b8dv_star.md) · [bv2167_f3dxq9_plurality](bv2167_f3dxq9_plurality.md) · [bv2167_f3dxq9_star](bv2167_f3dxq9_star.md) · [coombs_ex18_monotonicity](coombs_ex18_monotonicity.md) · [coombs_ex20_amalgamated](coombs_ex20_amalgamated.md) · [coombs_ex20_district1](coombs_ex20_district1.md) · [coombs_ex20_district2](coombs_ex20_district2.md) · [coombs_ex21_twin_after](coombs_ex21_twin_after.md) · [coombs_ex21_twin_before](coombs_ex21_twin_before.md) · [coombs_ex22_scc](coombs_ex22_scc.md) · [felsenthal_ex6_pareto_approval](felsenthal_ex6_pareto_approval.md) · [felsenthal_ex6_ranked_robin](felsenthal_ex6_ranked_robin.md) · [minimax_ex30_noshow_after](minimax_ex30_noshow_after.md) · [minimax_ex30_noshow_before](minimax_ex30_noshow_before.md) · [minimax_ex31_truncation](minimax_ex31_truncation.md) · [minimax_ex32_amalgamated](minimax_ex32_amalgamated.md) · [minimax_ex32_district2](minimax_ex32_district2.md) · [minimax_ex33_scc](minimax_ex33_scc.md) · [succ_elim_ex10_amalgamated](succ_elim_ex10_amalgamated.md) · [succ_elim_ex10_district1](succ_elim_ex10_district1.md) · [succ_elim_ex10_district2](succ_elim_ex10_district2.md) · [succ_elim_ex11_twin_after](succ_elim_ex11_twin_after.md) · [succ_elim_ex11_twin_before](succ_elim_ex11_twin_before.md) · [succ_elim_ex12_sincere](succ_elim_ex12_sincere.md) · [succ_elim_ex12_truncated](succ_elim_ex12_truncated.md) · [succ_elim_ex9_noshow](succ_elim_ex9_noshow.md)
