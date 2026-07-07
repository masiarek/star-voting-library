# Pets Governance — Neighborhood Reps by Bloc Plurality / SNTV (2 seats): one of each

*Generated from [`pets_gov_bloc_plurality.yaml`](../pets_gov_bloc_plurality.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [plurality](../../../00_start_here) · **2 seats** · **Expected winners:** Dog, Bird

**Official tie-break (lot) order:** Dog > Cat > Fish > Bird > Rabbit > Hamster — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

One of six races in the Pets Governance election (BV2134, bvid kcf8vf; BV-confirmed).
Same 22 voters — a 13-voter MAJORITY (Dog, Cat, Fish) and a 9-voter MINORITY
(Bird, Rabbit, Hamster). This 2-seat Neighborhood Reps race uses choose-one Bloc
Plurality (SNTV): each voter marks one pet, the two most-marked win. The majority
concentrates on Dog (13) and the minority on Bird (9), so the seats split Dog +
Bird — one of each. SNTV lands ~proportional here because each faction rallies
behind a single champion (contrast Bloc Approval, which gave the majority both
seats). BV also elects Dog, Bird.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Dog,Cat,Fish,Bird,Rabbit,Hamster
13: 1,0,0,0,0,0
9: 0,0,0,1,0,0
```

## What the engine says

Full report from the [`_tabulated` mirror](../pets_governance_tabulated/pets_gov_bloc_plurality_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- SNTV (single non-transferable vote) — 2 winners ---
 Tabulating 22 ballots (1 vote/voter).

First-choice votes (most votes fill the seats):
   Dog        13  <- Elected
   Bird        9  <- Elected
   Cat         0
   Fish        0
   Rabbit      0
   Hamster     0

Winners — SNTV (single non-transferable vote), 2 seats:
   1. Dog   (13 votes)
   2. Bird   (9 votes)
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/pets_governance/pets_gov_bloc_plurality.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Vote splitting (worked set)](../../split_voting/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [pets_gov_approval](pets_gov_approval.md) · [pets_gov_bloc_star](pets_gov_bloc_star.md) · [pets_gov_ranked_robin](pets_gov_ranked_robin.md) · [pets_gov_star_pr](pets_gov_star_pr.md) · [pets_gov_stv](pets_gov_stv.md)
