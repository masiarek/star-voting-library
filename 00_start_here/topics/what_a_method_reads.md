# What a method reads — the informational basis of a voting rule

*Every tabulation is a two-step act: **compress** the ballots into some summary, then **decide** from the summary. Change the second step and you have a different method; change the first and you have changed what the method is even capable of noticing. This page is about the first step — which statistic a rule actually reads — the question Peter Fishburn turned into a classification in 1977. It answers a debate question worth having ("how much of my ballot does your method look at?") and defuses two claims that sound right and aren't.*

→ Related: [the C1/C2/C3 tiers in the Condorcet reading list](condorcet/condorcet_reading_list.md) · [summability](summability/) — how *big* the summary is · [the cycle–cocycle decomposition](cycle_cocycle_decomposition.md) — how the pairwise summary splits · [Borda](../other_ranked_methods/borda.md) · [pairwise counting](pairwise_counting.md).

**Runnable:** [Same matrix, different plurality](../../method_comparisons/same_matrix_different_plurality/) — three electorates, one pairwise table, three plurality winners.

---

## Three different questions, routinely confused

| Question | Asks | Answered by |
|---|---|---|
| **Which** statistic does the rule read? | can it even see margins? first choices? | Fishburn's tiers, below |
| **How big** is that statistic? | what must a precinct publish? | [summability](summability/) |
| **How hard** is it to compute from? | can you do it by hand? | complexity |

These are independent, and every pairing of them comes apart somewhere. Keeping them separate is most of the value on this page.

## Fishburn's tiers

Peter Fishburn (1977) sorted rules by how much of the **pairwise** data they need:

| Tier | Reads | Members you'll meet |
|:---:|---|---|
| **C1** | the **tournament** — who beat whom, and which pairs tied. Direction only, no sizes | Copeland (the core of [Ranked Robin](../RCV_Ranked_Robin/)), Smith set, Top Cycle, uncovered set |
| **C2** | the **weighted tournament** — the same graph *with the margins on it* | Minimax/Simpson, Ranked Pairs, Schulze, Kemeny, Split Cycle — and Borda |
| **C3** | more than the pairwise matrix contains | Dodgson, Young, **plurality**, RCV-IRV |

The one-line test for C1 vs C2: **hand the rule two elections whose head-to-head *directions* match but whose *margins* differ.** A C1 rule must return the same answer; a C2 rule may not. Copeland genuinely cannot tell a 50-vote blowout from a 1-vote squeaker. Minimax and Kemeny can, and do.

**Scope note, stated once so nobody has to catch us on it.** Fishburn's 1977 paper classified *Condorcet* social choice functions. Extending the labels to Borda, plurality and IRV is later convention — universal in the literature, but convention. It is not a direct citation of Fishburn.

## The claim that gets it wrong: "plurality needs more information"

Because plurality is C3 and Borda is C2, it is tempting to say plurality needs *more* information than Borda. **That is false, and it inverts badly for a lay reader** — a plurality *ballot* carries far less than a Borda ballot, and readers will hear the sentence as the opposite of the truth.

The two statistics are **incomparable, not nested.** First-place counts don't determine the pairwise table; the pairwise table doesn't determine first-place counts. C3 isn't a higher rung — it's the *residual* class, everything the pairwise matrix fails to capture. The precise claim is narrow:

> **Plurality's winner is not a function of the pairwise matrix.**

And it is demonstrable. [Three 12-ballot electorates](../../method_comparisons/same_matrix_different_plurality/) produce the identical pairwise table — Ben beats Ada 7–5, Ada ties Cal 6–6, Ben beats Cal 7–5, hence the same Condorcet winner, the same Borda scores, the same Ranked Robin / Minimax / Ranked Pairs / Kemeny result — and **three different plurality winners, one per candidate.**

The mechanism is worth carrying, because it explains the whole tier: **a ballot and its exact mirror cancel pairwise but not in the first-choice tally.** `Ada>Ben>Cal` plus `Cal>Ben>Ada` puts one vote on each side of every head-to-head, leaving every margin untouched, while handing out two different first preferences. Swap mirror pairs in and out and the plurality winner roams while the matrix sits still.

## Borda: the C2 rule that isn't a Condorcet method

Borda belongs in C2 because a Borda score *is* a row of the pairwise table added up. With `M(x,y)` the margin, `n` ballots and `m` candidates:

> **Borda(x) = ½ · Σ M(x,y) + n(m−1)/2**

The second term is identical for everyone, so it can't move anybody: **the margins alone fix the entire Borda ranking.** (They fix the raw *scores* only if you also supply `n` and `m` — a margin matrix doesn't remember how many people voted. If you want exact scores from a matrix alone, sum the pairwise *support* counts instead: `Borda(x) = Σ N(x,y)`. That is all a Borda count ever was.)

Three conditions on that identity, because it is not unconditional:

