---
search:
  exclude: true
---

# The field empties in round two — and Pareto is what keeps Dev out of the tie

*Generated from [`batch_all_out_round2_c4_b6.yaml`](../batch_all_out_round2_c4_b6.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [RCV-IRV (Instant Runoff)](../../concepts/README.md) · **1 seat** · **Expected winner:** Alex

## Scenario

A total batch elimination is not a round-one curiosity. Six voters, four
candidates: Alex, Bella and Colin rotate the top three between them, two voters
each, and every single ballot ranks Dev dead last.
Round 1 is ordinary. Alex 2, Bella 2, Colin 2, Dev 0 — Dev is the unique fewest,
so he is eliminated on his own, and because nobody ranked him first there is
nothing to transfer. Round 2 is where it stops: Alex 2, Bella 2, Colin 2,
majority is 4 of 6, nobody has it, and all three remaining candidates are tied
for fewest first choices. Batch elimination removes the entire remaining field,
and the count ends with all three tied for the win.
Dev is not in that tie, and the reason is worth naming: every voter prefers all
three others to Dev, so PARETO excludes him. That is precisely the role Pareto
plays in Moulin's forced-tie proposition — anonymity and neutrality force a tie
among the symmetric candidates, and Pareto is what stops a universally-rejected
candidate from being swept into it. See
07_Concepts/topics/ties/ties_are_forced.md.
Verified with pref_voting (Holliday & Pacuit): instant_runoff = {Alex, Bella,
Colin}, coombs = {Alex, Bella, Colin}, copeland = {Alex, Bella, Colin}. Coombs
lands in the same place by the mirror route — Dev carries all 6 last-place votes
and goes first, after which Alex, Bella and Colin have 2 apiece and tie.
This engine does not print those rounds. The vendored pyrankvote collapses the
whole thing into ONE round — it rejects Colin and Dev side by side, even though
Colin was tied at the top of the remaining field and Dev was alone at the bottom
— and elects Alex 4-2. So the round-2 structure described above is the METHOD's;
read it off pref_voting, not off the report below. expected_winners records what
this engine prints for this row order, not the method's answer.
Lesson: 07_Concepts/topics/ties/batch_elimination.md

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
Alex>Bella>Colin>Dev
Alex>Bella>Colin>Dev
Bella>Colin>Alex>Dev
Bella>Colin>Alex>Dev
Colin>Alex>Bella>Dev
Colin>Alex>Bella>Dev
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
--- RCV / Instant-Runoff Voting (single winner) ---
  The field empties in round two — and Pareto is what keeps Dev out of the tie
 Tabulating 6 ballots (ranked ballots).

ROUND 1
Candidate      Votes  Status
-----------  -------  --------
Alex               2  Hopeful
Bella              2  Hopeful
Colin              2  Rejected
Dev                0  Rejected

FINAL RESULT
Candidate      Votes  Status
-----------  -------  --------
Alex               4  Elected
Bella              2  Rejected
Colin              0  Rejected
Dev                0  Rejected


Winner(s) — RCV / Instant-Runoff Voting (single winner)
  Alex
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Smith Set (the generalized Condorcet winner) ---
The smallest group whose every member beats every candidate outside it —
the honest answer to "who is even in contention?".
   Smith set (3 of 4): Alex, Bella, Colin
   Outside (1):        Dev
   More than one member ⇒ NO Condorcet winner: the top of the tournament is a
   cycle, so the strongest "candidate" is a set, not a person. Which member of
   the set should win is exactly what Minimax / Ranked Pairs / Schulze disagree
   about — see 05_Ranked_Robin/01_Learn/cycle_resolution.md.
   RCV-IRV winner Alex is INSIDE the Smith set. ✓
      Not guaranteed — RCV-IRV is not Smith-efficient — but it holds here.
   More: 07_Concepts/topics/smith_set.md
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/batch_all_out_round2_c4_b6_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 06_Other/RCV_IRV/cases/batch_all_out_round2_c4_b6.yaml
```

## See also

- [Ties & tie-breaking (topic hub)](../../../../07_Concepts/topics/ties/README.md)
- [Runoff reversal (worked set)](../../../../01_STAR/02_Examples/runoff_overturns_leader/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [RCV_ballot_example](RCV_ballot_example.md) · [batch_all_out_condorcet_c3_b3](batch_all_out_condorcet_c3_b3.md) · [batch_all_out_cycle_c3_b3](batch_all_out_cycle_c3_b3.md) · [put_two_universes_c3_b4](put_two_universes_c3_b4.md) · [street_trees_five_rounds_c6_b100](street_trees_five_rounds_c6_b100.md)
