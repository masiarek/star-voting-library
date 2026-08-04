---
search:
  exclude: true
---

# BV2261 race 2 — a Condorcet cycle: every pair has a winner, and the tiebreak is still recorded

*Generated from [`bv2261_y2fbpc_tiebreak_recorded_cycle.yaml`](../bv2261_y2fbpc_tiebreak_recorded_cycle.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../../01_Learn) · **1 seat** · **Expected winner:** Anika

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/y2fbpc) · **[results ↗](https://bettervoting.com/y2fbpc/results)** (election `y2fbpc` · test `BV2261`).

**Official tie-break (lot) order:** Anika > Cleo > Beto — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

The same six voters and the same three candidates as race 1, arranged the other way. Here nothing draws: Anika beats Beto 4-2, Beto beats Cleo 4-2, and Cleo beats Anika 4-2 — a textbook Condorcet cycle. Every candidate goes 1-1-0 for a Copeland score of 1, and because every matchup is 4-2 every margin is +0 as well. So Ranked Robin arrives at exactly the same dead end as race 1 by the opposite route: draws there, a cycle here, and in both cases no deterministic rung can separate the field.
THE POINT OF THE PAIR is that BetterVoting's rung of last resort is deterministic and fully published. Its "random" tiebreak seeds TinyRand with (rawVoteCount + hash(raceId)) >>> 0, shuffles once, and reports the resulting order as `perm` with each candidate's index as tieBreakOrder — so the export records the entire sequence, not just the winner, and re-tallying returns the same answer.
Note what the raceId term in that seed buys: this race and race 1 have identical candidates and identical ballot counts, yet BV drew a DIFFERENT order — [Anika, Cleo, Beto] here against [Anika, Beto, Cleo] there. Without the per-race offset every race on a multi-method poll would share one tiebreak order.
This file pins lot_numbers to this race's recorded perm, so LH's lot rung replays BV's draw exactly. Companion race (every pair draws): bv2261_y2fbpc_tiebreak_recorded_draws.yaml. Lesson: 05_Ranked_Robin/03_Criteria/rr_tiebreaks/bv2261_y2fbpc_tiebreak_recorded.md Live results: https://bettervoting.com/y2fbpc/results

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
2:Anika>Beto>Cleo
2:Beto>Cleo>Anika
2:Cleo>Anika>Beto
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
--- Ranked Robin (RCV-RR / Copeland) Method (single winner) ---
 Tabulating 6 ballots (ranked ballots).

Ballots:
     2 × Anika > Beto > Cleo
     2 × Beto > Cleo > Anika
     2 × Cleo > Anika > Beto

Round-Robin — every pair, head-to-head (For – Against):
   Anika  beats Beto    4 – 2
   Cleo   beats Anika   4 – 2
   Beto   beats Cleo    4 – 2

--- Pairwise (Round-Robin) Matrix ---
Head-to-head / pairwise comparison — the Ranked Robin tally
Legend: For - Equal Support - Against   (row vs column)
          |   Anika   |  Beto    |  Cleo    |
---------------------------------------------
  Anika > |    ---    |4 - 0 - 2 |2 - 0 - 4 |
   Beto > | 2 - 0 - 4 |   ---    |4 - 0 - 2 |
   Cleo > | 4 - 0 - 2 |2 - 0 - 4 |   ---    |

Win–loss record — Copeland score = wins + ½·ties (highest score wins; ties broken by total margin, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  Anika      1–1–0         1      +0  Beto
    2  Cleo       1–1–0         1      +0  Anika
    3  Beto       1–1–0         1      +0  Cleo

Winner — Ranked Robin (RCV-RR): Anika
   *** 3 candidates tie for the most wins (Anika, Beto, Cleo) — a Condorcet cycle (no candidate beats all others). Resolved by total margin, then lot order. (This is where Minimax / Ranked Pairs / Schulze differ — see 05_Ranked_Robin/01_Learn/cycle_resolution.md.)
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Smith Set (the generalized Condorcet winner) ---
The smallest group whose every member beats every candidate outside it —
the honest answer to "who is even in contention?".
   Smith set (3 of 3): Anika, Beto, Cleo
   Outside (0):        —
   More than one member ⇒ NO Condorcet winner: the top of the tournament is a
   cycle, so the strongest "candidate" is a set, not a person. Which member of
   the set should win is exactly what Minimax / Ranked Pairs / Schulze disagree
   about — see 05_Ranked_Robin/01_Learn/cycle_resolution.md.
   Ranked Robin (RCV-RR) winner Anika is INSIDE the Smith set. ✓
      Guaranteed: Ranked Robin (Copeland) is Smith-efficient — every member of
      the set outscores every outsider, so the top of the win–loss table is
      always inside the set, however the tie among them is then broken.
   More: 07_Concepts/topics/smith_set.md
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/bv2261_y2fbpc_tiebreak_recorded_cycle_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 05_Ranked_Robin/03_Criteria/rr_tiebreaks/cases/bv2261_y2fbpc_tiebreak_recorded_cycle.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../../07_Concepts/topics/condorcet/README.md)
- [Ties & tie-breaking (topic hub)](../../../../../07_Concepts/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)
- [Glossary](../../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [bv2141_3r3yf7_four_degree_tie](bv2141_3r3yf7_four_degree_tie.md) · [bv2261_y2fbpc_tiebreak_recorded_draws](bv2261_y2fbpc_tiebreak_recorded_draws.md) · [bv2262_2gvwr9_nine_way_dead_heat](bv2262_2gvwr9_nine_way_dead_heat.md) · [dead_heat_lot_tiebreak](dead_heat_lot_tiebreak.md)
