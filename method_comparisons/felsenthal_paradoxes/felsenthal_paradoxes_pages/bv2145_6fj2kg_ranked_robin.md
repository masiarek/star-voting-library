# Felsenthal Ex.2 — Ranked Robin: the Condorcet winner survives

*Generated from [`bv2145_6fj2kg_ranked_robin.yaml`](../bv2145_6fj2kg_ranked_robin.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../00_start_here/RCV_Ranked_Robin) · **1 seat** · **Expected winner:** Ada

## Scenario

Race 2 of 3 in the Felsenthal runoff-paradoxes election, part 1 of 2 (BV2145, bvid 6fj2kg; BV-confirmed). Source: Dan S. Felsenthal (2010), Appendix A2, Example 2 — see bv2145_6fj2kg_irv.yaml for the full citation and setup.
The same 17 ranked ballots counted by Ranked Robin (Copeland): Ada wins both her head-to-heads (Ben 9–8, Cleo 9–8) — 2 pairwise wins, the Condorcet winner, elected directly. What the runoff procedure's elimination order threw away, the round-robin count keeps.
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

Full report from the [`_tabulated` mirror](../felsenthal_paradoxes_tabulated/bv2145_6fj2kg_ranked_robin_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Ranked Robin (RCV-RR / Copeland) Method (single winner) ---
 Tabulating 17 ballots (ranked ballots).

Ballots:
     3 × Ada > Ben > Cleo
     2 × Ada > Cleo > Ben
     4 × Ben > Ada > Cleo
     2 × Ben > Cleo > Ada
     4 × Cleo > Ada > Ben
     2 × Cleo > Ben > Ada

Round-Robin — every pair, head-to-head (For – Against):
   Ada   beats Ben    9 – 8
   Ada   beats Cleo   9 – 8
   Ben   beats Cleo   9 – 8

--- Pairwise (Round-Robin) Matrix ---
Head-to-head / pairwise comparison — the Ranked Robin tally
Legend: For - Equal Support - Against   (row vs column)
         |    Ada    |   Ben    |  Cleo    |
--------------------------------------------
   Ada > |    ---    |9 - 0 - 8 |9 - 0 - 8 |
   Ben > | 8 - 0 - 9 |   ---    |9 - 0 - 8 |
  Cleo > | 8 - 0 - 9 |8 - 0 - 9 |   ---    |

Win–loss record — Copeland score = wins + ½·ties (most wins wins; ties broken by total margin, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  Ada        2–0–0         2      +2  Ben, Cleo
    2  Ben        1–1–0         1      +0  Cleo
    3  Cleo       0–2–0         0      -2  —

Winner — Ranked Robin (RCV-RR): Ada
   beats every opponent head-to-head — the Condorcet winner.
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/felsenthal_paradoxes/bv2145_6fj2kg_ranked_robin.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README.md)
- [Runoff reversal (worked set)](../../../01_STAR/runoff_overturns_leader/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [bv2144_mxfmhm_plurality](bv2144_mxfmhm_plurality.md) · [bv2144_mxfmhm_star](bv2144_mxfmhm_star.md) · [bv2145_6fj2kg_irv](bv2145_6fj2kg_irv.md) · [bv2145_6fj2kg_star](bv2145_6fj2kg_star.md) · [bv2146_krk2px_irv](bv2146_krk2px_irv.md) · [bv2146_krk2px_ranked_robin](bv2146_krk2px_ranked_robin.md) · [bv2146_krk2px_star](bv2146_krk2px_star.md) · [bv2147_9gdrqg_irv](bv2147_9gdrqg_irv.md) · [bv2147_9gdrqg_star](bv2147_9gdrqg_star.md) · [bv2148_h87k6v_irv](bv2148_h87k6v_irv.md) · [bv2148_h87k6v_star](bv2148_h87k6v_star.md) · [bv2149_byk9v2_irv](bv2149_byk9v2_irv.md) · [bv2149_byk9v2_star](bv2149_byk9v2_star.md) · [bv2150_dxg8pb_irv](bv2150_dxg8pb_irv.md) · [bv2150_dxg8pb_ranked_robin](bv2150_dxg8pb_ranked_robin.md) · [bv2150_dxg8pb_star](bv2150_dxg8pb_star.md) · [bv2151_97hbpw_irv](bv2151_97hbpw_irv.md) · [bv2151_97hbpw_ranked_robin](bv2151_97hbpw_ranked_robin.md) · [bv2151_97hbpw_star](bv2151_97hbpw_star.md)
