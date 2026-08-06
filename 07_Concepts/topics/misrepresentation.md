# Misrepresentation — the measure that hands Borda the trophy, and why that's the lesson

*A 301 theory page, and the other half of the paper that started [distortion](distortion.md). Having proved that **no** ranked rule is ever perfect, Procaccia & Rosenschein went looking for a model where possibility results exist — and found one by borrowing **misrepresentation** from Monroe's proportional-representation work: assume each voter's dissatisfaction with a candidate is simply that candidate's **rank position** on their ballot. Under that assumption the impossibilities lift and every method gets a finite score. **Borda scores a perfect 1.** That result is worth knowing, and worth being suspicious of, for exactly the same reason — because under this measure the Borda count and the thing being measured are the same arithmetic.*

**Level: 301 · deep dive** Builds on [distortion](distortion.md) (301) — read that first; this page assumes its vocabulary.

Companions: [Same ranks, different utilities](../../method_comparisons/same_ranks_different_utilities/) — the same paper's impossibility, counted on three ballots · [Cardinal utility](cardinal_utility.md) — whether the numbers assumed here exist at all · [When a criterion is built to fit the method](condorcet/ordered_majority_rule_irv.md) — the pattern this page is a case study in · [ABC rules & the utilitarian–egalitarian spectrum](../../04_Approval/01_Learn/Multiwinner_Approval/abc_rules_spectrum.md) — where Monroe's idea lives in this repo already.

---

## The move: restrict the utilities until answers exist

The [distortion](distortion.md) framework asks what a ranked rule costs you when voters have arbitrary utilities that merely sum to a fixed total. The answer, in that unrestricted setting, is bleak: no rule is perfect ([even at 3 voters and 2 candidates](../../method_comparisons/same_ranks_different_utilities/)), several familiar rules are unbounded, and computing the loss is NP-complete.

So restrict the utilities. **Misrepresentation** — Monroe's measure, from his 1995 work on fully proportional representation — says a voter's unhappiness with a candidate is just *where that candidate sits on their ballot*:

> Voter *i*'s misrepresentation of candidate *j* is **μⁱⱼ = (rank of j on i's ballot) − 1.** Top choice → 0. Second → 1. Last of *m* → *m* − 1. A candidate's total is **μⱼ = Σᵢ μⁱⱼ**, and the best candidate is the one who minimizes it.

Then, exactly as with distortion, a rule's misrepresentation is the **worst-case ratio** between the winner's total and the best candidate's total.

Notice what this quietly does. Every voter now has the *same* utility scale — a permutation of 0, 1, …, m−1 — so the ballot determines the utilities completely, with no slack for the adversary to exploit. The intensity question that drives the whole distortion literature is not answered here; it is **assumed away**. That is the price of the possibility results below, and it should be quoted with them.

The paper is candid that this is a modelling convenience with a natural home: it works when candidates really are interchangeable-but-for-position — its own example is **meeting scheduling**, where a schedule conflicting with one of your requirements is genuinely "one worse" than a schedule conflicting with none. Elections between human beings are not obviously that kind of problem.

## The results

| Voting protocol | Misrepresentation | In this library's terms |
|---|---|---|
| **[Borda](ranked_ballot_methods_zoo.md)** | **1** — optimal | The rank-sum rule; see the catch below |
| Veto (vote against one) | **unbounded** | Not used in practice; the cautionary row |
| **[Plurality](plurality.md)** | **= m − 1** | Choose-one — loss grows with the field |
| Plurality with Runoff | **= m − 1** | Top-two runoff — *no better than plain plurality* |
| **Copeland** — i.e. **[Ranked Robin](../../05_Ranked_Robin/01_Learn/ranked_robin.md)** | **≤ m − 1** | Best of the non-Borda rules here |
| Bucklin | ≤ m | The graduated-majority method |
| Maximin (Minimax) | ≤ 1.62 (m − 1) | |
| **STV** ⇒ **[RCV-IRV](../../06_Other/RCV_IRV/concepts/README.md)** single-winner | **≤ 1.5 (m − 1)** | Elimination is the costliest ranked count here |

Two rows deserve a second look.

