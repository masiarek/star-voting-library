# Does the qualifying round throw away the consensus winner?

*Several reform packages are two-stage: an open qualifying election narrows a crowded field to the top few, then a good method runs the general. That design has a quiet assumption baked into it — that the primary won't discard the very candidate the reform exists to elect. This page measures whether that assumption holds, and finds that **it depends almost entirely on a design choice most proposals leave unspecified.***

**Level: 301.** Companions: [election simulation models](../00_start_here/topics/election_simulation_models.md) · [simulate utilities, not ballots](../00_start_here/topics/simulate_utilities_not_ballots.md) · [Ranked Robin vs. Consensus Choice](../00_start_here/RCV_Ranked_Robin/ranked_robin_vs_consensus_choice.md) · runnable: [`primary_method_simulation.py`](../06_Other/simulations/primary_method_simulation.py)

## The question, and why it isn't rhetorical

[Consensus Choice](../00_start_here/RCV_Ranked_Robin/ranked_robin_vs_consensus_choice.md), promoted by Better Choices for Democracy, is the live example. Step 1 of the proposal is *"an open qualifying election—without party restrictions—[that] determines at least four of the strongest candidates who advance to the general election."* Step 2 onward is the pairwise Condorcet count.

Neither their [main page](https://www.betterchoices.vote/consensus-choice) nor their [FAQ](https://www.betterchoices.vote/faqs) says **which voting method the qualifying round uses.** Alaska's top-4 uses Choose-One. If a reform's own first round runs on the method the reform exists to replace, the obvious worry is that it discards the consensus candidate before the good count ever sees the ballot.

Two positions, both held by people who know this field well, and **neither previously backed by published numbers**:

- **It matters a lot.** If the primary doesn't eliminate [vote-splitting](split_voting/README.md), the general's accuracy is capped by whatever the primary already distorted. Pair a top-4/5 open primary with a good method or don't bother.
- **It matters little.** With *four* candidates advancing, it's unlikely the consensus candidate fails to advance even under Plurality. Four slots is a lot of slack.

## The structural fact that makes this the whole question

With a **Condorcet general** (Ranked Robin / Consensus Choice), a full-field [Condorcet winner](../00_start_here/topics/condorcet/README.md) who *advances* **always wins**. They beat every candidate head-to-head, so they beat every survivor, so they are the Condorcet winner of the surviving subset too.

Therefore **the qualifying round is the only place the consensus winner can be lost.** Not a footnote to the proposal — the entire accuracy question. (The simulation asserts this as a test invariant rather than assuming it. It stops holding for a STAR general, where a Condorcet winner can advance and still miss the score-based top two — run `--general star` to see that mode.)

## The measured answer

From [`primary_method_simulation.py`](../06_Other/simulations/primary_method_simulation.py): 9-candidate open field, 501 voters, 2000 trials per cell, seed 20260723, general = Ranked Robin. Voters' utilities are sampled from a 2-D [spatial model](../00_start_here/topics/spatial_voting_model.md) and every ballot is derived from them.

**How often the qualifying round drops the Condorcet winner:**

| Qualifying method | top 2 | top 3 | **top 4** | top 5 |
|---|:--:|:--:|:--:|:--:|
| **Plurality (Choose-One)** | 45.5% | 30.7% | **17.3%** | 11.8% |
| Approval (score ≥ 4) | 5.9% | 1.3% | **0.4%** | 0.1% |
| Score (STAR's scoring round) | 3.5% | 0.5% | **0.0%** | 0.1% |
| Ranked Robin | 0.0% | 0.0% | **0.0%** | 0.0% |

End-to-end [VSE](../00_start_here/topics/what_makes_a_good_winner.md) at top-4: Plurality **0.962**, Approval **0.997**, Score **0.999**, no primary at all **0.999**.

## What it means

**1. Four slots is real slack — and still not enough.** The optimistic position is directionally right: Plurality's drop rate falls from 45.5% at top-2 to 17.3% at top-4. Advancing more candidates genuinely helps. But **one election in six** is not "very unlikely," and the candidate being discarded is precisely the one the reform is built to elect, lost in its own first round before the pairwise count runs.

**2. The fix is nearly free.** Swapping Choose-One for **Approval** in the qualifying round takes 17.3% → **0.4%** — roughly 40×, for a ballot no harder to mark, explain, or administer, and one that needs no new equipment. Score is comparable; a Condorcet qualifying round is 0% by construction. **There is no accuracy argument for Choose-One in the primary and a large one against it.**

**3. The method matters far more than the number of slots.** This is the practically useful finding:

| Change, from a Plurality top-4 baseline | Drop rate |
|---|:--:|
| baseline | 17.3% |
| advance one *more* candidate (top-5) | 11.8% |
| keep top-4, switch to **Approval** | **0.4%** |

Debating "should four or five advance?" is optimizing the wrong variable. Fixing the *method* is an order of magnitude more effective than adding slots.

**4. Polarization cuts both ways.** The factional model (voters clustered around three centers) is *gentler* on Plurality — 7.8% at top-4, since clustered voters fragment the centrist's support less. But it's also the only model where the **looser** approval cutoff is *worse* than the tighter one (≥3: 4.0% vs ≥4: 2.4%). Approval's cutoff is a modelling choice that moves the answer, exactly as in [How often do STAR and Approval disagree?](star_vs_approval_divergence.md).

## Caveats — read before quoting

- **Sincere ballots only**, no strategy, no candidate entry/exit effects.
- **Pre-primary drop-out pressure is not modelled** — parties pressuring co-partisans to withdraw *before* the qualifying round, the real Alaska failure mode. This is the biggest gap, and it cuts *toward* broad-support methods, so the numbers above understate the case for a good primary method rather than overstating it.
- **"Accuracy" means matching the full-field Condorcet winner.** That's the right benchmark for a Condorcet general, but it bakes in a Condorcet definition of the right answer; the VSE column is the utilitarian cross-check. See [three notions of "winner"](../00_start_here/STAR_Voting/properties_and_limits/STAR_three_winner_notions.md).
- **Cycles are counted, not hidden.** A Condorcet winner exists in ~99% of spatial, ~93% of factional, and ~54% of noise-model elections; rates are computed over elections where one exists.
- Fixed tiebreak (stable sort → lower candidate index) rather than a lot draw — identical across methods, so cross-method comparison stays fair.
- **Always report the model, field size, and N with the number.**

## Run it yourself

```bash
uv run 06_Other/simulations/primary_method_simulation.py --selftest
uv run 06_Other/simulations/primary_method_simulation.py
uv run 06_Other/simulations/primary_method_simulation.py --candidates 12 --advance 3 4 5
uv run 06_Other/simulations/primary_method_simulation.py --general star
```

`--selftest` checks four invariants: a Condorcet qualifying round never drops the Condorcet winner; `N ≥ C` advances everyone; an advanced Condorcet winner always wins a Condorcet general; and a hand-built 5-ballot [center squeeze](../00_start_here/RCV_IRV/RCV_IRV_center_squeeze.md) is dropped by a Plurality top-2.

Full sweep across all three electorate models: [simulations README](../06_Other/simulations/README.md#qualifying-round-primary-method-simulation).

## The takeaway for reform design

A two-stage proposal is only as accurate as its *first* stage. That makes "what method does the qualifying election use?" the single highest-leverage unanswered question in any top-N package — more consequential than the cycle tiebreak, more consequential than how many advance. It deserves an answer in the proposal text, not a footnote.

*Sources: [betterchoices.vote/consensus-choice](https://www.betterchoices.vote/consensus-choice) and [/faqs](https://www.betterchoices.vote/faqs) (advocacy — cited for their own proposal's wording, not as a neutral referee), retrieved 2026-07-23. All rates are this repo's own measurement; the simulation is seeded and self-testing, and disagreement with it is welcome and checkable.*
