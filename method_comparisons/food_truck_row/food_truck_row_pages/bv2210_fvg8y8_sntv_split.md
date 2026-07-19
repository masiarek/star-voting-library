# Food-Truck Row — SNTV: the 57% majority splits three ways and gets zero seats

*Generated from [`bv2210_fvg8y8_sntv_split.yaml`](../bv2210_fvg8y8_sntv_split.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [plurality](../../../00_start_here) · **2 seats** · **Expected winners:** Donut, Eclair

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/fvg8y8) · **[results ↗](https://bettervoting.com/fvg8y8/results)** (election `fvg8y8`).

## Scenario

One 100-voter electorate, two food-truck spots, five counts — this file is the SNTV count (choose one truck, top-2 fill the spots). The savory side is a 57-voter OUTRIGHT MAJORITY split across three trucks (Arepa 20 first choices, Bao 19, Churro 18); the sweet side is a disciplined 43-voter minority on two (Donut 22, Eclair 21). Same opinions on every ballot; only the counting rule changes: SNTV hands the majority ZERO seats (Donut+Eclair), Bloc STAR and Bloc Ranked Robin hand it BOTH (Arepa+Bao), STAR-PR and STV share them one per side (Arepa+Donut). THE HEADLINE HERE: 57% of the room is first-choice savory, but one non-transferable vote split three ways tops out at 20 — under both sweet trucks. Running MORE candidates cost the majority EVERYTHING; SNTV punishes exactly the thing healthy politics wants (more choice). The blocs: vote-splitting check lives on the Bloc STAR yaml (the engine runs it on the STAR path). Full lesson: README.md in this folder. Live on BetterVoting (Test ID BV2210): https://bettervoting.com/fvg8y8 — all five races agree with the LH engine, no genuine tie anywhere. Live results: https://bettervoting.com/fvg8y8/results

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Arepa,Bao,Churro,Donut,Eclair
20: 1,0,0,0,0
19: 0,1,0,0,0
18: 0,0,1,0,0
22: 0,0,0,1,0
21: 0,0,0,0,1
```

## What the engine says

Full report from the [`_tabulated` mirror](../food_truck_row_tabulated/bv2210_fvg8y8_sntv_split_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- SNTV (single non-transferable vote) — 2 winners ---
 Tabulating 100 ballots (1 vote/voter).

First-choice votes (most votes fill the seats):
   Donut     22  <- Elected
   Eclair    21  <- Elected
   Arepa     20
   Bao       19
   Churro    18

Winners — SNTV (single non-transferable vote), 2 seats:
   1. Donut   (22 votes)
   2. Eclair   (21 votes)
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/food_truck_row/bv2210_fvg8y8_sntv_split.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Ties & tie-breaking (topic hub)](../../../00_start_here/topics/ties/README.md)
- [Vote splitting (worked set)](../../split_voting/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [bv2210_fvg8y8_bloc_rr_sweep](bv2210_fvg8y8_bloc_rr_sweep.md) · [bv2210_fvg8y8_bloc_star_sweep](bv2210_fvg8y8_bloc_star_sweep.md) · [bv2210_fvg8y8_star_pr_share](bv2210_fvg8y8_star_pr_share.md) · [bv2210_fvg8y8_stv_share](bv2210_fvg8y8_stv_share.md)
