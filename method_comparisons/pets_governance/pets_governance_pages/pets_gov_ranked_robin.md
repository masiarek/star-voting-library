# Pets Governance — Mayor by Ranked Robin (1 seat): the Condorcet winner

*Generated from [`pets_gov_ranked_robin.yaml`](../pets_gov_ranked_robin.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../00_start_here/RCV_Ranked_Robin) · **1 seat** · **Expected winner:** Dog

**Official tie-break (lot) order:** Dog > Cat > Fish > Bird > Rabbit > Hamster — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)).

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

Full report from the [`_tabulated` mirror](../pets_governance_tabulated/pets_gov_ranked_robin_tabulated.txt) (regenerated on every run; every analysis forced on):

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

Win–loss record — Copeland score = wins + ½·ties (most wins wins; ties broken by total margin, then lot order):
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

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/pets_governance/pets_gov_ranked_robin.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [pets_gov_approval](pets_gov_approval.md) · [pets_gov_bloc_plurality](pets_gov_bloc_plurality.md) · [pets_gov_bloc_star](pets_gov_bloc_star.md) · [pets_gov_star_pr](pets_gov_star_pr.md) · [pets_gov_stv](pets_gov_stv.md)
