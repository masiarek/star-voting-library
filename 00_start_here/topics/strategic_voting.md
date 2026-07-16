# Strategic Voting Across the Equal Vote Methods

**Strategic voting** (also *tactical* or *insincere* voting) is casting a ballot that doesn't reflect your honest preferences, in the hope of a better outcome. The [Equal Vote Coalition](https://www.equal.vote) treats **honesty** as a core test of a voting method: *can a voter safely express her sincere opinion, and how much does the method reward insincerity?*

Two facts frame everything below:

- **No method is immune.** The [Gibbard–Satterthwaite theorem](gibbard_satterthwaite_theorem.md) proves that *every* ranked or scored method has *some* scenario where a voter can gain by voting insincerely. So "you can construct a strategy" isn't a mark against a method — the real questions are **how often it pays, whether it's actionable, and whether it backfires.**
- **Honest ≠ the same as strategy-proof.** A method can *fail* a criterion on paper (STAR fails Later-No-Harm, for instance) yet still make honesty the *practical* best play. This page separates the paper property from the practical incentive, and tries to be even-handed to all three [Equal Vote methods](choosing_among_evc_methods.md) — STAR, Approval, and Ranked Robin.

External references worth reading directly: the Equal Vote Coalition's **[Strategic STAR](https://www.equal.vote/strategic-star)** and **[Gaming the Vote](https://www.equal.vote/gaming_the_vote)**, and STAR Voting's **[Is STAR vulnerable to strategic voting?](https://www.starvoting.org/strategic_voting)**. (These are advocacy sources; this page reports their claims and evidence while flagging the honest counterpoints.)

## The four kinds of insincere vote

The Equal Vote taxonomy names four distinct ways to vote insincerely on a rated or ranked ballot. The names matter — people argue past each other by confusing them:

| Type | Also called | What the voter does |
|---|---|---|
| **Strong insincerity** | **Favorite betrayal**, *compromising*, *decapitation* | Gives someone a **higher** score/rank than their true favorite |
| **Weak insincerity** | **Burial**, *skipping* | Keeps the favorite on top, but ranks/scores a *less*-preferred candidate **below** an even-less-preferred one |
| **Restrictive sincerity** | **Tactical minimization**, *bullet voting*, *truncation* (down-voting) | **Lowers** support for non-favorites (e.g. scores everyone but the favorite a 0) |
| **Expansive sincerity** | **Tactical maximization** (up-voting) | **Raises** support for non-favorites (e.g. gives a strong front-runner a 5 to hedge) |

Only the first two distort *preference order*; the last two only distort *how much*. That distinction is why fully-expressive methods (STAR, Score) face the bottom two while choose-one and ranked methods face the top two.

## How each method handles each strategy

This is a comparison, not a verdict — each method resists some strategies well and is exposed to others.

| Strategy | Choose-One / IRV (the contrast) | Approval | Ranked Robin (Condorcet) | STAR |
|---|---|---|---|---|
| **Favorite betrayal** | **Strongly incentivized** (choose-one) or possible ([IRV center squeeze](rcv_irv_vs_star.md)) | Not needed — approve favorite freely | Rare; sincere ranking usually best | Rare; runoff makes it backfire |
| **Burial** | n/a (choose-one) / possible in IRV | n/a (no order) | **The main worry** — you can bury a rival | Possible but rarely pays (see below) |
| **Bullet voting** (min) | is the ballot | **The central tension** — approve only your favorite? | n/a (must rank) | Runoff discourages it |
| **Tactical maximization** (max) | n/a | **The other side of the tension** — approve a front-runner you dislike? | n/a | Runoff discourages it |
| Main honesty question | "Is my favorite electable?" | "Where do I draw my approval line?" | "Do I dare bury a rival?" | "Do I dare mis-order the top two?" |

A few honest observations from that table:

- **Approval's strategy is the most *actionable*.** Its one genuine dilemma — the **approval threshold**: do you approve only your favorite (bullet voting) or also the tolerable front-runner (tactical maximization)? — is easy to reason about, which cuts both ways: simple to use, but also simple to game. Approval never asks you to betray your favorite, which is its real strength. See [Approval's honest limits](../Approval_Voting/approval_honest_limits.md).
- **Ranked Robin's exposure is burial.** Because it's purely ordinal (order, not strength), a faction can in principle *bury* a strong rival below weaker candidates. In practice sincere ranking is usually optimal and Condorcet methods are considered strongly strategy-resistant — but burial is the named risk. See [Ranked Robin's honest limits](../RCV_Ranked_Robin/RCV_RR_honest_limits.md).
- **STAR's exposure is the bottom two, softened by the runoff.** Because scores are summed in round one but treated only as *order* in the runoff, exaggeration has limited upside and real downside (below). STAR does **fail Later-No-Harm** — honestly scoring a second choice *can*, in constructions, help them beat your favorite — which is a genuine, admitted property. See [STAR's honest limits](../STAR_Voting/properties_and_limits/STAR_honest_limits.md).

