---
tags:
  - criteria
  - simulation
---

# Continuous model, discrete ballot — the encoding step

*A spatial model hands every voter a **real number** for every candidate. A ballot gives them **six bubbles**. Getting from the first to the second is a step almost every write-up performs in one unexplained line, and it is not arithmetic — it is two independent modelling choices stacked, either of which can change who wins. This page is about that seam: what each side of it is, what the crossing costs, and what has to be named beside any number that crossed it.*

**Level: 301 · deep dive** Builds on [the spatial model](spatial_voting_model.md) (the continuous side), [cardinal utility](cardinal_utility.md) (what a "cardinal" ballot is claiming), and [simulate utilities, not ballots](simulate_utilities_not_ballots.md) (which measures the *other* knob on this same seam).

---

## The two objects

**The model is continuous.** In the [spatial model](spatial_voting_model.md), voters and candidates are points in ℝ^d — a list of *d* real numbers each, one per issue axis, where *d* = 1 is the familiar left–right line, *d* = 2 is a map of two issues, and *d* = 100 is unpicturable but perfectly well-defined. The load-bearing move is that candidates live in the **same space as voters**, so the distance between a voter and a candidate exists at all; a voter's utility is minus that distance. Three things are continuous about it, and all three matter here:

- **The value.** The distance is a real number. Two candidates 0.0001 apart and two candidates 0.9 apart are different situations, and the model says so.
- **The positions.** Voters are drawn from a distribution over the space, not from a finite list of preference types — that's what the [six Euclidean spaces](euclidean_spaces.md) enumerate.
- **The comparisons.** Because the gaps are real-valued, "I barely prefer Ana" and "I desperately prefer Ana" are different *numbers*, which is what makes welfare measures like [VSE](what_makes_a_good_winner.md) definable at all.

**The ballot is discrete and cardinal, and those are two separate facts.** This is the conflation worth breaking up first, because most arguments about score ballots run them together:

- **Cardinal** is an *invariance class*, not a resolution. An interval scale survives positive affine transformation `u → au + b`, so the ordering of *differences* is preserved while ratios are not ([cardinal utility](cardinal_utility.md)). You can watch it hold: the [rescaled twin case](../../method_comparisons/hillinger_evaluative_voting/cases/cases_pages/hillinger_t4_affine.md) runs one election as marks `(0, 1, 2)` and again as `(1, 3, 5)`; the totals move, the finalists, the winner and the runoff margin do not.
- **Discrete** is how many rungs exist to write on. A [0–5 ballot](../scores_and_ranks/score_ballot.md) has six.

Cardinality says which transformations preserve meaning. Discreteness says how much meaning could be expressed in the first place. A continuous scale can be cardinal; so can a 0–5 one; so can a 0/1 one. Losing resolution does not stop a ballot being cardinal — it just gives it less to be cardinal *about*.

## The seam has two knobs, not one

Turning a distance into a mark does two lossy things, and they are separable — which matters, because a write-up that names one has still not specified the encoder:

1. **Normalize** — whose scale? A **global `d_max`** (`U = 5 × (1 − d/d_max)`, one denominator for the whole electorate, so a 5 means "close in the space") or **per-voter min-max** (your nearest gets 5, your furthest 0 — what STAR's own voter guidance describes and what this repo's simulations use).
2. **Quantize** — how many rungs, and where do the cuts between them fall?

Knob 1 is measured in [simulate utilities, not ballots](simulate_utilities_not_ballots.md), by [`score_encoding_stability.py`](../../06_Other/simulations/score_encoding_stability.py), which fixes the scale at 0–5 and varies the normalization. Short version: a global `d_max` compresses 81% of all marks into {2,3,4}, erases 2.5% of ballots into expressing nothing at all, overstates [Equal Support](../../01_STAR/01_Learn/the_count/STAR_Automatic_Runoff.md) threefold, and changes the winner 6.8%–27.2% of the time depending on the space.

Knob 2 is measured here, by [`score_resolution.py`](../../06_Other/simulations/score_resolution.py), which fixes the normalization at per-voter min-max and varies the rungs. Every row below is the *same* rule at a different resolution, scored against the same voter who could have written any real number.

## What the rungs cost

4,000 elections, 101 voters, 4 candidates, `uniform_cube`, 2-D. `differs` is how often this ballot elects someone other than the continuous baseline elects from identical positions; `VSE` is the winner's [voter satisfaction efficiency](what_makes_a_good_winner.md) against the true spatial utilities; `silenced` is the share of the strict preferences a voter genuinely holds that the ballot cannot express because both candidates landed on the same rung.

