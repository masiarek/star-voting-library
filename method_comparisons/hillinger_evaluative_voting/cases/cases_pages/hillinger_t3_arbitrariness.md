---
search:
  exclude: true
---

# Hillinger Table 3 — one approval result, two opposite Borda winners

*Generated from [`hillinger_t3_arbitrariness.yaml`](../hillinger_t3_arbitrariness.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Approval Voting](../../../../04_Approval/01_Learn) · **1 seat** · **Expected winner:** Ada

## Scenario

Claude Hillinger, "Voting and the Cardinal Aggregation of Judgments" (Munich
Discussion Paper 2004-9), section 10, Table 3 — his answer to the
Saari-van Newenhizen (1988) criticism of Approval Voting.

SVN's argument: a voter with the strict preference a > b > c cannot express it
on an approval ballot. They must arbitrarily pick (1,0,0) or (1,1,0), and one
can construct profiles where that arbitrary choice decides the election. So
Approval - and, SVN generalize, cardinal voting at large - is indeterminate.

Hillinger's inversion: the argument only bites if the STRICT ORDERINGS are the
true preferences. Assume instead that the approval marks are what the voters
actually mean, and it is the rankings that become arbitrary - because a coarse
score under-determines the ranking in exactly the same way.

These are the seven approval ballots of his Table 3. Ada 5, Ben 2, Cora 4;
Ada wins. Now complete each ballot to a strict ranking. TWO completions are
consistent with these very marks:

  reading 1   3x Ada>Ben>Cora   2x Ben>Cora>Ada   2x Ada>Cora>Ben
              Borda: Ada 10, Ben 7, Cora 4   ->  ADA wins
  reading 2   3x Ada>Cora>Ben   2x Ben>Cora>Ada   2x Cora>Ada>Ben
              Borda: Ada  8, Ben 2, Cora 11  ->  CORA wins

Same ballots, same voters, opposite Borda winners. The ordinal formalism is as
under-determined by the marks as the marks are by the formalism - which is
Hillinger's point, and it is a genuine standoff rather than a refutation.

Teaching page: 04_Approval/01_Learn/approval_indeterminacy.md
Concept page:  07_Concepts/topics/cardinal_utility.md

## Ballots

Row 1 = candidate names; each later row is one voter's approvals (`1` = approve, `0`/blank = not approved).

```text
Ada,Ben,Cora
1,0,0    # approves Ada only
1,0,0    # approves Ada only
1,0,0    # approves Ada only
0,1,1    # approves Ben and Cora
0,1,1    # approves Ben and Cora
1,0,1    # approves Ada and Cora
1,0,1    # approves Ada and Cora
```

## What the engine says

Full report from the [`_tabulated` mirror](../cases_tabulated/hillinger_t3_arbitrariness_tabulated.txt) (regenerated on every run; every analysis forced on):

<!-- --8<-- [start:report] -->
```text
--- Approval Voting (single winner) ---
 Tabulating 7 ballots (any non-zero score = approval).

Ballots:
   columns = Ada, Ben, Cora      (1 = approve; 0 / blank / marker = not approved)
     3 × 1,0,0
     2 × 0,1,1
     2 × 1,0,1

   Ada  -- 5 (71%) -- Elected
   Cora -- 4 (57%)
   Ben  -- 2 (29%)

[Approval Distribution] (how many candidates each ballot approved)
   11 approvals across 7 ballots — average 1.6 of 3 (range 1–2).
     approved 1: 3 ballots
     approved 2: 4 ballots

[Co-Approval Matrix]
 Of the voters who approved the ROW candidate, the % who ALSO approved the COLUMN candidate.
         |  Ada   |  Cora  |  Ben   |
   ----------------------------------
   Ada   |   --   |  40%   |   0%   |
   Cora  |  50%   |   --   |  50%   |
   Ben   |   0%   |  100%  |   --   |

Winner — Approval Voting (single winner)
  Ada
```
<!-- --8<-- [end:report] -->

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/hillinger_evaluative_voting/cases/hillinger_t3_arbitrariness.yaml
```

## See also

- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [hillinger_t4_affine](hillinger_t4_affine.md) · [hillinger_t4_ev3](hillinger_t4_ev3.md)
