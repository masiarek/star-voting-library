# What should we call this method? — the naming options, weighed

*One method, roughly seven centuries old, and at least six names in circulation. This page is not the [naming decoder](condorcet_naming_decoder.md) — that one maps which word **means** what. This one argues about which word we should **use**, and what each choice costs. It is a live dispute, including among the people who coined the names, so it is laid out as pros and cons rather than a ruling.*

**Level: reference** (a 201/301 aid). The teaching page for the method is [Ranked Robin](ranked_robin.md).

---

## The thing being named

Strip the labels and the method is short to state: **compare every pair of candidates head-to-head; whoever wins the most matchups wins.** Ties are broken by summing win margins.

That core is old. It was described by Ramon Llull in **1299**, rediscovered by the Marquis de Condorcet in the 1780s, and formalised as an algorithm by A. H. Copeland in **1951**. The margins tiebreak makes it what the literature calls **Copeland//Borda**. The name *"Ranked Robin"* was coined by Sara Wolk of the Equal Vote Coalition in **2021**.

So the naming question is not "what do we call this new thing?" It is "which of several existing names for a 700-year-old thing should a teaching library lead with?"

## Why this is genuinely unsettled

Three facts, all from the primary sources, that any answer has to survive:

**1. The person who coined "Ranked Robin" says it means Condorcet in general.** On electowiki's talk page in 2025, Wolk wrote that she "always intended the name Ranked Robin to be a rebrand of Condorcet," and gave as her first takeaway: *"Ranked Robin is a synonym for Condorcet on a ranked ballot."* The specific Copeland-plus-margins procedure is Equal Vote's *default recommendation*, which she notes is under review — not the definition of the name. That means using "Ranked Robin" to denote one exact algorithm is now contradicted by its originator.

**2. Equal Vote's own page has already shifted.** Their [current page](https://www.equal.vote/ranked_robin) opens by calling it "a modern name for one of the oldest voting methods out there. First described in the literature in 1299." Their [previous version](https://www.equal.vote/ranked_robin_old) said no such thing — it never mentioned Copeland or 1299 at all.

**3. The name drew an objection on day one.** Markus Schulze — of the Schulze method — opened the electowiki talk page in November 2021 arguing the title is misleading, because "round robin" has long been used for Condorcet methods generally and no single proposal should claim it. Another contributor made the sharper version: "ranked" and "robin" are both so general that the name behaves like "ranked choice voting" does for IRV — a category word annexed by one method.

That last comparison should sting for us in particular, because **this repo's entire terminology policy exists to resist exactly that move** when FairVote does it with "RCV."

## The candidates

### "Ranked Robin"

**For.** It is what the audience arrives with — Equal Vote's materials, BetterVoting's interface, and the STAR-adjacent community all use it. It is friendly, memorable, and the sports metaphor teaches the mechanic in three words. It is also what our own engine emits and what our BetterVoting elections are titled.

**Against.** It is branding, not a method name, and naming the brand rather than the method is the thing we criticise elsewhere. It is ambiguous as of 2025 by its coiner's own account. And it is annexation of a general term, which is Schulze's objection and a fair one.

### "Copeland" (or precisely, Copeland//Borda)

**For.** It is the actual algorithm, it is what the academic literature calls it, and it is unambiguous — vital in passages about clone independence, tiebreaks and cycle resolution, where "Ranked Robin" now genuinely fails to pick out one procedure. Best for the research-companion audience.

**Against.** It means nothing to a newcomer and teaches nothing about the mechanic. It is also named after a person, which is part of what the rebranding was trying to get away from — a contributor on that talk page made the case for descriptive names over "the last name of a white guy," and whatever one makes of the framing, "Copeland" does not tell a voter what happens to their ballot.

### "Condorcet method"

**For.** It is the family term, it is what the originator now says the brand means, and it is the most defensible sentence to write in front of a hostile expert. It also correctly signals that the cycle rule is a choice, not part of the definition.

**Against.** It is the least self-explanatory word of the lot to a general audience, it is a *family* rather than one method (so it under-specifies exactly when we need to be exact), and it too is a person's name.

### "Consensus Choice" — and the phantom "Consensus Voting"

