# Simulating proportional systems — how the studies are built

**One line:** almost every quantitative claim about how a proportional method "performs" comes out of a simulation, and the result usually depends more on how the *voters* were generated than on the method being tested — so this page is the parameter list, the voter models, and the honest sensitivity warnings you need to read one of those studies critically.

→ what the word promises: [What "proportional" actually means](what_proportional_means.md) · the method: [STAR-PR](STAR_PR/README.md) · the simulations this repo actually runs: [`06_Other/simulations/`](../../06_Other/simulations/README.md)

**Level: 401 · deep dive**

---

## Why the voter model is the real design choice

A simulation needs *preferences* before it can test a method, and there is no neutral way to invent them. The generator you pick determines how much structure exists in the electorate — and structure is exactly what voting methods differ on. Two studies can test the same method, run a million trials each, and disagree because one drew voters at random and the other placed them in ideological space.

| Model | How preferences are generated | Structure it produces | Consequence for simulations |
|---|---|---|---|
| **Impartial Culture (IC)** | each voter's full ranking drawn uniformly and independently from all possible rankings | none — no systematic correlation between voters | inflates paradox and cycle rates; a deliberate worst case, not a realistic electorate |
| **Impartial Anonymous Culture (IAC)** | uniform over *profiles* (vote counts) rather than over each voter independently | mild shared-culture correlation | different paradox rates from IC despite the similar name — the two are routinely confused |
| **Spatial** | voters and candidates are points in an ideological space; preference follows proximity | correlated preferences resembling real electorates | more Condorcet structure; results depend heavily on dimensionality and dispersion |
| **Clustered spatial** | a spatial model with explicit voter clusters or a multimodal distribution | clear blocs, bimodality, geographic separation | changes the *comparative ranking* of methods; the best empirical fit of the four |

**One correction worth carrying, because the summary tables usually get it wrong:** spatial models are often described as producing *single-peaked* preferences. That is guaranteed only in **one dimension**. In 2D or higher — the dimensionality most studies actually use — preferences are generally not single-peaked, majority cycles reappear, and the tidy Condorcet structure of the 1D case is not available. "Spatial" does not mean "cycle-free"; it means "correlated."

## The model STAR's own research uses, and why

