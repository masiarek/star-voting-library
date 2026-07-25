# May's Theorem — why two candidates are easy, and everything hard starts at three

*Every impossibility result in this library is the answer to a question that only becomes interesting at **three** candidates. With exactly **two**, there is no debate to have: majority rule is not merely a good choice, it is **provably the only** rule meeting three conditions almost nobody would give up. That's May's Theorem (1952), and it is the positive result the negative ones are measured against. It also supplies the fairest available framing of Choose-One voting: **First-Past-The-Post is not an unreasonable system — it is a two-candidate system, deployed in a world with more than two candidates.***

→ Related: [Arrow](arrow_theorem_and_star.md) — what happens when you relax "only two" · [social welfare function](social_welfare_function.md) — the object Arrow quantifies over · [Gibbard–Satterthwaite](gibbard_satterthwaite_theorem.md) · [Plurality](plurality.md) · [two-party dominance](two_party_dominance.md) · [the spoiler effect](spoiler_effect.md).

---

## The theorem

Two alternatives, `x` and `y`. Each voter reports a preference for `x`, a preference for `y`, or indifference. A rule takes those reports and returns a group decision. **May's Theorem:** simple majority rule is the *unique* rule satisfying all of —

1. **Decisiveness** — the rule always returns a result, for every possible profile of votes.
2. **Anonymity** — permuting *who* cast which vote never changes the outcome. No voter counts more than another; the rule sees the tally, not the names. This is **one person, one vote** stated as mathematics.
3. **Neutrality** — swapping the *names* of the two alternatives swaps the result. Neither option is the default; the rule has no thumb on the scale.
4. **Positive responsiveness** — if the group is tied and one voter switches toward `x`, then `x` now wins outright. (Strictly stronger than [monotonicity](monotonicity), which only requires that extra support never *hurts*.)

May proved these conditions **independent** — drop any one and majority rule is no longer unique. That's the point of his title.

**Why the fourth condition is the strong one.** Plain [monotonicity](monotonicity) is enough to exclude the frankly perverse — *elect whichever alternative receives an odd number of votes* is the textbook specimen it kills. **Positive responsiveness does strictly more: it also breaks every tie that isn't mathematically forced.** With an odd number of voters that's enough to make majority rule *resolute* — it always names one winner. With an even number it isn't, and can't be: the 50/50 split is a tie no axiom can dissolve. That single exception is the two-candidate face of a general result — **no anonymous, neutral, Pareto rule is resolute on an even electorate** — worked out in [Ties Are Forced](ties/ties_are_forced.md).

## What each condition rules out

The conditions are worth reading as a list of things you *could* build, and why you generally don't:

| Give up… | …and you can have | Which is |
|---|---|---|
| **Anonymity** | weighted voting, shareholder votes, a dictatorship, the electoral college | sometimes intended, usually not |
| **Neutrality** | a **supermajority requirement**, a tie-goes-to-the-incumbent rule, jury unanimity | often *deliberate* |
| **Positive responsiveness** | rules that can ignore an added vote | rarely wanted |
| **Decisiveness** | a rule that sometimes returns "no decision" | occasionally honest |

The neutrality row is the interesting one. **A ⅔ threshold to amend a constitution is not neutral** — it privileges the status quo by construction. That isn't a bug someone failed to notice; it's the entire purpose. May's Theorem is what lets you name the price precisely: a supermajority rule buys status-quo protection and pays for it in neutrality, and nothing else about majority rule needs to change. Being able to state the trade exactly is more useful than arguing about whether supermajorities are "fair."

**Legislatures break both axioms routinely, and mean to.** A chamber voting `{yes, no}` on a bill is running a two-alternative rule, so May applies directly — and real legislative rules fail his conditions on purpose. Any status-quo bias (a supermajority to amend, a filibuster, a veto override bar) is a **neutrality** failure. A **bicameral** legislature is an **anonymity** failure: a senator's vote is not interchangeable with a representative's, because passage requires both chambers. So "this rule violates May's conditions" is a description, not an indictment. The axioms are how you *name* a design choice, not a test it has to pass.

## Why this reframes Choose-One fairly

Here is the payoff, and it matters for how this repo argues.

**With exactly two candidates, [Choose-One / FPTP](plurality.md) *is* majority rule** — and therefore, by May, the provably correct rule. So Choose-One is not stupid, badly designed, or the product of people who hadn't thought about it. Within the domain it was built for, it is optimal, and no reform can improve on it.

