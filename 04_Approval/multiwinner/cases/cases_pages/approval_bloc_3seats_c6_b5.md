# Bloc Approval — 3-seat city council at-large

*Generated from [`approval_bloc_3seats_c6_b5.yaml`](../approval_bloc_3seats_c6_b5.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Approval Voting](../../../../00_start_here/Approval_Voting) · **3 seats** · **Expected winners:** Adams, Brown, Clark

## Scenario

A 3-seat at-large council race matching the multi-winner ballot mockup
(00_start_here/Approval_Voting/img/approval_ballot_multiwinner_3seats.png):
six candidates, five voters, each approving any number of candidates.
Sum the columns; the three most-approved win. Adams, Brown, and Clark
take the seats (3 approvals each) — no tie, no drama: the plain
"checklist ballot, add it up" mechanics of multi-winner Approval.
Companion cases: approval_bloc_2seats_c4_b6 (majority sweep + tie-break)
and approval_bloc_4seats_c7_b12_lackner_skowron (AV vs PAV on the
literature's running example).

## Ballots

Row 1 = candidate names; each later row is one voter's approvals (`1` = approve, `0`/blank = not approved).

```text
Adams,Brown,Clark,Davis,Evans,Foster
1,1,0,0,0,0   # voter 1 — Adams, Brown
0,1,1,1,0,0   # voter 2 — Brown, Clark, Davis
1,0,0,0,1,1   # voter 3 — Adams, Evans, Foster
1,1,1,0,0,0   # voter 4 — Adams, Brown, Clark
0,0,1,1,1,0   # voter 5 — Clark, Davis, Evans
```

## What the engine says

Full report from the [`_tabulated` mirror](../cases_tabulated/approval_bloc_3seats_c6_b5_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Approval Voting (3 winners) ---
 Tabulating 5 ballots (any non-zero score = approval).

Ballots:
   columns = Adams, Brown, Clark, Davis, Evans, Foster      (1 = approve; 0 / blank / marker = not approved)
     1 × 1,1,0,0,0,0
     1 × 0,1,1,1,0,0
     1 × 1,0,0,0,1,1
     1 × 1,1,1,0,0,0
     1 × 0,0,1,1,1,0

   Adams  -- 3 (60%) -- Elected
   Brown  -- 3 (60%) -- Elected
   Clark  -- 3 (60%) -- Elected
   Davis  -- 2 (40%)
   Evans  -- 2 (40%)
   Foster -- 1 (20%)

[Approval Distribution] (how many candidates each ballot approved)
   14 approvals across 5 ballots — average 2.8 of 6 (range 2–3).
     approved 2: 1 ballot
     approved 3: 4 ballots

[Co-Approval Matrix]
 Of the voters who approved the ROW candidate, the % who ALSO approved the COLUMN candidate.
           | Adams  | Brown  | Clark  | Davis  | Evans  | Foster |
   ---------------------------------------------------------------
   Adams   |   --   |  67%   |  33%   |   0%   |  33%   |  33%   |
   Brown   |  67%   |   --   |  67%   |  33%   |   0%   |   0%   |
   Clark   |  33%   |  67%   |   --   |  67%   |  33%   |   0%   |
   Davis   |   0%   |  50%   |  100%  |   --   |  50%   |   0%   |
   Evans   |  50%   |   0%   |  50%   |  50%   |   --   |  50%   |
   Foster  |  100%  |   0%   |   0%   |   0%   |  100%  |   --   |

Winners — Approval Voting (3 winners)
  Adams, Brown, Clark
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 04_Approval/multiwinner/cases/approval_bloc_3seats_c6_b5.yaml
```

## See also

- [Ties & tie-breaking (topic hub)](../../../../00_start_here/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [approval_bloc_2seats_c4_b6](approval_bloc_2seats_c4_b6.md) · [approval_bloc_4seats_c7_b12_lackner_skowron](approval_bloc_4seats_c7_b12_lackner_skowron.md)
