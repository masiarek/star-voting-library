# Voting 301 — proportional, criteria, debate theory

*Audience: skeptics, academics, RCV advocates, deep self-study. Concede limits honestly — that candor is the credibility.*

**Prereq:** [Voting 101](CURRICULUM_101.md) + [201](CURRICULUM_201.md). · Up: [Curriculum hub](../CURRICULUM.md).

---

## 301.1 — Proportional STAR (and STV)

- **Objective:** give a cohesive minority the representation it earned.
- **Key terms:** proportional representation, Droop quota, Allocated Score, Sequentially Spent Score (SSS), Reweighted Range Voting (RRV), STV.
- **See it:** the proportional trio in [`03_STAR_PR/`](../../03_STAR_PR/) — [allocated](../../03_STAR_PR/_main/cases/cases_pages/02a_c5_b63_proportional-allocated-score.md) / [SSS](../../03_STAR_PR/_main/cases/cases_pages/02b_c5_b63_proportional-sss.md) / [RRV](../../03_STAR_PR/_main/cases/cases_pages/02c_c5_b63_proportional-rrv.md), and [STV vs STAR-PR](../proportional_representation/stv/proportional_stv_vs_star.md) on the same electorate. Contrast with [Bloc STAR](../../02_STAR_Bloc/). Exercises: [Two seats, one neighborhood (ex12)](../../01_STAR/exercises/ex12_bloc_vs_proportional.md) — the Bloc sweep vs the Allocated share on ten ballots — and [The transfer machine (ex14)](../../01_STAR/exercises/ex14_transfer_machine.md) — STV's quota and transfers by hand.
- **The point:** STV is the proportional multi-winner *cousin of IRV*, not IRV; proportional methods seat coalitions in proportion, while Bloc STAR lets a majority sweep.
- **Deeper math:** [the math behind proportional STAR](../proportional_representation/STAR_PR/the_math_behind_proportional_star.md) — quotas, D'Hondt reweighting, JR/EJR, fair division.
- **ABC rules & the utilitarian–egalitarian spectrum:** [ABC rules](../Approval_Voting/Multiwinner_Approval/abc_rules_spectrum.md) — the approval-committee formalism (AV / PAV / Chamberlin–Courant / Phragmén) and the shadow-STAR bridge (Bloc STAR = AV, RRV = PAV), verified with `abcvoting`.
- **Thiele methods:** [Thiele methods](../Approval_Voting/Multiwinner_Approval/thiele_methods.md) — AV/PAV/CC as one parameterised family; **RRV is the score-ballot cousin of seq-PAV**, while Allocated Score / SSS follow the STV lineage.

## 301.2 — Favorite betrayal: does *only* "RCV" avoid it?

