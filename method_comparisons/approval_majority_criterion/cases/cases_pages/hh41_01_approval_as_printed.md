# Hamlin & Hua §4.1 — the approval count as printed: B wins with 100%

*Generated from [`hh41_01_approval_as_printed.yaml`](../hh41_01_approval_as_printed.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Approval Voting](../../../../04_Approval/concepts) · **1 seat** · **Expected winner:** B

## Scenario

The worked example from section 4.1 ("The majority criterion") of Hamlin, A. &
Hua, W. (2023), "The case for approval voting," Constitutional Political
Economy 34: 335-345 — reproduced exactly as printed, candidate labels and all.

The paper's assumed preferences:
  60 voters: A > B > C
  30 voters: B > C > A
  10 voters: C > B > A
and the approval ballots it assumes those voters cast (each bloc approves its
top two):
  60 voters: A + B
  30 voters: B + C
  10 voters: C + B

A is the first choice of 60% of voters, so the majority criterion says A must
win. B is approved on every ballot and wins with 100% approval. The paper
concedes the failure and argues it is of trivial consequence; this folder
runs the argument.

Note what the approval ballots can no longer distinguish: the 30 B>C>A voters
and the 10 C>B>A voters cast IDENTICAL ballots, so the engine collapses them
to a single 40-voter row. That erasure is the lesson, not a display quirk.

Claim-check page: ../../../04_Approval/concepts/hamlin_hua_2023.md
Set overview: ../README.md

## Ballots

Row 1 = candidate names; each later row is one voter's approvals (`1` = approve, `0`/blank = not approved).

```text
Count:A,B,C
60:1,1,0   # A > B > C — approves A and B
30:0,1,1   # B > C > A — approves B and C
10:0,1,1   # C > B > A — approves C and B
```

## What the engine says

Full report from the [`_tabulated` mirror](../cases_tabulated/hh41_01_approval_as_printed_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Approval Voting (single winner) ---
 Tabulating 100 ballots (any non-zero score = approval).

Ballots:
   columns = A, B, C      (1 = approve; 0 / blank / marker = not approved)
    60 × 1,1,0
    40 × 0,1,1

   B -- 100 (100%) -- Elected
   A -- 60 (60%)
   C -- 40 (40%)

[Approval Distribution] (how many candidates each ballot approved)
   200 approvals across 100 ballots — average 2.0 of 3 (range 2–2).
     approved 2: 100 ballots

[Co-Approval Matrix]
 Of the voters who approved the ROW candidate, the % who ALSO approved the COLUMN candidate.
      |   B    |   A    |   C    |
   -------------------------------
   B  |   --   |  60%   |  40%   |
   A  |  100%  |   --   |   0%   |
   C  |  100%  |   0%   |   --   |

Winner — Approval Voting (single winner)
  B
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/approval_majority_criterion/cases/hh41_01_approval_as_printed.yaml
```

## See also

- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [hh41_02_preferences_ranked_robin](hh41_02_preferences_ranked_robin.md) · [hh41_03_marks_read_pairwise](hh41_03_marks_read_pairwise.md) · [hh41_04_stipulated_utilities_star](hh41_04_stipulated_utilities_star.md) · [hh41_05_majority_bullet_votes](hh41_05_majority_bullet_votes.md)
