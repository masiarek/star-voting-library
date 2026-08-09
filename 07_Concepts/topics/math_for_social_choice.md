---
tags:
  - theory
  - foundations
  - multi-winner
---

# The mathematics of social choice — what to study, in what order

*Social choice is **aggregation**: many individual opinions in, one collective decision out. Which mathematics you need follows from two questions — **what structure are the opinions?** (an order, a score vector, an approval set) and **what are you trying to guarantee?** (a winner nobody can beat, or a fair *division* of several seats). Answer those two and the syllabus writes itself, because the single-winner and proportional branches need genuinely different mathematics. This page maps both, marks the parts that pay off fastest, and says honestly where the ceiling is for a reader who wants to follow the literature rather than extend it.*

**Level: reference · deep dive** Companions: [the statistics you actually need](statistics_for_voting.md) (reading empirical papers) · [how to learn about voting methods](how_to_learn_about_voting_methods.md) (the concept path, not the math).

---

## The fork that decides your syllabus

The two halves of the field diverge early, and studying the wrong branch first is the most common way to stall:

| | **Single-winner** | **Proportional (PR)** |
|---|---|---|
| The question | *Who is the collective favorite?* | *How do we split k seats so every group gets its share?* |
| The core mathematics | **graph theory** (tournaments, cycles) + **axiomatics** | **apportionment** + **optimization** + **fair division** |
| The famous impossibility | [Arrow](arrow_theorem_and_star.md) (ranked ballots) · [Gibbard–Satterthwaite](gibbard_satterthwaite_theorem.md) (strategy) | **Balinski–Young** (quota vs. paradox-freedom) |
| The hard case | a **cycle** — A beats B beats C beats A | a **remainder** — the seats don't divide evenly |
| Repo deep dive | [the math behind Condorcet](../../05_Ranked_Robin/01_Learn/the_math_behind_condorcet.md) | [the math behind proportional STAR](../../03_STAR_PR/01_Learn/STAR_PR/the_math_behind_proportional_star.md) |

Both branches share a foundation (discrete math, probability, the axiomatic habit), and both end up in game theory. But a graph-theory course will not teach you PR, and apportionment theory will not teach you why Condorcet methods disagree.

---

## Tier 0 — the arithmetic that does most of the real work

Worth saying before the syllabus, because it is the honest answer for most people: **the mathematics that actually decides real elections is fourth-grade arithmetic applied carefully.** Quotas are a division. Divisor methods are a division repeated. Reweighting is a fraction. If your goal is to *run, explain, or advocate* a method rather than prove things about it, this tier plus a spreadsheet is genuinely enough:

- **Quotas.** Hare quota = votes ÷ seats. **Droop** quota = ⌊votes ÷ (seats + 1)⌋ + 1 — the smallest number of votes that *cannot* be achieved by more candidates than there are seats. At district magnitude M, roughly `1/(M+1)` of the vote wins a seat: three seats ≈ 25%, ten seats ≈ 9%.
- **Divisor sequences.** D'Hondt divides by 1, 2, 3, … ; Sainte-Laguë by 1, 3, 5, …. Rank the resulting quotients, hand out seats down the list. That is the whole algorithm.
- **Percentages, weighted averages, and where the denominator went.** More published voting arguments break here than anywhere else — see [the statistics you actually need](statistics_for_voting.md) on sum vs. mean.

Everything below this line is for *reading the literature* and *proving things*, not for counting a ballot.

---

## The shared foundation

