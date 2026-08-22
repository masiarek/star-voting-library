---
tags:
  - foundations
  - simulation
---

# Statistical cultures — the named recipes for generating a random election

*A simulation study never says "we generated random elections." It says "impartial culture," or "urn with α = 0.1," or "norm-Mallows φ = 0.5" — a **name** and a **number**, both load-bearing, and neither usually explained. This page says what the names mean, what the numbers do, and which three of them are quoted wrongly often enough to be worth a warning. As with [the six Euclidean spaces](euclidean_spaces.md), everything here is measured rather than asserted: a companion script runs each culture and checks its output against values that are known exactly in advance.*

**Level: 201 → 301 · deep dive** Companion: [Election simulation models](election_simulation_models.md) (the conceptual menu, and the standing caveat) · [The six Euclidean spaces](euclidean_spaces.md) (the spatial family in close-up) · [Simulate utilities, not ballots](simulate_utilities_not_ballots.md) (why you sample preferences at all).

## What the word means

A **statistical culture** is a probability distribution over whole preference profiles — a named recipe that rolls an entire synthetic electorate at once, rather than one voter at a time.

The word is historical, not descriptive. It comes from **[Impartial Culture](https://en.wikipedia.org/wiki/Impartial_culture)** (Guilbaud 1952; Garman & Kamien 1968), where a "culture" meant the shared opinion-generating process an electorate's voters were imagined to draw from. It has nothing to do with culture in the ordinary sense, and a reader meeting it cold can be forgiven for expecting it to.

The distinction that makes the term worth having is that a culture is a distribution over **profiles**, not over voters. Some cultures — impartial culture, Mallows, Plackett-Luce — do generate each voter independently, so the profile distribution is just the voter distribution repeated. Others do not: [the urn model's](#the-urn-model-and-the-identity-hiding-in-it) whole mechanism is that voter *n* depends on voters 1…*n−1*. Any statistic whose derivation assumes independent voters is simply invalid on urn output, and the fact that a culture is allowed to correlate its voters is exactly why the family needs a name of its own.

## Every dial runs between the same two poles

The zoo is smaller than it looks. Almost no culture is a single distribution — each is a *family* with a parameter, and the parameter nearly always controls **how correlated the voters are with each other**, running between the same two ends:

- **unanimity** — every voter casts the same ballot, zero disagreement
- **independent and uniform** — which *is* Impartial Culture

So IC is not one culture among many so much as **the place the others land when the dial is turned all the way up**. Mallows at φ = 1 is IC. The urn at α = 0 is IC. Stratification with one empty class is IC. Once you see that, a parameter table stops being a list of unrelated magic numbers and becomes one axis with several routes along it.

## The menu, and what each parameter does

The samplers below are [`prefsampling`](https://github.com/COMSOC-Community/prefsampling)'s, which is the layer [`pref_voting`](https://pref-voting.readthedocs.io/) calls when you ask it for a random profile — so these are the names and arguments that actually appear in code, not just in papers.

| Culture | Parameter | What the dial does | Endpoints |
|---|---|---|---|
| `impartial` (IC) | — | — | the reference point itself |
| `impartial_anonymous` (IAC) | — | — | uniform over *tallies*, not labelled profiles |
| `urn` | `alpha ≥ 0` | contagion: `alpha × m!` copies of each drawn vote go back in the urn | `0` = IC · `1/m!` = IAC |
| `mallows` | `phi ∈ [0,1]` | decay per swap: `P(v) ∝ φ^(Kendall-tau distance from a central ranking)` | `0` = unanimity · `1` = IC |
| `norm_mallows` | `norm_phi ∈ [0,1]` | the same, rescaled so it means one thing at every candidate count | same poles |
| `plackett_luce` | one strength per candidate | candidate quality: `P(A first) = γ_A / Σγ` | all equal = IC |
| `stratification` | `weight ∈ [0,1]` | size of an upper class every voter ranks above the lower | `0` or `1` = IC |
| `single_peaked_conitzer` / `_walsh` | optional `axis` | restricts to a single-peaked domain | — |
| `single_crossing`, `group_separable` | — / tree shape | other structured domains | — |
| `euclidean` | dimensions + a *space* | geometry — [the six spaces](euclidean_spaces.md) | — |

Values you will actually meet in the literature: `urn` α between 0.05 and 0.5 (the effect saturates fast, as the table below shows), `norm_phi` at quarters, and Euclidean models in one to three dimensions.

## Measured

Each culture run 2,000 times, and two things counted. **`disagree`** is the mean share of candidate pairs that two randomly chosen ballots order differently — 0 is unanimity, 0.5 is independent uniform ballots. **`no CW`** is how often the election has no [Condorcet winner](condorcet/README.md).

```text title="python 06_Other/simulations/statistical_cultures.py — 2,000 elections, 51 voters, 4 candidates, seed 42"
culture                          what the dial does                disagree   no CW
------------------------------------------------------------------------------------
impartial (IC)                   every ranking equally likely         0.500  16.65%
impartial_anonymous (IAC)        every TALLY equally likely           0.480  16.75%
urn alpha=0                      = IC exactly                         0.500  16.60%
urn alpha=1/m! (0.0417)          = IAC exactly                        0.480  16.75%
urn alpha=0.1                    the rich get richer                  0.454  15.10%
urn alpha=0.5                    the rich get richer                  0.336   6.20%
urn alpha=1.0                    the rich get richer                  0.252   3.40%
norm_mallows phi=1.0             noise around one ranking             0.500  17.85%
norm_mallows phi=0.75            noise around one ranking             0.465   0.80%
norm_mallows phi=0.5             noise around one ranking             0.365   0.00%
norm_mallows phi=0.25            noise around one ranking             0.211   0.00%
norm_mallows phi=0.0             noise around one ranking             0.000   0.00%
plackett_luce equal              equal candidate strengths            0.500  16.50%
plackett_luce skewed             strengths 1, 2, 4, 8 ...             0.361   0.00%
stratification w=0.0             upper class ranked above lower       0.500  16.65%
stratification w=0.5             upper class ranked above lower       0.167   0.00%
single_peaked_conitzer           peak uniform, then spread            0.447   0.00%
single_peaked_walsh              same domain, other distribution      0.365   0.00%
single_crossing                  voters ordered on one axis           0.381   0.00%
group_separable                  nested blocs (Schroeder tree)        0.500   0.00%
euclidean gaussian_ball          spatial, clustered centre            0.423   1.05%
euclidean uniform_cube           spatial, corners included            0.434   1.00%
```

The `disagree` column is where the "one dial" claim stops being rhetoric: read down the urn block, or down the Mallows block, and you can watch the same electorate being tuned from independent (0.500) toward unanimous (0.000). The endpoint identities land exactly where they should — `urn alpha=0` reproduces IC's 0.500 and `urn alpha=1/m!` reproduces IAC's 0.480, to three decimals.

### Finding 1 — Impartial Culture is a knife-edge

Compare the top row with `norm_mallows phi=0.75`. Disagreement barely moves: **0.500 → 0.465**, a 7% drop that no eyeball would notice in a ballot set. The Condorcet-cycle rate moves from **16.65% to 0.80%** — a 95% collapse.

That ratio is the single most useful thing on this page. It means the famous IC paradox rates are not a description of "elections where voters disagree a lot"; they are a description of **one exact point** — perfect independence — that a real electorate misses by a mile. Voters who are correlated even slightly, by a shared media diet or a common left-right axis or simple social contact, are already in the 0.8% world, not the 16.65% one. It also means a study that reports paradox rates without naming its culture has told you almost nothing, because the number is hypersensitive in a range where the electorates all look alike.

This is the measured version of what the [simulation-model page](election_simulation_models.md#the-standing-caveat-results-are-conditional-on-the-model) says in the abstract, and it lines up with the sweep in [how often do Condorcet methods tie?](ties/how_often_condorcet_methods_tie.md#the-realistic-electorate-answer-it-rarely-matters-at-all) — 8.68% under IC against 0.15% under a spatial model at three candidates.

### Finding 2 — the same disagreement, opposite structure

Now compare `impartial (IC)` with `group_separable`. Both score **0.500** on disagreement: by that measure the two electorates are indistinguishable, as internally divided as an electorate can be. Yet IC produces no Condorcet winner 16.65% of the time and group-separable produces one **always**.

So disagreement does not cause cycles. **Structure does** — or rather, the absence of it. A group-separable electorate is one whose candidates fall into nested blocs that every voter treats as blocs, and that restriction rules cycles out no matter how fiercely voters disagree inside it. The same holds for the single-peaked and single-crossing rows: all of them are 0.00%, at disagreement levels from 0.365 to 0.447.

The practical consequence is that **"how divided is the electorate" and "how hard is this election to count" are different questions**, and a summary statistic answering the first tells you nothing about the second. It also explains why the structured domains are worth having in a sampler at all: they are the models that make [cycle-resolution machinery](../../05_Ranked_Robin/01_Learn/cycle_resolution.md) look permanently unnecessary, which is a good reason never to sweep on them alone.

## Three traps

### Raw `phi` cannot be quoted across candidate counts

Mallows decays per *swap*, but the number of available swaps grows as `m(m−1)/2`. A fixed per-swap penalty therefore bites harder and harder in relative terms, and the same φ drifts steadily toward unanimity as candidates are added:

```text title="python 06_Other/simulations/statistical_cultures.py --normalise"
  m  max Kendall-tau   raw phi=0.5   norm_phi=0.5
----------------------------------------------------
  3                3         0.417          0.370
  4                6         0.388          0.366
  5               10         0.360          0.362
  7               21         0.306          0.356
 10               45         0.245          0.352
```

Raw φ = 0.5 loses **41%** of its dispersion between 3 and 10 candidates; normalised φ = 0.5 loses 5%. `norm_mallows` exists precisely to pin the expected normalised distance, so **"φ = 0.5" is only meaningful with a candidate count attached, and "norm-φ = 0.5" is the one that travels.** Note which way the drift runs — it is easy to assume a fixed φ gets noisier as the ballot gets longer, and it does the opposite.

### `single_peaked_conitzer` and `single_peaked_walsh` are not two implementations of one thing

They sample the same *domain* — every profile either produces is single-peaked on the axis — but not the same *distribution* over it. Conitzer picks the peak uniformly and then spreads left or right by coin flip; Walsh fills the ballot from worst to best, taking the leftmost or rightmost survivor. Where the peaks land:

```text title="python 06_Other/simulations/statistical_cultures.py --peaks — 20,000 ballots, 7 candidates"
sampler                       0      1      2      3      4      5      6
-------------------------------------------------------------------------
single_peaked_conitzer    0.143  0.143  0.144  0.143  0.143  0.144  0.140
single_peaked_walsh       0.015  0.094  0.239  0.312  0.230  0.094  0.015
```

Conitzer is flat at 1/7 = 0.143 by construction. Walsh puts **twenty times** more voters at the centre of the axis than at either end — an electorate of moderates, where Conitzer's is an electorate spread evenly across the spectrum. Those are different political assumptions wearing the same label, so "single-peaked" without a sampler name is underspecified.

### The urn model, and the identity hiding in it

Two things about `urn`, both easy to miss.

First, **α = 1/m! is exactly IAC**. Adding `alpha × m!` copies back means adding exactly one copy — the Pólya urn that produces a uniform distribution over anonymous tallies. This is not an approximation or a coincidence: `prefsampling` *implements* `impartial_anonymous` as `return urn(alpha=1/m!)`. So IC and IAC are not two rival conventions but two settings of one dial, which is the same point the [simulation-model page](election_simulation_models.md#a-correction-worth-flagging) makes when it presents IC, IAC and IANC as one construction under three symmetry groups.

Second, **urn voters are not independent**, and the library's own docstring says so. Vote *n* is drawn from an urn that already contains votes 1…*n−1*. That is the entire mechanism — it is how the model represents social influence without any geometry — but it invalidates any downstream statistic that assumes i.i.d. ballots, including most closed-form confidence intervals.

## Checking the numbers

None of the table above is worth much unless the measuring apparatus is known to work, so the script carries fourteen anchors whose values are fixed before it runs:

```text title="python 06_Other/simulations/statistical_cultures.py --verify"
anchor                                     measured               expected  status
------------------------------------------------------------------------------------
IC disagree (n=5, m=3)                       0.5009        0.5000 +/- 0.01  ok
IC disagree (n=50, m=4)                      0.4997        0.5000 +/- 0.01  ok
IC disagree (n=200, m=8)                     0.5000        0.5000 +/- 0.01  ok
IC no-CW, m=3 (Gehrlein 8.77%)              8.7250%       8.7700% +/- 1.2%  ok
IAC no-CW, m=3 (Gehrlein 6.25%)             6.0500%       6.2500% +/- 1.2%  ok
urn(alpha=0) disagree == IC                  0.5003        0.5002 +/- 0.01  ok
urn(alpha=0) no-CW == IC                   16.4667%      16.4000% +/- 2.0%  ok
tally count (n=3, m=3)                      56.0000          56.0000 +/- 0  ok
urn(alpha=1/m!) uniform over tallies      2.8777 sd   0.0000 sd +/- 4.0 sd  ok
mallows(phi=1) disagree == IC                0.4997        0.5000 +/- 0.02  ok
mallows(phi=0) disagree == 0                 0.0000       0.0000 +/- 1e-09  ok
stratification(w=0.0) disagree == IC         0.4997        0.5000 +/- 0.02  ok
stratification(w=1.0) disagree == IC         0.4997        0.5000 +/- 0.02  ok
ordinal seeding is honest               True / True            True / True  ok

14/14 anchors hold.
```

Three of these are worth reading rather than skimming.

**IC's disagreement is 0.5 exactly, and provably.** If `c` of `n` voters prefer candidate *i* to *j*, then exactly `c(n−c)` voter-pairs disagree about that pair. Under IC, `c` is Binomial(n, ½), and `E[c(n−c)] = n(n−1)/4` — which divided by the `n(n−1)/2` available pairs is **½, for every n and every m**. The measured 0.5000 at 200 voters and 8 candidates is the arithmetic checking itself, the same move the [Euclidean page](euclidean_spaces.md#measured-not-asserted-and-one-surprise) makes with its 25% figure.

**The IAC anchor had to be rebuilt to mean anything.** The obvious check — does `urn(alpha=1/m!)` match `impartial_anonymous`? — compares a function with itself, since the latter is implemented as the former, and could never fail. So the script checks the *definition* instead: it enumerates all 56 anonymous profiles for 3 voters and 3 candidates (the same 56 the [simulation-model page](election_simulation_models.md#a-correction-worth-flagging) counts when it compares IC, IAC and IANC on the smallest interesting election) and confirms the urn spreads uniformly over them, the largest of 56 cells landing 2.88 standard errors out — about where the maximum of 56 draws should sit.

**The ordinal samplers seed honestly.** Worth stating because their Euclidean siblings do not: in `prefsampling` 0.1.24, seeding the Euclidean path collapses `GAUSSIAN_BALL` to a single repeated point and lands candidate *j* exactly on voter *j* ([prefsampling#6](https://github.com/COMSOC-Community/prefsampling/issues/6), [pref_voting#186](https://github.com/voting-tools/pref_voting/issues/186), and [the story](euclidean_spaces.md#the-trap-seeding-these-breaks-them)). The cultures on this page are unaffected — same seed gives the same profile, different seeds give different ones — and the two spatial rows in the main table sidestep the defect by drawing their positions from a generator the script owns.

## So which one should a study use?

The honest answer is the one the [companion page](election_simulation_models.md#the-standing-caveat-results-are-conditional-on-the-model) already gives: there is no neutral choice, so **name the culture and its parameters beside every number.** What this page adds is how much that disclosure is worth — a 7% change in voter disagreement moved the headline paradox rate by a factor of twenty, and two cultures with *identical* disagreement disagreed completely about whether cycles happen at all.

Three practical rules follow:

- **Never sweep on one culture.** A result that holds under IC, an urn, a structured domain and a spatial model is a result; a result from one of them is a property of that model.
- **Never sweep only on structured domains.** Single-peaked, single-crossing and group-separable all report 0.00% cycles, so a sweep confined to them will conclude that cycle-resolution rules are interchangeable — because on those models they are.
- **Treat IC as a stress test, not a prediction.** Beyond the knife-edge problem, it has a harder one: under IC every voting rule has average [distortion](distortion.md) Ω(m) while picking a winner at random achieves ≤ m, so there is provably no skill for a method to display ([Caragiannis & Fehrs 2024](https://arxiv.org/abs/2307.07350), worked through [here](distortion.md#does-averaging-rescue-rankings-not-by-itself)).

## The script

[`06_Other/simulations/statistical_cultures.py`](../../06_Other/simulations/statistical_cultures.py) — every table on this page, reproducible from the seeds shown.

```bash
python 06_Other/simulations/statistical_cultures.py --verify
```

Its companion, for the spatial family: [`euclidean_spaces.py`](../../06_Other/simulations/euclidean_spaces.py) and [the six Euclidean spaces](euclidean_spaces.md).
