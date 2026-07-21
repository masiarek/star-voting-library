# The strategic pathologies — five "Molochs," and where STAR stands

*Every single-winner voting method has a **strategic failure mode**: a situation where a voter's honest ballot works against them, and the individually-rational move is to lie. Jameson Quinn (Center for Election Science) catalogued these as **"Molochs"** — coordination traps where each voter's self-interest drags the whole electorate to a worse place. This page lays out the five, names the **game** each one is, and gives the honest scorecard: **which ones STAR and Ranked Robin escape, which they only soften, and which nobody can escape.***

> **Attribution & lean.** The "Moloch" framing is Quinn's, and he's **advocacy-adjacent** — his own preferred methods are Approval and 3-2-1, *not* STAR. That makes this a useful *outside* lens: where the scorecard credits STAR, it's crediting it against a yardstick built by someone who doesn't champion it. Each row links to a runnable case in this library so you can check the result yourself.

---

## The five Molochs at a glance

| Moloch | The game it is | Method it plagues | Runnable here |
|---|---|---|---|
| **Lesser Evil** | coordination trap (wasted-vote) | First-Past-the-Post | [vote-splitting / spoiler](../../method_comparisons/split_voting/) · [spoiler effect](spoiler_effect.md) |
| **Center Squeeze** | premature elimination | RCV-IRV (Hare) | [center squeeze](../../method_comparisons/center_squeeze/) · [favorite betrayal](../../method_comparisons/favorite_betrayal_irv/) |
| **Dark Horse** | prisoner's dilemma | Borda / ranked-point | [the Dark Horse](../../method_comparisons/dark_horse_borda/) |
| **Chicken / Burr** | chicken (snowdrift) | Approval / Score | [the chicken dilemma](../../method_comparisons/chicken_dilemma/) |
| **Condorcet Cycle** | Gibbard-universal | *every* method | [cycle resolution](../RCV_Ranked_Robin/cycle_resolution.md) · [Gibbard–Satterthwaite](gibbard_satterthwaite_theorem.md) |

## The scorecard — STAR and Ranked Robin on each

| Moloch | STAR | Ranked Robin | Why |
|---|:--:|:--:|---|
| **Lesser Evil** | ✅ escapes | ✅ escapes | no wasted vote — score/rank everyone honestly; a third candidate never spoils |
| **Center Squeeze** | ✅ escapes | ✅ escapes | the scoring round + runoff (STAR) and pairwise wins (RR) find the broadly-liked center IRV eliminates |
| **Dark Horse** | ✅ escapes | ✅ escapes | a score lets you zero-out a rival *without* propping up the nobody; RR rewards no such burial |
| **Chicken / Burr** | ⚠️ softens | ✅ escapes | STAR's runoff makes the slippery Approval slope *non-slippery*; RR just lets the majority beat the third candidate |
| **Condorcet Cycle** | ➖ shares | ➖ shares | [Gibbard](gibbard_satterthwaite_theorem.md): no method escapes; cycles are rare (~1–5%) and must be resolved somehow |

**The honest tally: STAR escapes three cleanly, softens one, and shares one with every method that exists.** Ranked Robin escapes four and shares the fifth. Neither is strategy-*proof* — Gibbard forbids that for any real method — but both dodge the traps that actually bite in practice.

