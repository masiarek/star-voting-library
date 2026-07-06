# Pets Governance — Delegates by STV (3 seats): proportional again

*Generated from [`pets_gov_stv.yaml`](../pets_gov_stv.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STV (proportional, ranked ballots)](../../../00_start_here/proportional_representation) · **3 seats** · **Expected winners:** Dog, Bird, Cat

## Scenario

One of five races in the Pets Governance demo (LH-only). Same 22 voters, a
13-voter MAJORITY (Dog, Cat, Fish) and a 9-voter MINORITY (Bird, Rabbit,
Hamster), voting ranked ballots. This 3-seat Delegates race uses STV (Droop
quota = floor(22/4)+1 = 6). The majority (13) meets two quotas and the minority
(9) meets one, so STV elects Dog, Cat (majority) and Bird (minority) — 2 + 1,
proportional. Like STAR-PR (Bird, Dog, Fish) it seats the minority; the two
proportional methods differ only on the majority's third pick (Cat vs Fish).

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
13:Dog>Cat>Fish>Bird>Rabbit>Hamster
9:Bird>Rabbit>Hamster>Fish>Cat>Dog
```

## What the engine says

Full report from the [`_tabulated` mirror](../pets_governance_tabulated/pets_gov_stv_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- STV / Single Transferable Vote (multi-winner — 3 seats) ---
  Pets Governance — Delegates by STV (3 seats): proportional again
 Tabulating 22 ballots (ranked ballots).
 3 seats; Droop quota = 6 (27.3% of 22).

ROUND 1
Candidate      Votes  Status
-----------  -------  --------
Dog               13  Elected
Bird               9  Elected
Cat                0  Hopeful
Rabbit             0  Hopeful
Fish               0  Hopeful
Hamster            0  Hopeful

FINAL RESULT
Candidate      Votes  Status
-----------  -------  --------
Dog             5.50  Elected
Bird            5.50  Elected
Cat             7.50  Elected
Rabbit          3.50  Rejected
Fish            0.00  Rejected
Hamster         0.00  Rejected


Winner(s) — STV / Single Transferable Vote (multi-winner — 3 seats)
  Dog
  Bird
  Cat
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/pets_governance/pets_gov_stv.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [pets_gov_approval](pets_gov_approval.md) · [pets_gov_bloc_star](pets_gov_bloc_star.md) · [pets_gov_ranked_robin](pets_gov_ranked_robin.md) · [pets_gov_star_pr](pets_gov_star_pr.md)
