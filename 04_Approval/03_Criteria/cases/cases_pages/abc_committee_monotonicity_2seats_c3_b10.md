---
search:
  exclude: true
---

# Committee monotonicity (2 of 2) — add a seat, and five rules drop the winner

*Generated from [`abc_committee_monotonicity_2seats_c3_b10.yaml`](../abc_committee_monotonicity_2seats_c3_b10.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Approval Voting](../../../01_Learn/README.md) · **2 seats** · **Expected winners:** A, C

## Scenario

The other half of a matched pair: the SAME ten ballots as
abc_committee_monotonicity_1seat_c3_b10.yaml, counted for TWO seats instead
of one.

Two voters approve only A, three approve A and C, three approve B and C, two
approve only B. Approval counts: C 6, A 5, B 5.

With one seat, eleven of the thirteen rules in Lackner & Skowron's Table 3.1
elect the consensus candidate C (SAV and rev-seq-PAV pick A or B instead).
Add a seat and the rules split:

- Approval Voting (the count in this file) keeps C and adds a second - so the
  one-seat winner is still seated. AV is committee monotone.
- Chamberlin-Courant, PAV, Monroe, leximax-Phragmen and MAV all elect {A,B}
  and DROP C. The candidate who won outright when there was one seat is not
  on the committee once a seat is added.

That is what committee monotonicity (Definition 3.2) forbids, and the reason
it matters is practical rather than aesthetic: a body that expects to grow -
a hiring round that may fund one more post, a purchase list that may afford
one more item - cannot use a rule whose answer to "who else?" is "start over".

A and B tie at 5 for the second seat, so AV's own answer here is a tie the
engine settles by priority order; both tied committees contain C, which is
the only part the lesson rests on.

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

Full report from the [`_tabulated` mirror](../cases_tabulated/abc_committee_monotonicity_2seats_c3_b10_tabulated.txt) (regenerated on every run; every analysis forced on):

<!-- --8<-- [start:report] -->
```text
--- Approval Voting (2 winners) ---
 Tabulating 10 ballots (any non-zero score = approval).

Ballots:
   columns = A, B, C      (1 = approve; 0 = not approved)
     2 × 1,0,0
     3 × 1,0,1
     3 × 0,1,1
     2 × 0,1,0

   C -- 6 (60%) -- Elected
   A -- 5 (50%) -- Elected
   B -- 5 (50%)
  Note: A, B each have 5 approvals and tie for the last 1 seat.
        Candidate priority order (A > B) broke the tie: A elected, B not elected.

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

Winners — Approval Voting (2 winners)
  C, A
```
<!-- --8<-- [end:report] -->

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 04_Approval/03_Criteria/cases/abc_committee_monotonicity_2seats_c3_b10.yaml
```

## See also

- [Monotonicity (topic hub)](../../../../07_Concepts/topics/monotonicity/README.md)
- [Ties & tie-breaking (topic hub)](../../../../07_Concepts/topics/ties/README.md)
- [Vote splitting (worked set)](../../../../method_comparisons/split_voting/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [abc_committee_monotonicity_1seat_c3_b10](abc_committee_monotonicity_1seat_c3_b10.md) · [cc_pareto_dominated_c4_b2](cc_pareto_dominated_c4_b2.md) · [monroe_pareto_dominated_c4_b24](monroe_pareto_dominated_c4_b24.md) · [sav_strategy_bullet_vote_c5_b2](sav_strategy_bullet_vote_c5_b2.md)
