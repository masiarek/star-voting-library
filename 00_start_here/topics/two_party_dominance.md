# Two-Party Dominance — the case for it, the case against, and what actually changes it

"Break the two-party system" is a rallying cry for a lot of voting reformers — but two-party dominance is **not** self-evidently bad, and plenty of thoughtful people defend it. A reform library that only prosecutes it isn't teaching; it's campaigning. So this page steelmans **both** sides, then draws the one distinction that actually matters for voting methods: **what makes two-party dominance change, and what doesn't.**

## The case *for* two-party systems

These aren't strawmen — they're the serious arguments, and some are backed by real political science:

- **Governability.** A two-party system usually hands one party a working majority, so a government can pass a coherent program instead of haggling a fragile coalition into existence. Fragmented multiparty parliaments can produce paralysis, frequent collapses, or caretaker governments (the cautionary tales: interwar Weimar, post-war Italy, some periods in Israel).
- **Accountability.** Voters know who is in charge and whom to blame, and power alternates cleanly. No voter wakes up to a coalition government that no one actually voted for, assembled in back-room deals after the election.
- **Moderation (the median-voter pull).** In classic Downsian theory, two big parties compete for the *center*, forcing each toward the median voter — a centripetal, moderating force. Both parties are broad coalitions that must aggregate diverse interests *before* the election rather than after.
- **No extremist kingmakers.** In a fragmented legislature a small radical party can hold the balance of power and extract outsized concessions. Two-party systems deny fringe parties that leverage.
- **Simplicity.** Two clear choices are low-information and easy to reason about.

## The case *against*

- **Limited choice / "lesser of two evils."** Large blocs of voters have no party that fits them; many feel they're voting against, not for.
- **Underrepresentation.** Third parties and independents can win substantial vote shares yet almost no seats — a persistent votes-to-seats gap (e.g. Australia's Greens under the [Alternative Vote](../RCV_IRV/case_studies/RCV_IRV_australia.md)).
- **Duopoly and safe seats.** With only two viable brands and many uncompetitive districts, the two parties face little real competition and can quietly collude to keep others out.
- **Polarization.** The moderating pull is a *tendency*, not a law — modern US politics shows a two-party system can instead calcify into intense polarization, negative partisanship, and gridlock, with primaries dragging candidates *away* from the center.
- **It can be manufactured, not chosen.** When two-party dominance is propped up by the [spoiler effect](spoiler_effect.md) and vote-splitting, it may reflect the *voting method* punishing alternatives rather than the electorate's genuine preferences.

## Where the scholarship lands

There's no free lunch. The standard framing (Arend Lijphart, *Patterns of Democracy*) contrasts **majoritarian** democracies (two-party, single-party governments, clear accountability) with **consensus** democracies (multiparty, proportional, broad power-sharing). Each buys something and pays for it: majoritarian systems trade breadth of representation for decisiveness and clarity; consensus systems trade decisiveness for inclusion and (Lijphart argues) at least as good policy outcomes on many measures. *Which* trade-off is "better" is a values question, not a settled fact — which is exactly why this page doesn't rule on it.

## The part that's about voting methods (and the honest caveat)

Here is the distinction reformers most often blur. Two-party dominance has **two different sources**, and different fixes touch different sources:

1. **Spoiler-enforced dominance.** Under [choose-one plurality](plurality.md), a third-party vote can help elect your *worst* choice, so voters and donors abandon alternatives pre-emptively. This part is a **voting-method artifact** — and **better single-winner methods remove it.** STAR, Approval, Ranked Robin, and IRV all let you support a favorite without spoiling, so new parties can *run and grow* without being blamed as spoilers.

2. **Structural (Duverger) dominance.** Even with the spoiler gone, [**single-member districts are majoritarian**](https://en.wikipedia.org/wiki/Duverger%27s_law): each seat has exactly one winner, so the system still tends toward two big blocs. Australia's century under the Alternative Vote is the proof — no spoiler problem, and *still* two-party-preferred in the lower house.

So the honest claim, which cuts against a common overreach:

> **Better single-winner methods end the *spoiler-enforced* part of two-party dominance — they do not, by themselves, end two-party dominance.** What reliably produces a multiparty legislature is **proportional representation** ([STV](../proportional_representation/stv/proportional_stv_vs_star.md), MMP, party-list, [proportional STAR](../proportional_representation/STAR_PR/README.md)) — multi-winner methods, not single-winner ones.

This is why Australia is two-party in its AV House but multiparty in its **STV** Senate. If your goal is specifically to *break* two-party dominance, single-winner reform is necessary-but-not-sufficient; the lever is proportional multi-winner elections. If your goal is honest, spoiler-free single-winner elections (a worthy goal on its own), STAR/Approval/Ranked Robin deliver that whether or not the party system ever changes.

## How do you *count* parties? (ENP)

"Two-party" and "multiparty" sound obvious until you try to measure them — a country with two giants and five specks isn't a seven-party system in any meaningful sense. The standard fix is the **[Effective Number of Parties](../GLOSSARY.md)** (Laakso–Taagepera):

```
ENP = 1 / Σ(sᵢ²)      where sᵢ is party i's share of votes or seats
```

Squaring the shares makes big parties dominate the sum, so tiny parties barely move it. Four equal parties give ENP = 4; one dominant party with three specks gives barely above 1. In practice the **US sits near 2**, while highly proportional systems like **Israel exceed 6**.

Two things this buys you. First, it makes the claim above **testable** rather than rhetorical: you can check whether a reform actually changed the party system, instead of arguing about it. Second, it reframes the trade-off on this page as a *dial*, not a binary — the [Lijphart](#the-case-for-two-party-systems) argument is really about where on that dial a country wants to sit. [Jameson Quinn](in_memoriam_jameson_quinn.md) has argued the sweet spot is around **3–4**: enough parties to escape zero-sum, us-versus-them politics, but few enough that each must still assemble a broad coalition rather than campaign on one narrow issue. That figure is a judgment call, not a finding — but the *metric* is standard.

## Takeaway

Two-party dominance is a genuine trade-off, not a self-evident evil — it buys governability and accountability at the cost of choice and representation, and reasonable people weigh those differently. And whatever you think of it, be precise about the mechanism: **the spoiler effect is method-caused and fixable with better single-winner voting; the deeper two-party tendency of single-member districts is structural and only proportional representation changes it.**

## Related

- [The spoiler effect](spoiler_effect.md) · [Choose-One / plurality](plurality.md) — the method-caused half
- [The Alternative Vote in Australia](../RCV_IRV/case_studies/RCV_IRV_australia.md) — two-party House, multiparty (STV) Senate
- [Proportional representation: STV vs STAR-PR](../proportional_representation/stv/proportional_stv_vs_star.md) · [Proportional STAR](../proportional_representation/STAR_PR/README.md) — what actually yields multiparty legislatures
- [Choosing among the Equal Vote methods](choosing_among_evc_methods.md) · [Glossary](../GLOSSARY.md)
