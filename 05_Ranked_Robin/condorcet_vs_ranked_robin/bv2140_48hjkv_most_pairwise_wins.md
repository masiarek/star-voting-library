# BV2140 — Ranked Robin: most pairwise wins, with no Condorcet winner

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/48hjkv) · **[results ↗](https://bettervoting.com/48hjkv/results)** (election `48hjkv`).

The [electowiki Ranked Robin worked example](https://electowiki.org/wiki/Ranked_Robin), reproduced end-to-end. It is the repo's first case built on **equal-rank ballots** (voters tie candidates, e.g. `Ava=Bianca=Cedric`). It teaches the core Ranked Robin idea — *elect whoever wins the most head-to-head matchups* — in the interesting case where **no candidate beats everyone** (there is no Condorcet winner), yet Ranked Robin still names a clear winner.

## The lesson

Ranked Robin (RCV-RR / Copeland) reads the whole ballot and runs a round-robin: every candidate is compared head-to-head with every other, and whoever wins the **most** matchups is elected. Here **Ava wins 3 of her 4 matchups** (beating Cedric, Deegan, and Eli) and is elected.

The twist: **there is no Condorcet winner.** A Condorcet winner beats *everyone* head-to-head, and nobody here does — **Ava herself loses to Bianca, 15–14.** In fact the top three form a rock-paper-scissors cycle: Ava beats Cedric, Cedric beats Bianca, and Bianca beats Ava. So "who beats everyone?" has no answer, but "who wins the most matchups?" still does — that's the question Ranked Robin asks, and why it always produces a winner where a strict Condorcet rule would stall. (Compare the two companions in this folder: [`01_condorcet_winner`](01_condorcet_winner.yaml), where a clean Condorcet winner exists, and [`02_cycle_no_condorcet`](02_cycle_no_condorcet.yaml), a pure 3-way tie.)

## The ballots

35 voters, five candidates (Ava, Bianca, Cedric, Deegan, Eli). `=` ties candidates at the same rank; `>` separates rank levels.

```
 8:Ava>Cedric>Deegan>Bianca>Eli
 6:Ava=Bianca=Cedric>Eli>Deegan
 6:Eli>Ava>Bianca=Cedric=Deegan
 6:Deegan>Bianca=Cedric>Eli>Ava
 4:Bianca>Ava>Eli>Deegan>Cedric
 3:Eli>Deegan>Bianca=Cedric>Ava
 2:Deegan=Eli>Bianca=Cedric>Ava
```

## View 1 — BetterVoting

BetterVoting's [results page](https://bettervoting.com/48hjkv/results) tabulates the same 35 ballots with its own `RankedRobin.ts` engine and declares **⭐ Ava wins! ⭐** — the "Head-to-head wins" chart and Race Details table give the identical records:

| Candidate | # Wins | Win Rate |
|-----------|:------:|:--------:|
| **Ava** | **3** | **75%** |
| Bianca | 2 | 50% |
| Cedric | 2 | 50% |
| Deegan | 2 | 50% |
| Eli | 1 | 25% |

![BV head-to-head wins bar chart — Ava 75%, Bianca/Cedric/Deegan 50%, Eli 25%](img/REPLACE_48hjkv_result_bars.png)
![BV Race Details table — Ava 3 wins (75%), Bianca/Cedric/Deegan 2 (50%), Eli 1 (25%)](img/REPLACE_48hjkv_race_details.png)

This is exactly the LH win–loss record below (Ava 3, Bianca/Cedric/Deegan 2, Eli 1). **BV = LH** — the equal-rank ballots tabulated identically on both engines, confirming BetterVoting reads tied ranks the same way. Note also that BV's ballot-data export carries a `precinct` column (blank here — this election defines no precincts).

## View 2 — the LH tabulation engine

The LH engine reads the equal-rank ballots natively (its round-robin parser scores tied candidates as *Equal Support* against each other) and reproduces the electowiki pairwise matrix exactly:

```
--- Ranked Robin (RCV-RR / Copeland) Method (single winner) ---
 Tabulating 35 ballots (ranked ballots).

Ballots:
     8 × Ava > Cedric > Deegan > Bianca > Eli
     6 × Ava=Bianca=Cedric > Eli > Deegan
     6 × Eli > Ava > Bianca=Cedric=Deegan
     6 × Deegan > Bianca=Cedric > Eli > Ava
     4 × Bianca > Ava > Eli > Deegan > Cedric
     3 × Eli > Deegan > Bianca=Cedric > Ava
     2 × Deegan=Eli > Bianca=Cedric > Ava

Round-Robin — every pair, head-to-head (For – Against):
   Ava     beats Cedric   18 – 11
   Ava     beats Deegan   24 – 11
   Bianca  beats Ava      15 – 14
   Ava     beats Eli      18 – 17
   Deegan  beats Cedric   15 – 14
   Cedric  beats Bianca    8 –  4
   Cedric  beats Eli      20 – 15
   Deegan  beats Bianca   19 – 10
   Eli     beats Deegan   19 – 14
   Bianca  beats Eli      24 – 11

--- Pairwise (Round-Robin) Matrix ---
Head-to-head / pairwise comparison — the Ranked Robin tally
Legend: For - Equal Support - Against   (row vs column)
           |     Ava      |   Cedric    |   Deegan    |   Bianca    |    Eli      |
-----------------------------------------------------------------------------------
     Ava > |     ---      |18 -  6 - 11 |24 -  0 - 11 |14 -  6 - 15 |18 -  0 - 17 |
  Cedric > | 11 -  6 - 18 |    ---      |14 -  6 - 15 | 8 - 23 -  4 |20 -  0 - 15 |
  Deegan > | 11 -  0 - 24 |15 -  6 - 14 |    ---      |19 -  6 - 10 |14 -  2 - 19 |
  Bianca > | 15 -  6 - 14 | 4 - 23 -  8 |10 -  6 - 19 |    ---      |24 -  0 - 11 |
     Eli > | 17 -  0 - 18 |15 -  0 - 20 |19 -  2 - 14 |11 -  0 - 24 |    ---      |

Win–loss record — Copeland score = wins + ½·ties (most wins wins; ties broken by total margin, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  Ava        3–1–0         3     +20  Cedric, Deegan, Eli
    2  Cedric     2–2–0         2      +1  Bianca, Eli
    3  Bianca     2–2–0         2      +1  Ava, Eli
    4  Deegan     2–2–0         2      -8  Cedric, Bianca
    5  Eli        1–3–0         1     -14  Deegan

Winner — Ranked Robin (RCV-RR): Ava
   the most head-to-head wins (3).
```

Full detail (forced-maximal) in the `_tabulated` mirror: [`bv2140_48hjkv_most_pairwise_wins_tabulated.txt`](condorcet_vs_ranked_robin_tabulated/bv2140_48hjkv_most_pairwise_wins_tabulated.txt).

## Reading the matrix

Each cell is `For – Equal Support – Against` for the row candidate vs the column candidate. Ava's row shows wins over Cedric (18–11), Deegan (24–11), and Eli (18–17) — but a loss to Bianca (14–15). That single loss is why Ava is **not** a Condorcet winner, even though her 3 wins are the most of anyone. The `Equal Support` column is where the tied ranks land: e.g. Cedric vs Bianca is `8 – 23 – 4`, because 23 of the 35 voters ranked Cedric and Bianca *equal*.

## Cross-checks

- **LH native** `run_ranked_robin` — Ava, 3 wins (above).
- **BetterVoting** `RankedRobin.ts` — Ava, 3 wins; records identical to LH (View 1). Frozen: [`bv2140_48hjkv_most_pairwise_wins_bv_export.json`](bv2140_48hjkv_most_pairwise_wins_bv_export.json).
- **pref_voting** Copeland — the pref_voting wrapper currently shares the YAML reader that predates the `=` split, so this equal-rank profile isn't yet cross-checkable there; tracked separately. The pairwise records are independently confirmed by BV (above) and by a score-encoding of the same weak orders through LH.

