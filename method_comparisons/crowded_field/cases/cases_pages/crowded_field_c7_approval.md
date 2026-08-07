---
search:
  exclude: true
---

# Crowded field, rung 7 — 7 candidates, 65 voters, counted by Approval

*Generated from [`crowded_field_c7_approval.yaml`](../crowded_field_c7_approval.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Approval Voting](../../../../04_Approval/01_Learn/README.md) · **1 seat** · **Expected winner:** Felix

**Official tie-break (lot) order:** Ana > Bruno > Clara > Diego > Elsa > Felix > Greta — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

RUNG 3, counted by Approval. Felix wins on 36 while the Condorcet winner Diego takes
22 — third from last, on the same fixed approve-at-4 rule that elected him at both
earlier rungs.

Diego's collapse is the crowded-field effect in a form all its own. He is nearly
everyone's second or third choice, but a wider field pushes each bloc's approval line
past him: the blocs at 12 and 16 now have Clara, Elsa or Felix sitting where Diego used
to be on their ballot. Approval reads where you drew the line, not whom you preferred.

Same caveat as rung 2, doubled — quote this column only with the cutoff attached.

Same 65 voters and the same fixed candidate positions as crowded_field_c7_star.yaml;
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
Count:Ana,Bruno,Clara,Diego,Elsa,Felix,Greta
6:1,1,0,0,0,0,0    # bloc at 0
10:1,1,1,0,0,0,0    # bloc at 4
13:0,1,1,1,0,0,0    # bloc at 8
9:0,0,1,1,1,1,0    # bloc at 12
12:0,0,0,0,1,1,0    # bloc at 16
8:0,0,0,0,1,1,1    # bloc at 20
7:0,0,0,0,0,1,1    # bloc at 24
```

## What the engine says

Full report from the [`_tabulated` mirror](../cases_tabulated/crowded_field_c7_approval_tabulated.txt) (regenerated on every run; every analysis forced on):

<!-- --8<-- [start:report] -->
```text
--- Approval Voting (single winner) ---
 Tabulating 65 ballots (any non-zero score = approval).

Ballots:
   columns = Ana, Bruno, Clara, Diego, Elsa, Felix, Greta      (1 = approve; 0 / blank / marker = not approved)
     6 × 1,1,0,0,0,0,0
    10 × 1,1,1,0,0,0,0
    13 × 0,1,1,1,0,0,0
     9 × 0,0,1,1,1,1,0
    12 × 0,0,0,0,1,1,0
     8 × 0,0,0,0,1,1,1
     7 × 0,0,0,0,0,1,1

   Felix -- 36 (55%) -- Elected
   Clara -- 32 (49%)
   Bruno -- 29 (45%)
   Elsa  -- 29 (45%)
   Diego -- 22 (34%)
   Ana   -- 16 (25%)
   Greta -- 15 (23%)

[Approval Distribution] (how many candidates each ballot approved)
   179 approvals across 65 ballots — average 2.8 of 7 (range 2–4).
     approved 2: 25 ballots
     approved 3: 31 ballots
     approved 4: 9 ballots

[Co-Approval Matrix]
 Of the voters who approved the ROW candidate, the % who ALSO approved the COLUMN candidate.
          | Felix  | Clara  | Bruno  |  Elsa  | Diego  |  Ana   | Greta  |
   -----------------------------------------------------------------------
   Felix  |   --   |  25%   |   0%   |  81%   |  25%   |   0%   |  42%   |
   Clara  |  28%   |   --   |  72%   |  28%   |  69%   |  31%   |   0%   |
   Bruno  |   0%   |  79%   |   --   |   0%   |  45%   |  55%   |   0%   |
   Elsa   |  100%  |  31%   |   0%   |   --   |  31%   |   0%   |  28%   |
   Diego  |  41%   |  100%  |  59%   |  41%   |   --   |   0%   |   0%   |
   Ana    |   0%   |  62%   |  100%  |   0%   |   0%   |   --   |   0%   |
   Greta  |  100%  |   0%   |   0%   |  53%   |   0%   |   0%   |   --   |

Winner — Approval Voting (single winner)
  Felix
```
<!-- --8<-- [end:report] -->

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/crowded_field/cases/crowded_field_c7_approval.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../07_Concepts/topics/condorcet/README.md)
- [Ties & tie-breaking (topic hub)](../../../../07_Concepts/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [crowded_field_c3_approval](crowded_field_c3_approval.md) · [crowded_field_c3_irv](crowded_field_c3_irv.md) · [crowded_field_c3_ranked_robin](crowded_field_c3_ranked_robin.md) · [crowded_field_c3_star](crowded_field_c3_star.md) · [crowded_field_c5_approval](crowded_field_c5_approval.md) · [crowded_field_c5_irv](crowded_field_c5_irv.md) · [crowded_field_c5_ranked_robin](crowded_field_c5_ranked_robin.md) · [crowded_field_c5_star](crowded_field_c5_star.md) · [crowded_field_c7_irv](crowded_field_c7_irv.md) · [crowded_field_c7_ranked_robin](crowded_field_c7_ranked_robin.md) · [crowded_field_c7_star](crowded_field_c7_star.md)
