# The statistics you actually need to read voting research

*Voting papers lean on a small, specific set of statistical ideas — and in this field several of them aren't background maths at all: **they are the thing being argued about.** Whether you total scores or take their median isn't a technical detail, it's the difference between two voting methods. This page covers only the concepts that **change a voting answer**, and points at where each one bites. It is not a statistics course; every entry is here because you'll misread a paper without it.*

**Level: 201 → 301.** Companion: [election simulation models](election_simulation_models.md) (the model-building subset) · [simulate utilities, not ballots](simulate_utilities_not_ballots.md).

---

## 1. Mean, sum, and median — a method-defining choice

The big one. These are not three ways of saying "average"; picking between them **picks a voting method**:

| Rule | Method | Behaviour |
|---|---|---|
| **Sum** (≡ mean, when everyone scores everyone) | **Score / Range**, and STAR's scoring round | rewards **intensity** — a 5 counts five times a 1 |
| **Median** | **[Majority Judgment](three_two_one_voting.md)** | ignores how extreme the extremes are |

Why it matters: the **mean is dragged by outliers, the median isn't.** So under a summing method, exaggerating your scores (5s and 0s instead of 4s and 1s) genuinely moves the total — which is exactly the residual strategic incentive [PVSI](pvsi_strategic_incentive.md) measures for STAR. Under a median method that exaggeration does almost nothing… but neither does *sincere* intensity, so the method can't tell "everyone's decent second choice" from "one faction's passion." **Robustness and expressiveness are the trade**, and mean-vs-median is where you make it.

Watch for this: an argument that quietly assumes the mean is the right summary is assuming a *cardinal, intensity-counting* view of democracy. That's a defensible position, not a neutral one.

## 2. Sum vs mean — they diverge exactly when the denominator does

If every voter scores every candidate, ranking by total and ranking by average give the **same order** — the denominator is identical, so it cancels. They come apart the moment some ballots don't count for some candidates: **abstentions, blanks, and skipped races**.

That's not academic. It's precisely the [runoff-denominator](../STAR_Voting/the_count/runoff_percentages.md) question — should the runoff percentage be out of *all* ballots, or only those expressing a preference (excluding [Equal Support](../GLOSSARY.md))? Any paper reporting a percentage owes you its denominator.

## 3. Distribution shape — consensus, polarization, and why the average hides it

A single number destroys the shape of the thing it summarizes. Three electorates can share an identical mean score:

- **Consensus** — scores bunched together. Nearly everyone agrees.
- **Polarized (bimodal)** — two clumps at opposite ends, nobody in between.
- **Uniform** — scores spread evenly. No structure at all.

**A rated ballot preserves this and a ranked ballot destroys it** — with rankings you can see *that* voters split, never *how far apart* they are. That is the substance behind the [majority-of-consensus critique](majority_criterion/README.md), and it's why this repo's simulations report the *model* alongside every rate.

## 4. Variance — the statistical name for "divisive"

**Variance** (and its square root, **standard deviation**) measures spread. It's the most under-used idea in this literature, because it's what "polarizing candidate" actually means:

> Two candidates with the **same average score** can be completely different politicians. One got 3s from everybody. The other got 5s from half the electorate and 0s from the other half. Same mean — **wildly different variance.**

That single sentence is the [majority criterion](majority_criterion/README.md) debate in miniature: the broadly-liked candidate and the polarizing one, arithmetically tied on the mean, separated only by the spread. Whenever a method is accused of electing a "divisive" winner, the claim is about variance.

## 5. Normalization — turning feelings into a 0–5 ballot

**Min-max normalization** rescales a voter's private utilities so their favourite gets the top of the scale and their least favourite the bottom. It's how simulations derive a "sincere" STAR ballot, and roughly what real voters do.

The consequence to remember: heavy **strategic** normalization — everything pushed to 5 or 0 — collapses a rated ballot into an essentially **ordinal** one, which is why [STAR's escape from Arrow](arrow_theorem_and_star.md) is cleanest under reasonably sincere scoring.

## 6. Independence vs correlation — why "random ballots" mislead

Two events are **independent** if one tells you nothing about the other; **correlated** if it does. Real electorates are **heavily correlated** — someone who likes candidate A usually likes ideologically similar candidate B.

This is the single most important modelling fact in the field. [Impartial culture](election_simulation_models.md) assumes **independence**, which is why it manufactures Condorcet cycles and paradoxes far more often than reality does. It's a **stress test, not a prediction** — and any paper quoting a paradox rate from impartial culture without saying so is overstating it.

## 7. Expected value, sampling error, and Monte Carlo

- **Expected value** — the long-run average. [VSE](what_makes_a_good_winner.md#measuring-it-empirically-vse-bayesian-regret) is an expected value: average voter satisfaction across thousands of simulated elections.
- **Sampling error** — real polls are wrong by a few points, and that uncertainty is what makes strategy *risky*. Papers model it explicitly (Wolk–Quinn–Ogren use 5% noise) — which is why a **live running tally**, having no error at all, raises the strategic incentive above the published figures.
- **Monte Carlo** — answer a hard question by simulating it many times and counting. Every simulation in this repo is Monte Carlo, which is why results come with a **seed** and a **trial count**: without them the number isn't reproducible.

## 8. Two formulas worth recognizing on sight

- **Sum of squares → [Effective Number of Parties](../GLOSSARY.md):** `ENP = 1 / Σ(sᵢ²)`. Squaring makes big parties dominate, so tiny parties barely register — that's the point.
- **Quota → seats:** the **Droop quota** `1/(M+1)` sets the vote share needed for one seat at [district magnitude](../GLOSSARY.md) M. Three seats ≈ 25%, ten seats ≈ 9%.

## The habit that matters more than any formula

**Never quote a rate without its model.** Every number in this literature is conditional on assumptions — the electorate model, the strategy model, the candidate count, the tie rule. "STAR and Approval disagree 12% of the time" is meaningless until you add *under which model, with which approval cutoff*. That standing caution ([301.6](../curriculum/CURRICULUM_301.md)) is worth more than any single statistic, and it's the fastest way to spot an overclaim — including your own.

## Related

- [Election simulation models](election_simulation_models.md) — the model-building maths in depth
- [Simulate utilities, not ballots](simulate_utilities_not_ballots.md) — why you sample preferences and derive ballots
- [The spatial model](spatial_voting_model.md) — the geometry these distributions live in
- [PVSI](pvsi_strategic_incentive.md) · [what makes a good winner?](what_makes_a_good_winner.md) — the two metrics built from all of the above