| Area | What it buys you in this field | Concretely |
|---|---|---|
| **Relations & order theory** | The definition of a ballot. A ranked ballot *is* a binary relation; a profile is a tuple of them. Transitivity, completeness, weak vs. strict orders, quotient structures. | Why "individually transitive, collectively cyclic" is not a paradox but the expected behavior of aggregation |
| **Combinatorics & counting** | Sizing the problem: how many profiles, how many committees, how many pairwise comparisons. Binomial coefficients everywhere. | `C(n,2)` pairwise contests → [summability](summability/README.md); `C(m,k)` committees → why exhaustive search dies |
| **Proof technique & the axiomatic method** | The literature's native genre is *characterization* and *impossibility*. You need to read a proof by contradiction and follow "assume a rule satisfying A, B, C; derive a contradiction." | Every theorem named after a person on this page |
| **Probability** | Electorate models, cycle frequencies, Monte Carlo, tie probability, seeded shuffles. | Impartial culture gives a ~8.8% chance of no Condorcet winner with 3 candidates as voters → ∞; real electorates are far lower ([measured](condorcet/condorcet_efficiency_measured.md)) |
| **Statistics** | Reading simulation papers without being fooled by them. | [The statistics you actually need](statistics_for_voting.md) |
| **Linear algebra** | Spatial models, the pairwise matrix as a matrix, reweighting bookkeeping, and — once you get to biproportional PR — matrix scaling. | [the spatial voting model](spatial_voting_model.md) · [pairwise counting](pairwise_counting.md) |

---

## The single-winner branch

**Graph theory is the spine.** Turn a profile into a *tournament* — a directed graph with one arc per pair, pointing from winner to loser — and the entire Condorcet family becomes graph algorithms:

