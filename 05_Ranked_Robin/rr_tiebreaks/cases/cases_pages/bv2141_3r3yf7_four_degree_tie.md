---
search:
  exclude: true
---

# BV2141 — a Copeland tie that needs all four Equal-Vote tiebreak degrees (electowiki)

*Generated from [`bv2141_3r3yf7_four_degree_tie.yaml`](../bv2141_3r3yf7_four_degree_tie.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../concepts) · **1 seat** · **Expected winner:** Ava

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/3r3yf7) · **[results ↗](https://bettervoting.com/3r3yf7/results)** (election `3r3yf7`).

**Official tie-break (lot) order:** Fabio > Eli > Cedric > Deegan > Ava > Bianca — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../../01_STAR/concepts/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

The electowiki Ranked Robin "all four tie-breaking degrees" example (electowiki.org/wiki/Ranked_Robin). 81 voters, six candidates, with equal rankings and partial (truncated) ballots. Ava and Bianca TIE for the most pairwise wins (3 each), and they also tie on total win margin (+55) AND on votes-against (149) — so the first three degrees of the Equal Vote Coalition's Ranked Robin tiebreak protocol all fail to separate them. Only the 4th-degree beatpath comparison resolves it, to Bianca (14 vs 7). Neither engine here implements that 4-degree protocol: LH breaks the (wins, then margin) tie by pre-published lot, and BetterVoting breaks it at RANDOM — its results log even says so: "Ava picked in random tie-breaker, more robust tiebreaker not yet implemented." This file pins lot_numbers to BV's recorded random order (perm) so LH reproduces BV's frozen instance (Ava). Note BV's "random" is a SEEDED shuffle: a re-tally of these same 81 ballots returns Ava again — the order moves only if the ballot count changes. What it is not is derivable from the ballots. See 05_Ranked_Robin/concepts/rr_tiebreak_lh_vs_bv.md, and the case built to confirm it: 05_Ranked_Robin/rr_tiebreaks/bv2261_y2fbpc_tiebreak_recorded.md. Live results: https://bettervoting.com/3r3yf7/results

## Parameters (from the YAML)

```yaml
voting_method: RankedRobin
num_winners: 1
expected_winners: [Ava]
lot_numbers: [Fabio, Eli, Cedric, Deegan, Ava, Bianca]
bv_election_id: 3r3yf7
bv_test_id: BV2141
```

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
10:Eli>Deegan>Ava=Cedric>Fabio
9:Bianca=Deegan>Eli>Cedric
8:Deegan>Eli>Ava=Bianca=Cedric
8:Bianca>Ava>Fabio>Cedric
8:Fabio>Cedric>Ava>Deegan>Bianca
7:Ava>Eli>Bianca>Fabio
6:Fabio>Bianca=Cedric>Ava
6:Cedric>Deegan=Eli>Ava=Bianca>Fabio
5:Deegan>Ava=Bianca>Eli>Cedric
4:Cedric>Bianca>Ava
4:Ava>Bianca=Fabio
4:Ava=Bianca>Fabio
2:Bianca=Fabio>Ava=Eli
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
--- Ranked Robin (RCV-RR / Copeland) Method (single winner) ---
 Tabulating 81 ballots (ranked ballots).

Ballots:
    10 × Eli > Deegan > Ava=Cedric > Fabio
     9 × Bianca=Deegan > Eli > Cedric
     8 × Deegan > Eli > Ava=Bianca=Cedric
     8 × Bianca > Ava > Fabio > Cedric
     8 × Fabio > Cedric > Ava > Deegan > Bianca
     7 × Ava > Eli > Bianca > Fabio
     6 × Fabio > Bianca=Cedric > Ava
     6 × Cedric > Deegan=Eli > Ava=Bianca > Fabio
     5 × Deegan > Ava=Bianca > Eli > Cedric
     4 × Cedric > Bianca > Ava
     4 × Ava > Bianca=Fabio
     4 × Ava=Bianca > Fabio
     2 × Bianca=Fabio > Ava=Eli

Round-Robin — every pair, head-to-head (For – Against):
   Deegan  beats Eli      30 – 19
   Ava     beats Eli      46 – 33
   Eli     beats Cedric   41 – 32
   Eli     beats Fabio    45 – 32
   Bianca  beats Eli      50 – 31
   Ava     beats Deegan   43 – 38
   Deegan  ties  Cedric   32 – 32
   Fabio   beats Deegan   39 – 38
   Deegan  beats Bianca   37 – 35
   Cedric  beats Ava      33 – 30
   Ava     beats Fabio    56 – 16
   Ava     ties  Bianca   29 – 29
   Cedric  beats Fabio    42 – 39
   Bianca  beats Cedric   39 – 28
   Bianca  beats Fabio    51 – 24

--- Pairwise (Round-Robin) Matrix ---
Head-to-head / pairwise comparison — the Ranked Robin tally
Legend: For - Equal Support - Against   (row vs column)
           |     Eli      |   Deegan    |    Ava      |   Cedric    |   Fabio     |   Bianca    |
-------------------------------------------------------------------------------------------------
     Eli > |     ---      |19 - 32 - 30 |33 -  2 - 46 |41 -  8 - 32 |45 -  4 - 32 |31 -  0 - 50 |
  Deegan > | 30 - 32 - 19 |    ---      |38 -  0 - 43 |32 - 17 - 32 |38 -  4 - 39 |37 -  9 - 35 |
     Ava > | 46 -  2 - 33 |43 -  0 - 38 |    ---      |30 - 18 - 33 |56 -  9 - 16 |29 - 23 - 29 |
  Cedric > | 32 -  8 - 41 |32 - 17 - 32 |33 - 18 - 30 |    ---      |42 -  0 - 39 |28 - 14 - 39 |
   Fabio > | 32 -  4 - 45 |39 -  4 - 38 |16 -  9 - 56 |39 -  0 - 42 |    ---      |24 -  6 - 51 |
  Bianca > | 50 -  0 - 31 |35 -  9 - 37 |29 - 23 - 29 |39 - 14 - 28 |51 -  6 - 24 |    ---      |

Win–loss record — Copeland score = wins + ½·ties (highest score wins; ties broken by total margin, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  Ava        3–1–1       3.5     +55  Deegan, Eli, Fabio
    2  Bianca     3–1–1       3.5     +55  Cedric, Eli, Fabio
    3  Deegan     2–2–1       2.5      +7  Bianca, Eli
    4  Cedric     2–2–1       2.5     -14  Ava, Fabio
    5  Eli        2–3–0         2     -21  Cedric, Fabio
    6  Fabio      1–4–0         1     -82  Deegan

Winner — Ranked Robin (RCV-RR): Ava
   *** 2 candidates tie on the highest Copeland score (3.5): Ava, Bianca — a dead heat (they draw head-to-head, not a cycle). Resolved by total margin, then lot order.
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Smith Set (the generalized Condorcet winner) ---
The smallest group whose every member beats every candidate outside it —
the honest answer to "who is even in contention?".
   Smith set (6 of 6): Ava, Bianca, Deegan, Cedric, Eli, Fabio
   Outside (0):        —
   More than one member ⇒ NO Condorcet winner: the top of the tournament is a
   cycle, so the strongest "candidate" is a set, not a person. Which member of
   the set should win is exactly what Minimax / Ranked Pairs / Schulze disagree
   about — see 05_Ranked_Robin/concepts/cycle_resolution.md.
   Note: the Copeland leaders (Ava, Bianca) are only part of the set — the
   win–loss table's top block understates how wide the contention is.
   Ranked Robin (RCV-RR) winner Ava is INSIDE the Smith set. ✓
      Guaranteed: Ranked Robin (Copeland) is Smith-efficient — every member of
      the set outscores every outsider, so the top of the win–loss table is
      always inside the set, however the tie among them is then broken.
   Fine print: this set contains a pairwise DRAW, and a draw is enough to keep a
   candidate in the Smith set but not in the tighter Schwartz set — so Schwartz
   may be smaller here.
   More: 07_Concepts/topics/smith_set.md
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/bv2141_3r3yf7_four_degree_tie_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 05_Ranked_Robin/rr_tiebreaks/cases/bv2141_3r3yf7_four_degree_tie.yaml
```

## See also

- [Ties & tie-breaking (topic hub)](../../../../07_Concepts/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../../01_STAR/concepts/Tie_Breaking_STAR/tie_breaking.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [bv2261_y2fbpc_tiebreak_recorded_cycle](bv2261_y2fbpc_tiebreak_recorded_cycle.md) · [bv2261_y2fbpc_tiebreak_recorded_draws](bv2261_y2fbpc_tiebreak_recorded_draws.md) · [bv2262_2gvwr9_nine_way_dead_heat](bv2262_2gvwr9_nine_way_dead_heat.md) · [dead_heat_lot_tiebreak](dead_heat_lot_tiebreak.md)
