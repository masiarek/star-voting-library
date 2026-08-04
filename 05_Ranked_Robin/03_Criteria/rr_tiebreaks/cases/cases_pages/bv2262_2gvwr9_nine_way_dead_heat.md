---
search:
  exclude: true
---

# BV2262 — nine candidates, a nine-way dead heat: the recorded tiebreak still pins the winner

*Generated from [`bv2262_2gvwr9_nine_way_dead_heat.yaml`](../bv2262_2gvwr9_nine_way_dead_heat.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../../01_Learn) · **1 seat** · **Expected winner:** Boris

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/2gvwr9) · **[results ↗](https://bettervoting.com/2gvwr9/results)** (election `2gvwr9` · test `BV2262`).

**Official tie-break (lot) order:** Boris > Felix > Greta > Dmitri > Carmen > Alice > Ivan > Elena > Hugo — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

The scale check on BV2261. Nine club members sit around a table and all nine are candidates for chair; each member ranks themselves first and then continues clockwise, so the nine ballots are nine rotations of one order. That construction makes the deadlock exact rather than fiddled: for two candidates at cyclic distance d, exactly 9-d voters prefer the earlier one, so every member beats the four who follow them and loses to the four who precede them. All nine finish 4-4-0 on a Copeland score of 4, and every one of them nets a margin of exactly zero (+7, +5, +3, +1 against -7, -5, -3, -1). It is a nine-way Condorcet cycle — no drawn matchup anywhere, and nothing in the ballots that separates anybody.
So every deterministic rung ties, and BetterVoting's head-to-head rung cannot even apply (it is 2-way only, and nine are tied). Both engines reach their rung of last resort, and the question is what survives in the export. Answer: the whole nine-deep order. BV recorded tieBreakType "random", a nine-long `perm`, tieBreakOrder 0..8 on the nine tied candidates, and `other[]` listing the eight losers in that same order. Its winner, Boris, is sixth in the candidate list — this shuffle is not a no-op.
This file pins lot_numbers to that recorded perm, so LH's lot rung replays BV's draw and elects Boris too. Independently, tools_adam/bv_replay_tiebreak.py recomputes the same perm from (9 ballots + raceId) alone — no ballot content — which is the sharp version of the point: BV's order is RECORDED and reproducible, but never DERIVABLE from how anyone voted. Companion at three candidates: bv2261_y2fbpc_tiebreak_recorded_{draws,cycle}.yaml. Lesson: 05_Ranked_Robin/03_Criteria/rr_tiebreaks/bv2262_2gvwr9_nine_way_dead_heat.md Live results: https://bettervoting.com/2gvwr9/results

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
Alice>Boris>Carmen>Dmitri>Elena>Felix>Greta>Hugo>Ivan
Boris>Carmen>Dmitri>Elena>Felix>Greta>Hugo>Ivan>Alice
Carmen>Dmitri>Elena>Felix>Greta>Hugo>Ivan>Alice>Boris
Dmitri>Elena>Felix>Greta>Hugo>Ivan>Alice>Boris>Carmen
Elena>Felix>Greta>Hugo>Ivan>Alice>Boris>Carmen>Dmitri
Felix>Greta>Hugo>Ivan>Alice>Boris>Carmen>Dmitri>Elena
Greta>Hugo>Ivan>Alice>Boris>Carmen>Dmitri>Elena>Felix
Hugo>Ivan>Alice>Boris>Carmen>Dmitri>Elena>Felix>Greta
Ivan>Alice>Boris>Carmen>Dmitri>Elena>Felix>Greta>Hugo
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
--- Ranked Robin (RCV-RR / Copeland) Method (single winner) ---
 Tabulating 9 ballots (ranked ballots).

Ballots:
     1 × Alice > Boris > Carmen > Dmitri > Elena > Felix > Greta > Hugo > Ivan
     1 × Boris > Carmen > Dmitri > Elena > Felix > Greta > Hugo > Ivan > Alice
     1 × Carmen > Dmitri > Elena > Felix > Greta > Hugo > Ivan > Alice > Boris
     1 × Dmitri > Elena > Felix > Greta > Hugo > Ivan > Alice > Boris > Carmen
     1 × Elena > Felix > Greta > Hugo > Ivan > Alice > Boris > Carmen > Dmitri
     1 × Felix > Greta > Hugo > Ivan > Alice > Boris > Carmen > Dmitri > Elena
     1 × Greta > Hugo > Ivan > Alice > Boris > Carmen > Dmitri > Elena > Felix
     1 × Hugo > Ivan > Alice > Boris > Carmen > Dmitri > Elena > Felix > Greta
     1 × Ivan > Alice > Boris > Carmen > Dmitri > Elena > Felix > Greta > Hugo

Round-Robin — every pair, head-to-head (For – Against):
   Alice   beats Boris    8 – 1
   Alice   beats Carmen   7 – 2
   Alice   beats Dmitri   6 – 3
   Alice   beats Elena    5 – 4
   Felix   beats Alice    5 – 4
   Greta   beats Alice    6 – 3
   Hugo    beats Alice    7 – 2
   Ivan    beats Alice    8 – 1
   Boris   beats Carmen   8 – 1
   Boris   beats Dmitri   7 – 2
   Boris   beats Elena    6 – 3
   Boris   beats Felix    5 – 4
   Greta   beats Boris    5 – 4
   Hugo    beats Boris    6 – 3
   Ivan    beats Boris    7 – 2
   Carmen  beats Dmitri   8 – 1
   Carmen  beats Elena    7 – 2
   Carmen  beats Felix    6 – 3
   Carmen  beats Greta    5 – 4
   Hugo    beats Carmen   5 – 4
   Ivan    beats Carmen   6 – 3
   Dmitri  beats Elena    8 – 1
   Dmitri  beats Felix    7 – 2
   Dmitri  beats Greta    6 – 3
   Dmitri  beats Hugo     5 – 4
   Ivan    beats Dmitri   5 – 4
   Elena   beats Felix    8 – 1
   Elena   beats Greta    7 – 2
   Elena   beats Hugo     6 – 3
   Elena   beats Ivan     5 – 4
   Felix   beats Greta    8 – 1
   Felix   beats Hugo     7 – 2
   Felix   beats Ivan     6 – 3
   Greta   beats Hugo     8 – 1
   Greta   beats Ivan     7 – 2
   Hugo    beats Ivan     8 – 1

--- Pairwise (Round-Robin) Matrix ---
Head-to-head / pairwise comparison — the Ranked Robin tally
Legend: For - Equal Support - Against   (row vs column)
           |   Alice   |  Boris   | Carmen   | Dmitri   |  Elena   |  Felix   |  Greta   |  Hugo    |  Ivan    |
----------------------------------------------------------------------------------------------------------------
   Alice > |    ---    |8 - 0 - 1 |7 - 0 - 2 |6 - 0 - 3 |5 - 0 - 4 |4 - 0 - 5 |3 - 0 - 6 |2 - 0 - 7 |1 - 0 - 8 |
   Boris > | 1 - 0 - 8 |   ---    |8 - 0 - 1 |7 - 0 - 2 |6 - 0 - 3 |5 - 0 - 4 |4 - 0 - 5 |3 - 0 - 6 |2 - 0 - 7 |
  Carmen > | 2 - 0 - 7 |1 - 0 - 8 |   ---    |8 - 0 - 1 |7 - 0 - 2 |6 - 0 - 3 |5 - 0 - 4 |4 - 0 - 5 |3 - 0 - 6 |
  Dmitri > | 3 - 0 - 6 |2 - 0 - 7 |1 - 0 - 8 |   ---    |8 - 0 - 1 |7 - 0 - 2 |6 - 0 - 3 |5 - 0 - 4 |4 - 0 - 5 |
   Elena > | 4 - 0 - 5 |3 - 0 - 6 |2 - 0 - 7 |1 - 0 - 8 |   ---    |8 - 0 - 1 |7 - 0 - 2 |6 - 0 - 3 |5 - 0 - 4 |
   Felix > | 5 - 0 - 4 |4 - 0 - 5 |3 - 0 - 6 |2 - 0 - 7 |1 - 0 - 8 |   ---    |8 - 0 - 1 |7 - 0 - 2 |6 - 0 - 3 |
   Greta > | 6 - 0 - 3 |5 - 0 - 4 |4 - 0 - 5 |3 - 0 - 6 |2 - 0 - 7 |1 - 0 - 8 |   ---    |8 - 0 - 1 |7 - 0 - 2 |
    Hugo > | 7 - 0 - 2 |6 - 0 - 3 |5 - 0 - 4 |4 - 0 - 5 |3 - 0 - 6 |2 - 0 - 7 |1 - 0 - 8 |   ---    |8 - 0 - 1 |
    Ivan > | 8 - 0 - 1 |7 - 0 - 2 |6 - 0 - 3 |5 - 0 - 4 |4 - 0 - 5 |3 - 0 - 6 |2 - 0 - 7 |1 - 0 - 8 |   ---    |

Win–loss record — Copeland score = wins + ½·ties (highest score wins; ties broken by total margin, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  Boris      4–4–0         4      +0  Felix, Dmitri, Carmen, Elena
    2  Felix      4–4–0         4      +0  Greta, Alice, Ivan, Hugo
    3  Greta      4–4–0         4      +0  Boris, Alice, Ivan, Hugo
    4  Dmitri     4–4–0         4      +0  Felix, Greta, Elena, Hugo
    5  Carmen     4–4–0         4      +0  Felix, Greta, Dmitri, Elena
    6  Alice      4–4–0         4      +0  Boris, Dmitri, Carmen, Elena
    7  Ivan       4–4–0         4      +0  Boris, Dmitri, Carmen, Alice
    8  Elena      4–4–0         4      +0  Felix, Greta, Ivan, Hugo
    9  Hugo       4–4–0         4      +0  Boris, Carmen, Alice, Ivan

Winner — Ranked Robin (RCV-RR): Boris
   *** 9 candidates tie for the most wins (Alice, Boris, Carmen, Dmitri, Elena, Felix, Greta, Hugo, Ivan) — a Condorcet cycle (no candidate beats all others). Resolved by total margin, then lot order. (This is where Minimax / Ranked Pairs / Schulze differ — see 05_Ranked_Robin/01_Learn/cycle_resolution.md.)
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Smith Set (the generalized Condorcet winner) ---
The smallest group whose every member beats every candidate outside it —
the honest answer to "who is even in contention?".
   Smith set (9 of 9): Alice, Boris, Carmen, Dmitri, Elena, Felix, Greta, Hugo, Ivan
   Outside (0):        —
   More than one member ⇒ NO Condorcet winner: the top of the tournament is a
   cycle, so the strongest "candidate" is a set, not a person. Which member of
   the set should win is exactly what Minimax / Ranked Pairs / Schulze disagree
   about — see 05_Ranked_Robin/01_Learn/cycle_resolution.md.
   Ranked Robin (RCV-RR) winner Boris is INSIDE the Smith set. ✓
      Guaranteed: Ranked Robin (Copeland) is Smith-efficient — every member of
      the set outscores every outsider, so the top of the win–loss table is
      always inside the set, however the tie among them is then broken.
   More: 07_Concepts/topics/smith_set.md
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/bv2262_2gvwr9_nine_way_dead_heat_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 05_Ranked_Robin/03_Criteria/rr_tiebreaks/cases/bv2262_2gvwr9_nine_way_dead_heat.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../../07_Concepts/topics/condorcet/README.md)
- [Ties & tie-breaking (topic hub)](../../../../../07_Concepts/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)
- [Glossary](../../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [bv2141_3r3yf7_four_degree_tie](bv2141_3r3yf7_four_degree_tie.md) · [bv2261_y2fbpc_tiebreak_recorded_cycle](bv2261_y2fbpc_tiebreak_recorded_cycle.md) · [bv2261_y2fbpc_tiebreak_recorded_draws](bv2261_y2fbpc_tiebreak_recorded_draws.md) · [bv2270_8h4bvh_head_to_head_vs_margin](bv2270_8h4bvh_head_to_head_vs_margin.md) · [dead_heat_lot_tiebreak](dead_heat_lot_tiebreak.md)
