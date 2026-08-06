# Cardinal utility — the number a score ballot is reaching for

*A 301 theory page, and the missing definition under a lot of this library. Half a dozen pages here already assume voters "have utilities" — [distortion](distortion.md) treats a ranked ballot as lossy compression of them, [VSE](what_makes_a_good_winner.md) scores methods against them, the [spatial model](spatial_voting_model.md) manufactures them from distance, and the simulations [sample them first](simulate_utilities_not_ballots.md). None of those pages says what a utility **is**, or what makes one **cardinal**. This one does — and then asks the question that decides the whole ranked-vs-rated argument: is the number a voter writes in a 0–5 bubble a **measurement** of anything?*

**Level: 301 · deep dive** Builds on [scores vs. ranks](../scores_and_ranks/scores_vs_ranks.md) (101) and [preference vs. support](../scores_and_ranks/preference_vs_support.md) (201).

Companions: [Does Arrow apply to STAR?](arrow_theorem_and_star.md) — where the ordinal/cardinal line is load-bearing · [Grading as a rival primitive](../scores_and_ranks/grading_as_a_rival_primitive.md) — the attack on utility from *inside* the cardinal camp · [Social welfare function](social_welfare_function.md) — the object being maximized · [Distortion](distortion.md) — utility as the assumed ground truth · [Ordinal vs. cardinal as mechanism design](ordinal_vs_cardinal_mechanism_design.md) — the same question asked with an incentive constraint attached, and Kim's normed ballot reusing Hillinger's move.

---

## The definition that actually does the work

"Cardinal" does not mean "has numbers." Every utility function has numbers. What separates ordinal from cardinal is **which transformations leave the meaning intact** — the invariance class. That is the whole definition, and almost every confusion downstream comes from skipping it.

| Scale | Invariant under | Preserves | A voting analogue |
|---|---|---|---|
| **Ordinal** | *any* increasing transformation (`u → f(u)`, `f` monotone) | the **order** only | a [ranked ballot](../scores_and_ranks/ranked_ballot.md) |
| **Cardinal** (interval) | *positive affine* only (`u → au + b`, `a > 0`) | order **+ the ordering of differences** | a [0–5 score ballot](../scores_and_ranks/score_ballot.md) |
| **Ratio** | *positive scaling* only (`u → au`) | order, differences, **and ratios** | (nothing in common use — a ballot with a meaningful absolute zero) |

An ordinal scale can say *"I prefer Ana to Bruno."* A cardinal scale can additionally say *"I prefer Ana to Bruno **more than** I prefer Bruno to Chloe"* — because the ordering of the gaps survives rescaling. It still cannot say *"Ana is twice as good as Bruno"*; that is a ratio claim, and it dies the moment you slide the origin. This is the precise sense in which a score carries what the repo elsewhere calls [**support**](../scores_and_ranks/preference_vs_support.md) and a rank does not.

**You can watch the invariance hold.** The [rescaled twin case](../../method_comparisons/hillinger_evaluative_voting/cases/cases_pages/hillinger_t4_affine.md) runs one election twice — once with marks `(0, 1, 2)`, once with every mark put through `u′ = 2u + 1` to give `(1, 3, 5)`. The totals move (39 → 108, 29 → 88, 22 → 74). The finalists, the winner, the runoff margin and the ordering do not. That is cardinality, demonstrated rather than asserted.

## Two axes, not one: measurability × comparability

Here is the distinction that makes the standard objection to score voting precise, and it is missed constantly in debate: **cardinal is not the same as interpersonally comparable.** They are independent properties, and Amartya Sen's framework (*Collective Choice and Social Welfare*, 1970) treats them as separate axes.

- **Measurability** — how much structure exists *within* one person's utilities. Ordinal? Cardinal? Ratio?
- **Comparability** — how much of that structure can be read *across* people. Not at all? Units comparable ("a one-point gain for me is a one-point gain for you")? Levels comparable ("I am better off than you")? Fully?

A voter can have a perfectly good cardinal utility function that is completely incomparable to anyone else's — cardinality is a fact about one person's own scale, and rescaling *each voter separately* is exactly what a purely intrapersonal reading permits. So:

