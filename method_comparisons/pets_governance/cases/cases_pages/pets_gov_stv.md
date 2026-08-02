---
search:
  exclude: true
---

# Pets Governance — Delegates by STV (3 seats): proportional again

*Generated from [`pets_gov_stv.yaml`](../pets_gov_stv.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STV (proportional, ranked ballots)](../../../../03_STAR_PR/concepts) · **3 seats** · **Expected winners:** Dog, Bird, Cat

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/kcf8vf) · **[results ↗](https://bettervoting.com/kcf8vf/results)** (election `kcf8vf`).

## Scenario

One of six races in the Pets Governance election (BV2134, bvid kcf8vf; BV-confirmed). Same 22 voters, a
13-voter MAJORITY (Dog, Cat, Fish) and a 9-voter MINORITY (Bird, Rabbit,
Hamster), voting ranked ballots. This 3-seat Delegates race uses STV (Droop
quota = floor(22/4)+1 = 6). The majority (13) meets two quotas and the minority
(9) meets one, so STV elects Dog, Cat (majority) and Bird (minority) — 2 + 1,
proportional. Like STAR-PR (Bird, Dog, Fish) it seats the minority; the two
proportional methods differ only on the majority's third pick (Cat vs Fish).

## Parameters (from the YAML)

```yaml
voting_method: STV
num_winners: 3
expected_winners: [Dog, Bird, Cat]
bv_election_id: kcf8vf
bv_test_id: BV2134
```

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
13:Dog>Cat>Fish>Bird>Rabbit>Hamster
9:Bird>Rabbit>Hamster>Fish>Cat>Dog
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

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

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Smith Set (the generalized Condorcet winner) ---
The smallest group whose every member beats every candidate outside it —
the honest answer to "who is even in contention?".
   Smith set (1 of 6): Dog
   Outside (5):        Cat, Fish, Bird, Rabbit, Hamster
   One member ⇒ Dog is the Condorcet winner, beating every rival head-to-head.
   More: 07_Concepts/topics/smith_set.md
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/pets_gov_stv_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/pets_governance/cases/pets_gov_stv.yaml
```

## See also

- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [pets_gov_approval](pets_gov_approval.md) · [pets_gov_bloc_plurality](pets_gov_bloc_plurality.md) · [pets_gov_bloc_star](pets_gov_bloc_star.md) · [pets_gov_ranked_robin](pets_gov_ranked_robin.md) · [pets_gov_star_pr](pets_gov_star_pr.md)
