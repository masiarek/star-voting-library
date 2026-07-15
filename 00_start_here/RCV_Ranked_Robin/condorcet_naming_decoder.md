# Round-robin, Copeland, Condorcet, Ranked Robin — a naming decoder

*One family of voting methods, half a dozen names, and two Wikipedia articles that overlap so much they look redundant. If "the Condorcet family" has ever left you unsure whether **round-robin voting**, **Copeland's method**, and **Ranked Robin** are the same thing or different things — you're not confused, the names genuinely blur. This page maps them, links where each is defined, and flags the sources to read critically.*

**Level: reference** (a 201/301 aid). The teaching page for the method itself is [Ranked Robin](ranked_robin.md); this is just the terminology map.

## The one-line answer

> **round-robin voting** (the family) ⊃ **Copeland's method** (the algorithm) ≈ **Ranked Robin** (a branded Copeland variant).

They're at *different levels of generality* — a category, a specific method in it, and a brand name for a tweaked version of that method. Say "Condorcet" or "round-robin" when you mean the family; say "Ranked Robin" only for the specific branded method.

## The map

| Term | What level | Who uses it | Defined at |
|---|---|---|---|
| **Condorcet method(s)** | the **family** (traditional academic name) | social-choice theory | [Wikipedia](https://en.wikipedia.org/wiki/Condorcet_method) |
| **Round-robin voting** | the **family** (a newer umbrella name) | Wikipedia's recent reframing; reform advocates | [Wikipedia](https://en.wikipedia.org/wiki/Round-robin_voting) |
| **Pairwise / paired-comparison** | the **family** (plain-descriptive) | general | — |
| **Copeland's method** | the **algorithm** — most head-to-head wins (½ per tie) | academic; originated by [Ramon Llull](https://en.wikipedia.org/wiki/Ramon_Llull) ~1299 | [Wikipedia](https://en.wikipedia.org/wiki/Copeland%27s_method) |
| **Ranked Robin** (**RCV-RR**) | a **branded method** — Copeland + a defined cycle tiebreak (sum of win margins) | Equal Vote Coalition (name coined by Sara Wolk, 2021) | [electowiki](https://electowiki.org/wiki/Ranked_Robin) · [equal.vote](https://www.equal.vote/ranked_robin) |
| **Consensus Voting** | a **brand alias** for Ranked Robin | Equal Vote / STAR-adjacent marketing | [equal.vote](https://www.equal.vote/ranked_robin) |
| **Consensus Choice** | a **sibling brand** (Copeland-family, different tiebreak) | *Better Choices for Democracy* | — |
| ~~**RCV-RR**~~ | *this repo's* house shorthand — **not** an external term | — | — |

Other members of the *round-robin / Condorcet* family — **Minimax**, **Ranked Pairs**, **Schulze**, **Kemeny** — sit beside Copeland; they differ in *how* they use the same pairwise results (defeat-dropping or path strength rather than simple win-counting). See [the ranked-ballot zoo](../topics/ranked_ballot_methods_zoo.md).

## Why the two Wikipedia articles overlap (the trap you hit)

[Round-robin voting](https://en.wikipedia.org/wiki/Round-robin_voting) and [Copeland's method](https://en.wikipedia.org/wiki/Copeland%27s_method) feel redundant for a concrete reason: **one is the family, the other is its simplest member** — and Copeland is the method that most *literally* implements "round-robin tournament standings," so the category name and the method sound identical. Two extra wrinkles:

- **"Round-robin voting" as the umbrella name is a recent Wikipedia reframing** of what was long just called "Condorcet methods." That renaming has seen editorial back-and-forth (it makes the family sound friendlier and less mathematical), and the churn is part of why the articles feel unsettled.
- **Neither article pins down "Ranked Robin"** — it's a brand for a Copeland *variant*, so its natural home is the Copeland article as a sourced aside, not the category article. (If you're tempted to add it: it rests almost entirely on advocacy sources, so it needs an independent one, and — for a STAR-aligned editor — a [conflict-of-interest](https://en.wikipedia.org/wiki/Wikipedia:Conflict_of_interest) disclosure and a Talk-page proposal.)

## Read the sources knowing where they lean

- **[electowiki](https://electowiki.org/wiki/Ranked_Robin)** is the canonical definition for the *Ranked Robin* name — but it's a community wiki, **reform-advocacy-adjacent**. Cite it for definitions; lean on academic sources for critical/limits claims.
- **[equal.vote](https://www.equal.vote/ranked_robin)** is the promoter (**STAR / Equal Vote** camp) — the source for the brand, not a neutral referee.
- **Wikipedia / academic** ("Condorcet method," "Copeland's method") is the neutral ground — but note the "round-robin voting" umbrella framing is itself contested.

(Fuller roster of who-leans-where: [advocacy organizations](../topics/advocacy_organizations.md) · [who's who](../topics/whos_who_voting_reform.md).)

## The clear version, in this repo

- [Ranked Robin](ranked_robin.md) — the method, taught (with the "Names & family" section this page expands)
- [Terminology — the ranked-method family tree](../tips/TIPS_terminology.md#the-ranked-method-family-tree) — the diagram of where every method sits
- [Ranked Robin vs. Condorcet](ranked_robin_vs_condorcet.md) — why a *cycle* leaves "the Condorcet winner" blank while Ranked Robin still elects one
- [The math behind Condorcet](the_math_behind_condorcet.md) — tournaments, Smith/Schwartz, the impossibility theorems
- [Glossary](../GLOSSARY.md)
