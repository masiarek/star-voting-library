---
search:
  exclude: true
---

# BV2130 — Presidential Board: party alignment (Plurality)

*Generated from [`bv2130_bvhchj_party_plurality.yaml`](../bv2130_bvhchj_party_plurality.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [plurality](../../../../07_Concepts) · **1 seat** · **Expected winner:** Democrat

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/bvhchj) · **[results ↗](https://bettervoting.com/bvhchj/results)** (election `bvhchj` · test `BV2130`).

## Scenario

The second race of the Presidential Board election (BetterVoting bvhchj) — a choose-one Plurality poll of party alignment, alongside the 7-seat STAR-PR board race in the same election. 102 voters, 8 parties; Democrat leads with 39 first-choices and wins. Companion to bv2130_presidential_board_star_pr.yaml (the STAR-PR board seats). BV also elects Democrat. Live results: https://bettervoting.com/bvhchj/results

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Democrat,Republican,Libertarian,Green,Constitution,Socialism and Liberation,Solidarity,Independent
39: 1,0,0,0,0,0,0,0
15: 0,0,0,0,0,1,0,0
14: 0,0,0,0,0,0,0,1
11: 0,0,1,0,0,0,0,0
11: 0,0,0,1,0,0,0,0
7: 0,0,0,0,0,0,1,0
2: 0,1,0,0,0,0,0,0
2: 0,0,0,0,1,0,0,0
1: 0,0,0,0,0,0,0,0
```

## What the engine says

Full report from the [`_tabulated` mirror](../cases_tabulated/bv2130_bvhchj_party_plurality_tabulated.txt) (regenerated on every run; every analysis forced on):

<!-- --8<-- [start:report] -->
```text
--- Choose-One / Plurality Voting Method (single winner) ---
 Tabulating 102 ballots.

                   Democrat  Republican  Libertarian  Green  Constitution  Socialism and Liberation  Solidarity  Independent 
  39 ×                X          -            -         -         -                   -                  -            -      
  15 ×                -          -            -         -         -                   X                  -            -      
  14 ×                -          -            -         -         -                   -                  -            X      
  11 ×                -          -            X         -         -                   -                  -            -      
  11 ×                -          -            -         X         -                   -                  -            -      
  7 ×                 -          -            -         -         -                   -                  X            -      
  2 ×                 -          X            -         -         -                   -                  -            -      
  2 ×                 -          -            -         -         X                   -                  -            -      
  1 ×                 -          -            -         -         -                   -                  -            -      

  Count the marks:  Democrat 39 · Socialism and Liberation 15 · Independent 14 · Libertarian 11 · Green 11 · Solidarity 7 · Republican 2 · Constitution 2
  (1 ballot(s) marked nobody.)

Winner — Choose-One / Plurality Voting Method (single winner)
 Democrat   (39 of 102 marks)
```
<!-- --8<-- [end:report] -->

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 03_STAR_PR/02_Examples/cases/bv2130_bvhchj_party_plurality.yaml
```

## See also

- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [02a_c5_b63_proportional-allocated-score](02a_c5_b63_proportional-allocated-score.md) · [02b_c5_b63_proportional-sss](02b_c5_b63_proportional-sss.md) · [02c_c5_b63_proportional-rrv](02c_c5_b63_proportional-rrv.md) · [03b_star_pr_3seats](03b_star_pr_3seats.md) · [bv2130_presidential_board_star_pr](bv2130_presidential_board_star_pr.md) · [lackner_skowron_shadow_star_pr_c7_b12](lackner_skowron_shadow_star_pr_c7_b12.md) · [lackner_skowron_shadow_star_pr_rrv_c7_b12](lackner_skowron_shadow_star_pr_rrv_c7_b12.md) · [rrv_sample_c15_b13_three-parties](rrv_sample_c15_b13_three-parties.md)
