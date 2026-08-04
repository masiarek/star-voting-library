---
search:
  exclude: true
---

# BV parity — Plurality (choose-one): most first-marks wins

*Generated from [`BV_Library_plurality_single_winner.yaml`](../BV_Library_plurality_single_winner.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [plurality](../../../../07_Concepts) · **1 seat** · **Expected winner:** Dave

## Scenario

Ported from BetterVoting's tabulator unit tests (Plurality.test.ts :: "Single Winner Test").
Choose-one ballots (a single 1 per voter); Dave has the most and wins. The original
had three spoiled/invalid ballots — one abstention, two out-of-bounds marks, and one
overvote — which BetterVoting counts as zero support; here the abstention is written
as blanks and the invalid rows as all-zero so the file validates while preserving the
winner. This engine tabulates choose-one 0/1 ballots via its STAR path, which for
single-mark ballots is equivalent to a plurality count.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

Markers on these ballots: `-` blank · `~` race abstention · `&` candidate abstention · `?` spoiled · `%` spoiled+reissued — all tabulate as 0 (reported honestly).

```text
Alice,Bob,Carol,Dave
0,1,0,0
0,1,0,0
0,0,1,0
0,0,1,0
0,0,1,0
0,0,0,1
0,0,0,1
0,0,0,1
0,0,0,1
0,0,0,1
-,-,-,-
0,0,0,0
0,0,0,0
0,0,0,0
```

## What the engine says

Full report from the [`_tabulated` mirror](../cases_tabulated/BV_Library_plurality_single_winner_tabulated.txt) (regenerated on every run; every analysis forced on):

<!-- --8<-- [start:report] -->
```text
--- Choose-One / Plurality Voting Method (single winner) ---
 Tabulating 14 ballots.

                   Alice   Bob   Carol   Dave 
                     -      X      -      -   
                     -      X      -      -   
                     -      -      X      -   
                     -      -      X      -   
                     -      -      X      -   
                     -      -      -      X   
                     -      -      -      X   
                     -      -      -      X   
                     -      -      -      X   
                     -      -      -      X   
                     -      -      -      -   
                     -      -      -      -   
                     -      -      -      -   
                     -      -      -      -   

  Count the marks:  Dave 5 · Carol 3 · Bob 2 · Alice 0
  (4 ballot(s) marked nobody.)

Winner — Choose-One / Plurality Voting Method (single winner)
 Dave   (5 of 14 marks)
```
<!-- --8<-- [end:report] -->

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/BV_Library/cases/BV_Library_plurality_single_winner.yaml
```

## See also

- [Ballot & terminology basics](../../../../07_Concepts/topics/ballot_and_terminology_basics.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [BV_Library_approval_single_winner](BV_Library_approval_single_winner.md) · [BV_Library_ranked_robin_single_winner](BV_Library_ranked_robin_single_winner.md) · [BV_Library_ranked_robin_ties](BV_Library_ranked_robin_ties.md) · [BV_Library_star_condorcet_winner](BV_Library_star_condorcet_winner.md) · [BV_Library_star_pr_basic_two_seats](BV_Library_star_pr_basic_two_seats.md) · [BV_Library_star_pr_fractional_surplus](BV_Library_star_pr_fractional_surplus.md) · [BV_Library_star_pr_voters_fewer_than_seats](BV_Library_star_pr_voters_fewer_than_seats.md) · [BV_Library_star_runnerup_tie](BV_Library_star_runnerup_tie.md) · [BV_Library_star_runoff](BV_Library_star_runoff.md) · [BV_Library_star_runoff_score_tie_five_star](BV_Library_star_runoff_score_tie_five_star.md) · [BV_Library_star_runoff_tie_score_resolves](BV_Library_star_runoff_tie_score_resolves.md)
