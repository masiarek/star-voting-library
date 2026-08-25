---
tags:
  - simulation
  - strategy
---

# vse-sim — the simulator behind the VSE numbers, read from source

*Nearly every "STAR scores 96%" chart in circulation traces back to one Python codebase. It is public, so most of the questions people ask of a VSE chart — which electorate? what counts as a strategic voter? how good are their polls? — do not need to be argued about. They can be looked up. This page looks them up, quotes the source, and then names the few questions the source genuinely cannot answer for you.*

**Level: 301 · deep dive** Read first: [What makes a good winner?](what_makes_a_good_winner.md#measuring-it-empirically-vse-bayesian-regret) (what VSE is) · [Election simulation models](election_simulation_models.md) (the menu of electorates, and the standing caveat) · [Simulate utilities, not ballots](simulate_utilities_not_ballots.md) (why utilities are the primitive). Companion metric: [PVSI](pvsi_strategic_incentive.md). The author: [Jameson Quinn](in_memoriam_jameson_quinn.md).

---

## Where the code is

| Repo | What it is | Licence | State (2026-08-24) |
|---|---|---|---|
| [`electionscience/vse-sim`](https://github.com/electionscience/vse-sim) | **The canonical one.** Quinn's simulator; the published [VSE charts](https://electionscience.github.io/vse-sim/) are its output. | **None on the code** — see below | Python 3.14, uv-locked, `src/vse_sim/` layout, last push 2026-07-17, 62 stars |
| [`endolith/elsim`](https://github.com/endolith/elsim) | Independent Monte-Carlo simulator — "Election Simulator 3000". Computes VSE and other metrics; also the source of the animated ["core collapse"](../../06_Other/RCV_IRV/concepts/RCV_IRV_center_squeeze.md) center-squeeze pictures. | MIT | actively pushed |
| [`johnh865/election_sim`](https://github.com/johnh865/election_sim) | A third VSE-style simulator (scored, Condorcet, IRV, multi-winner). | MIT | last push 2022 |
| [`pref_voting`](https://pref-voting.readthedocs.io/) | Not a VSE project, but ships the profile generators (IC, IAC, Mallows, urn, spatial) any of these models need — and is [already a dependency here](../tabulation_engines/cross_checking_with_pref_voting.md). | MIT | active |

**The licence detail matters and is easy to get wrong.** `vse-sim` has a `docs/LICENSE`, but it is the Jekyll theme's MIT licence (© 2015 Barry Clark) covering the website scaffolding, not the simulator. The code itself carries no licence, which under default copyright means *readable and citable, not vendorable*. That is why this repo reimplemented [3-2-1](../../06_Other/three_two_one/README.md) from the published description instead of copying Quinn's `V321` class.

## The VSE formula, exactly

From `core.py`:

```python
def normalized_vse(utility, best, random_baseline):
    denominator = best - random_baseline
    if isclose(denominator, 0):
        return 0.0
    return (utility - random_baseline) / denominator
```

called with `best = max(utils)` and `rand = mean(utils)`, where `utils` is the electorate's `socUtils`. So:

- **The "random winner" baseline is not a draw** — it is the *mean social utility over the candidates*, which is the expected utility of a uniformly random winner, computed exactly rather than sampled. Cheaper and lower-variance than simulating a coin flip.
- **`socUtils` is the plain mean of raw utilities across voters, per candidate.** No per-voter renormalization happens before the sum, so a voter with a wide utility spread counts for more in the welfare measure than a voter with a narrow one. That is a deliberate, contestable position on interpersonal comparison — the one [cardinal utility](cardinal_utility.md) is about — and it is *not* the same convention as the per-voter min-max used to build the ballots.
- **A utility-tied electorate scores 0.0**, not a division by zero.

## The settings behind the published charts

`scripts/generate_published_results.py` is the whole configuration, in one call:

| Knob | Value | Comment |
|---|---|---|
| electorate model | `KSModel(dcdecay=(1,3), wcdecay=(1.5,3), dccut=.2, wcalpha=1.5)` | "Kitchen sink" — the hierarchical-cluster model: beta-decaying issue clusters, sub-dimensions within each, and per-voter "caring" weights. **Candidates are drawn from the same cluster process as voters** (`nvot + ncand` together), so they look like people, not uniform noise. |
| voters | **40** | Small. Near-ties are common at this size. |
| candidates | **6** | VSE ordering is field-size sensitive; this is the field it was measured on. |
| elections | **15,000** | per method per chooser |
| polling | `fuzzyMediaFor()` | Gaussian noise on the honest standings, σ = **one standard deviation** of those standings. Polls are wrong by default. |
| seed | `"target15000"` | seeds both `random` and `numpy` |
| methods | `allSystems` | `Score(1000/10/2/1)`, `BulletyApprovalWith(.6)`, `Srv(10)`, `Srv(2)`, Plurality, Borda, IRV, IRV′, Schulze, Ranked Pairs, 3-2-1, MAV, MJ, IRNR |

Two things a STAR reader should notice. `Score(1)` is what the code prints as **`IdealApproval`** — so the "Approval" line is a modelled ideal, with the more realistic bullet-voting variant tracked *separately* as `BulletyApproval60`. And the STAR line is **`Srv(10)`**, a 0–10 ballot; the real-world 0–5 STAR ballot is `Srv(5)`, which appears only in the secondary `markMethods` set. A 0–5 vs 0–10 difference is not nothing — this repo has [measured what the scoring rule and resolution do](../../06_Other/simulations/score_encoding_stability.py) to a winner.

## What "a strategic voter" is

Each voter carries **three ballots per method**, memoized onto the voter object: `hon`, `strat`, and `extraStrat`. A *chooser* decides which one gets cast:

- **`ProbChooser([(p, beStrat), (1-p, beHon)])`** — each voter independently flips a weighted coin. This is the mechanism behind any "percent of voters behaving strategically" axis, and note what it is: **a random slice of the whole electorate, not a coordinated bloc.** Strategists drawn at random from every faction partly cancel each other; a disciplined faction does not. The two experiments produce different curves and the axis label cannot tell them apart.
- **`OssChooser`** — *one-sided strategy*: voters who prefer the honest winner stay honest, and only those who prefer the strategic target defect. This is the closer analogue of a real attack.
- **`LazyChooser`** — honest when honest and strategic ballots coincide, extra-strategic otherwise.

**The fractions the published run actually simulates are 0%, 25%, 50%, 75%, 100%** (`baseRuns`), plus the one-sided variants — five points, not a continuous sweep. A chart plotting an 11-point 0–100 grid is either a custom sweep or not this simulator; worth asking which.

A voter is only counted as strategic if the defection is in their interest at all: `isStrat = stratGap > 0`, where `stratGap = utility(target) − utility(frontrunner)`.

**Who the target is differs by method.** `stratTarget2` aims at the poll runner-up; `stratTarget3` aims at *third place*, on the reasoning that under a runoff or elimination rule "second place is pointless (can't change pairwise)". IRV, STAR (`Srv`), 3-2-1 and IRNR use the third-place target; everything else uses the runner-up.

## What the strategy *is*, per family

This is the part most often assumed rather than checked, and the two families do genuinely different things.

**Ranked methods** (Plurality, Borda, Schulze, Ranked Pairs, IRV) — `ranked.py`: the target goes to the **top** rank and the frontrunner to the **bottom**, with everyone else filled in around them. That is compromise and [burial](burial/README.md) in a single move, and it is the attack a Condorcet method is most exposed to. IRV gets a bespoke version that reorders around the frontrunner rather than a flat bury — so **IRV strategy is implemented**, which matters when reading a chart where IRV's line does not move.

**Score and Approval** — `score.py`: the ballot is **linearly rescaled between the two poll leaders' utilities and clamped**, not bullet-voted:

```python
strat = [max(0, min(cls.topRank, floor(
            (cls.topRank + .99) * (util - cuts[1]) / (cuts[0] - cuts[1])
        ))) for util in voter]
```

Its own doctest shows the consequence: a voter with utilities `[5,6,7]` and polls ranking candidate 1 in the middle casts `[0, 5.0, 10]` — a middle candidate keeps a middle score. So **a fully strategic Score electorate does not collapse onto Approval** under this model. If you expected it to (a reasonable expectation — max/min exaggeration is the usual textbook Score strategy), the source is telling you the model is gentler than that, and the Score line should be read accordingly.

**The honest ballots** are worth knowing too: `honBallot` is **per-voter min–max onto 0..topRank** — `floor((topRank + .99) × (u − min) / (max − min))` — the same rule this repo's own simulations use, and not the global-scale alternative that [changes the answer](simulate_utilities_not_ballots.md#measured-what-stars-scale-rule-costs). At `topRank = 1` that rule makes honest Approval "approve everyone in the upper half of my own utility range" — a midpoint-of-range cutoff, which is one of several defensible cutoffs and the one the "Approval" line is built on.

## The polling model is a knob, and it is noisy by default

Strategy is computed from `polls = media(honest_results)`, so "how much do strategists know?" is a first-class parameter:

| Media model | What strategists see |
|---|---|
| `truth` | the honest result exactly — perfect information |
| `topNMediaFor(n)` | only the top *n* are distinguishable; everyone else is flattened to last |
| `fuzzyMediaFor(σ)` | Gaussian noise on every standing (**the published default**, σ = 1 SD) |
| `biasedMediaFor` / `skewedMediaFor` | systematic distortion against trailing candidates |

The fuzzy and biased models also tally `changed` — how often the noise reordered the top two — so the simulator already measures how often its own strategists are aiming at the wrong target. Any claim of the form "method X only looks bad because you gave its voters better polls than the others" is testable here in one line, and should be tested symmetrically rather than for one method.

## What it gives you for free: the sincere baseline

`multiResults` always runs **honest, fully strategic, one-sided, and "smart one-sided"** before any caller-supplied choosers. The honest column is not optional — it falls out of every run.

That matters because the single most common defect in strategy charts is [reporting the strategic number without its sincere baseline](compliance_vs_strategic_preservation.md), which merges "this method is bad on honest ballots" with "this method was successfully attacked" into one indistinguishable column. With this codebase, omitting the baseline takes deliberate effort.

## What it does not do

- **Coalitions.** Strategists are independent coin flips, so nothing reports *how large* a successful attacking bloc had to be — the fifth question on the [checklist](compliance_vs_strategic_preservation.md#what-to-ask-of-any-study-of-this-shape).
- **Defenders.** One side strategizes; the honest side never counter-strategizes.
- **More than one strategy per method.** Each method has one `fillStratBallot`. Push-over, truncation, and turkey-raising are not separately modelled.
- **Error bars.** VSE is a mean over elections. The CSV writes one row per election, so confidence intervals are computable — they are simply not printed, and they are missing from most charts drawn from it.
- **Large electorates.** 40 voters, 6 candidates. Ties are broken by `random.choice`.

None of these are defects in the tool; they are the boundary of what its output licenses you to say.

## Reading someone else's VSE-under-strategy chart

| Question | Answered in the source? |
|---|---|
| What electorate model, how many voters and candidates? | **Yes** — but only if the chart says it reused the published config. Ask. |
| How many elections per point? | **Yes** (15,000 published) — ask whether a custom run kept it. |
| What is the sincere baseline for each method? | **Yes, always computed.** If it is not on the chart, it was dropped. |
| Which strategy, per method? | **Yes** — burial-and-compromise for ranked, poll-anchored rescaling for scored. |
| Are the strategic voters a random slice or a bloc? | **Random slice** in `ProbChooser`. If the chart means a bloc, it is not this mechanism. |
| How good are the strategists' polls? | **Yes** — noisy by one SD unless overridden. Ask whether the same media model was used for every method. |
| Which strategy fractions were run? | **0/25/50/75/100.** A finer grid is a custom run. |
| What confidence interval separates two lines? | **No** — computable from the CSV, never printed. |
| How large a coalition did a successful attack need? | **No** — not modelled. |
| Does strategy *pay* for the strategists? | **Partly** — the one-sided runs tally `worked` as +1/0/−1. For the real answer, [PVSI](pvsi_strategic_incentive.md). |

Two checks worth running on any such chart, because they are cheap and they catch the two most likely errors:

1. **A method whose line is perfectly flat across the whole axis.** Every method in `allSystems` has a strategy implemented, IRV included. Flat to the pixel across 0–100% is more likely to be a chooser that was never wired up than a method that is immune.
2. **Score against Approval at 100% strategic.** Under the textbook Score strategy they would coincide; under *this* model they must not, because the strategic score ballot interpolates between the poll leaders. Whichever way a chart shows it, the chart should be able to say which strategy model it used.

## Reproducing it

The documented path (`docs/chart-reproduction.md`):

```bash
uv run python scripts/generate_published_results.py --elections 15000 --output artifacts/published-results
```

The CSV's first line records the media model, repo version, seed, model, methods, `nvot`, `ncand` and `niter` — so a result from it is self-describing, which is more than most published charts manage.

**Caveat as of 2026-08-24:** at `ef44ce4` that script does not run — `ModuleNotFoundError: No module named 'debugDump'`. It still imports `from vse import CsvBatch, …` and `from debugDump import setDebug`, module names that the move to the `src/vse_sim/` layout retired; the test suite imports `vse_sim.*`. The script was born working and was broken **two minutes later**: `d999795` created it alongside the reproduction guide while a root `vse.py` still existed, and the very next commit `f77a30f` — "Modernize package and move to Python 3.14" — moved the modules under `src/` without touching it. It has not been edited since. CI stays green because `testpaths` covers `src/vse_sim` and `tests`, so `scripts/` is never collected. The fix really is two lines (`from vse_sim.diagnostics import setDebug` / `from vse_sim.simulation import CsvBatch, KSModel, allSystems, fuzzyMediaFor` — `simulation.py` re-exports the last two), verified end-to-end on a copy: exit 0, and a self-describing CSV.

The general lesson is worth more than the bug: **a reproduction command that no test executes is not a reproduction command.** Full write-up — the evidence, the timeline, the fix, and the same audit run against this repo's own twenty documented-but-untested scripts: [a reproduction command nobody runs](../about_this_repo/vse_sim_reproduction_gap.md).

## References

- [`electionscience/vse-sim`](https://github.com/electionscience/vse-sim) — the code · [VSE FAQ and charts](https://electionscience.github.io/vse-sim/) · [interactive chart](https://electionscience.github.io/vse-sim/vse-graph.html) · [strategy view](https://electionscience.github.io/vse-sim/stratstuff.html)
- [Wolk, Quinn & Ogren (2023)](../../01_STAR/01_Learn/reference/wolk_quinn_ogren_2023.md) — the peer-reviewed VSE/PVSI paper, claim-checked here (authors are STAR advocates; lean disclosed)
- [Distortion](distortion.md) — VSE's proved, worst-case academic sibling
- [Formal compliance vs. strategic preservation](compliance_vs_strategic_preservation.md) — this repo's own strategy simulations, and the five-question checklist for any study of that shape
