# Condorcet-Consistent Choice Among Three Candidates — the maximin result (Brandt, Dong & Peters, 2024)

*A rigorous social-choice result, read for what it does and doesn't prove. **Felix Brandt, Chris Dong & Dominik Peters**, ["Condorcet-Consistent Choice Among Three Candidates"](https://arxiv.org/abs/2411.19857) (arXiv:2411.19857, Nov 2024; journal version 2025) asks: if you restrict to **exactly three candidates**, which [Condorcet extension](README.md) best resists the two nastiest variable-electorate paradoxes — the **[no-show paradox](../../voting_paradoxes/no_show.md)** and the **reinforcement paradox**? Their answer: **[maximin](../../voting_paradoxes/minimax.md)** and two of its refinements (**Nanson's rule** and **leximin**) occupy a uniquely defensible position. This is the theoretical backbone under the [Better Choices](better_choices_pairwise_ballot.md) proposal's minimax count — and, unlike advocacy literature, a neutral academic result (the authors are theorists, not campaigners). It cuts for a specific Condorcet rule, and this repo — which leans STAR, a method the theorem doesn't even cover — reports it straight.*

→ Runnable: the paper's Fig. 1 profile, with its minimality proved — [the minimal tilted cycle (5 voters)](../../../method_comparisons/minimal_tilted_cycle/README.md) · its Theorem 2 profile — [the reinforcement paradox](../../../method_comparisons/reinforcement_paradox/README.md).
→ Related: [Minimax / Simpson-Kramer (Felsenthal paradoxes)](../../voting_paradoxes/minimax.md) · [the No-Show paradox](../../voting_paradoxes/no_show.md) · [Participation topic hub](../participation/) · [Better Choices — the pairwise-ballot method](better_choices_pairwise_ballot.md) · [cycle resolution](../../../05_Ranked_Robin/concepts/cycle_resolution.md) · [Condorcet reading list](condorcet_reading_list.md).

---

## Why "exactly three candidates" is the whole point

Two candidates are trivial: majority rule satisfies essentially every fairness property at once. Three or more candidates is where [Arrow](../arrow_theorem_and_star.md) and Gibbard–Satterthwaite bite and every rule starts trading one virtue for another. The paper's move is to ask whether the **smallest hard case — three candidates** — is tractable enough to pick a *best* Condorcet rule, even if no such rule exists in general. It is. Three candidates is special because it is exactly where **[Moulin's impossibility theorem](../../voting_paradoxes/no_show.md) stops applying**: Moulin (1988) proved every Condorcet extension suffers the no-show paradox once there are **≥ 4 candidates** (and enough voters). At three, there's room to escape — and this paper maps exactly who does.

## The two paradoxes, and the findings

**Reinforcement paradox** (a.k.a. consistency / [multiple-districts](../../voting_paradoxes/multiple_districts.md), Young–Levenglick 1978): two separate groups of voters each elect A, but the *combined* electorate does not. A rule that does this contradicts what every sub-group agreed on. **Runnable** — the paper's own Theorem 2 profile, cast as two towns whose merger flips the winner from Ada to Cara, counted across every method: [Reinforcement paradox — when both halves pick Ada but the whole picks Cara](../../../method_comparisons/reinforcement_paradox/README.md).

> **Finding:** with three candidates, the reinforcement paradox **must occur for *every* Condorcet extension once there are ≥ 8 voters** — no escape, for anyone. But **certain refinements of maximin are immune when there are ≤ 7 voters.**

**No-show paradox** ([participation](../participation/) failure, Moulin 1988): a voter gets a *better* result by staying home than by voting sincerely — abstention beats participation.

> **Finding:** among **homogeneous** Condorcet extensions (rules unchanged when you scale the whole electorate up proportionally), **the *only* ones immune to the no-show paradox are refinements of maximin.**

Add the trivial fact that any Condorcet extension elects the Condorcet winner when one exists, and the scorecard for three candidates is:

| Property | Maximin refinements (Nanson / leximin) | Any other Condorcet extension |
|---|:---:|:---:|
| Elects the Condorcet winner when one exists | ✅ (by definition) | ✅ (by definition) |
| Immune to the **no-show** paradox (homogeneous rules) | ✅ **uniquely** | ❌ |
| Immune to the **reinforcement** paradox, ≤ 7 voters | ✅ | ❌ (in general) |
| Immune to the **reinforcement** paradox, ≥ 8 voters | ❌ | ❌ — *nobody is* |

A companion fact from the same paper's Fig. 2 makes the family tractable: at three candidates, **maximin = Ranked Pairs = Schulze = Kemeny = Dodgson = Young** are one and the same rule — the [three-candidate collapse](three_candidate_collapse.md).

The paper then gives **axiomatic characterizations** of maximin, Nanson's rule, and leximin — short lists of independently reasonable axioms that *uniquely* pin down each rule. That's the honest form of "use this rule": not "trust us," but "here are principles you'd likely accept, and this is the only rule satisfying all of them."

## What maximin and its refinements are

