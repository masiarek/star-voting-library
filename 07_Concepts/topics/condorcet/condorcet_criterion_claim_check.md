# Claim check — Wikipedia's "Condorcet winner criterion"

*Wikipedia's [Condorcet winner criterion](https://en.wikipedia.org/wiki/Condorcet_winner_criterion) article is the page most people land on first, and its argument section is unusually strong — the claims are real properties, not advocacy inventions. This page checks four of them anyway. Three hold and one is **too soft on Condorcet**, which is the opposite of the failure mode you expect. Two are stated with definitions that don't survive contact with a pairwise tie.*

**Level: 301 · for debaters** → Companions: [the Condorcet hub](README.md) · [FairVote's article, claim-checked](fairvote_condorcet_claim_check.md) (the same exercise pointed the other way) · [the naming decoder](../../../05_Ranked_Robin/01_Learn/condorcet_naming_decoder.md) (where this article's vocabulary comes from, and which of it is safe) · [criteria at a glance](../criteria_at_a_glance.md). Curriculum: [301](../../CURRICULUM.md).

> **Source lean, disclosed** (house rule). Wikipedia is this library's [neutral tier](../how_to_learn_about_voting_methods.md) — right for notability and for criteria claims. **But this specific article cluster is an exception worth naming:** the Condorcet pages have seen sustained editorial reframing toward friendlier, less mathematical vocabulary ("round-robin voting" for the family, "beats-all winner" and "majority-preferred candidate" for the winner), documented in [the naming decoder](../../../05_Ranked_Robin/01_Learn/condorcet_naming_decoder.md#why-the-two-wikipedia-articles-overlap-the-trap-you-hit). Nothing below is wrong *because* of that. But when an article's terminology is contested, check the terminology as carefully as the claims — which is why half this page is about definitions.

---

## Claim 1 — "Stability (no weak spoilers)"

> "Condorcet methods are highly resistant to spoiler effects. Intuitively, this is because the only way to dislodge a Condorcet winner is by beating them, implying spoilers can exist only if there is no majority-rule winner."

**Verdict: true, and it is a real advantage over STAR.** Concede it cleanly.

The mechanism is exactly as described. If X beats everyone and candidate Y enters, one of three things happens: Y loses to X, and X still beats everyone (nothing changed); Y beats X and everyone else, so **Y is the new Condorcet winner** — Y won, Y did not *spoil*; or Y beats X but loses to someone else, creating a **cycle**, and only then does the outcome depend on the tiebreak rule. So a Condorcet method can only be spoiled by an entry that destroys the Condorcet winner altogether. That is a strong and genuine property.

**Two things to add before you repeat it.**

