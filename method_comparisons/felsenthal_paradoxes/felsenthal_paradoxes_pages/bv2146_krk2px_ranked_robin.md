# Felsenthal Ex.2 after the raise — Ranked Robin: unmoved, still Ada

*Generated from [`bv2146_krk2px_ranked_robin.yaml`](../bv2146_krk2px_ranked_robin.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../00_start_here/RCV_Ranked_Robin) · **1 seat** · **Expected winner:** Ada

## Scenario

Race 2 of 3 in the Felsenthal runoff-paradoxes election, part 2 of 2 (BV2146, bvid krk2px; BV-confirmed). Source: Dan S. Felsenthal (2010), Appendix A2, Example 2 (continued) — see bv2146_krk2px_irv.yaml for the setup.
The raise (2× Cleo>Ben>Ada → Ben>Cleo>Ada) only swaps Ben and Cleo on those ballots; Ada's position against each rival is untouched, so the pairwise table barely moves: Ada still beats Ben 9–8 and Cleo 9–8 and stays the Condorcet winner. Ranked Robin elects Ada before and after — monotone where the runoff procedure (the IRV race) flips.
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

Full report from the [`_tabulated` mirror](../felsenthal_paradoxes_tabulated/bv2146_krk2px_ranked_robin_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Ranked Robin (RCV-RR / Copeland) Method (single winner) ---
 Tabulating 17 ballots (ranked ballots).

Ballots:
     3 × Ada > Ben > Cleo
     2 × Ada > Cleo > Ben
     4 × Ben > Ada > Cleo
     4 × Ben > Cleo > Ada
     4 × Cleo > Ada > Ben

Round-Robin — every pair, head-to-head (For – Against):
   Ada   beats Ben     9 –  8
   Ada   beats Cleo    9 –  8
   Ben   beats Cleo   11 –  6

--- Pairwise (Round-Robin) Matrix ---
Head-to-head / pairwise comparison — the Ranked Robin tally
Legend: For - Equal Support - Against   (row vs column)
         |     Ada      |    Ben      |    Cleo     |
-----------------------------------------------------
   Ada > |     ---      | 9 -  0 -  8 | 9 -  0 -  8 |
   Ben > |  8 -  0 -  9 |    ---      |11 -  0 -  6 |
  Cleo > |  8 -  0 -  9 | 6 -  0 - 11 |    ---      |

Win–loss record — Copeland score = wins + ½·ties (most wins wins; ties broken by total margin, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  Ada        2–0–0         2      +2  Ben, Cleo
    2  Ben        1–1–0         1      +4  Cleo
    3  Cleo       0–2–0         0      -6  —

Winner — Ranked Robin (RCV-RR): Ada
   beats every opponent head-to-head — the Condorcet winner.
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/felsenthal_paradoxes/bv2146_krk2px_ranked_robin.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README.md)
- [Runoff reversal (worked set)](../../../01_STAR/runoff_overturns_leader/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [bv2144_mxfmhm_plurality](bv2144_mxfmhm_plurality.md) · [bv2144_mxfmhm_star](bv2144_mxfmhm_star.md) · [bv2145_6fj2kg_irv](bv2145_6fj2kg_irv.md) · [bv2145_6fj2kg_ranked_robin](bv2145_6fj2kg_ranked_robin.md) · [bv2145_6fj2kg_star](bv2145_6fj2kg_star.md) · [bv2146_krk2px_irv](bv2146_krk2px_irv.md) · [bv2146_krk2px_star](bv2146_krk2px_star.md)