- **Tournaments and their solution sets** — Copeland (count out-degree), the **Smith set** (the smallest dominant set — a top cycle), the uncovered set, Banks, Slater. This is the C1 tier of [Fishburn's classification](condorcet/condorcet_reading_list.md).
- **Cycles and feedback arc sets** — Kemeny's rule is the minimum feedback arc set problem in disguise, and is NP-hard. Slater likewise.
- **Path/beatpath algorithms** — Schulze is a widest-path computation (Floyd–Warshall).
- **McGarvey's theorem** — *every* tournament is realizable by some profile. The consequence is bracing: no property of the pairwise matrix is off the table, so a rule that reads only the tournament has to cope with any graph at all.
- **Combinatorial Hodge theory** — the decomposition of a pairwise-comparison flow into a consistent "gradient" part plus a genuinely cyclic part, which puts a number on how much of a profile is irreducibly circular. See [the cycle–cocycle decomposition](cycle_cocycle_decomposition.md).

**Then the axiomatics.** [Arrow](arrow_theorem_and_star.md) (ranked ballots, IIA, ≥3 alternatives), [Gibbard–Satterthwaite](gibbard_satterthwaite_theorem.md) (strategy-proofness), [May's theorem](mays_theorem.md) (why majority rule is uniquely right for exactly *two* options), Black's single-peakedness and the median voter theorem (the domain restriction that makes cycles vanish). Note the scope carefully: Arrow is a theorem about *ranked* input, which is why rated methods sidestep it and land under Gibbard's 1978 generalization instead — see [ordinal vs. cardinal, as mechanism design](ordinal_vs_cardinal_mechanism_design.md).

**And the modern quantitative layer:** **distortion** — the worst-case ratio between the winner's true social cost and the optimum, when the rule sees only ordinal information. *Metric* distortion assumes voters and candidates sit in a metric space, and the results are sharp: no deterministic ranked rule beats a factor of 3, and rules achieving exactly 3 are now known. See [distortion](distortion.md) and [cardinal utility](cardinal_utility.md).

---

## The PR branch — four pillars

This is the branch worth studying if PR is the goal, and it is where the mathematics is currently most active.

### 1. Apportionment theory

The oldest and most directly useful. Two families, and the impossibility that separates them:

- **Divisor methods** — Jefferson/**D'Hondt** (divisors 1, 2, 3…), Webster/**Sainte-Laguë** (1, 3, 5…), Adams, **Huntington–Hill** (geometric-mean divisors — the US House method). All are *house-monotone* and paradox-free, none is guaranteed to stay within quota.
- **Quota methods** — Hamilton / **largest remainder**. Always within quota, and vulnerable to the [Alabama paradox](../../03_STAR_PR/03_Criteria/alabama_paradox/README.md), the population paradox, and the new-states paradox.
- **The Balinski–Young theorem (1982)** — no apportionment method can both always satisfy quota and always avoid the population paradox. This is PR's Arrow: the trade is structural, not a failure of imagination.

Why this matters for *ballot-based* PR and not just party lists: score-PR's reweighting rules are apportionment in disguise. Deweighting a ballot by `1/(1+support)` after each win **is** the D'Hondt divisor sequence. That equivalence is worked out in [the math behind proportional STAR](../../03_STAR_PR/01_Learn/STAR_PR/the_math_behind_proportional_star.md).

### 2. Optimization, submodularity, and complexity

Most principled PR rules are stated as *maximize a satisfaction function over committees* — which is an integer program:

- **Thiele's methods** (1890s) maximize a sum of concave per-voter satisfactions; with harmonic weights `1, ½, ⅓, …` that is **PAV**. **Chamberlin–Courant** maximizes each voter's single best representative (a facility-location / assignment problem). **Monroe** adds equal-size constituencies.
- **These optimal versions are NP-hard** — PAV, CC, Monroe, and Kemeny all are. That is not a footnote; it is *why* every deployed method is sequential and greedy.
- **Submodularity is the reason greedy works anyway.** Concave satisfaction ⇒ diminishing returns ⇒ submodular objective ⇒ the greedy algorithm carries a `1 − 1/e` approximation guarantee (Nemhauser–Wolsey–Fisher, 1978). Sequential PAV, RRV, and the STAR-PR variants are all instances of that greedy.
- **Phragmén's methods** take the dual view — treat each seat as a unit of "load" to be spread across the voters who elected it, and **minimize the maximum load**. A min–max convex problem rather than a max-sum one, and it produces measurably different committees.
- **The Method of Equal Shares** (Peters & Skowron, 2020; originally "Rule X") gives every voter an equal budget and makes candidates buy their way in. It runs in polynomial time *and* satisfies EJR — the combination that made it the headline result of the last decade, and it is now used for real participatory budgeting in Poland and Switzerland.

So: **linear/integer programming**, **convex optimization**, **submodular maximization**, and enough **complexity theory** to read an NP-hardness reduction and an approximation ratio.

### 3. Fair division and cooperative game theory

What "proportional" *means*, formally. This is where the field has moved since ~2015, and it is the part most under-taught relative to its importance:

- **PSC** (Proportionality for Solid Coalitions) — the classical STV-era guarantee.
- **JR → PJR → EJR → EJR+ / FJR** — the justified-representation hierarchy: any group of voters that is large enough *and* cohesive enough is owed representation, with each rung strengthening what "owed" means.
- **The core** — borrowed straight from cooperative game theory: no group of voters could break away with their proportional share of the seats and all do better. The strongest notion, and for approval PR it is still **open** whether a rule always achieving it exists.
- **Priceability** — the market reading: a committee is priceable if you can hand out equal budgets and explain every winner as a purchase. This is what the Method of Equal Shares makes literal.

Prerequisites: basic **cooperative game theory** (characteristic functions, the core, Shapley value) and **fair division** (proportionality, envy-freeness). Moulin's *Fair Division and Collective Welfare* is the standard entry.

### 4. Matrix scaling — the pillar people miss

**Biproportional apportionment** — seats proportional to party *and* to district, simultaneously — is a matrix problem: find diagonal scalings of a vote matrix whose rounded row and column sums hit both sets of targets. The algorithm is **iterative proportional fitting** (RAS / Sinkhorn–Knopp), the existence proof is convex optimization, and the whole thing is deployed in Swiss cantonal elections as "double Pukelsheim." If you want the mathematically prettiest corner of PR, it is this one.

Adjacent, and worth knowing exists: **Meek's STV** solves for candidates' keep-values by fixed-point iteration rather than closed form — numerical analysis inside a vote count.

---

## What to study, in order

Assuming PR is the destination. Each step is useful on its own, so stopping early is a real option, not a failure:

1. **Tier 0 arithmetic + quotas + divisor methods.** A weekend. Covers most of what PR practice needs, and makes every later abstraction concrete.
2. **Discrete mathematics** — relations, orders, counting, proof technique. The one genuinely non-negotiable course.
3. **Probability and statistics**, at the level of reading a simulation paper: distributions, expectation, sampling error, and the discipline of never quoting a rate without its model.
4. **Apportionment theory** (Balinski–Young). Short, self-contained, and directly explains every reweighting rule you will meet.
5. **Optimization**: linear and integer programming, then convexity, then submodularity and the greedy guarantee. This is the step that turns "the rule is NP-hard" from a scary sentence into a design decision.
6. **Cooperative game theory and fair division** — the core, proportionality, envy-freeness. Then the JR/PJR/EJR literature reads as ordinary mathematics rather than jargon.
7. **Computational complexity**, enough to follow a reduction and an approximation ratio.
8. **Graph theory and tournaments** — move this to position 2 if single-winner Condorcet methods are your actual interest.
9. **Game theory and mechanism design** — strategic voting, equilibria, and why strategy-proofness is unattainable.
10. **Metric distortion / algorithmic social choice** — the current research frontier, and it presumes 5, 7, and 9.

**The shortest honest path to reading modern PR papers** is 1 → 2 → 4 → 5 → 6. Graph theory and mechanism design can wait unless the single-winner branch is what you're after.

---

## Where each idea lands in this repo

Everything below is runnable here — that is the point of the library.

| You just studied… | Run it here |
|---|---|
| Quotas, divisor methods, reweighting | [the math behind proportional STAR](../../03_STAR_PR/01_Learn/STAR_PR/the_math_behind_proportional_star.md) · [what "proportional" actually means](../../03_STAR_PR/01_Learn/what_proportional_means.md) |
| The Alabama paradox, concretely | [the Alabama paradox, tabulated](../../03_STAR_PR/03_Criteria/alabama_paradox/README.md) |
| Thiele / PAV / Phragmén | [the abcvoting engine](../../06_Other/abcvoting_tabulation_engine/README.md) — `pav`, `seqpav`, `seqphragmen` on real ballots |
| Quota vs. reweighting, same ballots | [STAR-PR: Allocated Score, SSS, RRV](../../03_STAR_PR/01_Learn/STAR_PR/README.md) · [STV vs. proportional STAR](../../method_comparisons/stv_vs_star_pr/README.md) |
| Comparing multi-winner families | [comparing multi-winner methods](comparing_multiwinner_methods.md) · [electing more than one](electing_more_than_one.md) |
| Tournaments, cycles, Copeland | [the math behind Condorcet](../../05_Ranked_Robin/01_Learn/the_math_behind_condorcet.md) · [tournament solutions](tournament_solutions.md) · [the Smith set](smith_set.md) |
| Cyclic vs. consistent components of a profile | [the cycle–cocycle decomposition](cycle_cocycle_decomposition.md) |
| Arrow, Gibbard–Satterthwaite, May | [does Arrow's theorem apply to STAR?](arrow_theorem_and_star.md) · [Gibbard–Satterthwaite](gibbard_satterthwaite_theorem.md) · [May's theorem](mays_theorem.md) |
| Distortion and cardinal utility | [distortion](distortion.md) · [cardinal utility](cardinal_utility.md) · [ordinal vs. cardinal as mechanism design](ordinal_vs_cardinal_mechanism_design.md) |
| Probability models of electorates | [election simulation models](election_simulation_models.md) · [simulate utilities, not ballots](simulate_utilities_not_ballots.md) · [the spatial voting model](spatial_voting_model.md) |
| Counting complexity / summability | [summability](summability/README.md) |
| Cross-checking a count against an independent library | [cross-checking with pref_voting](../tabulation_engines/cross_checking_with_pref_voting.md) |

---

## Sources, with their leans marked

**Free and online — start here.**

| Source | Why | The lean |
|---|---|---|
| **[Multi-Winner Voting with Approval Preferences](https://link.springer.com/book/10.1007/978-3-031-09016-5)** — Martin Lackner & Piotr Skowron (Springer, 2023) | **The** book for the PR branch. Open access, ~120 pages, and it covers Thiele, Phragmén, the JR/PJR/EJR hierarchy, and the complexity results in one consistent vocabulary. Its companion library `abcvoting` is [vendored in this repo](../../06_Other/abcvoting_tabulation_engine/README.md). | **Neutral / academic.** |
| **[Handbook of Computational Social Choice](https://procaccia.info/wp-content/uploads/2020/03/comsoc.pdf)** — Brandt, Conitzer, Endriss, Lang & Procaccia (CUP, 2016) | The field's reference work, complete and free. Ch. 2 (introduction), ch. 3 (tournament solutions), ch. 9 (multiwinner), ch. 12 (complexity of manipulation). | **Neutral / academic.** Dense. |
| **[Voting Methods](https://plato.stanford.edu/entries/voting-methods/)** — Eric Pacuit, *Stanford Encyclopedia of Philosophy* | The best free survey, and rigorous about definitions. Read before any wiki. | **Neutral / academic.** |
| **[equalshares.net](https://equalshares.net/)** | The Method of Equal Shares explained by its authors, with the participatory-budgeting deployments. | **Authors of the method** — excellent on mechanics, naturally favorable on verdicts. |
| **[pref_voting](https://pref-voting.readthedocs.io/)** — Holliday & Pacuit | The definitions as runnable code, organized by the standard taxonomy. Already declared in this repo. | **Neutral / academic.** |

**Books.** Full annotations on the repo's shelf: [social choice theory](../books/social_choice_theory.md) · [electoral systems & PR](../books/electoral_systems_and_pr.md).

- **Balinski & Young, *Fair Representation* (1982; 2nd ed. 2001)** — apportionment done properly, and the impossibility theorem in its original setting. The single best value-per-page on this list. **The lean:** rigorous and largely neutral, though the authors argue openly for Webster/Sainte-Laguë.
- **Pukelsheim, *Proportional Representation: Apportionment Methods and Their Applications* (2nd ed. 2017)** — the technical reference, including biproportional methods. Consult it, don't read it front to back. **The lean:** mathematics with legal applications; no campaign.
- **Moulin, *Fair Division and Collective Welfare* (2003)** — the fair-division and cooperative-game foundation the modern PR axioms are built on. **The lean:** academic, welfare-economics framing.
- **Börgers, *Mathematics of Social Choice* (2010)** — the gentlest real *textbook*, with exercises. Classical ranked methods; rated methods are not its subject. **The lean:** neutral textbook.
- **Taylor, *Social Choice and the Mathematics of Manipulation* (2005)** — the strategy-proofness results, proved. **The lean:** neutral.
- **Nurmi, *Voting Paradoxes and How to Deal with Them* (1999)** — a catalogue of what goes wrong, useful as a lookup table. **The lean:** survey-neutral. Pairs with the repo's own [paradoxes collection](../voting_paradoxes/README.md).

---

## The caveat worth keeping

Two, actually, and they pull in opposite directions.

**The mathematics does not settle the question.** Every impossibility theorem on this page says the same thing in a different dialect: there is no rule that satisfies all the properties you want, so choosing a voting method is choosing *which* guarantee to give up. That is a normative decision wearing a formal costume. The math tells you the menu is finite and what each item costs; it does not order for you.

**And precision is still worth it**, because the most common failure in voting argument is not bad mathematics but *transferred* mathematics — quoting an apportionment theorem at a ballot-based rule that it wasn't proved for, or a tournament result at a rule that reads margins. Knowing which theorem covers which object is most of what this syllabus buys.

## Related

- [The statistics you actually need to read voting research](statistics_for_voting.md) — the empirical-paper companion
- [How to learn about voting methods](how_to_learn_about_voting_methods.md) — the concepts path, no math required
- [Condorcet methods — a reading list](condorcet/condorcet_reading_list.md) — the single-winner branch in depth
- [The math behind proportional STAR](../../03_STAR_PR/01_Learn/STAR_PR/the_math_behind_proportional_star.md) · [The math behind Condorcet](../../05_Ranked_Robin/01_Learn/the_math_behind_condorcet.md)
- [Books on voting methods](../books/README.md) · [Glossary](../GLOSSARY.md) · [Curriculum](../CURRICULUM.md)
