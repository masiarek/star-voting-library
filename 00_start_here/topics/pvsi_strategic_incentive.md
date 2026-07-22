# PVSI — the Pivotal Voter Strategic Incentive

*[VSE](what_makes_a_good_winner.md#measuring-it-empirically-vse-bayesian-regret) asks **"does this method pick a good winner?"** PVSI asks the other half of the question: **"does this method reward you for lying on your ballot?"** It is VSE's companion metric, introduced in the same peer-reviewed paper, and it's the number behind claims like "in STAR, strategy is as likely to backfire as to work."*

**Level: 301.** Source: [Wolk, Quinn & Ogren (2023)](../STAR_Voting/reference/wolk_quinn_ogren_2023.md) — peer-reviewed, open access, and claim-checked here (the authors are STAR advocates; lean disclosed).

---

## The one-line definition

**PVSI is the average gain a *pivotal* voter gets from voting strategically instead of honestly**, expressed as a percentage of the utility gap between that voter's favorite and an average candidate.

| PVSI | Reading |
|---|---|
| **~0%** | strategy essentially never pays — honesty is the safe default |
| **negative** | strategy **backfires** more often than it works |
| **high positive** | strategy is genuinely rewarded, so expect voters to use it |
| **100%** (the ceiling) | a tactical vote would be *guaranteed* to swap an average winner for your favorite |

The scale matters: Plurality's ~14% is not "14% of voters strategize" — it means the decisive voter's expected payoff from strategizing is 14% of the way from an average candidate to their favorite. That's a large, reliable incentive.

## How it's measured — the pivotal-voter idea

Take a faction that would like to run a particular strategy. Order its members by who stands to gain most, then flip them to the strategic ballot one at a time until **the outcome actually changes**. The voter who tips it is the **pivotal voter**, and PVSI measures the utility change from *their* perspective. Simulation runs where the outcome never changes count as zero.

Formally, averaged over many simulated elections:

```
PVSI = ( U(strategic winner) − U(honest winner) ) ÷ ( U(favorite) − U(average candidate) )
```

evaluated for the pivotal voter. A "random faction" is defined by picking two candidates at random and taking the voters who prefer the first.

**Why pivotal?** Because strategy only matters when it changes something. The overwhelming majority of strategic ballots change no outcome at all; averaging over *those* would drown the signal. Isolating the decisive voter measures the incentive a voter actually faces when their vote can matter — which is exactly the moment strategy is tempting.

## The strategies tested

| Strategy | What the voter does |
|---|---|
| **Favorite Betrayal** | rate the *allied frontrunner* above your true favorite |
| **Burial** | rate the *enemy frontrunner* below candidates you actually like less |
| **Bullet voting** | support only your favorite, nobody else |
| **Inclusive / Exclusive** | (Approval) lower or raise your approval threshold |
| **Polarized Inclusive / Exclusive** | (STAR) score every candidate either 5 or 0 |
| **Honest Inflation / Deflation** | (STAR) exaggerate — 5, 4, 1, 0 — to boost an ally or block an enemy, **keeping your honest order** |

## What the numbers say

Most-incentivized strategy per method, on the paper's clustered-spatial model (6 candidates):

| Method | PVSI | The strategy that pays |
|---|:--:|---|
| **Plurality** | **~14%** | Favorite Betrayal — "vote for the lesser of two evils" |
| **Approval** | ~10% | set your threshold between the two frontrunners (Exclusive 10.1%; FB 9.8%) |
| **RCV-IRV** | ~3% | **Favorite Betrayal** — a positive incentive here means *ranking your favorite first can backfire* |
| **Approval Top Two** | ~3% | threshold-setting, much damped by the runoff |
| **STAR** | **~2%** | exaggerate your scores **while keeping honest preference order** |
| **Smith/Minimax** | **disincentivized across the board** | — |

Two findings do more work than the individual numbers:

1. **In STAR, Approval Top Two and Smith/Minimax, every strategy that gives *less than full support to your favorite* is disincentivized.** That is the measurable version of "vote your conscience": favorite betrayal, burial and bullet voting are all *strongly* disincentivized in STAR.
2. **STAR's only surviving incentive is honesty-preserving.** The ~2% rewards exaggerating *magnitudes* (5s and 0s rather than 4s and 1s), not reordering your preferences. Your honest ranking still decides the runoff — so the residual strategy doesn't corrupt the information the method relies on.

Note the direction of the IRV result: because IRV's most-rewarded strategy *is* favorite betrayal, the method that's marketed as letting you "vote your heart" measurably rewards not doing so. See [favorite betrayal](../STAR_Voting/properties_and_limits/favorite_betrayal_voting_301.md) and [center squeeze](../RCV_IRV/RCV_IRV_center_squeeze.md) for the mechanism.

## How PVSI relates to VSE

They measure different axes, and a method can do well on one and badly on the other:

- **VSE** — *accuracy*: how good is the winner, in voter-satisfaction terms?
- **PVSI** — *incentive*: how much pressure is there to misrepresent your preferences?

VSE also degrades *because* of strategy, so the two interact: a method with a high PVSI will tend to see more strategic ballots, which feeds back into a worse real-world VSE. That coupling is the paper's core argument for judging methods on both at once rather than on a pass/fail checklist.

## The "backfire ratio" chart — get the attribution right

The widely-shared figures **STAR 1:1 · Approval 2.6:1 · RCV-IRV 2.7:1 · Plurality 17.8:1** are a *works : backfires* restatement produced by the Equal Vote Coalition from the VSE simulator — **not** numbers printed in the paper. The paper reports **PVSI percentages** (the table above). Same underlying simulation, two presentations: cite the ratios to the infographic and the percentages to the journal article. (A 1:1 ratio and a ~2% PVSI are saying the same thing about STAR from different angles: strategy is roughly a coin flip, so it isn't worth running.)

## Run the cousin in this library

[`fbc_simulation.py`](../../06_Other/simulations/README.md) computes a **works : backfires ratio** by *exhaustive* ballot search — every possible betrayal ballot for every voter. That is a **different and broader** measurement than PVSI's realistic strategic-faction model, so the **magnitudes are not directly comparable**; only the *direction* (STAR less rewardingly manipulable than IRV, and both far less than Plurality) is shared. It's a useful independent sanity check precisely because it's built differently.

## The honest limits

- **Model-dependent.** The headline figures come from one clustered-spatial electorate model; Appendix B checks robustness across parameters, and the *ordering* holds up better than the exact values. Never quote a PVSI without its model — the standing rule for every simulated number here ([election simulation models](election_simulation_models.md), [the spatial model](spatial_voting_model.md)).
- **It assumes decent polling.** Every viability-aware strategy depends on knowing who the frontrunners are. Real polls carry error (the paper models 5% noise); worse information makes strategy riskier than PVSI suggests.
- **It's a marginal measure, not a coordination cost.** PVSI describes the single decisive voter, and deliberately says nothing about how hard it is to organize a whole faction to strategize in unison — which in practice is the bigger barrier.
- **Low is the goal; zero is impossible.** [Gibbard–Satterthwaite](gibbard_satterthwaite_theorem.md) guarantees every method with 3+ candidates is manipulable, so STAR's ~2% is *small, not nil* — see [STAR's honest limits](../STAR_Voting/properties_and_limits/STAR_honest_limits.md).
- **Advocate-authored.** The metric is sound and the code is published, but it was introduced by STAR proponents; on their own data a Condorcet method (Smith/Minimax) beats STAR on this very metric — which the [claim-check](../STAR_Voting/reference/wolk_quinn_ogren_2023.md) reports rather than buries.

## Related

- [What makes a good winner?](what_makes_a_good_winner.md) — VSE / Bayesian Regret, the accuracy half of the pair
- [Strategic voting](strategic_voting.md) · [the five strategic pathologies](strategic_pathologies.md) — the behaviours PVSI puts a number on
- [Gibbard–Satterthwaite](gibbard_satterthwaite_theorem.md) — why no method scores a true zero
- [The Smith set](smith_set.md) · [Ranked Robin](../RCV_Ranked_Robin/README.md) — the Condorcet family that scores best here
- [Single-winner scorecard](../../method_comparisons/single_winner_scorecard/README.md) — where these figures sit among the other criteria
- [Wolk, Quinn & Ogren (2023), claim-checked](../STAR_Voting/reference/wolk_quinn_ogren_2023.md) — the source paper
