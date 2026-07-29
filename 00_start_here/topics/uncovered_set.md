# The uncovered set — "you're beaten by someone who beats everyone you beat"

*The one idea from the [tournament-solutions](tournament_solutions.md) literature that survives contact with a normal audience. Forget cycles and axioms for a moment and ask a much smaller question: **is this candidate redundant?** If somebody beats them head-to-head, and also beats everyone they beat, then yes — strictly, on the pairwise evidence alone. That candidate is **covered**. The **uncovered set** is everybody left. It is the weakest structural filter in the field, it has three completely different definitions that turn out to be the same thing, and it is exactly the line between electing a Pareto-optimal candidate and not.*

→ Related: [tournament solutions](tournament_solutions.md) — the family this belongs to · [the Smith set](smith_set.md) — the *other* generalized Condorcet winner, and a **coarser** one · [what a method reads](what_a_method_reads.md) · [pairwise counting](pairwise_counting.md) · **Level: Voting 301**

**Runnable:** [STAR elects a covered candidate](../../method_comparisons/tournament_solutions/cases/cases_pages/star_elects_a_covered_candidate_c4_b5.md) — five ballots, four cities, and the filter that most candidates pass.

---

## The definition, in one sentence

> **A covers B** when A beats B head-to-head **and** A also beats everyone B beats.
>
> **The uncovered set** is every candidate nobody covers.

That's it. If A covers B, then B contributes nothing A doesn't already contribute: any argument for B ("B beats C, B beats D") is an argument A satisfies too, *plus* A beats B. Electing B over A would be hard to defend to the room.

Two properties make it well-behaved, and they are worth stating because most cycle-related concepts lack them:

- **The covering relation is transitive** — even though "beats" isn't. Covering is defined by set inclusion of who-you-beat, and inclusion is transitive. So the covering relation is a genuine partial order sitting *inside* the messy tournament, and the uncovered set is simply its maximal elements.
- **It's never empty.** A cycle can destroy the Condorcet winner; it cannot destroy the uncovered set.

And when a [Condorcet winner](condorcet/) exists, the uncovered set is just that one candidate — they beat everyone, so they cover everyone. Like every tournament solution, this only becomes interesting in a cycle.

## Three definitions, one set

This is the part that makes the uncovered set feel less like an arbitrary construction. It was proposed independently by Fishburn (1977) and Miller (1980), out of a game-theoretic notion of Gillies (1959), and it has three characterizations that look unrelated:

1. **Covering.** Nobody beats you who also beats everyone you beat.
2. **Reachability in two steps.** You can get from yourself to *every* rival along at most two arrows — "I beat you, or I beat somebody who beat you." Every excuse is one hop deep. (Shepsle & Weingast, 1984.) In graph theory these vertices are the **kings** of the tournament, and they form its **center**.
3. **Winning a sub-election.** You are a Condorcet winner of some inclusion-maximal subtournament that has one (Brandt, 2011).

The equivalence of (1) and (2) is a two-line argument: if nobody covers you, then for each candidate `b` who beats you there must be somebody you beat who beats `b` — otherwise `b` would cover you — and that "somebody" is your second hop. It also hands you the algorithm: reachability in ≤ 2 steps is a statement about `M(T)² + M(T) + I` having no zero entries, so the uncovered set falls out of one matrix multiplication, `O(m^2.38)`.

Characterization (2) is the one to say out loud. "Every candidate who beat me was beaten by someone I beat" is a sentence a voter can check by hand on a printed pairwise table.

## Why it matters: the Pareto line

Here is the result that turns the uncovered set from a curiosity into a criterion.

> **The uncovered set is the *coarsest* Pareto-optimal tournament solution** (Brandt et al., 2015). Equivalently: a tournament solution is Pareto-optimal **if and only if** it is a refinement of the uncovered set.

So "stay inside the uncovered set" is not one taste among many — it is precisely the condition for never electing a Pareto-dominated candidate while reading only the win-loss graph. Everything sharper than the uncovered set (Banks, bipartisan, Copeland, Slater, Markov) inherits Pareto-optimality for free; anything coarser (the Smith set, the top cycle, Condorcet non-losers) does not.

