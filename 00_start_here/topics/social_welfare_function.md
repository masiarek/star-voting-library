# Social welfare function — the object Arrow's theorem is actually about

*Almost every impossibility argument you'll meet turns on a distinction that debate rarely bothers to state: does a voting rule output a **winner**, or a **ranking**? Arrow's theorem is about the second kind. Get the type wrong and you'll either over-apply the theorem ("Arrow proved every method is unfair") or miss why some methods dodge it on a technicality. This page pins down the two objects, states the Pareto and IIA axioms at both levels, and shows the trap: **majority rule is both Paretian and IIA, and escapes Arrow only because it is not a social welfare function at all.***

→ Related: [Does Arrow apply to STAR?](arrow_theorem_and_star.md) — the ordinal/cardinal escape · [Gibbard–Satterthwaite](gibbard_satterthwaite_theorem.md) — the other impossibility · [distortion](distortion.md) — social welfare as a *number* · [criteria at a glance](criteria_at_a_glance.md) · [the math behind Condorcet](../RCV_Ranked_Robin/the_math_behind_condorcet.md).

---

## Two objects, two types

Fix a set of voters `N = {1,…,n}` and a set of candidates `A`. A voter's ballot is a **linear order** on `A` — a strict ranking, no ties. Write `L(A)` for the set of those, and `R(A)` for the set of **weak orders** (complete and transitive, ties allowed). A **profile** `P = (≽₁,…,≽ₙ)` is one ballot per voter.

| | Outputs | Type | Anchoring theorem |
|---|---|---|---|
| **Social welfare function (SWF)** | a whole social *ranking* | `f : L(A)ⁿ → R(A)` | **Arrow (1951)** |
| **Social choice function (SCF)** | a *winner* (or tied set) | `f : L(A)ⁿ → A` | **Gibbard–Satterthwaite (1973/75)** |

The SWF's output is called the **social preference order**. Note the asymmetry in Arrow's setup: individual ballots may *not* contain ties, but the social result *may*. That's a modeling convenience, not a law of nature — real ballots routinely permit equal ranks ([weak ranks](../scores_and_ranks/weak_ranks.md)), and STAR's [Equal Support](../GLOSSARY.md) bucket exists precisely because voters do want to say "these two are the same to me."

Nearly every method taught in this repo is an **SCF** — STAR, Approval, RCV-IRV, Plurality all name a winner. [Ranked Robin](../RCV_Ranked_Robin/) is the interesting hybrid: its pairwise win-loss record *is* a social ranking, and the winner is read off the top of it.

## The two axioms, stated at both levels

Because there are two types of object, each axiom has two readings. Conflating them is the single most common error in criterion tables.

**Pareto / unanimity** ([Vilfredo Pareto](whos_who_voting_reform.md), 1848–1923):

- **SWF (weak Pareto):** if `a ≻ᵢ b` for *every* voter `i`, then `a ≻ b` in the social ranking.
- **SCF (Pareto criterion):** if every voter prefers `a` to `b`, then `b` is not elected. A candidate is **Pareto optimal** if no rival is unanimously preferred over them.
- **Strong Pareto:** all weakly prefer `a`, at least one strictly ⟹ `a ≻ b`. Arrow only needs the weak form — assuming *less* makes the theorem *stronger*.

**Independence of Irrelevant Alternatives (IIA):** the social ranking of `a` vs `b` depends only on how individuals rank `a` vs `b` — never on where anyone puts a third candidate `c`. Violating this is precisely the [spoiler effect](spoiler_effect.md).

**Arrow's theorem.** With `|A| ≥ 3`, every SWF that is weakly Paretian and IIA is a **dictatorship** — there is one voter whose ranking simply *is* the output.

The proof runs on **decisive coalitions**. A coalition `C` is decisive for `a` over `b` if `C` unanimously preferring `a` forces `a ≻ b` socially. Weak Pareto is exactly the statement that the *grand coalition* `N` is decisive — that's the seed. A **Contagion (Field Expansion) Lemma** upgrades "decisive for one pair" to "decisive for all pairs"; a **Splitting (Group Contraction) Lemma** shows any decisive coalition of size ≥ 2 contains a smaller decisive one. Iterate down from `N` and you land on a singleton. Without Pareto there is no nonempty decisive set to start shrinking.

## The trap: majority rule is Paretian *and* IIA

Pairwise majority rule satisfies both axioms, easily. So why isn't it a counterexample to Arrow?

**Because it isn't an SWF.** Its output need not be transitive — the [Condorcet paradox](condorcet/) produces `a ≻ b ≻ c ≻ a`, which is not a weak order, so it isn't in `R(A)` and the function `f : L(A)ⁿ → R(A)` is not well defined. Majority rule escapes Arrow by **failing to have the right type**, not by beating an axiom.

This is the correct frame for [Condorcet methods](condorcet/) generally, and it cuts against a sloppy claim in both directions:

- **Against the critics:** "Condorcet methods sometimes elect nobody" is false for real methods. Bare "elect the Condorcet winner" is a partial rule; [Ranked Robin](../RCV_Ranked_Robin/), Ranked Pairs, and Schulze are *completions* that always return a winner. Any criterion table with a "Condorcet Method — Always a Winner: NO" row needs that row split.
- **Against the advocates:** a completion doesn't dodge Arrow either. Once a Condorcet method always outputs a ranking, it *is* an SWF, and Arrow applies in full — so it must fail IIA or Pareto or be a dictatorship. [Ranked Robin fails IIA](../../01_STAR/iia_cycle_spoiler/), which is exactly where cycle-resolution rules live. Patching the cycle is what *costs* you IIA; it doesn't buy an exemption.

