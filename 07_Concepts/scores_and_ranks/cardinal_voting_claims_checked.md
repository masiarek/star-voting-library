# electowiki's "Cardinal voting," claim-checked

*[electowiki](https://electowiki.org/wiki/Cardinal_voting)'s cardinal-voting article is the best short map of the score-ballot family anywhere — the taxonomy tables alone are worth the visit. It also contains **two outright logical errors** and one comparison that quietly reads two different studies off the same ruler. This page separates the three.*

**Level: 301 · for debaters** Companions: [scores vs. ranks](scores_vs_ranks.md) · [scale granularity can flip the winner](scale_granularity_flips_the_winner.md) · [what makes a good winner?](../topics/what_makes_a_good_winner.md) · [criteria at a glance](../topics/criteria_at_a_glance.md)

> **Source lean, disclosed** (house rule): electowiki is the election-reform community's own encyclopedia — excellent for *branded method mechanics* where Wikipedia is thin, [advocacy-adjacent for *verdicts*](../topics/how_to_learn_about_voting_methods.md). This article argues **for** cardinal methods, which is the same side this library is on. That is exactly why it's worth auditing: a source that flatters your conclusion is the one you check hardest.

---

## What it gets right

- **The "pure" vs. "semi-cardinal" split.** [Approval](../../04_Approval/01_Learn/approval_voting.md) and [Score](../../06_Other/Range/concepts/range_voting.md) are pure — each candidate's total depends only on the scores given to *that* candidate. [STAR](../../01_STAR/01_Learn/STAR_start_here.md) is not, because the runoff reintroduces a comparison between candidates. This is the cleanest one-line explanation of why Score and Approval satisfy the [favorite betrayal criterion](../../01_STAR/01_Learn/properties_and_limits/favorite_betrayal_voting_301.md) and **STAR does not**. Worth knowing — though note "semi-cardinal" is electowiki's own coinage, not standard vocabulary, so don't expect a political scientist to recognize it.
- **Scale invariance.** For sum, average, or median aggregation, 0–5 vs. 0–100 vs. −42–7 changes nothing; only the *psychology* of the voter changes. Correct.
- **Gradation is what matters, not range.** To carry strictly *more* information than a ranking, the number of score levels must exceed the number of candidates. Correct as stated — *n* levels are exactly enough to express any strict ranking of *n* candidates, so beating a ranking takes more than *n*. The practical consequence for this library: **STAR's 0–5 is six levels, so it can express any strict ranking of up to six candidates exactly**; from seven candidates on, some voters are forced into ties. That's the ceiling behind [scale granularity can flip the winner](scale_granularity_flips_the_winner.md).
- **The majority-criterion critique**, including the arithmetic — see the runnable case below.
- **Its own Criticism section**, which supplies the strongest rebuttal to the article's earlier IIA boast: if voters **normalize** (stretch their scores to fill the scale around whoever is running), then a candidate entering or leaving changes the ballots themselves, and nominal [IIA](../topics/arrow_theorem_and_star.md) compliance doesn't survive contact with real voters. This library flags the same caveat on [the spoiler effect](../topics/spoiler_effect.md) — score methods are spoilerproof *on an absolute scale*.

## Error 1 — monotonicity is not "stricter than" IIA

The article argues that increasing a candidate's score can only help them, calls that monotonicity, and then says it is a stricter requirement than [independence of irrelevant alternatives](../topics/arrow_theorem_and_star.md), so IIA "is satisfied as well."

**That implication is invalid.** Monotonicity and IIA are logically independent — neither entails the other. The counterexample is already in this repo: **the [Borda count](../../method_comparisons/dark_horse_borda/) is monotone and fails IIA spectacularly**, which is the whole dark-horse story. A method can also satisfy IIA and fail monotonicity; the article itself later cites **Ebert's method** as a cardinal rule that fails monotonicity, which contradicts its own reasoning two sections earlier.

The **conclusion** is fine — Score and Approval do satisfy both. The **reason** is different: in a pure cardinal method each candidate's total is computed from the scores given to that candidate alone. That single property (separability) yields monotonicity *and* IIA independently. Neither is derived from the other, and the derivation matters, because it tells you exactly where the guarantee stops: at [STAR's runoff](../../01_STAR/01_Learn/the_count/STAR_Automatic_Runoff.md), which compares two candidates and is therefore not separable.

