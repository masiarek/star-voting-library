# Parallel Universe Tiebreaking — when the tie is in the *middle* of the count

*Every other page in this hub answers the same question: the count has finished, the top is tied, who wins? **Parallel Universe Tiebreaking (PUT) answers a different one.** In a method that eliminates a candidate each round, a tie can strike while the count is still running — two candidates tied for last, and the rule must cut one. Whichever you cut changes every round that follows. PUT's answer is to refuse to choose: run **every** elimination order, and elect everyone who wins in **some** universe. It is the only tie convention in this library that treats an arbitrary mid-count coin flip as information to be reported rather than a detail to be settled and forgotten.*

→ **Level: 301 · deep dive** — part of the [Ties & Tie-Breaking](README.md) hub · the theorem underneath it: [Ties Are Forced](ties_are_forced.md) · where it bites hardest: [RCV-IRV](../../../06_Other/RCV_IRV/concepts/README.md) · Glossary: [`lot numbers`](../../GLOSSARY.md)

---

## The gap this fills

[Ties Are Forced](ties_are_forced.md) catalogues **four ways out** of a tie — fixed ordering, randomize, return the tied set, assume it won't happen — and shows all four already running in this repo. That list is complete for the situation it describes: *the count is over and the top is tied.*

But a sequential-elimination method has a second, earlier tie, and none of the four is written for it:

> **The final tie asks "who wins?" The mid-count tie asks "which count do we even run?"**

