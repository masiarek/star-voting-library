---
search:
  exclude: true
---

# Block approval voting — uncap the marks and the sweep reverses

*Generated from [`mmp_block_approval.yaml`](../mmp_block_approval.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Approval Voting](../../../../04_Approval/01_Learn/README.md) · **3 seats** · **Expected winners:** Dev, Enzo, Finn

**Official tie-break (lot) order:** Alma > Bram > Cleo > Dev > Enzo > Finn > Gus > Hugo > Iris — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

The same 9 voters as mmp_minority_sweep.yaml, with one rule changed: no cap on
how many candidates a voter may mark.

Under the 3-mark cap the two independent voters spend everything on Gus, Hugo
and Iris, and never get to say that they prefer Pine to Oak. Uncapped, they say
it: they approve their three independents AND the Pine slate. Nothing about
their opinion changed — only how much of it the ballot could hold.

That single extra sentence moves Dev, Enzo and Finn from 3 to 5 and hands Pine
all three seats. Oak's 4 marks are unchanged; Oak simply stops being the
largest number on the page.

The lesson is not "approval is better" — block approval is still a majoritarian
at-large method that can hand one bloc every seat, which is exactly what it does
here. The lesson is that in this family the WINNER IS AN ARTIFACT OF THE CAP.
Same voters, same opinions, three different answers: capped at 3 → Oak sweeps;
uncapped → Pine sweeps; capped at 3 but run in two rounds → Pine sweeps
(mmp_majority_block_runoff.yaml). For proportionality you need a different
count, not a different mark limit — see STAR-PR or STV.

Shrunk from the "Block approval voting" column of Wikipedia's block voting table
(10,000 voters, 12 candidates).

## Ballots

Row 1 = candidate names; each later row is one voter's approvals (`1` = approve, `0`/blank = not approved).

```text
Alma,Bram,Cleo,Dev,Enzo,Finn,Gus,Hugo,Iris
1,1,1,0,0,0,0,0,0   # Oak voter — approves the Oak slate only
1,1,1,0,0,0,0,0,0   # Oak voter
1,1,1,0,0,0,0,0,0   # Oak voter
1,1,1,0,0,0,0,0,0   # Oak voter
0,0,0,1,1,1,0,0,0   # Pine voter — approves the Pine slate only
0,0,0,1,1,1,0,0,0   # Pine voter
0,0,0,1,1,1,0,0,0   # Pine voter
0,0,0,1,1,1,1,1,1   # independent voter — independents AND Pine
0,0,0,1,1,1,1,1,1   # independent voter
```

## What the engine says

Full report from the [`_tabulated` mirror](../cases_tabulated/mmp_block_approval_tabulated.txt) (regenerated on every run; every analysis forced on):

<!-- --8<-- [start:report] -->
```text
--- Approval Voting (3 winners) ---
 Tabulating 9 ballots (any non-zero score = approval).

Ballots:
   columns = Alma, Bram, Cleo, Dev, Enzo, Finn, Gus, Hugo, Iris      (1 = approve; 0 = not approved)
     4 × 1,1,1,0,0,0,0,0,0
     3 × 0,0,0,1,1,1,0,0,0
     2 × 0,0,0,1,1,1,1,1,1

   Dev  -- 5 (56%) -- Elected
   Enzo -- 5 (56%) -- Elected
   Finn -- 5 (56%) -- Elected
   Alma -- 4 (44%)
   Bram -- 4 (44%)
   Cleo -- 4 (44%)
   Gus  -- 2 (22%)
   Hugo -- 2 (22%)
   Iris -- 2 (22%)

[Approval Distribution] (how many candidates each ballot approved)
   33 approvals across 9 ballots — average 3.7 of 9 (range 3–6).
     approved 3: 7 ballots
     approved 6: 2 ballots

[Co-Approval Matrix]
 Of the voters who approved the ROW candidate, the % who ALSO approved the COLUMN candidate.
         |  Dev   |  Enzo  |  Finn  |  Alma  |  Bram  |  Cleo  |  Gus   |  Hugo  |  Iris  |
   ----------------------------------------------------------------------------------------
   Dev   |   --   |  100%  |  100%  |   0%   |   0%   |   0%   |  40%   |  40%   |  40%   |
   Enzo  |  100%  |   --   |  100%  |   0%   |   0%   |   0%   |  40%   |  40%   |  40%   |
   Finn  |  100%  |  100%  |   --   |   0%   |   0%   |   0%   |  40%   |  40%   |  40%   |
   Alma  |   0%   |   0%   |   0%   |   --   |  100%  |  100%  |   0%   |   0%   |   0%   |
   Bram  |   0%   |   0%   |   0%   |  100%  |   --   |  100%  |   0%   |   0%   |   0%   |
   Cleo  |   0%   |   0%   |   0%   |  100%  |  100%  |   --   |   0%   |   0%   |   0%   |
   Gus   |  100%  |  100%  |  100%  |   0%   |   0%   |   0%   |   --   |  100%  |  100%  |
   Hugo  |  100%  |  100%  |  100%  |   0%   |   0%   |   0%   |  100%  |   --   |  100%  |
   Iris  |  100%  |  100%  |  100%  |   0%   |   0%   |   0%   |  100%  |  100%  |   --   |

Winners — Approval Voting (3 winners)
  Dev, Enzo, Finn
```
<!-- --8<-- [end:report] -->

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/multi_member_plurality/cases/mmp_block_approval.yaml
```

## See also

- [Runoff reversal (worked set)](../../../../01_STAR/02_Examples/runoff_overturns_leader/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [mmp_block_voting](mmp_block_voting.md) · [mmp_limited_voting](mmp_limited_voting.md) · [mmp_majority_block_runoff](mmp_majority_block_runoff.md) · [mmp_majority_ceiling](mmp_majority_ceiling.md) · [mmp_minority_sweep](mmp_minority_sweep.md) · [mmp_sntv](mmp_sntv.md) · [mmp_sweep_floor](mmp_sweep_floor.md)
