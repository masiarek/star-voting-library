# Grading as a rival primitive — Balinski & Laraki's assault on the ranked model

*A 301 theory page. Most of the ranked-vs-rated debate accepts one shared assumption: that a voter's real opinion **is** an ordering, and the only question is how much of it a ballot captures. Michel Balinski and Rida Laraki's **Majority Judgment** (MIT Press, 2011) attacks that assumption directly. Their claim is not "rankings are lossy" — it is that the **preference order is the wrong primitive**, a modeling error inherited from Arrow, and that what voters actually have (and can reliably report) are **absolute grades in a common language**. This page lays out the argument, its strongest evidence, and the recent experiment that undercuts its load-bearing premise.*

**Level: 301.** Companions: [Preference vs. support](preference_vs_support.md) — the same gap, shown on two ballots · [Scores vs. ranks](scores_vs_ranks.md) — the general distinction · [Distortion](../topics/distortion.md) — the *other* academic assault on ordinal ballots, from computer science · [Majority Judgment's paradoxes](../voting_paradoxes/majority_judgment.md) — the case against, worked · ["Preference" — the word that causes half the confusion](../topics/preference.md).

---

## The claim, at full strength

Since Arrow, the standard object of social choice has been the **preference profile**: each voter supplies a complete transitive ordering of the candidates, and a voting rule aggregates orderings into an outcome. Everything downstream — Arrow's theorem, Gibbard–Satterthwaite, Condorcet consistency, the entire criteria literature — is built on that object.

Balinski and Laraki argue the object is wrong. Their case, compressed:

- **Voters don't natively hold orderings; they hold evaluations.** Asked "is Bayrou any good?", a voter answers with a judgment about Bayrou — not with Bayrou's position in a queue. The ordering is something an analyst *derives*, and a ballot that demands it forces a construction the voter didn't have.
- **A shared vocabulary of grades supplies the comparability that utilities lack.** This is the move that matters. The classic objection to summing scores is that your 5 and my 5 aren't the same unit. Their answer: fix a **common language** — *Excellent, Very Good, Good, Acceptable, Poor, To Reject* — with meanings established by shared usage, exactly as grades work in wine judging, figure skating, diving, and school. Comparability then isn't *assumed*, it's **instituted by the scale**.
- **Aggregate by median, not sum.** The **majority grade** is the median of a candidate's grades, with an iterative tie-break (the *majority-gauge*). They prove the median-type functions are the ones that are **strategy-proof in grading**: a voter cannot push a candidate's majority grade in their preferred direction by misreporting. Summing has no such property.
- **This escapes Arrow rather than surviving it.** With absolute grades, a candidate's collective grade depends only on that candidate's own grades, so Independence of Irrelevant Alternatives holds trivially. Arrow's impossibility doesn't bind, because its domain — preference orders — is the very thing being rejected.

**Why this is a bigger claim than "scores carry more information."** The expressiveness argument concedes the ranked model and complains it's lossy. Balinski and Laraki refuse the model. On their account, "which do you prefer?" is not a more basic question than "how good is this one?" — it is a *derived* and partly artificial one, and building a century of theory on it was the mistake. That's the strongest academic statement available that ranked ballots have no privileged claim to the word **preference**.

## What they deliberately give up

Read this part before recruiting them as an ally, because it is not incidental:

- **The majority criterion.** MJ can elect a candidate whom an absolute majority grades below another. Not a bug in their view — a majority's *ordering* shouldn't override the electorate's *evaluations*, and protecting against that is presented as a feature in polarized fields.
- **The Condorcet criterion.** Rejected on the same grounds.
- **Summing.** Explicitly argued to be inferior to the median on strategy-resistance.

So Majority Judgment is a rival to **STAR and Score** as much as to IRV. It sits inside the cardinal camp and argues against the score-summing family that STAR's Scoring Round belongs to — see the [books entry](../books/rated_and_score_methods.md) for the same warning. Quoting Balinski and Laraki as backup for "score ballots are better" while their book argues *against* your aggregation rule is exactly the kind of selective sourcing this library tries not to do.

## The evidence for

**The Orsay experiment (2007).** Balinski and Laraki ran majority judgment in parallel with the real first round of the French presidential election in Orsay's 12th precinct — voters cast their official ballot, then graded every candidate. Two findings they lean on: voters used the verbal scale fluently and without confusion, and the **invalid-ballot rate was about 1.08%** — comparable to or better than single-mark, and well inside the range this library quotes for rated ballots on the [scores-vs-ranks](scores_vs_ranks.md) spoilage question. The outcome also moved sharply: the centrist Bayrou, squeezed out under plurality, performed far better on grades — the same [center-squeeze](../../06_Other/RCV_IRV/concepts/RCV_IRV_center_squeeze.md) story STAR tells, from the grading side.

The broader French in-situ program (Baujard, Igersheim, Lebon, Laslier and colleagues, 2007 and 2012) is the best real-world evidence anywhere that voters can and will use an evaluative ballot on a live election day.

## The evidence against — including against the premise

**The paradoxes.** MJ carries a long list: Condorcet winner and loser, absolute winner and loser, truncation, reinforcement, no-show, and twin — most of them reachable with only **two candidates**. That's the Felsenthal & Machover critique, and this repo already works four of the examples: [Majority Judgment's paradoxes](../voting_paradoxes/majority_judgment.md). The median was proposed to cure the mean's intensity problem, and it inherits a different disease — a single well-placed grade can overrule an absolute majority, and the iterative tie-break adds a reinforcement failure that is genuinely hard to see coming.