**One precision that matters, and gets fumbled constantly:** *covered* does **not** mean *Pareto-dominated*. Pareto domination means every single voter ranks the other candidate higher — much rarer, and much stronger. A covered candidate can be many voters' genuine favourite. The theorem says the uncovered set is the coarsest solution that *excludes* Pareto-dominated candidates; it does not say the candidates it excludes are Pareto-dominated. Our runnable case is exactly this: the covered city is nobody's Pareto-dominee, and one ballot scores it top.

Where it sits relative to the [Smith set](smith_set.md), which the repo already covers:

| Filter | Asks | Strength |
|---|---|---|
| Condorcet non-losers | is anyone *worse* than you in every matchup? | weakest |
| Top cycle / **Smith set** | are you in the club that beats all outsiders? | weak |
| **Uncovered set** | is anyone strictly redundant-making you? | weak — **but** the Pareto line |
| Copeland, Banks, bipartisan, Slater… | sharper, various | strong |

Uncovered ⊆ Smith, always. The Smith set answers *who is in contention*; the uncovered set answers *who isn't redundant*.

## What our methods do with it

**Ranked Robin never elects a covered candidate.** The Copeland set is always a subset of the uncovered set, and the proof is one line: if B covers A then B beats everything A beats *plus* A itself, so B's win count is strictly greater than A's, so A cannot have the maximum win count. Verified as a sanity check over 300,000 random tournaments — zero violations.

That is a genuine, citable virtue of [Ranked Robin](../../05_Ranked_Robin/concepts/ranked_robin.md), and via the Pareto theorem above it means **Ranked Robin is Pareto-optimal in the tournament sense**. It's a better thing to say about the method than any axiom scorecard, because a voter can follow it.

**RCV-IRV can, and often does.** Over 120,000 random tie-free four-candidate ranked profiles, IRV elected a covered candidate 9.1% of the time — 61.6% of the time when there was no Condorcet winner. Two honest caveats on that number, both cutting the same way: uniform-random profiles ("impartial culture") produce far more cycles than real electorates do — 14.8% here, against the [2-in-182 rate observed in real IRV elections](../RCV_IRV/) — so treat 9.1% as *what the failure looks like when cycles are common*, not as a forecast for any real jurisdiction. When there is a Condorcet winner, no method that elects them can elect a covered candidate.

**STAR can too — and here it is.** Five ballots, four cities, every ballot using four distinct scores so nothing is a tie-breaking artifact ([full case](../../method_comparisons/tournament_solutions/cases/cases_pages/star_elects_a_covered_candidate_c4_b5.md)):

```text
--- Runoff (Preference) Matrix ---
                |  * Austin   |   Boston   |   Chicago  | * Denver   |
----------------------------------------------------------------------
     * Austin > |     ---     | 4 - 0 - 1  | 2 - 0 - 3  | 2 - 0 - 3  |
       Boston > |  1 - 0 - 4  |    ---     | 3 - 0 - 2  | 3 - 0 - 2  |
      Chicago > |  3 - 0 - 2  | 2 - 0 - 3  |    ---     | 3 - 0 - 2  |
     * Denver > |  3 - 0 - 2  | 2 - 0 - 3  | 2 - 0 - 3  |    ---     |

Scoring Round:  Austin 14 · Denver 11 · Chicago 10 · Boston 9
Automatic Runoff:  Denver 3 — Austin 2  →  Denver wins.
```

Read the grid for Denver. **Chicago beats Denver** — and Austin, the only city Denver beats, **is also beaten by Chicago**. Chicago does everything Denver does and more, so Denver is covered, and the uncovered set is `{Austin, Boston, Chicago}`. Three of four cities clear the bar. STAR elects the fourth.

Both halves of that, because the repo doesn't get to keep only the flattering one:

- **Against STAR.** No rule reading only the win-loss graph would elect Denver, and the objection travels in one sentence to a lay audience. Plurality, RCV-IRV and Ranked Robin all elect Chicago here; STAR is the outlier, and the engine says so in its own divergence block.
- **For STAR.** Covering is a purely *ordinal* verdict, and STAR is deliberately reading what the tournament throws away. Denver is **not** Pareto-dominated — ballot 3 scores Denver 5 and Chicago 0 — and Denver outscores both Boston and Chicago. The ordinal evidence says "redundant"; the cardinal evidence says "more support." That disagreement *is* the score-versus-pairwise argument, in five ballots.

