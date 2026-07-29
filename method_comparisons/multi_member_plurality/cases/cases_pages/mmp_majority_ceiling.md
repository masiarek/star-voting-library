# Block Voting (3 seats): the majority ceiling — a unanimous candidate holds only 33%

*Generated from [`mmp_majority_ceiling.yaml`](../mmp_majority_ceiling.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [plurality](../../../../07_Concepts) · **3 seats** · **Expected winners:** Alice, Bruno, Cleo

**Official tie-break (lot) order:** Alice > Bruno > Cleo > Dev > Esme — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../../01_STAR/concepts/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

Why "the winner got less than half the votes" cannot be read as vote splitting
in a MULTI-SEAT choose-one race — the arithmetic forbids it.

30 voters, 3 seats, 5 candidates. Each voter marks 3 names (Block Voting), so
90 votes are cast in total. Alice is on EVERY single ballot — literal
unanimity, the most consensus a candidate can possibly have.

And Alice's share of votes cast is 30 / 90 = 33.3%.

With k marks per voter the total is k x voters, so no candidate can exceed
1/k of votes cast no matter how popular: 33% at 3 seats, 25% at 4, 9% at 11.
A screening rule that flags every race whose leader is under 50% therefore
flags 100% of multi-seat block-vote races — including unanimous ones. That is
a denominator artifact, not evidence of a split.

This does NOT clear Block Voting. Its real defect is the opposite one: a
bare majority sweeps every seat (see mmp_block_voting.yaml, 60/40 -> 3-0).
The point is narrower and cuts both ways — the sub-majority test is blind
here, missing the actual pathology while flagging consensus as a failure.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Alice,Bruno,Cleo,Dev,Esme
12: 1,1,1,0,0
10: 1,1,0,1,0
8:  1,0,1,0,1
```

## What the engine says

Full report from the [`_tabulated` mirror](../cases_tabulated/mmp_majority_ceiling_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Block Voting (plurality-at-large) — 3 winners ---
 Tabulating 30 ballots (3 votes/voter).

Votes (most votes fill the seats):
   Alice    30  <- Elected
   Bruno    22  <- Elected
   Cleo     20  <- Elected
   Dev      10
   Esme      8

Winners — Block Voting (plurality-at-large), 3 seats:
   1. Alice   (30 votes)
   2. Bruno   (22 votes)
   3. Cleo   (20 votes)
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/multi_member_plurality/cases/mmp_majority_ceiling.yaml
```

## See also

- [Vote splitting (worked set)](../../../split_voting/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [mmp_block_voting](mmp_block_voting.md) · [mmp_limited_voting](mmp_limited_voting.md) · [mmp_sntv](mmp_sntv.md)