> **Summing scores across voters requires cardinal measurability *and* unit comparability.** Cardinality alone does not license addition. It never did.

This is why the objection "your 5 and my 5 aren't the same thing" is not a quibble to be waved off — it is a request for the *second* axis, and the first axis does not supply it. (It is also why the [Rawlsian maximin](what_makes_a_good_winner.md) alternative has different requirements: it needs *level* comparability but not cardinality at all. Different ethics, different measurement bill.)

## The von Neumann–Morgenstern trap

The most common bad argument for score ballots runs: *"von Neumann and Morgenstern proved utility is cardinal, therefore intensities are real, therefore scoring is sound."* Every step of that is doing something other than it appears to.

vNM utility (*Theory of Games and Economic Behavior*, 1944) is genuinely cardinal — unique up to positive affine transformation, exactly as above. But look at where the cardinality **comes from**: it is recovered from choices among **lotteries**. Your utility gap between Ana and Bruno is pinned down by the probability `p` at which you are indifferent between Bruno for certain and a gamble paying Ana with probability `p`, Chloe otherwise. The number is calibrated by your **attitude toward risk**, not by introspected strength of feeling.

Those are not the same quantity, and nothing guarantees they coincide. A vNM utility function is a representation of risk preferences that happens to have interval structure; "how much I like Ana" is a psychological magnitude. Treating the first as a measurement of the second is an extra assumption, not a theorem — and it is one the expected-utility literature has never established. Nor does vNM give you the comparability axis: it is silent across people by construction.

**So the trap is worth stating plainly:** vNM makes *one person's* scale cardinal, on a calibration that has nothing to do with intensity, and offers nothing interpersonal. A ballot mark is not a vNM utility. Any argument that leans on vNM to justify adding up 0–5 marks has borrowed the word "cardinal" and left the theorem behind.

## How economics talked itself out of it, and social choice inherited the ban

Classical economics was **utilitarian**: the purpose of institutions is to maximize the sum of individual utilities. It stayed philosophy because it never measured anything. The **marginalist** counterattack claimed superior scientific standing, and the twentieth century finished the job — Lionel Robbins (1932) argued interpersonal utility comparisons are value judgments rather than science; Samuelson's **revealed preference**, in the operationalist spirit of the day, rebuilt demand theory on observable choice alone; behaviorism made the same move in psychology. Cardinal utility was left looking metaphysical.

Arrow's *Social Choice and Individual Values* (1951) was built inside that settlement: its inputs are **rankings**, and its [social welfare function](social_welfare_function.md) is ordinal all the way down. The impossibility result is therefore a theorem about a deliberately impoverished input — which is the point [Does Arrow apply to STAR?](arrow_theorem_and_star.md) turns on, and it is worth being clear that the restriction was a *methodological commitment of the era*, not a discovery about elections.

The cardinal counterattack came from inside economics. **Marcus Fleming** (1952) and **John Harsanyi** (1955, 1977) showed that collective choice satisfying reasonable conditions *is* possible once preferences are expressed on an independent cardinal scale. What neither supplied was a ballot. Operationalizing them for actual elections is a much later project — Warren Smith's range voting (2000), Balinski & Laraki's [majority judgment](../scores_and_ranks/grading_as_a_rival_primitive.md) (2010), and the paper this page leans on most.

## Harsanyi's aggregation theorem — the cardinal camp's strongest formal card

Harsanyi's argument (the 1977 derivation, which Hillinger considers the cleaner one) needs two assumptions:

- **Assumption I — individual rationality.** People decide under uncertainty by maximizing expected utility (i.e. they have vNM utilities).
- **Assumption II — the ethical stance.** In judging a social arrangement, a person abstracts from their own position and reasons as though they were equally likely to be *any* member of society, inheriting that person's circumstances **and tastes**. This is the **veil of ignorance** (Rawls, 1958/1971).

Put them together and the social ranking that every individual would endorse is the one maximizing the **average of individual utilities** — the **utilitarian social welfare function**. Applied to voting: if you could be any voter with equal probability, the rule you would unanimously choose is *pick the alternative with the largest score sum*.

