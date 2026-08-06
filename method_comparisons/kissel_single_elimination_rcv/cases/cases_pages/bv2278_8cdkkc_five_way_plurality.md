---
search:
  exclude: true
---

# BV2278 — Kissel's five-way example (Choose-One): A wins on 30.6%

*Generated from [`bv2278_8cdkkc_five_way_plurality.yaml`](../bv2278_8cdkkc_five_way_plurality.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [plurality](../../../../07_Concepts/README.md) · **1 seat** · **Expected winner:** A

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/8cdkkc) · **[results ↗](https://bettervoting.com/8cdkkc/results)** (election `8cdkkc` · test `BV2278`).

## Scenario

The Choose-One (Plurality) race of BV2278 (BetterVoting election 8cdkkc) — the same 1000-voter field as the IRV, Ranked Robin and STAR races, with every voter marking only their first choice. A wins with 306, or 30.6%: the paper's own ">30%" line, and the number the whole example is built around. Nearly 70% of the electorate preferred someone else, and the candidate they actually agree on — C, the moderate who beats A 511-489 and B 700-300 — finishes THIRD here with 202. This race is why the paper is looking for a better count at all; the argument of the case is that the count it proposes (batch-eliminate to the top two) still lands on A. Live results: https://bettervoting.com/8cdkkc/results

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

Markers on these ballots: `-` blank · `~` race abstention · `&` candidate abstention · `?` spoiled · `%` spoiled+reissued — all tabulate as 0 (reported honestly).

```text
Count:A,B,C,D,E
306:1,0,0,0,0     # A-partisans
300:0,1,0,0,0     # B-partisans
111:0,0,1,0,0     # moderates leaning A
 91:0,0,1,0,0     # moderates leaning B
183:0,0,0,1,0     # D's voters
  9:0,0,0,0,1     # the <1% candidate
```

## What the engine says

Full report from the [`_tabulated` mirror](../cases_tabulated/bv2278_8cdkkc_five_way_plurality_tabulated.txt) (regenerated on every run; every analysis forced on):

<!-- --8<-- [start:report] -->
```text
--- Choose-One / Plurality Voting Method (single winner) ---
 Tabulating 1000 ballots.

                     A      B      C      D      E   
  306 ×              X      -      -      -      -   
  300 ×              -      X      -      -      -   
  202 ×              -      -      X      -      -   
  183 ×              -      -      -      X      -   
  9 ×                -      -      -      -      X   

  Count the marks:  A 306 · B 300 · C 202 · D 183 · E 9

Winner — Choose-One / Plurality Voting Method (single winner)
 A   (306 of 1000 marks)
```
<!-- --8<-- [end:report] -->

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/kissel_single_elimination_rcv/cases/bv2278_8cdkkc_five_way_plurality.yaml
```

## See also

- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [bv2277_tqfdbg_mayor_irv](bv2277_tqfdbg_mayor_irv.md) · [bv2277_tqfdbg_mayor_plurality](bv2277_tqfdbg_mayor_plurality.md) · [bv2277_tqfdbg_mayor_rr](bv2277_tqfdbg_mayor_rr.md) · [bv2277_tqfdbg_mayor_star](bv2277_tqfdbg_mayor_star.md) · [bv2278_8cdkkc_five_way_irv](bv2278_8cdkkc_five_way_irv.md) · [bv2278_8cdkkc_five_way_rr](bv2278_8cdkkc_five_way_rr.md) · [bv2278_8cdkkc_five_way_star](bv2278_8cdkkc_five_way_star.md)
