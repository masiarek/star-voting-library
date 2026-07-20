# Equal & opposite — the equally weighted vote, made runnable

*The Equal Vote Coalition's "Test of Balance" in one picture: **two voters with exact-opposite opinions on every candidate cancel out completely.** If a race was tied before their two ballots, it's tied after — neither outweighed the other. That's what an **equally weighted vote** means, and it's the reason STAR has no forced vote-splitting. This folder makes the demonstration runnable: a base election, then the same election with the two mirror ballots added — the winner never moves. The concept, in full: [The Equally Weighted Vote — the Test of Balance](../../00_start_here/STAR_Voting/properties_and_limits/equally_weighted_vote.md).*

**▶ Live on BetterVoting:** base — [vote](https://bettervoting.com/36f4v2) · **[results ↗](https://bettervoting.com/36f4v2/results)** (`36f4v2`, BV2219) · plus-cancel — [vote](https://bettervoting.com/q8q9m7) · **[results ↗](https://bettervoting.com/q8q9m7/results)** (`q8q9m7`, BV2220). Two elections differing only by the two mirror ballots — both elect Comet.

→ Related: [the spoiler effect](../../00_start_here/topics/spoiler_effect.md) (what an *unequal* vote causes) · [the Equal Vote scorecard](../../method_comparisons/single_winner_scorecard/) (row 1: "spoiler / vote splitting").

---

## The two mirror ballots

Six candidates — **Astra, Bolt, Comet, Dune, Echo, Flux** — on a 0–5 ballot. Two voters disagree on *every* one; each candidate's two scores sum to 5 (an opposite score is `5 − s`):

| Candidate | Voter A | Voter B | Sum |
|---|:--:|:--:|:--:|
| Astra | 2 | 3 | 5 |
| Bolt | 1 | 4 | 5 |
| Comet | 0 | 5 | 5 |
| Dune | 1 | 4 | 5 |
| Echo | 5 | 0 | 5 |
| Flux | 4 | 1 | 5 |

Add both to *any* election and nothing moves, for two reasons that together are the whole point:

- **Scoring round:** every candidate gains exactly **5** stars (A + B = 5 each). Everyone rises by the same amount, so the ordering — and the top-two finalists — are untouched.
- **Automatic runoff:** whichever finalist Voter A prefers, Voter B prefers the other *by the same margin* (their scores are opposite). They cancel **1–1**.

## The demonstration — before and after

**Before** ([`bv2219_…_base.yaml`](bv2219_36f4v2_equal_opposite_base.yaml)) — three voters, a decisive STAR winner:

```
Scoring Round
   Comet  -- 14 -- First place
   Echo   -- 12 -- Second place
   Astra  --  9      Bolt -- 7      Dune -- 3      Flux -- 1
 Comet and Echo advance.
Automatic Runoff
   Comet  -- 2 -- First place   vs   Echo -- 1        → Comet wins
```

**After** ([`bv2220_…_plus_cancel.yaml`](bv2220_q8q9m7_equal_opposite_plus_cancel.yaml)) — the same three voters **plus** the two mirror ballots:

```
Scoring Round
   Comet  -- 19 -- First place        (14 + 5)
   Echo   -- 17 -- Second place       (12 + 5)
   Astra  -- 14   Bolt -- 12   Dune -- 8   Flux -- 6      (each +5)
 Comet and Echo advance.
Automatic Runoff
   Comet  -- 3 -- First place   vs   Echo -- 2        → Comet wins
```

Every score total rose by exactly **5**; the runoff went **3–2** instead of 2–1 — the two ballots put one vote on *each* side and cancelled. **Same winner, Comet.** The two voters had maximal, perfectly-opposed opinions, and their combined effect on the outcome was *zero*. (Full detail in the [`_tabulated` mirrors](equal_and_opposite_tabulated/).)

## Why a clear-winner base, and not just the two ballots?

The [source graphic](../../00_start_here/STAR_Voting/properties_and_limits/equally_weighted_vote.md#the-picture-two-exactly-opposite-ballots) shows the two mirror ballots *alone* — which produces a **perfect six-way tie** (every candidate totals 5), decided only by lot. That's the cleanest statement of balance, but a pure tie has no reproducible winner to freeze or test against. So this case pairs the mirror ballots with a small decisive base: the property it proves — *"add an exact-opposite pair to any election and the winner is unchanged"* — is the same balance, but now **deterministic**, checkable by the test suite, and safe to freeze against BetterVoting.

## The parallel in ranked methods

Balance isn't unique to scores. A ranked ballot and its **exact reverse** also cancel: in every head-to-head pair, one ballot's `X > Y` is met by the other's `Y > X`, so the pairwise margin is unchanged. So [Ranked Robin](../../00_start_here/RCV_Ranked_Robin/ranked_robin.md) passes the Test of Balance too. The method that *fails* it is [Choose-One](../../00_start_here/topics/plurality.md): a single mark can only *add* to one candidate, never subtract — there is no ballot anyone can cast to cancel it, which is exactly why plurality splits votes. ([RCV-IRV](../../00_start_here/RCV_IRV/RCV_IRV_equal_vote.md) is the subtle one — opposite ballots don't reliably cancel under sequential elimination.)

## Files

| Case | What it shows |
|---|---|
| base — [tabulated report](equal_and_opposite_tabulated/bv2219_36f4v2_equal_opposite_base_tabulated.txt) · [`.yaml`](bv2219_36f4v2_equal_opposite_base.yaml) | the base election — Comet wins 2–1 |
| plus-cancel — [tabulated report](equal_and_opposite_tabulated/bv2220_q8q9m7_equal_opposite_plus_cancel_tabulated.txt) · [`.yaml`](bv2220_q8q9m7_equal_opposite_plus_cancel.yaml) | base + two mirror ballots — Comet still wins, 3–2 |

*Source of the demonstration: Equal Vote Coalition, "Equally Weighted Vote" (the Test of Balance, after Mark Frohnmayer). Cast renamed here (Astra…Flux) for a fresh example. Live on BetterVoting as **BV2219** ([`36f4v2`](https://bettervoting.com/36f4v2/results)) and **BV2220** ([`q8q9m7`](https://bettervoting.com/q8q9m7/results)) — two STAR elections that reproduce the same Comet wins. BetterVoting's own STAR count agrees with the engine on both (Comet, scores 14 and 19); the frozen exports are `bv2219_…_base_bv_export.json` and `bv2220_…_plus_cancel_bv_export.json`.*