**It is close to definitional.** "The only way to dislodge a Condorcet winner is by beating them" follows from what a [Condorcet extension](../../GLOSSARY.md#the-wider-field-computational-social-choice) *is*. The syllogism isn't the evidence; the **empirical rarity of cycles** is — and that is a separate, checkable claim (theory and observation both put a Condorcet winner in [roughly 90–99% of real elections](../spoiler_effect.md#how-social-choice-theory-frames-it), with the first cycle in a ranked US election found only in 2021). Lead with the frequency, not the logic. Compare the [criterion-built-to-fit-the-method](../criteria_at_a_glance.md) tell: a property that follows from a definition is worth less in debate than one that survives data.

**It is not IIA, and should never be read as such.** Condorcet methods *do* fail [independence of irrelevant alternatives](../arrow_theorem_and_star.md) — [Arrow](../arrow_theorem_and_star.md) guarantees that no ranked method escapes. "Stability" / "no weak spoilers" names a **conditional** guarantee: spoilerproof *whenever a Condorcet winner exists*, undefined otherwise. That is weaker than IIA and stronger than nothing, and the newer vocabulary blurs which.

**Where it cuts against STAR — say this before an opponent does.** [STAR is not Condorcet-compliant](../../../05_Ranked_Robin/01_Learn/condorcet_naming_decoder.md#looks-like-condorcet-but-isnt-star-3-2-1). Its finalists are chosen by **score total**, not by beating everyone — so a new entrant can change *which two candidates reach the runoff* and flip the result with a Condorcet winner sitting right there, un-elected. Score and Approval are IIA-clean, but only [on an absolute scale](../../scores_and_ranks/cardinal_voting_claims_checked.md); real voters **normalize** around the field, which puts the spoiler back. The honest ordering on this one axis:

| | Spoiler resistance |
|---|---|
| **Score / Approval** | None *in principle* — but only on an absolute scale; normalization reopens it |
| **Condorcet (Ranked Robin, Ranked Pairs, Schulze)** | Immune **whenever a Condorcet winner exists**; vulnerable only in a cycle |
| **STAR** | Removes the forced split; a [narrow residual](../../../01_STAR/01_Learn/properties_and_limits/residual_vote_splitting.md) survives, and finalist selection is disturbable |
| **RCV-IRV** | Reduces the classic spoiler, adds [center squeeze](../../../06_Other/RCV_IRV/concepts/RCV_IRV_center_squeeze.md) |
| **Choose-One** | Full |

This library's [spoiler page](../spoiler_effect.md) already grades it that way. Nothing to correct — but the Condorcet row is a point *for* Condorcet and *against* STAR, and pretending otherwise is the exact behaviour the [fairness rule](../how_to_learn_about_voting_methods.md) forbids.

## Claim 2 — Participation

> "One disadvantage of majority-rule methods is they can all theoretically fail the participation criterion in constructed examples. However, studies suggest this is empirically rare for modern Condorcet methods, like ranked pairs. One study surveying 306 publicly-available election datasets found no examples of participation failures for methods in the ranked pairs-minimax family."

**Verdict: true, but *too soft on Condorcet* — and the empirical claim needs its citation checked before reuse.**

This is the interesting one, because the article understates a weakness of the family it is describing.

**"Can all theoretically fail… in constructed examples" is weaker than the truth.** It is **Moulin's theorem (1988)**: *every* Condorcet extension fails the [participation criterion](../participation/) once there are **four or more candidates**. Not a quirk of ingenious construction — a proven incompatibility between Condorcet-consistency and participation. "Constructed examples" makes it sound like a curiosity someone had to work hard to find; it is a theorem saying no such method can avoid it. → [the No-Show paradox, worked](../../voting_paradoxes/no_show.md).

**The genuinely interesting nuance is missing.** Moulin's bound is *≥4 candidates*, and at **exactly three** the picture inverts: Brandt, Dong & Peters (2024) prove that refinements of maximin (leximin, Nanson) are **uniquely immune** to the no-show paradox among homogeneous Condorcet extensions. So "Condorcet methods fail participation" is true in general and false at three candidates for a specific family — a sharper and more useful fact than the one the article gives. → [Condorcet-consistent choice among three candidates](three_candidate_maximin.md).

**On the 306 datasets: plausible, unverified, don't repeat it yet.** Empirical rarity is entirely consistent with what we already believe (participation failures need a cycle-adjacent structure, and cycles are rare), so the *direction* is credible. But this library's rule is to verify a citation rather than inherit it, and a bare "one study" with no author or year is exactly the shape of claim that propagates unchecked. Find the paper, confirm the dataset and the method family, then quote it. Note also that "no failures observed in 306 datasets" is an upper bound on frequency, **not** evidence of immunity — Moulin's theorem says the failures exist.

**Fairness both directions.** [STAR fails participation too](../../voting_paradoxes/no_show.md). The methods that provably *cannot* are the score-summing ones — Score and Approval — because an added sincere ballot only ever adds support in the direction the voter wanted. So on this axis: **Score / Approval > Condorcet ≈ STAR**, and Condorcet is not the outlier the passage's hedging implies.

## Claim 3 — Smith / top cycle

> "The Smith criterion guarantees an even stronger kind of majority rule. It says that if there is no majority-rule winner, the winner must be in the top cycle, which includes all the candidates who can beat every other candidate, either directly or indirectly. Most, but not all, Condorcet systems satisfy the top-cycle criterion."

**Verdict: right conclusion, wrong definition, and it silently merges two different sets.**

**The definition given is not the Smith set.** "All the candidates who can beat every other candidate, **either directly or indirectly**" describes **beatpath reachability** — X reaches Y if X beats Y, or beats someone who beats Y, and so on. That defines the **Schwartz set** (the top cycle). The **[Smith set](../smith_set.md)** is a different construction: *the smallest non-empty set whose every member beats everyone outside it*. The two coincide when there are no pairwise ties, and **come apart when there are** — Smith is the larger, more conservative set, because a tie is not a win. Using "Smith criterion" and "top-cycle criterion" as synonyms, as the passage does, is fine in casual reading and wrong the moment a tie appears.

**"Most, but not all" is correct — and worth making concrete rather than leaving abstract.** The split matters, because it separates two methods people treat as interchangeable:

| Method | Smith-efficient? | |
|---|:--:|---|
| **[Ranked Robin](../../../05_Ranked_Robin/01_Learn/ranked_robin.md) / Copeland** | ✅ | the best win–loss records *are* the top of the club |
| **Ranked Pairs, Schulze** | ✅ | |
| **Minimax** | ❌ | in a 4+ candidate cycle its "least bad worst loss" pick can land *outside* the Smith set |

That is a real argument for Ranked Robin over Minimax, and it is the kind of thing "most Condorcet systems satisfy it" hides.

**This one is runnable.** The engine prints the Smith set on every Ranked Robin and RCV-IRV report (`show_smith_set`, forced on in the `_tabulated` mirror) — it names the set, says whether it is a lone Condorcet winner or a top cycle, and states whether the winner landed inside it. For RR the block is descriptive; for RCV-IRV it is a genuine pass/fail. → [the Smith set, worked](../smith_set.md), with a four-candidate cycle where the fourth candidate is provably out of contention.

## Claim 4 — the vocabulary itself

The article's framing terms — *majority-rule winner*, *majority-preferred candidate*, *beats-all winner*, *tournament winner* — all name the same candidate, and **three of the four are not safe swaps.** "Majority winner" collides with over-half (a beats-all winner may hold no absolute majority at all); "majority-preferred candidate" is scope-ambiguous and means something narrower throughout *this* library (STAR's runoff finalist); "tournament winner" collides with [tournament solutions](../tournament_solutions.md), which usually return a set. Full table and what to say instead: [the naming decoder](../../../05_Ranked_Robin/01_Learn/condorcet_naming_decoder.md#the-winner-has-aliases-too-and-they-are-not-the-methods).

## The short version

- **Take the stability argument** — it is sound and it beats STAR. But lead with *cycles are rare* (the evidence) rather than *only a beat dislodges a beats-all winner* (the definition), and never let it be heard as IIA.
- **Sharpen the participation paragraph rather than quoting it.** Moulin's theorem, ≥4 candidates, provably unavoidable — then the three-candidate maximin exception, which is the part worth knowing. Leave the "306 datasets" line alone until someone has the citation.
- **Don't reuse the Smith definition.** Say *smallest set whose every member beats everyone outside it*, and name Minimax as the family member that fails.
- **Concede the axis.** Condorcet's spoiler resistance is better than STAR's. The STAR answer is not to dispute that — it is that [the ballot carries intensity](../../scores_and_ranks/scores_vs_ranks.md) and a ranked one does not, which is [a different design disagreement](../../../05_Ranked_Robin/01_Learn/condorcet_naming_decoder.md#the-word-consensus-carries-three-different-jobs) and the honest place to have the argument.

---

## See also

- [FairVote's "Why the Condorcet Criterion Is Less Important Than It Seems," claim-checked](fairvote_condorcet_claim_check.md) — the same exercise on an article arguing the opposite side
- [electowiki's "Cardinal voting," claim-checked](../../scores_and_ranks/cardinal_voting_claims_checked.md) — and on an article arguing *this library's* side, which is the one to check hardest
- [The Smith set](../smith_set.md) · [tournament solutions](../tournament_solutions.md) · [the No-Show paradox](../../voting_paradoxes/no_show.md) · [the spoiler effect](../spoiler_effect.md)
- [Condorcet methods — a reading list](condorcet_reading_list.md) — the sources, each with its lean marked
- [How to learn about voting methods](../how_to_learn_about_voting_methods.md) — the source-tier policy this page applies

# file: condorcet_criterion_claim_check.md
