# Approval 101 — most approvals wins

*Generated from [`approval_101_c3_b5.yaml`](../approval_101_c3_b5.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Approval Voting](../../../../00_start_here/Approval_Voting) · **1 seat** · **Expected winner:** Bob

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/ff6mk3) · **[results ↗](https://bettervoting.com/ff6mk3/results)** (election `ff6mk3`).

## Scenario

The simplest Approval election: each voter marks 1 (approve) or 0 for every
candidate, and the most-approved candidate wins. Five voters, three
candidates. Bob is nobody's only choice, but four of five voters approve
him — the broadest support in the field.
This is BetterVoting test BV135, a REAL election: ff6mk3.
Live results: https://bettervoting.com/ff6mk3/results
BetterVoting agrees exactly — Bob 4, Ann 3, Cal 2, no tie.
Frozen export: approval_101_c3_b5_bv_export.json.

More Approval cases: method_comparisons/BV_Library (a real BetterVoting
approval election) and method_comparisons/black_curtain (the same five
voters counted by Approval vs STAR vs RCV-IRV).

## Ballots

Row 1 = candidate names; each later row is one voter's approvals (`1` = approve, `0`/blank = not approved).

```text
Ann,Bob,Cal
1,1,0   # voter 1 — approves Ann and Bob
0,1,1   # voter 2 — approves Bob and Cal
1,1,0   # voter 3 — approves Ann and Bob
0,1,0   # voter 4 — approves only Bob
1,0,1   # voter 5 — approves Ann and Cal
```

## What the engine says

Full report from the [`_tabulated` mirror](../cases_tabulated/approval_101_c3_b5_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Approval Voting (single winner) ---
 Tabulating 5 ballots (any non-zero score = approval).

Ballots:
   columns = Ann, Bob, Cal      (1 = approve; 0 / blank / marker = not approved)
     2 × 1,1,0
     1 × 0,1,1
     1 × 0,1,0
     1 × 1,0,1

   Bob -- 4 (80%) -- Elected
   Ann -- 3 (60%)
   Cal -- 2 (40%)

[Approval Distribution] (how many candidates each ballot approved)
   9 approvals across 5 ballots — average 1.8 of 3 (range 1–2).
     approved 1: 1 ballot
     approved 2: 4 ballots

[Co-Approval Matrix]
 Of the voters who approved the ROW candidate, the % who ALSO approved the COLUMN candidate.
        |  Bob   |  Ann   |  Cal   |
   ---------------------------------
   Bob  |   --   |  50%   |  25%   |
   Ann  |  67%   |   --   |  33%   |
   Cal  |  50%   |  50%   |   --   |

Winner — Approval Voting (single winner)
  Bob
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 04_Approval/_main/cases/approval_101_c3_b5.yaml
```

## See also

- [Ties & tie-breaking (topic hub)](../../../../00_start_here/topics/ties/README.md)
- [The Black Curtain (worked set)](../../../../method_comparisons/black_curtain/README.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)
