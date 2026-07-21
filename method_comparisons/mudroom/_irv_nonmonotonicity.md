<!-- Unlisted, deliberately. This page is not linked from the folder README or any nav. -->
# The Non-Monotonicity Files 🍿 — a (guilty-pleasure) collection

> **⚠️ House-rules exemption in effect.** This page is the repo's guilty pleasure: a deliberately *one-sided* montage of RCV-IRV punishing candidates for gaining support — and rewarding them for losing it. It breaks the library's own [fairness rule](../paradoxes_and_whoops/reading_these_fairly.md) **on purpose**, and it isn't linked from any index. Two honest promises anyway: **every example below is real and verified elsewhere in this repo** (the curation is the unfair part, never the facts), and the grown-up, even-handed version — rarity stated, STAR's own limits conceded — is always one click away in [the monotonicity worked set](../monotonicity/) and the [concept page](../../00_start_here/RCV_IRV/RCV_IRV_non_monotonicity.md). Read it as a highlight reel, not a courtroom. **And for turnabout:** we threw the same unfair mud at *our own* method in the [STAR Whoops reel](_star_whoops.md) — because every method has one.

*Monotonicity is the one property you'd swear any voting method has: **ranking a candidate higher can't make them lose, and lower can't make them win.** Instant-runoff cheerfully violates both directions, because it eliminates on first-choice counts and elimination order is fragile. Here's the reel.*

---

## 🥇 Real elections that actually did this

- **Burlington, VT 2009 (Mayor).** The certified, real 8,980 ballots. Montroll beats *every* rival head-to-head (5–0, a Condorcet winner) — and IRV eliminates him in the semifinal. Worse: raise the *winner* Kiss on 750 of the real ballots and he **loses**. Burlington repealed IRV the next year. → [Burlington 2009, runnable](../burlington_2009/README.md).
- **Alaska 2022 (US House special).** Give the winner **more**: had ~6,000 Palin-only voters ranked the winner **Peltola** *first*, Peltola would have **lost** — the extra first-place votes eliminate Palin first, and Begich beats Peltola. Ranking the winner higher defeats her. → [upward monotonicity, Alaska](../monotonicity/upward_monotonicity_alaska.md).
- **San Francisco D7 2020 (Supervisor).** The mirror, also real: shift the *loser* **Engardio** *down* on ~800 ballots and he **wins** — the shift eliminates Melgar first (by 3 votes) and Engardio takes the final. Less support, more victory. → [downward monotonicity, San Francisco](../monotonicity/downward_monotonicity_sf.md).

## 🥈 The lab specimens (clean, minimal, runnable)

- **The textbook pair.** 4 voters raise X from second to first — X goes from **winning** to **losing**, nothing else changed. → [monotonicity worked set](../monotonicity/).
- **Best = worst.** A 24-voter election where IRV elects **A** whether the voters are picking the best candidate *or* reverse every ballot to pick the worst. Its "best" and "worst" are the same guy. → [reversal symmetry](../reversal_symmetry/).

## 🥉 …and it's not even rare

A spatial-model study (**Ornstein & Norman, *Public Choice* 2014**) estimates a **lower bound of ~15%** monotonicity failure in *competitive* three-candidate IRV races — climbing toward 50% as the race tightens. Not a freak coincidence; a structural feature of eliminate-and-transfer. → [the concept, with the citation](../../00_start_here/RCV_IRV/RCV_IRV_non_monotonicity.md#how-often-does-this-happen-not-rare).

---

## The obligatory conscience clause

Okay, fine — the fair version, because the repo insists and it's the honest one:

- Monotonicity failures are **real but concentrated in close, near-three-way races**; most IRV elections never trip one.
- The failure is **IRV-specific**, not "ranked voting" — [Ranked Robin](../../00_start_here/RCV_Ranked_Robin/README.md) and other whole-ballot methods are monotonic.
- **STAR isn't perfectly clean either** — it passes mono-raise but fails the stronger *mono-raise-delete* in lab constructions ([conceded here](../monotonicity/README.md)).
- Both STAR and IRV beat Choose-One by a mile; the honest debate is between good options.

There. Now you can go back to enjoying the reel — responsibly. For the version you'd actually cite in a debate, use the [worked set](../monotonicity/) and [read it fairly](../paradoxes_and_whoops/reading_these_fairly.md).
