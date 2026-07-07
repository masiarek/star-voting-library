# Felsenthal Ex.4 after two no-shows — Runoff/IRV: the abstainers do better

*Generated from [`bv2151_97hbpw_irv.yaml`](../bv2151_97hbpw_irv.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [RCV-IRV (Instant Runoff)](../../../00_start_here/RCV_IRV) · **1 seat** · **Expected winner:** Beth

## Scenario

Race 1 of 3 in the No-Show-paradox pair, part 2 of 2 (BV2151, bvid 97hbpw; BV-confirmed; the pair is BV2150/51). Source: Dan S. Felsenthal, "Review of Paradoxes Afflicting Various Voting Procedures Where One Out of m Candidates (m ≥ 2) Must Be Elected", University of Haifa / LSE, revised 26 May 2010; Appendix A2, Example 4 (the No-Show and Twin paradoxes).
Ceteris paribus, TWO of the four Andy>Beth>Carl voters stay home: 9 voters — 2×(Andy>Beth>Carl), 3×(Beth>Carl>Andy), 1×(Carl>Andy>Beth), 3×(Carl>Beth>Andy). First choices are now Andy 2, Beth 3, Carl 4, so the runoff procedure (IRV; identical for three candidates) deletes ANDY — and Beth beats Carl 5–4. The two abstainers get Beth (their second choice) instead of Carl (their last, BV2150): staying home served them better than voting — the No-Show paradox. Read in reverse it is the weak TWIN paradox: add two voters identical to the Andy pair, and the twins' arrival elects their common worst choice.
Live results: https://bettervoting.com/97hbpw/results

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
2:Andy>Beth>Carl
3:Beth>Carl>Andy
1:Carl>Andy>Beth
3:Carl>Beth>Andy
```

## What the engine says

Full report from the [`_tabulated` mirror](../felsenthal_paradoxes_tabulated/bv2151_97hbpw_irv_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- RCV / Instant-Runoff Voting (single winner) ---
  Felsenthal Ex.4 after two no-shows — Runoff/IRV: the abstainers do better
 Tabulating 9 ballots (ranked ballots).

ROUND 1
Candidate      Votes  Status
-----------  -------  --------
Carl               4  Hopeful
Beth               3  Hopeful
Andy               2  Rejected

FINAL RESULT
Candidate      Votes  Status
-----------  -------  --------
Beth               5  Elected
Carl               4  Rejected
Andy               0  Rejected


Winner(s) — RCV / Instant-Runoff Voting (single winner)
  Beth
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/felsenthal_paradoxes/bv2151_97hbpw_irv.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Runoff reversal (worked set)](../../../01_STAR/runoff_overturns_leader/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [bv2144_mxfmhm_plurality](bv2144_mxfmhm_plurality.md) · [bv2144_mxfmhm_star](bv2144_mxfmhm_star.md) · [bv2145_6fj2kg_irv](bv2145_6fj2kg_irv.md) · [bv2145_6fj2kg_ranked_robin](bv2145_6fj2kg_ranked_robin.md) · [bv2145_6fj2kg_star](bv2145_6fj2kg_star.md) · [bv2146_krk2px_irv](bv2146_krk2px_irv.md) · [bv2146_krk2px_ranked_robin](bv2146_krk2px_ranked_robin.md) · [bv2146_krk2px_star](bv2146_krk2px_star.md) · [bv2147_9gdrqg_irv](bv2147_9gdrqg_irv.md) · [bv2147_9gdrqg_star](bv2147_9gdrqg_star.md) · [bv2148_h87k6v_irv](bv2148_h87k6v_irv.md) · [bv2148_h87k6v_star](bv2148_h87k6v_star.md) · [bv2149_byk9v2_irv](bv2149_byk9v2_irv.md) · [bv2149_byk9v2_star](bv2149_byk9v2_star.md) · [bv2150_dxg8pb_irv](bv2150_dxg8pb_irv.md) · [bv2150_dxg8pb_ranked_robin](bv2150_dxg8pb_ranked_robin.md) · [bv2150_dxg8pb_star](bv2150_dxg8pb_star.md) · [bv2151_97hbpw_ranked_robin](bv2151_97hbpw_ranked_robin.md) · [bv2151_97hbpw_star](bv2151_97hbpw_star.md) · [bv2152_r6ctvy_approval](bv2152_r6ctvy_approval.md) · [bv2152_r6ctvy_ranked_robin](bv2152_r6ctvy_ranked_robin.md) · [bv2153_pcttmr_approval](bv2153_pcttmr_approval.md) · [bv2153_pcttmr_irv](bv2153_pcttmr_irv.md) · [bv2153_pcttmr_ranked_robin](bv2153_pcttmr_ranked_robin.md) · [bv2154_wq6yv7_approval](bv2154_wq6yv7_approval.md) · [bv2154_wq6yv7_irv](bv2154_wq6yv7_irv.md) · [bv2154_wq6yv7_ranked_robin](bv2154_wq6yv7_ranked_robin.md) · [felsenthal_ex6_pareto_approval](felsenthal_ex6_pareto_approval.md) · [felsenthal_ex6_ranked_robin](felsenthal_ex6_ranked_robin.md)