| ballot | differs | VSE | silenced | Equal Support |
|---|---|---|---|---|
| **0–1** (approval) | 13.6% | 0.9743 | 41.8% | 51.5% |
| **0–2** | 8.3% | 0.9892 | 22.3% | 28.4% |
| **0–3** | 5.7% | 0.9923 | 15.0% | 19.1% |
| **0–5** (the STAR ballot) | 3.8% | 0.9922 | 9.0% | 11.6% |
| **0–9** | 2.8% | 0.9925 | 5.0% | 6.4% |
| **0–99** | 0.5% | 0.9909 | 0.4% | 0.6% |
| **continuous** | *baseline* | 0.9904 | 0.0% | 0.0% |

```bash
.venv/bin/python 06_Other/simulations/score_resolution.py
```

Three things fall out, and the second is the one people get wrong.

**Welfare saturates at three or four rungs.** One bit costs real welfare — 0.9743, and it is the only row that does. By 0–3 the ladder has hit its ceiling: 0–3, 0–5, 0–9, 0–99 and infinite resolution all land within 0.002 of each other, and their order among themselves is not stable across seeds. Whatever more rungs buy, it is not a better winner *by this yardstick*. (The quantized rows do sit a hair *above* continuous in every seed tried. It is 0.002, it is not what this page is claiming, and the honest reading is that the effect is nil rather than reversed.) That is the average-case echo of what [distortion](distortion.md) proves in the worst case — the first scrap of intensity information is worth more than everything you could do without it, and the returns die fast. It is also the empirical shadow of the theory's harshest row: Approval-only input has *unbounded* worst-case metric distortion, and 0/1 is exactly the rung that costs measurable average welfare here too.

**More rungs keep changing *who* wins long after they stop changing *how good* the winner is.** 0–5 elects someone other than the infinite-precision winner in 3.8% of elections and 0–99 in 0.5% — the extra rungs are visibly still moving the result — while VSE across that whole range does not improve at all. Those elections are re-sorting near-ties between near-equally-good candidates — the extra resolution is deciding photo-finishes, not rescuing anybody. Which is a general reading rule for this whole literature: **a changed winner is not by itself evidence of a defect.** It has to be paired with a yardstick that says the new winner is worse, or it is just a coin landing the other way up.

**"Silenced" is a fairness measure, not a welfare one.** A 0/1 ballot cannot say 42% of what its voter thinks, and drives half the electorate into Equal Support in the runoff — that is a real cost to the voter *as a voter*, and it is the honest kernel of [the equal-scores criticism](../../01_STAR/01_Learn/reference/are_equal_score_votes_discounted.md). But it is not the same quantity as welfare, and the two come apart: the equal-band encoder below silences *more* preferences than the default one at every resolution while scoring the same or better on VSE, because the preferences it merges are ones at the extremes of a ballot, where merging them changes no outcome.

## The pressure comes from the field size

Six rungs against four candidates is roomy; six rungs against sixteen is not. Same run, swept across field sizes:

| candidates | 0–1 | 0–2 | 0–3 | 0–5 | 0–9 | 0–99 |
|---|---|---|---|---|---|---|
| 3 | 11.3% | 5.4% | 4.2% | **2.7%** | 1.8% | 0.3% |
| 4 | 13.6% | 8.3% | 5.7% | **3.8%** | 2.8% | 0.5% |
| 6 | 20.6% | 16.8% | 10.5% | **6.7%** | 4.5% | 1.2% |
| 10 | 25.7% | 33.1% | 18.3% | **11.9%** | 7.6% | 1.9% |
| 16 | 29.7% | 55.0% | 24.0% | **17.6%** | 11.4% | 2.4% |

*(winner differs from the continuous baseline;* `--sweep-candidates` *also prints VSE and silenced)*

```bash
.venv/bin/python 06_Other/simulations/score_resolution.py --sweep-candidates
```

The rung count is not the variable on its own — **it is the rung count against the number of candidates that have to share the rungs.** A real STAR election with three to six candidates sits comfortably in the flat part of the table, which is the practical defence of 0–5: not that six is a magic number, but that six rungs are past the knee for the field sizes single-winner elections actually have. Push the field to sixteen and 0–5 is doing visibly more rounding than the ballot's designers were promising.

## Where the cuts fall is a *second* choice, and at low resolution it dominates

Look at the 0–2 column above: 5.4% → 8.3% → 16.8% → 33.1% → **55.0%**. Every other column rises smoothly with the field; that one detonates, and at sixteen candidates a three-level ballot is worse than a one-bit ballot. Its VSE collapses to **0.9120**, below approval's 0.9756.

The cause is not the number of levels. It is where the cuts sit. **Rounding to the nearest of K+1 rungs does not divide the range into equal bands** — the end bands are half-width and the interior ones full-width, so at K=2 the middle rung is a catch-all covering *half* the voter's range (.25 / .50 / .25). On a large field most candidates land in it and the tally can only see who reached the top quarter. Cut the same three levels into equal-width bands instead and most of the damage goes away:

