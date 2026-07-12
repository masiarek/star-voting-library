# STAR for skeptics — the honest 5-minute path

*You think scoring candidates sounds gimmicky, you're not convinced anything's really broken, and "sounds too good" makes you suspicious. Fair — good instincts. This page meets you there: no cheerleading, just the fast honest path, and every claim below is backed by an election you can re-count yourself in this repo.*

**Level: 201.** If you came from the RCV camp specifically, jump to [STAR vs RCV-IRV](../rcv_irv_vs_star.md).

**"This looks like a gimmick."**
It's two steps of grade-school arithmetic: add up the 0–5 scores, then the top two have a runoff. You can [count it by hand](count_star_by_hand.md) — it's *simpler* to tally than most reforms, including RCV.

**"Why change at all — what's actually broken?"**
Choose-one voting splits similar candidates and can elect the option most people *didn't* want — the [spoiler effect](../spoiler_effect.md). That's why people vote "lesser evil" instead of who they like. See it in 60 seconds: [the team lunch](../../01_STAR/_main/_main_pages/bv2184_fyy886_lunch_vote.md).

**"Isn't ranked-choice (RCV) already the fix everyone's pushing?"**
RCV-IRV is better than choose-one, but it has real, specific failures: it can eliminate the broadly-preferred centrist ([center squeeze](../RCV_IRV/RCV_IRV_center_squeeze.md)); ranking a candidate *higher* can make them *lose* ([non-monotonic](../RCV_IRV/RCV_IRV_non_monotonicity.md) — [watch it flip](../../method_comparisons/monotonicity/)); and it isn't precinct-summable, so it's hard to hand-count and audit. Those aren't STAR talking points — they're in the neutral [criteria table](../criteria_at_a_glance.md) as runnable elections. STAR isn't RCV-IRV.

**"Scores can be gamed — won't everyone just vote 5s and 0s?"**
The runoff removes the payoff. Your in-between scores still choose the finalists, but the winner is decided by simple preference between the top two — so exaggerating doesn't pay. Simulations rate STAR the most **[strategy-resistant](../strategic_voting.md)** of the common methods, and even the worst case just makes it behave like [Approval](../Approval_Voting/approval_voting.md) — still a good method, not a broken one.

**"Sounds too good. What's the catch?"** — *the real question, and the one that should decide it.*
Here's the honest catch: **no voting method is perfect — that's a theorem** ([Gibbard–Satterthwaite](../gibbard_satterthwaite_theorem.md)). STAR fails [later-no-harm and favorite-betrayal](STAR_honest_limits.md) in rare constructed cases, is **not** a [Condorcet method](../topics/condorcet/) (it can miss a beats-everyone candidate), and asks a bit more of voters than a single mark. This repo states all of it out loud on the [honest limits](STAR_honest_limits.md) page. A reform that *hides* its weaknesses is the one to distrust; the honest read is that STAR's trade-offs are good ones, not that it has none.

**"Is it even real, or a math toy?"**
Used by real organizations and political parties since 2019; **not** yet adopted by any government (recent Oregon ballot measures fell short). The honest, current picture: [Is STAR actually used?](common_misunderstandings.md)

## The skeptic's real advantage here

You don't have to take any of this on faith. **This repo exists so you can check** — every claim above is a small [YAML election you can re-tabulate](../why_yaml_test_cases.md) with an independent engine, cross-checked against a real platform. So don't believe the advocates (including us); verify:

- [Criteria at a glance](../criteria_at_a_glance.md) — where STAR *does and doesn't* win, each failure a runnable case
- [STAR's honest limits](STAR_honest_limits.md) — the weaknesses, stated plainly
- [Common misunderstandings](common_misunderstandings.md) — the gut objections, answered honestly
- [Do the experts really think RCV-IRV is "bad"?](../expert_consensus_and_irv.md) — even the pro-STAR expert consensus, graded skeptically

You don't have to love STAR. But it's a serious, checkable proposal — and the fact that this library tests it *against* every rival, and concedes where it loses, is itself the reason to take it seriously.