**And now the premise itself.** The common-language claim is load-bearing — it is what buys interpersonal comparability, and therefore what makes the whole program more than a re-labelled score ballot. In 2026, [**Delemazure, Brunetti, Baujard & Bouveret**](https://hal.science/hal-05114129v1) tested it: an online experiment (N = 1955) grading French presidential candidates under **different grade scales**. The finding is blunt — the grade distributions candidates received were **strongly affected by which scale voters were given**, so the data **reject** the assertion that grades carry absolute meaning.

Note who ran it. Baujard is one of the authors of the French field experiments that supplied evaluative voting's best empirical support. This is the cardinal camp testing its own premise and reporting against it — which is why it is worth more than a critic's version of the same result, and why it belongs on this page rather than being left to opponents to bring up.

## What this library takes from it

**Use Balinski and Laraki for the modeling point, not the method.** The durable, citable contribution is that *"preference = ordering"* is a **contested modeling choice with a serious academic rival**, not the neutral default it's usually treated as. That is the strongest possible support for this library's insistence that a [score ballot reports preferences too](preference_vs_support.md), and that "rank your preferences" is a marketing phrase rather than a definition. It costs nothing and concedes nothing, because it doesn't depend on MJ being a good method.

**Don't use them for the comparability argument.** After Delemazure et al., "a shared grade scale establishes a common unit" is a claim with direct experimental evidence against it. The honest position is the modest one: score ballots capture something ranks can't (this is [demonstrable on two ballots](preference_vs_support.md) and needs no theory of absolute meaning), while whether those numbers are interpersonally comparable remains genuinely unsettled — and is the one objection to score-summing that has never been answered.

**Don't use them against STAR's critics as if they were on our side.** They argue for the median over the sum. If their strategy-proofness-in-grading result is right, it is an argument against the Scoring Round, partially offset by the fact that STAR's runoff exists precisely to blunt score-summing's strategic incentive — the trade-off is real and is [STAR's honest limits](../../01_STAR/01_Learn/properties_and_limits/STAR_honest_limits.md) territory.

**Lean disclosure:** *Majority Judgment* is Balinski and Laraki advocating their own method — the strongest rival case *within* the cardinal camp, and one that cuts against score-summing. Felsenthal & Machover are its sharpest critics and are themselves ordinalists. Delemazure et al. (2026) is peer-reviewed and adversarial to the premise, from authors sympathetic to evaluative voting.

## Sources

- Balinski & Laraki, *Majority Judgment: Measuring, Ranking, and Electing* (MIT Press, 2011) — [MIT Press page](https://mitpress.mit.edu/9780262545716/majority-judgment/); the repo's [books entry](../books/rated_and_score_methods.md).
- Balinski & Laraki, [*Election by Majority Judgment: Experimental Evidence*](https://www.rangevoting.org/ElectionByMajorityJudgmentExptEvidenceFinal.pdf) — the Orsay 2007 write-up. *(Hosted on rangevoting.org, which advocates for score voting and is critical of MJ — the paper is the authors' own, the host is not neutral.)*
- Felsenthal & Machover, *The Majority Judgement voting procedure: a critical evaluation* (2008), via Felsenthal's paradox review §A9 — worked here: [Majority Judgment's paradoxes](../voting_paradoxes/majority_judgment.md).
- Delemazure, Brunetti, Baujard & Bouveret, [*Do Grades Have Absolute Meaning? An Experiment on Majority Judgment*](https://hal.science/hal-05114129v1) — *Social Choice and Welfare*, 2026.

## See also

- [Preference vs. support](preference_vs_support.md) · [Scores vs. ranks](scores_vs_ranks.md) · [The fidelity ladder](fidelity_ladder.md)
- [Distortion](../topics/distortion.md) — the computer-science route to the same conclusion, with theorems
- [Does Arrow's theorem apply to STAR?](../topics/arrow_theorem_and_star.md) — MJ's Arrow escape is a sharper version of the same argument
- [Majority Judgment's paradoxes](../voting_paradoxes/majority_judgment.md) · [Range voting's paradoxes](../voting_paradoxes/range_voting.md)
- [Rated & score methods — the reading list](../books/rated_and_score_methods.md)
