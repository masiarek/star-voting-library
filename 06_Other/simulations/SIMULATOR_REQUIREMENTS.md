# A voting simulation harness — goals, requirements, and the existing landscape

**Level: reference · deep dive**

**One line:** for the six methods this library teaches, no existing simulator covers more than half of them — the closest is [VMES](https://github.com/ragconsumer/VMES) in Julia, not [vse-sim](https://github.com/electionscience/vse-sim) in Python — and the case for writing the harness in Rust turns out to depend entirely on *which* of two workloads you want, with a measured 2.9× gap for one and a measured 238× gap for the other.

This is a decision document, not a plan of record. Nothing here has been built. It answers the prior question — *what would a simulator be for, and what would it have to do?* — before any language argument, and it puts the landscape survey in front of the requirements so the requirements can be **harvested from what other people already learned** rather than invented.

**Companions.** [A Rust voting kernel — goals and requirements](../../07_Concepts/tabulation_engines/rust_kernel_requirements.md) and [A Rust tabulation kernel — scope](../../07_Concepts/tabulation_engines/rust_kernel_scope.md) work the same question for the *counter*. Their answer was **no** (2026-08-10), and that answer does not transfer here: a test library's dominant cost is authoring, a simulator's is running. That is a different calculation, and [Part 6](#part-6-should-it-be-rust-measured) does it with a benchmark instead of an intuition.

**Read first if you are starting cold:** [Election simulation models](../../07_Concepts/topics/election_simulation_models.md) (the menu of electorates) · [Simulate utilities, not ballots](../../07_Concepts/topics/simulate_utilities_not_ballots.md) (why utilities are the primitive) · [vse-sim, read from source](../../07_Concepts/topics/vse_sim.md) (the canonical simulator, in detail) · [this folder's README](README.md) (what already runs here).

---

## What this library already has

Not nothing — which changes the question from *"should we build a simulator?"* to *"what would a harness add to twelve scripts that already work?"*

| | state |
|---|---|
| simulation scripts in [this folder](README.md) | **12**, each answering one question, each `uv run`-able standalone |
| voter models available | six [Euclidean spaces](../../07_Concepts/topics/euclidean_spaces.md) + the [statistical cultures](../../07_Concepts/topics/statistical_cultures.md), both implemented *and* cross-checked against `prefsampling` |
| single-winner methods reimplemented in numpy | 6 — STAR, Score, Approval, Ranked Robin, RCV-IRV, Plurality ([`condorcet_efficiency_simulation.py`](condorcet_efficiency_simulation.py)) |
| multi-winner methods simulated | 3 — Allocated Score, SSS, RRV — but only inside [`pr_alabama_paradox.py`](pr_alabama_paradox.py), and only via `starvote` at ~350 elections/s |
| Bloc STAR simulated | **none** |
| strategy modelled | two scripts — [`fbc_simulation.py`](fbc_simulation.py), [`strategic_cw_preservation.py`](strategic_cw_preservation.py) |
| VSE computed | as a *side* metric in two scripts; **there is no cross-method VSE table for this library's own six methods** |

So the gaps are specific rather than general: **multi-winner, Bloc STAR, and a shared VSE surface.** Everything else exists in some script, in a form that cannot be reused by the next script because each one reimplements the methods it needs.

That duplication is the real argument for a harness, and it is worth naming precisely. Twelve scripts share `sample_utilities()` by *copying* it or by importing across files ([`score_encoding_stability.py`](score_encoding_stability.py) imports from [`star_vs_rr_divergence.py`](star_vs_rr_divergence.py), which imports from [`condorcet_efficiency_simulation.py`](condorcet_efficiency_simulation.py)). That chain works, and it is one edit away from a silent divergence between two scripts that both claim to model the same electorate.

---

# Part 1 — What a simulation would be *for*

The discipline from the [kernel requirements page](../../07_Concepts/tabulation_engines/rust_kernel_requirements.md#the-discipline-one-primary-goal) applies unchanged: **each goal below produces a materially different program.** Pick one. The rest are allowed to happen for free or not at all.

### S1 — Reproduce and audit the published VSE numbers

**Success looks like:** this repo can state *"we ran it; here is the number and here is the config"* for the "STAR scores 91%" charts, instead of citing them.

**Demands:** exactly vse-sim's electorate (`KSModel`, 40 voters, 6 candidates), exactly its strategy models, and exactly its metric — because a reproduction that changes the model is not a reproduction.

**Verdict:** **already 90% free, and the remaining 10% is not a simulator.** The published config is a single documented command, the code is public, and this repo has [read it from source and written down every setting](../../07_Concepts/topics/vse_sim.md). The one obstacle is that the reproduction script [does not currently run](../../07_Concepts/about_this_repo/vse_sim_reproduction_gap.md) — a two-line import fix, verified end-to-end. Fix that upstream and S1 is done without writing a simulator. **Do this first regardless of everything else on this page.**

### S2 — Measure this library's own claims, on one shared electorate

**Success looks like:** one table, six methods, per electorate model, with VSE *and* Condorcet efficiency *and* divergence rates, all computed from the same sampled utilities in the same run — so the rows are comparable to each other and not just to themselves.

**Demands:** the six methods on one shared preference primitive, a fixed set of [electorate models](../../07_Concepts/topics/election_simulation_models.md), and a self-describing output format. Nothing exotic.

**Verdict:** **the strongest goal, because it is the one that serves the readers.** Every other item on this list benefits the maintainer. This one puts a number under sentences the library currently has to hedge — and it is mostly *consolidation* of code that already exists, which makes it the cheapest real goal too.

### S3 — Strategy and manipulability

**Success looks like:** a [PVSI](../../07_Concepts/topics/pvsi_strategic_incentive.md)-style number per method, with the sincere baseline beside it, and the coalition size a successful attack needed.

**Demands:** far more than S2 — a strategy model per method per attack type, a polling/information model, and a chooser that decides who defects. This is where simulators get big: vse-sim carries three ballots per voter per method for exactly this reason.

**Verdict:** high value and high cost, and the place where an existing library genuinely earns its keep. [VMES](#part-5-the-landscape) already implements it for these methods; writing a third one is hard to justify unless the goal is to *disagree* with it.

### S4 — Multi-winner: Bloc STAR and STAR-PR

**Success looks like:** a defensible answer to *"how proportional is Allocated Score, actually?"* and *"how much does Bloc STAR over-represent the majority?"* — measured, not asserted.

**Demands:** the hard part is **not** the tabulation, which `starvote` already does. It is that **the metric is unsettled.** Single-winner welfare has an agreed shape (VSE against the best single candidate). Multi-winner does not: you must choose between utilitarian welfare over the committee, a proportionality axiom ([JR / PJR / EJR / FJR](https://arxiv.org/pdf/2408.02300), checkable by [`abcvoting`](https://github.com/martinlackner/abcvoting), already a dependency here), Skowron's [proportionality degree](https://www.mimuw.edu.pl/~ps219737/papers/proportionality-degree.pdf), or coverage — and these **conflict with each other by construction**, so the choice decides the ranking before a single election is run.

**Verdict:** **the largest genuine gap, and the one nobody else has closed for STAR-PR specifically.** It is also the goal most likely to produce something publishable in the [research-topics companion repo](https://github.com/masiarek/star-voting-research-topics), precisely because the metric question is open rather than settled.

### S5 — Exhaustive search and the counterexample factory

**Success looks like:** *"no 3-candidate, 7-ballot STAR election exhibits a monotonicity failure"* — proved by enumeration, with a witness emitted **as a YAML case file** when one exists.

**Demands:** raw speed, an allocation-free kernel, and symmetry reduction. See [Part 6](#part-6-should-it-be-rust-measured) — this is the only goal on the list where the language choice is load-bearing, and even there it buys less than the ratio suggests.

**Verdict:** the most *interesting* goal, and the one where a result is a finding rather than a chart. Also the one that most needs sizing before it is promised: the frontier is sharp and it is closer than it looks.

### S6 — Interactive simulation on the teaching site

**Success looks like:** a reader drags a candidate across an issue space on a published page and watches the STAR winner change — a live [Yee diagram](../../07_Concepts/topics/spatial_voting_model.md).

**Verdict:** genuinely valuable teaching, and it is **the same capability question as G1 on the kernel page**, with the same amendment: price [Pyodide](https://pyodide.org/) before assuming a second language is required. A Yee diagram is a few thousand tiny elections per frame — which is the *fast* shape, so this and S5 want the same kernel.

### S7 — Learning Rust on a domain with known answers

**Verdict:** entirely legitimate and worth saying out loud if it is the real driver, exactly as [G5](../../07_Concepts/tabulation_engines/rust_kernel_requirements.md) has it. If it is the goal, scope it to **one method and one model**, put it in the [Rust learning library](https://github.com/masiarek/rust-learning-library) rather than here, and let this page's requirements be aspiration rather than specification.

---

# Part 2 — The pipeline every simulator has

Every serious simulator surveyed below has the same four-stage shape, and the clearest statement of it is 19 years old — Warren Smith's [IEVS](https://rangevoting.org/IEVS/IEVS.c), in a comment at the top of a 5,905-line C file:

> Software Architecture: I. voting methods. II. voting strategies. III. ignorance generators. IV. utility generators. […] The information-flow-direction is IV→III→II→I→winners→regrets. […] The idea is to build a "Chinese menu" system which can investigate A\*B\*C\*D kinds of scenarios BUT the effort to write it is only A+B+C+D.

That is the single most important design requirement on this page, and it is the one a script-per-question folder violates by construction. Twelve scripts each hard-wire one path through the menu; a harness makes the four stages independent so that adding a method costs one implementation rather than twelve.

| Stage | What it produces | Where the modelling choices hide |
|---|---|---|
| **IV. Utilities** | a real number per (voter, candidate) | the [electorate model](../../07_Concepts/topics/election_simulation_models.md) — spatial vs statistical, dimensions, clustering, candidate placement |
| **III. Information** | each voter's *perceived* utilities and the public polls | how wrong voters are about their own interests, and how wrong strategists are about the standings |
| **II. Ballots** | one ballot per voter per method | the [encoding rule](../../07_Concepts/topics/simulate_utilities_not_ballots.md#measured-what-stars-scale-rule-costs) (min-max? global scale?), the approval cutoff, truncation, and any strategy |
| **I. Tabulation** | winners, plus the audit trail | tie ladders — the one place two correct implementations legitimately disagree ([the ladders, written down](../../07_Concepts/tabulation_engines/tiebreak_ladders.md)) |
| **Metric** | VSE, Condorcet efficiency, divergence, proportionality | the multi-winner problem from S4, and whether a sincere baseline is printed |

**Stage III is the one most often collapsed into stage II, and it should not be.** IEVS keeps them separate — `AddIgnorance()` perturbs each voter's true utility by Gaussian noise *before* any ballot is written, with two modes: a constant amplitude for everyone, or a stratified one where different voters are differently well-informed. vse-sim instead models ignorance only at the *poll* level (`fuzzyMediaFor`), so its voters know their own preferences perfectly and are merely wrong about who is winning. **These are different claims about people**, and a chart built on one of them cannot be compared to a chart built on the other. A harness should carry both and say which was used.

---

# Part 3 — Requirements

Written as if **S2** were the primary goal, with notes where another goal changes the answer.

## Non-goals — state these first, they do more work

- **NG-1.** The harness does not replace the twelve scripts. They are each a *finished answer to a question* and several are cited by teaching pages; a harness that requires rewriting them has negative value on day one.
- **NG-2.** The harness does not tabulate through the [LH engine's](../../07_Concepts/tabulation_engines/LH_starvote/README.md) CLI. Measured below: process-per-election is ~5 elections/second against ~100,000 for an in-process kernel.
- **NG-3.** The harness does not draw random ballots. Ever. It samples utilities and derives ballots — the [rung-2 rule](../../07_Concepts/topics/simulate_utilities_not_ballots.md), non-negotiable, and the single most common defect in amateur simulators.
- **NG-4.** The harness does not invent electorate models. `prefsampling` and the two [reference scripts](README.md) already define them, cross-checked; a third definition is a drift surface.
- **NG-5.** The harness does not produce a number without the model beside it. See FR-9.

## Functional requirements

| # | Requirement | Priority | Note |
|---|---|---|---|
| FR-1 | Tabulate the six methods on one shared electorate: STAR, Bloc STAR, STAR-PR (allocated / SSS / RRV), Ranked Robin, Approval, RCV-IRV | must | the point of the exercise |
| FR-2 | The preference primitive is **utility**; every ballot is derived, never drawn | must | NG-3 |
| FR-3 | The utility→ballot **encoding rule is a parameter**, not a constant | must | measured to move the STAR winner [6.8%–27.2%](../../07_Concepts/topics/simulate_utilities_not_ballots.md#measured-what-stars-scale-rule-costs) depending on the space |
| FR-4 | The Approval **cutoff is swept**, not fixed | must | Approval has no canonical sincere conversion; the divergence rate moves [10%→40%](../../method_comparisons/star_vs_approval_divergence.md) non-monotonically with it |
| FR-5 | Ties are reported as ties, and any tiebreak used is **named in the output** | must | "never let an arbitrary tiebreaker silently inflate a result" — this folder's own standing rule |
| FR-6 | Every strategic number is printed **beside its sincere baseline** | must | [the merged-number failure](../../07_Concepts/topics/compliance_vs_strategic_preservation.md), which makes Plurality tie Ranked Robin |
| FR-7 | Output is **self-describing**: model, parameters, seed, method set, election count, and the code version, in the file | must | vse-sim's CSV header does this and it is the best thing about it |
| FR-8 | Report a **confidence interval**, not just a mean | must | the omission in almost every published VSE chart; the per-election rows make it free |
| FR-9 | Voter-ignorance and polling are **separate, independently settable stages** | should | Part 2 |
| FR-10 | A multi-winner run states **which** proportionality/welfare metric it used | must (S4) | they conflict; the choice is the experiment |
| FR-11 | Emit a discovered counterexample as a valid YAML case file | must (S5) | a finding that does not land in the case library is a finding that evaporates |
| FR-12 | Cross-check every method against an independent implementation on a sample of runs | should | the house method; `pref_voting`, `abcvoting`, `starvote` |

## Non-functional requirements

| # | Requirement | Rationale |
|---|---|---|
| NFR-1 | **Deterministic given a seed, and the seed is in the output** | a simulation that cannot be re-run is not evidence |
| NFR-2 | **Seeding is verified, not assumed** | `prefsampling` 0.1.24 silently degenerates when seeded — [filed](../../07_Concepts/about_this_repo/upstream_bug_reports.md), and it is *this repo's own* bug report, so the failure mode is not hypothetical |
| NFR-3 | Arithmetic policy for the PR family is stated and uniform | see [Part 5's arithmetic lesson](#what-the-stv-implementations-know-that-the-simulators-do-not) — floats make the result depend on ballot order |
| NFR-4 | A control method is present in every comparison | Ranked Robin must read 100.0% Condorcet efficiency; any other value means the harness is broken, and [the existing script prints it for exactly that reason](condorcet_efficiency_simulation.py) |
| NFR-5 | Any bound on coverage — top-N, sampled encodings, truncated sweeps — is **logged**, not silent | silent truncation reads as "we covered everything" |
| NFR-6 | Reproduction commands are **executed by a test** | the [vse-sim reproduction gap](../../07_Concepts/about_this_repo/vse_sim_reproduction_gap.md): a documented command no test runs is not a command |

## What each of the six methods specifically demands

| Method | Ballot from utilities | The awkward part |
|---|---|---|
| **STAR** | per-voter min-max onto 0–5 | the encoding rule (FR-3); the runoff tie ladder |
| **Bloc STAR** | same ballot, N seats, no reweighting | **the metric** — a majority sweep is the expected behaviour, so "it over-represents" needs a number that says by how much against what baseline |
| **STAR-PR** | same ballot; quota or divisor reweighting | fractional weights → NFR-3; and the [count-vs-weight bug](../../STARVote_LH_tabulation_engine/BUG_allocated_count_vs_weight.md) is a live example of a *plausible wrong number* surviving in a published engine |
| **Ranked Robin** | rank by utility | cycles are the interesting case and the spatial models nearly never produce them — [0.15% vs 16.65%](../../07_Concepts/topics/statistical_cultures.md) depending on the model, so a structured-domain-only sweep concludes cycle rules are interchangeable |
| **Approval** | cutoff — **there is no canonical one** | FR-4; the cutoff *is* the experiment, and IEVS (mean-based, coin toss at the mean) and vse-sim (midpoint of range) do not even agree on the default |
| **RCV-IRV** | rank by utility, optionally truncated | elimination order under a tie is a behaviour of a *specific library*, not a property of IRV; and truncation policy decides the exhausted-ballot rate, which is what half the teaching pages are about |

---

# Part 4 — Is the Python VSE library useful?

**Yes, as a specification. No, as a dependency.** Those answers are cleanly separable and it is worth not blurring them.

**As a specification it is close to indispensable**, and this library has already extracted most of that value: the [read-from-source page](../../07_Concepts/topics/vse_sim.md) documents the exact VSE formula, the published run's electorate, what a "strategic voter" is under each chooser, what the strategy actually does per method family, and what the polling model is. Anything built here should adopt its two best habits outright — the self-describing CSV header (FR-7) and the always-computed sincere baseline (FR-6) — and should reuse its formula rather than re-derive one.

**As a dependency it does not fit**, and the reason is method coverage rather than code quality:

| Adam's six | in vse-sim? |
|---|---|
| STAR, single-winner | **partly** — as `Srv(10)`, a **0–10** ballot. The 0–5 STAR ballot is `Srv(5)`, which appears only in a secondary method set, not in the published run |
| Bloc STAR | no |
| STAR-PR (allocated / SSS / RRV) | no |
| Ranked Robin (Copeland) | no |
| Approval | **partly** — the published "Approval" line is `Score(1)`, an *ideal* approver; the realistic variant is tracked separately as `BulletyApproval60` |
| RCV-IRV | yes |

**vse-sim is single-winner only.** Its fourteen method modules — Borda, bullety approval, IRNR, IRV, IRV′, MAV, MJ, Plurality, ranked, Ranked Pairs, Schulze, Score, `Srv`, 3-2-1 — contain no multi-winner rule at all. So it covers **one and a half** of the six, and the two it half-covers are half-covered in the direction that matters: the ballot resolution is wrong for STAR, and the Approval line is a modelled ideal rather than a modelled voter.

Two further practical points. The **licence** is the one people get wrong: `vse-sim` ships a `docs/LICENSE`, but it is the Jekyll theme's MIT licence covering the website scaffolding — the simulator code itself carries **no licence**, which under default copyright means *readable and citable, not vendorable*. And the published-results script currently [does not run](../../07_Concepts/about_this_repo/vse_sim_reproduction_gap.md) at HEAD.

So the honest summary: **read it, cite it, adopt its habits, fix its two-line bug upstream — and do not plan to import it.**

---

# Part 5 — The landscape

Fifteen projects worth knowing, grouped by what they are actually for. Star counts and dates are as of 2026-08-24.

## Simulators (the direct comparables)

| Project | Language | Covers Adam's six? | What it is |
|---|---|---|---|
| **[VMES](https://github.com/ragconsumer/VMES)** — Marcus Ogren | **Julia** | **all six** | The most complete match on this page. `STARVoting(5)` — the **0–5** ballot — plus `RankedRobin`, `blockstar`, `allocatedscore`, `sss`, `seqmonroe`, `rrv`, `spav`, `mes`, `allocatedrankedrobin`, `sntv`, `rcv`. Carries VSE *and* [PVSI](../../07_Concepts/topics/pvsi_strategic_incentive.md), a multi-winner `mw_winner_quality`, free-riding, and eight voter models. Active (last push 2026-08-20) |
| **[vse-sim](https://github.com/electionscience/vse-sim)** — Jameson Quinn | Python | 1.5 of 6 | The canonical one; the published VSE charts are its output. Single-winner only. See [Part 4](#part-4-is-the-python-vse-library-useful) and [the source read-through](../../07_Concepts/topics/vse_sim.md) |
| **[elsim](https://github.com/endolith/elsim)** — "Election Simulator 3000" | Python | ~2 of 6 | MIT, actively pushed, clean three-stage API (elections → strategies → methods). Plurality, runoff, IRV, Hare, Borda, Coombs, Black, Approval, **STAR**. Documents its own throughput — ~25,000 elections/s with optional Numba. Also the source of the animated "core collapse" [center-squeeze](../RCV_IRV/concepts/RCV_IRV_center_squeeze.md) pictures |
| **[votesim / election_sim](https://github.com/johnh865/election_sim)** | Python | ~3 of 6 | MIT; scored methods, Condorcet (Smith-minimax, ranked pairs), IRV, and multi-winner **reweighted range, Sequential Monroe, STV**. Last push 2022 |
| **[IEVS](https://rangevoting.org/IEVS/IEVS.c)** — Warren D. Smith, 2007 | **C** | ~3 of 6 | 5,905 lines, **68 voting methods**, 11 utility generators, capped at 32 candidates and 2,048 voters. Bayesian regret, Yee diagrams, and a **"reality-based" utility generator built from Tideman's real-world election collection**. The four-stage architecture in [Part 2](#part-2-the-pipeline-every-simulator-has) is its comment block. Licence: non-commercial with acknowledgement — *not* open source |
| **[quadelect](https://github.com/kristomu/quadelect)** — Kristofer Munsterhjelm | **C++** | ~2 of 6 | Not a VSE tool — a **method-discovery** tool, and the most methodologically interesting project here. Uses **lil'UCB best-arm identification** (`src/bandit/`) to spend simulation effort adaptively on the methods still in contention, and **linear programming** (glpk, `src/linear_model/constraints/relative_criteria/`) to *solve for* criterion counterexamples rather than sample for them. Has `monotonator`, `find_distinguisher`, `test_vse_bandit`, `multiwinner_spatial`. Active |
| **[kingmaker](https://crates.io/crates/kingmaker)** | **Rust** | ~1 of 6 | "A modular, performant, social choice framework for the simulation, computation, and analysis of strategic voting." Mallows preferences, tactics (burial, compromise) with probability weights, builder-pattern blocs. v0.1.0, ~600 downloads, last updated 2025-05 — **the only Rust simulator found, and it is a seedling** |
| **[elect](https://github.com/fresheneesz/elect)** | JavaScript | ~2 of 6 | Bayesian regret for **multi-winner**, via a genuinely different welfare model: voters are points on issues, candidates become "dictators" implementing their platform, and regret is measured over the resulting policies. Worth knowing because it is one answer to S4's open metric question |
| **[electionsim](https://github.com/revmen/electionsim)** | Go | ~1 of 6 | Single-winner utility efficiency with random candidates and voters. Small, last push 2019 |
| **[votingMethods / voteSim](https://github.com/Naghan1132/votingMethods)** | R | ~1 of 6 | An R package for testing methods on a generated simulation. Small |

## Infrastructure this repo already uses (or should)

| Project | Language | What it supplies |
|---|---|---|
| **[prefsampling](https://github.com/COMSOC-Community/prefsampling)** | Python | The profile and Euclidean samplers, already a dependency — with a [seeding bug this repo filed](../../07_Concepts/about_this_repo/upstream_bug_reports.md) that is the reason NFR-2 exists |
| **[pref_voting](https://pref-voting.readthedocs.io/)** | Python | The [independent cross-check](../../07_Concepts/tabulation_engines/cross_checking_with_pref_voting.md) — Copeland, Minimax, Coombs, the grade methods |
| **[abcvoting](https://github.com/martinlackner/abcvoting)** | Python | Multi-winner approval rules **and the JR/PJR/EJR checks** — which is the S4 metric machinery, already installed |
| **[mapof-elections](https://science-for-democracy.github.io/mapof-elections/)** (mapel) | Python | The academic framework: embeds whole elections as points in a 2-D similarity space so a *dataset* of electorates can be characterized rather than a single model asserted. Faliszewski, Szufa et al. |

## What the STV implementations know that the simulators do not

Two Rust projects that are **tabulators, not simulators** — and both answer a requirements question the simulators leave open.

**[stv-rs](https://github.com/gendx/stv-rs)** implements Meek STV under **five** distinct arithmetic modes: `fixed9`, `bigfixed9`, `float64`, `exact` rationals, and `approx`. Its README states the two findings that matter: **`float64` makes the result depend on the order of the ballots**, and `exact` makes "algorithm complexity explode" so it is impractical at scale. It also notes that **parallelization requires associative and commutative arithmetic, which excludes `float64`** — so the arithmetic choice and the concurrency design are the same decision, not two.

**[ConcreteSTV](https://github.com/AndrewConway/ConcreteSTV)** reproduces the counts of actual Australian jurisdictions, *including deliberately emulating the electoral commissions' known bugs*, and has found and helped fix real errors in ACT, NSW and federal Senate counts. Its epistemics are the part to steal: matching an official result is, in its own words, "only very weak evidence" of correctness, because the program may contain the same bug. And on ties it supports exactly two responsible options — a public draw with an explicit `--tie` order, or a PRNG with a **published seed** — which is NFR-1 stated as product design.

That is the same conclusion this repo reached from the other direction with its own [published `lot_numbers:`](../../07_Concepts/tabulation_engines/tiebreak_ladders.md).

## What they assume — the assumptions worth knowing before quoting any of them

| Assumption | vse-sim | IEVS | elsim | this repo's scripts |
|---|---|---|---|---|
| Electorate | hierarchical clusters, **40 voters, 6 candidates** | 11 generators incl. real-election-derived | IC, spatial, normal | six Euclidean spaces + statistical cultures |
| Honest score ballot | per-voter min–max | per-voter min–max | configurable | per-voter min–max |
| Honest approval cutoff | **midpoint of range** | **mean, coin toss at the mean** | configurable | swept, `>= 4` default |
| Voter self-knowledge | perfect (ignorance is at poll level only) | **imperfect** — `AddIgnorance`, constant or stratified | n/a | perfect |
| Strategists | independent coin flips, **not a coalition** | fraction of voters, one strategy | n/a | modelled explicitly per script |
| Strategy fractions | **0/25/50/75/100 only** | parameterized | n/a | per script |
| Ties | `random.choice` | varies | varies | reported, never silently broken |
| Confidence intervals | computable, **never printed** | summarizer | — | per script |

**The two rows to stare at are the approval cutoff and voter self-knowledge**, because both are silent modelling choices that no chart label mentions and both move results. Two simulators disagreeing about what a sincere Approval ballot *is* will produce two different "Approval" lines from identical electorates, and neither is wrong.

## What questions they posed

Worth reading as a list, because the questions are more transferable than the code:

- **vse-sim / Quinn:** *how much of the achievable voter satisfaction does each method deliver, and how much does strategy take away?* — with the answer expressed on a normalized 0–1 scale anchored at "random winner" and "best possible winner."
- **IEVS / Smith:** *the same question, but across 68 methods and 11 electorates at once* — the "Chinese menu," built so the comparison space is A×B×C×D for A+B+C+D of work.
- **quadelect / Munsterhjelm:** *not "which of these methods is best" but "what is the best method in this space?"* — searching over composed methods, and proving criterion failures by LP rather than finding them by sampling.
- **elsim / endolith:** *what do the classic results actually look like when re-run?* — reproduction and visualization as the goal, which is why it produced the center-squeeze animation.
- **VMES / Ogren:** *what is the strategic incentive under each method* ([PVSI](../../01_STAR/01_Learn/reference/wolk_quinn_ogren_2023.md)), *and how do the multi-winner variants compare* — the only one on this list asking both.
- **mapof / Faliszewski et al.:** *is the electorate model even the right unit of analysis?* — replacing "assume IC" with a map of where real and synthetic elections sit relative to each other.
- **ConcreteSTV / Conway:** *does the official count match the law?* — the only one whose findings changed legislation.

This library's own question is a seventh, and it is not on that list: **how does one election look under every method at once** — the [same-opinion line-up](../../07_Concepts/topics/same_opinions_every_method.md). That is a *case* question, not a *rate* question, and it is why twelve scripts exist here rather than one simulator.

---

# Part 6 — Should it be Rust? Measured

The [kernel pages](../../07_Concepts/tabulation_engines/rust_kernel_requirements.md) answered **no** for the counter, on the grounds that a test library's dominant cost is authoring. A simulator's dominant cost is running, so the argument has to be re-made rather than inherited — and this repo's rule is to measure rather than assert.

**Setup.** Identical minimal STAR kernel — sum the scores, take the top two, run the pairwise runoff — written once in Rust and once in Python, with ballot generation inside the timed loop in both. Intel Core i5-10500 @ 3.10 GHz, rustc 1.97.1 (`opt-level=3`, LTO, `codegen-units=1`), CPython 3.13.13, numpy 2.2.6. Single core throughout. The Rust source is at the bottom of this section so the numbers can be re-run.

### Workload A — Monte-Carlo sampling (5 candidates, 501 voters)

| Implementation | elections/s/core | vs pure Python |
|---|---|---|
| pure Python | 1,227 | 1× |
| **numpy, one election at a time** | 27,323 | 22× |
| **numpy, batched across elections** | 66,049 | 54× |
| **Rust** | **191,100** | 156× |
| *(`starvote.election`, the real engine, 5 cands / 501 voters)* | *348* | *0.3×* |

**Rust beats well-written numpy by 2.9×.** That is the whole margin, and it is not a reason to change language — because numpy is already vectorizing across the 501 voters, which is where the work is.

### Workload B — exhaustive enumeration (3 candidates, 7 ballots)

| Implementation | elections/s/core | vs pure Python |
|---|---|---|
| pure Python | 110,538 | 1× |
| **Rust, runtime dimensions (`Vec`)** | 9,838,000 | 89× |
| **Rust, compile-time dimensions (fixed arrays)** | **26,260,000** | **238×** |
| *(`starvote.election`, same shape)* | *15,423* | *0.14×* |

**Rust beats Python by 238×** — and note that the fixed-size version is 2.7× the `Vec` version, which is a design requirement in its own right: the inner loop must not allocate, and the dimensions want to be compile-time constants or const generics.

### The finding: the case for Rust runs opposite to intuition

Big electorates favour Python, because numpy vectorizes across voters and there is real work per election to amortize the interpreter over. Tiny electorates in enormous numbers favour Rust, because per-election overhead is *all* there is and numpy's vectorization has nothing to bite on. **The simulator Adam described — sampling realistic electorates — is workload A.** The 238× number belongs to a different program.

### And even for workload B, speed buys less than it looks

There are 4,792,382,636,184 distinct anonymous STAR profiles at 3 candidates, 7 ballots, scores 0–5. At the measured rates:

| | Python | Rust |
|---|---|---|
| 3 candidates, **7** ballots (4.79 × 10¹²) | 1.4 core-years | **2.1 core-days** — about 6 hours on 8 cores, **~1 hour** with the `m! = 6` candidate-relabelling symmetry |
| 3 candidates, **9** ballots (3.33 × 10¹⁵) | 953 core-years | 4.0 core-years — ~4 months on 12 cores |

So Rust genuinely converts "impossible" into "an afternoon" at 7 ballots. But the profile count grows by **~26× per additional voter**, so a 238× speedup buys **fewer than two extra voters**. Constant factors do not defeat combinatorial explosion. What does is symmetry reduction (a free 6× here), and what quadelect does instead: **solve for counterexamples with linear programming rather than search for them.** If S5 is the goal, the LP approach is worth more than the language.

**And the shape matters as much as the size.** The same enumeration for *ranked* ballots is trivial — 792 profiles at 3 candidates and 7 voters, against 4.79 trillion for score ballots, because a ranked ballot has 6 possible values and a 0–5 score ballot has 216. Exhaustive search over ranked methods needs no Rust at all; it is the score ballot that explodes.

<details>
<summary>The benchmark source (re-runnable)</summary>

```rust
// Minimal STAR kernel: 3 candidates, 7 ballots, scores 0-5.
const M: usize = 3;
const N: usize = 7;

#[inline(always)]
fn star_winner(b: &[[u8; M]; N]) -> usize {
    let mut tot = [0u32; M];                       // scoring round
    for row in b.iter() { for c in 0..M { tot[c] += row[c] as u32; } }
    let mut a = 0usize;                            // top two
    for c in 1..M { if tot[c] > tot[a] { a = c; } }
    let mut d = if a == 0 { 1 } else { 0 };
    for c in 0..M { if c != a && tot[c] > tot[d] { d = c; } }
    let (mut pa, mut pd) = (0u32, 0u32);           // automatic runoff
    for row in b.iter() {
        if row[a] > row[d] { pa += 1 } else if row[d] > row[a] { pd += 1 }
    }
    if pa > pd { a } else if pd > pa { d } else if tot[a] >= tot[d] { a } else { d }
}
```

Build with `opt-level = 3`, `lto = true`, `codegen-units = 1`; drive it with a splitmix64 stream inside the timed loop and accumulate the winner into a sink so nothing is optimized away. The Python comparison is the same algorithm transliterated, and the numpy comparison replaces the two loops with `sum(axis=0)` and a boolean count. **Note the tie rule in the last line is a placeholder** — a real kernel resolves it on the [published ladder](../../07_Concepts/tabulation_engines/tiebreak_ladders.md), and that is exactly the part a benchmark is entitled to skip and a simulator is not.

</details>

---

# Part 7 — Recommendation

**1. Fix vse-sim's reproduction script upstream.** Two lines, already verified end-to-end, and it closes S1 without writing anything. It also puts a filed-and-fixed contribution against the canonical simulator on the record, which is worth more than a private fork. Details and the patch: [a reproduction command nobody runs](../../07_Concepts/about_this_repo/vse_sim_reproduction_gap.md).

**2. Evaluate VMES before building anything.** It is the only project on this page that covers all six methods, its `STARVoting(5)` is the *right ballot*, it carries PVSI and a multi-winner quality metric, it is actively maintained, and it is written by a co-author of the [paper this library already claim-checks](../../01_STAR/01_Learn/reference/wolk_quinn_ogren_2023.md). The honest first question is not "what language should our simulator be?" but **"why is this not our simulator?"** — and the answer might legitimately be *Julia is a third language in a two-language repo*, or *its documentation is a Google Doc*, or *we want an independent implementation precisely so the numbers can disagree*. Any of those is a fine answer. None of them can be given before someone runs it.

**3. If something is built here, build it in Python, as a harness rather than a simulator.** Workload A is 2.9× off Rust and the twelve scripts already contain most of the pieces. The valuable move is the "Chinese menu" refactor from [Part 2](#part-2-the-pipeline-every-simulator-has): four independent stages, so that adding Bloc STAR costs one implementation rather than twelve. That work is worth doing whatever happens next, which is the [ladder principle](../../07_Concepts/tabulation_engines/rust_kernel_requirements.md) — order the work so that stopping is never a loss.

**4. The one place Rust earns its keep is S5, and only for score ballots.** 238×, measured, converting a 1.4-core-year enumeration into an afternoon. If that is the goal, scope it to *exactly* that: no models, no strategy, no metrics, no CLI — an enumerator, one method, an allocation-free kernel with compile-time dimensions, and a YAML emitter for the witness. That is a few hundred lines, it is a genuinely good Rust learning project, and it produces a publishable result rather than a chart. But read [Part 6's last paragraph](#and-even-for-workload-b-speed-buys-less-than-it-looks) first: linear programming may beat brute force by more than Rust beats Python.

**5. The multi-winner metric question (S4) is a page before it is a program.** Which welfare measure for Bloc STAR and STAR-PR, and why — with the conflict between proportionality and utilitarian welfare stated rather than resolved by default. That page is worth writing whether or not any simulator follows it, and it is the piece that is missing from every project surveyed here.

---

## Open questions

| # | Question | Leaning |
|---|---|---|
| Q-1 | Does VMES already do this, well enough? | **Unknown, and answerable in an afternoon.** Blocks everything else |
| Q-2 | Primary goal — S2 (measure our own claims) or S4 (multi-winner) or S5 (search)? | S2 as the default; S4 as the one with a publishable gap |
| Q-3 | Which multi-winner welfare metric? | State the conflict; report at least two |
| Q-4 | Rationals or floats in the PR family? | [stv-rs's answer](#what-the-stv-implementations-know-that-the-simulators-do-not): floats make results ballot-order-dependent and block parallel reduction. Fixed-point is the middle road |
| Q-5 | Does the harness call `starvote`, or reimplement? | Reimplement for speed, **cross-check against `starvote` on a sample** (FR-12). Calling it is 350 elections/s |
| Q-6 | One harness, or keep twelve scripts? | Keep the scripts; extract the four stages beneath them (NG-1) |
| Q-7 | Is any of this promised publicly before it exists? | No |

---

## Related

- [The simulations folder](README.md) — the twelve scripts, what each measures, and the findings
- [vse-sim, read from source](../../07_Concepts/topics/vse_sim.md) · [a reproduction command nobody runs](../../07_Concepts/about_this_repo/vse_sim_reproduction_gap.md) — the canonical simulator, and its live bug
- [Election simulation models](../../07_Concepts/topics/election_simulation_models.md) · [Simulate utilities, not ballots](../../07_Concepts/topics/simulate_utilities_not_ballots.md) · [The six Euclidean spaces](../../07_Concepts/topics/euclidean_spaces.md) · [Statistical cultures](../../07_Concepts/topics/statistical_cultures.md) — the modelling layer, already built and cross-checked
- [A Rust voting kernel — goals and requirements](../../07_Concepts/tabulation_engines/rust_kernel_requirements.md) · [A Rust tabulation kernel — scope](../../07_Concepts/tabulation_engines/rust_kernel_scope.md) — the same question for the *counter*, decided **no**
- [The result contract](../../07_Concepts/tabulation_engines/result_schema.md) · [Tiebreak ladders](../../07_Concepts/tabulation_engines/tiebreak_ladders.md) — what a second implementation has to match
- [Formal compliance vs. strategic preservation](../../07_Concepts/topics/compliance_vs_strategic_preservation.md) · [PVSI](../../07_Concepts/topics/pvsi_strategic_incentive.md) · [Condorcet efficiency, measured](../../07_Concepts/topics/condorcet/condorcet_efficiency_measured.md) — this library's existing measured results

*Up: [Simulations](README.md) · [06_Other](../README.md).*
