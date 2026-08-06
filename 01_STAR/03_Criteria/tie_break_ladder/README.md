# 01_STAR/03_Criteria/tie_break_ladder — the STAR tiebreak ladder, worked

The **happy-path** side of STAR tie-breaking: elections that **tie but never reach the lot**, because the deterministic rungs (pairwise / score, then five-star) settle everything. This is the live, BV-backed home for the worked example in **[the tie-breaking ladder doc](../../01_Learn/Tie_Breaking_STAR/tie_breaking.md)**.

Contrast the two neighbours:
- **[Flat_scores_ties/…05 — BV555/`xmyf7k`](../../09_Parked/Flat_scores_ties/README.md#case-05)** — every rung ties down to the **random floor** (LH-only).
- **[tie_break_dead_rung/](../tie_break_dead_rung/README.md)** — five-star is a *dead rung* (no 5s to weigh), so the tie drops to the lot.

Here, five-star and score do their job, so LH and BetterVoting **agree deterministically**.

| Case | Cast | Method | Winner | Ties resolved by |
|---|---|---|---|---|
| [Tied for the second finalist **(BV2276, `qhjyr2`)**](bv2276_qhjyr2_second_finalist_tie.md) | Ana/Ben/Cora/Dev | STAR | Ana | **pairwise** (scoring) — the first rung, on its own |
| [Ice cream ladder **(BV2180, `fp62p2`)**](bv2180_fp62p2_ice_cream_ladder.md) | ice cream | STAR | Strawberry | five-star (scoring), then score (runoff) — lot never reached |
| [No Condorcet winner — top-two tie **(BV830, `vb3xv2`)**](bv830_vb3xv2_no_condorcet_tie_score.md) | A/B/C (abstract) | STAR | B | score (runoff) — a head-to-head tie the Condorcet standard can't break |

Read them in that order: BV2276 is the ladder at its shortest (one rung, done), BV2180 is what happens when that rung *can't* decide and five-star takes over, and BV830 moves the tie from the scoring round into the runoff.

**Live on BetterVoting:** [vote](https://bettervoting.com/qhjyr2) · **[results ↗](https://bettervoting.com/qhjyr2/results)** (BV2276) · [vote](https://bettervoting.com/fp62p2) · **[results ↗](https://bettervoting.com/fp62p2/results)** (BV2180) · [vote](https://bettervoting.com/vb3xv2) · **[results ↗](https://bettervoting.com/vb3xv2/results)** (BV830).

> ⚠️ **BV2276 doubles as a bug fixture.** Its BetterVoting results page currently names *Ben* as the runoff opponent in the Race Details tables while the charts correctly name *Cora* — [issue #1484](https://github.com/Equal-Vote/bettervoting/issues/1484). The tabulation and the winner are unaffected; see [the case page](bv2276_qhjyr2_second_finalist_tie.md#a-live-reporting-bug-preserved-here-on-purpose) for the side-by-side.
