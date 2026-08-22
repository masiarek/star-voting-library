---
search:
  exclude: true
---

# Monroe elects a committee every voter would trade away

*Generated from [`monroe_pareto_dominated_c4_b24.yaml`](../monroe_pareto_dominated_c4_b24.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Approval Voting](../../../01_Learn/README.md) · **2 seats** · **Expected winners:** B, C

## Scenario

Example 3.1 from Lackner & Skowron. Twenty-four voters, four candidates, two
seats. Two voters approve only A; one approves A and C; one approves A and D;
ten approve B and C; ten approve B and D.

Monroe's rule elects {C,D}, scoring 22 - it assigns each winner an
equal-sized constituency, and C and D each have exactly twelve voters to
represent. But {C,D} is DOMINATED by {A,B} in the book's sense (Definition
3.1): every one of the 24 voters approves someone in {A,B}, while only 22
approve someone in {C,D}. Nobody is worse off under {A,B} and two voters -
the two who approve A alone - go from no representative at all to one. Every
voter would weakly prefer {A,B}, and Monroe elects {C,D} anyway.

That is what Pareto efficiency forbids, and the example shows exactly WHY
Monroe fails it: equal-sized constituencies are a constraint, and a rule that
insists on the constraint must sometimes refuse a committee that is better
for everybody.

Approval Voting - the count in this file - is the control. B leads with 20;
C and D tie at 11 for the second seat, settled here by priority order. AV
never elects a dominated committee (Proposition A.1), which is the "strong"
in Table 3.1's Pareto column.

Reproduce the Monroe side:
python 06_Other/abcvoting_tabulation_engine/abc_axiom_check.py --verbose

Source: Lackner, M. & Skowron, P. (2023), "Multi-Winner Voting with Approval
Preferences", SpringerBriefs, doi:10.1007/978-3-031-09016-5, Example 3.1.

## Ballots

Row 1 = candidate names; each later row is one voter's approvals (`1` = approve, `0`/blank = not approved).

```text
A,B,C,D
1,0,0,0   # 2 voters — approve A only
1,0,0,0
1,0,1,0   # 1 voter — approves A and C
1,0,0,1   # 1 voter — approves A and D
0,1,1,0   # 10 voters — approve B and C
0,1,1,0
0,1,1,0
0,1,1,0
0,1,1,0
0,1,1,0
0,1,1,0
0,1,1,0
0,1,1,0
0,1,1,0
0,1,0,1   # 10 voters — approve B and D
0,1,0,1
0,1,0,1
0,1,0,1
0,1,0,1
0,1,0,1
0,1,0,1
0,1,0,1
0,1,0,1
0,1,0,1
```

## What the engine says

Full report from the [`_tabulated` mirror](../cases_tabulated/monroe_pareto_dominated_c4_b24_tabulated.txt) (regenerated on every run; every analysis forced on):

<!-- --8<-- [start:report] -->
```text
--- Approval Voting (2 winners) ---
 Tabulating 24 ballots (any non-zero score = approval).

Ballots:
   columns = A, B, C, D      (1 = approve; 0 = not approved)
     2 × 1,0,0,0
     1 × 1,0,1,0
     1 × 1,0,0,1
    10 × 0,1,1,0
    10 × 0,1,0,1

   B -- 20 (83%) -- Elected
   C -- 11 (46%) -- Elected
   D -- 11 (46%)
   A -- 4 (17%)
  Note: C, D each have 11 approvals and tie for the last 1 seat.
        Candidate priority order (C > D) broke the tie: C elected, D not elected.

[Approval Distribution] (how many candidates each ballot approved)
   46 approvals across 24 ballots — average 1.9 of 4 (range 1–2).
     approved 1: 2 ballots
     approved 2: 22 ballots

[Co-Approval Matrix]
 Of the voters who approved the ROW candidate, the % who ALSO approved the COLUMN candidate.
      |   B    |   C    |   D    |   A    |
   ----------------------------------------
   B  |   --   |  50%   |  50%   |   0%   |
   C  |  91%   |   --   |   0%   |   9%   |
   D  |  91%   |   0%   |   --   |   9%   |
   A  |   0%   |  25%   |  25%   |   --   |

Winners — Approval Voting (2 winners)
  B, C
```
<!-- --8<-- [end:report] -->

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 04_Approval/03_Criteria/cases/monroe_pareto_dominated_c4_b24.yaml
```

## See also

- [Ties & tie-breaking (topic hub)](../../../../07_Concepts/topics/ties/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [abc_committee_monotonicity_1seat_c3_b10](abc_committee_monotonicity_1seat_c3_b10.md) · [abc_committee_monotonicity_2seats_c3_b10](abc_committee_monotonicity_2seats_c3_b10.md) · [cc_pareto_dominated_c4_b2](cc_pareto_dominated_c4_b2.md) · [resign_av_holds_after_kai_c6_b5](resign_av_holds_after_kai_c6_b5.md) · [resign_av_holds_c7_b5](resign_av_holds_c7_b5.md) · [resign_rrv_after_hana_c4_b5](resign_rrv_after_hana_c4_b5.md) · [resign_rrv_seated_c5_b5](resign_rrv_seated_c5_b5.md) · [resign_star_pr_after_bruno_c3_b5](resign_star_pr_after_bruno_c3_b5.md) · [resign_star_pr_seated_c4_b5](resign_star_pr_seated_c4_b5.md) · [sav_strategy_bullet_vote_c5_b2](sav_strategy_bullet_vote_c5_b2.md)
