# Criteria at a glance — Approval, STAR, Ranked Robin, RCV-IRV

*A single pass/fail map of the four single-winner methods this library covers, across the criteria voting theorists argue about — with, wherever we have one, a **runnable election** you can open to watch the failure happen. A linked ✗ has a worked demo behind it.*

**Level: 201 → 301 · for debaters** Read the caveat first — it's the whole point.

## Read this before the table: pass/fail is a *starting point*, not a verdict

A checkmark grid is the most-abused object in voting reform. It quietly implies that (a) every criterion is equally important, and (b) "fails" is binary — when the questions that actually matter are **how often** a method fails in realistic elections and **how badly**, and **which criteria you value**. Even STAR's own advocates argue against the format (["Farewell to Pass/Fail"](https://www.starvoting.org/pass_fail)), and our [ranked-ballot zoo](ranked_ballot_methods_zoo.md) says the same: *this is the catalog, not the verdict.* What "good" means is the judgment call in [What makes a voting method good?](what_makes_a_voting_method_good.md) — read that alongside this.

So use this table to *navigate to the worked cases*, not to crown a winner.

## The table

Each **criterion name** links to an explanation of that criterion; where a cell's **✗ is itself a link** (blue), it opens a *runnable* election demonstrating that failure. (More below in [Watch the failures happen](#watch-the-failures-happen-runnable).)

