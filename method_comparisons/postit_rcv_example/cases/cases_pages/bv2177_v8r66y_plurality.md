---
search:
  exclude: true
---

# The Post-it election, seven ways — Choose-One: Purple on 7 first choices

*Generated from [`bv2177_v8r66y_plurality.yaml`](../bv2177_v8r66y_plurality.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [plurality](../../../../07_Concepts/README.md) · **1 seat** · **Expected winner:** Purple

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/v8r66y) · **[results ↗](https://bettervoting.com/v8r66y/results)** (election `v8r66y` · test `BV2177`).

## Scenario

One of seven races in the Post-it seven-ways election (BV2177, bvid v8r66y;
BV-confirmed) — the BV2176 electorate from Equal Vote's video "Updated: How
does RCV work? — With Post-its!" (https://youtu.be/Vte4nly_Neg), run through
every method BetterVoting supports. This race keeps only each voter's first
choice: Purple 7, Green 6, Blue 4, Pink 3 — Purple wins with 35% of the
vote, seeing nothing of the 13 voters who put Purple last-or-unranked.
Identical to RCV-IRV's round 1 (and RCV-IRV lands on Purple here too, so on
this electorate the "instant runoff" changed nothing about the winner —
only about the margin story). See the fairness lesson page:
postit_video_fair_and_balanced.md.

Live results: https://bettervoting.com/v8r66y/results
Companion races: BV2176's bv2176_p8dp28_star.yaml / _irv.yaml /
_ranked_robin.yaml (identical ballots to the BV2177 STAR/IRV/RR/STV races)
and bv2177_v8r66y_approval.yaml.
Overview page: bv2177_v8r66y_seven_methods.md

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Purple,Green,Blue,Pink
1,0,0,0
1,0,0,0
1,0,0,0
1,0,0,0
1,0,0,0
1,0,0,0
1,0,0,0
0,1,0,0
0,1,0,0
0,1,0,0
0,1,0,0
0,1,0,0
0,1,0,0
0,0,1,0
0,0,1,0
0,0,1,0
0,0,1,0
0,0,0,1
0,0,0,1
0,0,0,1
```

## What the engine says

Full report from the [`_tabulated` mirror](../cases_tabulated/bv2177_v8r66y_plurality_tabulated.txt) (regenerated on every run; every analysis forced on):

<!-- --8<-- [start:report] -->
```text
--- Choose-One / Plurality Voting Method (single winner) ---
 Tabulating 20 ballots.

                   Purple  Green   Blue   Pink 
                     X       -      -      -   
                     X       -      -      -   
                     X       -      -      -   
                     X       -      -      -   
                     X       -      -      -   
                     X       -      -      -   
                     X       -      -      -   
                     -       X      -      -   
                     -       X      -      -   
                     -       X      -      -   
                     -       X      -      -   
                     -       X      -      -   
                     -       X      -      -   
                     -       -      X      -   
                     -       -      X      -   
                     -       -      X      -   
                     -       -      X      -   
                     -       -      -      X   
                     -       -      -      X   
                     -       -      -      X   

  Count the marks:  Purple 7 · Green 6 · Blue 4 · Pink 3

Winner — Choose-One / Plurality Voting Method (single winner)
 Purple   (7 of 20 marks)
```
<!-- --8<-- [end:report] -->

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/postit_rcv_example/cases/bv2177_v8r66y_plurality.yaml
```

## See also

- [Runoff reversal (worked set)](../../../../01_STAR/02_Examples/runoff_overturns_leader/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [bv2176_p8dp28_irv](bv2176_p8dp28_irv.md) · [bv2176_p8dp28_ranked_robin](bv2176_p8dp28_ranked_robin.md) · [bv2176_p8dp28_star](bv2176_p8dp28_star.md) · [bv2177_v8r66y_approval](bv2177_v8r66y_approval.md) · [bv2178_8kg698_irv](bv2178_8kg698_irv.md) · [bv2178_8kg698_ranked_robin](bv2178_8kg698_ranked_robin.md) · [bv2178_8kg698_star](bv2178_8kg698_star.md)
