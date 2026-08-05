# Parallel Universe Tiebreaking — when the tie is in the *middle* of the count

*Every other page in this hub answers the same question: the count has finished, the top is tied, who wins? **Parallel Universe Tiebreaking (PUT) answers a different one.** In a method that eliminates a candidate each round, a tie can strike while the count is still running — two candidates tied for last, and the rule must cut one. Whichever you cut changes every round that follows. PUT's answer is to refuse to choose: run **every** elimination order, and elect everyone who wins in **some** universe. It is the only tie convention in this library that treats an arbitrary mid-count coin flip as information to be reported rather than a detail to be settled and forgotten.*

→ **Level: 301 · deep dive** — part of the [Ties & Tie-Breaking](README.md) hub · the theorem underneath it: [Ties Are Forced](ties_are_forced.md) · where it bites hardest: [RCV-IRV](../../../06_Other/RCV_IRV/concepts/) · Glossary: [`lot numbers`](../../GLOSSARY.md)

---

## The gap this fills

[Ties Are Forced](ties_are_forced.md) catalogues **four ways out** of a tie — fixed ordering, randomize, return the tied set, assume it won't happen — and shows all four already running in this repo. That list is complete for the situation it describes: *the count is over and the top is tied.*

But a sequential-elimination method has a second, earlier tie, and none of the four is written for it:

> **The final tie asks "who wins?" The mid-count tie asks "which count do we even run?"**