## The asymmetry that keeps Pareto from being oversold

**Pareto forbids; it does not require.** The criterion says non-Pareto-optimal candidates must *not* win. It says nothing about which Pareto-optimal candidate *should*.

[Plurality](plurality.md) satisfies Pareto — a candidate ranked below `X` by everyone gets no first-place votes and can't win — yet plurality routinely elects a poor Pareto-optimal candidate. Passing Pareto is a floor, not a recommendation. Relatedly: **Pareto ⟹ the unanimity criterion** (a candidate holding *every* first-place vote wins), since every rival is then unanimously dominated. The converse fails.

And the sting in the tail: **a dictatorship is Paretian.** The dictator's top choice is never unanimously dominated. That is why Arrow's conclusion is devastating rather than reassuring — the axioms are so mild that dictatorship clears them.

## Who actually fails Pareto

A short list, because "fails Pareto" sounds worse than it usually is — most methods pass:

| Rule | Pareto | Why |
|---|:---:|---|
| Plurality, Borda, IRV, STAR, Ranked Robin | ✓ | unanimous domination survives the count |
| **Dictatorship** | ✓ | the dictator's favorite is never dominated |
| **Imposed / constant rule** ("X always wins"; "everything ties") | ✗ | ignores the ballots entirely |
| **[Sequential pairwise / agenda voting](../other_ranked_methods/agenda_voting.md)** | ✗ | a unanimously-preferred candidate can be eliminated early — runnable at [agenda_voting.md](../other_ranked_methods/agenda_voting.md) |
| **Anti-plurality** | ✗ | on unanimous `A>B>C` it elects A *and* B; B is dominated |
| **[Approval](../Approval_Voting/)** | ✗ | worked: [Felsenthal Ex.6](../../method_comparisons/felsenthal_paradoxes/felsenthal_ex6_pareto.md) |

**Why Approval fails and STAR doesn't** is the instructive pair, and it's a ballot-expressiveness point, not a tabulation one. An approval ballot cannot record a strict preference *within* the approved set, so "every voter prefers A to C" is a fact the ballots never carried and the count cannot honor.

STAR passes, and the argument is short. If every voter scores `a` strictly above `b`, then `a`'s score total strictly exceeds `b`'s — so `b` can only reach the runoff alongside `a`, and there every voter prefers `a`. `b` never wins. Note this leans on the [scoring round](../STAR_Voting/the_count/) and the runoff *together*: the runoff alone wouldn't do it.

## Two senses of "social welfare" — don't cross them

The phrase does double duty, and the repo uses both:

1. **Arrow's SWF** — the *ordinal* object above. A function producing a social ranking. No utilities anywhere; Arrow deliberately avoided interpersonal comparison.
2. **Welfarist social welfare** — a *cardinal* quantity, `W(u₁,…,uₙ)`, aggregating voter utilities. Utilitarian (sum), egalitarian (max-min), or Nash (product).

Sense 2 is the hidden spine of three pages that otherwise look unrelated: [distortion](distortion.md) (a candidate's social welfare = the sum of voter utilities; the optimum minimizes total cost), [VSE](what_makes_a_good_winner.md) (the 100% mark *is* the utilitarian optimum), and the [ABC rules spectrum](../Approval_Voting/Multiwinner_Approval/abc_rules_spectrum.md) (AV / PAV / Chamberlin–Courant are one family differing only in the aggregator — see **welfarist rule** in the [glossary](../GLOSSARY.md)). Same object, three aggregators.

The cleanest way to hold the two apart: **Arrow's SWF asks "what order?"; welfarist social welfare asks "how much?"** — and [cardinal ballots are exactly what lets you ask the second question](../scores_and_ranks/scores_vs_ranks.md), which is why STAR sits [outside Arrow's frame](arrow_theorem_and_star.md) but squarely inside the distortion literature.

## Reading a criterion table without being fooled

Grids of YES/NO across methods circulate widely. Three checks:

1. **Are the rows SWFs or SCFs?** A table mixing "elects a Condorcet winner" (SCF) with "produces a transitive ranking" (SWF) is comparing different objects.
2. **Which columns are actually Arrow's?** Unrestricted domain, transitive-and-complete output, weak Pareto, IIA, non-dictatorship. **Monotonicity and Condorcet-efficiency are not Arrow conditions** — including them implies the impossibility involves them, which it doesn't.
3. **Does dictatorship pass everything?** If so the table is *correct* and you've found Arrow's punchline: the axioms are mild enough that the worst rule clears them. That's the lesson, not a bug in the table.

Per [reading these fairly](../../method_comparisons/paradoxes_and_whoops/reading_these_fairly.md): a criterion failure is a trade-off to weigh, never a disqualification.

## Sources

- Kenneth J. Arrow, *Social Choice and Individual Values* (1951) — the theorem ([book note](../books/social_choice_theory.md)). **Lean:** neutral, foundational.
- Peter C. Fishburn, "Condorcet Social Choice Functions," *SIAM J. Appl. Math.* 33(3), 1977 — the precise SCF vocabulary ([reading list](condorcet/condorcet_reading_list.md)).
- Amartya Sen, *Collective Choice and Social Welfare* (1970; exp. ed. 2017) — the welfarist sense, and the bridge between the two ([book note](../books/social_choice_theory.md)).
- The decisive-coalition proof (Contagion / Splitting Lemmas) is the standard modern presentation in the computational-social-choice textbooks; see [the math behind Condorcet](../RCV_Ranked_Robin/the_math_behind_condorcet.md) for how it sits alongside Gibbard–Satterthwaite.
