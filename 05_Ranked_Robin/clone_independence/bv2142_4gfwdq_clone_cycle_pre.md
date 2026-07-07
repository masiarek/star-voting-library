# BV2142 — clone independence (1/2): a no-Condorcet cycle, and where LH and BV part ways

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/4gfwdq) · **[results ↗](https://bettervoting.com/4gfwdq/results)** (election `4gfwdq`).

Part 1 of the electowiki clone-independence pair (the "before"). It sets up the teaming attack in [BV2143](bv2143_9pr3wr_teaming_fails.md), and on its own it already shows LH and BetterVoting breaking a tie **differently**. Full lesson: [rr_clone_independence.md](../../00_start_here/RCV_Ranked_Robin/rr_clone_independence.md).

## The setup

33 voters. A, B, C sit in a cycle (A beats B, B beats C, C beats A) — no Condorcet winner — and all three tie at **4 wins**.

```
12:A>B>C>D>E>F
11:B>C>A>D>E>F
10:C>A>B>D>E>F
```

## View 1 — BetterVoting: random

BV finds the 3-way tie and, with no margin rung for three tied candidates, picks at random:

- `tied: [C, B, A]` — all `copelandScore: 4`
- `tieBreakType: random`
- `elected: [C]` (this draw); log: *"C picked in random tie-breaker, more robust tiebreaker not yet implemented."*

![BV result for 4gfwdq — A, B, C tie at 4 wins; C elected by random tiebreak](img/REPLACE_4gfwdq_result.png)

## View 2 — LH: margin, then lot

LH ranks the tie by total win margin — and A and B tie there too (**+101** each) while **C is lower (+95)**. So LH **drops C** and settles A-vs-B by lot (pinned to A):

```
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  A          4–1–0         4    +101  B, D, E, F
    2  B          4–1–0         4    +101  C, D, E, F
    3  C          4–1–0         4     +95  A, D, E, F
Winner — Ranked Robin (RCV-RR): A
```

The divergence is real, not just a different coin: **LH's margin rung would never elect C** (lowest margin), yet BV's random draw did. Frozen export: [`bv2142_4gfwdq_clone_cycle_pre_bv_export.json`](bv2142_4gfwdq_clone_cycle_pre_bv_export.json). Full LH detail: [`_tabulated`](clone_independence_tabulated/bv2142_4gfwdq_clone_cycle_pre_tabulated.txt).

## Next

[BV2143 — teaming](bv2143_9pr3wr_teaming_fails.md): the A-faction runs clones and the two engines end up with **opposite** winners.