That is a real result and the strongest formal warrant the cardinal camp has. Note precisely what it costs: it needs Assumption I, so the utilities in it are **vNM utilities** — see the trap above — and Assumption II smuggles in comparability by having one person imaginatively occupy another's tastes, which is the very step Robbins objected to. The theorem does not dissolve the comparability problem; it *assumes a resolution* and derives the consequence.

## Hillinger's three moves

Claude Hillinger's **"Voting and the Cardinal Aggregation of Judgments"** (Munich Discussion Paper 2004-9, [DOI](https://doi.org/10.5282/ubm/epub.353)) is the most useful single source for turning all of the above into a ballot. His thesis: voting is an instance of the **aggregation of judgments** — a more general thing than the aggregation of preferences — and to aggregate judgments you must first **measure** them. Aggregation has been unproblematic wherever it rested on an *independent and unrestricted* scale; voting theory's scales are neither. Three moves are worth taking away, and the third is the one that matters for STAR.

### 1. Every voting rule is already cardinal — they differ only in what they forbid

This reframing is the paper's best teaching device. Nobody chooses between "ordinal methods" and "cardinal methods"; every rule assigns numbers and adds them. What separates them is the **restriction** each imposes on the scale.

| Rule | The implied scale | The restriction imposed |
|---|---|---|
| **Plurality** | two values, `(0, 1)` | `1` may be given to **exactly one** candidate |
| **Borda** | `N` equidistant values, `N−1 … 0` | every voter must use **every value exactly once** — forced strict ranking, forced equal gaps |
| **Cumulative** | `(0, 1, … N)` | the marks must **sum to** `N` |
| **Approval** | two values, `(0, 1)` | none on allocation — plurality's restriction *lifted* |
| **Evaluative (EV)** | `t` values, chosen pragmatically | none |

Read down the "restriction" column and the ranked-vs-rated debate looks different. Borda's equal steps are not a neutral reading of a ranking — they are a cardinal assumption imposed on every voter alike. Plurality is not "the simple method"; it is a cardinal scale with a severe allocation rule bolted on. Only approval and EV are, in Hillinger's phrase, free of such restrictions.

### 2. Ordinal scales are *context dependent* — and that is why IIA fails

The genuinely original contribution. Hillinger adds a second axis to the familiar ordinal/cardinal one: is the scale **context dependent** or **independent**? A context-dependent scale is one whose values depend on the set of objects being measured.

A ranking is context dependent, and this is easy to miss because it looks like pure order. But on a ranking the *distance* between two candidates is measured in **intervening candidates** — so it changes when a third party enters or drops out, without anyone's opinion changing at all. That, he argues, is the mechanism behind violations of [independence of irrelevant alternatives](spoiler_effect.md): Arrow's paradox is "a consequence of the situational scale he chose." On an independent scale, the value attached to a candidate depends on **that candidate alone**, so IIA is satisfied automatically — no rule design required.

Whether this fully explains Arrow is contestable (the theorem is a statement about aggregation, not only about scales). But as a diagnosis of *why* [spoilers](spoiler_effect.md) exist, it is sharp, and it is the cleanest available answer to "why does adding a candidate change the result between two others?"

### 3. The ballot number is a normed report, not a measurement of feeling

This is the move that rescues score ballots from the comparability objection — and it works by **giving up** the claim that the objection attacks.

Hillinger explicitly refuses the psychological reading. He agrees preference intensities should be reflected in the vote, but disagrees "with the relevance of the psycho/physical intensity of preferences." His scales are **arbitrarily normed by specifying the admissible values** a voter may report; they are uniform across voters and give each voter the same power over the outcome. His justification is worth quoting because it is a political argument, not a measurement one:

> Some voters will feel much more passionately about the alternatives than others. I believe … that such passions should not be rewarded by a proportional increase in voting power.

And the invariance, stated as a physicist would: the voting scales "are arbitrary up to a linear transformation. Only, when adding different measurements, we must use the same scale!"

