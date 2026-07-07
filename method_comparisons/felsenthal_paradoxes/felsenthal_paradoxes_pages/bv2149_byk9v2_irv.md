# Felsenthal Ex.3 Combined — Runoff/IRV: Bruno won both districts, Alma wins the whole

*Generated from [`bv2149_byk9v2_irv.yaml`](../bv2149_byk9v2_irv.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [RCV-IRV (Instant Runoff)](../../../00_start_here/RCV_IRV) · **1 seat** · **Expected winner:** Alma

## Scenario

Race 1 of 2 in the Combined stage of the Felsenthal Reinforcement-paradox trio (BV2149, bvid byk9v2; BV-confirmed; the trio is BV2147/48/49). Source: Dan S. Felsenthal, "Review of Paradoxes Afflicting Various Voting Procedures Where One Out of m Candidates (m ≥ 2) Must Be Elected", University of Haifa / LSE, revised 26 May 2010; Appendix A2, Example 3 (the Reinforcement paradox).
The amalgamated electorate: the 32 voters of Districts I (BV2147) and II (BV2148) together, ceteris paribus. No first-round majority (Alma 10, Bruno 14, Cora 8), so CORA is deleted — and Alma beats Bruno 17–15 in the runoff. Bruno won BOTH districts separately; amalgamating two electorates that each chose Bruno makes plurality-with-runoff (run as IRV, identical for three candidates) elect Alma. That violates the Reinforcement postulate — the multiple-districts / inconsistency paradox, live on BetterVoting. The combined pairwise preferences form a Condorcet CYCLE (Alma>Bruno 17–15, Bruno>Cora 18–14, Cora>Alma 21–11), so no Condorcet argument rescues the flip: the procedure simply disagrees with itself.
Live results: https://bettervoting.com/byk9v2/results

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
4:Alma>Bruno>Cora
6:Alma>Cora>Bruno
1:Bruno>Alma>Cora
13:Bruno>Cora>Alma
7:Cora>Alma>Bruno
1:Cora>Bruno>Alma
```

## What the engine says

Full report from the [`_tabulated` mirror](../felsenthal_paradoxes_tabulated/bv2149_byk9v2_irv_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- RCV / Instant-Runoff Voting (single winner) ---
  Felsenthal Ex.3 Combined — Runoff/IRV: Bruno won both districts, Alma wins the whole
 Tabulating 32 ballots (ranked ballots).

ROUND 1
Candidate      Votes  Status
-----------  -------  --------
Bruno             14  Hopeful
Alma              10  Hopeful
Cora               8  Rejected

FINAL RESULT
Candidate      Votes  Status
-----------  -------  --------
Alma              17  Elected
Bruno             15  Rejected
Cora               0  Rejected


Winner(s) — RCV / Instant-Runoff Voting (single winner)
  Alma
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/felsenthal_paradoxes/bv2149_byk9v2_irv.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README.md)
- [Runoff reversal (worked set)](../../../01_STAR/runoff_overturns_leader/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [bv2144_mxfmhm_plurality](bv2144_mxfmhm_plurality.md) · [bv2144_mxfmhm_star](bv2144_mxfmhm_star.md) · [bv2145_6fj2kg_irv](bv2145_6fj2kg_irv.md) · [bv2145_6fj2kg_ranked_robin](bv2145_6fj2kg_ranked_robin.md) · [bv2145_6fj2kg_star](bv2145_6fj2kg_star.md) · [bv2146_krk2px_irv](bv2146_krk2px_irv.md) · [bv2146_krk2px_ranked_robin](bv2146_krk2px_ranked_robin.md) · [bv2146_krk2px_star](bv2146_krk2px_star.md) · [bv2147_9gdrqg_irv](bv2147_9gdrqg_irv.md) · [bv2147_9gdrqg_star](bv2147_9gdrqg_star.md) · [bv2148_h87k6v_irv](bv2148_h87k6v_irv.md) · [bv2148_h87k6v_star](bv2148_h87k6v_star.md) · [bv2149_byk9v2_star](bv2149_byk9v2_star.md) · [bv2150_dxg8pb_irv](bv2150_dxg8pb_irv.md) · [bv2150_dxg8pb_ranked_robin](bv2150_dxg8pb_ranked_robin.md) · [bv2150_dxg8pb_star](bv2150_dxg8pb_star.md) · [bv2151_97hbpw_irv](bv2151_97hbpw_irv.md) · [bv2151_97hbpw_ranked_robin](bv2151_97hbpw_ranked_robin.md) · [bv2151_97hbpw_star](bv2151_97hbpw_star.md)