Only methods that eliminate have this problem. [RCV-IRV](../../../06_Other/RCV_IRV/concepts/) has it every round. Coombs has it. Baldwin and Nanson have it. [Ranked Robin](../../../05_Ranked_Robin/01_Learn/) does **not** — it compares every pair at once, so there is no round order to get wrong — and neither does the [STAR](../../../01_STAR/) runoff, though STAR has a near-miss worth its own section [below](#stars-version-of-the-same-problem).

## Three answers, and what each conceals

| Answer | What it does | What it costs |
|---|---|---|
| **Pick one** | break the tie by lot, statute, or a seeded RNG, then continue down that single path | the result is real but **arbitrary** — and the arbitrariness is invisible in the report |
| **Batch-eliminate** | remove *all* candidates tied for last in one step | can delete a candidate who would have survived; the convention used in the [SEP entry](#sources) |
| **PUT** | branch on every legal elimination, union the winners | the winner set can grow — and the cost is combinatorial |

The first two produce exactly one winner and look decisive. That is precisely the problem: **they hide a genuine ambiguity behind a confident-looking report.** PUT is the only one of the three that tells you the count was ambiguous at all.

## Worked example — four voters, and a candidate who exists in only one universe

Four voters, three candidates:

```yaml
title: PUT demo — the winner depends on which tie you break
voting_method: RCV_IRV
num_winners: 1
ballots: |-
  2:A>B>C
  1:B>A>C
  1:C>B>A
```

First choices: **A 2, B 1, C 1.** Four voters, so a majority needs 3 — nobody has it. **B and C are tied for last**, and the rule must cut one.

**Universe 1 — eliminate C.** C's ballot is `C>B>A`, so it transfers to B:

```
A ......  2
B ......  2   ← 1 own + 1 transferred from C
                no majority (needs 3); two candidates, four voters → tied
```

**Universe 2 — eliminate B.** B's ballot is `B>A>C`, so it transfers to A:

```
A ......  3   ← majority, elected
C ......  1
```

So the two universes disagree: cut C and the election ends **tied between A and B**; cut B and **A wins outright**. PUT unions them:

> **PUT winner set = {A, B}** — where standard IRV reports **A**, full stop.

B's claim is not a technicality. There is a legal, correct execution of the rules in which B ties for the win, and whether that execution happens turns on a coin flip two steps earlier that appears nowhere in the result.

Note what is nested inside universe 1: two candidates and an even electorate, which is the [forced tie](ties_are_forced.md) of Moulin's proposition, arriving as a *sub-election* of a method that was supposed to have finished. The mid-count tie and the final tie are the same theorem wearing different clothes.

### Cross-checked three ways

Consistent with this library's [rule for Ranked Robin](../../../05_Ranked_Robin/01_Learn/rr_tiebreak_lh_vs_bv.md), the tally is confirmed against an engine nobody here wrote:

| Engine | Convention | Result |
|---|---|---|
| `pref_voting` `instant_runoff` | standard (pick one) | **{A}** |
| `pref_voting` `instant_runoff_put` | PUT | **{A, B}** |
| `pref_voting` `coombs_put` | PUT, Coombs elimination | **{A, B}** |
| batch-elimination (SEP convention) | cut B *and* C together | **{A}** |
| LH RCV-IRV engine | seeded pick-one | one winner, arbitrarily |

```bash
uv run python -c "from pref_voting.profiles import Profile; from pref_voting.iterative_methods import instant_runoff, instant_runoff_put; p=Profile([[0,1,2],[0,1,2],[1,0,2],[2,1,0]]); print(instant_runoff(p), instant_runoff_put(p))"
```

**Where this repo stands, stated plainly.** The vendored RCV-IRV engine takes the *pick-one* road, and says so in a comment at [`rcv_irv_tabulation.py`](../../../06_Other/RCV_IRV/RCV_IRV_tabulation_engine/rcv_irv_tabulation.py): pyrankvote breaks elimination ties with `random.choice()`, which unseeded would elect different winners from identical ballots run to run, so the engine sets `random.seed(0)` to make the coin flip "arbitrary but stable." That is the honest engineering choice for a library whose counts must reproduce — but it is worth knowing exactly what it buys and what it costs. **It buys reproducibility, not correctness.** On the ballots above, our own report would name a single winner and give no sign that a second candidate had an equal claim in a different universe.

## What PUT actually costs

Two costs, and only one of them is the famous one.

**1. It relocates the tie rather than removing it.** PUT's output is a *set*. When that set has more than one member you are back at [approach 3](ties_are_forced.md#four-ways-out-and-what-each-one-costs) — return the tied set — and still need a fixed order, a lot, or a coin to seat somebody. PUT does not save you from the four ways out. It moves the choice to the end, where it is **visible and reportable**, instead of burying it in round two.

**2. It is expensive.** Branching on every tied elimination explores up to `m!` elimination orders. This is the real barrier: in simulation work with many tied profiles, PUT implementations can simply fail to finish.

The saving grace is worth stating, because it is easy to miss: **the PUT winner set from a given state depends only on *which candidates remain*, not on the order that got you there.** So the search has at most `2^m` distinct states, not `m!` paths, and memoizing on the remaining-candidate set collapses the blow-up — for ten candidates, at most 1,024 states against 3.6 million orders. Whether a given implementation does this is worth checking before concluding that PUT is impractical.

**And in a public election, none of this matters.** Exact ties among thousands of ballots are astronomically rare, PUT and pick-one agree essentially always, and the honest summary is that this is a small-electorate and simulation concern. That is the [same caveat](why_contrived_tie_cases.md) the rest of this hub carries, and it applies here undiminished.

## STAR's version of the same problem

STAR has no elimination rounds, so it has no elimination-order problem. But it has one structurally similar moment: **which two candidates advance** to the automatic runoff. If three candidates tie for second place on total score, the choice of finalist decides the runoff, exactly as the choice of eliminee decides an IRV branch.

STAR resolves this with its [official tiebreak protocol](../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md) — pairwise, then five-star, then lot — which is a *pick-one* answer. A PUT-flavoured STAR would run the runoff for each candidate who could have advanced and report the union. Nobody proposes this, and the reason is instructive: STAR's ladder usually has real information left to use at that rung, so picking one is not arbitrary the way cutting a tied last-place candidate is. When the ladder *is* out of information — the [dead rung](../../../01_STAR/03_Criteria/tie_break_dead_rung/README.md) — the arbitrariness returns, and STAR is in the same position IRV was in.

This is also why the comparison in [Tie-Breaking: STAR vs RCV-IRV](tiebreaking_star_vs_irv.md) lands where it does. A score ballot carries more tie-breaking signal than a strict ranking, so the moment of pure arbitrariness arrives later and less often — not never.

## The honest limits

1. **PUT is not "more correct."** It is a different definition of the method, and a defensible argument says a voting rule ought to name a winner rather than a set of might-have-beens. What PUT is unambiguously better at is **disclosure**.
2. **It does not fix IRV's real problems.** [Center squeeze](../center_squeeze), [non-monotonicity](../monotonicity) and exhausted ballots are properties of the elimination *structure*, not of its tie convention. PUT changes nothing about any of them, and citing it as a repair would be exactly the overreach this library warns about elsewhere.
3. **The example here is engineered.** Four voters were chosen to make the branch visible on one screen. Do not read the size of the effect off the size of the example — see [why we build contrived tie cases](why_contrived_tie_cases.md).

## Sources

- Wesley H. Holliday & Eric Pacuit, [`pref_voting`](https://pref-voting.readthedocs.io/) — implements `instant_runoff_put`, `hare_put`, `coombs_put`, `plurality_with_runoff_put` and others; the cross-check engine used above. **Lean:** neutral; an academic library.
- Eric Pacuit, "Voting Methods," *Stanford Encyclopedia of Philosophy* — states Hare and Coombs with the **batch-elimination** convention ("all of the poorly performing candidates will be removed in each round"). **Lean:** neutral; the standard reference.
- Hervé Moulin, *The Strategy of Social Choice* (North-Holland, 1983) — the forced-tie proposition that shows up nested inside universe 1. Via [Ties Are Forced](ties_are_forced.md).
- The term itself comes from RCV-IRV tabulation practice, where implementers had to decide what a certified counting program does when two candidates tie for elimination.

## Related

- [Ties & Tie-Breaking hub](README.md) · [Ties Are Forced](ties_are_forced.md) — the four ways out, and why PUT is not one of them · [Why build "silly" tie elections?](why_contrived_tie_cases.md)
- [Tie-Breaking: STAR vs RCV-IRV](tiebreaking_star_vs_irv.md) — fewer ties, or easier ties?
- [Which RCV-IRV? § tie-breaks](../../../06_Other/RCV_IRV/concepts/variants/RCV_IRV_variants.md) — how real statutes answer the mid-count tie
- [Ranked Robin tiebreaks — LH vs BetterVoting](../../../05_Ranked_Robin/01_Learn/rr_tiebreak_lh_vs_bv.md) — two engines, identical ballots, different winners
- [The Smith set](../smith_set.md) · [Glossary](../../GLOSSARY.md)