So the ballot mark stops pretending to be a reading of an inner state and becomes what it visibly is — **a report on a shared, bounded instrument**. The interpersonal-comparability objection was aimed at a claim about mental magnitudes; against a normed reporting convention it lands differently, because nobody claimed your 5 and my 5 are the same feeling. They are the same *allowance*. This is the same logic the library already runs under a different name — [the equally weighted vote](../../01_STAR/01_Learn/properties_and_limits/equally_weighted_vote.md) and [one person, one vote](one_person_one_vote.md).

## Where the "5 or 6 levels" figure comes from

The claim-check below leans on Hillinger's "5–6 levels" limit, so it is worth showing what he actually rests it on. His §3 argument is **empirical, not theoretical**: societies already collect and aggregate cardinal judgments constantly, and have done so long enough for a house style to emerge.

| Domain | The instrument | How it's aggregated |
|---|---|---|
| **Schooling** | letter or numeric grades — German universities run **1–5**, 1 = excellent, 5 = fail (with a 0.5 for exceptional work) | repeated **weighted averaging** — a quiz counts less than an exam, course grades average into a degree |
| **Commerce** | quality ratings, usually verbal — *excellent / good / average / poor / unacceptable* — converted to **(2, 1, 0, −1, −2)** | mean across respondents |
| **Opinion polling** | the *Politbarometer* (Forschungsgruppe Wahlen) rates politicians **+5 to −5**; Michigan's **feeling thermometer** runs 0–100 | mean per politician |

Two things follow, and they pull in opposite directions for STAR.

**The supportive one.** Whenever a discrete scale is chosen for judgments, it lands on roughly **five or six values** — which Hillinger reads as a practical ceiling on how finely people can discriminate along a cardinal scale. STAR's **0–5** is six levels. On this reading the STAR ballot is not a voting-reform invention at all; it is the same instrument that schooling, commerce and polling each arrived at independently. That is the strongest available answer to *"you're asking voters to do something unnatural"* — they already do it for films, restaurants and their children's report cards, and nobody calls that an unreasonable cognitive demand. It also reframes the [expressiveness argument](../scores_and_ranks/scores_vs_ranks.md): the question is not whether people *can* grade, but whether a ballot is allowed to record what they already do.

**The awkward one.** His own recommendation is *narrower* than STAR's: **three levels `(−1, 0, +1)` for general elections**, five for committees of experts, on the grounds that scale fineness is a cost/benefit judgment rather than a matter of principle — you do not weigh a freighter on a precision balance. So the most-cited cardinal-voting advocate would hand a general electorate a **three-level** ballot, not a six-level one. STAR sits inside his stated limit, so this is a mild disagreement rather than an objection — but it is a disagreement, and the "fineness is pragmatic" premise behind it is the claim later evidence hits hardest ([see the claim-check](#claim-check)).

> **Sourcing note.** Hillinger's own citations here are Duncan (1984) on the history of social measurement — whose first chapter treats **voting itself as an instance of social measurement**, the framing this whole page runs on — and Dawes (1972) on rating and attitude scales. Both are outside voting theory, which is what makes them useful: the 5–6 convergence is not a fact the cardinal-voting camp generated for its own use.

## How much a ballot can say, counted

A small, sharp idea from §4 that the library did not previously have: **count the distinct votes a ballot format admits.** With `N` candidates (excluding the all-equal votes, which are abstentions):

| Candidates | Plurality | Approval | EV-3 | EV-5 |
|---|:--:|:--:|:--:|:--:|
| *N* | `N` | `2ᴺ − 2` | `3ᴺ − 3` | `5ᴺ − 5` |
| **5** | **5** | **30** | **240** | **3,120** |

Plurality with five candidates admits five possible ballots. That is the entire vocabulary the electorate is given to describe what it wants. Approval multiplies it sixfold, a three-level scale eightfold again. It is a crude measure of expressiveness — it counts distinct marks, not useful distinctions — but as a one-line answer to "does the ballot format really matter that much?" it is hard to beat.

## The strict-ranking assumption, quantified

The other quantitative idea worth importing. Social choice theory routinely assumes voters have **strict, complete, transitive** rankings — Saari's "unrestricted domain" makes it a definition, and calls voters without one *irrational*. Hillinger asks how plausible that is. Let `p` be the probability that, for a randomly chosen pair, a voter strictly prefers one to the other. With `p = 0.8`:

- **3 candidates** → 3 pairs → `0.8³ ≈ 0.512`. Barely half of voters have a strict order over *three* candidates.
- **6 candidates** → 15 pairs → `0.8¹⁵ ≈ 0.035`. Essentially nobody does.

The probability of a strict order collapses as the field grows. Hillinger's asymmetry is the payoff: on an EV-*k* ballot a voter **may** report a strict order — *"he can, but is not forced."* Indifference is expressible rather than an error to be modelled away. This is the empirical case for [weak ranks](../scores_and_ranks/weak_ranks.md) and for rated ballots generally, and it deserves more weight in debate than it gets. (Saari himself concedes the assumption "seems to violate reality," defending it as a simplification.)

## Run the paper's own example

Hillinger's §12 Table 4 is his "mirror pathology" of IRV: where plurality's famous defect is that an *unpopular* candidate can win, IRV's is that the **most popular** candidate can be eliminated in round one. Thirty voters, three candidates — and the engine reproduces his score totals exactly (Ana 39, Bruno 29, Chloe 22).

What the runnable version adds: Hillinger reports only the STV failure, but this one electorate splits **three ways**.

| Method | Winner | Why |
|---|---|---|
| **Plurality** | **Chloe** | most first choices (11) — and last-ranked by 19 |
| **RCV-IRV** | **Bruno** | Ana holds the fewest first choices (9), is eliminated first, her ballots transfer |
| **STAR · Score · Ranked Robin** | **Ana** | highest score sum, and the [Condorcet winner](condorcet/README.md) — beats Bruno 20–10, Chloe 19–11 |

Ana is the one candidate **nobody ranks last**, and she is the first one IRV throws out. → **[the case, with the full count](../../method_comparisons/hillinger_evaluative_voting/README.md)**

*(One footnote from checking his arithmetic against the engine: the paper reports the Ana–Bruno pairwise as `ab(20/11)`, which sums to 31 of 30 voters. It is 20–10; the `ac(19/11)` beside it is correct. A typo, not an error in the argument — but it is the kind of thing a runnable companion catches.)*

## Claim-check

Per [house practice](../../method_comparisons/fairvote_star_whitepaper/README.md), an advocacy source gets tested rather than quoted. Hillinger is arguing for his own proposal, and the paper is a **discussion paper** — not peer reviewed. It shows: the axiom list in §11 skips **A4** and mislabels **A.5**, and footnote 8 dismisses proportional representation as "another terrible, though popular, idea" without a word of support. Take the ideas, not the polish.

**What holds up:**

- **The restriction table (§4).** Straightforwardly true and genuinely clarifying. Borda *does* impose equal cardinal steps on every voter; plurality *is* a restricted two-value scale.
- **The strict-order probability argument (§10).** Simple, quantitative, and damaging to a domain assumption most of the field treats as free.
- **The neutral middle (§10).** He concedes a real criticism of approval — that a voter with no information is forced to be *for* or *against* — and answers it: on a three-level scale a zero is genuinely neutral. This is why a middle value earns its place, and it maps onto the library's own [abstention markers](../../YAML_library/README.md), which tabulate as 0 without pretending to be a judgment.
- **The expressive case for a negative pole (§9).** If voting is partly expressive, a ballot that can only say *"for"* silences voters whose strongest feeling is opposition. Underrated, and the library has no page on it.

**Where it overreaches:**

- **The Harsanyi warrant does not transfer — and this is the paper's weakest joint.** Move 3 says the ballot numbers are arbitrary normed conventions, not utilities. But the theorem imported in §7 is about **vNM utilities**, and its conclusion is that maximizing their sum is what rational agents behind a veil of ignorance would choose. Maximize the sum of *normed reports* instead and you have a defensible voting rule — but not the utilitarian conclusion, because the objects being summed are no longer the objects the theorem is about. Hillinger wants the practicality of the convention **and** the moral authority of the theorem. The argument supports one or the other.
    > **Provenance — this one is the library's own, not a citation.** The other objections on this page trace to published work or to Hillinger's own admissions. This one was constructed here, by reading §6–§7 against §11, and no source is being leaned on for it. That is worth flagging in both directions: it is not backed by a literature that has vetted it, and it is not a criticism you can attribute to anyone but us. If it is wrong, the likeliest repair is that Hillinger means his normed reports to *stand in* for vNM utilities as a practical proxy — in which case the transfer needs an argument that the proxy preserves what the theorem uses, and the paper does not give one. **If you find this argument made (or refuted) in print, that citation belongs here.**
