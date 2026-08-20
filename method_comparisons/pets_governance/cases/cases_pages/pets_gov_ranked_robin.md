---
search:
  exclude: true
---

# Pets Governance — Mayor by Ranked Robin (1 seat): the Condorcet winner

*Generated from [`pets_gov_ranked_robin.yaml`](../pets_gov_ranked_robin.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../../05_Ranked_Robin/01_Learn/README.md) · **1 seat** · **Expected winner:** Dog

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/kcf8vf) · **[results ↗](https://bettervoting.com/kcf8vf/results)** (election `kcf8vf` · test `BV2134`).

**Official tie-break (lot) order:** Dog > Cat > Fish > Bird > Rabbit > Hamster — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

One of six races in the Pets Governance election (BV2134, bvid kcf8vf; BV-confirmed). Same 22 voters, a
13-voter MAJORITY (Dog, Cat, Fish) and a 9-voter MINORITY (Bird, Rabbit,
Hamster), voting ranked ballots. This single-seat Mayor race uses Ranked Robin
(RCV-RR / Copeland). Because the 13-voter majority ranks Dog first and outnumbers
the minority, Dog beats every rival head-to-head — the Condorcet winner. So the
executive (Mayor) goes to the majority's choice even as the proportional Council
races (STAR-PR, STV) seat the minority.

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
13:Dog>Cat>Fish>Bird>Rabbit>Hamster
9:Bird>Rabbit>Hamster>Fish>Cat>Dog
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
--- Ranked Robin (RCV-RR / Copeland) Method (single winner) ---
 Tabulating 22 ballots (ranked ballots).

Ballots:
    13 × Dog > Cat > Fish > Bird > Rabbit > Hamster
     9 × Bird > Rabbit > Hamster > Fish > Cat > Dog

Round-Robin — every pair, head-to-head (For – Against):
   Dog      beats Cat       13 –  9
   Dog      beats Fish      13 –  9
   Dog      beats Bird      13 –  9
   Dog      beats Rabbit    13 –  9
   Dog      beats Hamster   13 –  9
   Cat      beats Fish      13 –  9
   Cat      beats Bird      13 –  9
   Cat      beats Rabbit    13 –  9
   Cat      beats Hamster   13 –  9
   Fish     beats Bird      13 –  9
   Fish     beats Rabbit    13 –  9
   Fish     beats Hamster   13 –  9
   Bird     beats Rabbit    22 –  0
   Bird     beats Hamster   22 –  0
   Rabbit   beats Hamster   22 –  0

--- Pairwise (Round-Robin) Matrix ---
Head-to-head / pairwise comparison — the Ranked Robin tally
Legend: For - Equal Support - Against   (row vs column)
            |     Dog      |    Cat      |    Fish     |    Bird     |   Rabbit    |  Hamster    |
--------------------------------------------------------------------------------------------------
      Dog > |     ---      |13 -  0 -  9 |13 -  0 -  9 |13 -  0 -  9 |13 -  0 -  9 |13 -  0 -  9 |
      Cat > |  9 -  0 - 13 |    ---      |13 -  0 -  9 |13 -  0 -  9 |13 -  0 -  9 |13 -  0 -  9 |
     Fish > |  9 -  0 - 13 | 9 -  0 - 13 |    ---      |13 -  0 -  9 |13 -  0 -  9 |13 -  0 -  9 |
     Bird > |  9 -  0 - 13 | 9 -  0 - 13 | 9 -  0 - 13 |    ---      |22 -  0 -  0 |22 -  0 -  0 |
   Rabbit > |  9 -  0 - 13 | 9 -  0 - 13 | 9 -  0 - 13 | 0 -  0 - 22 |    ---      |22 -  0 -  0 |
  Hamster > |  9 -  0 - 13 | 9 -  0 - 13 | 9 -  0 - 13 | 0 -  0 - 22 | 0 -  0 - 22 |    ---      |

Win–loss record — Copeland score = wins + ½·ties (highest score wins; ties broken by the Ranked Robin degrees, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  Dog        5–0–0         5     +20  Cat, Fish, Bird, Rabbit, Hamster
    2  Cat        4–1–0         4     +12  Fish, Bird, Rabbit, Hamster
    3  Fish       3–2–0         3      +4  Bird, Rabbit, Hamster
    4  Bird       2–3–0         2     +32  Rabbit, Hamster
    5  Rabbit     1–4–0         1     -12  Hamster
    6  Hamster    0–5–0         0     -56  —

Winner — Ranked Robin (RCV-RR): Dog
   beats every opponent head-to-head — the Condorcet winner.
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Smith Set (the generalized Condorcet winner) ---
The smallest group whose every member beats every candidate outside it —
the honest answer to "who is even in contention?".
   Smith set (1 of 6): Dog
   Outside (5):        Cat, Fish, Bird, Rabbit, Hamster
   One member ⇒ Dog is the Condorcet winner, beating every rival head-to-head.
   Ranked Robin (RCV-RR) winner Dog is INSIDE the Smith set. ✓
      Guaranteed: Ranked Robin (Copeland) is Smith-efficient — every member of
      the set outscores every outsider, so the top of the win–loss table is
      always inside the set, however the tie among them is then broken.
   More: 07_Concepts/topics/smith_set.md
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/pets_gov_ranked_robin_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/pets_governance/cases/pets_gov_ranked_robin.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../07_Concepts/topics/condorcet/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [pets_gov_approval](pets_gov_approval.md) · [pets_gov_bloc_plurality](pets_gov_bloc_plurality.md) · [pets_gov_bloc_star](pets_gov_bloc_star.md) · [pets_gov_star_pr](pets_gov_star_pr.md) · [pets_gov_stv](pets_gov_stv.md)