## Why exaggeration tends to backfire in STAR

The mechanism is worth understanding because it's STAR's clearest honesty argument, and CPython's Tim Peters put it crisply: STAR *"uses each [system] to counter the worst of the other."* Scores are **cardinal** (summed) when choosing the two finalists, then **ordinal** (just which is higher) in the runoff:

- **Betray your favorite** (score a "lesser evil" above them) → you might knock your favorite out of the runoff, and your full runoff vote then goes to the lesser evil instead. Backfires.
- **Bury a strong consensus candidate** (the [FairVote hypothesis](https://www.fairvote.org/explaining_fairvote_s_position_on_star_voting)) → to do this you must *raise* someone you like *less*, which raises the chance your own favorite gets squeezed out of the top two. And if several factions all try it, all but one end up worse off than if they'd been honest.
- **Bullet-vote or exaggerate the scale** → the runoff only reads *order*, so a 5-vs-4 counts the same as 5-vs-0; you gain nothing in the runoff by inflating, and you lose your say among candidates you flattened together.

The honest limit on this argument: it says exaggeration *rarely pays and often backfires* — **not** that STAR is favorite-betrayal-proof. It isn't. The measured version is the brute-force simulation in [Favorite Betrayal — Voting 301](../STAR_Voting/properties_and_limits/favorite_betrayal_voting_301.md), which finds STAR and IRV fail the favorite-betrayal criterion at *about the same low rate* — STAR's real edge is that a betrayal **backfires far more often than it works**, not that it never works.

## What the simulations say

Strategic incentive is often summarized as a ratio — how often a strategic vote *helps* the voter vs. how often it *backfires*. From Dr. [Jameson Quinn](in_memoriam_jameson_quinn.md)'s [Voter Satisfaction Efficiency](https://electionscience.github.io/vse-sim/VSE/) work:

- **Choose-One Plurality ≈ 17:1** — strategy almost always pays (the "lesser evil" problem).
- **IRV ≈ 3:1** — strategy pays about three times as often as it backfires.
- **STAR ≈ 1:1** — a strategic vote is about as likely to backfire as to help, so it isn't worth attempting.

Two nuances kept for honesty: (1) these are model outputs — the exact numbers move with the electorate model, field size, and assumptions (this repo's own [simulations](../../06_Other/simulations/README.md) make the same point about not quoting a bare rate); (2) a separate finding is that STAR, IRV, Score, and Condorcet methods all produce **more representative outcomes when voters are honest** — the difference is whether the method also *incentivizes* honesty at the individual level, where STAR and Condorcet score well and IRV less so.

**Actionability** is the practical clincher: even where a STAR or Condorcet strategy exists, it only bites in a close three-way tie, and executing it needs near-perfect polling on *everyone's* scores — and if one faction tries it, rivals can respond, making the outcome *less* predictable. That's why the honest advice under STAR, Condorcet, and 3-2-1 is simply *show your sincere preference order.*

## The even-handed bottom line

- **Approval** never makes you betray a favorite — its only tactic is where to set your approval line, which is easy to reason about (a strength and an exposure).
- **Ranked Robin** is strongly strategy-resistant in practice; its named risk is burial, and it can't express *no preference* as gracefully as a scored ballot.
- **STAR** fails Later-No-Harm on paper, but its cardinal-then-ordinal runoff makes exaggeration and burial usually backfire, and its two-round count makes *why honesty pays* unusually easy to explain.

No method removes strategy entirely (Gibbard–Satterthwaite guarantees that). Among the Equal Vote methods the differences are about *how actionable* the strategy is and *whether it pays* — and on those measures all three are dramatically safer than the choose-one status quo.

**See also:** [Choosing among the Equal Vote methods](choosing_among_evc_methods.md) · [Favorite Betrayal — Voting 301](../STAR_Voting/properties_and_limits/favorite_betrayal_voting_301.md) · [Residual vote-splitting](../STAR_Voting/properties_and_limits/residual_vote_splitting.md) · [Scores vs. ranks (cardinal vs ordinal)](../scores_and_ranks/scores_vs_ranks.md) · [STAR FAQ](../STAR_Voting/getting_started/STAR_FAQ.md) · [Glossary](../GLOSSARY.md)
