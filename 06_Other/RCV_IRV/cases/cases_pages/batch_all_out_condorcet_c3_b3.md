---
search:
  exclude: true
---

# Batch elimination empties the field — with a Condorcet winner sitting there

*Generated from [`batch_all_out_condorcet_c3_b3.yaml`](../batch_all_out_condorcet_c3_b3.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [RCV-IRV (Instant Runoff)](../../concepts/README.md) · **1 seat** · **Expected winner:** Amy

## Scenario

The same three voters and the same three candidates as the cycle case
(batch_all_out_cycle_c3_b3), with ONE ballot changed: the second voter now says
Bruno>Amy>Clara instead of Bruno>Clara>Amy. That single swap breaks the cycle
and hands the election an undisputed Condorcet winner — Amy beats Bruno 2-1 and
beats Clara 2-1, so she is preferred head-to-head to everyone.
It changes nothing about the instant-runoff count. First choices are still Amy
1, Bruno 1, Clara 1; nobody has a majority; all three are still tied for fewest.
Batch elimination removes the whole field again and reports a THREE-WAY TIE — in
an election that has a clear winner by every pairwise measure.
That is the price of the convention, and it is worth paying attention to,
because the usual defence of the total batch does not apply here. In the cycle
case a three-way tie is the only answer an anonymous, neutral rule CAN give: the
profile is symmetric, so there is nothing to separate the candidates with. This
profile is not symmetric. Ranked Robin elects Amy. Coombs elects Amy — its
elimination rule reads the BOTTOM of the ballot, where Clara has 2 last-place
votes to Bruno's 1 and Amy's 0, so Coombs cuts exactly one candidate and the
count proceeds normally. A fair rule can absolutely name a winner here. Batch
IRV declines to.
Verified with pref_voting (Holliday & Pacuit): instant_runoff = {Amy, Bruno,
Clara}, coombs = {Amy}, copeland = {Amy}.
Lesson: 07_Concepts/topics/ties/batch_elimination.md

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
Amy>Bruno>Clara
Bruno>Amy>Clara
Clara>Amy>Bruno
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
--- RCV / Instant-Runoff Voting (single winner) ---
  Batch elimination empties the field — with a Condorcet winner sitting there
 Tabulating 3 ballots (ranked ballots).

ROUND 1
Candidate      Votes  Status
-----------  -------  --------
Amy                1  Hopeful
Bruno              1  Hopeful
Clara              1  Rejected

FINAL RESULT
Candidate      Votes  Status
-----------  -------  --------
Amy                2  Elected
Bruno              1  Rejected
Clara              0  Rejected


Winner(s) — RCV / Instant-Runoff Voting (single winner)
  Amy
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Smith Set (the generalized Condorcet winner) ---
The smallest group whose every member beats every candidate outside it —
the honest answer to "who is even in contention?".
   Smith set (1 of 3): Amy
   Outside (2):        Bruno, Clara
   One member ⇒ Amy is the Condorcet winner, beating every rival head-to-head.
   RCV-IRV winner Amy is INSIDE the Smith set. ✓
      Not guaranteed — RCV-IRV is not Smith-efficient — but it holds here.
   More: 07_Concepts/topics/smith_set.md
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/batch_all_out_condorcet_c3_b3_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 06_Other/RCV_IRV/cases/batch_all_out_condorcet_c3_b3.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../07_Concepts/topics/condorcet/README.md)
- [Ties & tie-breaking (topic hub)](../../../../07_Concepts/topics/ties/README.md)
- [Runoff reversal (worked set)](../../../../01_STAR/02_Examples/runoff_overturns_leader/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [RCV_ballot_example](RCV_ballot_example.md) · [batch_all_out_cycle_c3_b3](batch_all_out_cycle_c3_b3.md) · [batch_all_out_round2_c4_b6](batch_all_out_round2_c4_b6.md) · [put_two_universes_c3_b4](put_two_universes_c3_b4.md) · [street_trees_five_rounds_c6_b100](street_trees_five_rounds_c6_b100.md)
