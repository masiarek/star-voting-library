# BV2133 — Pet poll II (Approval): broad support elects Bird

*Generated from [`bv2133_dyxrbr_pet2_approval.yaml`](../bv2133_dyxrbr_pet2_approval.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Approval Voting](../../../../00_start_here/Approval_Voting) · **1 seat** · **Expected winner:** Bird

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/dyxrbr) · **[results ↗](https://bettervoting.com/dyxrbr/results)** (election `dyxrbr`).

## Scenario

One of four races in the BV2133 "Pet poll II" (BetterVoting election dyxrbr). This is the Approval race (approve any pet, 1 = approve). Bird is approved by the 9 Bird-first voters and the 10 Fish-first voters (who approve Cat, Fish, Bird) = 19 approvals — more than Dog (13) or Cat (10) or Fish (10) — so Approval elects Bird. Same electorate as the Plurality race (Dog), RCV-IRV race (Fish) and STAR race (Cat): four methods, four winners. BV also elects Bird. Live results: https://bettervoting.com/dyxrbr/results

## Ballots

Row 1 = candidate names; each later row is one voter's approvals (`1` = approve, `0`/blank = not approved).

```text
Dog,Cat,Fish,Bird
9: 0,0,0,1
10: 0,1,1,1
13: 1,0,0,0
```

## What the engine says

Full report from the [`_tabulated` mirror](../cases_tabulated/bv2133_dyxrbr_pet2_approval_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Approval Voting (single winner) ---
 Tabulating 32 ballots (any non-zero score = approval).

Ballots:
   columns = Dog, Cat, Fish, Bird      (1 = approve; 0 / blank / marker = not approved)
     9 × 0,0,0,1
    10 × 0,1,1,1
    13 × 1,0,0,0

   Bird -- 19 (59%) -- Elected
   Dog  -- 13 (41%)
   Cat  -- 10 (31%)
   Fish -- 10 (31%)

[Approval Distribution] (how many candidates each ballot approved)
   52 approvals across 32 ballots — average 1.6 of 4 (range 1–3).
     approved 1: 22 ballots
     approved 3: 10 ballots

[Co-Approval Matrix]
 Of the voters who approved the ROW candidate, the % who ALSO approved the COLUMN candidate.
         |  Bird  |  Dog   |  Cat   |  Fish  |
   -------------------------------------------
   Bird  |   --   |   0%   |  53%   |  53%   |
   Dog   |   0%   |   --   |   0%   |   0%   |
   Cat   |  100%  |   0%   |   --   |  100%  |
   Fish  |  100%  |   0%   |  100%  |   --   |

Winner — Approval Voting (single winner)
  Bird
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/pet_poll_four_winners/cases/bv2133_dyxrbr_pet2_approval.yaml
```

## See also

- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [bv2133_dyxrbr_pet2_irv](bv2133_dyxrbr_pet2_irv.md) · [bv2133_dyxrbr_pet2_plurality](bv2133_dyxrbr_pet2_plurality.md) · [bv2133_dyxrbr_pet2_star](bv2133_dyxrbr_pet2_star.md)
