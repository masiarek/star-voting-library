---
search:
  exclude: true
---

# Alaska 2022 (sincere) — Begich is the Condorcet winner

*Generated from [`alaska_sincere_c3_b200.yaml`](../alaska_sincere_c3_b200.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [RCV-IRV (Instant Runoff)](../../../../06_Other/RCV_IRV/concepts/README.md) · **1 seat** · **Expected winner:** Peltola

## Scenario

The August 2022 Alaska US House special, reduced to a faithful 200-voter
teaching model (Peltola / Begich / Palin), as RANKED ballots. Sincere: Begich
is the Condorcet winner — he beats Peltola 9 and Palin 39 head-to-head. Every
Condorcet method (MinMax, Schulze, Ranked Pairs, and Condorcet-Hare) elects
Begich; RCV-IRV alone eliminates him first (fewest first-choices) and elects
Peltola. The burial twin shows rb-j's strategy: 20 Peltola voters rank Begich
last, manufacturing a cycle. See the write-up: condorcet_burial_alaska/README.md

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
50:Peltola>Begich>Palin
36:Palin>Begich>Peltola
29:Begich>Palin>Peltola
25:Peltola
23:Palin
16:Begich>Peltola>Palin
12:Begich
5:Peltola>Palin>Begich
4:Palin>Peltola>Begich
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
--- RCV / Instant-Runoff Voting (single winner) ---
  Alaska 2022 (sincere) — Begich is the Condorcet winner
 Tabulating 200 ballots (ranked ballots).

ROUND 1
Candidate      Votes  Status
-----------  -------  --------
Peltola           80  Hopeful
Palin             63  Hopeful
Begich            57  Rejected

FINAL RESULT
Candidate      Votes  Status
-----------  -------  --------
Peltola           96  Elected
Palin             92  Rejected
Begich             0  Rejected
Blank Votes       12  Rejected


Winner(s) — RCV / Instant-Runoff Voting (single winner)
  Peltola
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Smith Set (the generalized Condorcet winner) ---
The smallest group whose every member beats every candidate outside it —
the honest answer to "who is even in contention?".
   Smith set (1 of 3): Begich
   Outside (2):        Peltola, Palin
   One member ⇒ Begich is the Condorcet winner, beating every rival head-to-head.
   RCV-IRV winner Peltola is OUTSIDE the Smith set. ✗
      Every member of the set (Begich) beats Peltola head-to-head, yet
      RCV-IRV elected Peltola anyway. RCV-IRV is not Smith-efficient (nor
      Condorcet-efficient) — this is the shape a center squeeze leaves behind.
   More: 07_Concepts/topics/smith_set.md
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/alaska_sincere_c3_b200_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/condorcet_burial_alaska/cases/alaska_sincere_c3_b200.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../07_Concepts/topics/condorcet/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [alaska_buried_c3_b200](alaska_buried_c3_b200.md)
