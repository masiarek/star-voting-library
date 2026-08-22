---
search:
  exclude: true
---

# BV2286 — Ballot B (three dogs on the paper): Approval elects the Golden Retriever

*Generated from [`bv2286_p2wggg_b3_three_dogs_approval.yaml`](../bv2286_p2wggg_b3_three_dogs_approval.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Approval Voting](../../../../04_Approval/01_Learn/README.md) · **1 seat** · **Expected winner:** Golden Retriever

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/p2wggg) · **[results ↗](https://bettervoting.com/p2wggg/results)** (election `p2wggg` · test `BV2286`).

## Scenario

Race 5 of 7 in the BV2286 "Three dogs and a cat" election (BetterVoting p2wggg). The same sixty voters, approving every candidate they would be happy with. Because a dog voter can approve more than one dog, the three-way split of race 3 simply does not occur — the dog side's support adds up instead of dividing. The Golden Retriever wins with 34 of 60 (57%): it is the one breed approved by voters from all three dog camps, where the Labrador is approved by two of them (26) and the German Shepherd by one (8). Cat holds its undivided 26. Approval finds the broadest reach; it does not ask which of two candidates more voters actually prefer, which is the job STAR's automatic runoff does in race 6 — and there the answer is the Labrador. Live results: https://bettervoting.com/p2wggg/results

## Ballots

Row 1 = candidate names; each later row is one voter's approvals (`1` = approve, `0`/blank = not approved).

```text
Count:Labrador,Golden Retriever,German Shepherd,Cat,Parrot
14:1,1,0,0,0   # Labrador camp — the Golden is fine too
12:1,1,0,0,0   # Golden camp — the Labrador is fine too
8:0,1,1,0,0    # Shepherd camp — the Golden is fine too
20:0,0,0,1,0   # cat people
6:0,0,0,1,1    # parrot people — a cat would do
```

## What the engine says

Full report from the [`_tabulated` mirror](../cases_tabulated/bv2286_p2wggg_b3_three_dogs_approval_tabulated.txt) (regenerated on every run; every analysis forced on):

<!-- --8<-- [start:report] -->
```text
--- Approval Voting (single winner) ---
 Tabulating 60 ballots (any non-zero score = approval).

Ballots:
   columns = Labrador, Golden Retriever, German Shepherd, Cat, Parrot      (1 = approve; 0 = not approved)
    26 × 1,1,0,0,0
     8 × 0,1,1,0,0
    20 × 0,0,0,1,0
     6 × 0,0,0,1,1

   Golden Retriever -- 34 (57%) -- Elected
   Labrador         -- 26 (43%)
   Cat              -- 26 (43%)
   German Shepherd  -- 8 (13%)
   Parrot           -- 6 (10%)

[Approval Distribution] (how many candidates each ballot approved)
   100 approvals across 60 ballots — average 1.7 of 5 (range 1–2).
     approved 1: 20 ballots
     approved 2: 40 ballots

[Co-Approval Matrix]
 Of the voters who approved the ROW candidate, the % who ALSO approved the COLUMN candidate.
                     | Golden Retriever |     Labrador     |       Cat        | German Shepherd  |      Parrot      |
   ------------------------------------------------------------------------------------------------------------------
   Golden Retriever  |        --        |       76%        |        0%        |       24%        |        0%        |
   Labrador          |       100%       |        --        |        0%        |        0%        |        0%        |
   Cat               |        0%        |        0%        |        --        |        0%        |       23%        |
   German Shepherd   |       100%       |        0%        |        0%        |        --        |        0%        |
   Parrot            |        0%        |        0%        |       100%       |        0%        |        --        |

Winner — Approval Voting (single winner)
  Golden Retriever
```
<!-- --8<-- [end:report] -->

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/pet_poll_breed_split/cases/bv2286_p2wggg_b3_three_dogs_approval.yaml
```

## See also

- [Vote splitting (worked set)](../../../split_voting/README.md)
- [Runoff reversal (worked set)](../../../../01_STAR/02_Examples/runoff_overturns_leader/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [bv2286_p2wggg_a1_one_dog_plurality](bv2286_p2wggg_a1_one_dog_plurality.md) · [bv2286_p2wggg_a2_one_dog_star](bv2286_p2wggg_a2_one_dog_star.md) · [bv2286_p2wggg_b1_three_dogs_plurality](bv2286_p2wggg_b1_three_dogs_plurality.md) · [bv2286_p2wggg_b2_three_dogs_irv](bv2286_p2wggg_b2_three_dogs_irv.md) · [bv2286_p2wggg_b4_three_dogs_star](bv2286_p2wggg_b4_three_dogs_star.md) · [bv2286_p2wggg_b5_three_dogs_ranked_robin](bv2286_p2wggg_b5_three_dogs_ranked_robin.md)