- **"No paradoxes" is bought with a sincerity assumption.** §11's claim that unrestricted cardinal voting has no paradoxes holds "when voters cast sincere, non-strategic votes" — he says so, and admits it is "rather trivial from a formal point of view," since unrestricted cardinal voting is just addition. [Gibbard's theorem](gibbard_satterthwaite_theorem.md) still applies to EV, and §8 concedes strategy "cannot be ruled out."
- **The Condorcet dismissal is asserted, not argued.** That an EV winner beating a [Condorcet winner](condorcet/README.md) "need cause no concern" is exactly the contested question — and it is the question STAR answers the other way (see below).
- **"Fineness of the scale is a pragmatic issue" is the claim most exposed by later evidence.** [Delemazure et al. (2026)](../scores_and_ranks/grading_as_a_rival_primitive.md) found grade distributions shift substantially with the scale voters are handed — and this library has a [worked case where granularity flips the winner](../scores_and_ranks/scale_granularity_flips_the_winner.md). The scale is doing substantive work, not merely pragmatic work. **Note the asymmetry, though:** that same result is aimed at Balinski & Laraki's *common language of grades*, and it barely scratches Hillinger's move 3 — he never claimed the numbers carry absolute shared meaning. The finding spares his comparability argument and undercuts his scale-choice argument. Precision about which claim is hit matters here.

### Where he cuts against STAR

Fairness runs both ways, so this gets its own section rather than a footnote further down. The temptation with a source who is 80% on your side is to quote the 80% and bury the rest; a page that did that would be advocacy wearing a claim-check's clothes. Hillinger is a **cardinal ally who would delete STAR's second half**, and that is the most interesting thing about him:

- **His rule is the sum, full stop.** EV elects whoever maximizes the score total — [Score voting](../../06_Other/Range/concepts/range_voting.md). STAR's [automatic runoff](../../01_STAR/01_Learn/the_count/STAR_Automatic_Runoff.md) deliberately re-imposes a majoritarian check on that sum, which is precisely the correction Hillinger says is unnecessary.
- **He would use three levels, not six.** EV-3 `(−1, 0, +1)` for general elections; EV-5 for expert committees. STAR's 0–5 sits inside his own stated 5–6 limit on meaningful discrimination, so this is a mild disagreement — but it is a disagreement.
- **He wants a negative pole.** STAR's 0 is a floor, not an "against." His `−1` lets a voter vote *against* a candidate, and he considers the expressive value of that a strong argument.
- **But on runoffs he is closer to STAR than to pure Score.** §13 is easy to miss: he explicitly favours runoff elections under EV — *"I would recommend though that the scales of the primary election be retained."* His reason is informational, not majoritarian (voters are ill-informed; a runoff lets two finalists position themselves and gives voters time to learn). Same instinct as STAR — one round to narrow, one to decide — reached by a different argument and implemented as a real second election with a scored ballot rather than an automatic pairwise count.

Note that the last bullet cuts against the tidy version of this section: **§13 complicates Hillinger's own position**, and a page arguing only "he'd delete the runoff" would be quoting him as selectively as one arguing only "he's on our side." He lands on *narrow, then decide* by a route that has nothing to do with majority rule — which is a more useful fact than either simplification.

**Lean disclosure:** Hillinger advocates evaluative/utilitarian voting and argues against plurality, Borda, approval, IRV and proportional representation. He is a useful source for *definitions and framing* and a partisan one for *verdicts* — including his verdict against STAR-style majoritarian correction. Fleming and Harsanyi are the underlying theory and are not advocating any ballot. Sen's measurability/comparability framework is neutral ground and the best place to stand when the argument gets heated.

