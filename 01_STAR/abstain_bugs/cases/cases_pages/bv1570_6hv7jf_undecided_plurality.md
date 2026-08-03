---
search:
  exclude: true
---

# BV1570 — undecided plurality election still declares a winner

*Generated from [`bv1570_6hv7jf_undecided_plurality.yaml`](../bv1570_6hv7jf_undecided_plurality.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [plurality](../../../../07_Concepts) · **1 seat** · **Expected winner:** Approve

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/6hv7jf) · **[results ↗](https://bettervoting.com/6hv7jf/results)** (election `6hv7jf`).

## Scenario

A Plurality ("choose one") race, two options, three voters, all "undecided":
one ballot deselects Approve (a `0`, then blank), one is fully blank, one
deselects Reject. Markers: `&` = the BetterVoting `null` (left blank).

**BetterVoting** counts all three as abstentions (nTallyVotes = 0), reports the
wrong voter count (the results view showed 2, not 3), and still declares a winner
(Approve) off zero tallied votes (bettervoting#894).

**LH diverges:** only the fully-blank ballot abstains. The two ballots that carry
an explicit `0` are real tally votes (both options score 0), so LH sees
nTallyVotes = 2, nAbstentions = 1, a 0-0 tie, resolved to Approve by lot. Same
winner, different count — LH counts an explicit 0 as a cast vote, per the #884
dispute.

## Parameters (from the YAML)

```yaml
bv_test_id: BV1570
```

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

Markers on these ballots: `-` blank · `~` race abstention · `&` candidate abstention · `?` spoiled · `%` spoiled+reissued — all tabulate as 0 (reported honestly).

```text
Approve,Reject
0,&
&,&
&,0
```

## What the engine says

Full report from the [`_tabulated` mirror](../cases_tabulated/bv1570_6hv7jf_undecided_plurality_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Choose-One / Plurality Voting Method (single winner) ---
 Tabulating 3 ballots.

                   Approve  Reject 
                      -       -    
                      -       -    
                      -       -    

  Count the marks:  Approve 0 · Reject 0
  (3 ballot(s) marked nobody.)

 A 2-way tie for first: Approve, Reject — 0 mark(s) each.
   Counting the marks is all a choose-one ballot can do, so the ballots cannot break it;
   the pre-published lot order decides: ['Approve', 'Reject'].

[Lot-decided tie — rare]
  ⚠ The result here was set by lot, not by the votes.

Winner — Choose-One / Plurality Voting Method (single winner)
 Approve   (0 of 3 marks, by lot)
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/abstain_bugs/cases/bv1570_6hv7jf_undecided_plurality.yaml
```

## See also

- [Ties & tie-breaking (topic hub)](../../../../07_Concepts/topics/ties/README.md)
- [Ballot & terminology basics](../../../../07_Concepts/topics/ballot_and_terminology_basics.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [bv11_6xhfp8_full_equal_support](bv11_6xhfp8_full_equal_support.md) · [bv655_jfrk9t_equal_opposition](bv655_jfrk9t_equal_opposition.md)
