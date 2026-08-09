---
search:
  exclude: true
---

# Co-op board — Yes/No approval ballot (same nine voters)

*Generated from [`coop_board_approval.yaml`](../coop_board_approval.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Approval Voting](../../../../04_Approval/01_Learn/README.md) · **3 seats** · **Expected winners:** Chris, Dana, Ella

## Scenario

The APPROVAL half of the matched pair. Same nine co-op members, same
opinions as coop_board_scores_allocated.yaml -- projected onto a Yes/No
ballot by a stated rule: APPROVE IFF SCORE >= 3.

The threshold is a choice, and it is the whole experiment. State it, and
read the result as evidence about this projection rather than about
approval voting in general.

Approval counts: Chris 9, Dana 5, Ella 5, Ben 4, Amy 2.

The LH engine counts this file as BLOC approval (top-N by approvals). The
PROPORTIONAL approval rules -- seq-Phragmen, PAV, seqPAV -- are not in the
LH engine; run them with the abcvoting wrapper:

  .venv/bin/python 06_Other/abcvoting_tabulation_engine/abc_tabulation.py \
    method_comparisons/proportional_ballots/cases/coop_board_approval.yaml

All four approval rules agree here: Chris, Dana, Ella. The score ballot's
two proportional tabulations both say Ben, Chris, Dana.

## Ballots

Row 1 = candidate names; each later row is one voter's approvals (`1` = approve, `0`/blank = not approved).

```text
Amy,Ben,Chris,Dana,Ella
1,0,1,1,1      # Member 1 — scored 5,1,3,3,4
0,0,1,1,0      # Member 2 — scored 2,2,4,3,0
0,1,1,0,1      # Member 3 — scored 0,4,4,2,3
0,1,1,1,1      # Member 4 — scored 1,3,4,4,4
1,0,1,0,1      # Member 5 — scored 5,2,5,2,5
0,0,1,0,0      # Member 6 — scored 1,2,4,0,0
0,0,1,1,0      # Member 7 — scored 1,2,5,4,2
0,1,1,0,1      # Member 8 — scored 2,5,4,0,4
0,1,1,1,0      # Member 9 — scored 1,3,3,5,0
```

## What the engine says

Full report from the [`_tabulated` mirror](../cases_tabulated/coop_board_approval_tabulated.txt) (regenerated on every run; every analysis forced on):

<!-- --8<-- [start:report] -->
```text
--- Approval Voting (3 winners) ---
 Tabulating 9 ballots (any non-zero score = approval).

Ballots:
   columns = Amy, Ben, Chris, Dana, Ella      (1 = approve; 0 = not approved)
     1 × 1,0,1,1,1
     2 × 0,0,1,1,0
     2 × 0,1,1,0,1
     1 × 0,1,1,1,1
     1 × 1,0,1,0,1
     1 × 0,0,1,0,0
     1 × 0,1,1,1,0

   Chris -- 9 (100%) -- Elected
   Dana  -- 5 (56%) -- Elected
   Ella  -- 5 (56%) -- Elected
   Ben   -- 4 (44%)
   Amy   -- 2 (22%)

[Approval Distribution] (how many candidates each ballot approved)
   25 approvals across 9 ballots — average 2.8 of 5 (range 1–4).
     approved 1: 1 ballot
     approved 2: 2 ballots
     approved 3: 4 ballots
     approved 4: 2 ballots

[Co-Approval Matrix]
 Of the voters who approved the ROW candidate, the % who ALSO approved the COLUMN candidate.
          | Chris  |  Dana  |  Ella  |  Ben   |  Amy   |
   -----------------------------------------------------
   Chris  |   --   |  56%   |  56%   |  44%   |  22%   |
   Dana   |  100%  |   --   |  40%   |  40%   |  20%   |
   Ella   |  100%  |  40%   |   --   |  60%   |  40%   |
   Ben    |  100%  |  50%   |  75%   |   --   |   0%   |
   Amy    |  100%  |  50%   |  100%  |   0%   |   --   |

Winners — Approval Voting (3 winners)
  Chris, Dana, Ella
```
<!-- --8<-- [end:report] -->

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/proportional_ballots/cases/coop_board_approval.yaml
```

## See also

- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [coop_board_scores_allocated](coop_board_scores_allocated.md) · [coop_board_scores_sss](coop_board_scores_sss.md)
