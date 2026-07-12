# The Gibbard–Satterthwaite theorem — why *no* method is strategy-proof

*The formal reason "just vote honestly" can never be guaranteed. Proved independently by [Allan Gibbard](whos_who_voting_reform.md) (1973) and Mark Satterthwaite (1975), it is — with [Arrow's theorem](what_makes_a_good_winner.md) — one of the two impossibility results that anchor voting theory. This page states it plainly, lists the escape hatches, and explains why it reframes the whole strategy debate (including STAR's).*

**Level: 301.** Companion: [Strategic voting across the Equal Vote methods](strategic_voting.md) · [What makes a voting method good?](what_makes_a_voting_method_good.md).

## The statement, in plain terms

> For a single-winner election with **three or more** candidates, **any** voting rule that is **deterministic**, **non-dictatorial**, and can elect **any** of the candidates is **manipulable**: there is at least one situation in which some voter can get a result they prefer by voting *insincerely*.

In one line: **no reasonable ranked voting method is strategy-proof.** There is no method where honesty is *always*, provably, the best move for every voter in every situation. Manipulation is always *possible* — the theorem says nothing about whether it's *easy*, *common*, or *safe*, which is the part that actually matters (below).

## What "manipulable" does and doesn't mean

- **It means:** somewhere in the space of all possible elections, there's a profile where one voter, by misrepresenting their preferences, flips the winner to someone they like better. One counterexample is enough to make a method "manipulable."
- **It does *not* mean:** that manipulation is easy to pull off, that it happens often in real elections, that the manipulator can know when to do it, or that it doesn't backfire. Those are empirical questions about a *specific* method — and they're where methods differ enormously.

## The escape hatches (what the theorem quietly assumes)

A method can dodge Gibbard–Satterthwaite only by giving up one of its premises:

- **Two candidates.** With only two options there's nothing to manipulate — honest majority rule is strategy-proof. (It's the ≥3 case that bites.)
- **Dictatorship.** If one voter's ballot always decides, no one else can manipulate — strategy-proof, and useless.
- **A restricted outcome set** (not "onto"). A rule that can only ever elect one fixed candidate is trivially unmanipulable.
- **Randomization.** [Gibbard's 1977 follow-up](https://en.wikipedia.org/wiki/Gibbard%27s_theorem) shows the *only* strategy-proof processes are random mixtures of dictatorships and pairwise votes — e.g. **random ballot** (pick one voter's ballot at random). Strategy-proof, but nobody wants elections decided by lottery.

Every *usable* method fails at least one escape condition — so every usable method is manipulable. That's the whole point.

## Does it apply to STAR, Approval, and Score?

Strictly, Gibbard–Satterthwaite is about **ranked (ordinal)** rules, so it doesn't *literally* cover cardinal ballots. But that's a technicality, not a loophole:

- Voters ultimately care about **who wins** — an ordinal preference over outcomes — so the incentive to misreport survives the switch to scores. **[Gibbard's more general 1973/1978 game-form theorem](https://en.wikipedia.org/wiki/Gibbard%27s_theorem)** covers cardinal mechanisms too.
- And concretely, cardinal methods have their own well-known strategy: **exaggeration** (score your side 5, everyone else 0), which pushes Score toward Approval, and **bullet voting**. STAR's automatic runoff is specifically designed to *blunt* that incentive — but it does not *eliminate* it, because no method can. See [strategic voting](strategic_voting.md).

So the honest statement covers all four of this library's methods: **Approval, STAR, Ranked Robin, and RCV-IRV are all manipulable.** None is strategy-proof. (It's one row you won't find passed in [Criteria at a glance](criteria_at_a_glance.md), because *no* method passes it.)

## Why this reframes the entire strategy debate

This is the theoretical backbone of the repo's honesty stance — **"resistant, not proof."** Because *no* method is strategy-proof, "which voting method can't be gamed?" is the wrong question (the answer is always "none"). The right questions are empirical and comparative:

- **When does honesty pay?** For which method, and under what electorate, is a sincere ballot the best *practical* strategy most of the time?
- **How hard and how risky is manipulation?** Does it require coordination and knowing the result in advance? Does it backfire?

Those are exactly what [Voter Satisfaction Efficiency](election_simulation_models.md) simulations and the [strategic-voting analysis](strategic_voting.md) measure. Gibbard–Satterthwaite doesn't end the debate — it *starts* it correctly, by ruling out the fantasy of an unmanipulable method and forcing the argument onto *degrees* of strategy-resistance. STAR's own advocates concede the point openly; the honest case for any method has to. See [STAR's honest limits](STAR_Voting/STAR_honest_limits.md).

## Relation to Arrow's theorem

Arrow (1951) and Gibbard–Satterthwaite are close cousins — G-S can even be derived from Arrow. Roughly:

- **Arrow** is about *aggregation*: no rule can combine individual rankings into a group ranking while satisfying a short list of fairness conditions.
- **Gibbard–Satterthwaite** is about *incentives*: no rule can make honest voting a dominant strategy.

Two faces of the same fact — **there is no perfect voting method** — which is why every method in this library has an [honest-limits](STAR_Voting/STAR_honest_limits.md) page, and why "it fails criterion X" is a trade-off to weigh, never a disqualification. Deeper math: [the math behind Condorcet](RCV_Ranked_Robin/the_math_behind_condorcet.md) (Arrow & Gibbard–Satterthwaite in context).

## Sources

- A. Gibbard, "Manipulation of Voting Schemes: A General Result," *Econometrica* 41 (1973).
- M. Satterthwaite, "Strategy-proofness and Arrow's Conditions," *Journal of Economic Theory* 10 (1975).
- A. Gibbard, "Manipulation of Schemes That Mix Voting with Chance," *Econometrica* 45 (1977).
- [Gibbard–Satterthwaite theorem (Wikipedia)](https://en.wikipedia.org/wiki/Gibbard%E2%80%93Satterthwaite_theorem) · [Gibbard's theorem (Wikipedia)](https://en.wikipedia.org/wiki/Gibbard%27s_theorem)

## Related

- [Strategic voting across the Equal Vote methods](strategic_voting.md) — the practical "when does it pay?" side
- [What makes a good winner?](what_makes_a_good_winner.md) · [What makes a voting method good?](what_makes_a_voting_method_good.md) — Arrow and the trade-off framing
- [Criteria at a glance](criteria_at_a_glance.md) — the pass/fail map (and why no method aces it)
- [Glossary](GLOSSARY.md) · [Who's who in voting methods](whos_who_voting_reform.md) (Gibbard, Satterthwaite)
