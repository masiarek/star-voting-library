---
search:
  exclude: true
---

# Committee monotonicity (1 of 2) — one seat, and the consensus candidate takes it

*Generated from [`abc_committee_monotonicity_1seat_c3_b10.yaml`](../abc_committee_monotonicity_1seat_c3_b10.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Approval Voting](../../../01_Learn/README.md) · **1 seat** · **Expected winner:** C

## Scenario

Half of a matched pair. The SAME ten ballots are counted twice, once for one
seat and once for two: this file is the one-seat count, its companion
abc_committee_monotonicity_2seats_c3_b10.yaml is the two-seat count.

Ten voters, three candidates: two approve only A, three approve A and C,
three approve B and C, two approve only B. Approval counts: C 6, A 5, B 5.

For ONE seat, eleven of the thirteen rules in Lackner & Skowron's Table 3.1
elect the consensus candidate C - Approval Voting, CC, PAV, seq-PAV, seq-CC,
Monroe, Greedy Monroe, seq-Phragmen, leximax-Phragmen, the Method of Equal
Shares and MAV. C is the only candidate a majority approves, and she is
nobody's enemy. (SAV and rev-seq-PAV instead pick A or B here, because SAV
divides each ballot's vote among its marks: A and B score 3.5 to C's 3.)

The interesting half is the companion file. Committee monotonicity
(Definition 3.2) says that growing the committee from k to k+1 should ADD a
member, never reshuffle: the one-seat winner should still be seated when
there are two seats. Approval Voting and the sequential rules honour that.
Chamberlin-Courant, PAV, Monroe, leximax-Phragmen and MAV all elect {A,B} for
two seats and drop C entirely - the candidate who won outright when there was
a single seat is not even on the committee once a seat is ADDED. That is
Proposition A.2 in the book, and it is the ✗ in Table 3.1's committee
monotonicity column.

Reproduce it: python 06_Other/abcvoting_tabulation_engine/abc_axiom_check.py

Source: Lackner, M. & Skowron, P. (2023), "Multi-Winner Voting with Approval
Preferences", SpringerBriefs, doi:10.1007/978-3-031-09016-5, Proposition A.2.

## Ballots

Row 1 = candidate names; each later row is one voter's approvals (`1` = approve, `0`/blank = not approved).

```text
A,B,C
1,0,0   # 2 voters — approve A only
1,0,0
1,0,1   # 3 voters — approve A and C
1,0,1
1,0,1
0,1,1   # 3 voters — approve B and C
0,1,1
0,1,1
0,1,0   # 2 voters — approve B only
0,1,0
```

## What the engine says

Full report from the [`_tabulated` mirror](../cases_tabulated/abc_committee_monotonicity_1seat_c3_b10_tabulated.txt) (regenerated on every run; every analysis forced on):

<!-- --8<-- [start:report] -->
```text
--- Approval Voting (single winner) ---
 Tabulating 10 ballots (any non-zero score = approval).

Ballots:
   columns = A, B, C      (1 = approve; 0 = not approved)
     2 × 1,0,0
     3 × 1,0,1
     3 × 0,1,1
     2 × 0,1,0

   C -- 6 (60%) -- Elected
   A -- 5 (50%)
   B -- 5 (50%)

[Approval Distribution] (how many candidates each ballot approved)
   16 approvals across 10 ballots — average 1.6 of 3 (range 1–2).
     approved 1: 4 ballots
     approved 2: 6 ballots

[Co-Approval Matrix]
 Of the voters who approved the ROW candidate, the % who ALSO approved the COLUMN candidate.
      |   C    |   A    |   B    |
   -------------------------------
   C  |   --   |  50%   |  50%   |
   A  |  60%   |   --   |   0%   |
   B  |  60%   |   0%   |   --   |

Winner — Approval Voting (single winner)
  C
```
<!-- --8<-- [end:report] -->

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 04_Approval/03_Criteria/cases/abc_committee_monotonicity_1seat_c3_b10.yaml
```

## See also

- [Monotonicity (topic hub)](../../../../07_Concepts/topics/monotonicity/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [abc_committee_monotonicity_2seats_c3_b10](abc_committee_monotonicity_2seats_c3_b10.md) · [cc_pareto_dominated_c4_b2](cc_pareto_dominated_c4_b2.md) · [monroe_pareto_dominated_c4_b24](monroe_pareto_dominated_c4_b24.md) · [sav_strategy_bullet_vote_c5_b2](sav_strategy_bullet_vote_c5_b2.md)
