# Ordinal vs. cardinal, as mechanism design — Kim's answer to "but they'll exaggerate"

*The strongest objection to score ballots is not that intensities are unmeasurable. It is practical: **sure, scores would be better if people reported them honestly — and they won't.** Semin Kim's 2017 paper takes that objection seriously by refusing to assume honesty at all. It imposes an incentive constraint first, and asks what the best rule is that survives it. The answer is that a cardinal rule still beats every ordinal rule — and that the winning mechanism looks a great deal like Approval voting.*

**Level: 301 · deep dive** Builds on [cardinal utility](cardinal_utility.md) (301) and [Gibbard–Satterthwaite](gibbard_satterthwaite_theorem.md) (301).

Companions: [Cardinal utility](cardinal_utility.md) — what a score is reaching for · [Gibbard–Satterthwaite](gibbard_satterthwaite_theorem.md) — the impossibility this paper steps around · [Distortion](distortion.md) — the same ordinal-vs-cardinal gap measured in the worst case rather than on average · [Strategic voting](strategic_voting.md) — the practical side. **Run it:** [the (A,B)-scoring family, on one electorate](../../method_comparisons/kim_ordinal_vs_cardinal/README.md).

---

## The move that makes the paper possible

Voting theory's two famous impossibilities both bite here. [Arrow](arrow_theorem_and_star.md) says no rule can aggregate rankings while satisfying a short fairness list. [Gibbard–Satterthwaite](gibbard_satterthwaite_theorem.md) says no deterministic, non-dictatorial rule over three or more candidates is **strategy-proof** — honest voting is never a dominant strategy. Our page on the latter lists four ways out: two candidates, dictatorship, a restricted outcome set, or randomization. Every one is either useless or unusable.

Kim takes a fifth, and it belongs on that list: **weaken the incentive requirement itself.**

| | Requires | Reads as |
|---|---|---|
| **Strategy-proofness** (dominant-strategy IC) | honesty is best *no matter what anyone else does* | G–S applies; nothing usable survives |
| **Bayesian incentive compatibility (BIC)** | honesty is best *when everyone else is honest*, in expectation over a shared prior | truth-telling is a Bayes–Nash equilibrium |

BIC is genuinely weaker, and the weakening is exactly what earns the positive results. Whether it is *weak enough to be uninteresting* is the live question, and it gets its own section below.

The rest of the setup is standard Bayesian mechanism design with one deliberate amputation: **no monetary transfers.** In ordinary mechanism design you fix incentive problems by paying people; in an election you may not. Kim's model is the classic problem with that tool removed — which is why its results do not look like the auction-theory results a reader might expect.

**The environment, stated plainly**, because every result below is conditional on it:

- `n` voters, `m ≥ 3` alternatives, private values drawn **independently** across voters.
- Each voter's values are **normalized**: top alternative = 1, bottom = 0, the middle ones somewhere between. The middle value *is* the preference intensity.
- The environment is **neutral** — alternatives are symmetric *ex ante*, so before ballots are cast no candidate is more likely than another to be anyone's favorite.
- Rules may be **randomized**: a rule maps reported values to a *lottery* over alternatives.
- Welfare is **utilitarian** — the sum (equivalently, with identical distributions, the average) of expected utilities.

## Result 1 — inside the ordinal world, incentives are nearly free

**Theorem 1.** For any ordinally Pareto-efficient rule, there is an **incentive-compatible** ordinal rule giving every voter the same expected utility.

Kim calls this somewhat surprising, and it is. The strategic-voting literature treats ranked rules as riddled with incentives to misreport; here, in a neutral environment, Pareto efficiency alone buys incentive compatibility at no welfare cost. Note which direction it cuts: **this is a result in favor of ranked ballots**, and the honest reading is that the case against them is not primarily about incentives.

Two supports underneath it are worth having on their own.

**Proposition 1** characterizes the Pareto-efficient ordinal rules: they are exactly the **scoring rules whose scores are the expected values of the ranked positions**, given the voter's ranking. Not an arbitrary point vector — the statistically correct one.

**Corollary 1** picks out the utilitarian-best member. And here is the part worth sitting with: if a voter's second-place value is uniform on `(0,1)`, its expected value is **½**, so the optimal ordinal rule is `(1, ½, 0)` — **the Borda count**.

> **Borda is the benchmark, not a strawman.** This library is otherwise hard on Borda — see [Dark Horse](../../method_comparisons/dark_horse_borda/README.md) — so it matters that in Kim's environment Borda is *the best an ordinal ballot can do*. Theorem 2's claim is that a cardinal rule beats **that**, which is a far stronger claim than beating plurality.