1. **Equal spacing** — standard Borda points (`m−1, m−2, …, 0`).
2. **Complete ballots**, or ties handled by splitting points evenly.
3. **Truncation breaks it.** Under the common "unranked candidates get 0 points" rule, Borda is *not* margin-determined — so real truncated-ballot Borda is not C2. Worth knowing, since real ranked ballots are truncated.

Why the identity matters beyond bookkeeping: it is the reason [Borda and the Condorcet family diverge in a structured way](cycle_cocycle_decomposition.md) rather than randomly. Borda reads the pairwise table through a sum, which is blind to circulation; Condorcet methods read the same table through its signs, which circulation can flip.

## STAR, Score and Approval have no Fishburn class

Not "an unusual one" — **none**, and the reason is sharper than the obvious one.

The obvious reason is that Fishburn classifies rules whose input is a *ranked* profile. A critic answers that easily: map the score ballots to the rankings they induce, then classify. The decisive reason is that **this cannot be done, because STAR is not a function of the ranked profile at all.**

Two score profiles can induce *exactly the same* ranked profile — hence exactly the same pairwise matrix — and elect different STAR winners. Six voters ranking Ada>Ben>Cara, five Ben>Cara>Ada, four Cara>Ada>Ben, scored `5,4,0 / 0,5,1 / 4,0,5`, elect **Ada**; the same rankings scored `5,4,0 / 0,5,4 / 1,0,5` elect **Ben**. Plurality, RCV-IRV and Ranked Robin return Ada on both. Only STAR moves.

A function must return the same answer on the same input. There is simply nothing here for C1/C2/C3 to classify. **In any tier column, STAR / Score / Approval get `n/a — not a ranked-ballot rule`** — never a hedged class like "C3" or "beyond C2," because readers strip hedges and would come away thinking STAR counts like Dodgson.

This isn't STAR dodging a question. It's the same type distinction as the [SWF/SCF](social_welfare_function.md) one: a classification applies to a domain, and STAR is not in it. What STAR's tabulation actually needs is a **score-count matrix plus a pairwise matrix** — richer than either alone, and still perfectly summable.

*(Footnote for completeness: on the Brams–Fishburn dichotomous-preference domain, Approval is a genuine SCF on preference profiles and is determined by the majority tournament — C1-like. That's a theoretical domain, not real approval ballots, but a critic will find it, so here it is.)*

## Why C3 is not a demerit

C3 is a bag, not a basement. It holds **plurality** — the cheapest, most summable method in this library, one number per candidate — *and* **[RCV-IRV](../RCV_IRV/)**, the one method here whose count [doesn't summarize into precinct subtotals](../STAR_Voting/properties_and_limits/STAR_summability.md) at all. Those two have nothing in common except that the pairwise matrix doesn't determine them.

Which is exactly why the tiers must not be read as a ladder:

- **Not a summability ladder.** Plurality is C3 and first-order summable; Kemeny is C2 and NP-hard.
- **Not a difficulty ladder.** See the previous line.
- **Not a quality ladder.** C1 vs C2 is invisible to a precinct: Copeland and Schulze publish the *identical* C×C table. The tier says which part of it they *look* at.

## The debate use

The version that travels is not the taxonomy — it's the question:

> **How much of my ballot does your method actually look at?**

It is positive rather than an attack: it says what pairwise and score counting *see*, not what any method gets wrong. It makes vote-splitting precise instead of rhetorical — in two of the three electorates above, the plurality winner isn't the candidate a majority prefers head-to-head, and you can watch the ballots that do it. And it cuts symmetrically, which is what makes it usable: pressed honestly, the same framing forces the admission that **STAR sits outside the ladder entirely** — which is the pro-STAR point restated, not dodged.

## Sources

- Peter C. Fishburn, "Condorcet Social Choice Functions," *SIAM Journal on Applied Mathematics* 33(3), 1977, pp. 469–489 — the classification, for Condorcet SCFs. **Lean:** neutral; taxonomy.
- William S. Zwicker, "Introduction to the Theory of Voting," in *Handbook of Computational Social Choice* (2016), §2.5 — the modern restatement, including the observation that one *should* balk at "plurality needs more information than Borda." **Lean:** neutral.
- The tier assignments used across this repo, and the `[C1]`/`[C2]` tags printed by [`cycle_resolution_report.py`](../../STARVote_LH_tabulation_engine/tools_adam/pref_voting_tabulation_engine/), follow `pref_voting`'s own module organization.

## Related

- [Same matrix, different plurality](../../method_comparisons/same_matrix_different_plurality/) — the runnable exhibit
- [Copeland vs Borda margins](../../method_comparisons/copeland_vs_borda_margins/) — C1 vs C2, worked · [the cycle–cocycle decomposition](cycle_cocycle_decomposition.md) — the theorem underneath
- [Summability](summability/) — the *how big* question · [pairwise counting](pairwise_counting.md) — what the matrix is
- [The Condorcet reading list](condorcet/condorcet_reading_list.md) — the tiers applied to the Condorcet family · [the ranked-ballot zoo](ranked_ballot_methods_zoo.md)
