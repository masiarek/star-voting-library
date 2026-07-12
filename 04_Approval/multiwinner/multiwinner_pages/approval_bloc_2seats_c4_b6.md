# Bloc Approval — 2 seats, majority sweep

*Generated from [`approval_bloc_2seats_c4_b6.yaml`](../approval_bloc_2seats_c4_b6.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Approval Voting](../../../00_start_here/Approval_Voting) · **2 seats** · **Expected winners:** Amy, Ben

## Scenario

Multi-winner (bloc / at-large) Approval: same 0/1 ballot, but the TWO
most-approved candidates win. Six voters, four candidates, two seats.
A cohesive majority (4 of 6 voters — all approve Amy, two also Ben)
takes BOTH seats; the minority's candidates (Cora, Doug) win nothing.
Ben and Cora tie 2–2 for the last seat, and candidate priority order
(left-to-right columns) breaks it for Ben — watch the engine's tie
note. The lesson: bloc Approval is majoritarian, not proportional —
same trade-off as Bloc STAR (02_STAR_Bloc). Proportional rules on the
SAME ballots (SPAV, PAV, seq-Phragmén — run them via
06_Other/abcvoting_tabulation_engine/) instead elect Amy + Cora decisively,
giving the minority its seat; see
00_start_here/Approval_Voting/approval_multiwinner.md.

## Ballots

Row 1 = candidate names; each later row is one voter's approvals (`1` = approve, `0`/blank = not approved).

```text
Amy,Ben,Cora,Doug
1,0,0,0   # voter 1 — majority faction: bullet-approves Amy
1,1,0,0   # voter 2 — majority faction: Amy and Ben
1,1,0,0   # voter 3 — majority faction: Amy and Ben
1,0,0,0   # voter 4 — majority faction: bullet-approves Amy
0,0,1,1   # voter 5 — minority faction: Cora and Doug
0,0,1,0   # voter 6 — minority faction: bullet-approves Cora
```

## What the engine says

Full report from the [`_tabulated` mirror](../multiwinner_tabulated/approval_bloc_2seats_c4_b6_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Approval Voting (2 winners) ---
 Tabulating 6 ballots (any non-zero score = approval).

Ballots:
   columns = Amy, Ben, Cora, Doug      (1 = approve; 0 / blank / marker = not approved)
     2 × 1,0,0,0
     2 × 1,1,0,0
     1 × 0,0,1,1
     1 × 0,0,1,0

   Amy  -- 4 (67%) -- Elected
   Ben  -- 2 (33%) -- Elected
   Cora -- 2 (33%)
   Doug -- 1 (17%)
  Note: Ben, Cora each have 2 approvals and tie for the last 1 seat.
        Candidate priority order (Ben > Cora) broke the tie: Ben elected, Cora not elected.

[Approval Distribution] (how many candidates each ballot approved)
   9 approvals across 6 ballots — average 1.5 of 4 (range 1–2).
     approved 1: 3 ballots
     approved 2: 3 ballots

[Co-Approval Matrix]
 Of the voters who approved the ROW candidate, the % who ALSO approved the COLUMN candidate.
         |  Amy   |  Ben   |  Cora  |  Doug  |
   -------------------------------------------
   Amy   |   --   |  50%   |   0%   |   0%   |
   Ben   |  100%  |   --   |   0%   |   0%   |
   Cora  |   0%   |   0%   |   --   |  50%   |
   Doug  |   0%   |   0%   |  100%  |   --   |

Winners — Approval Voting (2 winners)
  Amy, Ben
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 04_Approval/multiwinner/approval_bloc_2seats_c4_b6.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Ties & tie-breaking (topic hub)](../../../00_start_here/topics/ties/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [approval_bloc_3seats_c6_b5](approval_bloc_3seats_c6_b5.md) · [approval_bloc_4seats_c7_b12_lackner_skowron](approval_bloc_4seats_c7_b12_lackner_skowron.md)
