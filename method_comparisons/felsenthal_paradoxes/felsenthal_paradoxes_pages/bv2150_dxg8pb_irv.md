# Felsenthal Ex.4 full electorate — Runoff/IRV: their worst choice wins

*Generated from [`bv2150_dxg8pb_irv.yaml`](../bv2150_dxg8pb_irv.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [RCV-IRV (Instant Runoff)](../../../00_start_here/RCV_IRV) · **1 seat** · **Expected winner:** Carl

## Scenario

Race 1 of 3 in the No-Show-paradox pair, part 1 of 2 (BV2150, bvid dxg8pb; BV-confirmed; the pair is BV2150/51). Source: Dan S. Felsenthal, "Review of Paradoxes Afflicting Various Voting Procedures Where One Out of m Candidates (m ≥ 2) Must Be Elected", University of Haifa / LSE, revised 26 May 2010; Appendix A2, Example 4 (the No-Show and Twin paradoxes).
The full electorate: 11 voters — 4×(Andy>Beth>Carl), 3×(Beth>Carl>Andy), 1×(Carl>Andy>Beth), 3×(Carl>Beth>Andy). No first-round majority (Andy 4, Beth 3, Carl 4), so plurality-with-runoff (run as IRV; identical for three candidates) deletes BETH — and Carl beats Andy 7–4. Carl is the WORST outcome for the four Andy>Beth>Carl voters, and Beth is the Condorcet winner (beats Andy 6–5, Carl 7–4), so this race also exhibits the Condorcet winner paradox. Part 2 (BV2151): two of the Andy voters stay home and their side does BETTER — the No-Show paradox.
Live results: https://bettervoting.com/dxg8pb/results

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
4:Andy>Beth>Carl
3:Beth>Carl>Andy
1:Carl>Andy>Beth
3:Carl>Beth>Andy
```

## What the engine says

Full report from the [`_tabulated` mirror](../felsenthal_paradoxes_tabulated/bv2150_dxg8pb_irv_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- RCV / Instant-Runoff Voting (single winner) ---
  Felsenthal Ex.4 full electorate — Runoff/IRV: their worst choice wins
 Tabulating 11 ballots (ranked ballots).

ROUND 1
Candidate      Votes  Status
-----------  -------  --------
Carl               4  Hopeful
Andy               4  Hopeful
Beth               3  Rejected

FINAL RESULT
Candidate      Votes  Status
-----------  -------  --------
Carl               7  Elected
Andy               4  Rejected
Beth               0  Rejected


Winner(s) — RCV / Instant-Runoff Voting (single winner)
  Carl
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/felsenthal_paradoxes/bv2150_dxg8pb_irv.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README.md)
- [Runoff reversal (worked set)](../../../01_STAR/runoff_overturns_leader/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [bv2144_mxfmhm_plurality](bv2144_mxfmhm_plurality.md) · [bv2144_mxfmhm_star](bv2144_mxfmhm_star.md) · [bv2145_6fj2kg_irv](bv2145_6fj2kg_irv.md) · [bv2145_6fj2kg_ranked_robin](bv2145_6fj2kg_ranked_robin.md) · [bv2145_6fj2kg_star](bv2145_6fj2kg_star.md) · [bv2146_krk2px_irv](bv2146_krk2px_irv.md) · [bv2146_krk2px_ranked_robin](bv2146_krk2px_ranked_robin.md) · [bv2146_krk2px_star](bv2146_krk2px_star.md) · [bv2147_9gdrqg_irv](bv2147_9gdrqg_irv.md) · [bv2147_9gdrqg_star](bv2147_9gdrqg_star.md) · [bv2148_h87k6v_irv](bv2148_h87k6v_irv.md) · [bv2148_h87k6v_star](bv2148_h87k6v_star.md) · [bv2149_byk9v2_irv](bv2149_byk9v2_irv.md) · [bv2149_byk9v2_star](bv2149_byk9v2_star.md) · [bv2150_dxg8pb_ranked_robin](bv2150_dxg8pb_ranked_robin.md) · [bv2150_dxg8pb_star](bv2150_dxg8pb_star.md) · [bv2151_97hbpw_irv](bv2151_97hbpw_irv.md) · [bv2151_97hbpw_ranked_robin](bv2151_97hbpw_ranked_robin.md) · [bv2151_97hbpw_star](bv2151_97hbpw_star.md)