- **Key terms:** Favorite-Betrayal Criterion, Later-No-Harm, center squeeze, the incompatibility theorem.
- **Material:** [favorite betrayal (301)](../STAR_Voting/properties_and_limits/favorite_betrayal_voting_301.md). Companion exercise: [Later-no-harm, both readings (ex10)](../../01_STAR/exercises/ex10_later_no_harm.md) — the criterion IRV keeps and STAR trades, live in one election.
- **The point:** neither STAR nor RCV-IRV is FBC-proof; RCV-IRV fails it structurally ([Alaska '22](../../method_comparisons/alaska_2022/alaska_301.md)), STAR only in lab constructions.

## 301.3 — "Are equal-score votes discounted?"

- **Key terms:** Equal Support / No Preference, exhausted vs no-preference.
- **Material:** [Aren't equal-score votes discounted?](../STAR_Voting/reference/are_equal_score_votes_discounted.md); demo [equal_support_runoff_demo](../../01_STAR/_main/cases/cases_pages/equal_support_runoff_demo.md); drill: [The vanishing votes (ex07)](../../01_STAR/exercises/ex07_vanishing_votes.md).
- **In the result display:** [Two Denominators, One Winner](../STAR_Voting/the_count/runoff_percentages.md) shows exactly where Equal Support lands — counted in full in the score round, then set aside to form the "voters with a preference" denominator.

## 301.4 — The honest limits & theory

- **Key terms:** Gibbard / Gibbard–Satterthwaite, strategy resistance vs proofness, Condorcet efficiency, Test of Balance.
- **Material:** [STAR's honest limits](../STAR_Voting/properties_and_limits/STAR_honest_limits.md); "resistant, not proof." Worked gamble: [Bullet voting backfires (ex06)](../../01_STAR/exercises/ex06_bullet_backfire.md).
- **The Equal Vote / Test of Balance:** [The Equally Weighted Vote](../STAR_Voting/properties_and_limits/equally_weighted_vote.md) (why STAR passes) and [RCV-IRV Fails the Equal Vote Criterion](../RCV_IRV/RCV_IRV_equal_vote.md) (why RCV-IRV fails — stated fairly, with the honest caveats).
- **Deeper math:** [the math behind Condorcet](../RCV_Ranked_Robin/the_math_behind_condorcet.md) (tournaments, Smith/Schwartz, Arrow & Gibbard–Satterthwaite).
- **The generalized Condorcet winner:** [The Smith set — the smallest club that beats everyone outside it](../topics/smith_set.md) — when a cycle erases the Condorcet winner, the smallest set that beats everyone outside it is the principled "still in contention" list; the Smith-efficiency scorecard (Ranked Robin ✅, Minimax ❌, STAR ❌ by design), the Smith//X constructions, and ISDA — worked on a runnable 4-candidate cycle ([`04_smith_set_c4_b7`](../../05_Ranked_Robin/condorcet_vs_ranked_robin/cases/cases_pages/04_smith_set_c4_b7.md)).

## 301.5 — The vote-splitting formula (blocs)

- **Objective:** confirm a spoiler in numbers for a declared bloc.
- **Material:** the `blocs:` field + `[Vote-splitting check]` (see the engine); [the split-voting set](../../method_comparisons/split_voting/).

## 301.6 — When Condorcet, Score, and Runoff disagree (and how often)

- **Objective:** "Winner" isn't one thing — three reasonable definitions can name three different candidates; STAR targets the runoff winner *by design* (it is not a Condorcet method).
- **Material:** [three winner notions](../STAR_Voting/properties_and_limits/STAR_three_winner_notions.md); builds on the 101.4 Runoff Reversal lesson ([`01_STAR/runoff_overturns_leader/`](../../01_STAR/runoff_overturns_leader/)). Exercises: [Lillehammer 1994 (ex04)](../../01_STAR/exercises/ex04_olympics_1994.md) — Score vs STAR on real Olympic ballots — and the construction capstone [Build your own reversal (ex08)](../../01_STAR/exercises/ex08_build_a_reversal.md).
- **Frequency:** [`06_Other/simulations/`](../../06_Other/simulations/) measures how often score and runoff diverge — and shows the rate swings with the model, the electorate size, and the tie rule. **Lesson: never quote a rate without the model + size + tie split.**
- **Ranked Robin vs. Condorcet:** [Ranked Robin vs. Condorcet](../RCV_Ranked_Robin/ranked_robin_vs_condorcet.md) — why a cycle leaves "the Condorcet winner" blank while Ranked Robin still elects one.
- **Which Condorcet rule, though?** For three candidates, mostly a non-question: [the famous Condorcet methods collapse into one](../topics/condorcet/three_candidate_collapse.md) (maximin = Ranked Pairs = Schulze = Kemeny = Dodgson = Young), and the one *best-justified* against the variable-electorate paradoxes is the maximin family — [Brandt, Dong & Peters (2024)](../topics/condorcet/three_candidate_maximin.md).

## 301.7 — "Exhausted ballots": what FairVote's word hides

- **Objective:** untangle the overloaded RCV-IRV term — separate the fair, voter-side cases from the method-caused ones a fully and correctly ranked ballot still suffers.
- **Key terms:** ballot exhaustion, inactive ballot, ranking limit, majority-of-remaining-ballots, forced vs voluntary exhaustion.
- **Material:** [exhausted ballots](../RCV_IRV/RCV_IRV_exhausted_ballots.md) · [forced vs voluntary exhaustion](../RCV_IRV/forced_vs_voluntary_exhaustion.md); contrast [are equal-score votes discounted?](../STAR_Voting/reference/are_equal_score_votes_discounted.md).
- **The point:** exhaustion is **IRV**-specific (Ranked Robin reads every rank); STAR counts every ballot in both rounds, so nothing exhausts.

## 301.8 — Scale granularity can flip the winner

- **Objective:** a score scale's *resolution* (0–5 vs 0–9…) is a modeling choice; when the top contenders are bunched, compressing the scale can move a **finalist** and flip the **STAR** winner — even though rescaling never reorders any voter's own preferences.
- **Key terms:** score resolution / granularity, finalist selection, near-tie, quantization.
- **Material:** [Scale granularity can flip the winner](../scores_and_ranks/scale_granularity_flips_the_winner.md); case [`rrv_sample_c15_b13_three-parties`](../../03_STAR_PR/_main/cases/rrv_sample_c15_b13_three-parties.yaml) (0–5 → Orange5, 0–9 → Orange1).
- **Companion — "unorthodox STAR":** [Running STAR on a scale wider than 0–5](../STAR_Voting/properties_and_limits/STAR_nonstandard_scale.md) — the 0–5 range is a *convention*, not a rule; which round the scale touches (finalists, never the runoff), the honest tradeoff, and how to make LH tabulate a 0–10 STAR election (`maximum_score=N`).
- **The point:** a *fragile, mapping-dependent* divergence — present both counts, never quote one.

## 301.9 — How the simulations are built (VSE's foundation)

- **Objective:** understand the models that generate synthetic electorates for [VSE / Bayesian-Regret](../topics/what_makes_a_good_winner.md#measuring-it-empirically-vse-bayesian-regret) studies — and why every simulation result is conditional on the model.
- **Key terms:** Impartial Culture (IC) / Impartial Anonymous Culture (IAC), spatial model, Euclidean distance, Mallows (Kendall-Tau, φ), Plackett-Luce, Pólya urn, Yee diagram.
- **Page:** [Election simulation models](../topics/election_simulation_models.md) — the neutral menu, the math prerequisites, and the standing caveat. **Prerequisite:** [Simulate utilities, not ballots](../topics/simulate_utilities_not_ballots.md) — the methodology point that you sample *preferences* and derive ballots, never sample random ballots directly (and why `[0,1]` utilities beat random `{0..5}` scores).
- **The point:** pairs with 301.6's habit — *never quote a rate without the model* — and with 201.6's VSE overview.
- **A worked frequency study:** [How often do STAR and Approval disagree?](../../method_comparisons/star_vs_approval_divergence.md) — a seeded, self-testing simulation (~12% at 3 candidates / ~25% at 5, realistic model) that makes the "no single number" lesson concrete: divergence depends on the electorate model *and* the approval cutoff, because Approval has no canonical sincere ballot. The cutoff's outcome-power as a paper drill: [Where do you draw the line? (ex13)](../../01_STAR/exercises/ex13_draw_the_line.md) — one electorate, three thresholds, three Approval winners.

## 301.10 — The ranked-ballot method zoo (many tabulations of one ballot)

- **Objective:** a *single* ranked ballot supports a dozen-plus tabulations that pick different winners — the definitive proof that "RCV" names a ballot, not a method — and locate the repo's engines (Hare = IRV, Copeland = Ranked Robin) inside the wider field.
- **Page:** [The ranked-ballot method zoo](../topics/ranked_ballot_methods_zoo.md) — grouped by family, an at-a-glance criterion table, and a live calculator sandbox.
- **The point:** the catalog, not the verdict — *which* properties matter is 201.6's question.

## 301.11 — Reading advocacy claims: a claim-check, worked

- **Objective:** practice checking a voting-method claim against a countable election — quote it verbatim, build the smallest electorate that tests it, tabulate.
- **Material:** [FairVote's Condorcet article, claim-checked](../topics/condorcet/fairvote_condorcet_claim_check.md); the steelman companion [Edelman's "Myth of the Condorcet Winner," tabulated](../topics/condorcet/edelman_condorcet_myth.md).
- **The point:** steelman first — the "hated least ≠ liked most" point is *true* (the cardinal critique, which cuts against IRV too). The habit generalizes to pro-STAR literature; see [STAR's honest limits](../STAR_Voting/properties_and_limits/STAR_honest_limits.md).

## 301.12 — Participation: can showing up ever hurt you?

- **Objective:** the Participation criterion and the no-show / Twin paradoxes — "vote, it can only help your side" is a promise some methods structurally can't make.
- **Material:** the [Participation topic hub](../topics/participation/) + the live pair [`method_comparisons/participation_no_show/`](../../method_comparisons/participation_no_show/); catalog: [no-show paradox](../voting_paradoxes/no_show.md); the rare STAR-side failure, as a predict-then-peek exercise: [The tenth ballot](../../01_STAR/exercises/ex02_tenth_ballot.md).
- **The point:** the honest scorecard — only pure summation (Score/Approval) and Choose-One are immune; STAR's runoff costs it the formal guarantee too, just far more rarely than IRV's elimination machinery. Frame per [reading these fairly](../../method_comparisons/paradoxes_and_whoops/reading_these_fairly.md).
- **The three-candidate twist:** Moulin's theorem (every Condorcet method fails no-show) needs ≥ 4 candidates. At *exactly three*, [Brandt, Dong & Peters (2024)](../topics/condorcet/three_candidate_maximin.md) prove there **is** a no-show-immune family — the refinements of maximin (leximin, Nanson), and *uniquely* so. A rare case where restricting the problem buys a clean escape.

## 301.13 — Consistency: winning every district ≠ winning the whole

- **Objective:** the consistency criterion (join-consistency / reinforcement) — if every district separately elects X, must the combined electorate? Point-summing rules must, by arithmetic; STAR (like RCV-IRV, top-two, and Condorcet methods) need not, because "who advances to the runoff" is not additive.
- **Key terms:** consistency / reinforcement, runoff pairing, precinct-summable (the contrast).
- **Material:** the predict-then-peek exercise [Two districts, one mayor](../../01_STAR/exercises/ex01_two_districts.md) (live on BetterVoting as BV2188–90); catalog: [the multiple-districts (reinforcement) paradox](../voting_paradoxes/multiple_districts.md), whose Felsenthal trio (BV2147–49) is the IRV-side sibling; contrast [STAR Is Summable](../STAR_Voting/properties_and_limits/STAR_summability.md) — the *tallies* add across precincts even though the *winner inference* doesn't.
- **Run it across every method:** [Reinforcement paradox — both halves pick Ada, the whole picks Cara](../../method_comparisons/reinforcement_paradox/README.md) — the same 9 voters counted five ways: Score/Approval/Plurality keep the promise (additive), Ranked Robin can't, and STAR's *scoring round* keeps it but the *runoff* breaks it (a live Runoff Reversal). The concrete instance of a theorem: [Brandt, Dong & Peters (2024)](../topics/condorcet/three_candidate_maximin.md) prove **every** Condorcet method must show this paradox once there are ≥ 8 voters.
- **The point:** "she carried both districts and still lost" is a headline risk, not a tabulation risk — no one tallies a citywide seat district-by-district. Carry the worked answer.

## 301.14 — Distortion: putting a number on what a ranking throws away

- **Objective:** meet the mainstream-academic formalization of this library's central question — if a ballot records order but never degree, what does that cost? — and learn to quote it without overclaiming in either direction.
- **Key terms:** distortion, social welfare, unit-sum (normalized) vs metric model, uncovered set, cardinal queries.
- **Page:** [Distortion](../topics/distortion.md) — the two models and why the model decides the verdict, the scoreboard (Copeland/**Ranked Robin** ≤ 5 constant · **STV/IRV** O(log m), *not* constant · Plurality & Borda linear in the field · approval-only input **unbounded**), and the result that most supports score ballots: rankings **plus a few numeric queries** collapse the worst case from Θ(m²) to *constant*.
- **The point:** distortion is [VSE](../topics/what_makes_a_good_winner.md)'s academic sibling — same premise (utility is the target, a ballot is a lossy channel), opposite instrument (proved worst case vs simulated average case). Useful when someone dismisses VSE as reform-movement math: the peer-reviewed literature made the identical modeling choice.
- **Keep it honest:** the metric bound is only **3**, so rankings are not hopeless; the best *strategyproof* mechanisms are essentially ordinal; and **no published distortion bound for STAR** exists that we could find — an open gap, not a result to cite. Frame per [reading these fairly](../../method_comparisons/paradoxes_and_whoops/reading_these_fairly.md).
- **How a bound of 3 is even possible** (same page, second half): the three-line Condorcet-winner ≤ 3 proof (triangle inequality + "a majority said so"), the midpoint-voters lower bound (near-indifference is the one thing a ranking cannot say), and where STAR's rounds sit: the **automatic runoff is pairwise majority, so the ≤ 3 lemma plugs straight in between the finalists** — a conditional guarantee, since the scoring round's worst case lies outside the ordinal theory entirely.

## 301.15 — Grading as a rival primitive (Balinski & Laraki)

- **Objective:** see the strongest academic argument that the **preference order is the wrong primitive** — not merely lossy — and learn why it is *not* an ally of score-summing.
- **Key terms:** common language of grades, majority grade (median), majority-gauge, strategy-proof in grading, absolute vs relative evaluation.
- **Page:** [Grading as a rival primitive](../scores_and_ranks/grading_as_a_rival_primitive.md); the case against, worked: [Majority Judgment's paradoxes](../voting_paradoxes/majority_judgment.md); the reading-list entry: [rated & score methods](../books/rated_and_score_methods.md).
- **The point:** *"preference = ordering"* is a **contested modeling choice with a serious academic rival**, not the neutral default — which is the citable backing for [preference vs. support](../scores_and_ranks/preference_vs_support.md) and for refusing to cede the word "preference" to ranked ballots.
- **Keep it honest:** Balinski & Laraki argue the **median over the sum**, so they cut against STAR's Scoring Round as much as against IRV; MJ fails the majority *and* Condorcet criteria by design; and a 2026 experiment (Delemazure, Brunetti, Baujard & Bouveret, N = 1955) **rejects** the common-language premise that the comparability argument rests on.

## 301.16 — The social welfare function (what Arrow's theorem is about)

- **Objective:** learn the type distinction that most impossibility debate skips — a rule that outputs a **ranking** (SWF) vs one that outputs a **winner** (SCF) — and stop both over- and under-applying Arrow.
- **Key terms:** social welfare function `f : L(A)ⁿ → R(A)`, social choice function, social preference order, weak vs strong Pareto, IIA, decisive coalition, Contagion / Splitting Lemma, welfarist social welfare.
- **Page:** [Social welfare function](../topics/social_welfare_function.md) — the two objects, both axioms stated at both levels, who actually fails Pareto, and the two senses of "social welfare."
- **The point:** **majority rule is both Paretian and IIA, and escapes Arrow only because it is not an SWF** — its output can cycle, so it isn't a ranking at all. That reframes Condorcet methods correctly: a completion like [Ranked Robin](../RCV_Ranked_Robin/) *is* an SWF, so Arrow applies in full, and the cycle-resolution rule is what costs it IIA. Patching the cycle doesn't buy an exemption.
- **Keep it honest:** Pareto **forbids, it does not require** — plurality is Paretian and still elects poorly; and **a dictatorship is Paretian**, which is exactly why Arrow's conclusion bites. Pairs with 301.4's Arrow/Gibbard framing and with [Does Arrow apply to STAR?](../topics/arrow_theorem_and_star.md) — that page's ordinal/cardinal escape is a claim about the SWF's *domain*, and this page supplies the type it escapes from.

## 301.17 — May's Theorem: why the hard part starts at three

- **Objective:** meet the **positive** result the impossibility theorems are measured against, and get the fairest available framing of Choose-One voting.
- **Key terms:** May's theorem, anonymity, neutrality, positive responsiveness, decisiveness, the two-alternative case.
- **Page:** [May's Theorem](../topics/mays_theorem.md) — the four conditions, what giving up each one buys you, and the hinge into Arrow.
- **The point:** with exactly two alternatives, majority rule is **provably the unique** reasonable rule — so **[FPTP](../topics/plurality.md) *is* majority rule at two candidates and cannot be improved on there.** Every spoiler, vote-split and wasted-vote pathology comes from running a two-candidate rule on three or more. That's a stronger and fairer critique than "FPTP is broken," and it reframes [two-party dominance](../topics/two_party_dominance.md) as the system being pushed back toward the only domain where it works.
- **Read as a pair with 301.16:** *majority rule is uniquely right for two alternatives (May), and cannot be coherently extended to three ([Condorcet's paradox](../topics/condorcet/), then [Arrow](../topics/arrow_theorem_and_star.md)).* Every method in this library is a proposal for what to do about that gap.
- **Keep it honest:** May's theorem says **nothing** about which multi-candidate method is better — its content evaporates at three. Citing it to defend a particular reform is overreach. Useful sibling fact: at two candidates STAR, RCV-IRV, Ranked Robin and Approval all collapse to majority rule.
- **Also new here:** the **[Duggan–Schwartz theorem](../topics/gibbard_satterthwaite_theorem.md#allowing-ties-does-not-escape-it-duggan-and-schwartz)** — allowing tied winners does *not* escape Gibbard–Satterthwaite. You cannot tiebreak your way out of manipulability.

## 301.18 — Ties are forced (the small impossibility theorem)

- **Objective:** stop treating ties as an engineering wart. Learn the theorem that makes them unavoidable, the arithmetic that says exactly *when*, and the four-way menu every real system has to pick from.
- **Key terms:** resolute / irresolute SCF, nonimposition, reverse Borda, Moulin's proposition, the `P₄` rotation profile, set extension principle.
- **Page:** [Ties Are Forced](../topics/ties/ties_are_forced.md) — the theorem, the witness profile (which this repo already runs), the four ways out and what each costs.
- **The point:** **anonymity + neutrality + Pareto are incompatible with always naming one winner** whenever the voter count `n` has a divisor `r` with `1 < r ≤ m` candidates (Moulin, 1983). Restated: *ties are forced exactly when the smallest prime factor of `n` is at most `m`* — so **every even electorate has a forced tie**, for any number of candidates. The design question was never "how do we avoid ties," it's "which axiom do we spend."
- **The repo payoff:** the three engines here have each already answered it differently — **LH** breaks ties by a pre-published lot order (spends **neutrality**), **BetterVoting** breaks them at **random** (spends **determinism**, which is why a random BV tie can't be frozen into an export), and **`pref_voting`** returns the whole tied **leader set** (spends decisiveness, and by [Duggan–Schwartz](../topics/gibbard_satterthwaite_theorem.md#allowing-ties-does-not-escape-it-duggan-and-schwartz) buys no strategyproofness for it). The [LH-vs-BV divergence](../RCV_Ranked_Robin/rr_tiebreak_lh_vs_bv.md) is three defensible answers to a forced choice, not a bug. And the "contrived" [tie probes](../topics/ties/why_contrived_tie_cases.md) turn out to be the theorem's own witness profile.
- **Keep it honest:** "forced" means *some* profile ties, **not** that ties are likely — exact ties stay astronomically rare in large electorates, and the theorem ranks no method above another (all are caught). It also costs only **resoluteness**, which has four known workarounds; do not cite it as though it were [Arrow](../topics/arrow_theorem_and_star.md). Note too that the proposition is stated for **ordinal** rules — what carries over to STAR's score ballot is the *symmetry argument*, not the proposition itself.
- **Read with 301.17:** May's **positive responsiveness** breaks every tie that isn't forced, which is why majority rule is resolute on an *odd* electorate and cannot be on an even one. The 50/50 split is this theorem's two-candidate face.

---

*Up: [Curriculum hub](../CURRICULUM.md) · Prev: [Voting 201](CURRICULUM_201.md) · Next: [Voting 401 — failure modes & the safety check](CURRICULUM_401.md).*
