---
search:
  exclude: true
---

# Zero support — nobody scored anybody (Approval)

*Generated from [`zero_support_approval.yaml`](../zero_support_approval.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Approval Voting](../../../../04_Approval/01_Learn/README.md) · **1 seat** · **Expected winner:** Ada

**Official tie-break (lot) order:** Ada > Ben > Cleo > Dev > Elsa — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

Five nominees, three voters, and every single score is 0.

This is the degenerate limit of a tie: not "the ballots point two ways" but
"the ballots point nowhere at all". Every candidate has the same total (0),
every head-to-head is Equal Support 0-0, and every rung above the lot has
nothing to count — so whichever method is asked, the answer comes from the
published lot order and not from a vote.

It is a real shape, not only a thought experiment. A committee ballot that
goes out with five names nobody has heard of comes back like this; so does a
race where the electorate deliberately withholds support. What the file is
for is checking that the engine says so OUT LOUD rather than reporting a
winner as though somebody had chosen one.

Same three ballots are counted six ways in this folder — see the README for
what each method does with them, and which of the six admits the lot decided.

## Ballots

Row 1 = candidate names; each later row is one voter's approvals (`1` = approve, `0`/blank = not approved).

```text
Ada,Ben,Cleo,Dev,Elsa
0,0,0,0,0   # voter 1 — turned out, then scored every nominee 0
0,0,0,0,0   # voter 2 — a deliberate 0 is not a blank ballot
0,0,0,0,0   # voter 3 — the third ballot says the same thing
```

## What the engine says

Full report from the [`_tabulated` mirror](../cases_tabulated/zero_support_approval_tabulated.txt) (regenerated on every run; every analysis forced on):

<!-- --8<-- [start:report] -->
```text
--- Approval Voting (single winner) ---
 Tabulating 3 ballots (any non-zero score = approval).
 Abstentions: 3 of 3 ballots approved no one (0 ballots cast an approval).

Ballots:
   columns = Ada, Ben, Cleo, Dev, Elsa      (1 = approve; 0 = not approved)
     3 × 0,0,0,0,0

   Ada  -- 0 (0%) -- Elected
   Ben  -- 0 (0%)
   Cleo -- 0 (0%)
   Dev  -- 0 (0%)
   Elsa -- 0 (0%)
  Note: Ada, Ben, Cleo, Dev, Elsa each have 0 approvals and tie for the last 1 seat.
        Candidate priority order (Ada > Ben > Cleo > Dev > Elsa) broke the tie: Ada elected, Ben, Cleo, Dev, Elsa not elected.

[Approval Distribution] (how many candidates each ballot approved)
   0 approvals across 3 ballots — average 0.0 of 5 (range 0–0).
     approved none: 3 ballots

[Co-Approval Matrix]
 Of the voters who approved the ROW candidate, the % who ALSO approved the COLUMN candidate.
         |  Ada   |  Ben   |  Cleo  |  Dev   |  Elsa  |
   ----------------------------------------------------
   Ada   |   --   |   ·    |   ·    |   ·    |   ·    |
   Ben   |   ·    |   --   |   ·    |   ·    |   ·    |
   Cleo  |   ·    |   ·    |   --   |   ·    |   ·    |
   Dev   |   ·    |   ·    |   ·    |   --   |   ·    |
   Elsa  |   ·    |   ·    |   ·    |   ·    |   --   |

Winner — Approval Voting (single winner)
  Ada
```
<!-- --8<-- [end:report] -->

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/zero_support_election/cases/zero_support_approval.yaml
```

## See also

- [Ties & tie-breaking (topic hub)](../../../../07_Concepts/topics/ties/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [one_point_bloc_star](one_point_bloc_star.md) · [zero_support_bloc_star](zero_support_bloc_star.md) · [zero_support_plurality](zero_support_plurality.md) · [zero_support_ranked_robin](zero_support_ranked_robin.md) · [zero_support_star](zero_support_star.md) · [zero_support_star_pr](zero_support_star_pr.md)