| 16 candidates | 0–1 | 0–2 | 0–3 | 0–5 | 0–9 |
|---|---|---|---|---|---|
| round-to-nearest (VSE) | 0.9756 | **0.9120** | 0.9847 | 0.9926 | 0.9957 |
| equal-width bands (VSE) | 0.9756 | **0.9746** | 0.9893 | 0.9947 | 0.9962 |

```bash
.venv/bin/python 06_Other/simulations/score_resolution.py --candidates 16 --equal-bands
```

Same resolution, different cut points, 0.063 of VSE. (The 0–1 column is identical under both by construction — with one threshold there is no interior band to place — which is a useful check that the flag does what it says.) The effect fades fast with resolution: at 0–5 the choice is worth 0.0021 on that same field and 0.0014 on a four-candidate one. Real, not zero, and equal-width wins every comparison here — but decisive only when the rungs are few enough that one band can swallow the middle of the ballot.

This is worth recognizing, because it is not a new problem: it is **[Approval's cutoff problem](../../04_Approval/01_Learn/approval_honest_limits.md) reappearing inside a *score* encoder.** Where you draw the line changes the winner; a coarse score ballot just has two or three lines instead of one. The [STAR-vs-Approval divergence](../../method_comparisons/star_vs_approval_divergence.md) sweep found the same shape empirically from the other direction — the divergence rate moves from ~10% to ~40% as the approval threshold slides, non-monotonically. Coarse cardinal ballots are threshold instruments, and thresholds have to be chosen rather than defaulted into.

## The honest limits

This measures one thing well and should not be stretched:

- **One space, one normalization, honest voters.** Everything above is `uniform_cube`, per-voter min-max, linear loss, no strategy. `--all-spaces` moves the numbers; [`uniform_sphere`](euclidean_spaces.md) is the usual outlier, as it is for the normalization knob.
- **VSE is a utilitarian yardstick, and STAR is a [hybrid](../../01_STAR/01_Learn/the_count/STAR_hybrid_nature.md).** A method that deliberately applies a majority correction after a sum will never look optimal against a pure sum, and shouldn't. "Saturates at three rungs" is a claim about *this* measure; a majoritarian yardstick would rank the rows differently, and the [runoff-reversal](../../01_STAR/02_Examples/runoff_overturns_leader/README.md) cases are where the two yardsticks visibly pull apart.
- **The tie-breaks are the folder's conventions, not the engine's ladder** (top two by total, ties to the lower index). This is a divergence-rate measurement, not a tabulator; for a real count, run the LH engine on a case file.
- **Quantization is only half of the seam.** These runs hold the normalization fixed. The other knob moves winners by up to 27.2%, which is larger than anything measured here — so nothing on this page licenses skipping that one.

## The rule this produces

The house rule for the normalization knob already reads: *name the conversion rule beside the number, exactly as the electorate model is named beside it.* This page extends it by one item, because the conversion rule turns out to have two parts:

> **A spatial number is only as specified as its encoder.** Name the electorate model, the normalization, **the resolution, and where the cuts fall.** A winner quoted from a single encoding is a claim about the encoding as much as about the method — and where the choice is genuinely arbitrary, sample the encodings and report a win rate rather than a winner.

## Related

- [Simulate utilities, not ballots](simulate_utilities_not_ballots.md) — the other knob on this seam, measured: normalization, and what a global `d_max` costs
- [The spatial model](spatial_voting_model.md) · [the six Euclidean spaces](euclidean_spaces.md) — the continuous side, in close-up
- [Cardinal utility](cardinal_utility.md) — what "cardinal" claims, and why resolution is a different axis · [scores vs. ranks](../scores_and_ranks/scores_vs_ranks.md) · [preference vs. support](../scores_and_ranks/preference_vs_support.md)
- [Distortion](distortion.md) — the same shape proved in the worst case: rankings Θ(m²), one scrap of intensity O(m), approval-only unbounded
- [What makes a good winner?](what_makes_a_good_winner.md) — the VSE column's definition · [election simulation models](election_simulation_models.md) — which utility model to draw from
- [Are equal-score votes discounted?](../../01_STAR/01_Learn/reference/are_equal_score_votes_discounted.md) — the "silenced" column, argued from the voter's side · [Approval's honest limits](../../04_Approval/01_Learn/approval_honest_limits.md) — the cutoff problem in its original home
- Code: [`score_resolution.py`](../../06_Other/simulations/score_resolution.py) · [`score_encoding_stability.py`](../../06_Other/simulations/score_encoding_stability.py) · [the simulations folder](../../06_Other/simulations/README.md)
