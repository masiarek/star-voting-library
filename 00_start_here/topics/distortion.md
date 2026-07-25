# Distortion — putting a number on what a ranking throws away

*A 301 theory page. **Distortion** is how mainstream computational social choice formalized the question this library keeps circling: if a ballot records only **order** and never **degree**, how much is that costing you? The literature's answer is a ratio you can prove bounds on — and, unlike most of the ranked-vs-rated debate, it has actual theorems attached. It is also the honest place to check the strong version of the pro-score claim, because the results cut both ways.*

**Level: 301.** This page is the **umbrella**: both models, the cross-method scoreboard, and how to quote it. For the metric model in depth — the triangle-inequality proof of why the price is exactly 3× — go to **[Metric distortion](metric_distortion.md)**.

Companions: [What makes a good winner? (VSE)](what_makes_a_good_winner.md) — distortion's average-case, simulated sibling · [Simulate utilities, not ballots](simulate_utilities_not_ballots.md) — the same "utility is the ground truth" move, in code · [Scores vs. ranks](../scores_and_ranks/scores_vs_ranks.md) — the ballot-level distinction this measures · [Does Arrow apply to STAR?](arrow_theorem_and_star.md) — the *other* place the ordinal/cardinal line is load-bearing.

---

## The one idea

Assume — as social choice has since von Neumann and Morgenstern — that voters really do have **cardinal utilities**: numbers saying how good each candidate would be for them. The **social welfare** of a candidate is the sum of those numbers. If we could see the utilities, picking a winner would be trivial arithmetic: elect the candidate with the highest total.

We can't see them. Standard voting rules are handed only the **rankings** those utilities induce. So:

> **Distortion** of a rule = the *worst-case* ratio between the welfare of the best possible candidate and the welfare of the candidate the rule actually elects.

```
                            welfare of the BEST candidate
distortion(f)  =   max     ────────────────────────────────────
                 over all   welfare of the candidate f ELECTS
                 profiles
```

Distortion 1 = the rule always finds the welfare-maximizing winner. Distortion 3 = in the worst case it elects someone a third as good as it could have. Distortion "unbounded" = there is no worst case; the rule can be arbitrarily bad.

**Read what that construction assumes, because it is the whole ranked-vs-rated argument made formal:** the rule is *penalized for only seeing rankings*. The ground truth of the entire literature is cardinal utility; the ranking is explicitly modeled as **lossy compression** of it. The survey's own framing: the loss is "due to having access to preferences of limited expressiveness, particularly ordinal rankings."