Every pathology this library documents is a symptom of **running that two-candidate rule on three or more candidates**: the [spoiler effect](spoiler_effect.md), [vote splitting](../../method_comparisons/split_voting/README.md), [wasted votes](wasted_votes.md), the strategic pressure to abandon a favorite. None of these exist at two candidates. All of them appear the moment a third enters.

That is a considerably stronger argument than "FPTP is broken," and a fairer one — it identifies the actual defect (a domain mismatch) instead of impugning the rule. It also explains [two-party dominance](two_party_dominance.md) as something other than an accident: a system well-behaved only at two candidates exerts continuous pressure toward exactly two, and Duverger's law is that pressure observed. The two-party equilibrium is FPTP being pushed back into the domain where May's theorem applies.

**The one-liner:** *Choose-One isn't the wrong answer. It's the right answer to a question with only two options — and we stopped having those.*

## At two candidates, every method here collapses to majority rule

Worth checking, because it's easy to assume the methods differ everywhere:

- **[STAR](../STAR_Voting/)** — with two candidates both are automatically finalists, so the scoring round decides nothing and the [automatic runoff](../STAR_Voting/the_count/) is a straight pairwise majority vote.
- **[RCV-IRV](../RCV_IRV/)** — no one can be eliminated before someone has a majority; round one settles it.
- **[Ranked Robin](../RCV_Ranked_Robin/)** — one pairwise matchup *is* the whole round robin.
- **[Approval](../Approval_Voting/)** — among voters who distinguish the two, it is majority rule; approving both or neither abstains from the pair.

So the repo's own convention that [two-candidate intro files suppress the finalists matrix](../../CLAUDE.md) — because it merely echoes the runoff — isn't a display quirk. It's May's Theorem showing up in the output: at two candidates there is only one thing any of these methods can be doing.

**The honest limit.** This makes May's Theorem a *baseline*, not an argument for any method. It says nothing whatsoever about which multi-candidate rule is better, because its whole content evaporates at three. Anyone citing May to defend a particular reform has overreached.

## The hinge into Arrow

Now relax exactly one condition — the third, "only two alternatives" — while keeping anonymity and neutrality. That single move is what turns a clean uniqueness theorem into an impossibility theorem.

At three or more alternatives you need a rule that produces a coherent group *ranking*, not just a binary verdict — a [social welfare function](social_welfare_function.md) — and Arrow proves that no such rule can be weakly Paretian and IIA without being a dictatorship. Pairwise majority rule itself survives at three candidates only by ceasing to be a ranking at all: it can [cycle](../RCV_Ranked_Robin/cycle_resolution.md).

Read as a pair, the two theorems say something sharper than either alone:

> **Majority rule is uniquely right for two alternatives (May), and cannot be coherently extended to three (Condorcet's paradox, then Arrow).**

Everything else in voting theory — every method in this repo, every criterion in the [criteria table](criteria_at_a_glance.md) — is a proposal for what to do about that gap. There is no neutral extension waiting to be found; that's the theorem. So the choice among [STAR](../STAR_Voting/), [Ranked Robin](../RCV_Ranked_Robin/), [Approval](../Approval_Voting/), and the rest is a choice about **which properties of majority rule you most want to preserve** once you've been told you can't keep them all.

## Sources

- Kenneth O. May, "A Set of Independent Necessary and Sufficient Conditions for Simple Majority Decision," *Econometrica* 20(4), 1952, pp. 680–684. **Lean:** neutral; a uniqueness proof.
- William S. Zwicker, "Introduction to the Theory of Voting," in *Handbook of Computational Social Choice* (Brandt, Conitzer, Endriss, Lang & Procaccia, eds., Cambridge University Press, 2016), §2.1 and §2.4 — the framing used on this page, including the observation that multicandidate voting is precisely May's third condition relaxed. **Lean:** neutral; the standard academic reference.
- [May's theorem (Wikipedia)](https://en.wikipedia.org/wiki/May%27s_theorem) — for the neutral statement and the independence of the conditions.

## Related

- [Does Arrow apply to STAR?](arrow_theorem_and_star.md) · [Social welfare function](social_welfare_function.md) · [Gibbard–Satterthwaite](gibbard_satterthwaite_theorem.md)
- [Plurality / Choose-One](plurality.md) · [two-party dominance](two_party_dominance.md) · [the spoiler effect](spoiler_effect.md) · [wasted votes](wasted_votes.md)
- [Glossary](../GLOSSARY.md) — anonymity, neutrality, positive responsiveness · [Who's who](whos_who_voting_reform.md)