**Provenance of the criticism above,** since a claim-check that doesn't disclose its own sourcing is doing the thing it exists to prevent. The sincerity assumption, the "rather trivial" concession and the §8 admission on strategy are **Hillinger's own words**. The scale-granularity objection rests on [published evidence](../scores_and_ranks/grading_as_a_rival_primitive.md) (Delemazure et al., 2026) and a [worked case](../scores_and_ranks/scale_granularity_flips_the_winner.md) in this repo. The sloppy axiom list is checkable on the page. **The Harsanyi-transfer objection is the library's own construction** and is flagged as such where it is made — treat it as an argument to test, not a result to cite.

## New terms this page introduces

Added to the [glossary](../GLOSSARY.md) alongside the definitions above.

| Term | One line |
|---|---|
| **Cardinal utility** | a utility scale unique up to positive affine transformation — order **and** the ordering of differences survive rescaling |
| **Ordinal utility** | unique up to any increasing transformation — order survives, nothing else does |
| **Affine invariance** | `u → au + b` with `a > 0`; the transformation class that defines a cardinal scale |
| **Measurability vs. comparability** | Sen's two axes — structure *within* a person's utilities vs. how much reads *across* people; summing needs both |
| **vNM utility** | von Neumann–Morgenstern utility: cardinal, but calibrated on risk attitude over lotteries, not on felt intensity |
| **Harsanyi's aggregation theorem** | vNM rationality + the veil of ignorance ⟹ the utilitarian (sum-maximizing) social welfare function |
| **Evaluative voting (EV)** / **utilitarian voting** | Hillinger's rule — score every candidate on a uniform unrestricted scale, largest sum wins; **EV-3** = `(−1, 0, +1)`, **EV-5** = `(−2 … +2)` |
| **Context-dependent vs. independent scale** | whether a candidate's value depends on who else is running; ranks are context dependent, which is why IIA fails |
| **Dichotomous / trichotomous / multichotomous preferences** | Brams & Fishburn's `K` — how many indifference classes a voter actually has (2 / 3 / 4+) |
| **Voting pathology** | Hillinger's preferred word for the "paradoxes" — they are defects of restricted ballots, not logical curiosities |

## Related

- [Scores vs. ranks](../scores_and_ranks/scores_vs_ranks.md) · [preference vs. support](../scores_and_ranks/preference_vs_support.md) — the same distinction at the ballot level, without the theory
- [Does Arrow apply to STAR?](arrow_theorem_and_star.md) — the ordinal restriction as an escape hatch, and its real bound
- [Grading as a rival primitive](../scores_and_ranks/grading_as_a_rival_primitive.md) — Balinski & Laraki's rival answer to comparability, and the 2026 experiment against it
- [Distortion](distortion.md) · [what makes a good winner?](what_makes_a_good_winner.md) — what the literature does *with* the cardinal premise
- [Simulate utilities, not ballots](simulate_utilities_not_ballots.md) — the same premise as a methodology rule
- [The equally weighted vote](../../01_STAR/01_Learn/properties_and_limits/equally_weighted_vote.md) · [one person, one vote](one_person_one_vote.md) — Hillinger's "equal power" argument, in the library's own words
- [Scale granularity can flip the winner](../scores_and_ranks/scale_granularity_flips_the_winner.md) — why "how many levels" is not merely pragmatic
- **The case:** [Hillinger's example, run](../../method_comparisons/hillinger_evaluative_voting/README.md)

**Sources.** Hillinger, C. (2004), *Voting and the Cardinal Aggregation of Judgments*, Munich Discussion Paper 2004-9 ([DOI](https://doi.org/10.5282/ubm/epub.353)) · Fleming, M. (1952), "A cardinal concept of welfare," *QJE* 66 · Harsanyi, J. (1955), "Cardinal welfare, individualistic ethics, and the interpersonal comparisons of utility," *JPE* 63, and (1977) *Rational Behavior and Bargaining Equilibrium* · von Neumann, J. & Morgenstern, O. (1944), *Theory of Games and Economic Behavior* · Sen, A. (1970), *Collective Choice and Social Welfare* · Robbins, L. (1932), *An Essay on the Nature and Significance of Economic Science* · Arrow, K. (1951), *Social Choice and Individual Values*.
