# BV2143 — clone independence (2/2): teaming succeeds on LH, fails on BetterVoting

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/9pr3wr) · **[results ↗](https://bettervoting.com/9pr3wr/results)** (election `9pr3wr`).

Part 2 of the electowiki clone-independence pair (the "after"). Same electorate as [BV2142](bv2142_4gfwdq_clone_cycle_pre.md), but the A-faction runs clones — and **the two engines elect different winners from identical ballots.** Full lesson: [rr_clone_independence.md](../../00_start_here/RCV_Ranked_Robin/rr_clone_independence.md).

## The teaming ballots

The A-faction fields A1 and A2 (ranked together in A's old slot):

```
12:A1>A2>B>C>D>E>F
11:B>C>A1>A2>D>E>F
10:C>A1>A2>B>D>E>F
```

A1 and C tie at **5 wins**. Whether teaming works comes down to the tiebreak.

## View 1 — BetterVoting: head-to-head → C (teaming fails)

BV breaks the 2-way tie by head-to-head, and **C beats A1, 21–12**:

- `tied: []`, `tieBreakType: none`
- `elected: [C]`; log: *"C preferred over A1 in runoff."*

![BV result for 9pr3wr — A1 and C tie at 5 wins; C elected on head-to-head](img/REPLACE_9pr3wr_result.png)

So on BetterVoting the clones did **not** help the A-faction — C wins. Deterministic and freezable: [`bv2143_9pr3wr_teaming_fails_bv_export.json`](bv2143_9pr3wr_teaming_fails_bv_export.json).

## View 2 — LH: margin → A1 (teaming succeeds)

LH breaks the tie by total margin, and A1 (**+134**) beats C (**+104**):

```
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  A1         5–1–0         5    +134  B, A2, D, E, F
    2  C          5–1–0         5    +104  A1, A2, D, E, F
    3  B          4–2–0         4     +90  C, D, E, F
    4  A2         4–2–0         4     +68  B, D, E, F
Winner — Ranked Robin (RCV-RR): A1
```

By running clones the A-faction pushed B out of the top tier and lifted A1's margin above C — under a **margin** tiebreak the teaming **succeeds** (A1 wins). Full LH detail: [`_tabulated`](clone_independence_tabulated/bv2143_9pr3wr_teaming_fails_tabulated.txt).

## The takeaway

Same ballots, opposite winners: **LH (margin) → A1**, **BV (head-to-head) → C**. The clone-independence *failure* is a property of the margin tiebreak (LH, and the Equal Vote protocol), not of Ranked Robin as such — BV's head-to-head rung happens to resist this teaming. See [rr_tiebreak_lh_vs_bv.md](../../00_start_here/RCV_Ranked_Robin/rr_tiebreak_lh_vs_bv.md).
