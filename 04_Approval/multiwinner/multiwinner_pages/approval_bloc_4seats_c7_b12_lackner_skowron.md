# Bloc Approval — Lackner & Skowron's running example (k=4)

*Generated from [`approval_bloc_4seats_c7_b12_lackner_skowron.yaml`](../approval_bloc_4seats_c7_b12_lackner_skowron.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Approval Voting](../../../00_start_here/Approval_Voting) · **4 seats** · **Expected winners:** A, B, C, D

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/jt6r76) · **[results ↗](https://bettervoting.com/jt6r76/results)** (election `jt6r76`).

## Scenario

The running example (Example 2.1) from Lackner & Skowron, "Multi-Winner
Voting with Approval Preferences" (SpringerBriefs, 2023, open access,
doi:10.1007/978-3-031-09016-5): an academic society elects a k=4
steering committee from seven candidates; 12 approval ballots:
3 x {A,B} . 3 x {A,C} . 2 x {A,D} . 1 x {B,C,F} . 1 x {E} . 1 x {F} . 1 x {G}.
Approval counts: A=8, B=4, C=4, D=2, E=1, F=2, G=1. Bloc Approval (AV)
seats A, B, C, then TIES D and F for the last seat (2-2) - this engine's
priority order breaks it for D. The book (Example 2.4) shows PAV instead
elects {A,B,C,F} outright, the tied committee that leaves FEWER voters
with no representative at all (2 instead of 3). Run the proportional
rules on this file via 06_Other/abcvoting_tabulation_engine/ to see it.

Live on BetterVoting (BV27, election jt6r76): BV's Approval engine seats
A,B,C,F — its random draw broke the D/F tie for F, the book's other AV
committee. Two-view page: bv27_jt6r76_lackner_approval_committee.md.
Live results: https://bettervoting.com/jt6r76/results

## Ballots

Row 1 = candidate names; each later row is one voter's approvals (`1` = approve, `0`/blank = not approved).

```text
A,B,C,D,E,F,G
1,1,0,0,0,0,0   # 3 voters — {A,B}
1,1,0,0,0,0,0
1,1,0,0,0,0,0
1,0,1,0,0,0,0   # 3 voters — {A,C}
1,0,1,0,0,0,0
1,0,1,0,0,0,0
1,0,0,1,0,0,0   # 2 voters — {A,D}
1,0,0,1,0,0,0
0,1,1,0,0,1,0   # 1 voter — {B,C,F}
0,0,0,0,1,0,0   # 1 voter — {E}
0,0,0,0,0,1,0   # 1 voter — {F}
0,0,0,0,0,0,1   # 1 voter — {G}
```

## What the engine says

Full report from the [`_tabulated` mirror](../multiwinner_tabulated/approval_bloc_4seats_c7_b12_lackner_skowron_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Approval Voting (4 winners) ---
 Tabulating 12 ballots (any non-zero score = approval).

Ballots:
   columns = A, B, C, D, E, F, G      (1 = approve; 0 / blank / marker = not approved)
     3 × 1,1,0,0,0,0,0
     3 × 1,0,1,0,0,0,0
     2 × 1,0,0,1,0,0,0
     1 × 0,1,1,0,0,1,0
     1 × 0,0,0,0,1,0,0
     1 × 0,0,0,0,0,1,0
     1 × 0,0,0,0,0,0,1

   A -- 8 (67%) -- Elected
   B -- 4 (33%) -- Elected
   C -- 4 (33%) -- Elected
   D -- 2 (17%) -- Elected
   F -- 2 (17%)
   E -- 1 (8%)
   G -- 1 (8%)
  Note: D, F each have 2 approvals and tie for the last 1 seat.
        Candidate priority order (D > F) broke the tie: D elected, F not elected.

[Approval Distribution] (how many candidates each ballot approved)
   22 approvals across 12 ballots — average 1.8 of 7 (range 1–3).
     approved 1: 3 ballots
     approved 2: 8 ballots
     approved 3: 1 ballot

[Co-Approval Matrix]
 Of the voters who approved the ROW candidate, the % who ALSO approved the COLUMN candidate.
      |   A    |   B    |   C    |   D    |   F    |   E    |   G    |
   -------------------------------------------------------------------
   A  |   --   |  38%   |  38%   |  25%   |   0%   |   0%   |   0%   |
   B  |  75%   |   --   |  25%   |   0%   |  25%   |   0%   |   0%   |
   C  |  75%   |  25%   |   --   |   0%   |  25%   |   0%   |   0%   |
   D  |  100%  |   0%   |   0%   |   --   |   0%   |   0%   |   0%   |
   F  |   0%   |  50%   |  50%   |   0%   |   --   |   0%   |   0%   |
   E  |   0%   |   0%   |   0%   |   0%   |   0%   |   --   |   0%   |
   G  |   0%   |   0%   |   0%   |   0%   |   0%   |   0%   |   --   |

Winners — Approval Voting (4 winners)
  A, B, C, D
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 04_Approval/multiwinner/approval_bloc_4seats_c7_b12_lackner_skowron.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Ties & tie-breaking (topic hub)](../../../00_start_here/topics/ties/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [approval_bloc_2seats_c4_b6](approval_bloc_2seats_c4_b6.md) · [approval_bloc_3seats_c6_b5](approval_bloc_3seats_c6_b5.md)
