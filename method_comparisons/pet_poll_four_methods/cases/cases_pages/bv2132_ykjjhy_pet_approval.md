# BV2132 — Pet poll (Approval): broad support elects Cat

*Generated from [`bv2132_ykjjhy_pet_approval.yaml`](../bv2132_ykjjhy_pet_approval.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Approval Voting](../../../../00_start_here/Approval_Voting) · **1 seat** · **Expected winner:** Cat

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/ykjjhy) · **[results ↗](https://bettervoting.com/ykjjhy/results)** (election `ykjjhy`).

## Scenario

One of the four races in the BV2132 "Pet poll" (BetterVoting election ykjjhy). This is the Approval race: each voter approves any number of pets (1 = approve). Cat is approved by everyone except the pure Dog bloc — 22 approvals — so Approval elects Cat, the broadly-acceptable consensus candidate (and Condorcet winner). Same electorate as the Plurality race (Dog wins) and the RCV-IRV race (Fish wins). BV also elects Cat. Live results: https://bettervoting.com/ykjjhy/results

## Ballots

Row 1 = candidate names; each later row is one voter's approvals (`1` = approve, `0`/blank = not approved).

```text
Dog,Cat,Fish
9: 1,1,0
13: 0,1,1
```

## What the engine says

Full report from the [`_tabulated` mirror](../cases_tabulated/bv2132_ykjjhy_pet_approval_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Approval Voting (single winner) ---
 Tabulating 22 ballots (any non-zero score = approval).

Ballots:
   columns = Dog, Cat, Fish      (1 = approve; 0 / blank / marker = not approved)
     9 × 1,1,0
    13 × 0,1,1

   Cat  -- 22 (100%) -- Elected
   Fish -- 13 (59%)
   Dog  -- 9 (41%)

[Approval Distribution] (how many candidates each ballot approved)
   44 approvals across 22 ballots — average 2.0 of 3 (range 2–2).
     approved 2: 22 ballots

[Co-Approval Matrix]
 Of the voters who approved the ROW candidate, the % who ALSO approved the COLUMN candidate.
         |  Cat   |  Fish  |  Dog   |
   ----------------------------------
   Cat   |   --   |  59%   |  41%   |
   Fish  |  100%  |   --   |   0%   |
   Dog   |  100%  |   0%   |   --   |

Winner — Approval Voting (single winner)
  Cat
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/pet_poll_four_methods/cases/bv2132_ykjjhy_pet_approval.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../00_start_here/topics/condorcet/README.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [bv2132_ykjjhy_pet_irv](bv2132_ykjjhy_pet_irv.md) · [bv2132_ykjjhy_pet_plurality](bv2132_ykjjhy_pet_plurality.md) · [bv2132_ykjjhy_pet_star](bv2132_ykjjhy_pet_star.md)