| Criterion | Approval | STAR | Ranked Robin | RCV-IRV |
|---|:---:|:---:|:---:|:---:|
| [**Pareto**](social_welfare_function.md) (never elects a unanimously-beaten candidate) § | [✗](../../method_comparisons/felsenthal_paradoxes/cases/cases_pages/felsenthal_ex6_pareto_approval.md) | ✓ | ✓ | ✓ |
| [**Monotonicity**](monotonicity) (raising a candidate can't hurt them) | ✓ | ✓ | ✓ | [✗](../../method_comparisons/monotonicity/cases/cases_pages/monotonicity_irv_after.md) |
| [**Condorcet winner**](condorcet) (elects a beats-all candidate) | ✗ | [✗](../../01_STAR/01_Learn/properties_and_limits/STAR_three_winner_notions.md) | ✓ | [✗](../../06_Other/RCV_IRV/concepts/RCV_IRV_center_squeeze.md) |
| [**Condorcet loser**](../voting_paradoxes/condorcet_loser_paradox.md) (never elects a loses-to-all candidate) | ✗ | ✓ | ✓ | ✓ |
| [**Weak Condorcet loser**](../../method_comparisons/weak_condorcet_loser/README.md) (never elects a beats-*nobody* candidate) | [✗](../../method_comparisons/weak_condorcet_loser/cases/cases_pages/wcl_c3_b5_approval.md) | [✗](../../method_comparisons/weak_condorcet_loser/cases/cases_pages/wcl_c3_b5_star.md) | ✓ ‡ | ✓ |
| [**Majority favorite**](majority_criterion) (a majority's 1st choice wins) | ✗ † | [✗](../../01_STAR/03_Criteria/majority_criterion) | ✓ | ✓ |
| [**Mutual majority**](../GLOSSARY.md) | ✗ | ✗ | ✓ | ✓ |
| [**Participation**](participation) (showing up can't backfire) | ✓ | [✗](../../method_comparisons/participation_no_show) | ✗ | [✗](../../method_comparisons/participation_no_show) |
| [**Consistency**](../voting_paradoxes/multiple_districts.md) (two districts agreeing agree combined) | ✓ | ✗ | ✗ | ✗ |
| [**Independence of clones**](../../05_Ranked_Robin/03_Criteria/clone_independence) | ✓ | ✗ | [✗](../../05_Ranked_Robin/03_Criteria/clone_independence) | ✓ |
| [**Later-no-harm**](../../01_STAR/01_Learn/the_count/STAR_second_round_FAQ.md) (a backup can't sink your favorite) | ✗ | [✗](../../01_STAR/01_Learn/the_count/STAR_second_round_FAQ.md) | ✗ | ✓ |
| [**Favorite betrayal**](../../01_STAR/01_Learn/properties_and_limits/favorite_betrayal_voting_301.md) (never rewards burying your favorite) | ✓ | [✗](../../01_STAR/01_Learn/properties_and_limits/favorite_betrayal_voting_301.md) | ✗ | ✗ |
| [**Summable**](summability) (precinct subtotals; easy audit) | ✓ | ✓ | ✓ | [✗](../../01_STAR/01_Learn/properties_and_limits/STAR_summability.md) |

*(Ranked Robin = the repo's Copeland-based Condorcet method. "RCV-IRV" = ranked ballots counted by instant runoff.)*

**‡ Weak Condorcet loser (Ranked Robin) passes with one degenerate exception.** RR elects the candidate with the most *wins*, and a weak Condorcet loser has zero — so RR can only elect one when **every** candidate has zero wins (a total pairwise tie), where every candidate is simultaneously a weak Condorcet *winner* and *loser* and the distinction has collapsed anyway. Outside that case the pass is unconditional. Note this row is **strictly stronger** than the Condorcet-loser row above it: STAR passes that one absolutely (a strict loser always loses the runoff) and fails this one, because *a tie is not a loss* — the runoff doesn't resolve and the score tiebreaker decides. See [the worked election](../../method_comparisons/weak_condorcet_loser/README.md).

**§ Pareto is the floor, and it's the one row where Approval is the outlier.** If *every* voter prefers A to B, B must not win. Almost everything passes — it's mild enough that even a **dictatorship** passes it, which is exactly why [Arrow's conclusion](arrow_theorem_and_star.md) is devastating rather than reassuring. Approval fails, and the reason is about the *ballot*, not the count: an approval ballot cannot record a strict preference *within* the approved set, so "everyone prefers A to B" is a fact the ballots never carried ([worked: Felsenthal Ex.6](../../method_comparisons/felsenthal_paradoxes/felsenthal_ex6_pareto.md)). STAR passes because the scoring round and runoff work *together* — a unanimously-preferred A always outscores B, so B reaches the runoff only against A and loses it unanimously. Ranked Robin passes because b's pairwise wins are always a subset of a's; RCV-IRV passes because a unanimously-beaten candidate holds no first preferences while their dominator survives. **Careful, though: Pareto forbids, it does not require** — [plurality](plurality.md) passes this row and still elects badly. A ✓ here is a floor, not a recommendation. Full treatment: [social welfare function](social_welfare_function.md).

**† Majority favorite (Approval) is definition-dependent.** Approval fails it when voters approve candidates *beyond* their favorite (a majority can prefer A yet elect B they also approved); it passes if that majority bullet-votes A alone. Sources genuinely differ on how to score this cell — hence the flag rather than a bare mark.

## What the pattern actually says

- **No method passes everything** — that's [Arrow / Gibbard–Satterthwaite](gibbard_satterthwaite_theorem.md), not a shortcoming of any one row. Every column has ✗s. (Strategy-proofness is the row *no* method passes.)
- **Later-no-harm and favorite betrayal pull against each other.** RCV-IRV passes later-no-harm but fails favorite betrayal; Approval does the reverse; **STAR fails both — on purpose** (its advocates argue mitigating both beats passing one and hard-failing the other; that's the pass_fail essay above). Ranked Robin fails both too.
- **Ranked Robin is the Condorcet specialist** — it's the only column that elects the Condorcet winner and satisfies majority / mutual-majority — but it pays for it by failing participation, consistency, and clones (the price every Condorcet method pays: Moulin's theorem).
- **RCV-IRV's strengths are later-no-harm, clone independence, and the majority guarantees**; its costs are monotonicity, the Condorcet winner (center squeeze), and summability.
- **Approval and STAR** trade expressiveness and simplicity for the majoritarian criteria; **STAR's runoff buys back Condorcet-*loser* protection** that plain Score voting lacks (a Condorcet loser can top the scores but always loses the runoff).

- **The Pareto row is the one place STAR beats Approval on a *fairness axiom* rather than a majoritarian one.** Everywhere else Approval's ✗s are about majorities (majority favorite, mutual majority, Condorcet); here it fails the most basic requirement in the table, and STAR's runoff is what saves it. Worth knowing when the comparison is Approval-vs-STAR specifically.

None of that ranks the methods. It tells you *which trade you're making*.

## Which of these are actually Arrow's conditions? (none of the differentiating ones)

A trap worth naming, because circulated criterion grids routinely blur it. **Arrow's theorem** uses exactly five: unrestricted domain, a transitive-and-complete output, **weak Pareto**, **IIA**, and non-dictatorship. Of the rows above, **only Pareto is one of them.** Monotonicity, Condorcet-efficiency, later-no-harm, participation and the rest are ordinary fairness criteria — real, but not what the impossibility theorem is about. Putting them in the same grid implies Arrow rules them out too. It doesn't.

Two more axioms are missing from the table on purpose, because **all four methods pass them** and a row of four ✓s tells you nothing:

- **Anonymity** — permuting *which voter* cast which ballot never changes the result (one person, one vote).
- **Neutrality** — swapping two candidates' *names* swaps the result; no default, no incumbent bonus.

They're invisible here precisely because they're uncontroversial in a single-winner election — but they are not trivial. They're the two conditions [May's Theorem](mays_theorem.md) holds fixed to prove that **at two candidates majority rule is the unique reasonable rule**, and a [supermajority threshold](mays_theorem.md) is a deliberate, common violation of neutrality. Everything in this table exists only because May's third condition — *only two alternatives* — stops holding.

One last check when reading any such grid, ours included: **are the rows the same kind of object?** "Elects the Condorcet winner" is a property of a winner-picking rule; "produces a transitive ranking" is a property of a ranking-producing rule. Mixing them compares different things — see [social welfare function](social_welfare_function.md).

## Watch the failures happen (runnable)

The value of this repo isn't the ✗ — it's the countable election behind it:

- **RCV-IRV fails monotonicity** → the [before/after pair](../../method_comparisons/monotonicity) (raise the winner, they lose).
- **STAR fails monotonicity's *stronger* variant** (mono-raise-delete, though it passes the standard one) → the [mono-raise-delete pair](../../method_comparisons/monotonicity/cases/mono_raise_delete_before.yaml) · concept: [STAR & monotonicity](../../01_STAR/01_Learn/properties_and_limits/STAR_monotonicity.md).
- **STAR fails the majority criterion** → [the favorite loses to two rivals](../../01_STAR/03_Criteria/majority_criterion) (bv95a/bv95b).
- **STAR & IRV fail the Condorcet winner** → [three notions of "winner"](../../01_STAR/01_Learn/properties_and_limits/STAR_three_winner_notions.md) · [center squeeze](../../06_Other/RCV_IRV/concepts/RCV_IRV_center_squeeze.md).
- **STAR, IRV & Ranked Robin fail participation** → the live [no-show pair](../../method_comparisons/participation_no_show) (showing up flips the result).
- **Ranked Robin fails clone independence** → [clone independence](../../05_Ranked_Robin/03_Criteria/clone_independence).

## Sourcing & how these were checked

Each cell was cross-checked against Wikipedia's [Comparison of electoral systems](https://en.wikipedia.org/wiki/Comparison_of_electoral_systems) table **and** established social-choice results, with our own engine's worked cases as the tie-breaker where a source looked wrong (the standard tables also disagree on a few contested cells, like Approval's majority row above). STAR is scored on its **own** behavior, not copied from Score voting — the two differ on Condorcet-loser, later-no-harm, and clones because STAR's automatic runoff changes them.

## Related

- [What makes a good winner?](what_makes_a_good_winner.md) · [What makes a voting method good?](what_makes_a_voting_method_good.md) — the "which criteria matter" question
- [Do the experts really think RCV-IRV is "bad"?](expert_consensus_and_irv.md) — why a table like this isn't a verdict
- Per-method honest limits: [STAR](../../01_STAR/01_Learn/properties_and_limits/STAR_honest_limits.md) · [Approval](../../04_Approval/01_Learn/approval_honest_limits.md) · [Ranked Robin](../../05_Ranked_Robin/01_Learn/RCV_RR_honest_limits.md)
- [The ranked-ballot method zoo](ranked_ballot_methods_zoo.md) — the wider family and its own criterion table
