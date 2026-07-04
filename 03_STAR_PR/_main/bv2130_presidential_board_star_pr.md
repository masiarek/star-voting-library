# BV2130 — Presidential Board Election (Proportional STAR = Allocated Score)

*A real 7-seat Proportional STAR election on BetterVoting (`bvhchj`): 51 candidates, 102 sparse ballots. LH's `allocated` engine reproduces BetterVoting's **first six seats exactly**; the **seventh diverges** (LH → Claudia De La Cruz, BV → Karina Garcia — both Socialism & Liberation).*

Reference files: [`bv2130_presidential_board_star_pr.yaml`](bv2130_presidential_board_star_pr.yaml) (`voting_method: allocated`, 7 winners) · frozen export [`bv2130_presidential_board_star_pr_bv_export.json`](bv2130_presidential_board_star_pr_bv_export.json) (BV `bvhchj`). Backs sheet row **BV2130**. The election also has a second race (party-alignment **Plurality**) that elects **Democrat**.

## Method mapping — BV `STAR_PR` = Allocated Score

BetterVoting's proportional method is exported as **`STAR_PR`**, which LH does *not* recognize by that name — it is the **Allocated Score** method (`voting_method: allocated`; LH's other proportional variants are `sss` and `rrv`, which give different results). So this is the proportional analog of the [#904](https://github.com/Equal-Vote/bettervoting/issues/904)/[#1086](https://github.com/Equal-Vote/bettervoting/issues/1086) naming point: `STAR_PR` needs mapping to a concrete rule before any engine can reproduce it.

## Result — 6 of 7 seats match, seat 7 diverges

| Seat | LH (`allocated`) | BetterVoting (`STAR_PR`) |
|:--:|---|---|
| 1–6 | Bernie Sanders, Al Gore, Barack Obama, Cornel West, Chase Oliver, Kamala Harris | **same** ✓ |
| 7 | **Claudia De La Cruz** (Soc. & Lib.) | **Karina Garcia** (Soc. & Lib.) |

The two methods agree that the last seat goes to a Socialism & Liberation candidate — proportionality is working — but disagree on *which one*. In LH's exact Allocated Score math Claudia is clearly ahead at the final allocation:

```
The highest-scoring candidate wins a seat.
  Claudia De La Cruz (Socialism and Liberation) -- 34 + 5745/21952 -- First place   (≈ 34.262)
  Karina Garcia      (Socialism and Liberation) -- 33 + 21901/21952                 (≈ 33.998)
 Claudia De La Cruz wins a seat.
```

Full audit copy: [`_main_tabulated/bv2130_presidential_board_star_pr_tabulated.txt`](_main_tabulated/bv2130_presidential_board_star_pr_tabulated.txt).

## The finding

BetterVoting's result carries `tieBreakType: "random"`, and it elected Karina over Claudia — but in LH's computation this is **not a tie** (Claudia leads by ~0.26 of a reweighted point). So seat 7 is one of two things, both worth a maintainer's look:

1. a genuine **implementation difference** between BV's `STAR_PR` and LH's `allocated` (surplus/reweighting order, rounding, or quota), or
2. a **near-tie in BV's math** that BV broke at random — in which case, like the other cases, the outcome is **non-reproducible** (a different draw flips the last seat between two same-party candidates).

Either way, the first six seats are a clean cross-check that LH `allocated` == BV `STAR_PR`, and the seventh isolates exactly where they part ways. (This is the first *proportional* case in the set; the tie cases so far were STAR / Bloc STAR.)

## Related

- Proportional STAR variants in LH: [`02a` allocated](02a_c5_b63_proportional-allocated-score.yaml) · [`02b` sss](02b_c5_b63_proportional-sss.yaml) · [`02c` rrv](02c_c5_b63_proportional-rrv.yaml).
- The same random-tie-break family (single-winner / Bloc): [BV `jfk7pd`](../../01_STAR/tie_break_dead_rung/lot_random_vs_published_jfk7pd/lot_random_vs_published_jfk7pd.md) · [BV131](../../02_STAR_Bloc/_main/bv131_guido_bloc.md) · [BV750](../../02_STAR_Bloc/_main/bv750_tie_breaking_bloc.md).
