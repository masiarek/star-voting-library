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

## The tier the brands never mention (C1 / C2 / C3)

The table above maps the *marketing* names. The academic literature sorts the same family a different way — by **how much of the pairwise data a rule actually needs** — and knowing this one scheme, from [Fishburn (1977)](../topics/condorcet/condorcet_reading_list.md), stops most cross-talk before it starts:

| Class | Reads | Members |
|---|---|---|
| **C1** | only **who beat whom** (the tournament; margins discarded) | **Copeland** → **Ranked Robin**, Smith set, Schwartz set, Top Cycle |
| **C2** | the **margins** too | Minimax, Ranked Pairs, Schulze, Kemeny, Split Cycle |
| **C3** | must return to the ballots and iterate | Dodgson, Young |

Two things fall out of it. **"Tournament solution" means the C1 tier specifically** — not the whole family — so a theorem proved about tournament solutions doesn't automatically apply to Minimax. And **the tiers only diverge in a cycle**: when a Condorcet winner exists, every rule in every tier elects the same person, which is why so much of the literature argues about a rare case. → [the full reading list, with sources and leans](../topics/condorcet/condorcet_reading_list.md).

## The word "consensus" carries three different jobs

The table above lists *Consensus Voting* as a brand. But the word shows up in this repo, and across the web, in **three senses at different altitudes** — and sliding between them is the single most common source of confusion in this family:

| Sense | What it means | Careful |
|---|---|---|
| **Technical** | "consensus winner" = the **Condorcet winner** — beats every other candidate head-to-head | A *definition*, not a description. It's a stipulated label for a pairwise-majority fact. |
| **Brand** | **Consensus Voting** = Equal Vote's alias for Ranked Robin; **Consensus Choice** = *Better Choices for Democracy*'s sibling brand (same family, different cycle rule) | Two different organizations, two different tiebreaks. Not interchangeable at the byte level. |
| **Ordinary English** | broad, warm, genuinely-shared agreement — everyone is *content* | **Condorcet methods cannot see this.** A ranked ballot carries order, not intensity, so the count can't tell a warm second choice from grudging tolerance — see [honest limits](RCV_RR_honest_limits.md). |

**The claim to watch for**, common on advocacy sites and forums:

> "Condorcet methods are designed to make the best use of limited ranking information to find the consensus."

The **first half is a fair steelman** — and worth conceding cleanly. It admits ranking is *limited* information and claims Condorcet extracts the most available from it, which is true: a round-robin reads every rank against every opponent, and nothing exhausts. That's a real advantage over IRV, which reads one rank per ballot per round.

The **second half slides from sense 1 to sense 3.** "Finds the consensus" is true by *definition* (whoever wins the pairwise comparisons is *called* the consensus winner) and unproven in ordinary English (that person may be everyone's tepid second choice). The method doesn't discover consensus; it elects the pairwise-majority winner and the brand supplies the warmer word.

**Where the two reform camps part ways** is exactly here — and both answers are respectable:

- **Ranked Robin / Condorcet:** *extract maximum value from limited information.* Keep the familiar ranked ballot; count all of it.
- **STAR:** *don't limit the information.* Let the ballot carry degree (0–5), not just order, so intensity is visible at all.

That's a genuine design disagreement about ballots, not a dispute about counting — see [scores vs. ranks](../scores_and_ranks/scores_vs_ranks.md) and [preference vs. support](../scores_and_ranks/preference_vs_support.md).

## Looks like Condorcet — but isn't (STAR, 3-2-1)

Two **rated** methods *end* with a head-to-head step, which can fool you into filing them under Condorcet. They aren't. Both first narrow the field, then run a pairwise comparison only among the **survivors** — so the true Condorcet winner can be eliminated *before* the final:

- **STAR** — add 0–5 scores, take the top two by total, then a pairwise automatic runoff. The runoff is pairwise, but the *finalists* are chosen by score sum, not by beating everyone — so STAR is **not** Condorcet-compliant. → [STAR](../STAR_Voting/STAR_start_here.md) · [three notions of winner](../STAR_Voting/properties_and_limits/STAR_three_winner_notions.md).
- **3-2-1** — Good/OK/Bad, then most-Good → fewest-Bad → pairwise. Same shape: a pairwise *final*, but the two finalists come from the rating steps, so a Condorcet winner outside them never gets there. **Not** Condorcet. → [3-2-1 voting](../topics/three_two_one_voting.md).

**The tell:** a Condorcet method compares *every* pair across the *whole* field; these compare *one* pair among *pre-selected* finalists. A pairwise step ≠ a Condorcet method.

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

- [Condorcet methods — a reading list](../topics/condorcet/condorcet_reading_list.md) — the sources behind this page: books, papers, and the free surveys, each with its lean marked
- [Ranked Robin](ranked_robin.md) — the method, taught (with the "Names & family" section this page expands)
- [Terminology — the ranked-method family tree](../tips/TIPS_terminology.md#the-ranked-method-family-tree) — the diagram of where every method sits
- [Ranked Robin vs. Condorcet](ranked_robin_vs_condorcet.md) — why a *cycle* leaves "the Condorcet winner" blank while Ranked Robin still elects one
- [The math behind Condorcet](the_math_behind_condorcet.md) — tournaments, Smith/Schwartz, the impossibility theorems
- [Glossary](../GLOSSARY.md)
