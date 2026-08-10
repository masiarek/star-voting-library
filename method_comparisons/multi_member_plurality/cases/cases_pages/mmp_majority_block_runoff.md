---
search:
  exclude: true
---

# Majority block voting (round 2) — the runoff hands every seat to the runner-up

*Generated from [`mmp_majority_block_runoff.yaml`](../mmp_majority_block_runoff.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [plurality](../../../../07_Concepts/README.md) · **3 seats** · **Expected winners:** Dev, Enzo, Finn

**Official tie-break (lot) order:** Alma > Bram > Cleo > Dev > Enzo > Finn — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

ROUND 2 of the two-round method, on the same 9 voters as mmp_minority_sweep.yaml.

Majority block voting is plurality block voting with a majority requirement: a
candidate must clear half the voters, and if the seats aren't filled the trailing
candidates are dropped and the survivors are re-run. Round 1 IS
mmp_minority_sweep.yaml — Alma, Bram and Cleo lead on 4 votes each, but 5 of 9
is a majority, so nobody is elected. Gus, Hugo and Iris finish last on 2 and are
eliminated, leaving the two slates to contest the runoff.

Now the two independent voters have to choose between Oak and Pine, and they
prefer Pine. Their three marks move across: Dev, Enzo and Finn go from 3 to 5 —
a real majority of the 9 voters — and Pine takes all three seats.

So the two rounds give OPPOSITE clean sweeps from an unchanged electorate. Round
1's leader is not merely reduced to two seats or one; it is shut out entirely.
Both answers are defensible readings of the same ballots — Oak really did have
the most first-choice support, and Pine really was preferred by a majority —
which is the honest summary of the whole family: the count is doing the deciding.

Note the winners here reach 5 of 9 (56%) rather than the round-1 ceiling. That
ceiling is real and worth knowing before reading any block-vote percentage —
see mmp_majority_ceiling.yaml.

Shrunk from the "Majority block voting / 2 round voting" columns of Wikipedia's
block voting table (10,000 voters, 12 candidates).

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Alma,Bram,Cleo,Dev,Enzo,Finn
1,1,1,0,0,0   # Oak voter — unchanged from round 1
1,1,1,0,0,0   # Oak voter
1,1,1,0,0,0   # Oak voter
1,1,1,0,0,0   # Oak voter
0,0,0,1,1,1   # Pine voter — unchanged from round 1
0,0,0,1,1,1   # Pine voter
0,0,0,1,1,1   # Pine voter
0,0,0,1,1,1   # independent voter — their eliminated favourites freed these marks
0,0,0,1,1,1   # independent voter
```

## What the engine says

Full report from the [`_tabulated` mirror](../cases_tabulated/mmp_majority_block_runoff_tabulated.txt) (regenerated on every run; every analysis forced on):

<!-- --8<-- [start:report] -->
```text
--- Block Voting (plurality-at-large) — 3 winners ---
 Tabulating 9 ballots (3 votes/voter).

Votes (most votes fill the seats):
   Dev      5  <- Elected
   Enzo     5  <- Elected
   Finn     5  <- Elected
   Alma     4
   Bram     4
   Cleo     4

Winners — Block Voting (plurality-at-large), 3 seats:
   1. Dev   (5 votes)
   2. Enzo   (5 votes)
   3. Finn   (5 votes)
```
<!-- --8<-- [end:report] -->

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/multi_member_plurality/cases/mmp_majority_block_runoff.yaml
```

## See also

- [Runoff reversal (worked set)](../../../../01_STAR/02_Examples/runoff_overturns_leader/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [mmp_block_approval](mmp_block_approval.md) · [mmp_block_voting](mmp_block_voting.md) · [mmp_limited_voting](mmp_limited_voting.md) · [mmp_majority_ceiling](mmp_majority_ceiling.md) · [mmp_minority_sweep](mmp_minority_sweep.md) · [mmp_sntv](mmp_sntv.md) · [mmp_sweep_floor](mmp_sweep_floor.md)
