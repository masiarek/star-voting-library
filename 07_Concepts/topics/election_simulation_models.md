---
tags:
  - foundations
  - simulation
---

# Election simulation models — how voters and ballots are generated for testing

*You can't read voters' minds, and you can't run millions of real elections under a dozen methods. So to compare methods (the [VSE / Bayesian-Regret](what_makes_a_good_winner.md#measuring-it-empirically-vse-bayesian-regret) studies), you **simulate**: generate synthetic electorates, cast ballots, tabulate, and score the outcome — thousands of times. This page is the neutral technical menu of the models used to generate those electorates, and a standing caution: **every conclusion is conditional on the model.***

→ **Level: 301 · deep dive** — Curriculum [301.10](../curriculum/CURRICULUM_301.md). **Read first:** [Simulate utilities, not ballots](simulate_utilities_not_ballots.md) — *why* you sample preferences (the models below) and derive ballots from them, rather than drawing random ballots directly. Companion: [What makes a good winner?](what_makes_a_good_winner.md) · [What makes a voting method good?](what_makes_a_voting_method_good.md).

## The prerequisites (what the math is built from)

*Reading the wider literature rather than building a model? Start with [the statistics you actually need](statistics_for_voting.md) — mean vs median as a method-defining choice, variance as the meaning of "divisive", and why correlated electorates make impartial culture a stress test rather than a prediction.*

