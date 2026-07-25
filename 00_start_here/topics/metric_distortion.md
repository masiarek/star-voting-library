# Metric distortion — why the price of a ranked ballot is exactly 3×

*The deep-dive under the umbrella page **[Distortion](distortion.md)** (read that first — both models, the cross-method scoreboard, how to quote it). The umbrella's most surprising row says that under the spatial ("metric") assumption, the best purely ordinal rules elect a candidate whose social cost is at most **3×** optimal, and 3 is **provably the best possible**. This page explains how that's even possible — a three-line proof where the **triangle inequality does the work the ballot can't**, a one-picture lower bound showing the loss is exactly the near-indifference a ranking cannot express — and what the machinery does and doesn't say about STAR's two rounds.*

**Level: Voting 301** — builds on the [spatial model](spatial_voting_model.md) (201→301) and pairs with [VSE](what_makes_a_good_winner.md#measuring-it-empirically-vse-bayesian-regret) (the average-case cousin of this worst-case metric).

## What distortion measures

Put every voter and candidate at a point in a metric space — the [spatial model](spatial_voting_model.md), taken literally. A candidate's **social cost** is the sum of their distances to all voters; the **optimal** candidate minimizes it (the utilitarian, least-total-unhappiness pick — the same "best candidate" [Tideman & Plassmann's center](what_makes_a_good_winner.md#a-theorists-best-the-candidate-at-the-center) and VSE's 100% mark point at). A voting rule, though, never sees the distances — only the **rankings** they induce (closer = ranked higher). The rule's **distortion** is the worst-case ratio, over every possible electorate *and* every geometry consistent with the ballots it saw:

> distortion = max over instances of ( social cost of the rule's winner ÷ social cost of the optimal candidate ).

Distortion 1 would mean "always elects the utilitarian optimum." Distortion 3 means "never worse than 3× the optimum, even against an adversary who places the voters as maliciously as the ballots allow."

## The result that surprises everyone

- **Any Condorcet winner has distortion ≤ 3** (Anshelevich, Bhardwaj, Elkind, Postl & Skowron). Just winning every head-to-head, an ordinal fact, *geometrically forces* your social cost within 3× of anyone's — the proof is below.
- **No deterministic ordinal rule can beat 3** — a matching lower bound (also below), so 3 is the exact price of the ranking bottleneck, not a loose estimate.
- **The bound is achievable, unconditionally.** Whether 3 could actually be attained (Condorcet winners don't always exist) was open for years — the *optimal metric distortion conjecture* — until Gkatzelis, Halpern & Shah ([FOCS 2020](https://arxiv.org/abs/2004.07447)) resolved it with PluralityMatching, and Kizilkaya & Kempe ([2022](https://arxiv.org/abs/2206.07098)) found an almost embarrassingly simple optimal rule, **Plurality Veto**: give each candidate their first-place count as a score, then let voters (in some order) each decrement their *least* favorite remaining candidate; last one standing. Distortion exactly 3.

So "rankings are lossy compression" is true *and* the loss is capped at a small constant. Both halves of the sentence are theorems.

## How is that possible? The triangle inequality is the smuggled-in cardinal information

A ranking hides **intensity** — it reports `A > B` identically whether the voter adores A and despises B or can barely tell them apart. In an unstructured utility model that's fatal: with arbitrary (even normalized) utilities, deterministic ordinal rules have distortion that **grows unboundedly with the number of candidates** (Boutilier, Caragiannis, Haber, Lu, Procaccia & Sheffet 2015). If rankings were all you had *and utilities could be anything*, "lossy" really would mean "loses a lot."

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

Look where the loss lives: the midpoint voters are **essentially indifferent** — but a ranking has no way to say "barely." Their forced-strict `A>B` reads identically to B-voters' heartfelt `B>A`, and that's precisely the intensity information a scored ballot exists to carry ([preference vs. support](../scores_and_ranks/preference_vs_support.md)). The theory thus quantifies the score-ballot argument *and* caps it in the same breath: what rankings hide is real, it costs up to 3× in the worst case, and it can cost no more — because geometry won't let indifference hide anywhere worse. (Randomized rules can dip below 3 — random dictatorship already achieves just under 3, and recent work pushes the frontier toward ~2.7 — but nothing reaches 1; some price is information-theoretically forced.)

## The scoreboard lives on the umbrella

The 3 is a guarantee for the *best* rules, not for ordinal methods generally — Copeland/[Ranked Robin](../RCV_Ranked_Robin/ranked_robin.md) sits at ≤ 5, RCV-IRV/STV grows like log m (elimination leaks: the [center squeeze](center_squeeze/) is exactly a distortion event — the low-cost central candidate discarded for lacking first choices), and Plurality's 2m − 1 prices first-choice-only as the *most* lossy compression. The full cross-method table, with sources, is on **[the umbrella page](distortion.md#model-2-metric-rankings-are-surprisingly-cheap)** — one table, one place, no drift. Read any of it the repo's way ([severity × frequency](../../method_comparisons/paradoxes_and_whoops/reading_these_fairly.md)): these are **worst cases**; on realistic electorates every serious method sits far below its bound most of the time, which is what the average-case metric ([VSE](what_makes_a_good_winner.md#measuring-it-empirically-vse-bayesian-regret)) measures. Distortion is the guarantee; VSE is the expectation.

## Does STAR's runoff change the math? (Yes — it's where the lemma plugs in)

STAR isn't in the table above because its ballot is **cardinal** — the framework analyzes rules that see only rankings, so it doesn't directly score STAR at all. But the machinery maps onto STAR's two rounds surprisingly cleanly:

- **The runoff is pairwise majority — the exact fact the three-line proof feeds on.** STAR's [automatic runoff](../STAR_Voting/the_count/STAR_Automatic_Runoff.md) elects whichever finalist a majority prefers, so the winner W pairwise-beats the runner-up X — and step-by-step, the proof above applies verbatim: **cost(W) ≤ 3·cost(X)**. The runoff is a built-in distortion clamp *between the finalists*: whatever the scoring round surfaced, the majority check guarantees the elected finalist isn't more than 3× costlier than the one it passed over. In distortion language, this is precisely the "utilitarian pick, then majority check" [hybrid design](../STAR_Voting/the_count/STAR_hybrid_nature.md) — the scoring round chases the low-cost candidate, the runoff bolts on the triangle-inequality insurance.
- **When the Condorcet winner reaches the runoff, STAR elects them** (a Condorcet winner beats *any* opponent head-to-head, including the other finalist) — and then inherits the full ≤ 3-versus-everyone guarantee of the lemma. Since STAR elects the Condorcet winner in the overwhelming majority of simulated and real profiles, the ≤ 3 clamp is the *typical* regime, not a corner case.
- **What the runoff can't fix: a finalist round the optimum never reached.** The guarantee is conditional — the runoff only compares the two candidates the scoring round sent it. If the utility-optimal candidate misses the top two, no majority check can recover them. And here's the honest subtlety: the scoring round's worst-case behavior **isn't covered by this theory at all**, because how a voter maps distances onto 0–5 scores is a modeling step outside the ordinal framework ([the same step that drives every simulation's results](simulate_utilities_not_ballots.md)). With honest, well-calibrated scores the scoring round is *hunting the utilitarian optimum directly* — better than any ordinal rule can promise; with adversarial or badly quantized scores it can miss. So there is **no unconditional worst-case distortion number for STAR in this literature** — don't quote one. The theory gives STAR a conditional guarantee (runoff ≤ 3× the runner-up; full ≤ 3 whenever the Condorcet winner is a finalist) and hands the rest to average-case evidence, which is [VSE's department](what_makes_a_good_winner.md#measuring-it-empirically-vse-bayesian-regret) — where STAR's scoring round is exactly why it tops the charts.

One more twist from the same literature: distortion drops sharply if a rule may ask each voter just a **few cardinal questions** on top of the ranking (Amanatidis, Birmpas, Filos-Ratsikas & Voudouris). A 0–5 score ballot is, in effect, six buckets of exactly that kind of information — the theory's own escape hatch from the 3× floor, built into the ballot.

## What this does and doesn't prove (the fair reading, both directions)

**Concede to the cardinal camp:** the ground truth in this entire literature is utility. Rankings are formally modeled as lossy compression of cardinal preferences — a premise sitting at the center of mainstream computational social choice, not a fringe scored-ballot talking point. Anyone claiming intensity is meaningless or unmeasurable is arguing against the field's own foundations.

**Concede to the ordinal camp:** the loss is *bounded, small, and worst-case*. Distortion 3 for the best rules — and ≤ 3 for any Condorcet winner — means "rankings are lossy" cannot be inflated into "ranked methods are utility-blind." The [Condorcet ideal and the utilitarian ideal usually agree](what_makes_a_good_winner.md#the-deepest-split-majoritarian-vs-utilitarian); this theorem is the formal reason why: majority preference *geometrically implies* near-optimal total utility. A debater who says "only scored ballots can find the utilitarian winner" is overclaiming by exactly this theorem.

**And the load-bearing assumption, disclosed:** the 3 depends on the **metric** premise — the [spatial model](spatial_voting_model.md) with its triangle inequality. That model explains most real voting behavior (it's the "realistic" model VSE leans on), but it is a lens, not reality: drop it and ordinal distortion blows up with the field size (Boutilier et al.). So the honest one-sentence summary is: **to the extent electorates are spatial, rankings lose at most a small constant; the case for scored ballots then rests on average-case performance (VSE), expressiveness, and strategy resistance — not on a worst-case rescue.** That's a *narrower* claim than either camp's slogan, which is usually the sign you've got it right.

## Related

- [Distortion](distortion.md) — **the umbrella page**: both models (unit-sum vs. metric), the cross-method scoreboard, and how to quote it in an argument
- [The spatial model](spatial_voting_model.md) — the geometry this whole theory runs on
- [What makes a good winner?](what_makes_a_good_winner.md) — the utilitarian ideal, Tideman & Plassmann's center, and VSE (the average-case companion metric)
- [Preference vs. support](../scores_and_ranks/preference_vs_support.md) — the intensity information rankings drop, on countable ballots
- [Scoring methods vs. ranked voting](scoring-methods-vs-ranked-voting.md) · [Reading these fairly](../../method_comparisons/paradoxes_and_whoops/reading_these_fairly.md)

**Sources (academic — the right tier for theorems):** Procaccia & Rosenschein, *The Distortion of Cardinal Preferences in Voting* (CIA 2006) · Boutilier, Caragiannis, Haber, Lu, Procaccia & Sheffet, *Optimal Social Choice Functions: A Utilitarian View* (AIJ 2015) · Anshelevich, Bhardwaj, Elkind, Postl & Skowron, *Approximating Optimal Social Choice under Metric Preferences* (AIJ 2018; [arXiv:1512.07590](https://arxiv.org/abs/1512.07590)) · Skowron & Elkind, *Social Choice under Metric Preferences: Scoring Rules and STV* (AAAI 2017; [arXiv:1611.08549](https://arxiv.org/abs/1611.08549)) · Gkatzelis, Halpern & Shah, *Resolving the Optimal Metric Distortion Conjecture* (FOCS 2020; [arXiv:2004.07447](https://arxiv.org/abs/2004.07447)) · Kizilkaya & Kempe, *Plurality Veto: A Simple Voting Rule Achieving Optimal Metric Distortion* (IJCAI 2022; [arXiv:2206.07098](https://arxiv.org/abs/2206.07098)) · Amanatidis, Birmpas, Filos-Ratsikas & Voudouris, *Peeking Behind the Ordinal Curtain: Improving Distortion via Cardinal Queries* (AIJ 2021; [arXiv:1907.08165](https://arxiv.org/abs/1907.08165)) · Survey: Anshelevich, Filos-Ratsikas, Shah & Voudouris, *Distortion in Social Choice Problems: The First 15 Years and Beyond* (IJCAI 2021; [arXiv:2103.00911](https://arxiv.org/abs/2103.00911)).