Only methods that eliminate have this problem. [RCV-IRV](../../../06_Other/RCV_IRV/concepts/README.md) has it every round. Coombs has it. Baldwin and Nanson have it. [Ranked Robin](../../../05_Ranked_Robin/01_Learn/README.md) does **not** — it compares every pair at once, so there is no round order to get wrong — and neither does the [STAR](../../../01_STAR/README.md) runoff, though STAR has a near-miss worth its own section [below](#stars-version-of-the-same-problem).

## Three answers, and what each conceals

| Answer | What it does | What it costs |
|---|---|---|
| **Pick one** | break the tie by lot, statute, or a seeded RNG, then continue down that single path | the result is real but **arbitrary** — and the arbitrariness is invisible in the report |
| **Batch-eliminate** | remove *all* candidates tied for last in one step | can delete a candidate who would have survived; the convention used in the [SEP entry](#sources) |
| **PUT** | branch on every legal elimination, union the winners | the winner set can grow — and the cost is combinatorial |

Pick-one always produces exactly one winner and looks decisive. That is precisely the problem: **it hides a genuine ambiguity behind a confident-looking report.** Batch elimination *usually* does the same — but not always, and the exception is worth knowing: when the tied batch is the **entire remaining field**, it empties the ballot and reports every one of them as tied for the win. On a symmetric profile that is the only answer an anonymous, neutral rule may give. → [Batch elimination — what happens when the batch is *everyone*](batch_elimination.md).

So of the three, PUT is the one that discloses a mid-count ambiguity *whenever* there is one; batch elimination discloses it only when the tie is total.

## Worked example — four voters, and a candidate who exists in only one universe

Four voters, three candidates — the runnable case is [`put_two_universes_c3_b4`](../../../06_Other/RCV_IRV/cases/cases_pages/put_two_universes_c3_b4.md):

| Voters | Ballot |
|:--:|---|
| 2 | Anna > Blake > Cora |
| 1 | Blake > Anna > Cora |
| 1 | Cora > Blake > Anna |

First choices: **Anna 2, Blake 1, Cora 1.** Four voters, so a majority needs 3 — nobody has it. **Blake and Cora are tied for last**, and the rule must decide who goes.

**Universe 1 — eliminate Cora.** Her ballot is `Cora>Blake>Anna`, so it transfers to Blake:

```text title="Abridged for the lesson — not verbatim engine output"
Anna ....  2
Blake ...  2   ← 1 own + 1 transferred from Cora
               no majority (needs 3); two candidates, four voters → tied
```

**Universe 2 — eliminate Blake.** His ballot is `Blake>Anna>Cora`, so it transfers to Anna:

```text title="Abridged for the lesson — not verbatim engine output"
Anna ....  3   ← majority, elected
Cora ....  1
```

So the two universes disagree: cut Cora and the election ends **tied between Anna and Blake**; cut Blake and **Anna wins outright**. PUT unions them:

> **PUT winner set = {Anna, Blake}** — where standard RCV-IRV reports **Anna**, full stop.

Blake's claim is not a technicality. There is a legal, correct execution of the rules in which he ties for the win, and nothing in a standard report records that the execution which erased him was one of two available.

Note what is nested inside universe 1: two candidates and an even electorate, which is the [forced tie](ties_are_forced.md) of Moulin's proposition, arriving as a *sub-election* of a method that was supposed to have finished. The mid-count tie and the final tie are the same theorem wearing different clothes.

### Cross-checked three ways

Consistent with this library's [rule for Ranked Robin](../../../05_Ranked_Robin/01_Learn/rr_tiebreak_lh_vs_bv.md), the tally is confirmed against an engine nobody here wrote:

| Engine | Convention | Result |
|---|---|---|
| `pref_voting` `instant_runoff` | standard | **{Anna}** |
| `pref_voting` `instant_runoff_put` | PUT | **{Anna, Blake}** |
| `pref_voting` `coombs_put` | PUT, Coombs elimination | **{Anna, Blake}** |
| batch-elimination (SEP convention) | cut Blake *and* Cora together | **{Anna}** |
| LH RCV-IRV engine (vendored pyrankvote) | batch, in one round | **Anna**, seed-independent |

```bash
uv run python -c "from pref_voting.profiles import Profile; from pref_voting.iterative_methods import instant_runoff, instant_runoff_put; p=Profile([[0,1,2],[0,1,2],[1,0,2],[2,1,0]]); print(instant_runoff(p), instant_runoff_put(p))"
```

And this is what our own engine prints for the same ballots:

<!-- report:put_two_universes_c3_b4 -->
```text
--- RCV / Instant-Runoff Voting (single winner) ---
  Parallel universes — one count, two legal answers
 Tabulating 4 ballots (ranked ballots).

FINAL RESULT
Candidate      Votes  Status
-----------  -------  --------
Anna               2  Elected
Blake              1  Rejected
Cora               1  Rejected


Winner(s) — RCV / Instant-Runoff Voting (single winner)
  Anna
```
<!-- /report -->

**Where this repo stands, stated plainly — and it is not what you would guess.** You might expect our engine to flip a coin and hide the flip. It does not. Run [the case file](../../../06_Other/RCV_IRV/cases/cases_pages/put_two_universes_c3_b4.md) and the vendored `pyrankvote` removes **both** tied candidates in a single step and elects Anna in one round, listing Blake and Cora side by side as `Rejected`. Nothing in the output says a tie was ever resolved.

The engine does seed its RNG — [`rcv_irv_tabulation.py`](../../../06_Other/RCV_IRV/RCV_IRV_tabulation_engine/rcv_irv_tabulation.py) sets `random.seed(0)` because pyrankvote can break ties with `random.choice()`, which unseeded would elect different winners from identical ballots run to run. That is the right call for a library whose counts must reproduce. But **it is not what produces the answer here**: this result is seed-independent, verified at seeds 0, 1, 2, 7, 42 and 99, all Anna.

So this is not a story about hidden randomness. It is a story about a **hidden assumption**. Batch-removing both candidates is justified by noting that Blake and Cora hold only 2 votes between them, which cannot exceed Anna's 2 — but that reasoning quietly treats a 2–2 tie as a *loss* for Blake, which is precisely the question at issue. The winner is perfectly reproducible and still incomplete. **Reproducibility is not correctness**, and determinism is not disclosure.

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
2. **It does not fix IRV's real problems.** [Center squeeze](../center_squeeze/README.md), [non-monotonicity](../monotonicity/README.md) and exhausted ballots are properties of the elimination *structure*, not of its tie convention. PUT changes nothing about any of them, and citing it as a repair would be exactly the overreach this library warns about elsewhere.
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
