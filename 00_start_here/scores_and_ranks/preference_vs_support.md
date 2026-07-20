# Preference vs. Support — the two things a score says that a rank can't

*The single most useful idea for understanding score ballots. A **ranking** asks one question — "which do you like **more**?" A **score** asks two — "which do you like **more**?" *and* "**how much** do you like each?" The first is **preference** (order). The second is **support** (level). Ranks keep the first and throw away the second — which is exactly the information that tells a winner everyone loves apart from a winner nobody wanted.*

→ The general form of this distinction: [scores vs. ranks](scores_vs_ranks.md). This page is the vivid special case.

---

## The example that makes it click

Four candidates. Two ballots:

| | A | B | C | D |
|---|:--:|:--:|:--:|:--:|
| **Ballot 1** | 1 | 0 | 1 | 0 |
| **Ballot 2** | 5 | 4 | 5 | 4 |

**Same preference:** both say *A and C over B and D* (with A = C and B = D). **Opposite support:** Ballot 1 says *"none of these, really — but if you're making me choose, the odd ones"*; Ballot 2 says *"honestly, all four are fine — the odd ones by a hair."*

Now write each as a **ranking**. Both collapse to the *identical* ballot:

> **A = C  >  B = D**

The ranking **cannot tell them apart.** The reluctant voter and the enthusiastic voter are recorded as saying the exact same thing. Everything that separated *"I tolerate them"* from *"I love them"* — the **support** — is gone.

## The two questions, named

- **Preference** — *which* do you like more? A **relative / order** question: "A over B." Every ballot format can answer it.
- **Support** — *how much* do you like each one, on its own? An **absolute / level** question: "A is a 5; B is a 1." Only a rated (score) ballot answers it.

A rank is pure preference. A score is preference **and** support in a single mark.

## The race analogy

A ranking is a race that records only the **finishing order** — not the **times**, and not whether anyone actually ran fast. A photo finish between two world-record sprinters and a photo finish between two people crawling backwards produce the *same order column*: "1st, 2nd." You'd never make a hire or a policy call on finishing order while ignoring the clock — but a ranked ballot does exactly that. **Scores keep the clock.**

## Why it matters

1. **A mandate vs. a resignation.** A candidate can win by *preference* while having almost no *support* — the "least-bad" pick of a field nobody liked. Ranks can't tell "won a race everyone wanted" from "won a race everyone wanted to leave." Scores can: the [scoring round](../STAR_Voting/the_count/STAR_Scoring_Round.md) shows a winner averaging 4.5/5 (a mandate) versus 1.2/5 (a resignation) — same order, opposite legitimacy.
2. **Protest and honest indifference.** A score ballot lets you say *"I have a slight preference but I support none of you"* (`1,0,1,0`) — or *"I'm happy with the whole field"* (`5,4,5,4`). A ranking forces you to hand in an order as if you endorse it, hiding whether you actually back anyone.
3. **Consensus vs. compromise.** Support is how you tell a broadly-loved [consensus winner](../topics/what_makes_a_good_winner.md) from a barely-tolerated compromise — *even when they share the same preference order.*
4. **STAR uses both, on purpose.** [STAR](../STAR_Voting/STAR_start_here.md) reads **support** to pick the two finalists (the scoring round) and **preference** to choose between them (the [automatic runoff](../STAR_Voting/the_count/STAR_Automatic_Runoff.md)). Drop the support half and you're back to a ranked method that can't tell the sprinters from the crawlers.

## The honest cost of support

Support isn't free, and this library doesn't pretend it is. Reading *level* means trusting voters to use the scale sincerely — a strategic voter can min/max `1,0,1,0` into `5,0,5,0` and throw the support away ([strategic voting](../topics/strategic_voting.md)) — and adding scores across voters leans on comparing one person's "5" to another's. Pure preference sidesteps both. That's the [cardinal-vs-ordinal tradeoff](../topics/arrow_theorem_and_star.md), and it's exactly why STAR pairs the support-reading scoring round with a *preference* runoff, rather than trusting the raw sum alone.

## Related

- [Scores vs. ranks](scores_vs_ranks.md) — the general form of this distinction (relative vs. absolute)
- [The score ballot](score_ballot.md) · [the fidelity ladder](fidelity_ladder.md) — a score carries both; converting *down* to a rank loses the support, converting *up* has to fabricate it
- [What makes a good winner?](../topics/what_makes_a_good_winner.md) — the utilitarian (**support**) vs. majoritarian (**preference**) ideals, and why they can disagree
- [The equally weighted vote](../STAR_Voting/properties_and_limits/equally_weighted_vote.md) — equal *scores* say "preference: none, support: full," a distinction a rank can't record
- Glossary: [`score ballot`](../GLOSSARY.md)
