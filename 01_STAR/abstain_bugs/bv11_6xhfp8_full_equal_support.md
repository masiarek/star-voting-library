# BV11 — full & equal support (5,5) counted as abstentions

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/6xhfp8) · **[results ↗](https://bettervoting.com/6xhfp8/results)** (election `6xhfp8`) · issue [Equal-Vote/bettervoting#1053](https://github.com/Equal-Vote/bettervoting/issues/1053)

Three voters each give **both** candidates the maximum score (`5,5`) — full, equal support. A valid STAR ballot. BetterVoting counts every one of them as an **abstention**.

## What it teaches

1. **Full equal support is a cast vote, not an abstention.** Each `5,5` contributes 5 to both candidates in the scoring round. BetterVoting's policy ([#884](https://github.com/Equal-Vote/bettervoting/issues/884)) treats any all-equal ballot as an abstention, so it reports `nTallyVotes = 0`, `nAbstentions = 3`, and the submit dialog warns "Abstained / No preference" on a full-support ballot ([#1053](https://github.com/Equal-Vote/bettervoting/issues/1053)).
2. **Yet a winner is still declared** off zero tallied votes — BetterVoting elects Ann.
3. **LH diverges.** It counts all three as real votes (Ann 15, Bob 15), making it a genuine **tie**, resolved to Ann by lot (CSV column order). Same winner, opposite reasoning: BetterVoting says "everyone abstained," LH says "everyone tied." LH matches the view that full equal support is a real vote — the #884 dispute.

## The ballots

| Voter | Ann | Bob |
|---|:-:|:-:|
| 1 | 5 | 5 |
| 2 | 5 | 5 |
| 3 | 5 | 5 |

## The result

**Ann is elected** — but as a **tie broken by lot** (Ann 15 = Bob 15), not off zero votes.

```text
Scoring Round
   Ann -- 15 -- First place
   Bob -- 15 -- Second place
 Ann and Bob advance.
Automatic Runoff Round  (tie 0-0 → score tie 15-15 → five-star tie 3-3 → lot)
   Resolved: ['Ann'] (selected by lot-number priority: CSV column order).

Winner — STAR Voting Method (single winner)
 Ann
```

BetterVoting result: `elected: ["Ann"]`, `nTallyVotes: 0`, `nAbstentions: 3`.

Full engine detail: [`bv11_6xhfp8_full_equal_support_tabulated.txt`](abstain_bugs_tabulated/bv11_6xhfp8_full_equal_support_tabulated.txt) · source [`.yaml`](bv11_6xhfp8_full_equal_support.yaml). Part of the [BV abstain issue index](../../00_start_here/tabulation_engines/BV/abstain_issues_index.md).