- **Maximin** (Simpson–Kramer; Condorcet's own 1785 cycle rule): elect the candidate whose **worst pairwise loss is smallest** — least-strongly-beaten. Condorcet's three-candidate phrasing: in a cycle, "the adopted view results from the two [pairwise majorities] that are most probable [largest]." Bare maximin can **tie** (two candidates with equally bad worst losses), which is why refinements exist.
- **Leximin** — break maximin ties lexicographically: compare worst losses; if tied, second-worst; then third-worst. "Least bad, then next-least-bad."
- **Nanson's rule** — iteratively eliminate every candidate with a below-average [Borda](../ranked_ballot_methods_zoo.md) score. It's a Condorcet extension, and at three candidates it lands as a maximin refinement.

## How this reconciles with the repo's *other* minimax page

This looks, at first, to contradict [the repo's Minimax page](../../voting_paradoxes/minimax.md), which (following Felsenthal) lists Minimax as vulnerable to the no-show, twin, and reinforcement paradoxes. **Both are right — the difference is candidate count.** Every one of Felsenthal's damning Minimax examples uses **four candidates** (Example 30's no-show, for instance, has a four-candidate cyclical order). Brandt–Dong–Peters restrict to **three**, where Moulin's impossibility hasn't kicked in — and there, the *refinements* of maximin (bare maximin's ties resolved) are uniquely well-behaved. So the two results don't collide: **Minimax looks paradox-prone in the general (4+) case and uniquely well-behaved in the exactly-three case.** That's a genuinely clarifying pairing, not a contradiction — and a good caution against citing a criterion result without its candidate-count fine print.

## What this means for Better Choices — and the honest caveats

The [Better Choices](better_choices_pairwise_ballot.md) proposal counts its three-candidate final by minimax ("least bad loss"). This paper is the **serious backing** for that choice: at three candidates, minimax-family rules really are the best-defended Condorcet option against the two worst variable-electorate paradoxes. Three caveats keep it in proportion — all of which *strengthen* the case for reading the paper carefully rather than as a slogan:

1. **It's the *refinements* that are characterized, not bare minimax.** Better Choices as described (plain "smallest-margin loss") can tie; the clean theorems attach to **leximin / Nanson**, which specify the tie-break. A faithful implementation should pin down that tie-break (leximin is the natural one), not leave it to a coin.
2. **It's a three-candidate result — full stop.** With four or more candidates Moulin's theorem returns and *every* Condorcet extension, minimax included, fails no-show. Better Choices dodges this only by being a **Top-3** system (its primary guarantees exactly three finalists) — which is precisely why the primary that feeds it matters so much.
3. **The reinforcement paradox is unavoidable for everyone at ≥ 8 voters.** This is not "maximin escapes all paradoxes." It escapes *no-show* (uniquely) and *reinforcement for small electorates*. In any real public election (≫ 8 voters) Better Choices, [Ranked Robin](../../../05_Ranked_Robin/concepts/ranked_robin.md), and every other Condorcet rule can still exhibit reinforcement. The result is a "best available," not a "flawless."

**And the repo's own lean, stated plainly:** this theorem is entirely about the **Condorcet family** — rules that *insist* on the head-to-head winner. **[STAR is not a Condorcet extension](README.md)** (it's a [score method](../scoring-methods-vs-ranked-voting.md); it elects the Condorcet winner *very often* but not by rule), so the theorem simply **does not bind it**. STAR makes the opposite trade: it gives up the Condorcet *guarantee* to buy preference-strength expression and a two-step count with no separate primary — and it, too, can [fail no-show](../../voting_paradoxes/no_show.md) (the repo concedes this openly). So this paper is not "Condorcet beats STAR"; it's "**if** you commit to always electing the Condorcet winner, **then** at three candidates maximin-leximin is your strongest defense." Whether to make that commitment at all is the [scores-vs-ranks](../../scores_and_ranks/scores_vs_ranks.md) fork, which this result doesn't settle.

## Bottom line

For the narrow, tractable case of **exactly three candidates**, Brandt, Dong & Peters give the maximin family the strongest theoretical justification any Condorcet rule has: **uniquely** no-show-immune among homogeneous rules, reinforcement-immune for small electorates, with clean axiomatic characterizations of maximin, Nanson, and leximin. It is the rigorous foundation under [Better Choices](better_choices_pairwise_ballot.md)' minimax count — with the fine print that it's a three-candidate result, that it's the tie-broken *refinements* that are characterized, that reinforcement still bites everyone at scale, and that it says nothing about score methods like STAR, which decline the Condorcet commitment the theorem is about.

---

*Source: Felix Brandt, Chris Dong & Dominik Peters, ["Condorcet-Consistent Choice Among Three Candidates"](https://arxiv.org/abs/2411.19857) (arXiv:2411.19857; [author PDF](https://dominik-peters.de/publications/maximinpara.pdf)). Neutral academic social-choice theory — no campaign affiliation on either side. Glossary: [`Condorcet`](../../GLOSSARY.md) · [`no-show paradox`](../../GLOSSARY.md). See also [Darlington's pro-Minimax case](condorcet_reading_list.md) in the reading list — advocacy for the same rule family, read with its lean marked.*
