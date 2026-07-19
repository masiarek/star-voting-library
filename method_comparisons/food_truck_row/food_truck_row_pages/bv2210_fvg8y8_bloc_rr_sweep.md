# Food-Truck Row — Bloc Ranked Robin: ranked ballots sweep too

*Generated from [`bv2210_fvg8y8_bloc_rr_sweep.yaml`](../bv2210_fvg8y8_bloc_rr_sweep.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../00_start_here/RCV_Ranked_Robin) · **2 seats** · **Expected winners:** Arepa, Bao

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/fvg8y8) · **[results ↗](https://bettervoting.com/fvg8y8/results)** (election `fvg8y8`).

## Scenario

One 100-voter electorate, two food-truck spots, five counts — this file is the Bloc Ranked Robin count (ranked ballots, top-2 by win-loss record). The savory side is a 57-voter OUTRIGHT MAJORITY split across three trucks (Arepa 20 first choices, Bao 19, Churro 18); the sweet side is a disciplined 43-voter minority on two (Donut 22, Eclair 21). Same opinions on every ballot; only the counting rule changes: SNTV hands the majority ZERO seats (Donut+Eclair), Bloc STAR and Bloc Ranked Robin hand it BOTH (Arepa+Bao), STAR-PR and STV share them one per side (Arepa+Donut). THE HEADLINE HERE: switching to ranked ballots does not create proportionality — every savory truck beats every sweet truck 57-43 head-to-head, so the record's top two are both savory (Arepa 4-0, Bao 3-1). Proportionality comes from the COUNT (quotas and transfers), not the ballot shape. Full lesson: README.md in this folder. Live on BetterVoting (Test ID BV2210): https://bettervoting.com/fvg8y8 — all five races agree with the LH engine, no genuine tie anywhere. Live results: https://bettervoting.com/fvg8y8/results

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
20:Arepa>Bao>Churro
19:Bao>Arepa>Churro
18:Churro>Arepa>Bao
22:Donut>Eclair
21:Eclair>Donut
```

## What the engine says

Full report from the [`_tabulated` mirror](../food_truck_row_tabulated/bv2210_fvg8y8_bloc_rr_sweep_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Ranked Robin (RCV-RR / Copeland) Method (2 winners) ---
 Tabulating 100 ballots (ranked ballots).

Ballots:
    20 × Arepa > Bao > Churro
    19 × Bao > Arepa > Churro
    18 × Churro > Arepa > Bao
    22 × Donut > Eclair
    21 × Eclair > Donut

Round-Robin — every pair, head-to-head (For – Against):
   Arepa   beats Bao      38 – 19
   Arepa   beats Churro   39 – 18
   Arepa   beats Donut    57 – 43
   Arepa   beats Eclair   57 – 43
   Bao     beats Churro   39 – 18
   Bao     beats Donut    57 – 43
   Bao     beats Eclair   57 – 43
   Churro  beats Donut    57 – 43
   Churro  beats Eclair   57 – 43
   Donut   beats Eclair   22 – 21

--- Pairwise (Round-Robin) Matrix ---
Head-to-head / pairwise comparison — the Ranked Robin tally
Legend: For - Equal Support - Against   (row vs column)
           |    Arepa     |    Bao      |   Churro    |   Donut     |   Eclair    |
-----------------------------------------------------------------------------------
   Arepa > |     ---      |38 - 43 - 19 |39 - 43 - 18 |57 -  0 - 43 |57 -  0 - 43 |
     Bao > | 19 - 43 - 38 |    ---      |39 - 43 - 18 |57 -  0 - 43 |57 -  0 - 43 |
  Churro > | 18 - 43 - 39 |18 - 43 - 39 |    ---      |57 -  0 - 43 |57 -  0 - 43 |
   Donut > | 43 -  0 - 57 |43 -  0 - 57 |43 -  0 - 57 |    ---      |22 - 57 - 21 |
  Eclair > | 43 -  0 - 57 |43 -  0 - 57 |43 -  0 - 57 |21 - 57 - 22 |    ---      |

Win–loss record — Copeland score = wins + ½·ties (most wins wins; ties broken by total margin, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  Arepa      4–0–0         4     +68  Bao, Churro, Donut, Eclair
    2  Bao        3–1–0         3     +30  Churro, Donut, Eclair
    3  Churro     2–2–0         2     -14  Donut, Eclair
    4  Donut      1–3–0         1     -41  Eclair
    5  Eclair     0–4–0         0     -43  —

Winners — Ranked Robin (RCV-RR), 2 seats (Bloc — the top 2 by record):
   1. Arepa   (4–0–0, Copeland 4, margin +68)
   2. Bao   (3–1–0, Copeland 3, margin +30)
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/food_truck_row/bv2210_fvg8y8_bloc_rr_sweep.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Ties & tie-breaking (topic hub)](../../../00_start_here/topics/ties/README.md)
- [Vote splitting (worked set)](../../split_voting/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [bv2210_fvg8y8_bloc_star_sweep](bv2210_fvg8y8_bloc_star_sweep.md) · [bv2210_fvg8y8_sntv_split](bv2210_fvg8y8_sntv_split.md) · [bv2210_fvg8y8_star_pr_share](bv2210_fvg8y8_star_pr_share.md) · [bv2210_fvg8y8_stv_share](bv2210_fvg8y8_stv_share.md)
