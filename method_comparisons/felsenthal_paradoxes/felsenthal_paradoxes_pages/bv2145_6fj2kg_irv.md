# Felsenthal Ex.2 — Runoff/IRV: the Condorcet winner is eliminated first

*Generated from [`bv2145_6fj2kg_irv.yaml`](../bv2145_6fj2kg_irv.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [RCV-IRV (Instant Runoff)](../../../00_start_here/RCV_IRV) · **1 seat** · **Expected winner:** Ben

## Scenario

Race 1 of 3 in the Felsenthal runoff-paradoxes election, part 1 of 2 (BV2145, bvid 6fj2kg; BV-confirmed). Source: Dan S. Felsenthal, "Review of Paradoxes Afflicting Various Voting Procedures Where One Out of m Candidates (m ≥ 2) Must Be Elected", University of Haifa / LSE, revised 26 May 2010; Appendix A2, Example 2 (plurality with runoff).
17 voters, three candidates. Ada is the Condorcet winner (beats Ben 9–8 and Cleo 9–8; social ordering Ada>Ben>Cleo) but has the FEWEST first choices (Ada 5, Ben 6, Cleo 6). Plurality-with-runoff — run here as IRV, which is identical for three candidates — eliminates Ada first, and Ben beats Cleo 9–8. The Condorcet winner paradox, plus Felsenthal's SCC note: had Cleo withdrawn, Ada would have won the first round outright (9 of 17). The non-monotonicity half of the lesson is the paired election BV2146.
Live results: https://bettervoting.com/6fj2kg/results

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
3:Ada>Ben>Cleo
2:Ada>Cleo>Ben
4:Ben>Ada>Cleo
2:Ben>Cleo>Ada
4:Cleo>Ada>Ben
2:Cleo>Ben>Ada
```

## What the engine says

Full report from the [`_tabulated` mirror](../felsenthal_paradoxes_tabulated/bv2145_6fj2kg_irv_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- RCV / Instant-Runoff Voting (single winner) ---
  Felsenthal Ex.2 — Runoff/IRV: the Condorcet winner is eliminated first
 Tabulating 17 ballots (ranked ballots).

ROUND 1
Candidate      Votes  Status
-----------  -------  --------
Ben                6  Hopeful
Cleo               6  Hopeful
Ada                5  Rejected

FINAL RESULT
Candidate      Votes  Status
-----------  -------  --------
Ben                9  Elected
Cleo               8  Rejected
Ada                0  Rejected


Winner(s) — RCV / Instant-Runoff Voting (single winner)
  Ben
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/felsenthal_paradoxes/bv2145_6fj2kg_irv.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Monotonicity (topic hub)](../../../00_start_here/topics/monotonicity/README.md)
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README.md)
- [Runoff reversal (worked set)](../../../01_STAR/runoff_overturns_leader/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [bv2144_mxfmhm_plurality](bv2144_mxfmhm_plurality.md) · [bv2144_mxfmhm_star](bv2144_mxfmhm_star.md) · [bv2145_6fj2kg_ranked_robin](bv2145_6fj2kg_ranked_robin.md) · [bv2145_6fj2kg_star](bv2145_6fj2kg_star.md) · [bv2146_krk2px_irv](bv2146_krk2px_irv.md) · [bv2146_krk2px_ranked_robin](bv2146_krk2px_ranked_robin.md) · [bv2146_krk2px_star](bv2146_krk2px_star.md)
