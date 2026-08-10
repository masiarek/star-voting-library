---
search:
  exclude: true
---

# Plurality block voting — a 44% minority sweeps all three seats

*Generated from [`mmp_minority_sweep.yaml`](../mmp_minority_sweep.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [plurality](../../../../07_Concepts/README.md) · **3 seats** · **Expected winners:** Alma, Bram, Cleo

**Official tie-break (lot) order:** Alma > Bram > Cleo > Dev > Enzo > Finn > Gus > Hugo > Iris — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

The second electorate in this set (LH-only — see the folder README). Where
mmp_block_voting.yaml shows a 60% MAJORITY sweeping, this one shows the harder
version of the same defect: a faction that most voters voted against still
takes every seat.

9 voters, 3 seats, 9 candidates. Party Oak (Alma, Bram, Cleo) has 4 voters;
Party Pine (Dev, Enzo, Finn) has 3; two voters prefer the independents (Gus,
Hugo, Iris) and spend all three of their marks there. Block voting gives each
voter as many marks as there are seats, and every bloc votes its own slate, so
each candidate simply collects their own bloc: Oak 4, Pine 3, independents 2.

Oak sweeps 3-0 on 4 of 9 voters — 44%. The other 56% of the electorate elects
nobody, because it is split across two groups and neither one out-polls Oak on
its own. That is the whole mechanism: block voting rewards the largest bloc,
not the largest agreement, and the opposition's size is irrelevant unless it
concentrates.

This is also ROUND 1 of the two-round method — see mmp_majority_block_runoff.yaml,
where the same 9 voters reverse this result once the independents are dropped.
Uncapping the marks reverses it too: mmp_block_approval.yaml.

Shrunk from the 10,000-voter, 12-candidate table in Wikipedia's "Block voting"
article. Only the ORDER of the totals carries the lesson, so the electorate
rescales to the smallest integers that keep every inequality strict.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Alma,Bram,Cleo,Dev,Enzo,Finn,Gus,Hugo,Iris
1,1,1,0,0,0,0,0,0   # Oak voter — the full Oak slate
1,1,1,0,0,0,0,0,0   # Oak voter
1,1,1,0,0,0,0,0,0   # Oak voter
1,1,1,0,0,0,0,0,0   # Oak voter
0,0,0,1,1,1,0,0,0   # Pine voter — the full Pine slate
0,0,0,1,1,1,0,0,0   # Pine voter
0,0,0,1,1,1,0,0,0   # Pine voter
0,0,0,0,0,0,1,1,1   # independent voter — all three marks on the independents
0,0,0,0,0,0,1,1,1   # independent voter
```

## What the engine says

Full report from the [`_tabulated` mirror](../cases_tabulated/mmp_minority_sweep_tabulated.txt) (regenerated on every run; every analysis forced on):

<!-- --8<-- [start:report] -->
```text
--- Block Voting (plurality-at-large) — 3 winners ---
 Tabulating 9 ballots (3 votes/voter).

Votes (most votes fill the seats):
   Alma     4  <- Elected
   Bram     4  <- Elected
   Cleo     4  <- Elected
   Dev      3
   Enzo     3
   Finn     3
   Gus      2
   Hugo     2
   Iris     2

Winners — Block Voting (plurality-at-large), 3 seats:
   1. Alma   (4 votes)
   2. Bram   (4 votes)
   3. Cleo   (4 votes)
```
<!-- --8<-- [end:report] -->

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/multi_member_plurality/cases/mmp_minority_sweep.yaml
```

## See also

- [Vote splitting (worked set)](../../../split_voting/README.md)
- [Runoff reversal (worked set)](../../../../01_STAR/02_Examples/runoff_overturns_leader/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [mmp_block_approval](mmp_block_approval.md) · [mmp_block_voting](mmp_block_voting.md) · [mmp_limited_voting](mmp_limited_voting.md) · [mmp_majority_block_runoff](mmp_majority_block_runoff.md) · [mmp_majority_ceiling](mmp_majority_ceiling.md) · [mmp_sntv](mmp_sntv.md) · [mmp_sweep_floor](mmp_sweep_floor.md)
