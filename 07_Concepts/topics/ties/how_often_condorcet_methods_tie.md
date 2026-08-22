# How often does each Condorcet method tie?

**Level: 301 · deep dive**

*This hub's opening line says that how often ties arise "differ[s] by method" and then never says by how much. This page measures it, on a claim that has been sitting unanswered on Wikipedia since 2021 — and the answer turns out to reverse depending on something nobody in that discussion mentioned.*

## The claim under test

On [Talk:Copeland's method](https://en.wikipedia.org/wiki/Talk:Copeland%27s_method), February 2021, RobLa wrote that he was *"pretty sure"* a Monte Carlo simulation would show Copeland's method has *"way more ties"* than Schulze, Ranked Pairs, or almost any other Condorcet method — adding, carefully, that *"it would depend on the model being used and many other factors."* Nobody ran it. Five years later the article still carries the argument without the number.

Both halves of that turn out to be right, and the hedge is the more interesting half.

## What "tie" means here

Every method is asked for its **irresolute winner set** — the answer the rule gives *before* any tie-break. A method ties on an election when that set has more than one member. This is the [resolvability](https://en.wikipedia.org/wiki/Resolvability_criterion) question Markus Schulze pointed at in the same discussion, and it is the only comparison that is fair: bolt a good enough tie-break onto anything and it always names one winner, so comparing final answers would measure the tie-breaks rather than the methods.

Counts come from [`pref_voting`](../../tabulation_engines/cross_checking_with_pref_voting.md) — Holliday & Pacuit's library, the same third-party engine this repo already uses to cross-check Ranked Robin. Nothing below is this repo's own arithmetic, which matters, because the claim under test is about Copeland and not about our engine.

## The headline: at a public-election electorate, confirmed

20,000 elections per cell, 101 voters (**odd**, so no matchup can be drawn), [impartial culture](../election_simulation_models.md). Percentages are how often each method returned more than one winner; ± is a 95% Wilson interval.

| Candidates | no Condorcet winner | **Copeland** | Beat Path (Schulze) | Ranked Pairs | Minimax | Split Cycle |
|---|---|---|---|---|---|---|
| 3 | 8.68% | **8.68%** | 2.73% | 2.73% | 2.73% | 2.73% |
| 4 | 17.27% | **17.27%** | 5.25% | 4.67% | 5.27% | 6.05% |
| 5 | 25.39% | **21.95%** | 7.96% | 6.75% | 7.88% | 10.24% |
| 6 | 31.33% | **23.68%** | 9.28% | *(not computed)* | 9.33% | 13.70% |

Copeland ties **2.6 to 3.2 times as often** as Schulze or Minimax across the range. RobLa's "way more" is fair.

Two things to notice before the reversal below. First, a validation: the no-Condorcet-winner rate at three candidates comes out at **8.68%**, against Gehrlein's published impartial-culture limit of **8.77%** — the sweep reproduces a number it was never told, which is the cheapest evidence that the pipeline is sound. Second, look at the first two rows: **Copeland's tie rate is not merely close to the cycle rate, it is identical to it.** That is not a coincidence, and it is the whole mechanism — see [below](#why-copeland-and-not-the-others).

Conditioning on the cycle isolates the disagreement, since every method here elects the Condorcet winner uniquely whenever one exists:

| Candidates | **Copeland** | Beat Path | Ranked Pairs | Minimax | Split Cycle |
|---|---|---|---|---|---|
| 3 | **100.00%** | 31.41% | 31.41% | 31.41% | 31.41% |
| 4 | **100.00%** | 30.39% | 27.00% | 30.51% | 35.02% |
| 5 | **86.45%** | 31.36% | 26.62% | 31.02% | 40.36% |
| 6 | **75.59%** | 29.63% | *(not computed)* | 29.79% | 43.72% |

Given a cycle at three or four candidates, Copeland ties **always**. The others tie about a third of the time.

## The reversal nobody mentioned: voter parity

Hold the field at five candidates and vary the electorate instead. The **even** rows are the ones to read.

| Voters | no Condorcet winner | **Copeland** | Beat Path | Minimax | Split Cycle |
|---|---|---|---|---|---|
| 9 (odd) | 22.45% | 19.70% | 19.97% | 20.05% | 20.03% |
| **10 (even)** | 61.05% | **18.16%** | 38.38% | 38.14% | 40.92% |
| 25 (odd) | 24.64% | 21.46% | 14.59% | 14.51% | 15.64% |
| **26 (even)** | 49.90% | **16.17%** | 24.93% | 24.96% | 28.18% |
| 101 (odd) | 24.86% | 21.59% | 7.88% | 7.83% | 10.00% |
| **100 (even)** | 38.80% | 16.79% | 13.20% | 13.25% | 16.57% |

**On a ten-voter electorate Copeland ties less than half as often as Schulze does** — 18.16% against 38.38%. At twenty-six voters it is still ahead, 16.17% against 24.93%. The conjecture is not merely weaker at small scale; it is *backwards*.

The reason is that an even electorate can produce a **drawn matchup**, and a draw is a margin of zero. Feed a weighted-tournament method a grid full of zeros and it has nothing to weigh, so Schulze, Minimax and Split Cycle all tie. Copeland scores a draw as half a win and can still separate a candidate on two wins and two draws from one on two wins, a draw and a loss. The very coarseness that makes Copeland informationally poor is what makes it **robust when the margins are degenerate**.

Reading down the odd rows shows where the gap actually comes from:

- **Copeland** — 19.70% → 21.46% → 21.59%: flat, because it is tracking the cycle rate, and that converges to a constant.
- **Beat Path** — 19.97% → 14.59% → 7.88%: falling, because exact margin ties become rare as the electorate grows.

So the two methods are *comparably* indecisive on a committee and diverge steadily as the electorate scales. RobLa's conjecture is a claim about large electorates that happens to be stated without the qualifier.

## The realistic-electorate answer: it rarely matters at all

Impartial culture is a stress test, not a prediction — it assumes voters are independent and manufactures cycles at rates no real electorate shows. Re-run the same sweep on a [spatial model](../spatial_voting_model.md) (voters and candidates as Gaussian points, each voter ranking by distance), 101 voters:

| Candidates | no Condorcet winner | **Copeland** | Beat Path | Minimax |
|---|---|---|---|---|
| 3 | 0.15% | 0.15% | 0.06% | 0.06% |
| 4 | 0.46% | 0.46% | 0.14% | 0.14% |
| 5 | 0.70% | 0.70% | 0.26% | 0.26% |
| 6 | 1.25% | 1.22% | 0.52% | 0.52% |

The **ratio survives** — Copeland is still about 2.5× the others — but the **stakes collapse**: every method now ties well under 2% of the time, because a structured electorate almost always has a Condorcet winner. Conditional on a cycle, Copeland still ties 100% of the time at three to five candidates, so the mechanism is model-independent; only its frequency is not. And the parity reversal survives too: at ten voters spatial gives Copeland 16.47% against Beat Path's 27.65%.

The honest summary is three sentences. In a large public election Copeland reaches for a tie-break markedly more often than its siblings, but all of them do so rarely. In a small committee — the case Ranked Robin is often actually proposed for — Copeland is the *more* decisive choice whenever the membership is even. And no result on this page should be quoted without saying which electorate model produced it.

## Why Copeland, and not the others

The gap is not bad luck; it is Copeland's [informational basis](../what_a_method_reads.md). Copeland is a **C1** rule: it reads only the tournament — *who* beat whom, never *by how much*. Schulze, Ranked Pairs, Minimax and Split Cycle are **C2**: they read the margins. Inside a cycle the direction information is symmetric by construction, so a C1 rule has nothing left to separate anyone with, while a C2 rule still has the sizes.

At three and four candidates that is not a tendency but an arithmetic impossibility. Exhaustively, over every complete tournament:

| Candidates | tournaments | with no Condorcet winner | …yet a unique Copeland winner |
|---|---|---|---|
| 3 | 8 | 2 | **0** |
| 4 | 64 | 32 | **0** |
| 5 | 1,024 | 704 | 280 (39.8%) |
| 6 | 32,768 | 26,624 | 14,400 (54.1%) |

Copeland scores must sum to `C(n,2)`, and with nobody on `n−1` wins, nobody can sit alone on top — so at three or four candidates **Copeland cannot break a cycle, ever**. That is exactly the 100.00% in the conditional table, and the sampled rate falling to 86% and 76% at five and six candidates is this table's third row onward.

It also explains why [a second Copeland round cannot rescue it](../../../05_Ranked_Robin/03_Criteria/rr_tiebreaks/degrees_of_ties.md#why-not-just-run-copeland-again): second-order Copeland is **still C1**, re-reading the same tournament, so it adds no information and separates nothing at three candidates. Only margins help — which is precisely what [Ranked Robin's published ladder](../../../05_Ranked_Robin/03_Criteria/rr_tiebreaks/degrees_of_ties.md) reaches for. Its **1st Degree** is a sum of win margins, so the ladder is the device that buys back the C2 information the tally discarded.

The repo's own [eleven-ballot cycle](../../../05_Ranked_Robin/03_Criteria/rr_tiebreaks/cases/rr_degrees_three_way_cycle.yaml) is the whole page in one election: Copeland ties Dre, Edith and Frank at 1 apiece, while Beat Path, Ranked Pairs, Minimax and Split Cycle each name **Frank** outright with no tie-break at all — and Ranked Robin's 1st Degree also lands on Frank, +6. The ladder recovers exactly what the margin-readers saw directly.

## What this does not say

- **It is not a verdict on Ranked Robin.** Everything measured here is the *tally* stopping short, not the method failing to produce an answer. Ranked Robin's ladder resolves most of these deterministically, and where it cannot, [no rule could have done better](ties_are_forced.md).
- **"Ties more" is not "elects worse."** Copeland winners always lie inside the [Smith set](../smith_set.md); the method declines to narrow further, which is a different complaint from choosing badly.
- **Split Cycle's higher rate is by design.** It returns every undefeated candidate rather than picking one, so counting that as indecisiveness slightly misreads it — see [Split Cycle](../condorcet/split_cycle.md).
- **Ranked Pairs is missing from some cells, and not by accident.** It computes its irresolute winner set by enumerating every linear order consistent with the margins, so tied margins make it factorial — at nine voters `pref_voting`'s own tractability guard declines 14% of profiles, and at ten voters 53%. Those refusals are exactly the margin-tied profiles, the ones likeliest to tie, so quoting a rate over the remainder would bias it **downward** — the one direction that would flatter this page's conclusion. Cells above 1% skipped are left blank rather than estimated.

## Reproduce it

[`resolvability_sweep.py`](../../../STARVote_LH_tabulation_engine/tools_adam/resolvability_sweep.py) is seeded and deterministic:

```bash
.venv/bin/python STARVote_LH_tabulation_engine/tools_adam/resolvability_sweep.py --why
```

That prints the exhaustive mechanism table in a second. The full sampled sweep is `--n 20000 --n-slow 6000`, about fifteen minutes.

> **One trap worth recording, because it nearly became a published finding.** The first version of this sweep drew its spatial electorates with `generate_profile(probmodel="euclidean", seed=…)` and reported **0.00% cycles in every single spatial cell** — a tidy, quotable, completely false result. That path collapses when given a seed: 2,000 different seeds returned 2,000 copies of one degenerate profile in which every voter submits the identical ranking. The defect is not in `pref_voting` but one layer down in **prefsampling 0.1.24**, which it calls — `GAUSSIAN_BALL` returns a single point repeated once per voter, so every voter sits on the same spot, every candidate is equidistant, and the ranking falls back to index order. Filed upstream as [prefsampling#6](https://github.com/COMSOC-Community/prefsampling/issues/6), which also covers a second defect found alongside it: candidates are drawn from the same seeded stream as the voters, landing exactly on the first voters, on four of the six spaces. Unseeded calls are fine — so seeding *for reproducibility* is what breaks it. The sweep now draws positions from a numpy generator it owns. A simulation that returns a suspiciously clean zero deserves a check that the sampler is sampling.

## Related

- [Degrees of ties — how Ranked Robin is supposed to break one](../../../05_Ranked_Robin/03_Criteria/rr_tiebreaks/degrees_of_ties.md) · [Cycle resolution](../../../05_Ranked_Robin/01_Learn/cycle_resolution.md)
- [Ties are forced](ties_are_forced.md) — the impossibility theorem underneath all of this
- [What a method reads (C1 / C2 / C3)](../what_a_method_reads.md) · [Election simulation models](../election_simulation_models.md) · [The spatial model](../spatial_voting_model.md)
- [Ranked Robin (the method)](../../../05_Ranked_Robin/01_Learn/ranked_robin.md) · [Minimax](../../voting_paradoxes/minimax.md) · [Split Cycle](../condorcet/split_cycle.md)
