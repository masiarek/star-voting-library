<!-- Unlisted. One of the Mudroom's per-method reels. Deliberately one-sided; fair versions linked. -->
# The Ranked Robin Whoops Files 🍿 — mud for the consensus darling too

> **⚠️ Deliberately unfair, and it's about a method this repo *likes*.** Ranked Robin (Condorcet/Copeland) is the library's olive branch to ranked-choice voters — same ballot, a monotonic, summable, center-squeeze-free count. So naturally it gets the same mud-bucket as everyone else in the [Mudroom](README.md). Every "whoops" is real and conceded in [RR's honest limits](../../00_start_here/RCV_Ranked_Robin/RCV_RR_honest_limits.md); the curation is the unfair part.

*Condorcet methods look unbeatable — until the electorate refuses to have a "beats-everyone" candidate at all.*

---

## 🥇 The signature flaw: cycles

- **No Condorcet winner exists.** A majority prefers A>B, B>C, *and* C>A — rock-paper-scissors, so "elect the head-to-head winner" has nothing to elect. Ranked Robin falls back on a tiebreak (most wins → margin → lot), which is a *choice*, not a discovery. → [cycle resolution](../../00_start_here/RCV_Ranked_Robin/cycle_resolution.md); a live one in the [reversal-symmetry case](../reversal_symmetry/) (that 24-voter electorate is a cycle). This is [Gibbard](../../00_start_here/topics/gibbard_satterthwaite_theorem.md) collecting his due — no method escapes it, RR included.

## 🥈 Order without strength

- **The sincere dark horse.** Because a ranked ballot sees *order, not intensity*, RR can crown a **thinly-supported unknown** everyone merely tolerates as a second choice over a candidate a majority passionately prefers — "somebody 90% of voters never heard of," each side ranking them above the *other* side. → [RR's honest limits](../../00_start_here/RCV_Ranked_Robin/RCV_RR_honest_limits.md) and [the sincere dark horse](../dark_horse_borda/). (This is exactly the [preference-vs-support](../../00_start_here/scores_and_ranks/preference_vs_support.md) blind spot — the one thing STAR reads and RR can't.)

## 🥉 The bureaucratic whoops

- **Tie-broken by lot — and engines disagree.** Copeland ties get resolved by total margin, then a random lot; and LH breaks a Copeland tie differently from BetterVoting (margin→lot vs head-to-head→random), so the "winner" of a knife-edge RR race can depend on *which counter you use*. → [RR tiebreak, LH vs BV](../../00_start_here/RCV_Ranked_Robin/rr_tiebreak_lh_vs_bv.md).
- **Copeland's clone wrinkles.** Simple win-counting can be nudged by adding clone candidates in some constructions. → [RR clone independence](../../00_start_here/RCV_Ranked_Robin/rr_clone_independence.md).

---

## The conscience clause

The fair version, because the Mudroom insists:

- **Cycles are genuinely rare** (~1–5% in realistic models and empirical data), and *every* method must resolve them somehow — RR is not uniquely cursed here.
- RR **avoids** the failures that actually bite in real elections — it has *no* center squeeze and *no* non-monotonicity, which is more than IRV can say.
- The intensity-blindness is the honest cost of a *ranked* ballot; it's why STAR pairs scores with a runoff — a real distinction, not a knock that makes RR "bad."
- RR remains a strong, summable, honest method and the repo's genuine bridge to RCV voters. Mud thrown; respect intact.

For the version you'd actually cite, use [RR's honest limits](../../00_start_here/RCV_Ranked_Robin/RCV_RR_honest_limits.md).
