# Criteria at a glance — Approval, STAR, Ranked Robin, RCV-IRV

*A single pass/fail map of the four single-winner methods this library covers, across the criteria voting theorists argue about — with, wherever we have one, a **runnable election** you can open to watch the failure happen. A linked ✗ has a worked demo behind it.*

**Level: 201 → 301.** Read the caveat first — it's the whole point.

## Read this before the table: pass/fail is a *starting point*, not a verdict

A checkmark grid is the most-abused object in voting reform. It quietly implies that (a) every criterion is equally important, and (b) "fails" is binary — when the questions that actually matter are **how often** a method fails in realistic elections and **how badly**, and **which criteria you value**. Even STAR's own advocates argue against the format (["Farewell to Pass/Fail"](https://www.starvoting.org/pass_fail)), and our [ranked-ballot zoo](ranked_ballot_methods_zoo.md) says the same: *this is the catalog, not the verdict.* What "good" means is the judgment call in [What makes a voting method good?](what_makes_a_voting_method_good.md) — read that alongside this.

So use this table to *navigate to the worked cases*, not to crown a winner.

## The table

Each **criterion name** links to an explanation of that criterion; where a cell's **✗ is itself a link** (blue), it opens a *runnable* election demonstrating that failure. (More below in [Watch the failures happen](#watch-the-failures-happen-runnable).)

| Criterion | Approval | STAR | Ranked Robin | RCV-IRV |
|---|:---:|:---:|:---:|:---:|
| [**Monotonicity**](monotonicity) (raising a candidate can't hurt them) | ✓ | ✓ | ✓ | [✗](../../method_comparisons/monotonicity/monotonicity_pages/monotonicity_irv_after.md) |
| [**Condorcet winner**](condorcet) (elects a beats-all candidate) | ✗ | [✗](../STAR_Voting/STAR_three_winner_notions.md) | ✓ | [✗](../RCV_IRV/RCV_IRV_center_squeeze.md) |
| [**Condorcet loser**](../voting_paradoxes/condorcet_loser_paradox.md) (never elects a loses-to-all candidate) | ✗ | ✓ | ✓ | ✓ |
| [**Majority favorite**](majority_criterion) (a majority's 1st choice wins) | ✗ † | [✗](../../01_STAR/majority_criterion) | ✓ | ✓ |
| [**Mutual majority**](../GLOSSARY.md) | ✗ | ✗ | ✓ | ✓ |
| [**Participation**](participation) (showing up can't backfire) | ✓ | [✗](../../method_comparisons/participation_no_show) | ✗ | [✗](../../method_comparisons/participation_no_show) |
| [**Consistency**](../voting_paradoxes/multiple_districts.md) (two districts agreeing agree combined) | ✓ | ✗ | ✗ | ✗ |
| [**Independence of clones**](../../05_Ranked_Robin/clone_independence) | ✓ | ✗ | [✗](../../05_Ranked_Robin/clone_independence) | ✓ |
| [**Later-no-harm**](../STAR_Voting/STAR_second_round_FAQ.md) (a backup can't sink your favorite) | ✗ | [✗](../STAR_Voting/STAR_second_round_FAQ.md) | ✗ | ✓ |
| [**Favorite betrayal**](../STAR_Voting/favorite_betrayal_voting_301.md) (never rewards burying your favorite) | ✓ | [✗](../STAR_Voting/favorite_betrayal_voting_301.md) | ✗ | ✗ |
| [**Summable**](summability) (precinct subtotals; easy audit) | ✓ | ✓ | ✓ | [✗](../STAR_Voting/STAR_summability.md) |

*(Ranked Robin = the repo's Copeland-based Condorcet method. "RCV-IRV" = ranked ballots counted by instant runoff.)*

**† Majority favorite (Approval) is definition-dependent.** Approval fails it when voters approve candidates *beyond* their favorite (a majority can prefer A yet elect B they also approved); it passes if that majority bullet-votes A alone. Sources genuinely differ on how to score this cell — hence the flag rather than a bare mark.

## What the pattern actually says

- **No method passes everything** — that's [Arrow / Gibbard–Satterthwaite](gibbard_satterthwaite_theorem.md), not a shortcoming of any one row. Every column has ✗s. (Strategy-proofness is the row *no* method passes.)
- **Later-no-harm and favorite betrayal pull against each other.** RCV-IRV passes later-no-harm but fails favorite betrayal; Approval does the reverse; **STAR fails both — on purpose** (its advocates argue mitigating both beats passing one and hard-failing the other; that's the pass_fail essay above). Ranked Robin fails both too.
- **Ranked Robin is the Condorcet specialist** — it's the only column that elects the Condorcet winner and satisfies majority / mutual-majority — but it pays for it by failing participation, consistency, and clones (the price every Condorcet method pays: Moulin's theorem).
- **RCV-IRV's strengths are later-no-harm, clone independence, and the majority guarantees**; its costs are monotonicity, the Condorcet winner (center squeeze), and summability.
- **Approval and STAR** trade expressiveness and simplicity for the majoritarian criteria; **STAR's runoff buys back Condorcet-*loser* protection** that plain Score voting lacks (a Condorcet loser can top the scores but always loses the runoff).

None of that ranks the methods. It tells you *which trade you're making*.

## Watch the failures happen (runnable)

The value of this repo isn't the ✗ — it's the countable election behind it:

- **RCV-IRV fails monotonicity** → the [before/after pair](../../method_comparisons/monotonicity) (raise the winner, they lose).
- **STAR fails monotonicity's *stronger* variant** (mono-raise-delete, though it passes the standard one) → the [mono-raise-delete pair](../../method_comparisons/monotonicity/mono_raise_delete_before.yaml) · concept: [STAR & monotonicity](../STAR_Voting/STAR_monotonicity.md).
- **STAR fails the majority criterion** → [the favorite loses to two rivals](../../01_STAR/majority_criterion) (bv95a/bv95b).
- **STAR & IRV fail the Condorcet winner** → [three notions of "winner"](../STAR_Voting/STAR_three_winner_notions.md) · [center squeeze](../RCV_IRV/RCV_IRV_center_squeeze.md).
- **STAR, IRV & Ranked Robin fail participation** → the live [no-show pair](../../method_comparisons/participation_no_show) (showing up flips the result).
- **Ranked Robin fails clone independence** → [clone independence](../../05_Ranked_Robin/clone_independence).

## Sourcing & how these were checked

Each cell was cross-checked against Wikipedia's [Comparison of electoral systems](https://en.wikipedia.org/wiki/Comparison_of_electoral_systems) table **and** established social-choice results, with our own engine's worked cases as the tie-breaker where a source looked wrong (the standard tables also disagree on a few contested cells, like Approval's majority row above). STAR is scored on its **own** behavior, not copied from Score voting — the two differ on Condorcet-loser, later-no-harm, and clones because STAR's automatic runoff changes them.

## Related

- [What makes a good winner?](what_makes_a_good_winner.md) · [What makes a voting method good?](what_makes_a_voting_method_good.md) — the "which criteria matter" question
- [Do the experts really think RCV-IRV is "bad"?](expert_consensus_and_irv.md) — why a table like this isn't a verdict
- Per-method honest limits: [STAR](../STAR_Voting/STAR_honest_limits.md) · [Approval](../Approval_Voting/approval_honest_limits.md) · [Ranked Robin](../RCV_Ranked_Robin/RCV_RR_honest_limits.md)
- [The ranked-ballot method zoo](ranked_ballot_methods_zoo.md) — the wider family and its own criterion table
