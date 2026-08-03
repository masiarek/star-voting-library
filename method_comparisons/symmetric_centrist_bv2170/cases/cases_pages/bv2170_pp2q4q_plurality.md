---
search:
  exclude: true
---

# Symmetric centrist (47/47/3/3) — Choose-One: the poles tie, the centrist gets 6

*Generated from [`bv2170_pp2q4q_plurality.yaml`](../bv2170_pp2q4q_plurality.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [plurality](../../../../07_Concepts) · **1 seat** · **Expected winner:** Blake

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/pp2q4q) · **[results ↗](https://bettervoting.com/pp2q4q/results)** (election `pp2q4q`).

**Official tie-break (lot) order:** Casey > Blake > Avery — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../../01_STAR/concepts/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

One of four races in the Symmetric Centrist election (BV2170, bvid pp2q4q; BV-confirmed). 100 voters, three candidates, ONE electorate tabulated four ways. Under Choose-One (Plurality) only first choices count: Avery 47, Blake 47, Casey 6. The centrist Condorcet winner finishes last on first choices, and the two poles tie 47–47.

Random tiebreak — NOT freezable. The 47–47 pole tie is exact (perfect symmetry), so BetterVoting breaks it at RANDOM; this run elected Blake (frozen in the export), but a re-tally could elect Avery. lot_numbers is pinned to BV's `perm` for this run so LH reproduces the frozen result; the winner here is a coin flip, not a property of the ballots.

Live results: https://bettervoting.com/pp2q4q/results
Companion races: bv2170_pp2q4q_star.yaml, bv2170_pp2q4q_irv.yaml, bv2170_pp2q4q_ranked_robin.yaml.
Overview page: bv2170_pp2q4q_symmetric_centrist.md

## Parameters (from the YAML)

```yaml
bv_test_id: BV2170
```

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:Avery,Blake,Casey
47:1,0,0
47:0,1,0
3:0,0,1
3:0,0,1
```

## What the engine says

Full report from the [`_tabulated` mirror](../cases_tabulated/bv2170_pp2q4q_plurality_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Choose-One / Plurality Voting Method (single winner) ---
 Tabulating 100 ballots.

                   Avery  Blake  Casey 
  47 ×               X      -      -   
  47 ×               -      X      -   
  6 ×                -      -      X   

  Count the marks:  Blake 47 · Avery 47 · Casey 6

 A 2-way tie for first: Blake, Avery — 47 mark(s) each.
   Counting the marks is all a choose-one ballot can do, so the ballots cannot break it;
   the pre-published lot order decides: ['Casey', 'Blake', 'Avery'].

[Lot-decided tie — rare]
  ⚠ The result here was set by lot, not by the votes.

Winner — Choose-One / Plurality Voting Method (single winner)
 Blake   (47 of 100 marks, by lot)
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/symmetric_centrist_bv2170/cases/bv2170_pp2q4q_plurality.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../07_Concepts/topics/condorcet/README.md)
- [Ties & tie-breaking (topic hub)](../../../../07_Concepts/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../../01_STAR/concepts/Tie_Breaking_STAR/tie_breaking.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [bv2170_pp2q4q_irv](bv2170_pp2q4q_irv.md) · [bv2170_pp2q4q_ranked_robin](bv2170_pp2q4q_ranked_robin.md) · [bv2170_pp2q4q_star](bv2170_pp2q4q_star.md)
