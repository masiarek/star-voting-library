# Center Squeeze — one electorate, four tabulations, two answers (BV2137)

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/ywckmg) · **[results ↗](https://bettervoting.com/ywckmg/results)** (election `ywckmg`).

*The textbook "center squeeze," from Robert LeGrand's [ranked-ballot calculator](https://cs.angelo.edu/~rlegrand/rbvote/calc.html). One hundred voters rank three candidates. The broadly-liked centrist is the **Condorcet winner** — yet Instant-Runoff throws him out first. The same ballots, counted four ways on BetterVoting, split two-to-two. This is the single clearest "the tabulation, not the ballot, decides" lesson in the repo.*

→ **Level: Voting 301** — Curriculum [301.10](../../00_start_here/CURRICULUM.md). See also: [the ranked-ballot method zoo](../../00_start_here/topics/ranked_ballot_methods_zoo.md) · [center squeeze topic hub](../../00_start_here/topics/center_squeeze/) · [what makes a good winner?](../../00_start_here/topics/what_makes_a_good_winner.md).

## The electorate

One hundred voters, three candidates — a polarizing right (Reagan), a polarizing left (Carter), and a broadly-liked centrist (Anderson) who is almost everyone's second choice but few voters' first:

```
45:Reagan>Anderson>Carter
20:Anderson>Carter>Reagan
35:Carter>Anderson>Reagan
```

Head-to-head, **Anderson is the Condorcet winner** — he beats Reagan 55–45 and Carter 65–35. But he holds the **fewest first-choices** (20), which is exactly what a first-choice-elimination method punishes.

## The result: four methods, two winners

The same ballots run through the four tabulations BetterVoting supports. All four agree with LeGrand's calculator, `pref_voting`, and the LH engine:

| Method (race) | Winner | Why | Engines agreeing |
|---|---|---|---|
| **IRV (Hare)** | **Carter** | Anderson has fewest first-choices → eliminated round 1; Carter beats Reagan 55–45 | LeGrand · pref_voting · LH · **BV** |
| **STV, 1 seat** | **Carter** | single-seat STV *is* IRV | LeGrand · LH · **BV** |
| **Ranked Robin (Copeland)** | **Anderson** | wins every head-to-head — the Condorcet winner | LeGrand · pref_voting · LH · **BV** |
| **STAR (ranks→scores)** | **Anderson** | tops the score round (340) and wins the automatic runoff | LH · **BV** |

The split is the lesson: **the two elimination methods (IRV/STV) throw the centrist out; the two whole-ballot methods (Ranked Robin, STAR) keep him.** On LeGrand's full calculator, **13 of the ~15 methods elect Anderson** — only Hare (IRV) and Carey pick Carter. IRV is the outlier, not the norm.

## The center squeeze, in the LH engine

Instant-Runoff eliminates the consensus candidate first:

```
--- RCV / Instant-Runoff Voting (single winner) ---
 Tabulating 100 ballots (ranked ballots).
Winner(s) — RCV / Instant-Runoff Voting
  Carter
```

Ranked Robin counts every head-to-head and finds the Condorcet winner IRV discarded:

```
Round-Robin — every pair, head-to-head (For – Against):
   Anderson  beats Reagan     55 – 45
   Carter    beats Reagan     55 – 45
   Anderson  beats Carter     65 – 35
Winner — Ranked Robin (RCV-RR): Anderson
   beats every opponent head-to-head — the Condorcet winner.
```

STAR agrees with Ranked Robin (not IRV): Anderson tops the score round with 340 and wins the automatic runoff. Full detail in the [`_tabulated` mirror](center_squeeze_bv2137_tabulated/).

## The rank→score conversion (STAR race)

BetterVoting's STAR race needs 0–5 scores, but this is a *ranked* electorate, so we map each voter's ranking to scores linearly, **top rank → 5, bottom rank → 1**:

> `score(rank) = round( 1 + 4·(N − rank) / (N − 1) )`  → for N = 3 candidates: **5, 3, 1**.

So `Reagan>Anderson>Carter` becomes Reagan 5, Anderson 3, Carter 1. This is a modeling choice (a sincere linear voter), documented so the STAR result is reproducible — it is *not* a claim about how real STAR voters would score. Even so, STAR lands on the Condorcet winner.

## Which methods are on BetterVoting — and which aren't

BetterVoting natively tabulates **four** of LeGrand's ~15 methods: IRV, Ranked Robin, STV, and STAR (via the score conversion above). The other eleven — **Borda, Bucklin, Coombs, Dodgson, Simpson, Schulze, Tideman, Nanson, Baldwin, Raynaud, Small** — have no BetterVoting equivalent; they are verified with the [`pref_voting`](../../00_start_here/tabulation_engines/cross_checking_with_pref_voting.md) library and LeGrand's calculator. All eleven elect **Anderson** here. That BV-vs-others split is a property of BetterVoting's method menu, not of the election — see the [method zoo](../../00_start_here/topics/ranked_ballot_methods_zoo.md) for the full field.

## Sources

- Robert LeGrand, ranked-ballot calculator — [calc.html](https://cs.angelo.edu/~rlegrand/rbvote/calc.html) · [method descriptions](https://cs.angelo.edu/~rlegrand/rbvote/desc.html)
- Live results: [bettervoting.com/ywckmg/results](https://bettervoting.com/ywckmg/results) · frozen export: [`bv2137_ywckmg_bv_export.json`](bv2137_ywckmg_bv_export.json)
- Tabulatable sources: [IRV](bv2137_ywckmg_irv.yaml) · [Ranked Robin](bv2137_ywckmg_ranked_robin.yaml) · [STV](bv2137_ywckmg_stv.yaml) · [STAR](bv2137_ywckmg_star.yaml)
