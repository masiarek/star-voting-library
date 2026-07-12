# The spatial model — voters and candidates as points on a map

*The single most useful mental picture in voting theory. Put every voter and every candidate at a **point** — on a left–right line, or a 2-D map of issues — and assume each voter prefers whoever is **closer** to them. That one idea explains the political spectrum, predicts who wins under each method, and is why the word **"spatial"** keeps showing up in this repo's simulations. This page is the concept; the simulation menu that uses it is [Election simulation models](election_simulation_models.md).*

**Level: 201 → 301.**

## The picture

Imagine political opinion as a **line** — left on one end, right on the other. Every voter sits somewhere on it (their ideal point); so does every candidate. A voter likes a candidate to the degree they're **near**: closeness = agreement, distance = disagreement. Formally, a voter's **utility** for a candidate is (minus) the **distance** between their points.

- **One dimension** = the familiar left–right **[political spectrum](https://en.wikipedia.org/wiki/Political_spectrum)**.
- **Two dimensions** adds a second axis (say economic × social, or libertarian–authoritarian) — a *map* instead of a line.
- **More dimensions** for more independent issues. Real electorates seem to need only a **few** dimensions to explain most behavior.

The classic intuition is **[Hotelling's](https://en.wikipedia.org/wiki/Hotelling%27s_law) ice-cream vendors**: two carts on a beach each edge toward the middle to be closest to the most beachgoers. That "move to the center" pressure is the spatial model in one sentence.

## The one theorem to know: the median voter

Put voters on a line and ask "is there a candidate who beats every other head-to-head?" The answer, under mild assumptions, is **yes, and it's the candidate nearest the *median* voter** — the [**median voter theorem**](https://en.wikipedia.org/wiki/Median_voter_theorem) (Duncan [Black](whos_who_voting_reform.md), 1948; central to Anthony Downs's *Economic Theory of Democracy*, 1957).

Why: any candidate to the median's left is beaten by one just to their right (a majority — the median plus everyone to the right — is closer to the righter one), and vice versa. So in one dimension a **[Condorcet winner](topics/condorcet/) always exists**, and it's the center. That single fact drives most of what follows.

## Why it matters — the model *predicts* how methods behave

Because the spatial model tells you *who the Condorcet winner is* (the center), it tells you which methods will find them and which will miss:

- **[Ranked Robin](RCV_Ranked_Robin/ranked_robin.md) / Condorcet methods** elect the median candidate by construction — they're built to find the beats-all winner.
- **STAR** usually elects near the median too: the broadly-liked center piles up scores and wins the runoff.
- **RCV-IRV can *squeeze* the center out.** A centrist is many voters' *second* choice but few voters' *first*, so IRV eliminates them early — even though they'd beat everyone head-to-head. That's **[center squeeze](RCV_IRV/RCV_IRV_center_squeeze.md)**, and it's fundamentally a *spatial* phenomenon: you can only see it clearly on the map. (Alaska 2022 is the real-world case.)
- **[Plurality](plurality.md)** splits one side and hands it to the other — the [spoiler effect](spoiler_effect.md), also easiest to see spatially.

So "which method elects the compromise vs. squeezes it" isn't a matter of opinion in the spatial model — it's geometry.

## Yee diagrams — the method's fingerprint

[Ka-Ping Yee](http://zesty.ca/voting/) turned the 2-D spatial model into pictures: fix a few candidates on the map, then color each point by *who would win if the voters were centered there*. Each method produces a distinctive **map of winner-regions** — Condorcet/STAR carve clean regions around the central candidate; IRV's map has jagged, non-monotonic patches where nudging the electorate flips the winner unexpectedly. A Yee diagram is a method's visual fingerprint, and it's the most intuitive proof that methods genuinely differ.

## Why simulations lean on it (the "realistic" model)

This repo's simulations ([`fbc_simulation.py`](../06_Other/simulations/fbc_simulation.py), [`star_vs_approval_divergence.py`](../06_Other/simulations/star_vs_approval_divergence.py)) offer two electorate models, and **spatial is the realistic one**: draw voters from a bell curve on the map, candidates as points, utility = −distance. Empirical work finds spatial models explain **most** real voting behavior, which is why VSE / Bayesian-regret studies use them. The contrast model — **[impartial culture](election_simulation_models.md)** (every preference independent and random) — has *no* geometry, manufactures far more paradoxes than reality, and is treated as an adversarial stress test. When a simulation here reports "spatial ~12%, impartial ~23%," that gap *is* the model dependence — see [simulate utilities, not ballots](simulate_utilities_not_ballots.md).

## The honest limits

The spatial model is a **lens, not reality**:

- **Valence / quality is missing.** Voters also care about competence, honesty, charisma — things that aren't a "position." Pure distance ignores them.
- **How many dimensions, and which?** Results can hinge on the dimensionality and on how much each axis *weighs* (salience). One-dimensional results (a guaranteed Condorcet winner) can break in higher dimensions — where cycles reappear.
- **It can suppress the hard cases.** Precisely because a 1-D spatial model guarantees a Condorcet winner, it makes **[cycles](RCV_Ranked_Robin/cycle_resolution.md) nearly impossible** — so a purely spatial simulation never stress-tests cycle-resolution. (Impartial culture over-produces them; the truth is between.)
- **Real ballots aren't utilities.** Distance gives a *utility*; turning it into a ballot (min-max scores, an approval cutoff, a ranking) is a separate modeling step — the one that actually drives method differences.

So: use the map to build intuition and to *predict*, then check the prediction against countable elections and against a second, adversarial model. The geometry is a guide, not a verdict.

## Related

- [Election simulation models](election_simulation_models.md) — the full menu (spatial is model **B**), with the math prerequisites
- [Simulate utilities, not ballots](simulate_utilities_not_ballots.md) — why you sample spatial *utilities* and derive ballots
- [Center squeeze](RCV_IRV/RCV_IRV_center_squeeze.md) · [What makes a good winner?](what_makes_a_good_winner.md) — where the spatial picture pays off
- External: [median voter theorem](https://en.wikipedia.org/wiki/Median_voter_theorem) · [Ka-Ping Yee's voting-simulation diagrams](http://zesty.ca/voting/) · [cdsmith, *Simulating Elections with Spatial Voter Models*](https://cdsmithus.medium.com/simulating-elections-with-spatial-voter-models-1ff50892390)