That premise sits at the center of mainstream computational social choice, not at its advocacy fringe — [Procaccia & Rosenschein (2006)](https://link.springer.com/chapter/10.1007/11888874_31) defined it, and it has fifteen-plus years of AAAI/IJCAI/FOCS results behind it. If you want a citation for *"academics increasingly treat utility as the thing elections are trying to find, and rankings as a compression of it,"* this is the one to reach for.

## Two models — and the model decides the verdict

This is the part most people quoting distortion get wrong, and it is the same discipline this library already imposes on simulation results ([never quote a rate without the model](../curriculum/CURRICULUM_301.md)). There are **two standard settings**, and they give wildly different answers.

**1. Normalized / unit-sum.** Each voter's utilities sum to 1, but are otherwise arbitrary. No structure: a voter may love one candidate and despise every other, or be nearly indifferent across the field. This is the **adversarial** model — the analogue of impartial culture on the [simulation ladder](election_simulation_models.md).

**2. Metric.** Voters and candidates are points in a metric space (an "ideological distance"), and cost = distance. Preferences are *consistent with a geometry*. This is the analogue of the [spatial model](spatial_voting_model.md) — far more realistic, and far more constrained.

The unit-sum model says ordinal ballots are catastrophic. The metric model says they are pretty good. **Both are true statements about their models**, and any argument that quotes one without naming it is doing the thing this repo tells you not to do.

### Model 1 — unit-sum: rankings are catastrophic

| Result | Bound | Source |
|---|---|---|
| Borda | **unbounded** | Procaccia & Rosenschein 2006 |
| Plurality | **Θ(m²)** | Caragiannis & Procaccia 2011 |
| **every deterministic ordinal rule** | **Ω(m²)** — Plurality's bound is *optimal* | Caragiannis et al. 2017 |
| best randomized rule | O(√m · log\* m), with an Ω(√m) floor | Boutilier et al. 2015 |

Read the third row slowly. It is not "Plurality is bad." It is: **no deterministic rule reading only rankings can do better than quadratic-in-the-candidate-count loss.** Rearranging the ballots doesn't help; inventing a cleverer ranked method doesn't help. The loss is in the *information*, not the tabulation.

### Model 2 — metric: rankings are surprisingly cheap

*(Why 3 and not something worse — the triangle inequality doing the work the ballot can't — is worked out on [Metric distortion](metric_distortion.md). Here, just the scoreboard.)*

| Rule | Metric distortion | Source |
|---|---|---|
| **any** deterministic rule reading only rankings | **≥ 3** (tight lower bound) | Anshelevich et al. 2015 |
| Plurality Matching | **= 3** — optimal, conjecture resolved | [Gkatzelis, Halpern & Shah 2020 (FOCS)](https://arxiv.org/abs/2004.07447) |
| **Copeland** — i.e. [**Ranked Robin**](../RCV_Ranked_Robin/ranked_robin.md) | **≤ 5** | Anshelevich et al. 2015 |
| Munagala & Wang's rule | 4.236 — first break below 5 | 2019 |
| Ranked Pairs | **Θ(√m)** — *not* constant | Goel et al. 2017; Kempe 2020 |
| **STV** (⇒ [**RCV-IRV**](../RCV_IRV/README.md) single-winner) | between Ω(√log m) and **O(log m)** — *not* constant | [Skowron & Elkind 2017](https://ojs.aaai.org/index.php/AAAI/article/view/10591) |
| Plurality, Borda | **2m − 1** (linear in the field) | Anshelevich et al. 2015 |
| k-approval, Veto | 2n − 1 (linear in the *electorate*) | Anshelevich et al. 2015 |
| approval-style input | **unbounded** | Pierczyński & Skowron 2019 |

The survey states the moral bluntly, and it is a **counter** to the strong pro-score claim: as long as voters and candidates live in a metric space, *"it is always possible to choose a close-to-optimal alternative based only on the ordinal rankings of the agents, without even the need to know their actual locations in the space."*

So in the realistic model, **the price of ordinality is a factor of 3** — proven, tight, and not improvable by better cardinal ballots at the top end (distortion 1 needs the actual metric, which no ballot delivers). That's a real cost, and it is also a *bounded, modest* cost. Anyone claiming rankings are hopeless has to explain away this row.

## What this says about the methods in this library

Three findings here are directly usable, and one of them is a genuinely strong argument the repo hasn't been making:

**Ranked Robin has a constant metric-distortion bound; RCV-IRV does not.** Copeland — which is exactly what [Ranked Robin](../RCV_Ranked_Robin/ranked_robin.md) tabulates — is guaranteed within a factor of **5** of the welfare optimum no matter how many candidates run. STV/IRV's bound **grows with the field** (O(log m), with a super-constant floor, so it is not an artifact of loose analysis). Both crush Plurality and Borda, whose loss is *linear* in the number of candidates.

This is a mainstream-academic argument for **Condorcet over instant runoff, on the same ballot** — from a literature with no stake in the American reform fight. It fits this library's standing preference for [singing the virtues rather than attacking RCV](../RCV_Ranked_Robin/ranked_robin.md): the ballot is fine, the *count* is where the welfare goes.

**Condorcet-consistency is not what earns the 5.** Careful here — the bound runs through the **uncovered set** (Copeland always elects from it), *not* through the Condorcet criterion. Ranked Pairs is Condorcet-consistent and still lands at Θ(√m). "It's a Condorcet method, so it has low distortion" is a claim the literature does not support; don't make it.

**Approval-only input is unbounded.** A cardinal ballot with too few levels is not automatically better than a ranking — it is, in the metric setting, *worse than every ranked rule in the table*. This is the cleanest available refutation of "cardinal ⇒ more information ⇒ better outcomes" as a blanket claim, and it belongs in any honest STAR-vs-Approval discussion (see [how often STAR and Approval disagree](../../method_comparisons/star_vs_approval_divergence.md), where the same fragility shows up empirically as the cutoff problem).

**Where's STAR?** Honestly: **I could not find a published metric-distortion bound for STAR**, and you should not cite one until someone confirms it exists. STAR sits awkwardly in this framework — it reads scores (so it is not an ordinal rule, and the ≥ 3 lower bound doesn't automatically bind it), but its ballots are min-max normalized renderings rather than true utilities (so distortion 1 isn't free either). The nearest published relative is [*The Distortion of Approval Voting with Runoff*](https://www.ifaamas.org/Proceedings/aamas2023/pdfs/p1752.pdf) (Ebadian et al., AAMAS 2023) — same score-then-runoff shape, cruder ballot. **This is a real, citable open gap**, and a good candidate for the kind of runnable follow-up this library is for.

## The strongest result for the pro-score case

If you take one row out of the whole literature, take this one. Amanatidis, Birmpas, Filos-Ratsikas & Voudouris (2020) studied rules that read rankings **plus a few numeric queries** — "on a scale, how good is this one?" — asked of each voter:

| Cardinal information per voter | Unit-sum distortion |
|---|---|
| none (rankings only) | Θ(m²) |
| **one query** | **O(m)** |
| O(log m) queries | O(√m) — matches the best *randomized* ordinal rule |
| O(log² m) queries | **constant** |

And — the part that matters most — these bounds **hold without any normalization assumptions**.

That is the precise, defensible form of "scores are more powerful expression." Not *"cardinal ballots are better"* (Approval's unbounded row kills that), and not *"rankings are hopeless"* (the metric factor of 3 kills that). The defensible claim is: **a small amount of intensity information buys a large, provable reduction in worst-case welfare loss — quadratic to constant.** A 0–5 score ballot is, in this framing, roughly "a ranking plus a handful of queries."

## Where it cuts against

Fair is fair, and the [reading-these-fairly](../../method_comparisons/paradoxes_and_whoops/reading_these_fairly.md) rule applies to results we like too:

- **Truthful mechanisms are essentially ordinal.** Bhaskar, Dani & Ghosh (2018), and earlier Filos-Ratsikas et al. (2014) in matching: the best *strategyproof* mechanisms are ordinal, and asymptotically as good as the best ordinal non-truthful ones. Once you demand honesty-compatibility, cardinal input stops paying. This is the distortion literature independently rediscovering the objection every score-voting critic raises: **the extra information isn't stable under strategy.**
- **The metric bound is only 3.** In the model that actually resembles elections, ordinal rules are within a small constant of optimal. "Rankings destroy the information" is a unit-sum statement.
- **Distortion is worst-case.** A rule can have terrible distortion and excellent typical behavior — which is precisely why the reform world uses [VSE](what_makes_a_good_winner.md) instead. Worst-case bounds are the right tool for *"can this fail badly?"* and the wrong tool for *"how good is this usually?"*
- **Ballots aren't utilities.** Every voter min-max normalizes onto 0–5. That rendering step is itself a distortion the theory usually assumes away, and it is the same crux as the [approval cutoff](../../01_STAR/exercises/ex13_draw_the_line.md).

## Distortion vs. VSE — same question, opposite instruments

| | **Distortion** | **[VSE](what_makes_a_good_winner.md) / Bayesian Regret** |
|---|---|---|
| Case analyzed | **worst** case | **average** case |
| Method | proved (theorems, bounds) | simulated (thousands of elections) |
| Output | a ratio, often in *m* or *n* | a percentage, 0–100% |
| Optimum is | ratio 1 | 100% |
| Depends on | which model (unit-sum / metric) | which voter model + strategy mix |
| Home turf | academic CS/econ (AAAI, IJCAI, FOCS) | reform advocacy (advocacy-adjacent — [disclose it](how_to_learn_about_voting_methods.md)) |
| Weak spot | worst cases may be exotic | assumptions are contestable, not proved |

They are the same underlying commitment — *utility is the target, a ballot is a lossy channel* — measured from opposite ends. **That's the useful thing to know if someone dismisses VSE as reform-movement math:** the peer-reviewed literature made the identical modeling choice, and simply proved bounds instead of running simulations. VSE's *premise* is mainstream; only its *methodology* is advocacy-side.

## Using it in an argument

Say this:

> Modern social choice treats voter utility as the thing an election is trying to find, and a ranked ballot as a compressed encoding of it — that's what "distortion" measures. In the adversarial model, no deterministic ranked rule beats quadratic loss. In the realistic metric model, good ranked rules get within a factor of 3–5, so rankings are not hopeless. But asking voters for even a little intensity provably collapses the worst case from quadratic to constant. That's the real case for score ballots — a bounded, proven improvement, not a claim that rankings don't work.

Don't say *"academics have shown scores are better"* — Approval's unbounded distortion and the ordinal-truthfulness results are both sitting right there, and a reader who knows the literature will produce them.

## Sources

- Anshelevich, Filos-Ratsikas, Shah & Voudouris, [**Distortion in Social Choice Problems: The First 15 Years and Beyond**](https://www.ijcai.org/proceedings/2021/0589.pdf) (IJCAI-21 survey) — the single best entry point; every bound quoted above is in it.
- Procaccia & Rosenschein, [*The Distortion of Cardinal Preferences in Voting*](https://link.springer.com/chapter/10.1007/11888874_31) (2006) — the founding paper.
- Anshelevich, Bhardwaj & Postl, [*Approximating Optimal Social Choice under Metric Preferences*](https://www.cs.rpi.edu/~eanshel/papers/distortionFull.pdf) (2015 / AIJ 2018) — Copeland ≤ 5, the ≥ 3 lower bound, the scoring-rule results.
- Skowron & Elkind, [*Social Choice Under Metric Preferences: Scoring Rules and STV*](https://ojs.aaai.org/index.php/AAAI/article/view/10591) (AAAI 2017) — STV's O(log m).
- Gkatzelis, Halpern & Shah, [*Resolving the Optimal Metric Distortion Conjecture*](https://arxiv.org/abs/2004.07447) (FOCS 2020) — distortion 3, achieved.
- Ebadian et al., [*The Distortion of Approval Voting with Runoff*](https://www.ifaamas.org/Proceedings/aamas2023/pdfs/p1752.pdf) (AAMAS 2023) — the closest published analogue to STAR's shape.

**Lean disclosure:** this is peer-reviewed CS/economics with no stake in the US reform fight — the most neutral tier available on this question, and unusually so for voting-method material. Its blind spot is the opposite of advocacy's: it optimizes worst cases over models chosen for tractability, and says nothing about ballot usability, spoilage, or whether voters can actually fill the thing in.

## See also

- [Metric distortion](metric_distortion.md) — the metric model in depth, with the proof of the 3× bound
- [What makes a good winner?](what_makes_a_good_winner.md) · [What makes a voting *method* good?](what_makes_a_voting_method_good.md)
- [Preference vs. support](../scores_and_ranks/preference_vs_support.md) — the same loss, shown on two ballots instead of proved
- [Grading as a rival primitive](../scores_and_ranks/grading_as_a_rival_primitive.md) — the *other* academic assault on ordinal ballots, from Balinski & Laraki
- [Election simulation models](election_simulation_models.md) · [Simulate utilities, not ballots](simulate_utilities_not_ballots.md)
- [Ranked Robin](../RCV_Ranked_Robin/ranked_robin.md) · [The ranked-ballot method zoo](ranked_ballot_methods_zoo.md)