**Plurality with Runoff buys nothing.** Adding a second round to choose-one leaves the bound exactly where it was, at m − 1. A runoff fixes a *legitimacy* problem (the winner clears 50% of the final pair), not an *information* problem — the first round still threw away everything below your favorite. Worth remembering whenever top-two runoff is offered as the moderate reform.

**Ranked Robin beats instant runoff, again.** Copeland's m − 1 sits below STV's 1.5(m − 1), and this is the *second* framework to order them that way: under [metric distortion](distortion.md), Copeland is bounded by a constant (≤ 5) while STV/IRV's bound grows with the field. Two different models, built by different authors a decade apart, on different assumptions — same ranking. When results agree across models that disagree about everything else, that's the closest thing this literature offers to a robust finding. Same ballot, better count.

## The catch: the measure *is* the Borda count

Borda's perfect score is not a discovery about Borda. It is arithmetic.

The paper proves it in the sharpest possible form. **Proposition 5:** a scoring rule has misrepresentation exactly 1 — always elects the misrepresentation-minimizing candidate — **if and only if** its points are *affine in rank*, α_l = −a·l + b. That is the definition of Borda (up to shifting and scaling). Rearranged: rules that are Borda score 1; rules that are not Borda score worse than 1; and there is nothing in between.

Look at why. Misrepresentation totals a candidate's rank positions. The Borda count totals a candidate's rank positions, upside down. **Minimizing μⱼ and maximizing the Borda score are the same operation on the same numbers.** A measure defined as rank-sum will crown the rank-sum rule, and the "proof" of Borda's optimality is a change of sign.

This is the repo's standard debate tell, in a peer-reviewed setting: **[when someone says "method X uniquely satisfies criterion Y," check whether Y was reverse-engineered from X](condorcet/ordered_majority_rule_irv.md).** Here nobody is cheating — Monroe defined misrepresentation for a different purpose (multiwinner representation), and Procaccia & Rosenschein state the affine characterization openly rather than burying it. But the *usable* claim is narrow, and "academics proved Borda is the optimal voting method" is not it. The paper's own next sentence pulls the trophy back: Borda is notoriously easy to manipulate.

So the honest one-liner: **under a rank-based measure of unhappiness, the rank-based rule is optimal by construction, and the interesting question is what happens to every rule that isn't.** The table's other seven rows are the actual content.

## Three more findings worth carrying