- **Combinatorics** — [`N!`](https://en.wikipedia.org/wiki/Permutation) strict rankings of N candidates (5 → 120); [combinations](https://en.wikipedia.org/wiki/Combination) for candidate subsets.
- **Probability distributions** — [**Uniform**](https://en.wikipedia.org/wiki/Discrete_uniform_distribution) (Impartial Culture), [**Normal/Gaussian**](https://en.wikipedia.org/wiki/Normal_distribution) (spatial clustering around a center), [**Dirichlet**](https://en.wikipedia.org/wiki/Dirichlet_distribution) (random bloc mixtures that sum to 1).
- **Distance metrics** — [**Euclidean**](https://en.wikipedia.org/wiki/Euclidean_distance) `√Σ(xᵢ−yᵢ)²` (the heart of spatial models), and [**Kendall-Tau**](https://en.wikipedia.org/wiki/Kendall_tau_distance) (number of pairwise disagreements / adjacent swaps between two rankings — used by Mallows).

## Two families of model

### A. "Noise" / statistical models (no geometry)

*This page is the library's home for these six, so the term itself isn't a link — the deeper treatment is [why you sample preferences at all](simulate_utilities_not_ballots.md), [the standing caveat below](#the-standing-caveat-results-are-conditional-on-the-model), and [what IC does to a method comparison](distortion.md#does-averaging-rescue-rankings-not-by-itself). The outward citation at the end of each line is the defining source, for readers who want the original.*

- **Impartial Culture (IC)** — every one of the `N!` rankings is equally likely (each voter is an independent die-roll, prob `1/N!`). Simplest and most common in the literature; "nothing up my sleeve." *Caveat below on cycles — and a harder one on distortion.* ([Wikipedia](https://en.wikipedia.org/wiki/Impartial_culture))
- **Impartial Anonymous Culture (IAC)** — every anonymous *tally* (vote-count profile) is equally likely, via "stars-and-bars" combinatorics. It weights unusual/close configurations more heavily, so it's favored for **stress-testing** edge cases and [paradox rates](../voting_paradoxes/README.md). ([Wikipedia](https://en.wikipedia.org/wiki/Impartial_anonymous_culture))
- **Impartial, Anonymous and Neutral Culture (IANC)** — IAC with one more symmetry divided out: candidate *names* are immaterial too, so the object drawn is an equivalence class of tallies under relabelling the candidates (Eğecioğlu and Giritligil call a representative of one a **root**), and every class is equally likely. That makes the three a single construction under three groups — IC quotients by nothing, IAC by the voter permutations `Sₙ`, IANC by `Sₙ × S_m` — and it is the model that matches what an *anonymous and neutral* rule can actually see, since such a rule cannot tell two relabelled tallies apart in the first place. Classes are not all the same size: a tally with internal symmetry (the perfect Condorcet cycle, an exact three-way tie) sits in a class smaller than `m!`, so IANC gives those shapes extra weight and reads paradoxes a little higher than IAC on tiny electorates — converging to it as the electorate grows. ([Eğecioğlu & Giritligil 2013](https://sites.cs.ucsb.edu/~omer/DOWNLOADABLE/GMAS_public_preference13.pdf) — Wikipedia covers it as a section of [the IAC article](https://en.wikipedia.org/wiki/Impartial_anonymous_culture))
- **Mallows (φ-model)** — a *reference ("true") ranking* plus noise: the probability of a ballot decays exponentially in its Kendall-Tau distance from the reference. `φ=0` → everyone votes the reference; `φ=1` → pure IC; `0<φ<1` → clustered-with-noise. Good for "polarized but correlated" electorates. ([Mallows 1957](https://doi.org/10.1093/biomet/44.1-2.114) — no Wikipedia article exists)
- **Plackett-Luce** — each candidate has a "strength" `γ`; `P(A ranked 1st) = γ_A / Σγ`, then repeat for 2nd place among the rest. Common in machine-learning "learning-to-rank." ([Wikipedia](https://en.wikipedia.org/wiki/Plackett%E2%80%93Luce_model))
- **Pólya-Eggenberger (urn) models** — draw a ballot for A, return it *plus an extra* A: "the rich get richer." Produces heavy **bloc/clustering** correlation naturally, modeling social influence — no geometry needed. ([Wikipedia](https://en.wikipedia.org/wiki/P%C3%B3lya_urn_model))

*You don't have to write any of these samplers: all but IANC ship in `pref_voting`'s profile generators — the same library this repo already leans on for its [independent Copeland cross-check](../../05_Ranked_Robin/01_Learn/ranked_robin.md), so it's already a dependency. ([docs](https://pref-voting.readthedocs.io/en/latest/generate_profiles.html)) What those samplers are actually called, what each one's parameter does, and the three that are commonly quoted wrongly: [Statistical cultures](statistical_cultures.md) — which also measures how much the choice moves a result.*

### B. Spatial (geometric / ideological) models — the realistic "gold standard"

*New to the idea? Start with the concept page: [The spatial model — voters and candidates as points on a map](spatial_voting_model.md) (the political spectrum, the median voter theorem, and why it predicts center-squeeze). This subsection is the simulation-recipe version — and once you are writing the code, [the six Euclidean spaces](euclidean_spaces.md) names and draws the actual shapes the libraries offer (`uniform_ball`, `gaussian_cube`, `unbounded_gaussian`…), including which of them is worth its cost.*

Voters and candidates are **points in an N-dimensional space** (1-D left–right, 2-D adds e.g. libertarian–authoritarian). A voter prefers the candidate **closest** to them (Euclidean distance); for *scored* methods, distance is converted to a **utility** (e.g. `utility = 100 − distance × factor`, or a Gaussian/decreasing function). Voters are typically drawn from a **multivariate Normal** (a bell curve centered on the median voter); candidates uniform or clustered. This is what the **Ka-Ping Yee diagrams** visualize, and what the more sophisticated VSE "hierarchical clusters" model elaborates (issue clusters, identity clusters, varying salience).

## The standing caveat: results are conditional on the model

Different generators make different scenarios common or rare, which changes what a study concludes:

- **Impartial Culture** produces many near-ties (all candidates ~equal quality), which some theorists (e.g. [Tsetlin, Regenwetter & Grofman 2003](https://doi.org/10.1007/s00355-003-0269-z)) call unrealistic — methods never get to show their skill at "ferreting out the best candidate." **That objection is now a theorem, not just a worry:** under IC, *every* voting rule — deterministic or randomized — has average [distortion](distortion.md) Ω(m), while drawing a winner uniformly at random and ignoring the ballots achieves ≤ m. So on this model there is no skill to show, by proof ([Caragiannis & Fehrs 2024](https://arxiv.org/abs/2307.07350); worked through [here](distortion.md#does-averaging-rescue-rankings-not-by-itself)). Treat an IC-computed method comparison as close to information-free.
- **Spatial / n-dimensional** models make central candidates genuinely stronger (more realistic), but can make hard cases like **[Condorcet cycles](condorcet/README.md) nearly impossible**, so cycle-resolving methods never get tested.
- **Hierarchical-cluster** models sit in between — [8.68% of three-candidate elections have no Condorcet winner under IC, against 0.15% under a spatial model](ties/how_often_condorcet_methods_tie.md#the-realistic-electorate-answer-it-rarely-matters-at-all) — and produce cycles at a plausible ~5–15% rate, which is why the headline VSE numbers use them.

So a method's measured score is only as trustworthy as the voter/strategy model behind it. This is the same evenhandedness point from the [method-quality page](what_makes_a_voting_method_good.md#where-reasonable-people-disagree-the-live-debates): VSE is a strong tool, but it is *not model-independent*.

### A correction worth flagging

A common summary says "IC makes ties **and cycles** vanishingly rare in large elections." **Exact ties** do vanish as the electorate grows — but **cycles do not**: under IC the probability of *no Condorcet winner* converges to a *positive* limit (≈ **8.8%** for 3 candidates, rising with more candidates). And IC vs. IAC runs the *opposite* way often assumed: for 3 candidates in the large-electorate limit, **IC ≈ 8.77% vs. IAC ≈ 6.25%** (Gehrlein) — IC yields *more* cycles, not fewer. The right takeaway is just that **the model choice materially changes paradox rates**, so it must be stated.

**And the model choice bites hardest where the electorate is smallest.** Take the smallest interesting case — 3 candidates, 3 voters — small enough that all three models can be counted exactly instead of sampled. Exactly one profile *shape* has no Condorcet winner: the perfect cycle, one ballot each of `A>B>C`, `B>C>A`, `C>A>B`. It is 12 of IC's 216 labelled profiles, 2 of IAC's 56 tallies, and 1 of IANC's 10 classes — so the probability that a Condorcet winner exists is **94.44% (IC) · 96.43% (IAC) · 90.00% (IANC)**, three readings of one shape rather than three different findings. (The first two are Gehrlein's published values; the third is the exact count behind the 0.8959 the IANC paper sampled.) The gap then closes fast, and in a way worth knowing: for 3 candidates, IANC and IAC are *literally the same distribution* whenever the voter count shares no factor with `3! = 6`, because every class then has exactly 6 members — and at 4 candidates `m!` times the class count is within 0.02% of the tally count by twelve voters. Between these models, paradox rates are a small-electorate concern, not a large one.

## The second standing caveat: a strategic number needs its sincere baseline

The caveat above is about the electorate. This one is about the *ballots*, and it bites hardest on exactly the studies that look most sophisticated — the ones that let voters behave strategically.

A simulation that reports **one** number per method under strategy ("how often does the sincere [Condorcet winner](condorcet/README.md) still win?") has merged three events that carry opposite weight: the method missing while every ballot is honest, an attack succeeding, and an attack backfiring on the people who cast it. The failure mode is not subtle and it is not hypothetical — on that single merged number, methods converge, and they converge because a method that is **bad on sincere ballots has less left for an attacker to take**. [Plurality](plurality.md) ties [Ranked Robin](../../05_Ranked_Robin/01_Learn/ranked_robin.md) on it, having lost nothing to the attack at all, because burial cannot reach a rule that reads one mark.

So: **print the sincere column beside the strategic one, always.** The gap between them is the quantity the study is actually about; the strategic column alone is not interpretable. Two further columns are worth the trouble whenever a strategy is being modelled — whether the attack **paid or backfired for the attackers** (a method that punishes manipulation is doing something a hit rate cannot see), and **how large a coalition** the successful attack needed.

Worked through, with the tables and a five-question checklist for reading anyone else's version: [formal compliance vs. strategic preservation of the sincere winner](compliance_vs_strategic_preservation.md). The sincere baselines themselves, for six methods across these models: [Condorcet efficiency, measured](condorcet/condorcet_efficiency_measured.md).

## In this repo

Our test cases are **hand-crafted** (small, legible elections designed to isolate one behavior), not simulation-generated — the opposite end from VSE. The two are complementary: simulations answer "how *often* does a method go wrong across many electorates?", while our worked cases answer "*how* does it go wrong, concretely, on this ballot set?" (see [What makes a good winner?](what_makes_a_good_winner.md) and the [test-case catalog](../YAML_test_case_index/CATALOG.md)).

## References

- cdsmith, *Simulating Elections with Spatial Voter Models* — [blog](https://cdsmithus.medium.com/simulating-elections-with-spatial-voter-models-1ff50892390) · [code](https://github.com/cdsmith/spatial-voting)
- [Voter Satisfaction Efficiency (VSE) — model details](https://electionscience.github.io/vse-sim/) · [Gehrlein, *Condorcet's Paradox*](https://doi.org/10.1007/3-540-33799-7) (Springer, 2006 — paradox probabilities under IC/IAC)
- [What makes a good winner?](what_makes_a_good_winner.md) · [What makes a voting method good?](what_makes_a_voting_method_good.md)
