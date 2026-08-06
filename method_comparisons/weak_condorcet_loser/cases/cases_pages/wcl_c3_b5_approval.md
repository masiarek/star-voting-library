---
search:
  exclude: true
---

# Weak Condorcet loser — the same five voters, on Approval ballots

*Generated from [`wcl_c3_b5_approval.yaml`](../wcl_c3_b5_approval.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Approval Voting](../../../../04_Approval/01_Learn/README.md) · **1 seat** · **Expected winner:** Ben

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/c73pfw) · **[results ↗](https://bettervoting.com/c73pfw/results)** (election `c73pfw` · test `BV2249`).

## Scenario

The Approval companion to wcl_c3_b5_star.yaml. Same five voters, same
underlying opinions, rendered onto a yes/no ballot by approving every
candidate the voter scored 3 or higher on the 0-5 ballot:

  5,4,4 -> 1,1,1     5,4,1 -> 1,1,0     5,4,3 -> 1,1,1
  0,3,4 -> 0,1,1     0,3,4 -> 0,1,1

Approval counts: Ben 5, Cora 4, Ada 3. Approval elects Ben — the same weak
Condorcet loser STAR elected, and by a wide margin rather than a tiebreak.

Two things worth separating, because they are easy to run together:

1. WHERE THE PAIRWISE FACTS COME FROM. Ben's status as a weak Condorcet loser
   is a fact about these voters' PREFERENCES, which live on the score ballots
   (Ada beats Ben 3-2, Ada beats Cora 3-2, Ben ties Cora 2-2). It is not
   derived from the approval ballots.

2. THE APPROVAL BALLOT CANNOT SEE IT. Run the pairwise comparison on the
   APPROVAL ballots alone and Ben beats Ada 2-0 — because three voters
   approved both, and approval records that as a tie. Coarsening 0-5 down to
   0-1 destroyed the very margins that made Ada the Condorcet winner. The
   ballot cannot represent the situation it is failing.

That second point is the real lesson, and it is a preference-vs-support point,
not a scoreboard point: a two-level ballot has no way to say "Ada 5, Ben 4" —
both become "approved". So Approval does not so much CHOOSE the weak Condorcet
loser as lose the information that would have identified one.

The cutoff caveat applies as always: "approve everything 3 or higher" is one
modeling choice among several, and a different threshold gives a different
election. That is Approval's standing ambiguity, not a quirk of this case.

## Ballots

Row 1 = candidate names; each later row is one voter's approvals (`1` = approve, `0`/blank = not approved).

```text
Ada,Ben,Cora
1,1,1   # scored 5,4,4 -> approves all three
1,1,0   # scored 5,4,1 -> Cora falls below the cutoff
1,1,1   # scored 5,4,3 -> approves all three
0,1,1   # scored 0,3,4 -> rejects Ada
0,1,1   # scored 0,3,4 -> rejects Ada
```

## What the engine says

Full report from the [`_tabulated` mirror](../cases_tabulated/wcl_c3_b5_approval_tabulated.txt) (regenerated on every run; every analysis forced on):

<!-- --8<-- [start:report] -->
```text
--- Approval Voting (single winner) ---
 Tabulating 5 ballots (any non-zero score = approval).

Ballots:
   columns = Ada, Ben, Cora      (1 = approve; 0 / blank / marker = not approved)
     2 × 1,1,1
     1 × 1,1,0
     2 × 0,1,1

   Ben  -- 5 (100%) -- Elected
   Cora -- 4 (80%)
   Ada  -- 3 (60%)

[Approval Distribution] (how many candidates each ballot approved)
   12 approvals across 5 ballots — average 2.4 of 3 (range 2–3).
     approved 2: 3 ballots
     approved 3: 2 ballots

[Co-Approval Matrix]
 Of the voters who approved the ROW candidate, the % who ALSO approved the COLUMN candidate.
         |  Ben   |  Cora  |  Ada   |
   ----------------------------------
   Ben   |   --   |  80%   |  60%   |
   Cora  |  100%  |   --   |  50%   |
   Ada   |  100%  |  67%   |   --   |

Winner — Approval Voting (single winner)
  Ben
```
<!-- --8<-- [end:report] -->

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/weak_condorcet_loser/cases/wcl_c3_b5_approval.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../07_Concepts/topics/condorcet/README.md)
- [Ties & tie-breaking (topic hub)](../../../../07_Concepts/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [wcl_c3_b5_star](wcl_c3_b5_star.md)
