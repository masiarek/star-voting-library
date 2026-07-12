# Forced vs. Voluntary Exhaustion — two exhausted ballots that deserve different names

Two very different things get lumped under the single word *"exhausted."* One is a voter's own choice and no cause for complaint. The other is the ballot design failing a voter who did everything right. They deserve distinct names — because collapsing them lets the whole problem be waved away as *"well, that was the voter's choice."*

This page is the fine-grained companion to **[Exhausted (Inactive) Ballots](RCV_IRV_exhausted_ballots.md)**.

## The two kinds

**Voluntary exhaustion** — *self-truncation.* You chose to rank fewer candidates than you were allowed (maybe only your favorite). If those candidates are eliminated, your ballot exhausts. That's the direct, foreseeable consequence of **your own choice** — a legitimate thing to do, and not a flaw in the method. *(Standard term: voluntary truncation.)*

**Forced exhaustion** — *the ballot dropped out even though you ranked every candidate you were permitted to.* You were as expressive as the rules let you be, and the count still discarded your ballot. This one **isn't your choice** — it's imposed by the ballot design. *(Standard term: involuntary truncation. "Forced exhaustion" is this library's house label for it, because "involuntary truncation" buries the point — the voter didn't truncate anything; the ballot did.)*

## The key fact that makes "forced" the right word

**In single-winner RCV-IRV, a *fully-ranked* ballot can never exhaust.** If you rank every candidate, one of them is always still in the race until the final winner is chosen — so there's always somewhere for your vote to go.

Therefore **forced exhaustion can only happen under a ranking cap** — when the ballot lets you rank fewer candidates than are running (New York City: **5**; Minneapolis: **3**). You rank all 5 you're given; if all 5 are eliminated before the final round while 8 other candidates fight on, your ballot exhausts — not because you held back, but because the ballot **wouldn't let you** rank the rest.

The consequence is clean and important:

> **Forced exhaustion is a property of the ballot design (the ranking cap), not of the voter.** Lift the cap — let voters rank the whole field — and forced exhaustion in single-winner IRV disappears entirely. Voluntary exhaustion is the only kind left, and that one is a choice.

*(Caveat: this "fully-ranked can't exhaust" guarantee is specific to single-winner IRV. Multi-winner **STV** can exhaust even a fully-ranked ballot through quota/surplus transfers — a different mechanism.)*

## A worked micro-example

Six candidates — **A B C D E F** — but the ballot caps you at **3** rankings.

- A voter's true order is `C > E > A > B > D > F`. They rank the top three they're allowed: **C, E, A**.
- Rounds eliminate F, then D, then **C**, then **E**, then **A** — all three of the voter's ranked choices are gone before the final **B vs. D**… wait, D is already out; say the final is **B vs. F-survivor**. The point holds: once **C, E, A** are all eliminated, the ballot has **no continuing candidate** and exhausts — even though this voter would gladly have ranked **B** fourth and had a say in the final round.

Their neighbour who *chose* to bullet-vote **C** only also exhausts — but that was a choice. Same outcome on the tally sheet; **completely different stories**, and only one is the system's fault. That's why one word for both is misleading.

## Why the distinction matters

- **It changes who's responsible.** "Exhaustion is just voters choosing not to rank everyone" is only true of the *voluntary* kind. Forced exhaustion is the method (plus a cap) discarding a maximally-expressive ballot — and it's **fixable** by removing the cap.
- **The cap makes it common where it's least visible.** In a large field the cap bites hardest. New York City's 2021 mayoral primary ran **13** candidates against a **5**-rank cap; a large share of the exhaustion there was *forced*, not chosen.
- **It's uneven.** Voters who rank an underdog or a minor candidate first burn their limited slots on candidates who get eliminated early — so the cap force-exhausts *their* ballots more than mainstream voters', quietly tilting the result.

## Methods that don't force-exhaust

- **[Ranked Robin](../RCV_Ranked_Robin/ranked_robin.md)** (Condorcet) reads every ballot in every pairwise contest — no eliminations, so nothing exhausts, forced or voluntary.
- **Scored methods** (STAR, Score, Approval) never drop a ballot: a blank reads as **0** and still counts. (A different trade-off — a 0 is a real lowest score, not a neutral abstention — but the ballot never *leaves* the count.) See [scores vs. ranks](../scores_and_ranks/scores_vs_ranks.md).

## Related

- [Exhausted (Inactive) Ballots — the full picture](RCV_IRV_exhausted_ballots.md) (the two-failures section, real-election rates, and the proponent's fair rebuttal)
- [Strict vs. weak ranks](../scores_and_ranks/strict_vs_weak_ranks.md) — ranking limits and forbidden equal ranks
- [Ranked Robin](../RCV_Ranked_Robin/ranked_robin.md) — reads the whole ballot, never exhausts
- [Glossary](../GLOSSARY.md)
