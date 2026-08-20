---
search:
  exclude: true
---

# Successive elimination Ex.10 — amalgamated: every round ties, and the tie-break picks the winner

*Generated from [`succ_elim_ex10_amalgamated.yaml`](../succ_elim_ex10_amalgamated.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../../05_Ranked_Robin/01_Learn/README.md) · **1 seat** · **Expected winner:** C

## Scenario

The amalgamation half of Felsenthal's successive-elimination reinforcement example — and the case where this repo's count is more precise than the paraphrase it replaces. Source: Dan S. Felsenthal (2010), Appendix A4, Example 10.
All four ballots: District I's three (A>B>C>D, B>D>C>A, D>C>A>B) plus District II's one (C>D>B>A). Each district elected C on its own under the agenda B vs D, winner vs A, winner vs C.
Counted together, ALL THREE rounds are 2:2 ties. B vs D ties, the survivor vs A ties, the survivor vs C ties — so the elected candidate is decided entirely by the tie-break convention and not at all by the ballots. Breaking toward the earlier letter gives C, agreeing with both districts and producing NO paradox; breaking toward the candidate earlier on the agenda gives B, which neither district chose and which is the reinforcement failure. Felsenthal calls the break random and claims only that B CAN win, which is exactly right.
Worth stating plainly because the earlier prose here said "B beats D in round 1": it does not, that round is a 2:2 tie like the other two. The failure is real but conditional, and the condition is the tie-break rule. A four-voter electorate is small enough that a tie is unremarkable; the lesson is that the procedure has no way to resolve one from the ballots.
Labels are Felsenthal's own, capitalized, so the case can be read beside the paper's table.
Tabulated as Ranked Robin, which elects C by a margin tiebreak inside a Copeland tie. Run the procedure both ways with tools_adam/pref_voting_tabulation_engine/successive_elimination_report.py --agenda B,D,A,C and --tiebreak agenda; the report re-runs the other convention itself and says when the winner moves.

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
1:A>B>C>D
1:B>D>C>A
1:D>C>A>B
1:C>D>B>A
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
--- Ranked Robin (RCV-RR / Copeland) Method (single winner) ---
 Tabulating 4 ballots (ranked ballots).

Ballots:
     1 × A > B > C > D
     1 × B > D > C > A
     1 × D > C > A > B
     1 × C > D > B > A

Round-Robin — every pair, head-to-head (For – Against):
   A  ties  B   2 – 2
   C  beats A   3 – 1
   D  beats A   3 – 1
   B  ties  C   2 – 2
   B  ties  D   2 – 2
   C  ties  D   2 – 2

--- Pairwise (Round-Robin) Matrix ---
Head-to-head / pairwise comparison — the Ranked Robin tally
Legend: For - Equal Support - Against   (row vs column)
      |     A     |    B     |    C     |    D     |
----------------------------------------------------
  A > |    ---    |2 - 0 - 2 |1 - 0 - 3 |1 - 0 - 3 |
  B > | 2 - 0 - 2 |   ---    |2 - 0 - 2 |2 - 0 - 2 |
  C > | 3 - 0 - 1 |2 - 0 - 2 |   ---    |2 - 0 - 2 |
  D > | 3 - 0 - 1 |2 - 0 - 2 |2 - 0 - 2 |   ---    |

