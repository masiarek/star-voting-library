# BV parity — Approval: most approvals wins (single winner)

*Generated from [`BV_Library_approval_single_winner.yaml`](../BV_Library_approval_single_winner.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Approval Voting](../../../../00_start_here/Approval_Voting) · **1 seat** · **Expected winner:** Dave

## Scenario

Ported from BetterVoting's tabulator unit tests (Approval.test.ts :: "Single Winner Test").
Dave has the most approvals and wins. In the original two rows carried out-of-bounds
marks (a 2 and a -1) that BetterVoting counts as 0/not-approved; here they are written
as plain 0 so the file validates under this engine while preserving every approval total.

## Ballots

Row 1 = candidate names; each later row is one voter's approvals (`1` = approve, `0`/blank = not approved).

Markers on these ballots: `-` blank · `~` race abstention · `&` candidate abstention · `?` spoiled · `%` spoiled+reissued — all tabulate as 0 (reported honestly).

```text
Alice,Bob,Carol,Dave
1,1,1,1
0,1,1,1
0,1,1,1
0,0,1,1
0,0,1,1
0,0,1,1
0,0,0,1
-,-,-,-
0,0,0,0
0,0,0,0
```

## What the engine says

Full report from the [`_tabulated` mirror](../cases_tabulated/BV_Library_approval_single_winner_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Approval Voting (single winner) ---
 Tabulating 10 ballots (any non-zero score = approval).
 Abstentions: 3 of 10 ballots approved no one (7 ballots cast an approval).

Ballots:
   columns = Alice, Bob, Carol, Dave      (1 = approve; 0 / blank / marker = not approved)
     1 × 1,1,1,1
     2 × 0,1,1,1
     3 × 0,0,1,1
     1 × 0,0,0,1
     3 × 0,0,0,0

   Dave  -- 7 (70%) -- Elected
   Carol -- 6 (60%)
   Bob   -- 3 (30%)
   Alice -- 1 (10%)

[Approval Distribution] (how many candidates each ballot approved)
   17 approvals across 10 ballots — average 1.7 of 4 (range 0–4).
     approved none: 3 ballots
     approved 1: 1 ballot
     approved 2: 3 ballots
     approved 3: 2 ballots
     approved 4: 1 ballot

[Co-Approval Matrix]
 Of the voters who approved the ROW candidate, the % who ALSO approved the COLUMN candidate.
          |  Dave  | Carol  |  Bob   | Alice  |
   --------------------------------------------
   Dave   |   --   |  86%   |  43%   |  14%   |
   Carol  |  100%  |   --   |  50%   |  17%   |
   Bob    |  100%  |  100%  |   --   |  33%   |
   Alice  |  100%  |  100%  |  100%  |   --   |

Winner — Approval Voting (single winner)
  Dave
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/BV_Library/cases/BV_Library_approval_single_winner.yaml
```

## See also

- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [BV_Library_plurality_single_winner](BV_Library_plurality_single_winner.md) · [BV_Library_ranked_robin_single_winner](BV_Library_ranked_robin_single_winner.md) · [BV_Library_ranked_robin_ties](BV_Library_ranked_robin_ties.md) · [BV_Library_star_condorcet_winner](BV_Library_star_condorcet_winner.md) · [BV_Library_star_pr_basic_two_seats](BV_Library_star_pr_basic_two_seats.md) · [BV_Library_star_pr_fractional_surplus](BV_Library_star_pr_fractional_surplus.md) · [BV_Library_star_pr_voters_fewer_than_seats](BV_Library_star_pr_voters_fewer_than_seats.md) · [BV_Library_star_runnerup_tie](BV_Library_star_runnerup_tie.md) · [BV_Library_star_runoff](BV_Library_star_runoff.md) · [BV_Library_star_runoff_score_tie_five_star](BV_Library_star_runoff_score_tie_five_star.md) · [BV_Library_star_runoff_tie_score_resolves](BV_Library_star_runoff_tie_score_resolves.md)
