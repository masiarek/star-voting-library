# Condorcet methods — a reading list, with the nomenclature fixed first

*The Condorcet literature is genuinely hard to enter, and the reason is almost never the math — it's the names. "Condorcet method," "pairwise method," "round-robin voting," "tournament solution," "Copeland," "Ranked Robin," "Consensus Voting" all show up in the first ten minutes of reading, at four different levels of generality, from four camps with four agendas. This page is the way in: one taxonomy that makes the names stop sliding, then the sources worth your time, each with its lean marked.*

**Level: reference** (a 201/301 aid). Start with the [naming decoder](../../RCV_Ranked_Robin/condorcet_naming_decoder.md) if you just need the brands untangled; come here for the literature behind it.

---

## First, the one idea that fixes the nomenclature

Before any book: **"Condorcet method" is not a method.** It's a *property* — elect the candidate who beats every other head-to-head, whenever such a candidate exists — and dozens of different algorithms have it. The literature's own organizing scheme for those algorithms comes from **Peter Fishburn (1977)**, and it sorts them by *how much of the pairwise data the rule actually needs*:

| Fishburn class | What the rule reads | Members you'll meet | Where in this repo |
|---|---|---|---|
| **C1** | only **who beat whom** (the tournament — a matrix of wins/losses, margins discarded) | **Copeland**, Smith set, Schwartz set, Uncovered set, Top Cycle | [Ranked Robin](../../RCV_Ranked_Robin/ranked_robin.md) (a Copeland variant) · [Smith set](../smith_set.md) |
| **C2** | the **margins** too (how *badly* each pair went) | **Minimax**, **Ranked Pairs**, **Schulze (beatpath)**, **Kemeny**, Split Cycle | [cycle resolution](../../RCV_Ranked_Robin/cycle_resolution.md) |
| **C3** | more than the pairwise matrix — the rule must go back to the ballots and iterate | **Dodgson**, **Young** | [the ranked-ballot zoo](../ranked_ballot_methods_zoo.md) |

Once that ladder is in your head, most of the confusion resolves itself:

- **"Condorcet" / "pairwise" / "round-robin voting"** all name the **family** (the property), at different levels of formality and friendliness. "Round-robin voting" is a *recent* Wikipedia reframing of what the field has always called Condorcet methods — which is exactly why those two articles read as redundant.
- **"Tournament solution"** is the academic name for the **C1 tier specifically** — the theory of what to do with nothing but a win/loss graph. If a paper says "tournament solution," it is not talking about the whole family.
- **Copeland** is *one* C1 rule (most head-to-head wins, ½ per tie). **Ranked Robin** is a **brand** for Copeland plus a defined cycle tiebreak. **Consensus Voting** / **Consensus Choice** are further brands. None of these is a new tier of the taxonomy — they're leaves.
- **The famous disagreements inside the family are all about cycles.** When a Condorcet winner exists, every rule above elects the same person. C1 vs. C2 vs. C3 only matters when the pairwise results loop — which is why so much of the literature is about a case that is empirically rare. Keep that proportion in mind while reading; see [cycle resolution](../../RCV_Ranked_Robin/cycle_resolution.md) and the repo's [divergence ledger](../../../method_comparisons/divergence_review/INDEX.md).

> **The reading trick:** whenever a source names a method, ask *which tier?* A claim proved for C1 rules ("depends only on the tournament") does not transfer to Minimax, and a Minimax result does not transfer to Copeland. Half of all cross-talk in online voting arguments is a tier mismatch.

---

## Free, online, start here

