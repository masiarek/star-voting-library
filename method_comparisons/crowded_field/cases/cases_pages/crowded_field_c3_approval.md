---
search:
  exclude: true
---

# Crowded field, rung 3 — 3 candidates, 65 voters, counted by Approval

*Generated from [`crowded_field_c3_approval.yaml`](../crowded_field_c3_approval.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Approval Voting](../../../../04_Approval/01_Learn/README.md) · **1 seat** · **Expected winner:** Diego

**Official tie-break (lot) order:** Ana > Diego > Greta — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

RUNG 1, counted by Approval — each bloc approves everyone it would have scored 4 or
5 on the STAR ballot for this rung. Diego wins with 44 approvals of 65. Every method at
this rung agrees.

Same 65 voters and the same fixed candidate positions as crowded_field_c3_star.yaml;
the approval ballot is that file's 0–5 ballot thresholded at 4 (approve everyone you
would score 4 or 5). Change the cutoff in build_ladder.py and this file changes with it.

Construction: build_ladder.py in this folder. 65 voters in seven blocs at 0, 4, 8, 12,
16, 20, 24 (sizes 6, 10, 13, 9, 12, 8, 7); candidates fixed at Ana 1 · Bruno 6 ·
Clara 9 · Diego 11 · Elsa 14 · Felix 16 · Greta 22; utility = minus distance; scores =
each bloc's own min-max scaling onto 0–5. Nothing is tuned, and no count at any rung is
settled by a tie-break.

## Ballots

Row 1 = candidate names; each later row is one voter's approvals (`1` = approve, `0`/blank = not approved).

```text
Count:Ana,Diego,Greta
6:1,0,0    # bloc at 0
10:1,1,0    # bloc at 4
13:0,1,0    # bloc at 8
9:0,1,0    # bloc at 12
12:0,1,1    # bloc at 16
8:0,0,1    # bloc at 20
7:0,0,1    # bloc at 24
```

## What the engine says

Full report from the [`_tabulated` mirror](../cases_tabulated/crowded_field_c3_approval_tabulated.txt) (regenerated on every run; every analysis forced on):

<!-- --8<-- [start:report] -->
```text
--- Approval Voting (single winner) ---
 Tabulating 65 ballots (any non-zero score = approval).

Ballots:
   columns = Ana, Diego, Greta      (1 = approve; 0 / blank / marker = not approved)
     6 × 1,0,0
    10 × 1,1,0
    22 × 0,1,0
    12 × 0,1,1
    15 × 0,0,1

   Diego -- 44 (68%) -- Elected
   Greta -- 27 (42%)
   Ana   -- 16 (25%)

[Approval Distribution] (how many candidates each ballot approved)
   87 approvals across 65 ballots — average 1.3 of 3 (range 1–2).
     approved 1: 43 ballots
     approved 2: 22 ballots

[Co-Approval Matrix]
 Of the voters who approved the ROW candidate, the % who ALSO approved the COLUMN candidate.
          | Diego  | Greta  |  Ana   |
   -----------------------------------
   Diego  |   --   |  27%   |  23%   |
   Greta  |  44%   |   --   |   0%   |
   Ana    |  62%   |   0%   |   --   |

Winner — Approval Voting (single winner)
  Diego
```
<!-- --8<-- [end:report] -->

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/crowded_field/cases/crowded_field_c3_approval.yaml
```

## See also

- [Ties & tie-breaking (topic hub)](../../../../07_Concepts/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [crowded_field_c3_irv](crowded_field_c3_irv.md) · [crowded_field_c3_ranked_robin](crowded_field_c3_ranked_robin.md) · [crowded_field_c3_star](crowded_field_c3_star.md) · [crowded_field_c5_approval](crowded_field_c5_approval.md) · [crowded_field_c5_irv](crowded_field_c5_irv.md) · [crowded_field_c5_ranked_robin](crowded_field_c5_ranked_robin.md) · [crowded_field_c5_star](crowded_field_c5_star.md) · [crowded_field_c7_approval](crowded_field_c7_approval.md) · [crowded_field_c7_irv](crowded_field_c7_irv.md) · [crowded_field_c7_ranked_robin](crowded_field_c7_ranked_robin.md) · [crowded_field_c7_star](crowded_field_c7_star.md)
