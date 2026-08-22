---
search:
  exclude: true
---

# Chamberlin-Courant can elect a Pareto-dominated committee

*Generated from [`cc_pareto_dominated_c4_b2.yaml`](../cc_pareto_dominated_c4_b2.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Approval Voting](../../../01_Learn/README.md) · **2 seats** · **Expected winners:** C, D

## Scenario

The smallest counterexample in Lackner & Skowron's book: TWO voters, four
candidates, two seats. Voter 1 approves A, C and D; voter 2 approves B, C
and D.

Committee {C,D} gives EVERY voter two approved winners. Committee {A,B}
gives every voter exactly one. So {C,D} dominates {A,B} in the book's sense
(Definition 3.1): nobody is worse off and somebody is better off. A rule
that can return {A,B} is electing a committee that every single voter would
trade away.

Approval Voting - the count in this file - gets it right: C and D lead 2-2
against A and B at 1-1, so AV elects {C,D} outright. Chamberlin-Courant does
not, because CC only asks whether a voter has AT LEAST ONE approved winner.
Both voters are covered by {A,B} and both are covered by {C,D}, so CC scores
the two committees equally at 2 and returns both - the dominated one
included. That is Proposition A.1 in the book, and it is why CC is marked
only WEAKLY Pareto efficient in Table 3.1 while AV is marked strong.

Reproduce the CC side with the axiom checker:
python 06_Other/abcvoting_tabulation_engine/abc_axiom_check.py --verbose

Source: Lackner, M. & Skowron, P. (2023), "Multi-Winner Voting with Approval
Preferences", SpringerBriefs, doi:10.1007/978-3-031-09016-5, Proposition A.1.

## Ballots

The ballots as marked — a filled **Yes** is a `1` in that candidate's column, a filled **No** a `0`:

| # | Ballot as marked | A | B | C | D |
|:--:|:--|:--:|:--:|:--:|:--:|
| 1 | <img src="../img/cc_pareto_dominated_c4_b2_ballot_1.png" width="260" style="min-width:260px" alt="A Yes/No Approval ballot — voter 1 — approves A, C, D: A Yes, B No, C Yes, D Yes."> | 1 | 0 | 1 | 1 |
| 2 | <img src="../img/cc_pareto_dominated_c4_b2_ballot_2.png" width="260" style="min-width:260px" alt="A Yes/No Approval ballot — voter 2 — approves B, C, D: A No, B Yes, C Yes, D Yes."> | 0 | 1 | 1 | 1 |

The same ballots as the file records them:

Row 1 = candidate names; each later row is one voter's approvals (`1` = approve, `0`/blank = not approved).

```text
A,B,C,D
1,0,1,1   # voter 1 — approves A, C, D
0,1,1,1   # voter 2 — approves B, C, D
```

## What the engine says

Full report from the [`_tabulated` mirror](../cases_tabulated/cc_pareto_dominated_c4_b2_tabulated.txt) (regenerated on every run; every analysis forced on):

<!-- --8<-- [start:report] -->
```text
--- Approval Voting (2 winners) ---
 Tabulating 2 ballots (any non-zero score = approval).

Ballots:
   columns = A, B, C, D      (1 = approve; 0 = not approved)
     1 × 1,0,1,1
     1 × 0,1,1,1

   C -- 2 (100%) -- Elected
   D -- 2 (100%) -- Elected
   A -- 1 (50%)
   B -- 1 (50%)

[Approval Distribution] (how many candidates each ballot approved)
   6 approvals across 2 ballots — average 3.0 of 4 (range 3–3).
     approved 3: 2 ballots

[Co-Approval Matrix]
 Of the voters who approved the ROW candidate, the % who ALSO approved the COLUMN candidate.
      |   C    |   D    |   A    |   B    |
   ----------------------------------------
   C  |   --   |  100%  |  50%   |  50%   |
   D  |  100%  |   --   |  50%   |  50%   |
   A  |  100%  |  100%  |   --   |   0%   |
   B  |  100%  |  100%  |   0%   |   --   |

Winners — Approval Voting (2 winners)
  C, D
```
<!-- --8<-- [end:report] -->

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 04_Approval/03_Criteria/cases/cc_pareto_dominated_c4_b2.yaml
```

## See also

- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [abc_committee_monotonicity_1seat_c3_b10](abc_committee_monotonicity_1seat_c3_b10.md) · [abc_committee_monotonicity_2seats_c3_b10](abc_committee_monotonicity_2seats_c3_b10.md) · [monroe_pareto_dominated_c4_b24](monroe_pareto_dominated_c4_b24.md) · [resign_av_holds_after_kai_c6_b5](resign_av_holds_after_kai_c6_b5.md) · [resign_av_holds_c7_b5](resign_av_holds_c7_b5.md) · [resign_rrv_after_hana_c4_b5](resign_rrv_after_hana_c4_b5.md) · [resign_rrv_seated_c5_b5](resign_rrv_seated_c5_b5.md) · [resign_star_pr_after_bruno_c3_b5](resign_star_pr_after_bruno_c3_b5.md) · [resign_star_pr_seated_c4_b5](resign_star_pr_seated_c4_b5.md) · [sav_strategy_bullet_vote_c5_b2](sav_strategy_bullet_vote_c5_b2.md)