| Source | Why | The lean |
|---|---|---|
| **[Voting Methods](https://plato.stanford.edu/entries/voting-methods/)** — Eric Pacuit, *Stanford Encyclopedia of Philosophy* | The best free survey in existence, and scrupulously consistent about terms. Read this **before** any wiki: it defines the family, the criteria, and the individual rules in one vocabulary, and it's maintained. | **Neutral / academic.** Sells no method. |
| **[pref_voting](https://pref-voting.readthedocs.io/)** — Wesley Holliday & Eric Pacuit | The nomenclature as *runnable code*. Every Condorcet rule under its standard name, definition in the docstring, and the modules are literally organized by Fishburn's tiers (`c1_methods`, `margin_based_methods`, `iterative_methods`). The library is already declared in this repo — see [cross-checking with pref_voting](../../tabulation_engines/cross_checking_with_pref_voting.md). | **Neutral / academic.** |
| **[Handbook of Computational Social Choice](https://www.cambridge.org/core/books/handbook-of-computational-social-choice/)** (free PDF from the authors), ch. 3 "Tournament Solutions" — Brandt, Brill & Harrenstein | The modern restatement of the C1 tier, rigorous and self-contained. Where "tournament solution" is properly defined. | **Neutral / academic.** Dense. |
| **[Wikipedia: Condorcet method](https://en.wikipedia.org/wiki/Condorcet_method)** | Fine for the neutral family term and notability. But note the **[round-robin voting](https://en.wikipedia.org/wiki/Round-robin_voting)** umbrella rename is contested and has seen editorial churn — part of why the family looks unsettled from outside. | **NPOV pressure, but unstable on this topic.** |
| **[electowiki](https://electowiki.org/wiki/Condorcet_method)** | The only place many *branded* variants (Ranked Robin, Consensus Voting) are defined at all. Cite for definitions. | **Reform-advocacy-adjacent.** Weak for verdicts — never cite it for a criterion claim. |

---

## The papers that define the words

- **Peter C. Fishburn, "Condorcet Social Choice Functions," *SIAM Journal on Applied Mathematics* 33(3), 1977, pp. 469–489.** The source of the C1/C2/C3 classification above, and of "Condorcet social choice function" as a precise term. If you read one primary source for *vocabulary*, read this one. **The lean:** neutral; pure taxonomy.
- **H. Peyton Young, "Condorcet's Theory of Voting," *American Political Science Review* 82(4), 1988, pp. 1231–1244.** The historical correction, argued properly: Condorcet the man was after a *maximum-likelihood* estimate of the "correct" ranking, which is closer to Kemeny than to what now carries his name. Genuinely clarifying about why the modern label is a bit of a misnomer. **The lean:** academic; sympathetic to the maximum-likelihood reading.
- **T. Nicolaus Tideman, "Independence of Clones as a Criterion for Voting Rules," *Social Choice and Welfare* 4(3), 1987, pp. 185–206.** Coins the term, defines the criterion, introduces Ranked Pairs. Pairs with this repo's [clone independence in Ranked Robin](../../RCV_Ranked_Robin/rr_clone_independence.md). **The lean:** pro-Condorcet (Tideman's own rule).
- **Markus Schulze, "A New Monotonic, Clone-Independent, Reversal Symmetric, and Condorcet-Consistent Single-Winner Election Method," *Social Choice and Welfare* 36(2), 2011, pp. 267–303.** Long, but the definitions section is a de facto glossary for the C2 tier. **The lean:** the author is the method's inventor and advocate.
- **Wesley H. Holliday & Eric Pacuit, ["Split Cycle: A New Condorcet-Consistent Voting Method Independent of Clones and Immune to Spoilers"](https://arxiv.org/abs/2004.02350)** (arXiv:2004.02350; published in *Public Choice* 197, 2023). A modern paper whose background sections carefully re-lay the entire Condorcet landscape before adding to it — often the clearest available statement of what the older rules actually do. **The lean:** academic, proposing their own rule; unusually explicit about trade-offs.
- **James Green-Armytage, T. Nicolaus Tideman & Rafael Cosman, ["Statistical Evaluation of Voting Rules,"](https://link.springer.com/article/10.1007/s00355-015-0909-0) *Social Choice and Welfare* 46, 2016, pp. 183–212.** 54 rules tested for manipulability and utilitarian efficiency across five data-generating processes. The empirical counterweight to axiom-only argument — and honest enough to report that **Hare (IRV) and Condorcet-Hare** come out most strategy-resistant, a result that does not flatter every camp. **The lean:** Condorcet-sympathetic authors reporting an inconvenient finding — which is why it's worth citing.

---

## Books

All four below are on the repo's [annotated shelf](../../books/README.md) or belong beside it; leans are stated in the house style.

- **T. Nicolaus Tideman, *Collective Decisions and Voting: The Potential for Public Choice* (2006)** — the major Condorcet-sympathetic treatise, by the inventor of Ranked Pairs. Works through *what we should want* from a collective decision before asking which rule delivers it, and defines its criteria as it goes. The single best book if you want the family argued at full strength. **The lean:** pro-Condorcet, criterion-driven; a valuable opposing-camp read for a STAR-centered library. → [shelf entry](../../books/social_choice_theory.md).
- **Hannu Nurmi, *Comparing Voting Systems* (1987)** and ***Voting Paradoxes and How to Deal with Them* (1999)** — Nurmi's whole method *is* definitional hygiene: name the rule, name the criterion, show which fails. The right books for a reader whose complaint is "the words keep sliding." **The lean:** survey-neutral; Nurmi catalogs rather than advocates. → [shelf entry](../../books/social_choice_theory.md).
- **Iain McLean & Arnold B. Urken (eds.), *Classics of Social Choice* (1995)** — translations of Condorcet, Borda, and Ramon Llull (whose ~1299 round-robin predates Condorcet by five centuries). Reading where the names came from is clarifying in a way no summary is. **The lean:** historical, neutral.
- **Dan S. Felsenthal & Moshé Machover (eds.), *Electoral Systems: Paradoxes, Assumptions, and Procedures* (2012)** — Felsenthal's opening chapter is a tight taxonomy of single-winner rules and the pathologies each admits, with the terminology pinned down. Excellent as a lookup table. **The lean:** academic; the editors are critical of several popular rules and say so.
- **Donald G. Saari, *Decisions and Elections: Explaining the Unexpected* (2001)** — read for *why* methods disagree (his geometric account of aggregation is superb), but know that Saari argues **against** the Condorcet criterion and **for** Borda. That makes him a useful adversary here rather than a guide. **The lean:** pro-Borda, openly. → [shelf entry](../../books/social_choice_theory.md).

---

## Advocacy — read it, knowing where it stands

The Condorcet camp argues well, and the strongest version deserves a serious reading. Ours are marked, too.

- **Richard B. Darlington, ["Are Condorcet and Minimax Voting Systems the Best?"](https://arxiv.org/abs/1807.01366)** (arXiv:1807.01366) — the most sustained modern case for a *specific* Condorcet rule (Minimax), with five simulation tests. **The lean:** strongly pro-Minimax; the simulations are the author's own design, so read the *setup* as carefully as the results.
- **Marcus Ogren, ["How to Learn About Voting Methods"](https://voting-in-the-abstract.medium.com/how-to-learn-about-voting-methods-4e6c0e4d38d9)** — a field-wide reading path that transparently leans Condorcet. The repo's [runnable counterpart](../how_to_learn_about_voting_methods.md) follows its structure and states its own STAR lean in return.
- **[equal.vote](https://www.equal.vote/ranked_robin) / [electowiki: Ranked Robin](https://electowiki.org/wiki/Ranked_Robin)** — the promoters of the *branded* Copeland variant this repo teaches. Source for the brand, not a neutral referee. (Disclosure runs both ways: this library is STAR-centered.)
- **The arguments *against* the Condorcet criterion**, which are real and worth meeting head-on: [Edelman's "Myth of the Condorcet Winner," tabulated](edelman_condorcet_myth.md) and [the "ordered majority rule" paper, taken apart](ordered_majority_rule_irv.md). And in the other direction, [FairVote's Condorcet article, claim-checked](fairvote_condorcet_claim_check.md).

---

## Where each idea lands in this repo

| You just read about… | Run it here |
|---|---|
| Condorcet winners, pairwise matrices | [pairwise counting](../pairwise_counting.md) · [the math behind Condorcet](../../RCV_Ranked_Robin/the_math_behind_condorcet.md) |
| Copeland / tournament solutions (C1) | [Ranked Robin](../../RCV_Ranked_Robin/ranked_robin.md) · [Smith set](../smith_set.md) |
| Cycles, and what the tiers do about them | [cycle resolution](../../RCV_Ranked_Robin/cycle_resolution.md) · [the Condorcet-winner paradox](../../voting_paradoxes/condorcet_winner_paradox.md) |
| Clone independence | [clone independence in Ranked Robin](../../RCV_Ranked_Robin/rr_clone_independence.md) |
| Why the brands differ | [the naming decoder](../../RCV_Ranked_Robin/condorcet_naming_decoder.md) · [Ranked Robin vs. Consensus Choice](../../RCV_Ranked_Robin/ranked_robin_vs_consensus_choice.md) |
| Whether a *rated* method should chase the Condorcet winner at all | [three notions of winner](../../STAR_Voting/properties_and_limits/STAR_three_winner_notions.md) · [scores vs. ranks](../../scores_and_ranks/scores_vs_ranks.md) |
| Cross-checking a real count three ways | [cross-checking with pref_voting](../../tabulation_engines/cross_checking_with_pref_voting.md) |

---

## Related

- [Topic: Condorcet efficiency](README.md) — the hub this page sits under
- [Round-robin, Copeland, Condorcet, Ranked Robin — a naming decoder](../../RCV_Ranked_Robin/condorcet_naming_decoder.md) — the brands, mapped
- [Books on Voting Methods](../../books/README.md) — the general shelf, with covers and leans
- [How to Learn About Voting Methods](../how_to_learn_about_voting_methods.md) — the runnable reading path
- [Glossary](../../GLOSSARY.md)