Win–loss record — Copeland score = wins + ½·ties (highest score wins; ties broken by the Ranked Robin degrees, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  vs finalists  Beats
    1  C          1–0–2         2      +2             0  A
    2  D          1–0–2         2      +2             0  A
    3  B          0–0–3       1.5      +0             —  —
    4  A          0–2–1       0.5      -4             —  —

Winner — Ranked Robin (RCV-RR): C
   *** 2 candidates tie on the highest Copeland score (2): C, D — a dead heat (they draw head-to-head, not a cycle). Neither the 1st nor the 2nd Degree tiebreaker separates them — resolved by lot order.
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Smith Set (the generalized Condorcet winner) ---
The smallest group whose every member beats every candidate outside it —
the honest answer to "who is even in contention?".
   Smith set (4 of 4): C, D, B, A
   Outside (0):        —
   More than one member ⇒ NO Condorcet winner: the top of the tournament is a
   group held open by draws, so the strongest "candidate" is a set, not a
   person. Some members DO beat others, but no member beats them all — a draw
   blocks the sweep. No loop closes either, so there is no cycle for Minimax /
   Ranked Pairs / Schulze to resolve: which member wins is left to the
   tiebreak, not to a cycle rule. See
   05_Ranked_Robin/01_Learn/rr_tiebreak_lh_vs_bv.md.
   Note: the Copeland leaders (C, D) are only part of the set — the
   win–loss table's top block understates how wide the contention is.
   Ranked Robin (RCV-RR) winner C is INSIDE the Smith set. ✓
      Guaranteed: Ranked Robin (Copeland) is Smith-efficient — every member of
      the set outscores every outsider, so the top of the win–loss table is
      always inside the set, however the tie among them is then broken.
   Fine print: this set contains a pairwise DRAW, and a draw is enough to keep a
   candidate in the Smith set but not in the tighter Schwartz set — so Schwartz
   may be smaller here.
   More: 07_Concepts/topics/smith_set.md
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/succ_elim_ex10_amalgamated_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/felsenthal_paradoxes/cases/succ_elim_ex10_amalgamated.yaml
```

## See also

- [Ties & tie-breaking (topic hub)](../../../../07_Concepts/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [bv2144_mxfmhm_plurality](bv2144_mxfmhm_plurality.md) · [bv2144_mxfmhm_star](bv2144_mxfmhm_star.md) · [bv2145_6fj2kg_irv](bv2145_6fj2kg_irv.md) · [bv2145_6fj2kg_ranked_robin](bv2145_6fj2kg_ranked_robin.md) · [bv2145_6fj2kg_star](bv2145_6fj2kg_star.md) · [bv2146_krk2px_irv](bv2146_krk2px_irv.md) · [bv2146_krk2px_ranked_robin](bv2146_krk2px_ranked_robin.md) · [bv2146_krk2px_star](bv2146_krk2px_star.md) · [bv2147_9gdrqg_irv](bv2147_9gdrqg_irv.md) · [bv2147_9gdrqg_star](bv2147_9gdrqg_star.md) · [bv2148_h87k6v_irv](bv2148_h87k6v_irv.md) · [bv2148_h87k6v_star](bv2148_h87k6v_star.md) · [bv2149_byk9v2_irv](bv2149_byk9v2_irv.md) · [bv2149_byk9v2_star](bv2149_byk9v2_star.md) · [bv2150_dxg8pb_irv](bv2150_dxg8pb_irv.md) · [bv2150_dxg8pb_ranked_robin](bv2150_dxg8pb_ranked_robin.md) · [bv2150_dxg8pb_star](bv2150_dxg8pb_star.md) · [bv2151_97hbpw_irv](bv2151_97hbpw_irv.md) · [bv2151_97hbpw_ranked_robin](bv2151_97hbpw_ranked_robin.md) · [bv2151_97hbpw_star](bv2151_97hbpw_star.md) · [bv2152_r6ctvy_approval](bv2152_r6ctvy_approval.md) · [bv2152_r6ctvy_ranked_robin](bv2152_r6ctvy_ranked_robin.md) · [bv2153_pcttmr_approval](bv2153_pcttmr_approval.md) · [bv2153_pcttmr_irv](bv2153_pcttmr_irv.md) · [bv2153_pcttmr_ranked_robin](bv2153_pcttmr_ranked_robin.md) · [bv2154_wq6yv7_approval](bv2154_wq6yv7_approval.md) · [bv2154_wq6yv7_irv](bv2154_wq6yv7_irv.md) · [bv2154_wq6yv7_ranked_robin](bv2154_wq6yv7_ranked_robin.md) · [bv2160_r6qc8h_plurality](bv2160_r6qc8h_plurality.md) · [bv2160_r6qc8h_star](bv2160_r6qc8h_star.md) · [bv2161_q3h4fk_plurality](bv2161_q3h4fk_plurality.md) · [bv2161_q3h4fk_star](bv2161_q3h4fk_star.md) · [bv2162_4htk44_irv](bv2162_4htk44_irv.md) · [bv2162_4htk44_ranked_robin](bv2162_4htk44_ranked_robin.md) · [bv2162_4htk44_star](bv2162_4htk44_star.md) · [bv2163_74j6vv_irv](bv2163_74j6vv_irv.md) · [bv2163_74j6vv_ranked_robin](bv2163_74j6vv_ranked_robin.md) · [bv2163_74j6vv_star](bv2163_74j6vv_star.md) · [bv2164_xbqq8t_plurality](bv2164_xbqq8t_plurality.md) · [bv2164_xbqq8t_ranked_robin](bv2164_xbqq8t_ranked_robin.md) · [bv2164_xbqq8t_star](bv2164_xbqq8t_star.md) · [bv2165_9vxcj7_plurality](bv2165_9vxcj7_plurality.md) · [bv2165_9vxcj7_star](bv2165_9vxcj7_star.md) · [bv2166_b7b8dv_plurality](bv2166_b7b8dv_plurality.md) · [bv2166_b7b8dv_star](bv2166_b7b8dv_star.md) · [bv2167_f3dxq9_plurality](bv2167_f3dxq9_plurality.md) · [bv2167_f3dxq9_star](bv2167_f3dxq9_star.md) · [coombs_ex18_monotonicity](coombs_ex18_monotonicity.md) · [coombs_ex20_amalgamated](coombs_ex20_amalgamated.md) · [coombs_ex20_district1](coombs_ex20_district1.md) · [coombs_ex20_district2](coombs_ex20_district2.md) · [coombs_ex21_twin_after](coombs_ex21_twin_after.md) · [coombs_ex21_twin_before](coombs_ex21_twin_before.md) · [coombs_ex22_scc](coombs_ex22_scc.md) · [felsenthal_ex6_pareto_approval](felsenthal_ex6_pareto_approval.md) · [felsenthal_ex6_ranked_robin](felsenthal_ex6_ranked_robin.md) · [minimax_ex30_noshow_after](minimax_ex30_noshow_after.md) · [minimax_ex30_noshow_before](minimax_ex30_noshow_before.md) · [minimax_ex31_truncation](minimax_ex31_truncation.md) · [minimax_ex32_amalgamated](minimax_ex32_amalgamated.md) · [minimax_ex32_district2](minimax_ex32_district2.md) · [minimax_ex33_scc](minimax_ex33_scc.md) · [succ_elim_ex10_district1](succ_elim_ex10_district1.md) · [succ_elim_ex10_district2](succ_elim_ex10_district2.md) · [succ_elim_ex11_twin_after](succ_elim_ex11_twin_after.md) · [succ_elim_ex11_twin_before](succ_elim_ex11_twin_before.md) · [succ_elim_ex12_sincere](succ_elim_ex12_sincere.md) · [succ_elim_ex12_truncated](succ_elim_ex12_truncated.md) · [succ_elim_ex9_noshow](succ_elim_ex9_noshow.md) · [succ_elim_ex9_pareto](succ_elim_ex9_pareto.md)
