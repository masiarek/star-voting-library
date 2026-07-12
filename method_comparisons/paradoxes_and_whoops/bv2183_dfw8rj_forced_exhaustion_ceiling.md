# Forced Exhaustion Ceiling — when a ranking cap discards more ballots than the winner gets

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/dfw8rj) · **[results ↗](https://bettervoting.com/dfw8rj/results)** (BV2183, election `dfw8rj`).

> **Read this fairly.** This is a *deliberately constructed* worst case, built to show the **ceiling** of RCV-IRV ballot exhaustion under a ranking cap — **not** a claim that real elections look like this. Real exhaustion runs milder (roughly 10–27%; see the [real rates](../../00_start_here/RCV_IRV/RCV_IRV_exhausted_ballots.md#how-common-is-it-real-elections)). The point is what the *mechanism permits*, and that the cause is the **ballot cap**, not the voters. It sits in [`paradoxes_and_whoops/`](README.md) under the same [reading-these-fairly](reading_these_fairly.md) discipline as the Felsenthal/Nurmi cases.

## The setup

50 voters, five candidates — but the ballot **caps every voter at 2 rankings** (like a tight [ranking limit](../../00_start_here/RCV_IRV/forced_vs_voluntary_exhaustion.md); NYC caps at 5, Minneapolis at 3). Three minor candidates (Cleo, Dev, Eli) form a rotating bloc; their voters spend both of their allowed ranks on minor candidates.

```
15:Ada>Cleo      ← two real contenders, Ada & Ben, lead on first choices
14:Ben>Dev
 8:Cleo>Eli      ← 21 voters rank ONLY minor candidates —
 7:Dev>Cleo         all their ballots will exhaust
 6:Eli>Dev
```

## What happens

```
ROUND 1   Ada 15 | Ben 14 | Cleo 8 | Dev 7 | Eli 6   → Eli eliminated (Eli>Dev transfers)
ROUND 2   Ada 15 | Ben 14 | Dev 13 | Cleo 8          → Cleo eliminated; its 8 ballots EXHAUST
ROUND 3   Ada 15 | Ben 14 | Dev 13                   → Dev eliminated; its 13 ballots EXHAUST
FINAL     Ada 15 (Elected) | Ben 14 | Blank Votes 21
```

**Winner: Ada, 15 to 14 — a margin of one.** And **21 ballots (42%) were exhausted** — *more than the winner's own 15 votes.* Ada's "majority" (15 of the 29 still active) is really **30% of the 50 voters**. The margin is 1; the exhaustion is 21.

The kicker: **lift the 2-rank cap** — let those 21 voters rank all five candidates — and in single-winner IRV *no ballot can exhaust at all*, because there is always a continuing candidate. The exhaustion here is manufactured entirely by the **ballot design**, not by anything the voters did. That's [**forced** exhaustion](../../00_start_here/RCV_IRV/forced_vs_voluntary_exhaustion.md), the involuntary kind — the voters were as expressive as the rules allowed.

## BetterVoting confirms it

BV's own IRV tabulation agrees with the LH engine to the number: **winner Ada**, and `exhaustedVoteCount = [0, 0, 8, 21]` — 8 exhausted after round 2, **21 by the final round**. Frozen export: [`…_bv_export.json`](bv2183_dfw8rj_forced_exhaustion_ceiling_bv_export.json).

## The LH tabulation

```
--- RCV / Instant-Runoff Voting (single winner) ---
 Tabulating 50 ballots (ranked ballots).

ROUND 1   Ada 15 | Ben 14 | Cleo 8 | Dev 7 | Eli 6(Rejected)
ROUND 2   Ada 15 | Ben 14 | Dev 13 | Cleo 8(Rejected)
ROUND 3   Ada 15 | Ben 14 | Dev 13(Rejected) | Blank Votes 8
FINAL     Ada 15 (Elected) | Ben 14 | Blank Votes 21

Winner — RCV / Instant-Runoff Voting: Ada
```

Full report: [`…_tabulated.txt`](paradoxes_and_whoops_tabulated/bv2183_dfw8rj_forced_exhaustion_ceiling_tabulated.txt).

## Related

- [Forced vs. Voluntary Exhaustion](../../00_start_here/RCV_IRV/forced_vs_voluntary_exhaustion.md) — the concept this case makes concrete
- [Exhausted (Inactive) Ballots](../../00_start_here/RCV_IRV/RCV_IRV_exhausted_ballots.md) — the full picture, including the **real** election rates
- [Ranked Robin](../../00_start_here/RCV_Ranked_Robin/ranked_robin.md) — reads every ballot in every pair, so it never exhausts
- [Reading these paradoxes fairly](reading_these_fairly.md)
