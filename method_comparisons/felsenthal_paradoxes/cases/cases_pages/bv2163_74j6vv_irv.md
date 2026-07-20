# Nurmi Ex.16 truncated — RCV-IRV: ranking ONLY their favorite serves 17 voters better

*Generated from [`bv2163_74j6vv_irv.yaml`](../bv2163_74j6vv_irv.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [RCV-IRV (Instant Runoff)](../../../../00_start_here/RCV_IRV) · **1 seat** · **Expected winner:** B

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/74j6vv) · **[results ↗](https://bettervoting.com/74j6vv/results)** (election `74j6vv`).

## Scenario

Race 2 of 3 in the RCV-IRV truncation pair, part 2 of 2 (BV2163, bvid 74j6vv; BV-confirmed; the pair is BV2162/63). Source: Dan S. Felsenthal, "Review of Paradoxes Afflicting Various Voting Procedures Where One Out of m Candidates (m ≥ 2) Must Be Elected", University of Haifa / LSE, revised 26 May 2010; Appendix A6, Example 16, due to Nurmi (1999: 63).
Identical to BV2162 except one datum, ceteris paribus: the 17 voters whose full ordering is D>C>B>A TRUNCATE and rank only D. D is eliminated first exactly as before — but the truncated ballots EXHAUST instead of transferring to C, so C (24) is eliminated instead of B, C's transfers flow to B, and B wins. The truncators prefer B to A (the sincere-IRV winner of BV2162), so ranking FEWER candidates got them a BETTER result: the Truncation paradox, live. It also accidentally repairs IRV's Condorcet failure — B, the Condorcet winner, now wins.
Live results: https://bettervoting.com/74j6vv/results

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
33:A>B>C>D
29:B>A>C>D
24:C>B>A>D
17:D
```

## What the engine says

Full report from the [`_tabulated` mirror](../cases_tabulated/bv2163_74j6vv_irv_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- RCV / Instant-Runoff Voting (single winner) ---
  Nurmi Ex.16 truncated — RCV-IRV: ranking ONLY their favorite serves 17 voters better
 Tabulating 103 ballots (ranked ballots).

ROUND 1
Candidate      Votes  Status
-----------  -------  --------
A                 33  Hopeful
B                 29  Hopeful
C                 24  Hopeful
D                 17  Rejected

ROUND 2
Candidate      Votes  Status
-----------  -------  --------
A                 33  Hopeful
B                 29  Hopeful
C                 24  Rejected
D                  0  Rejected
Blank Votes       17  Rejected

FINAL RESULT
Candidate      Votes  Status
-----------  -------  --------
B                 53  Elected
A                 33  Rejected
C                  0  Rejected
D                  0  Rejected
Blank Votes       17  Rejected


Winner(s) — RCV / Instant-Runoff Voting (single winner)
  B
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/felsenthal_paradoxes/cases/bv2163_74j6vv_irv.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../00_start_here/topics/condorcet/README.md)
- [Exhausted ballots (conversation)](../../../../00_start_here/RCV_IRV/exhausted_ballots_301.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [bv2144_mxfmhm_plurality](bv2144_mxfmhm_plurality.md) · [bv2144_mxfmhm_star](bv2144_mxfmhm_star.md) · [bv2145_6fj2kg_irv](bv2145_6fj2kg_irv.md) · [bv2145_6fj2kg_ranked_robin](bv2145_6fj2kg_ranked_robin.md) · [bv2145_6fj2kg_star](bv2145_6fj2kg_star.md) · [bv2146_krk2px_irv](bv2146_krk2px_irv.md) · [bv2146_krk2px_ranked_robin](bv2146_krk2px_ranked_robin.md) · [bv2146_krk2px_star](bv2146_krk2px_star.md) · [bv2147_9gdrqg_irv](bv2147_9gdrqg_irv.md) · [bv2147_9gdrqg_star](bv2147_9gdrqg_star.md) · [bv2148_h87k6v_irv](bv2148_h87k6v_irv.md) · [bv2148_h87k6v_star](bv2148_h87k6v_star.md) · [bv2149_byk9v2_irv](bv2149_byk9v2_irv.md) · [bv2149_byk9v2_star](bv2149_byk9v2_star.md) · [bv2150_dxg8pb_irv](bv2150_dxg8pb_irv.md) · [bv2150_dxg8pb_ranked_robin](bv2150_dxg8pb_ranked_robin.md) · [bv2150_dxg8pb_star](bv2150_dxg8pb_star.md) · [bv2151_97hbpw_irv](bv2151_97hbpw_irv.md) · [bv2151_97hbpw_ranked_robin](bv2151_97hbpw_ranked_robin.md) · [bv2151_97hbpw_star](bv2151_97hbpw_star.md) · [bv2152_r6ctvy_approval](bv2152_r6ctvy_approval.md) · [bv2152_r6ctvy_ranked_robin](bv2152_r6ctvy_ranked_robin.md) · [bv2153_pcttmr_approval](bv2153_pcttmr_approval.md) · [bv2153_pcttmr_irv](bv2153_pcttmr_irv.md) · [bv2153_pcttmr_ranked_robin](bv2153_pcttmr_ranked_robin.md) · [bv2154_wq6yv7_approval](bv2154_wq6yv7_approval.md) · [bv2154_wq6yv7_irv](bv2154_wq6yv7_irv.md) · [bv2154_wq6yv7_ranked_robin](bv2154_wq6yv7_ranked_robin.md) · [bv2160_r6qc8h_plurality](bv2160_r6qc8h_plurality.md) · [bv2160_r6qc8h_star](bv2160_r6qc8h_star.md) · [bv2161_q3h4fk_plurality](bv2161_q3h4fk_plurality.md) · [bv2161_q3h4fk_star](bv2161_q3h4fk_star.md) · [bv2162_4htk44_irv](bv2162_4htk44_irv.md) · [bv2162_4htk44_ranked_robin](bv2162_4htk44_ranked_robin.md) · [bv2162_4htk44_star](bv2162_4htk44_star.md) · [bv2163_74j6vv_ranked_robin](bv2163_74j6vv_ranked_robin.md) · [bv2163_74j6vv_star](bv2163_74j6vv_star.md) · [bv2164_xbqq8t_plurality](bv2164_xbqq8t_plurality.md) · [bv2164_xbqq8t_ranked_robin](bv2164_xbqq8t_ranked_robin.md) · [bv2164_xbqq8t_star](bv2164_xbqq8t_star.md) · [bv2165_9vxcj7_plurality](bv2165_9vxcj7_plurality.md) · [bv2165_9vxcj7_star](bv2165_9vxcj7_star.md) · [bv2166_b7b8dv_plurality](bv2166_b7b8dv_plurality.md) · [bv2166_b7b8dv_star](bv2166_b7b8dv_star.md) · [bv2167_f3dxq9_plurality](bv2167_f3dxq9_plurality.md) · [bv2167_f3dxq9_star](bv2167_f3dxq9_star.md) · [felsenthal_ex6_pareto_approval](felsenthal_ex6_pareto_approval.md) · [felsenthal_ex6_ranked_robin](felsenthal_ex6_ranked_robin.md)