Ranked Robin, as guaranteed, stays inside: Copeland ties Boston and Chicago at 2–1, both uncovered. At four candidates that tie is unavoidable — a unique Copeland winner and a Condorcet winner are the same thing there (exhaustively true over all 64 four-candidate tournaments), so a cycle forces a tie. LH's margin rung then elects **Chicago** (+1 vs Boston's −1); BetterVoting's head-to-head rung would elect **Boston** (3–2). Deterministic on both sides, and [they disagree](../../05_Ranked_Robin/concepts/rr_tiebreak_lh_vs_bv.md) — and the disagreement isn't arbitrary on either side: the sharpest solution in the family, the **Slater set, returns `{Boston}`**, siding with BetterVoting's rung. Two engines, two published tiebreaks, and each has a tournament solution behind it.

## The caveat before you quote this at a real election

Covering is defined on a **tournament**, which assumes *no pairwise ties*. Real ballots tie, and then the object is a *weak* tournament — and the covering relation stops having one obvious meaning. There are at least four published extensions (Gillies, Fishburn, Bordes, McKelvey), identical on tie-free tournaments and genuinely different once a tie appears. They disagreed on 125,435 of the weak tournaments we sampled. A four-candidate example, with A and B tied and everything else decided:

```text
edges:  A>C   D>A   B>C   B>D   D>C        tie:  A=B

  Gillies    {A, B}
  Fishburn   {B}
  Bordes     {B, D}
  McKelvey   {A, B, D}
```

Four defensible answers to "who is redundant here," from one election. So: **"the uncovered set" is unambiguous only when every head-to-head is decided.** Say which variant you mean otherwise. (Our own pairwise report is a For / **Equal Support** / Against table — strictly richer than a tournament, which is what makes this resolvable in principle for our cases, but it does not pick a variant for you.) The exhibit above is tie-free by construction, and all four variants agree on it.

## Sources

- **Felix Brandt, Markus Brill & Paul Harrenstein, "Tournament Solutions,"** §3.3.2 of ch. 3 in the [Handbook of Computational Social Choice](https://procaccia.info/wp-content/uploads/2020/03/comsoc.pdf) (CUP 2016) — the definition, the two-step equivalence, the matrix algorithm, Theorem 3.6, and the Pareto result. **Lean:** neutral / academic.
- Peter C. Fishburn, "Condorcet Social Choice Functions," *SIAM J. Appl. Math.* 33(3), 1977, and Nicholas R. Miller, "A New Solution Set for Tournaments and Majority Voting," *AJPS* 24(1), 1980 — the two independent origins. **Lean:** neutral.
- Kenneth A. Shepsle & Barry R. Weingast, "Uncovered Sets and Sophisticated Voting Outcomes with Implications for Agenda Institutions," *AJPS* 28(1), 1984 — the two-step / kings characterization. **Lean:** neutral.
- The choice sets, rates and counterexamples here were computed with Eric Pacuit & Wesley Holliday's `pref_voting` (its four covering variants) and cross-checked against the LH engine; the exhibit is reproducible via [`tournament_solutions_report.py`](../../STARVote_LH_tabulation_engine/tools_adam/pref_voting_tabulation_engine/tournament_solutions_report.py). Nothing here is asserted from memory.

## Related

- [Tournament solutions](tournament_solutions.md) — the whole C1 family, and where Ranked Robin sits in it
- [The Smith set](smith_set.md) — the coarser sibling · [the math behind Condorcet](../../05_Ranked_Robin/concepts/the_math_behind_condorcet.md)
- [Tournament solutions, counted](../../method_comparisons/tournament_solutions/) — the runnable exhibits
- [Ranked Robin](../../05_Ranked_Robin/concepts/ranked_robin.md) · [its honest limits](../../05_Ranked_Robin/concepts/RCV_RR_honest_limits.md) · [STAR's properties and limits](../STAR_Voting/properties_and_limits/)
