# Felsenthal Ex.2 after the raise — Runoff/IRV: Ben loses by GAINING support

*Generated from [`bv2146_krk2px_irv.yaml`](../bv2146_krk2px_irv.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [RCV-IRV (Instant Runoff)](../../../00_start_here/RCV_IRV) · **1 seat** · **Expected winner:** Ada

## Scenario

Race 1 of 3 in the Felsenthal runoff-paradoxes election, part 2 of 2 (BV2146, bvid krk2px; BV-confirmed). Source: Dan S. Felsenthal, "Review of Paradoxes Afflicting Various Voting Procedures Where One Out of m Candidates (m ≥ 2) Must Be Elected", University of Haifa / LSE, revised 26 May 2010; Appendix A2, Example 2 (continued).
Identical to BV2145 except one datum, ceteris paribus: the two Cleo>Ben>Ada voters RAISE Ben to first (Ben>Cleo>Ada) — strictly more support for Ben, nothing else changes. First choices become Ada 5, Ben 8, Cleo 4, so the runoff procedure (IRV; identical for three candidates) now eliminates CLEO instead of Ada — and Ada beats Ben 9–8. Ben, who won BV2145, loses precisely because two voters moved him UP: the lack-of-monotonicity (more-is-less) paradox, Felsenthal's model CONDITIONAL paradox. Confirmed live on BetterVoting.
Live results: https://bettervoting.com/krk2px/results

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
3:Ada>Ben>Cleo
2:Ada>Cleo>Ben
4:Ben>Ada>Cleo
2:Ben>Cleo>Ada
4:Cleo>Ada>Ben
2:Ben>Cleo>Ada
```

## What the engine says

Full report from the [`_tabulated` mirror](../felsenthal_paradoxes_tabulated/bv2146_krk2px_irv_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- RCV / Instant-Runoff Voting (single winner) ---
  Felsenthal Ex.2 after the raise — Runoff/IRV: Ben loses by GAINING support
 Tabulating 17 ballots (ranked ballots).

ROUND 1
Candidate      Votes  Status
-----------  -------  --------
Ben                8  Hopeful
Ada                5  Hopeful
Cleo               4  Rejected

FINAL RESULT
Candidate      Votes  Status
-----------  -------  --------
Ada                9  Elected
Ben                8  Rejected
Cleo               0  Rejected


Winner(s) — RCV / Instant-Runoff Voting (single winner)
  Ada
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/felsenthal_paradoxes/bv2146_krk2px_irv.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Monotonicity (topic hub)](../../../00_start_here/topics/monotonicity/README.md)
- [Runoff reversal (worked set)](../../../01_STAR/runoff_overturns_leader/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [bv2144_mxfmhm_plurality](bv2144_mxfmhm_plurality.md) · [bv2144_mxfmhm_star](bv2144_mxfmhm_star.md) · [bv2145_6fj2kg_irv](bv2145_6fj2kg_irv.md) · [bv2145_6fj2kg_ranked_robin](bv2145_6fj2kg_ranked_robin.md) · [bv2145_6fj2kg_star](bv2145_6fj2kg_star.md) · [bv2146_krk2px_ranked_robin](bv2146_krk2px_ranked_robin.md) · [bv2146_krk2px_star](bv2146_krk2px_star.md) · [bv2147_9gdrqg_irv](bv2147_9gdrqg_irv.md) · [bv2147_9gdrqg_star](bv2147_9gdrqg_star.md) · [bv2148_h87k6v_irv](bv2148_h87k6v_irv.md) · [bv2148_h87k6v_star](bv2148_h87k6v_star.md) · [bv2149_byk9v2_irv](bv2149_byk9v2_irv.md) · [bv2149_byk9v2_star](bv2149_byk9v2_star.md)
