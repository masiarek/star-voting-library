# Pets Governance — Committee by Approval (2 seats): majority again

*Generated from [`pets_gov_approval.yaml`](../pets_gov_approval.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Approval Voting](../../../00_start_here/Approval_Voting) · **2 seats** · **Expected winners:** Dog, Cat

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/kcf8vf) · **[results ↗](https://bettervoting.com/kcf8vf/results)** (election `kcf8vf`).

## Scenario

One of six races in the Pets Governance election (BV2134, bvid kcf8vf; BV-confirmed). Same 22 voters, a
13-voter MAJORITY (Dog, Cat, Fish) and a 9-voter MINORITY (Bird, Rabbit,
Hamster). This race fills a 2-seat Committee by multi-winner Approval (each voter
approves their own party's pets). Bloc Approval is MAJORITARIAN: the two most-
approved are Dog and Cat (13 each), both majority — the minority is shut out
again. Compare with the proportional STAR-PR / STV races on the same electorate.

## Ballots

Row 1 = candidate names; each later row is one voter's approvals (`1` = approve, `0`/blank = not approved).

```text
Dog,Cat,Fish,Bird,Rabbit,Hamster
13: 1,1,1,0,0,0
9: 0,0,0,1,1,1
```

## What the engine says

Full report from the [`_tabulated` mirror](../pets_governance_tabulated/pets_gov_approval_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Approval Voting (2 winners) ---
 Tabulating 22 ballots (any non-zero score = approval).

Ballots:
   columns = Dog, Cat, Fish, Bird, Rabbit, Hamster      (1 = approve; 0 / blank / marker = not approved)
    13 × 1,1,1,0,0,0
     9 × 0,0,0,1,1,1

   Dog     -- 13 (59%) -- Elected
   Cat     -- 13 (59%) -- Elected
   Fish    -- 13 (59%)
   Bird    -- 9 (41%)
   Rabbit  -- 9 (41%)
   Hamster -- 9 (41%)
  Note: Dog, Cat, Fish each have 13 approvals and tie for the last 2 seats.
        Candidate priority order (Dog > Cat > Fish) broke the tie: Dog, Cat elected, Fish not elected.

[Approval Distribution] (how many candidates each ballot approved)
   66 approvals across 22 ballots — average 3.0 of 6 (range 3–3).
     approved 3: 22 ballots

[Co-Approval Matrix]
 Of the voters who approved the ROW candidate, the % who ALSO approved the COLUMN candidate.
            |   Dog   |   Cat   |   Fish  |   Bird  |  Rabbit | Hamster |
   ----------------------------------------------------------------------
   Dog      |    --   |   100%  |   100%  |    0%   |    0%   |    0%   |
   Cat      |   100%  |    --   |   100%  |    0%   |    0%   |    0%   |
   Fish     |   100%  |   100%  |    --   |    0%   |    0%   |    0%   |
   Bird     |    0%   |    0%   |    0%   |    --   |   100%  |   100%  |
   Rabbit   |    0%   |    0%   |    0%   |   100%  |    --   |   100%  |
   Hamster  |    0%   |    0%   |    0%   |   100%  |   100%  |    --   |

Winners — Approval Voting (2 winners)
  Dog, Cat
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/pets_governance/pets_gov_approval.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [pets_gov_bloc_plurality](pets_gov_bloc_plurality.md) · [pets_gov_bloc_star](pets_gov_bloc_star.md) · [pets_gov_ranked_robin](pets_gov_ranked_robin.md) · [pets_gov_star_pr](pets_gov_star_pr.md) · [pets_gov_stv](pets_gov_stv.md)