## Error 2 — the Bayesian Regret sign is backwards

The article's own argument is that the [majority criterion](../topics/majority_criterion/) forces a polarizing majority favorite over a consensus candidate. It then concludes that satisfying the majority criterion "reduces incentive for compromise and lowers Bayesian Regret."

**Bayesian Regret is avoidable unhappiness — lower is better.** If the criterion blocks the consensus winner, it *raises* regret. The sentence contradicts the paragraph it closes; "lowers" should read "raises."

This isn't pedantry, because the sign is the entire utilitarian case for cardinal voting. Run the article's own scenario and the direction is unmistakable — see below.

## Error 3 — Bayesian Regret and VSE are not one ruler

The article states that Score voting has the lowest Bayesian Regret of any common single-winner method tested, notes parenthetically that STAR was never included in those studies, then reports that [VSE](../topics/what_makes_a_good_winner.md#measuring-it-empirically-vse-bayesian-regret) is "an inverse of Bayesian Regret" and that **STAR** scores highest on VSE.

Read literally, those say two different methods are best on the same scale. What's actually going on: **Bayesian Regret** is Warren Smith's simulation program (rangevoting.org) and **VSE** is [Jameson Quinn](../topics/in_memoriam_jameson_quinn.md)'s — different electorate models, different strategy models, different candidate-generation assumptions. VSE is a *normalized rescaling* of regret, not its inverse, and cross-study rankings are not comparable. Both programs are also run by cardinal-method advocates, which the article doesn't say.

This library's honest version: under VSE the ordering is consistently roughly **STAR ≳ Approval > RCV-IRV > Plurality** ([expert consensus and IRV](../topics/expert_consensus_and_irv.md)), stated as one simulation program's result rather than a fact about the world.

## Value judgments wearing lab coats

Two sentences deserve a flag, not a correction:

- Polarization is undesirable, therefore **"forcing the electorate towards a moderate candidate should be in the general good."** That's a normative claim stated as a finding — and "forcing" concedes rather more than the argument intends. This library treats the same question as genuinely contested: [does a better ballot end polarization?](../topics/does_better_voting_end_polarization.md)
- Score voting is **"unbiased relative to polarization if the gradation is sufficiently large."** No threshold is given, so the claim can't fail.

## The runnable part: the 51/49 electorate

The article's central argument against the majority criterion is a polarized electorate: 51% love one candidate and hate the other, 49% the reverse, and a third candidate everyone would be content with loses anyway under any majority-criterion method. It adds a specific arithmetic claim — that a Condorcet method *would* elect the consensus candidate, provided **4% or more of the majority** expresses no preference between their favorite and the consensus choice.

We built it and ran it. **The claim holds, and the threshold is tight.**

100 voters. **Alma** is the 51% bloc's champion, **Bruno** the 49% bloc's, **Celia** is nobody's favorite and everybody's good outcome — with **3 of Alma's 51** honestly rating Alma and Celia equally.

<!-- report:majority_vs_consensus_51_49 -->
```text
[Divergence from STAR]
  STAR                   = Celia
  Choose-One (Plurality) = Alma   (differs from STAR)
  RCV-IRV                = Alma   (differs from STAR)
  Note: 3 of 100 ballots (3%) had equal non-zero scores, so their ranks were
        decided by candidate priority order. The RCV-IRV result may be an
        artifact of score-to-rank tie-breaking rather than a deep
        difference.
  Note: Ranked Robin (RCV-RR) agrees with STAR, so RCV-IRV is the lone
        outlier — the classic center-squeeze signature.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: cases_tabulated/majority_vs_consensus_51_49_RCV-IRV_tabulated.txt

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 100 ballots.
Count × Alma,Bruno,Celia
   49 ×    0,    5,    4
   48 ×    5,    0,    4
    3 ×    5,    0,    5

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Celia         -- 403 -- First place
   Alma          -- 255 -- Second place
   Bruno         -- 245
 Celia and Alma advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Celia         -- 49 -- First place
   Alma          -- 48
   Equal Support --  3
 Celia wins.
   Runoff math:
     100  ballots cast
   −   3  Equal Support (no preference between the two finalists)
     ───
      97  voters with a preference  (majority = 49)
           Celia 49 (51%)  ·  Alma 48 (49%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Celia
```
<!-- /report -->
**Alma is max-scored by an outright majority**, so [Choose-One](../topics/plurality.md) and [RCV-IRV](../../06_Other/RCV_IRV/concepts/RCV-IRV-Hare.md) — both of which satisfy the majority criterion — elect Alma, IRV in the first round. **Score, STAR and [Ranked Robin](../../05_Ranked_Robin/01_Learn/why_ranked_robin.md) all elect Celia.**

Drop the indifferent voters from three to two and Alma–Celia becomes a **49–49 pairwise tie**, Celia is no longer the Condorcet winner, and Ranked Robin flips to Alma. So the crossover sits just above 2 voters in 100 — **above 3.92% of the 51-voter majority bloc**, which is what "4% or more of the majority" claims. Verified.

And Error 2 is visible in the same numbers: Celia's expressed support totals **403** against Alma's **255**. Electing Alma to honor the majority criterion forfeits 148 points of stated satisfaction. That's regret going **up**, not down.

→ Run it: [`majority_vs_consensus_51_49.yaml`](../../01_STAR/03_Criteria/majority_criterion/cases/majority_vs_consensus_51_49.yaml) · full report: [page](../../01_STAR/03_Criteria/majority_criterion/cases/cases_pages/majority_vs_consensus_51_49.md) · [`_tabulated`](../../01_STAR/03_Criteria/majority_criterion/cases/cases_tabulated/majority_vs_consensus_51_49_tabulated.txt)

## Keep it fair

The case above is the utilitarian argument at its strongest, and it should not be oversold. **Alma really is the sincere favorite of more than half the room**, and "a majority should be able to elect its choice" is a serious democratic principle, not a bug — it is why the majority criterion exists and why [May's theorem](../topics/mays_theorem.md) makes majority rule *provably* optimal at two candidates. What the case shows is the **price** of that principle in a three-way race, not a refutation of it. The article states the tradeoff honestly in the same paragraph where it gets the sign backwards; that's a copy-editing failure, not a bad-faith one.

Note also that this scenario is [constructed to be maximally polarized](../../method_comparisons/paradoxes_and_whoops/reading_these_fairly.md) — severity is high, frequency is a separate question, and real electorates that split 51/49 with a universally-liked third option are not the common case.

## The short version

Borrow the taxonomy, the pure/semi-cardinal distinction, the gradation rule, and the 51/49 argument. Don't repeat the monotonicity-implies-IIA reasoning, don't quote the Bayesian Regret sentence, and never put "Score has the lowest BR" and "STAR has the highest VSE" in the same breath as though they settled a ranking.

---

**See also:** [the majority criterion set](../../01_STAR/03_Criteria/majority_criterion/README.md) · [STAR's honest limits](../../01_STAR/01_Learn/properties_and_limits/STAR_honest_limits.md) · [criteria at a glance](../topics/criteria_at_a_glance.md) · [how to learn about voting methods](../topics/how_to_learn_about_voting_methods.md) — the source-tier policy this page applies

# file: cardinal_voting_claims_checked.md
