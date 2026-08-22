---
tags:
  - criteria
  - simulation
---

# Simulate utilities, not ballots — the right primitive for comparing methods

*A 301 methodology note. When you run simulations to **compare** voting methods, the single most consequential decision is **where you inject the randomness**. Sampling random ballots (e.g. scores drawn uniformly from {0,1,2,3,4,5}) quietly rigs the comparison. Sampling random **utilities** and then *deriving* each ballot is the defensible approach — and it's what this repo's simulations already do.*

**Level: 301 · deep dive** Companion: [Election simulation models](election_simulation_models.md) (which *utility* model to use, once you're sampling utilities) · [How often do STAR and Approval disagree?](../../method_comparisons/star_vs_approval_divergence.md) (a worked application).

## The question: what is the random *primitive*?

There are three levels at which you could put the randomness, and they are not equivalent:

1. **Random ballots.** Draw each voter's ballot directly — e.g. a STAR ballot as six-sided-die scores per candidate, `{0..5}` uniform and independent.
2. **Random utilities → derived ballots.** Draw each voter's underlying **utility** (a real number) for each candidate, then *convert* that to whatever ballot each method needs — min-max onto 0–5 for STAR, a 0/1 cutoff for Approval, a rank order for IRV.
3. **Random voters & candidates in a model, utility = closeness.** Draw positions in an issue space; utility = −distance. (A structured *refinement* of #2.)

The reviewer's correction — "start from a number in [0,1], not from {0..5} scores" — is telling you to move from level 1 to level 2. That's correct. Here's why it matters.

## Why "random ballots" breaks a method comparison

- **There's no common ground to compare on.** To ask "who would STAR / Approval / IRV each elect from the *same electorate*," every method must render the **same underlying preferences** into its own ballot. Random 0–5 scores *are already a STAR ballot* — there's no neutral preference underneath from which to also derive a sincere Approval or ranked ballot. Starting from scores privileges the score methods by construction.
- **It assumes no preference structure.** Independent per-candidate scores imply candidates are unrelated — no ideological axis, no coalitions, no clones. Real electorates are highly structured; a model with none manufactures disagreement that reality doesn't have (see [impartial culture](election_simulation_models.md#the-standing-caveat-results-are-conditional-on-the-model), already the *adversarial* end of the spectrum — and raw random scores are even more artificial).
- **It skips the object of interest.** A ballot is a voter's *rendering* of their preferences (and, if strategic, of the race). The interesting method differences live in **how preferences become ballots** — the min-max scaling, the approval cutoff, the ranking. Sample ballots directly and you've thrown away both the preferences *and* the rendering step.
- **It bakes in arbitrary shape.** Uniform-independent `{0..5}` over-represents flat and extreme ballots in a way that corresponds to no coherent utility model. Utility-first + min-max produces ballot *shapes* that reflect the preference geometry.

## The correct primitive: utilities → ballots

Sample the **preference** (utility), then let each method draw its own ballot from it:

- **STAR:** min-max each voter's utilities onto 0–5 (`honest_scores`).
- **Approval:** approve everyone above a cutoff (above the voter's mean, or the midpoint of their range).
- **IRV / Ranked Robin:** rank candidates by utility.

Now every method is scored on **one shared electorate**, and the comparison is fair. This is not a repo invention — it's how VSE / Bayesian-regret studies have always worked, and it's the only setup that can even *define* "how good is the winner" (below).

## Your instinct was right — and it's already what the repo does

The two brute-force simulations here **sample utilities first**:

- [`fbc_simulation.py`](../../06_Other/simulations/fbc_simulation.py) and [`star_vs_approval_divergence.py`](../../06_Other/simulations/star_vs_approval_divergence.py) both call `sample_utilities()` (spatial or impartial), then derive STAR scores, approvals, and rankings from those utilities. No ballot is ever drawn at random.

So if a reviewer looked at the *committed* simulations, they're already at level 2/3. If an *earlier* sketch drew random `{0..5}` scores, that's the thing the correction applies to — and the fix is exactly what these scripts do.

## But `[0,1]` uniform isn't the finish line either (it's a ladder)

"More scientific" here is a ladder, not a switch:

| Rung | What you sample | Realism |
|---|---|---|
| 1 | random ballots (`{0..5}` scores) | ✗ artificial, rigs comparisons |
| 2 | random **utilities**, uniform & independent (**[impartial culture](election_simulation_models.md#a-noise-statistical-models-no-geometry)**) | better — but still *adversarial*: over-produces cycles and near-ties |
| 3 | **spatial / structured** utilities ([issue space](spatial_voting_model.md), [Mallows](election_simulation_models.md#a-noise-statistical-models-no-geometry), [clusters](spatial_voting_model.md#making-it-realistic-not-all-axes-weigh-the-same)) | most realistic; what VSE leans on |

So `[0,1]`-uniform utilities (impartial culture) is one rung up from random scores — the right *direction* — but it is itself a stress model, not "the truth." The honest habit is to run **both** a structured model and an adversarial one and **report which** (the [never-quote-a-rate-without-the-model](../curriculum/CURRICULUM_301.md) rule). Our sims default to running spatial *and* impartial for exactly this reason.

## When random scores are actually fine

Level-1 random ballots are **not wrong for everything** — they're wrong for *comparing methods and measuring welfare*. If your goal is to **stress-test a tabulator** ("does the engine compute the STAR winner correctly on weird inputs?"), random `{0..5}` scores are a perfectly good fuzzing fixture, because you're testing the *counter*, not modeling *voters*. Know which job you're doing.

## The preference→ballot step is a model too (and for Approval it's the crux)

Even utility-first, the *conversion* to a ballot is a modeling choice with real consequences:

- **STAR's min-max** assumes each voter uses the full 0–5 range — the "do scored ballots have a stable meaning?" debate lives here ([what makes a method good](what_makes_a_voting_method_good.md)).
- **Approval has no canonical conversion at all** — the voter picks a 0/1 cutoff, and *where* changes the winner. That's precisely why [STAR-vs-Approval divergence](../../method_comparisons/star_vs_approval_divergence.md) depends on the cutoff as well as the electorate model — its `--cutoffs` parameter *sweeps* the approval threshold (approve scores ≥5, ≥4, … ≥1) and the divergence rate moves from ~10% to ~40%, non-monotonically. The conversion rule isn't a detail; it's the experiment.

Sampling ballots directly hides this step; sampling utilities forces you to make it explicit — which is a feature, not a burden.

## Measured: what STAR's scale rule costs

The bullet above says min-max *assumes* each voter uses the full 0–5 range. That assumption has a natural-looking alternative, and the alternative is what most spatial write-ups actually reach for — so it is worth knowing what choosing between them does to the answer. Given a distance matrix, two rules turn it into a 0–5 ballot:

- **Global** — `U = 5 × (1 − d / d_max)`, one `d_max` shared by the whole electorate, rounded and clamped. The scale is *absolute*: a 5 means "close in the space," not "my favourite." This is the obvious rule and the one that circulates alongside descriptions of the [Euclidean samplers](euclidean_spaces.md).
- **Per-voter min-max** — your nearest candidate gets 5, your furthest 0, everyone else proportionally between. What this repo's simulations use, and what STAR's own voter guidance describes.

They are not close. Measured over 4,000 elections, 101 voters, 4 candidates on a `uniform_cube`, by [`score_encoding_stability.py`](../../06_Other/simulations/score_encoding_stability.py):

| score | global `d_max` | per-voter min-max | min-max on `−d²` |
|---|---|---|---|
| 0 | 1.8% | 29.5% | 28.1% |
| 1 | 13.4% | 10.4% | 7.5% |
| 2 | 27.4% | 10.8% | 9.0% |
| 3 | 31.0% | 10.5% | 10.5% |
| 4 | 22.7% | 9.6% | 12.5% |
| 5 | 3.6% | 29.2% | 32.5% |

A global `d_max` has to be wide enough for the furthest possible pair, so for a typical voter every candidate sits well inside it and the ballot compresses into the middle of the scale: **81% of all marks land in {2,3,4}**, and the endpoints — the two scores a real STAR voter uses most — nearly vanish. Two consequences follow, and neither is voter behaviour:

- **Dead ballots.** **2.5% of voters** score every candidate identically and express no preference at all. They are not abstaining; the encoding erased them. Min-max cannot do this — your nearest is always 5 and your furthest always 0 unless you are exactly equidistant, so the figure there is 0.00%.
- **Inflated [Equal Support](../../01_STAR/01_Learn/the_count/STAR_Automatic_Runoff.md).** Compression pushes far more voters into the no-preference bucket in the runoff: **32.4% against 11.4%**, roughly a threefold overstatement of how indecisive the same electorate is.

And the winner moves. Across the six spaces, the global rule and min-max elect **different candidates** this often, from identical positions:

| space | winner differs |
|---|---|
| `gaussian_ball` | 6.8% |
| `uniform_cube` | 7.1% |
| `gaussian_cube` | 7.2% |
| `uniform_ball` | 7.9% |
| `unbounded_gaussian` | 10.3% |
| `uniform_sphere` | **27.2%** |

`uniform_sphere` is the warning shot — an electorate of pure factions, where more than one election in four turns on the conversion arithmetic alone. `unbounded_gaussian` deserves its own note: it has **no maximum distance**, so a global `d_max` is not merely inadvisable there but undefined, and any implementation is quietly substituting the observed maximum for a quantity that does not exist.

Linear versus quadratic loss is the smaller decision of the two — min-max on `−d` and on `−d²` disagree 4.3% of the time — but it is still a decision, and still unstated in most write-ups.

**The rule this repo follows:** name the conversion rule beside the number, exactly as the electorate model is named beside it. A winner quoted from a single encoding is a claim about the encoding as much as about the method — and where the choice is genuinely arbitrary, sample the encodings and report a win rate rather than a winner.

## Why welfare metrics *require* utilities

The clincher: [**Voter Satisfaction Efficiency / Bayesian regret**](what_makes_a_good_winner.md#measuring-it-empirically-vse-bayesian-regret) scores a method by *how much utility the average voter gets from the winner*, versus the best-possible winner. That number is **undefined** without cardinal utilities. If you start from random ballots, you have no utilities, so you literally cannot compute "how good was this winner" — you can only compare methods to each other, not to the ideal. Utility-first is what makes welfare measurement possible.

## The bottom line

- **Comparing methods or measuring welfare** → sample **utilities** (a model — spatial and impartial, reported), then derive each method's ballot. *Never* sample ballots.
- **Stress-testing a tabulator** → random ballots are fine; you're testing the counter.
- Either way, the ballot is a *rendering* of a preference; the rendering (scaling, cutoff, ranking) is itself a modeling choice worth stating.

So: your `[0,1]`-utility instinct is the correct, more-scientific one — "more complicated" only because it makes the assumptions you were making anyway *explicit and reportable*. That explicitness **is** the rigor.

## Related

- [`score_encoding_stability.py`](../../06_Other/simulations/score_encoding_stability.py) · [the six Euclidean spaces](euclidean_spaces.md) — what the distance→score rule costs, measured
- [Election simulation models](election_simulation_models.md) — the menu of *utility* models (spatial, IC/IAC, Mallows, Plackett–Luce, Yee)
- [The spatial model — voters and candidates as points on a map](spatial_voting_model.md) — the geometry rung 3 rests on: issue space, distance-as-utility, Yee diagrams
- [How often do STAR and Approval disagree?](../../method_comparisons/star_vs_approval_divergence.md) · [the simulations folder](../../06_Other/simulations/README.md) — utility-first in practice
- [What makes a good winner?](what_makes_a_good_winner.md) (VSE) · [What makes a voting method good?](what_makes_a_voting_method_good.md) (the stable-meaning debate) · [Curriculum 301](../curriculum/CURRICULUM_301.md)
