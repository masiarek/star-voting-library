# BV2141 — a Copeland tie that needs all four Equal-Vote tiebreak degrees (electowiki)

*Generated from [`bv2141_3r3yf7_four_degree_tie.yaml`](../bv2141_3r3yf7_four_degree_tie.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../../00_start_here/RCV_Ranked_Robin) · **1 seat** · **Expected winner:** Ava

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/3r3yf7) · **[results ↗](https://bettervoting.com/3r3yf7/results)** (election `3r3yf7`).

**Official tie-break (lot) order:** Fabio > Eli > Cedric > Deegan > Ava > Bianca — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

The electowiki Ranked Robin "all four tie-breaking degrees" example (electowiki.org/wiki/Ranked_Robin). 81 voters, six candidates, with equal rankings and partial (truncated) ballots. Ava and Bianca TIE for the most pairwise wins (3 each), and they also tie on total win margin (+55) AND on votes-against (149) — so the first three degrees of the Equal Vote Coalition's Ranked Robin tiebreak protocol all fail to separate them. Only the 4th-degree beatpath comparison resolves it, to Bianca (14 vs 7). Neither engine here implements that 4-degree protocol: LH breaks the (wins, then margin) tie by pre-published lot, and BetterVoting breaks it at RANDOM — its results log even says so: "Ava picked in random tie-breaker, more robust tiebreaker not yet implemented." This file pins lot_numbers to BV's recorded random order (perm) so LH reproduces BV's frozen instance (Ava). A re-tally on BV could elect Bianca instead. See 00_start_here/RCV_Ranked_Robin/rr_tiebreak_lh_vs_bv.md. Live results: https://bettervoting.com/3r3yf7/results

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

Full report from the [`_tabulated` mirror](../cases_tabulated/bv2141_3r3yf7_four_degree_tie_tabulated.txt) (regenerated on every run; every analysis forced on):

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

Win–loss record — Copeland score = wins + ½·ties (most wins wins; ties broken by total margin, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  Ava        3–1–1       3.5     +55  Deegan, Eli, Fabio
    2  Bianca     3–1–1       3.5     +55  Cedric, Eli, Fabio
    3  Deegan     2–2–1       2.5      +7  Bianca, Eli
    4  Cedric     2–2–1       2.5     -14  Ava, Fabio
    5  Eli        2–3–0         2     -21  Cedric, Fabio
    6  Fabio      1–4–0         1     -82  Deegan

Winner — Ranked Robin (RCV-RR): Ava
   *** 2 candidates tie for the most wins (Ava, Bianca) — a dead heat (they draw head-to-head, not a cycle). Resolved by total margin, then lot order.
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 05_Ranked_Robin/rr_tiebreaks/cases/bv2141_3r3yf7_four_degree_tie.yaml
```

## See also

- [Ties & tie-breaking (topic hub)](../../../../00_start_here/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [dead_heat_lot_tiebreak](dead_heat_lot_tiebreak.md)
