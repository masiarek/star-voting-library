# Alaska 2022 (sincere) — Begich is the Condorcet winner

*Generated from [`alaska_sincere_c3_b200.yaml`](../alaska_sincere_c3_b200.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [RCV-IRV (Instant Runoff)](../../../../00_start_here/RCV_IRV) · **1 seat** · **Expected winner:** Peltola

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

Full report from the [`_tabulated` mirror](../cases_tabulated/alaska_sincere_c3_b200_tabulated.txt) (regenerated on every run; every analysis forced on):

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

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/condorcet_burial_alaska/cases/alaska_sincere_c3_b200.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../00_start_here/topics/condorcet/README.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [alaska_buried_c3_b200](alaska_buried_c3_b200.md)
