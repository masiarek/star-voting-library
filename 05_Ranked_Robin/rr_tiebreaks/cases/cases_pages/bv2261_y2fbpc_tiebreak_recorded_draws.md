---
search:
  exclude: true
---

# BV2261 race 1 — a perfectly balanced electorate: every pair draws, the tiebreak is recorded

*Generated from [`bv2261_y2fbpc_tiebreak_recorded_draws.yaml`](../bv2261_y2fbpc_tiebreak_recorded_draws.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../concepts) · **1 seat** · **Expected winner:** Anika

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/y2fbpc) · **[results ↗](https://bettervoting.com/y2fbpc/results)** (election `y2fbpc`).

**Official tie-break (lot) order:** Anika > Beto > Cleo — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../../01_STAR/concepts/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

Six voters, three candidates, and the most evenly balanced electorate that can exist: all six possible rankings of Anika, Beto and Cleo appear exactly once. Every head-to-head therefore draws 3-3, every candidate goes 0-0-2 for a Copeland score of 1, and every margin is +0. Ranked Robin's deterministic rungs — Copeland score, then total margin — both tie, so the count falls through to the rung of last resort.
THE POINT OF THIS CASE is what that last rung leaves behind. BetterVoting calls its rung "random", and it is unpredictable from the ballots — but it is NOT lost and it is NOT re-rolled. shuffleCandidatesForRandomTiebreak.ts seeds a deterministic PRNG (TinyRand) with (rawVoteCount + hash(raceId)) >>> 0, shuffles the candidates ONCE, and writes each candidate's position back as tieBreakOrder; the shuffled order ships in the results JSON as `perm`. So the export publishes the WHOLE tiebreak sequence — winner and runners-up — and a re-tally returns the same answer (verified: re-fetched, perm and tieBreakOrder byte-identical).
BV recorded perm [Anika, Beto, Cleo] for this race and elected Anika. This file pins lot_numbers to that recorded order, so LH's own lot rung replays BV's draw exactly — same winner, same full ordering. Companion race (a Condorcet cycle, different perm): bv2261_y2fbpc_tiebreak_recorded_cycle.yaml. Lesson: 05_Ranked_Robin/rr_tiebreaks/bv2261_y2fbpc_tiebreak_recorded.md Live results: https://bettervoting.com/y2fbpc/results

## Parameters (from the YAML)

```yaml
bv_test_id: BV2261
```

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
Anika>Beto>Cleo
Anika>Cleo>Beto
Beto>Anika>Cleo
Beto>Cleo>Anika
Cleo>Anika>Beto
Cleo>Beto>Anika
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
--- Ranked Robin (RCV-RR / Copeland) Method (single winner) ---
 Tabulating 6 ballots (ranked ballots).

Ballots:
     1 × Anika > Beto > Cleo
     1 × Anika > Cleo > Beto
     1 × Beto > Anika > Cleo
     1 × Beto > Cleo > Anika
     1 × Cleo > Anika > Beto
     1 × Cleo > Beto > Anika

Round-Robin — every pair, head-to-head (For – Against):
   Anika  ties  Beto    3 – 3
   Anika  ties  Cleo    3 – 3
   Beto   ties  Cleo    3 – 3

--- Pairwise (Round-Robin) Matrix ---
Head-to-head / pairwise comparison — the Ranked Robin tally
Legend: For - Equal Support - Against   (row vs column)
          |   Anika   |  Beto    |  Cleo    |
---------------------------------------------
  Anika > |    ---    |3 - 0 - 3 |3 - 0 - 3 |
   Beto > | 3 - 0 - 3 |   ---    |3 - 0 - 3 |
   Cleo > | 3 - 0 - 3 |3 - 0 - 3 |   ---    |

Win–loss record — Copeland score = wins + ½·ties (highest score wins; ties broken by total margin, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  Anika      0–0–2         1      +0  —
    2  Beto       0–0–2         1      +0  —
    3  Cleo       0–0–2         1      +0  —

Winner — Ranked Robin (RCV-RR): Anika
   *** 3 candidates tie on the highest Copeland score (1): Anika, Beto, Cleo — a dead heat (they draw head-to-head, not a cycle). Resolved by total margin, then lot order.
```

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
   about — see 05_Ranked_Robin/concepts/cycle_resolution.md.
   Ranked Robin (RCV-RR) winner Anika is INSIDE the Smith set. ✓
      Guaranteed: Ranked Robin (Copeland) is Smith-efficient — every member of
      the set outscores every outsider, so the top of the win–loss table is
      always inside the set, however the tie among them is then broken.
   Fine print: this set contains a pairwise DRAW, and a draw is enough to keep a
   candidate in the Smith set but not in the tighter Schwartz set — so Schwartz
   may be smaller here.
   More: 07_Concepts/topics/smith_set.md
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/bv2261_y2fbpc_tiebreak_recorded_draws_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 05_Ranked_Robin/rr_tiebreaks/cases/bv2261_y2fbpc_tiebreak_recorded_draws.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../07_Concepts/topics/condorcet/README.md)
- [Ties & tie-breaking (topic hub)](../../../../07_Concepts/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../../01_STAR/concepts/Tie_Breaking_STAR/tie_breaking.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [bv2141_3r3yf7_four_degree_tie](bv2141_3r3yf7_four_degree_tie.md) · [bv2261_y2fbpc_tiebreak_recorded_cycle](bv2261_y2fbpc_tiebreak_recorded_cycle.md) · [bv2262_2gvwr9_nine_way_dead_heat](bv2262_2gvwr9_nine_way_dead_heat.md) · [dead_heat_lot_tiebreak](dead_heat_lot_tiebreak.md)
