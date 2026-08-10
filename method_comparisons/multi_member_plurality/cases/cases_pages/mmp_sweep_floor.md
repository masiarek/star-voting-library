---
search:
  exclude: true
---

# Block voting — the smallest possible minority sweep (5 voters)

*Generated from [`mmp_sweep_floor.yaml`](../mmp_sweep_floor.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [plurality](../../../../07_Concepts/README.md) · **3 seats** · **Expected winners:** Nora, Omar, Priya

**Official tie-break (lot) order:** Nora > Omar > Priya > Quinn > Rosa > Theo — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

The floor case: the fewest ballots in which a minority can win every seat under
block voting. Five voters, three seats.

Two voters mark the full slate — Nora, Omar, Priya. The other three each mark
one name, and a different one: Quinn, Rosa, Theo. Every slate candidate finishes
on 2, every lone candidate on 1, and the slate takes all three seats on 40% of
the voters.

Five is the minimum. With four voters the slate bloc would need 2 of 4 to
out-poll each rival, which is half the electorate, not a minority; three
dissenters voting three different ways is the smallest opposition that is both
larger than the slate and unable to beat it anywhere.

Two things this case is NOT. It is not an argument that block voting usually
does this — it shows the shape of the failure at its smallest, the way a
two-candidate example shows vote splitting. And it is not about bullet voting
being a mistake: the three dissenters have no better move available. Each has
three marks and one candidate they like; spending the spare marks on someone
they don't want is how a voter defeats themselves. The corner they are in is
the method's, not theirs.

The full-size version of the same mechanism, with two organised parties and a
runoff: mmp_minority_sweep.yaml.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Nora,Omar,Priya,Quinn,Rosa,Theo
1,1,1,0,0,0   # slate voter — all three marks on the slate
1,1,1,0,0,0   # slate voter
0,0,0,1,0,0   # dissenter — one mark, for Quinn
0,0,0,0,1,0   # dissenter — one mark, for Rosa
0,0,0,0,0,1   # dissenter — one mark, for Theo
```

## What the engine says

Full report from the [`_tabulated` mirror](../cases_tabulated/mmp_sweep_floor_tabulated.txt) (regenerated on every run; every analysis forced on):

<!-- --8<-- [start:report] -->
```text
--- Multi-winner Plurality — 3 winners ---
 Tabulating 5 ballots (mixed votes/voter).

Votes (most votes fill the seats):
   Nora      2  <- Elected
   Omar      2  <- Elected
   Priya     2  <- Elected
   Quinn     1
   Rosa      1
   Theo      1

Winners — Multi-winner Plurality, 3 seats:
   1. Nora   (2 votes)
   2. Omar   (2 votes)
   3. Priya   (2 votes)
```
<!-- --8<-- [end:report] -->

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/multi_member_plurality/cases/mmp_sweep_floor.yaml
```

## See also

- [Vote splitting (worked set)](../../../split_voting/README.md)
- [Runoff reversal (worked set)](../../../../01_STAR/02_Examples/runoff_overturns_leader/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [mmp_block_approval](mmp_block_approval.md) · [mmp_block_voting](mmp_block_voting.md) · [mmp_limited_voting](mmp_limited_voting.md) · [mmp_majority_block_runoff](mmp_majority_block_runoff.md) · [mmp_majority_ceiling](mmp_majority_ceiling.md) · [mmp_minority_sweep](mmp_minority_sweep.md) · [mmp_sntv](mmp_sntv.md)