**And the neutrality assumption is load-bearing, by the author's own example.** Kim opens with a *non-neutral* environment — two alternatives popular ex ante — and shows Borda is **not** incentive compatible there: a voter whose second choice is nearly as good as their first can gain by misreporting the order. Change the single assumption to neutrality and the same rule becomes IC. Real elections have polls, frontrunners and incumbents, which is precisely what neutrality forbids. Theorem 1 is a result about a symmetric world, and it says so.

## Result 2 — a cardinal rule beats every ordinal rule, incentives included

**Theorem 2.** With identically distributed voters (and, in the working-paper version, `n ≥ 5`), there exists an **incentive-compatible cardinal rule** achieving higher utilitarian welfare than **any** ordinal rule.

The word doing the work is *incentive-compatible*. Building a cardinal rule that beats ordinal rules is trivial if you assume honesty — just add up the true values. The hard part is that the first-best cardinal rule is generally **not** IC: Börgers and Postl (2009) show it failing in exactly this kind of setting. Theorem 2 says you do not have to choose. The cardinal advantage survives the incentive constraint.

### The mechanism, and why it looks like Approval

The construction is the most teachable thing in the paper. Take each ranking-type of voter and split it in **two**, by a threshold `β` on the value of their **second** choice:

- **H type** — my second choice is close to my first.
- **L type** — my second choice is close to my last.

Then run a scoring rule where H types' ballots carry a **high** middle score and L types' a **low** one. That is one extra bit per voter beyond the ranking, and it is the only cardinal information the rule uses.

Why is it incentive compatible? Because `β` is chosen so that the voter sitting *exactly* on the threshold is **indifferent** between declaring H and declaring L. Everyone above the threshold then strictly prefers H, everyone below strictly prefers L, and honesty is a best response throughout. In the paper's two-voter uniform example that threshold is `β* = 1/√2 ≈ 0.707`.

**Proposition 2** names the resulting family. With three alternatives it is Myerson's **(A,B)-scoring rule**: each voter hands in a permutation of `(1, A, 0)` or `(1, B, 0)`, with `0 ≤ A ≤ B ≤ 1` — and *the voter chooses which*. The familiar rules are its corners:

| (A, B) | Rule | Ordinal? |
|---|---|:--:|
| `(0, 0)` | Plurality | yes |
| `(½, ½)` | Borda | yes |
| `(1, 1)` | Negative voting (anti-plurality) | yes |
| `(0, 1)` | **Approval** | **no** |
| `≈ (0.354, 0.854)` | **Kim's rule**, in the two-voter uniform example | **no** |

Read the last two rows together and the paper's punchline appears: **the optimal incentive-compatible rule is Approval voting with the corners pulled in.** Approval is the extreme version — 0 or 1, nothing between — of the same idea, and the same idea is: *let the voter say whether their second choice counts.* Approval's status as the one non-ordinal corner is Kim's own observation; it is the rule that, in his words, "requires more than information about ordinal preferences."

The welfare gain in the two-voter example is real but modest — `117/72` against Borda's `114/72`, about 2.6%.

**The takeaway for a score ballot, stated carefully.** The cardinal information that survives an incentive constraint is not *how much do you like each candidate*. It is one narrow question: **is your second choice nearer your first or your last?** A score ballot is the ballot that asks it. STAR's 0–5 asks it with six answers instead of two — but note that Kim proves the optimum among rules using *one* threshold, and never shows that more thresholds are better. See the limits below.

## Result 3 — the finding worth quoting in an argument

The published version closes with numerical work on the simplest non-trivial case: **two voters, three alternatives, uniform values.** It computes utilitarian welfare four ways — the **first-best** rule (honesty assumed), the **second-best** (the best IC rule), the **best ordinal** rule, and the Theorem 2 rule — and reports that:

> **The welfare lost to incentive constraints is much smaller than the welfare lost to restricting yourself to ordinal rules.**

In plain terms: **the ballot format costs you more than strategy does.** It also finds the second-best rule loses efficiency only in one situation — when the two voters have **opposite** rankings — and checks robustness by swapping the uniform distribution for a beta.

This is the average-case, Bayesian cousin of what [distortion](distortion.md) measures in the worst case, and the two agree in direction. That is worth something: the ordinal-vs-cardinal welfare gap is not an artifact of adversarial constructions.

**Note the contrast with two candidates.** Kim cites Azrieli and Kim (2013) and Schmitz and Tröger (2012) for the two-alternative case, where **no** IC rule outperforms the optimal ordinal ones and plain majority rule is optimal. The cardinal advantage is a three-or-more-candidate phenomenon — the same threshold at which [Gibbard–Satterthwaite](gibbard_satterthwaite_theorem.md) starts to bite. With two candidates there is nothing to be strategic about and nothing extra to say; both facts have the same cause.