**First, a correction this library owes.** Until 2026-07-29 these pages listed **"Consensus Voting"** as an Equal Vote alias for Ranked Robin, and the naming decoder cited equal.vote for it. That was wrong. The term appears **nowhere** on [equal.vote](https://www.equal.vote/ranked_robin), nowhere on [electowiki's Ranked Robin page](https://electowiki.org/wiki/Ranked_Robin), and nowhere on Better Choices for Democracy's site — every "consensus" on those pages is the ordinary English word. The likely mechanism is now clear: Better Choices for Democracy title their page *"[Consensus Choice **Voting**](https://www.betterchoices.vote/consensus-choice)"*, and dropping the middle word yields the phantom. It had propagated into a dozen of our pages, including the canonical terminology tips. Treat "Consensus Voting" as a name nobody actually uses.

**Consensus Choice** is real, and it belongs to someone else: it is [Better Choices for Democracy](https://www.betterchoices.vote/faqs)'s brand, usually paired with a "Top 4" primary. Worth noting in a page about naming honesty — their [method page](https://www.betterchoices.vote/consensus-choice) never uses the words *Condorcet* or *Copeland* either. Both camps sell the branding and bury the algorithm; this is not a failing unique to one of them. A third party says it out loud where neither site does: electowiki records that BC4D promotes "Consensus Choice Voting" as ["the organization's preferred term for Condorcet methods"](https://electowiki.org/wiki/Better_Choices_for_Democracy), with affiliated people favouring **variants of Copeland's method**. So the pattern here is not Equal Vote's alone — it is *two* organisations, each branding the same 700-year-old family, and each omitting its name.

**For.** "Consensus" describes the *goal* in a word a voter understands, and it is the friendliest of the options to a non-technical audience.

**Against.** It is not ours to adopt, and it is not the same algorithm — Consensus Choice resolves cycles by "Most Wins, Smallest Loss" where Ranked Robin sums margins, so borrowing the word merges two proposals that genuinely differ. It also quietly asserts the method's central claim — that its winner *is* the consensus — inside its own name, which is exactly the kind of loaded label we flag when other camps do it.

### "RCV-RR"

**For.** It is this repo's existing house compound and it parallels `RCV-IRV` precisely: the ranked ballot, plus which tabulation. Unambiguous and consistent with the rule we already follow.

**Against.** Nobody outside this repo says it, and like `RCV-IRV` it can read as jargon to a public audience.

### "Llull voting"

Occasionally floated, honest about the history, and used by essentially nobody. Worth a footnote, not a label.

## What is not negotiable

Some of this is decided for us, and it is worth being clear about which parts:

- **The engine** takes `voting_method: RankedRobin` (aliases `RCV_RR`, `Copeland`, `Consensus`) and prints "Ranked Robin (RCV-RR / Copeland)".
- **BetterVoting**'s method string is `RankedRobin`, and **BV election titles are permanent** — the ones already minted cannot be renamed.
- A permanent BV election description links to `05_Ranked_Robin/most_wins_vs_condorcet/`, so even the folder name carries a forever-redirect obligation if it ever moves.

So "rename everything" is not on the menu. Any choice here is about the *prose default*, not about the machinery.

## The precedent we already set

This repo has faced this exact shape of problem once before, and answered it. From the house terminology policy:

> **RCV** names a *ballot* (ranked); **IRV** names one *tabulation* of it. Default to `RCV-IRV`; use bare `IRV` in technical and critical passages, because center squeeze and non-monotonicity are IRV-specific; reserve bare `RCV` for the ranked-ballot family. In public-facing copy "RCV" is fine — clarify once on first mention, then use the familiar word. <!-- terminology-ok: quotes the house policy, which is itself about when bare RCV is correct -->

Mapped onto this method, that template reads: **Condorcet / round-robin** for the family · **Copeland** for the specific tabulation, in technical and critical passages · **Ranked Robin** as the public-facing word, clarified once · **RCV-RR** as the compound when disambiguation matters.

The appeal of that answer is that it requires no new principle — it is the rule we already apply, applied consistently. The objection to it is that it keeps a brand name in the lead position, and the brand is the one thing on the layer table that is actually new.

## Where this leaves us

The honest summary is that **the naming question is unresolved in the field, and our own preference is a judgement call rather than a finding.** The pattern above is what consistency with the rest of the repo would suggest; it is written here as an argument, not a ruling, and this page should be updated if Equal Vote's own review lands somewhere different.

What is *not* a judgement call is the underlying fact, and it belongs in front of the reader whichever label wins: **the method is Copeland's, the idea is Llull's, and the name is the only part invented in 2021.**

## Sources

- [Ranked Robin (electowiki)](https://electowiki.org/wiki/Ranked_Robin) and [its talk page](https://electowiki.org/wiki/Talk:Ranked_Robin) — the canonical definition of the name, and the naming argument itself, including Schulze's objection and Wolk's 2025 clarification. *Community wiki, Equal-Vote-adjacent: good for definitions, weak for verdicts.*
- [Equal Vote — Ranked Robin](https://www.equal.vote/ranked_robin) and the [superseded version](https://www.equal.vote/ranked_robin_old). *Advocacy; cite for their position, not for verdicts.*
- [Copeland's method (Wikipedia)](https://en.wikipedia.org/wiki/Copeland%27s_method) · [Round-robin voting (Wikipedia)](https://en.wikipedia.org/wiki/Round-robin_voting) — the neutral family and algorithm articles.
- [Better Choices for Democracy — Consensus Choice](https://www.betterchoices.vote/faqs) and their [method page](https://www.betterchoices.vote/consensus-choice), titled *"Consensus Choice Voting"*. *Advocacy; the sibling brand with a different cycle rule, and the likely source of the phantom "Consensus Voting".*
- [Better Choices for Democracy (electowiki)](https://electowiki.org/wiki/Better_Choices_for_Democracy) — the third-party description that names the underlying method (Condorcet, Copeland variants) where BC4D's own pages do not, and notes board member Wes Holliday, co-author of [Split Cycle](../../method_comparisons/split_cycle/). *Community wiki; better here than the org's own copy precisely because it is not theirs.*

*Related: [the naming decoder](condorcet_naming_decoder.md) (which word means what) · [Ranked Robin](ranked_robin.md) (the method) · [Ranked Robin vs. Consensus Choice](ranked_robin_vs_consensus_choice.md) (the sibling brand, compared).*
