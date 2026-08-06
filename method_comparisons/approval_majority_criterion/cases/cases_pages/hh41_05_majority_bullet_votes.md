---
search:
  exclude: true
---

# Hamlin & Hua §4.1 — the majority bullet-votes instead: A wins, same electorate

*Generated from [`hh41_05_majority_bullet_votes.yaml`](../hh41_05_majority_bullet_votes.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Approval Voting](../../../../04_Approval/01_Learn/README.md) · **1 seat** · **Expected winner:** A

## Scenario

The SAME 100 voters with the SAME preferences as hh41_01_approval_as_printed.yaml.
One thing changes: the 60-voter majority draws its approval line one candidate
higher and approves only A. Nobody's opinion moved.

  60 voters: A          (was A + B)
  30 voters: B + C
  10 voters: C + B

Now A wins with 60 approvals to B's 40, and the majority-criterion violation
disappears. This is a counterfactual — the paper's assumed ballots are the
ones in hh41_01 — and it is here to isolate what the §4.1 example actually
turns on. Not the electorate's preferences, which are unchanged: the
threshold. The violation exists only while the majority is generous.

Worth reading against the paper's own §4.3, which reports 1.6 to 3.15
approvals per ballot in real elections and surveys. Those numbers are cited
there to answer the bullet-voting critique — but they are also the frequency
estimate for THIS precondition. By the paper's own data, majorities usually
do approve a second candidate, so the §4.1 configuration is the common case,
not the exotic one.

Compare with STAR, where the same class of failure requires the majority to
support TWO rivals, not one — the Relaxed Majority Criterion:
../../../07_Concepts/topics/majority_criterion/README.md

Claim-check page: ../../../04_Approval/01_Learn/hamlin_hua_2023.md
Set overview: ../README.md

## Ballots

Row 1 = candidate names; each later row is one voter's approvals (`1` = approve, `0`/blank = not approved).

```text
Count:A,B,C
60:1,0,0   # A > B > C — bullet-votes A
30:0,1,1   # B > C > A — approves B and C
10:0,1,1   # C > B > A — approves C and B
```

## What the engine says

Full report from the [`_tabulated` mirror](../cases_tabulated/hh41_05_majority_bullet_votes_tabulated.txt) (regenerated on every run; every analysis forced on):

<!-- --8<-- [start:report] -->
```text
--- Approval Voting (single winner) ---
 Tabulating 100 ballots (any non-zero score = approval).

Ballots:
   columns = A, B, C      (1 = approve; 0 / blank / marker = not approved)
    60 × 1,0,0
    40 × 0,1,1

   A -- 60 (60%) -- Elected
   B -- 40 (40%)
   C -- 40 (40%)

[Approval Distribution] (how many candidates each ballot approved)
   140 approvals across 100 ballots — average 1.4 of 3 (range 1–2).
     approved 1: 60 ballots
     approved 2: 40 ballots

[Co-Approval Matrix]
 Of the voters who approved the ROW candidate, the % who ALSO approved the COLUMN candidate.
      |   A    |   B    |   C    |
   -------------------------------
   A  |   --   |   0%   |   0%   |
   B  |   0%   |   --   |  100%  |
   C  |   0%   |  100%  |   --   |

Winner — Approval Voting (single winner)
  A
```
<!-- --8<-- [end:report] -->

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/approval_majority_criterion/cases/hh41_05_majority_bullet_votes.yaml
```

## See also

- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [hh41_01_approval_as_printed](hh41_01_approval_as_printed.md) · [hh41_02_preferences_ranked_robin](hh41_02_preferences_ranked_robin.md) · [hh41_03_marks_read_pairwise](hh41_03_marks_read_pairwise.md) · [hh41_04_stipulated_utilities_star](hh41_04_stipulated_utilities_star.md)