## Run it

The (A,B) family is small enough to tabulate directly, so this library runs it on **one 36-voter electorate with fixed rankings**, changing only what a second choice is worth:

| (A, B) | Rule | Winner |
|---|---|:--:|
| `(0, 0)` | Plurality | **Cocoa** |
| `(½, ½)` | Borda | **Almond** |
| `(1, 1)` | Negative voting | **Berry** |
| `(0, 1)` | Approval, lukewarm second choices | **Almond** |
| `(0, 1)` | Approval, intense second choices | **Berry** |

One electorate, nobody changing their mind, three different winners from a dial the *designer* turns — and then two more from the same rankings when the *voters* hold it, using information no ranked ballot records. → **[the cases, with the full counts](../../method_comparisons/kim_ordinal_vs_cardinal/README.md)**

## Claim-check

Per [house practice](../../method_comparisons/fairvote_star_whitepaper/README.md), a source that supports our side gets tested harder, not quoted more. Kim is not an advocate — this is a technical paper in a general-interest economics journal, with no ballot to sell — which makes it a *better* source than the campaign literature and a *narrower* one.

**What holds up:**

- **The G–S escape is legitimate and clearly signposted.** Kim does not claim to have beaten Gibbard–Satterthwaite; he states the weakening in the first two paragraphs. Anyone citing Theorem 2 has to carry BIC along with it.
- **Theorem 1 is a concession, and it is in the paper.** A cardinal-voting result that also finds ordinal rules are fine on incentives is not cherry-picked toward a conclusion.
- **The Borda benchmark is honest.** Beating the best ordinal rule is the right bar, and the paper sets it for itself.
- **The (A,B) framing is genuinely clarifying** — independent of any theorem, "plurality, Borda, anti-plurality and approval are one family indexed by what your second choice is worth" is a better mental model than four separate rules, and it is checkable in five minutes with the cases above.

**Where it does not reach as far as it looks:**

