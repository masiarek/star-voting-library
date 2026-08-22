---
search:
  exclude: true
---

# Resignation monotonicity — plain Approval, before the resignation

*Generated from [`resign_av_holds_c7_b5.yaml`](../resign_av_holds_c7_b5.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Approval Voting](../../../01_Learn/README.md) · **5 seats** · **Expected winners:** Kai, Nora, Omar, Pia, Quinn

## Scenario

Example 3.3 of Oh & Peters (arXiv:2608.06156), counted by plain multi-winner
Approval — the ONE rule the paper proves is resignation monotone.

Five voters, five seats, seven candidates. Two voters share Kai and split on a
second name (Lena, Milo); the other three all approve the same slate of four
(Nora, Omar, Pia, Quinn).

Approval seats the four-strong slate plus Kai. Under PAV, seq-Phragmén and the
Method of Equal Shares the answer is the SAME committee — and that is what makes
this example sharp: the proportional rules cannot keep it together after Kai
resigns, and Approval can. The after half is
`resign_av_holds_after_kai_c6_b5.yaml`.

## Ballots

Row 1 = candidate names; each later row is one voter's approvals (`1` = approve, `0`/blank = not approved).

```text
Kai,Lena,Milo,Nora,Omar,Pia,Quinn
1,1,0,0,0,0,0     # Kai + Lena
1,0,1,0,0,0,0     # Kai + Milo
0,0,0,1,1,1,1     # the slate
0,0,0,1,1,1,1     # the slate
0,0,0,1,1,1,1     # the slate
```

## What the engine says

Full report from the [`_tabulated` mirror](../cases_tabulated/resign_av_holds_c7_b5_tabulated.txt) (regenerated on every run; every analysis forced on):

<!-- --8<-- [start:report] -->
```text
--- Approval Voting (5 winners) ---
 Tabulating 5 ballots (any non-zero score = approval).

Ballots:
   columns = Kai, Lena, Milo, Nora, Omar, Pia, Quinn      (1 = approve; 0 = not approved)
     1 × 1,1,0,0,0,0,0
     1 × 1,0,1,0,0,0,0
     3 × 0,0,0,1,1,1,1

   Nora  -- 3 (60%) -- Elected
   Omar  -- 3 (60%) -- Elected
   Pia   -- 3 (60%) -- Elected
   Quinn -- 3 (60%) -- Elected
   Kai   -- 2 (40%) -- Elected
   Lena  -- 1 (20%)
   Milo  -- 1 (20%)

[Approval Distribution] (how many candidates each ballot approved)
   16 approvals across 5 ballots — average 3.2 of 7 (range 2–4).
     approved 2: 2 ballots
     approved 4: 3 ballots

[Co-Approval Matrix]
 Of the voters who approved the ROW candidate, the % who ALSO approved the COLUMN candidate.
          |  Nora  |  Omar  |  Pia   | Quinn  |  Kai   |  Lena  |  Milo  |
   -----------------------------------------------------------------------
   Nora   |   --   |  100%  |  100%  |  100%  |   0%   |   0%   |   0%   |
   Omar   |  100%  |   --   |  100%  |  100%  |   0%   |   0%   |   0%   |
   Pia    |  100%  |  100%  |   --   |  100%  |   0%   |   0%   |   0%   |
   Quinn  |  100%  |  100%  |  100%  |   --   |   0%   |   0%   |   0%   |
   Kai    |   0%   |   0%   |   0%   |   0%   |   --   |  50%   |  50%   |
   Lena   |   0%   |   0%   |   0%   |   0%   |  100%  |   --   |   0%   |
   Milo   |   0%   |   0%   |   0%   |   0%   |  100%  |   0%   |   --   |

Winners — Approval Voting (5 winners)
  Nora, Omar, Pia, Quinn, Kai
```
<!-- --8<-- [end:report] -->

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 04_Approval/03_Criteria/cases/resign_av_holds_c7_b5.yaml
```

## See also

- [Monotonicity (topic hub)](../../../../07_Concepts/topics/monotonicity/README.md)
- [Vote splitting (worked set)](../../../../method_comparisons/split_voting/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [abc_committee_monotonicity_1seat_c3_b10](abc_committee_monotonicity_1seat_c3_b10.md) · [abc_committee_monotonicity_2seats_c3_b10](abc_committee_monotonicity_2seats_c3_b10.md) · [cc_pareto_dominated_c4_b2](cc_pareto_dominated_c4_b2.md) · [monroe_pareto_dominated_c4_b24](monroe_pareto_dominated_c4_b24.md) · [resign_av_holds_after_kai_c6_b5](resign_av_holds_after_kai_c6_b5.md) · [resign_rrv_after_hana_c4_b5](resign_rrv_after_hana_c4_b5.md) · [resign_rrv_seated_c5_b5](resign_rrv_seated_c5_b5.md) · [resign_star_pr_after_bruno_c3_b5](resign_star_pr_after_bruno_c3_b5.md) · [resign_star_pr_seated_c4_b5](resign_star_pr_seated_c4_b5.md) · [sav_strategy_bullet_vote_c5_b2](sav_strategy_bullet_vote_c5_b2.md)