> **Fine print (three caveats the scorecard glosses, raised in the discussion of Quinn's originals):**
> - **PR doesn't fully kill Lesser Evil.** Proportional representation softens it, but any **threshold** recreates a milder wasted-vote fear — a small new party below the cutoff still feels unsafe to support. Escape is partial, not total.
> - **Ranked Robin has its own, sincere dark horse.** RR escapes the *strategic Borda* Dark Horse (above), but a Condorcet method can crown a **thinly-supported unknown** everyone merely tolerates as a second choice — a real [RR limit](../RCV_Ranked_Robin/RCV_RR_honest_limits.md). STAR resists *both*, because it reads **support**, not just order ([preference vs support](../scores_and_ranks/preference_vs_support.md)). So on Dark Horse, STAR is a touch ahead of RR.
> - **Arrow only binds ordinal methods.** The impossibility that dooms *ranked* methods (Arrow) doesn't apply to a cardinal ballot — which is why STAR escapes Arrow but **not** Gibbard ([STAR escapes Arrow, not Gibbard](arrow_theorem_and_star.md)). The Condorcet-cycle row is a **Gibbard** limit, not an Arrow one.

## The five, one paragraph each

**Lesser Evil (FPTP).** The one you already live under. When you can only pick one, voting your true favorite "wastes" your vote, so you're pushed to the least-bad *viable* option — and the field collapses toward two poles. Score and pairwise ballots remove the wasted-vote fear entirely. → [spoiler effect](spoiler_effect.md).

**Center Squeeze (IRV).** Fix wasted votes with instant-runoff and you get a new trap: a broadly-liked centrist with few *first* choices is eliminated early, even though they'd beat either wing head-to-head — so their would-be supporters, by ranking them honestly, help elect the candidate they like least. This is the library's most-documented pathology. → [center squeeze](../../method_comparisons/center_squeeze/), [favorite betrayal](../../method_comparisons/favorite_betrayal_irv/), and the real [Alaska 2022](../../method_comparisons/alaska_2022/) and [monotonicity](../../method_comparisons/monotonicity/) cases.

**Dark Horse (Borda).** Under a strictly-ranked point method, the only way to oppose a rival is to rank *someone* above them — so factions bury their rivals behind a harmless nobody, and if everyone does it, the nobody wins with **zero honest support**. A prisoner's dilemma. A score ballot lets you oppose without being forced to support. → [the Dark Horse](../../method_comparisons/dark_horse_borda/).

**Chicken / Burr (Approval).** Two allies must cooperate to beat a third, but honest cooperation leaves them tied, so each is tempted to bullet-vote — a slippery slope that can hand victory to the majority-opposed candidate. STAR's runoff converts the *slippery* slope to a *non-slippery* one (the same fix as Quinn's [3-2-1](three_two_one_voting.md)): support both allies honestly, and a few defectors can't start an avalanche. → [the chicken dilemma](../../method_comparisons/chicken_dilemma/).

**Condorcet Cycle (universal).** Sometimes a majority prefers A to B, B to C, *and* C to A — a rock-paper-scissors with no honest winner. This is at the heart of the proof that **no** method escapes strategy ([Gibbard–Satterthwaite](gibbard_satterthwaite_theorem.md)). Cycles are genuinely rare (~1–5% in realistic models and empirical data), and every method — STAR and Ranked Robin included — must simply resolve them somehow. → [cycle resolution](../RCV_Ranked_Robin/cycle_resolution.md).

## The takeaway

The Molochs aren't a reason to despair of voting reform — they're a **method-selection tool**. Four of the five can be *designed away*; only the Condorcet cycle is permanent, and it's both rare and mild. The lesson Quinn draws, and the one this library's cases keep landing on:

> **Don't force voters to dishonestly support one candidate merely to oppose another.** A ballot that lets you say *how much* you like each option — independently — sidesteps Dark Horse and softens Chicken; a runoff or pairwise check sidesteps Center Squeeze and Lesser Evil. That's [STAR](../STAR_Voting/STAR_start_here.md) and [Ranked Robin](../RCV_Ranked_Robin/README.md), and it's why they hold up against a scorecard built by someone rooting for neither.

## Sources

- Jameson Quinn, *The Six Voting Molochs* — the framing and the four constructed scenarios (Dark Horse, Lesser Evil, Center Squeeze, Chicken). Advocacy-adjacent (Quinn favors Approval/3-2-1); used here as an outside lens, with every result reproduced in-repo.
- [Gibbard–Satterthwaite theorem](gibbard_satterthwaite_theorem.md) — why no method is strategy-proof (the cycle is the seed of the proof).
- Scott Alexander, *Meditations on Moloch* — the "Moloch" metaphor for multipolar coordination traps that Quinn borrows.
