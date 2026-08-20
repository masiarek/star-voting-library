<!-- Unlisted. One of the Mudroom's per-method reels. Deliberately one-sided; fair versions linked. -->
# The Ranked Robin Whoops Files 🍿 — mud for the consensus darling too

> **⚠️ Deliberately unfair, and it's about a method this repo *likes*.** Ranked Robin (Condorcet/Copeland) is the library's olive branch to ranked-choice voters — same ballot, a monotonic, summable, center-squeeze-free count. So naturally it gets the same mud-bucket as everyone else in the [Mudroom](README.md). Every "whoops" is real and conceded in [RR's honest limits](../../05_Ranked_Robin/01_Learn/RCV_RR_honest_limits.md); the curation is the unfair part.

*Condorcet methods look unbeatable — until the electorate refuses to have a "beats-everyone" candidate at all.*

---

## 🥇 The signature flaw: cycles

- **No Condorcet winner exists.** A majority prefers A>B, B>C, *and* C>A — rock-paper-scissors, so "elect the head-to-head winner" has nothing to elect. Ranked Robin falls back on a tiebreak (most wins → [1st Degree → 2nd Degree](../../05_Ranked_Robin/03_Criteria/rr_tiebreaks/degrees_of_ties.md) → lot), which is a *choice*, not a discovery. → [cycle resolution](../../05_Ranked_Robin/01_Learn/cycle_resolution.md); a live one in the [reversal-symmetry case](../reversal_symmetry/README.md) (that 24-voter electorate is a cycle). This is [Gibbard](../../07_Concepts/topics/gibbard_satterthwaite_theorem.md) collecting his due — no method escapes it, RR included.

## 🥈 Order without strength

- **The sincere dark horse.** Because a ranked ballot sees *order, not intensity*, RR can crown a **thinly-supported unknown** everyone merely tolerates as a second choice over a candidate a majority passionately prefers — "somebody 90% of voters never heard of," each side ranking them above the *other* side. → [RR's honest limits](../../05_Ranked_Robin/01_Learn/RCV_RR_honest_limits.md) and [the sincere dark horse](../dark_horse_borda/README.md). (This is exactly the [preference-vs-support](../../07_Concepts/scores_and_ranks/preference_vs_support.md) blind spot — the one thing STAR reads and RR can't.)

## 🥉 The bureaucratic whoops

- **Tie-broken by lot — and nobody implemented the ladder.** Ranked Robin ships with a four-rung tie-break protocol, and for two years *neither* engine in this repo ran it: BetterVoting handles only a two-way tie and shuffles anything bigger, while this library's own engine skipped straight to the whole-field margin rung and could hand the race to a candidate who lost the finalists' own match. Both are now known bugs rather than rival conventions — ours [fixed on 2026-08-19](../../05_Ranked_Robin/03_Criteria/rr_tiebreaks/degrees_of_ties.md), BV's filed as [#1469](https://github.com/Equal-Vote/bettervoting/issues/1469) — but the mud stands: a method whose tie-break is subtle enough that two independent implementations both got it wrong is a method whose knife-edge races were decided by *which counter you used*. → [degrees of ties](../../05_Ranked_Robin/03_Criteria/rr_tiebreaks/degrees_of_ties.md).
- **Copeland's clone wrinkles.** Simple win-counting can be nudged by adding clone candidates in some constructions. → [RR clone independence](../../05_Ranked_Robin/01_Learn/rr_clone_independence.md).

---

## The conscience clause

The fair version, because the Mudroom insists:

- **Cycles are genuinely rare** (~1–5% in realistic models and empirical data), and *every* method must resolve them somehow — RR is not uniquely cursed here.
- RR **avoids** the failures that actually bite in real elections — it has *no* center squeeze and *no* non-monotonicity, which is more than IRV can say.
- **The tie-break mud lands on the counters, not on the method.** Ranked Robin's degrees of ties were published, worked and four rungs deep the whole time; two implementations failed to follow them, in opposite directions. That is an argument for reading the spec, not against the method — and this repo's engine was one of the two, which is why the story is told here rather than filed under someone else's failures.
- The intensity-blindness is the honest cost of a *ranked* ballot; it's why STAR pairs scores with a runoff — a real distinction, not a knock that makes RR "bad."
- RR remains a strong, summable, honest method and the repo's genuine bridge to RCV voters. Mud thrown; respect intact.

For the version you'd actually cite, use [RR's honest limits](../../05_Ranked_Robin/01_Learn/RCV_RR_honest_limits.md).