- **BIC assumes a common prior and honest opponents — which polls destroy.** A voter who has read a poll no longer holds the symmetric prior the theorem is stated over. Kim's *own* opening example is the demonstration: make two alternatives popular ex ante and Borda stops being IC. Most of the strategic behavior this library worries about — [bullet voting](../../01_STAR/05_Practice/ex06_bullet_backfire.md), exaggeration, frontrunner-driven compression — is a response to exactly the information neutrality assumes away. **This paper does not retire the exaggeration critique of Score.** It shows the critique is not a theorem.
- **The optimal rules are lotteries.** Rules map reports to *randomized* outcomes, and randomization is doing real work (it is also one of G–S's own escape hatches). Every method this library teaches is deterministic apart from [tiebreaks](ties/README.md). A rule that is better on average because it sometimes flips a coin is not obviously a rule anyone would adopt.
- **The numbers are two voters.** The analytical results are general (Theorem 2 in the working paper wants `n ≥ 5`), but the welfare comparison everyone will want to quote — *format costs more than strategy* — is computed on a two-agent, three-alternative, uniform-value model. Treat it as a well-motivated indication, not a measured quantity.
- **The normalization smuggles in comparability, and the paper says so.** Setting every voter's top to 1 and bottom to 0 makes the scales interpersonally addable by construction. Kim flags in a footnote that it is arguable whether this captures intensity or licenses interpersonal comparison, and explicitly rules the question out of scope. That is honest, but it means the paper **assumes** the answer to the hardest question on the [cardinal utility](cardinal_utility.md) page rather than supplying one. It is the same normed-ballot move Hillinger makes — with the same strength (every voter gets equal power) and the same weakness (nobody has shown the normed number tracks anything).
- **"Cardinal beats ordinal" is a claim about a rule class, not about STAR.** Every rule in Kim's space maximizes a **sum**. STAR is not in that space: the [automatic runoff](../../01_STAR/01_Learn/the_count/STAR_Automatic_Runoff.md) applies a majoritarian correction *after* the sum, which is the very step the utilitarian framework treats as an error. The paper's support lands on **cardinal ballots**, and stops there.
- **One threshold is proven optimal; a 0–5 scale is not.** Kim's mechanism gives each voter **two** options. Nothing in the paper says six is better, and the [scale-granularity](../scores_and_ranks/scale_granularity_flips_the_winner.md) evidence suggests the number of levels does substantive work. Citing this paper for "0–5 is right" would be citing it for something it does not contain.

### Where it cuts against us

Fairness runs both ways, so this gets stated rather than buried:

- **The rule it endorses is Approval-shaped, not STAR-shaped.** If you read Proposition 2 as practical advice, the nearest real ballot is an [Approval](../../04_Approval/README.md) ballot, and the second-nearest is a three-level score ballot — Hillinger's EV-3, not a 0–5 grid.
- **Theorem 1 is ammunition for ranked-ballot advocates.** *"Efficient ordinal rules are incentive compatible"* is a sentence an [RCV](../../06_Other/RCV_IRV/README.md) advocate can use, and the correct response is not to dispute it but to name its condition (neutrality) and its scope (it says nothing about IRV specifically — Theorem 1 is about Pareto-efficient *scoring* rules, and IRV is not one).
- **The measured gain is small.** 2.6% in the worked example. This is not a paper that says ordinal ballots are broken; it says they leave something on the table.

**Sourcing disclosure, since a claim-check that hides its own sources is doing the thing it exists to prevent.** The published paper (*GEB* 104, 2017) is paywalled. The theorem statements, the motivating example, the construction, `β* = 1/√2`, the `117/72` vs `114/72` figures and Proposition 2 here are read from the author's **freely available 2013 job-market-paper version**, which the published article grew out of. Two differences are known and should be assumed to matter: the job-market paper says **ex-ante** Pareto efficient where the published abstract says **ex-post**, and its Theorem 3 (on single-peaked domains, every IC ordinal rule is peak-only) was **replaced** in publication by the numerical section. The Result 3 material above therefore comes from the published abstract and introduction only, not from a read of that section. Anyone building on this page should pull the published version.

**Lean disclosure:** none to declare in the usual sense — Kim is a theorist, not a reform advocate, and the paper endorses no ballot. The lean to watch is *ours*: this is a result that flatters score ballots, which is exactly why the limits section above is longer than the results section.

## New terms this page introduces

Added to the [glossary](../GLOSSARY.md).

| Term | One line |
|---|---|
| **Bayesian incentive compatibility (BIC)** | honesty is a best response *when others are honest*, in expectation over a shared prior — strictly weaker than strategy-proofness |
| **(A,B)-scoring rule** | Myerson's three-candidate family: each voter picks a permutation of `(1, A, 0)` or `(1, B, 0)`; plurality, Borda, anti-plurality and approval are its corners |
| **Negative voting** (anti-plurality) | the `(1,1)` corner — a ballot that says only who you are *against*; fewest last places wins |
| **Ordinally Pareto efficient (OPE)** | no other ordinal rule makes every voter better off in expectation |
| **First-best / second-best rule** | the welfare-maximizing rule with honesty assumed / with the incentive constraint imposed |
| **Neutral environment** | alternatives are symmetric *ex ante* — no candidate is more likely than another to be anyone's favorite before ballots are cast |

## Related

- [Cardinal utility](cardinal_utility.md) — measurability vs. comparability, the vNM trap, Harsanyi, and Hillinger's normed-ballot answer that Kim's normalization quietly reuses
- [Gibbard–Satterthwaite](gibbard_satterthwaite_theorem.md) — the escape hatch this paper takes
- [Distortion](distortion.md) — the worst-case measurement of the same ordinal-vs-cardinal gap
- [Strategic voting](strategic_voting.md) · [STAR's honest limits](../../01_STAR/01_Learn/properties_and_limits/STAR_honest_limits.md) — where the exaggeration critique actually lives
- [Approval in the theory literature](../../04_Approval/01_Learn/approval_in_the_literature.md) — what a checkmark means, which is the question Kim's mechanism answers with a threshold
- [Scores vs. ranks](../scores_and_ranks/scores_vs_ranks.md) — the ballot-level distinction, without the theory
- **The cases:** [one dial, three winners](../../method_comparisons/kim_ordinal_vs_cardinal/README.md)

**Sources.** Kim, S. (2017), "Ordinal versus cardinal voting rules: A mechanism design approach," *Games and Economic Behavior* 104, pp. 350–371 ([DOI](https://doi.org/10.1016/j.geb.2017.04.012)); working-paper version, Ohio State job market paper, 2013 ([PDF](https://economics.osu.edu/sites/economics.osu.edu/files/JMP_Semin_Kim.pdf)) · Myerson, R. (2002), "Comparison of scoring rules in Poisson voting games," *Journal of Economic Theory* 103, pp. 219–251 · Börgers, T. & Postl, P. (2009), "Efficient compromising," *Journal of Economic Theory* 144 · Majumdar, D. & Sen, A. (2004), "Ordinally Bayesian incentive compatible voting rules," *Econometrica* 72 · Gibbard, A. (1973) and Satterthwaite, M. (1975) — see [that page](gibbard_satterthwaite_theorem.md) for full citations.
