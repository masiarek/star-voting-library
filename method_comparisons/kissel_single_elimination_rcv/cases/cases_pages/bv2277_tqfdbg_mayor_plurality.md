---
search:
  exclude: true
---

# BV2277 — The mayor's race (Choose-One): Ada wins on 33%

*Generated from [`bv2277_tqfdbg_mayor_plurality.yaml`](../bv2277_tqfdbg_mayor_plurality.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [plurality](../../../../07_Concepts/README.md) · **1 seat** · **Expected winner:** Ada

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/tqfdbg) · **[results ↗](https://bettervoting.com/tqfdbg/results)** (election `tqfdbg` · test `BV2277`).

## Scenario

The Choose-One (Plurality) race of BV2277 (BetterVoting election tqfdbg) — the same 100-voter mayor's race as the IRV, Ranked Robin and STAR races, with every voter marking only their first choice. Ada wins with 33 of 100, the largest pile and nowhere near a majority. She also LOSES head-to-head to two of the three people she just beat: Cora 67-33 and Blake 67-33. This is the baseline the other three races are measured against — and the reason a jurisdiction goes looking for a better count in the first place. Adam Kissel's "single-elimination RCV" is one such attempt; it improves on this (it elects Blake, who at least beats Ada head-to-head) but still misses Cora, the candidate who beats everyone. Live results: https://bettervoting.com/tqfdbg/results

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:Ada,Blake,Cora,Dean
33:1,0,0,0     # Ada's voters
31:0,1,0,0     # Blake's voters
20:0,0,1,0     # the moderates
16:0,0,0,1     # Dean's voters
```

## What the engine says

Full report from the [`_tabulated` mirror](../cases_tabulated/bv2277_tqfdbg_mayor_plurality_tabulated.txt) (regenerated on every run; every analysis forced on):

<!-- --8<-- [start:report] -->
```text
--- Choose-One / Plurality Voting Method (single winner) ---
 Tabulating 100 ballots.

                    Ada   Blake   Cora   Dean 
  33 ×               X      -      -      -   
  31 ×               -      X      -      -   
  20 ×               -      -      X      -   
  16 ×               -      -      -      X   

  Count the marks:  Ada 33 · Blake 31 · Cora 20 · Dean 16

Winner — Choose-One / Plurality Voting Method (single winner)
 Ada   (33 of 100 marks)
```
<!-- --8<-- [end:report] -->

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/kissel_single_elimination_rcv/cases/bv2277_tqfdbg_mayor_plurality.yaml
```

## See also

- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [bv2277_tqfdbg_mayor_irv](bv2277_tqfdbg_mayor_irv.md) · [bv2277_tqfdbg_mayor_rr](bv2277_tqfdbg_mayor_rr.md) · [bv2277_tqfdbg_mayor_star](bv2277_tqfdbg_mayor_star.md) · [bv2278_8cdkkc_five_way_irv](bv2278_8cdkkc_five_way_irv.md) · [bv2278_8cdkkc_five_way_plurality](bv2278_8cdkkc_five_way_plurality.md) · [bv2278_8cdkkc_five_way_rr](bv2278_8cdkkc_five_way_rr.md) · [bv2278_8cdkkc_five_way_star](bv2278_8cdkkc_five_way_star.md)
