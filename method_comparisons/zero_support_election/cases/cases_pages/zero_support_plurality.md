---
search:
  exclude: true
---

# Zero support — nobody scored anybody (Plurality)

*Generated from [`zero_support_plurality.yaml`](../zero_support_plurality.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [plurality](../../../../07_Concepts/README.md) · **1 seat** · **Expected winner:** Ada

**Official tie-break (lot) order:** Ada > Ben > Cleo > Dev > Elsa — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

Five nominees, three voters, and every single score is 0.

This is the degenerate limit of a tie: not "the ballots point two ways" but
"the ballots point nowhere at all". Every candidate has the same total (0),
every head-to-head is Equal Support 0-0, and every rung above the lot has
nothing to count — so whichever method is asked, the answer comes from the
published lot order and not from a vote.

It is a real shape, not only a thought experiment. A committee ballot that
goes out with five names nobody has heard of comes back like this; so does a
race where the electorate deliberately withholds support. What the file is
for is checking that the engine says so OUT LOUD rather than reporting a
winner as though somebody had chosen one.

Same three ballots are counted six ways in this folder — see the README for
what each method does with them, and which of the six admits the lot decided.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Ada,Ben,Cleo,Dev,Elsa
0,0,0,0,0   # voter 1 — turned out, then scored every nominee 0
0,0,0,0,0   # voter 2 — a deliberate 0 is not a blank ballot
0,0,0,0,0   # voter 3 — the third ballot says the same thing
```

## What the engine says

Full report from the [`_tabulated` mirror](../cases_tabulated/zero_support_plurality_tabulated.txt) (regenerated on every run; every analysis forced on):

<!-- --8<-- [start:report] -->
```text
--- Choose-One / Plurality Voting Method (single winner) ---
 Tabulating 3 ballots.

                                                     Ada    Ben    Cleo   Dev    Elsa 
  voter 1 — turned out, then scored every nominee 0   -      -      -      -      -   
  voter 2 — a deliberate 0 is not a blank ballot      -      -      -      -      -   
  voter 3 — the third ballot says the same thing      -      -      -      -      -   

  Count the marks:  Ada 0 · Ben 0 · Cleo 0 · Dev 0 · Elsa 0
  (3 ballot(s) marked nobody.)

 A 5-way tie for first: Ada, Ben, Cleo, Dev, Elsa — 0 mark(s) each.
   Counting the marks is all a choose-one ballot can do, so the ballots cannot break it;
   the pre-published lot order decides: ['Ada', 'Ben', 'Cleo', 'Dev', 'Elsa'].

[Lot-decided tie — rare]
  ⚠ The result here was set by lot, not by the votes.

Winner — Choose-One / Plurality Voting Method (single winner)
 Ada   (0 of 3 marks, by lot)
```
<!-- --8<-- [end:report] -->

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/zero_support_election/cases/zero_support_plurality.yaml
```

## See also

- [Ties & tie-breaking (topic hub)](../../../../07_Concepts/topics/ties/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [zero_support_approval](zero_support_approval.md) · [zero_support_bloc_star](zero_support_bloc_star.md) · [zero_support_ranked_robin](zero_support_ranked_robin.md) · [zero_support_star](zero_support_star.md) · [zero_support_star_pr](zero_support_star_pr.md)