**Passing the famous criteria does not bound your loss.** The Veto rule satisfies **participation, monotonicity, and consistency** — three of the most-cited criteria in voting theory — and has *unbounded* misrepresentation (the paper's Remark 3). A rule can be axiomatically well-behaved and still elect a candidate arbitrarily far from the best one. This is the strongest available argument for the repo's position that [criteria tables are a starting point, not a verdict](criteria_at_a_glance.md): criteria are pass/fail questions about *edge cases*, and a bound is a statement about *magnitude*. They measure different things.

**But passing the majority criterion does.** Any rule satisfying the [majority criterion](majority_criterion/) has misrepresentation ≤ 2(m − 1) (Remark 4). A cheap, broad guarantee, and a small formal echo of the [metric argument](distortion.md#how-is-a-bound-of-3-even-possible-the-triangle-inequality-is-smuggled-in-cardinal-information) that majority preference *implies* something about welfare.

**A published erratum, for anyone reading the paper alongside this page.** Proposition 6 is printed as *"F has unbounded misrepresentation iff α₁ > α₂"* — and its own proof establishes the opposite direction. The first half assumes α₁ > α₂ and derives the **finite** bound (m−1)(2α₁−α₂)/(α₁−α₂); the second half assumes α₁ = α₂ and derives ∞. Corollary 5 settles it: Veto (where α₁ = α₂) is the unbounded one. Read the proposition as **bounded iff α₁ > α₂** — a scoring rule keeps a finite bound exactly when it puts *some* daylight between first place and second. Veto, which pays first and second alike, does not.

## Computing it

The complexity results run the opposite way from the general model, which is the point of restricting preferences in the first place:

- In the **general** (distortion) model, the core decision problem — MIN-SCORE-MAX-UTIL — is **NP-complete**, by reduction from Knapsack.
- In the **misrepresentation** model, the analogous problem is solvable in **O(n²m²)** by dynamic programming, and finding the worst-case losing profile is polynomial too.
- For scoring rules with two structural properties the paper names (*popular loser* and *even match* — plurality and veto have both), computing the misrepresentation admits an **FPTAS**: approximable to any ε you like, in polynomial time, via a reduction to cardinality-constrained Knapsack.
- **Open, and still worth someone's time:** characterizing which scoring rules have those two properties, and whether computing distortion for scoring rules is NP-complete in general (the authors conjecture yes; no proof).

## What this page does *not* license you to say

- **"Studies show Borda is the best voting method."** No. Under a rank-sum measure of loss, the rank-sum rule is optimal by construction, it is one of the [most manipulable methods known](strategic_voting.md), and the paper says so on the same page.
- **A misrepresentation number for STAR, Score, or Approval.** There isn't one. The framework analyzes rules that read **rankings**; STAR's winner is not a function of the ranked profile at all ([what a method reads](what_a_method_reads.md)). Same open gap as on the [distortion](distortion.md) page — don't paper over it.
- **"Rankings are fine after all."** The possibility results here are bought by assuming every voter's intensities are 0, 1, …, m−1. That assumption is precisely what the [distortion](distortion.md) model refuses to make, and the [three-ballot impossibility](../../method_comparisons/same_ranks_different_utilities/) shows what it costs when it's false.

## Where Monroe's idea already lives in this repo

Misrepresentation was invented for **multiwinner** representation, and that's where it does its most respectable work. Monroe's rule assigns each elected representative a disjoint quota of voters and minimizes the total misrepresentation of the assignment — the natural partner of **Chamberlin–Courant**, which minimizes it without the quota. Both are in this library already, on the approval side: see the [ABC rules spectrum](../../04_Approval/01_Learn/Multiwinner_Approval/abc_rules_spectrum.md) (AV / PAV / CC / Phragmén, verified with `abcvoting`, which implements `monroe` and `cc` directly) and [the math behind proportional STAR](../../03_STAR_PR/01_Learn/STAR_PR/the_math_behind_proportional_star.md), where the same NP-hardness drives the same move to greedy sequential rules. Reading this page's single-winner ratios next to that spectrum is the clearest way to see that they are one family: pick an unhappiness function, pick an aggregator, and you have named a rule.

## Sources

- Procaccia & Rosenschein, [*The Distortion of Cardinal Preferences in Voting*](https://www.cs.huji.ac.il/~jeff/papers/cia06procaccia.pdf) (CIA 2006, LNAI 4149, pp. 317–331; [Springer](https://link.springer.com/chapter/10.1007/11888874_31)) — §4 and its Table 1 are this page; §3 is the [distortion](distortion.md) page's founding-paper section.
- Monroe, *Fully Proportional Representation*, American Political Science Review 89(4), 1995 — where the misrepresentation measure comes from, and why it is a multiwinner idea first.
- Chamberlin & Courant (1983) — the companion objective, and the one this repo teaches on the [approval side](../../04_Approval/01_Learn/Multiwinner_Approval/abc_rules_spectrum.md).
- Anshelevich, Filos-Ratsikas, Shah & Voudouris, [*Distortion in Social Choice Problems: The First 15 Years and Beyond*](https://www.ijcai.org/proceedings/2021/0589.pdf) (IJCAI 2021) — the survey; useful here mainly for how little the misrepresentation branch was pursued compared with the metric one.

**Lean disclosure:** peer-reviewed AI / multiagent-systems research, no stake in the US reform fight — the neutral tier. Its blind spot is stated above and is not small: the model's central assumption (unhappiness = rank position) is the very thing the [scores-vs-ranks](../scores_and_ranks/scores_vs_ranks.md) argument is about, so results derived from it cannot settle that argument in either direction.

## See also

- [Distortion](distortion.md) — the umbrella page, and the model this one restricts
- [Same ranks, different utilities](../../method_comparisons/same_ranks_different_utilities/) — the founding impossibility, runnable
- [The valuable Condorcet loser](../../method_comparisons/valuable_condorcet_loser/) — the other runnable distortion companion
- [What makes a good winner?](what_makes_a_good_winner.md) · [Criteria at a glance](criteria_at_a_glance.md) · [The ranked-ballot method zoo](ranked_ballot_methods_zoo.md)
- [Cardinal utility](cardinal_utility.md) · [Scores vs. ranks](../scores_and_ranks/scores_vs_ranks.md)
