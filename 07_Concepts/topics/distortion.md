# Distortion — the formal price of a ranked ballot

*A 301 theory page. **Distortion** is how mainstream computational social choice formalized the question this library keeps circling: if a ballot records only **order** and never **degree**, how much is that costing you? The literature's answer is a ratio with theorems attached — and it cuts both ways. It openly adopts the **cardinal premise** (the ground truth is voter utility; a ranked ballot is explicitly modeled as **lossy compression** of it), which sounds like a slam-dunk for scored ballots — until you read the headline theorem: under the spatial assumption, the best purely ordinal rules land within **3×** of optimal, and 3 is **provably the best possible**. Rankings are lossy *and* the loss is capped at a small constant. Both halves are proved.*

**Level: 301 · deep dive** Builds on the [spatial model](spatial_voting_model.md) (201→301) and pairs with [VSE](what_makes_a_good_winner.md#measuring-it-empirically-vse-bayesian-regret) — the average-case cousin of this worst-case metric.

Companions: [Cardinal utility](cardinal_utility.md) — what the "utilities" assumed below actually *are*, and whether they can be added up · [What makes a good winner?](what_makes_a_good_winner.md) · [Simulate utilities, not ballots](simulate_utilities_not_ballots.md) — the same "utility is the ground truth" move, in code · [Scores vs. ranks](../scores_and_ranks/scores_vs_ranks.md) — the ballot-level distinction this measures · [Does Arrow apply to STAR?](arrow_theorem_and_star.md) — the *other* place the ordinal/cardinal line is load-bearing · [Grading as a rival primitive](../scores_and_ranks/grading_as_a_rival_primitive.md) — the assault on ordinal ballots from the economics side.

---

## What distortion measures

Assume — as social choice has since von Neumann and Morgenstern — that voters really do have **cardinal utilities**: numbers saying how good each candidate would be for them. A candidate's **social welfare** is the sum of those numbers (equivalently, in the metric setting, their **social cost** is the sum of distances to all voters, and the **optimal** candidate minimizes it — the utilitarian, least-total-unhappiness pick that [Tideman & Plassmann's center](what_makes_a_good_winner.md#a-theorists-best-the-candidate-at-the-center) and VSE's 100% mark both point at).

If we could see the utilities, picking a winner would be trivial arithmetic. We can't. A voting rule is handed only the **rankings** those utilities induce. So:

> **Distortion** of a rule = the *worst-case* ratio between the welfare of the best possible candidate and the welfare of the candidate the rule actually elects — over every possible electorate *and* every set of utilities consistent with the ballots the rule saw.

```
                            welfare of the BEST candidate
distortion(f)  =   max     ────────────────────────────────────
                 over all   welfare of the candidate f ELECTS
                 profiles
```

Distortion 1 = the rule always finds the welfare-maximizing winner. Distortion 3 = never worse than 3× optimal, even against an adversary placing voters as maliciously as the ballots allow. Distortion "unbounded" = there is no worst case; the rule can be arbitrarily bad.

**Read what that construction assumes, because it is the whole ranked-vs-rated argument made formal:** the rule is *penalized for only seeing rankings*. The survey's own framing — the loss is "due to having access to preferences of limited expressiveness, particularly ordinal rankings."

That premise sits at the center of mainstream computational social choice, not at its advocacy fringe — [Procaccia & Rosenschein (2006)](https://link.springer.com/chapter/10.1007/11888874_31) defined it, and it has fifteen-plus years of AAAI/IJCAI/FOCS results behind it. If you want a citation for *"academics increasingly treat utility as the thing elections are trying to find, and rankings as a compression of it,"* this is the one to reach for.

## Two models — and the model decides the verdict

This is the part most people quoting distortion get wrong, and it is the same discipline this library already imposes on simulation results ([never quote a rate without the model](../curriculum/CURRICULUM_301.md)). There are **two standard settings**, and they give wildly different answers.

**1. Normalized / unit-sum.** Each voter's utilities sum to 1, but are otherwise arbitrary. No structure: a voter may love one candidate and despise every other, or be nearly indifferent across the field. This is the **adversarial** model — the analogue of impartial culture on the [simulation ladder](election_simulation_models.md).

**2. Metric.** Voters and candidates are points in a metric space (an "ideological distance"), and cost = distance. Preferences are *consistent with a geometry*. This is the [spatial model](spatial_voting_model.md) taken literally — far more realistic, and far more constrained.

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

| Rule | Metric distortion | Source |
|---|---|---|
| **any Condorcet winner** (when one exists) | **≤ 3** | Anshelevich et al. 2015 |
| **any** deterministic rule reading only rankings | **≥ 3** (matching lower bound) | Anshelevich et al. 2015 |
| Plurality Matching | **= 3** — optimal, conjecture resolved | [Gkatzelis, Halpern & Shah 2020 (FOCS)](https://arxiv.org/abs/2004.07447) |
| Plurality Veto | **= 3** — same bound, far simpler rule | [Kizilkaya & Kempe 2022](https://arxiv.org/abs/2206.07098) |
| **Copeland** — i.e. [**Ranked Robin**](../../05_Ranked_Robin/01_Learn/ranked_robin.md) | **≤ 5** | Anshelevich et al. 2015 |
| Munagala & Wang's rule | 4.236 — first break below 5 | 2019 |
| Ranked Pairs | **Θ(√m)** — *not* constant | Goel et al. 2017; Kempe 2020 |
| **STV** (⇒ [**RCV-IRV**](../../06_Other/RCV_IRV/concepts/README.md) single-winner) | between Ω(√log m) and **O(log m)** — *not* constant | [Skowron & Elkind 2017](https://ojs.aaai.org/index.php/AAAI/article/view/10591) |
| Plurality, Borda | **2m − 1** (linear in the field) | Anshelevich et al. 2015 |
| k-approval, Veto | 2n − 1 (linear in the *electorate*) | Anshelevich et al. 2015 |
| approval-style input | **unbounded** | Pierczyński & Skowron 2019 |

Whether the 3 could actually be *attained* by a rule (Condorcet winners don't always exist) was open for years — the **optimal metric distortion conjecture** — until Gkatzelis, Halpern & Shah resolved it, and Kizilkaya & Kempe then found an almost embarrassingly simple optimal rule: **Plurality Veto** — give each candidate their first-place count as a score, then let voters in turn each decrement their *least* favorite remaining candidate; last one standing. Distortion exactly 3.

The survey states the moral bluntly, and it is a **counter** to the strong pro-score claim: as long as voters and candidates live in a metric space, *"it is always possible to choose a close-to-optimal alternative based only on the ordinal rankings of the agents, without even the need to know their actual locations in the space."*

## How is a bound of 3 even possible? The triangle inequality is smuggled-in cardinal information

A ranking hides **intensity** — it reports `A > B` identically whether the voter adores A and despises B or can barely tell them apart. In the unstructured model that really is fatal, per Model 1's table.

The metric assumption changes the game because **distances can't lie independently — they must satisfy the triangle inequality.** If a voter ranks `W > X`, they're at least as close to W as to X; and W and X can't be far from *each other* unless that voter is also far from X. Geometry converts ordinal counts into cardinal bounds: a majority saying "W over X" doesn't tell you *how much* better W is, but it caps *how much worse* W can possibly be. The intensity information the ballot dropped isn't recovered — it's **bounded** by the assumed shape of the space.

Here is the whole proof that a Condorcet winner W has social cost ≤ 3× any rival X. Let S be the majority of voters preferring W to X (so |S| ≥ n/2), and write cost(·) for the sum of distances to all n voters:

1. **Voters in S:** each has d(v, W) ≤ d(v, X) — that's just what their ballot says.
2. **W and X are near each other:** for any u ∈ S, d(W, X) ≤ d(u, W) + d(u, X) ≤ 2·d(u, X). Averaging over S (at least n/2 voters): d(W, X) ≤ 4·cost(X)/n.
3. **Voters outside S:** each has d(v, W) ≤ d(v, X) + d(W, X). Summing all n voters: cost(W) ≤ cost(X) + (n/2)·d(W, X) ≤ cost(X) + 2·cost(X) = **3·cost(X)**. ∎

Three lines, and every line is triangle inequality plus "a majority said so." That's the entire mechanism: **majority preference + geometry = a utility guarantee**, extracted from ballots that never mentioned utility.

## Why you can't do better than 3 — near-indifference is invisible

The matching lower bound is one picture. Two candidates, A and B, distance 1 apart on a line; half the voters sit exactly at B, the other half sit at the exact **midpoint** (and tie-break their ranking toward A):

```
A ●-----------○-----------● B
              ↑            ↑
         n/2 voters    n/2 voters
        (midpoint:      (at B:
         ½ from each)   0 from B, 1 from A)
```

The ballots are a perfect 50/50 split — `A>B` from the midpoint voters, `B>A` from B's — so a deterministic rule must pick someone, and by symmetry the adversary can arrange the geometry against whichever it picks. Say it picks A: cost(A) = (n/2)(½) + (n/2)(1) = 3n/4, while cost(B) = (n/2)(½) + 0 = n/4. Ratio: **exactly 3**.

Look where the loss lives: the midpoint voters are **essentially indifferent** — but a ranking has no way to say "barely." Their forced-strict `A>B` reads identically to B-voters' heartfelt `B>A`, and that is precisely the intensity information a scored ballot exists to carry ([preference vs. support](../scores_and_ranks/preference_vs_support.md)). The theory quantifies the score-ballot argument *and* caps it in the same breath: what rankings hide is real, it costs up to 3× in the worst case, and it can cost no more — because geometry won't let indifference hide anywhere worse. (Randomized rules dip just below 3 — random dictatorship already achieves 3 − 2/n, and recent work pushes the frontier toward ~2.7 — but nothing reaches 1; some price is information-theoretically forced.)

## What this says about the methods in this library

**Ranked Robin has a constant metric-distortion bound; RCV-IRV does not.** Copeland — which is exactly what [Ranked Robin](../../05_Ranked_Robin/01_Learn/ranked_robin.md) tabulates — stays within a factor of **5** of the welfare optimum no matter how many candidates run. STV/IRV's bound **grows with the field** (O(log m), with a super-constant floor, so it isn't an artifact of loose analysis). Elimination leaks: the [center squeeze](center_squeeze/) is *exactly* a distortion event — the low-cost central candidate discarded for lacking first choices. And Plurality's 2m − 1 prices first-choice-only as the *most* lossy compression of all.

That is a mainstream-academic argument for **Condorcet over instant runoff, on the same ballot** — from a literature with no stake in the American reform fight. It fits this library's standing preference for [singing the virtues rather than attacking RCV](../../05_Ranked_Robin/01_Learn/ranked_robin.md): the ballot is fine, the *count* is where the welfare goes.

**Condorcet-consistency is not what earns the 5.** Careful here. A Condorcet *winner*, when one exists, is within 3 — that's the lemma above. But a Condorcet-consistent *rule* must also do something sensible when no Condorcet winner exists, and that's where rules diverge: Copeland's bound runs through the **uncovered set** (it always elects from it), while Ranked Pairs is equally Condorcet-consistent and still lands at Θ(√m). "It's a Condorcet method, so it has low distortion" is a claim the literature does not support; don't make it.

**Approval-only input is unbounded.** A cardinal ballot with too few levels is not automatically better than a ranking — it is, in the metric setting, *worse than every ranked rule in the table*. This is the cleanest available refutation of "cardinal ⇒ more information ⇒ better outcomes" as a blanket claim, and it belongs in any honest STAR-vs-Approval discussion (see [how often STAR and Approval disagree](../../method_comparisons/star_vs_approval_divergence.md), where the same fragility shows up empirically as the cutoff problem).

Read all of it the repo's way ([severity × frequency](../../method_comparisons/paradoxes_and_whoops/reading_these_fairly.md)): these are **worst cases**. On realistic electorates every serious method sits far below its bound most of the time — which is what the average-case metric measures. Distortion is the guarantee; VSE is the expectation.

## Does STAR's runoff change the math? (Yes — it's where the lemma plugs in)

STAR isn't in the tables because its ballot is **cardinal** — the framework analyzes rules that see only rankings, so it doesn't directly score STAR at all. **No unconditional worst-case distortion number for STAR exists in this literature; don't quote one.** The nearest published relative is [*The Distortion of Approval Voting with Runoff*](https://www.ifaamas.org/Proceedings/aamas2023/pdfs/p1752.pdf) (Ebadian et al., AAMAS 2023) — same score-then-runoff shape, cruder ballot. **That's a real, citable open gap.** That paper now has a [runnable companion in this library](../../method_comparisons/valuable_condorcet_loser/), and its headline is the *unit-sum mirror image* of the metric insurance worked below: there, adding a majority runoff makes approval voting's distortion **worse** — Θ(m) → Θ(m²) — because a majority check structurally blocks the *valuable Condorcet loser*, the beloved-of-a-minority candidate with the highest welfare in the race (their Example 5.1, counted on nine ballots in the companion). Majority runoff = liability in the unit-sum model, insurance in the metric one; both are theorems, and the model decides.

What *can* be said rigorously is conditional, and the machinery maps onto STAR's two rounds surprisingly cleanly:

- **The runoff is pairwise majority — the exact fact the three-line proof feeds on.** STAR's [automatic runoff](../../01_STAR/01_Learn/the_count/STAR_Automatic_Runoff.md) elects whichever finalist a majority prefers, so the winner W pairwise-beats the runner-up X, and the proof applies: **cost(W) ≤ 3·cost(X)**. The runoff is a built-in distortion clamp *between the finalists* — whatever the scoring round surfaced, the majority check guarantees the elected finalist isn't more than 3× costlier than the one it passed over. In distortion language, this is precisely the "utilitarian pick, then majority check" [hybrid design](../../01_STAR/01_Learn/the_count/STAR_hybrid_nature.md): the scoring round chases the low-cost candidate, the runoff bolts on the triangle-inequality insurance.
  - *One honest wrinkle:* step 2 of the proof needs |S| ≥ n/2 — a majority of **all** voters. STAR's runoff uses the [decided-voters](../../01_STAR/01_Learn/the_count/runoff_percentages.md) denominator, so with heavy [Equal Support](../GLOSSARY.md) the winner's preferring-set can be under half the electorate, and the constant degrades accordingly. The clamp is real; it just isn't literally 3 in the equal-support-heavy corner.
- **When the Condorcet winner reaches the runoff, STAR elects them** (a Condorcet winner beats *any* opponent head-to-head, including the other finalist) — and then inherits the full ≤ 3-versus-everyone guarantee. Since STAR elects the Condorcet winner in the overwhelming majority of simulated and real profiles, the ≤ 3 clamp is the *typical* regime, not a corner case.
- **What the runoff can't fix: a finalist round the optimum never reached.** If the utility-optimal candidate misses the top two, no majority check can recover them. And the scoring round's worst-case behavior **isn't covered by this theory at all**, because how a voter maps distances onto 0–5 scores is a modeling step outside the ordinal framework ([the same step that drives every simulation's results](simulate_utilities_not_ballots.md)). With honest, well-calibrated scores the scoring round is *hunting the utilitarian optimum directly* — better than any ordinal rule can promise; with adversarial or badly quantized scores it can miss. So the theory gives STAR a conditional guarantee and hands the rest to average-case evidence, which is [VSE's department](what_makes_a_good_winner.md#measuring-it-empirically-vse-bayesian-regret) — where STAR's scoring round is exactly why it tops the charts.

## The strongest result for the pro-score case

If you take one row out of the whole literature, take this one. Amanatidis, Birmpas, Filos-Ratsikas & Voudouris studied rules that read rankings **plus a few numeric queries** — "on a scale, how good is this one?" — asked of each voter:

| Cardinal information per voter | Unit-sum distortion |
|---|---|
| none (rankings only) | Θ(m²) |
| **one query** | **O(m)** |
| O(log m) queries | O(√m) — matches the best *randomized* ordinal rule |
| O(log² m) queries | **constant** |

And — the part that matters most — these bounds **hold without any normalization assumptions**.

That is the precise, defensible form of "scores are more powerful expression." Not *"cardinal ballots are better"* (Approval's unbounded row kills that), and not *"rankings are hopeless"* (the metric factor of 3 kills that). The defensible claim is: **a small amount of intensity information buys a large, provable reduction in worst-case welfare loss — quadratic to constant.** A 0–5 score ballot is, in effect, six buckets of exactly that kind of information — the theory's own escape hatch from the 3× floor, built into the ballot.

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

## The fair reading, both directions

**Concede to the cardinal camp:** the ground truth in this entire literature is utility. Rankings are formally modeled as lossy compression of cardinal preferences — a premise at the center of mainstream computational social choice, not a fringe scored-ballot talking point. Anyone claiming intensity is meaningless or unmeasurable is arguing against the field's own foundations. And the query results show that a *little* intensity buys a lot.

**Concede to the ordinal camp:** the loss is *bounded, small, and worst-case*. Distortion 3 for the best rules — and ≤ 3 for any Condorcet winner — means "rankings are lossy" cannot be inflated into "ranked methods are utility-blind." The [Condorcet ideal and the utilitarian ideal usually agree](what_makes_a_good_winner.md#the-deepest-split-majoritarian-vs-utilitarian); this theorem is the formal reason why: majority preference *geometrically implies* near-optimal total utility. A debater who says "only scored ballots can find the utilitarian winner" is overclaiming by exactly this theorem.

**Two more that cut against us**, because the [reading-these-fairly](../../method_comparisons/paradoxes_and_whoops/reading_these_fairly.md) rule applies to results we like:

- **Truthful mechanisms are essentially ordinal.** Bhaskar, Dani & Ghosh (2018), and earlier Filos-Ratsikas et al. (2014) in matching: the best *strategyproof* mechanisms are ordinal, and asymptotically as good as the best ordinal non-truthful ones. Once you demand honesty-compatibility, cardinal input stops paying. This is the distortion literature independently rediscovering the objection every score-voting critic raises: **the extra information isn't stable under strategy.**
- **Ballots aren't utilities.** Every voter min-max normalizes onto 0–5. That rendering step is itself a distortion the theory usually assumes away, and it is the same crux as the [approval cutoff](../../01_STAR/05_Practice/ex13_draw_the_line.md).

**And the load-bearing assumption, disclosed:** the 3 depends on the **metric** premise — the [spatial model](spatial_voting_model.md) with its triangle inequality. That model explains most real voting behavior, but it is a lens, not reality: drop it and ordinal distortion blows up with the field size. So the honest one-sentence summary is: **to the extent electorates are spatial, rankings lose at most a small constant; the case for scored ballots then rests on average-case performance (VSE), expressiveness, and strategy resistance — not on a worst-case rescue.** That's a *narrower* claim than either camp's slogan, which is usually the sign you've got it right.

## Using it in an argument

Say this:

> Modern social choice treats voter utility as the thing an election is trying to find, and a ranked ballot as a compressed encoding of it — that's what "distortion" measures. In the adversarial model, no deterministic ranked rule beats quadratic loss. In the realistic metric model, good ranked rules get within a factor of 3–5, so rankings are not hopeless. But asking voters for even a little intensity provably collapses the worst case from quadratic to constant. That's the real case for score ballots — a bounded, proven improvement, not a claim that rankings don't work.

Don't say *"academics have shown scores are better"* — Approval's unbounded distortion and the ordinal-truthfulness results are both sitting right there, and a reader who knows the literature will produce them.

## Sources

**Academic — the right tier for theorems.**

- Anshelevich, Filos-Ratsikas, Shah & Voudouris, [*Distortion in Social Choice Problems: The First 15 Years and Beyond*](https://www.ijcai.org/proceedings/2021/0589.pdf) (IJCAI 2021 survey; [arXiv:2103.00911](https://arxiv.org/abs/2103.00911)) — the single best entry point; every bound quoted above is in it.
- Procaccia & Rosenschein, [*The Distortion of Cardinal Preferences in Voting*](https://link.springer.com/chapter/10.1007/11888874_31) (CIA 2006) — the founding paper.
- Boutilier, Caragiannis, Haber, Lu, Procaccia & Sheffet, *Optimal Social Choice Functions: A Utilitarian View* (AIJ 2015) — the unit-sum randomized bounds.
- Anshelevich, Bhardwaj, Elkind, Postl & Skowron, [*Approximating Optimal Social Choice under Metric Preferences*](https://www.cs.rpi.edu/~eanshel/papers/distortionFull.pdf) (AIJ 2018; [arXiv:1512.07590](https://arxiv.org/abs/1512.07590)) — Copeland ≤ 5, the ≤ 3 Condorcet lemma, the ≥ 3 lower bound, the scoring rules.
- Skowron & Elkind, [*Social Choice under Metric Preferences: Scoring Rules and STV*](https://ojs.aaai.org/index.php/AAAI/article/view/10591) (AAAI 2017; [arXiv:1611.08549](https://arxiv.org/abs/1611.08549)) — STV's O(log m).
- Gkatzelis, Halpern & Shah, [*Resolving the Optimal Metric Distortion Conjecture*](https://arxiv.org/abs/2004.07447) (FOCS 2020) — distortion 3, achieved.
- Kizilkaya & Kempe, [*Plurality Veto: A Simple Voting Rule Achieving Optimal Metric Distortion*](https://arxiv.org/abs/2206.07098) (IJCAI 2022).
- Amanatidis, Birmpas, Filos-Ratsikas & Voudouris, [*Peeking Behind the Ordinal Curtain: Improving Distortion via Cardinal Queries*](https://arxiv.org/abs/1907.08165) (AIJ 2021) — the query results.
- Ebadian et al., [*The Distortion of Approval Voting with Runoff*](https://www.ifaamas.org/Proceedings/aamas2023/pdfs/p1752.pdf) (AAMAS 2023) — the closest published analogue to STAR's shape; runnable companion: [the valuable Condorcet loser, counted](../../method_comparisons/valuable_condorcet_loser/).

**Lean disclosure:** this is peer-reviewed CS/economics with no stake in the US reform fight — the most neutral tier available on this question, and unusually so for voting-method material. Its blind spot is the opposite of advocacy's: it optimizes worst cases over models chosen for tractability, and says nothing about ballot usability, spoilage, or whether voters can actually fill the thing in.

## See also

- [The spatial model](spatial_voting_model.md) — the geometry this whole theory runs on
- [What makes a good winner?](what_makes_a_good_winner.md) — the utilitarian ideal, Tideman & Plassmann's center, and VSE · [What makes a voting *method* good?](what_makes_a_voting_method_good.md)
- [Preference vs. support](../scores_and_ranks/preference_vs_support.md) — the intensity information rankings drop, on countable ballots
- [Grading as a rival primitive](../scores_and_ranks/grading_as_a_rival_primitive.md) — the *other* academic assault on ordinal ballots, from Balinski & Laraki
- [Election simulation models](election_simulation_models.md) · [Simulate utilities, not ballots](simulate_utilities_not_ballots.md)
- [Ranked Robin](../../05_Ranked_Robin/01_Learn/ranked_robin.md) · [The ranked-ballot method zoo](ranked_ballot_methods_zoo.md) · [Scoring methods vs. ranked voting](scoring-methods-vs-ranked-voting.md)
- [Reading these fairly](../../method_comparisons/paradoxes_and_whoops/reading_these_fairly.md)