If you are simulating STAR specifically, there is a concrete answer rather than a menu. [Wolk, Quinn & Ogren (2023)](https://doi.org/10.1007/s10602-022-09389-3) — the peer-reviewed STAR paper — settled on a **clustered spatial model**, and their reasoning is the clearest published statement of why the choice matters:

- **Impartial Culture produces too many Condorcet cycles** (Tsetlin et al., 2003) — the electorate is too chaotic to resemble anything real.
- **Normally-distributed spatial models overcorrect**, producing too *few* cycles (Tideman, 2020) — too tidy in the opposite direction.
- A **clustered** spatial model sits between them, and because it is **non-parametric** — it admits an unbounded number of clusters rather than a number you fix in advance — it can reproduce real-world scenarios, cycles included, to whatever precision you want.

**Worth flagging honestly:** selecting a generator partly because it yields a realistic *rate of cycles* is a calibration choice, not a neutral one. It is well-argued and the alternatives are worse, but a reader should know the electorate was tuned to match reality on a property that also affects method comparisons. This is the sort of thing to check symmetrically — it would be a fair question to put to any paper, including one favoring a method you dislike.

### How the clustered spatial model is built

Voters and candidates are points in a vector space, distributed via a hierarchical Dirichlet structure of Gaussian clusters — a [CrossCat](https://doi.org/10.48550/arxiv.1512.01272)-style construction (Mansinghka et al., 2016). Three steps, each doing a job worth naming:

1. **Weight the issue dimensions — stick-breaking Dirichlet process.** Take a stick representing everything voters care about; break off a piece for the first issue, break a piece off *what remains* for the second, and so on. Issue weight decays exponentially on average, so a few issues dominate, many are marginal, and only finitely many dimensions need modeling. Dimensions are added until the remaining weight drops below a threshold.

2. **Bundle dimensions into "views" — Chinese Restaurant process.** Issues aren't independent; taxes, regulation and debt travel together. Each issue "sits" at a table, preferring tables where similar issues already sit and occasionally starting a new one. The bundles — fiscal, social, and so on — are *discovered*, not declared in advance.

3. **Cluster voters separately within each view — Chinese Restaurant process again.** The powerful step. A voter's group membership is not one-size-fits-all: they can sit with one crowd on fiscal questions and a different crowd on social ones. Each voter cluster gets a mean and variance per dimension, and voters' ideal points are drawn normally from them.

That third step is what makes the model realistic. A voter who is free-market **and** socially liberal, another who is state-control **and** socially liberal, a third who is free-market **and** socially conservative — cross-cutting identities that a single left-right axis cannot represent. And it is precisely those cross-cutting cleavages that let genuine Condorcet cycles emerge on their own, rather than being injected by randomness (IC) or smoothed away (single-cluster Gaussian).

**For a STAR-PR simulation specifically**, this is the electorate generator to reach for, with district magnitude and the utility function as the two sweeps that will move your results most. Note what does *not* yet exist here: none of this repo's simulations model proportional multi-winner races, so a STAR-PR study would be new work rather than a parameter change to an existing script.

## The parameters a study has to fix

Any of these can move a result, and papers vary in how many they report.

**Electorate** — number of voters (1,000–100,000; larger stabilizes results), number of candidates (typically 5–30), **number of seats**, and the voter-distribution model above (uniform, Gaussian, bimodal, or empirically sampled).

**Candidate placement** — random within the space, placed strategically by parties, or deliberately correlated / anti-correlated with voter clusters. How many parties nominate at all is itself a parameter.

**Ballot generation** — how spatial distance becomes a score or a ranking. The **utility function** (linear, quadratic, or Gaussian decay with distance) matters more than it sounds: it is what decides whether preference *intensity* carries real information. Plus noise and irrationality rates, truncation rate (how many voters submit partial ballots — central for STV), and the strategic-vs-sincere mix.

**Method parameters** — quota type (Droop, Hare, Hagenbach-Bischoff), any electoral threshold, the tie-breaking rule, STV's transfer method (weighted inclusive Gregory vs. random sample), and for scored methods the **score range** (0–5, 0–10).

**Structure** — trial count (typically 10⁴–10⁶ per condition), a fixed seed for reproducibility, sensitivity sweeps varying one parameter at a time, and whether the scenarios are Monte Carlo or adversarial.

## What gets measured

- **Proportionality indices** — Gallagher, Loosemore–Hanby
- **Voter Satisfaction Efficiency (VSE)** — the most common modern summary metric
- **Condorcet efficiency** — how often the Condorcet winner is elected
- **Utilitarian efficiency** — total voter utility of the outcome
- **Representation of minorities**, wasted votes, ballot exhaustion rate, strategic manipulability

## The two findings that dominate

**District magnitude beats almost everything else.** Seats per district moves PR outcomes more than any other single variable. Proportionality improves sharply from 1 → 5 seats and the gains flatten after roughly 7. This is also the lever with the clearest trade-off attached, since the same increase lowers the win threshold — see [what proportionality does not promise](what_proportional_means.md).

**Spatial model × utility function is second, and it is the one that decides score-vs-rank comparisons.** Scored methods can only outperform ranked ones when *preference intensity* carries information the ranking would discard. That is a property of the generator, not of the method: choose a utility function where intensity is flat or meaningless and STAR-family methods lose their advantage by construction. **This cuts against the repo's own subject as much as for it**, and is the first thing to check when a simulation reports that scored methods do especially well — or especially badly.

## Reading one of these critically

Methodological surveys converge on the same advice:

- **Match model to question.** IC for a neutral baseline or theoretical worst case; spatial or clustered for any claim about practical performance.
- **Demand sensitivity checks.** Dimensions, dispersion and cluster tightness should be varied and the variation reported. Different settings can *reverse* which method wins.
- **Prefer empirical calibration** — fit the model to real summary statistics where possible.
- **Look for more than one culture.** A robust claim survives both a structured and a neutral generator. A claim reported under only one is model-dependent until shown otherwise.

The failure mode is specific and common: a normative conclusion that holds only under an unrealistic impartial culture, or only under one narrow spatial specification.

## Where this repo sits

This library is mostly the *opposite* instrument — small hand-built elections where you can see every ballot, plus real frozen results. That is a deliberate complement to simulation, not a substitute: a simulation tells you how often something happens, a worked case tells you what it looks like and proves it can. The repo's own Monte Carlo tools live in [`06_Other/simulations/`](../../06_Other/simulations/README.md) (Condorcet efficiency, favorite-betrayal rates, runoff reversals, STAR-vs-Approval and STAR-vs-Ranked-Robin divergence), and none of them currently model *proportional* multi-winner races — the parameters above are what a PR simulation here would have to declare.

*Status note: this page is a synthesis of the methodological literature listed below, assembled as a reading aid. The individual claims have **not** been re-verified against each source here, and the two "dominant findings" above are reported as the literature's consensus rather than as anything this repo has measured. Treat it as a map of the terrain and a checklist for reading a study — not as evidence.*

## References

- M. Diss and E. Kamwa, "Simulations in Models of Preference Aggregation," *Œconomia* 10(2), 279–308, 2020. [doi:10.4000/oeconomia.8251](https://doi.org/10.4000/OECONOMIA.8251)
- N. Boehmer et al., "Guide to Numerical Experiments on Elections in Computational Social Choice," 2024. [arXiv:2402.11765](https://doi.org/10.48550/arxiv.2402.11765)
- H. Nurmi, "An assessment of voting system simulations," *Public Choice* 73(4), 459–487, 1992. [doi:10.1007/BF01789562](https://doi.org/10.1007/BF01789562)
- J. R. Chamberlin and M. X. Cohen, "Toward Applicable Social Choice Theory: A Comparison of Social Choice Functions under Spatial Model Assumptions," *APSR* 72(4), 1341–1356, 1978. [doi:10.2307/1954543](https://doi.org/10.2307/1954543)
- S. Merrill, "A Comparison of Efficiency of Multicandidate Electoral Systems," *AJPS* 28(1), 23, 1984. [doi:10.2307/2110786](https://doi.org/10.2307/2110786)
- F. Brandt and H. G. Seedig, "On the Discriminative Power of Tournament Solutions," 2016. [doi:10.1007/978-3-319-28697-6_8](https://doi.org/10.1007/978-3-319-28697-6_8)
- M. Jankowski and M. Tepe, "Social Heterogeneity and Choice Failure Under Condorcet and Borda," 143–166, 2017. [doi:10.1007/978-3-658-16714-1_6](https://doi.org/10.1007/978-3-658-16714-1_6)
- S. Wolk, J. H. Quinn, and M. Ogren, "STAR Voting, equality of voice, and voter satisfaction: considerations for voting method reform," *Constitutional Political Economy*, 2023. [doi:10.1007/s10602-022-09389-3](https://doi.org/10.1007/s10602-022-09389-3) — *authors are STAR advocates; the paper is peer-reviewed, the affiliation is worth knowing.*
- T. Tideman and F. Plassmann, "The Source of Election Results: An Empirical Analysis of Statistical Models of Voter Behavior."
- C. Song, "Three Empirical Analyses of Voting"; T. Matje, "Empirical Analyses of a Spatial Model of Voter Preferences," 2016.

## See also

- [What "proportional" actually means](what_proportional_means.md) — the criteria these simulations measure against
- [The math behind proportional STAR](STAR_PR/the_math_behind_proportional_star.md) — apportionment theory and the JR/PJR/EJR guarantees
- [`06_Other/simulations/`](../../06_Other/simulations/README.md) — the repo's own Monte Carlo tools
- [Voting 401](../../07_Concepts/curriculum/CURRICULUM_401.md) — where this level of material sits in the curriculum
