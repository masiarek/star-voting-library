# Borda Count — Manufacturing Scores from Ranks

*If a **score** ballot can be reduced to a **ranking** (drop the intensity), can you go the other way — turn a ranking back into scores? You can. The one principled way to do it is the **Borda count**, and the act of doing it is exactly **inventing** the intensity the voter never gave.*

→ The reverse direction: [scores vs. ranks](../../00_start_here/scores_and_ranks/scores_vs_ranks.md) · [strict vs. weak ranks](../../00_start_here/scores_and_ranks/strict_vs_weak_ranks.md) · Borda-elimination methods: [Baldwin & Nanson](../RCV_IRV/concepts/variants/RCV-IRV-Baldwin-Nanson.md) · Glossary: [`Borda`](../../00_start_here/GLOSSARY.md)

---

## What Borda does

Assign points by a candidate's **position** in the ranking: with N candidates, 1st place = N−1 points, 2nd = N−2, …, last = 0. Then add the points across all ballots; highest total wins. That's the whole method — **positional scoring**.

Conveniently, the even-spaced points for a 6-candidate ballot land on **0–5**, so a Borda'd ranking *looks* exactly like a STAR ballot:

```
ranked:   E > A > B > F > D > C
Borda  →  E=5  A=4  B=3  F=2  D=1  C=0
```

Tied ranks get the **average** of the positions they span (a "midrank"). So `E > A=B=F > D > C` → E=5, then A,B,F share (4+3+2)/3 = **3** each, D=1, C=0.

## The catch: Borda *assumes equal gaps*

Those manufactured scores are **scores under an assumption** — never the voter's scores. A ranking carries *order only*; it is silent on *how much* you prefer one rank over the next. Borda fills that silence by assuming every gap is the same size. But the voter might have felt a **cliff**, not a **ramp**:

```
ranked:        E   >  A  >  B  >  F  >  D  >  C
the voter felt:  E ≈ A ≈ B  (all great)   ≫   F, D, C  (all bad)
real scores:     5,  5,  5,                    1,  0,  0
Borda's guess:   5,  4,  3,                    2,  1,  0   ← flattens the cliff into a ramp
```

Borda has no way to know the difference — *the intensity was never on the ballot*. So any scores it produces are an artifact of the **spacing rule**, not the electorate.

## Different spacings → different "scores"

There isn't one "right" way to invent intensity; each spacing tells a different story:

| Spacing | Points (top → bottom) | Assumes… |
|---------|------------------------|----------|
| **Borda (even)** | 5, 4, 3, 2, 1, 0 | every gap is equal |
| **Dowdall** | 1, ½, ⅓, ¼, … | the *top* ranks matter far more |
| **Convex / concave** | your choice | a steeper or flatter intensity curve |

All are defensible conventions; none is *the* answer. (This is also why Borda is strategy-prone — burying a rival or running clones shifts everyone's positional points.)

## The fidelity ladder — how much each conversion *invents*

This is the key idea. Converting between scores and ranks is never free; what matters is **how much you fabricate**:

| Conversion | Used by | Drops | **Invents** |
|------------|---------|-------|-------------|
| **score → weak rank** | **Ranked Robin** | intensity | **nothing** — ties stay ties (`A=B`) |
| **score → strict rank** | **RCV-IRV** | intensity | a tie-break order (`A=B` forced to `A>B`) |
| **rank → score** | **Borda** | — | the **whole intensity** (the spacing) |

Read top to bottom and the fabrication grows. **Ranked Robin's reduction is the honest one** — precisely because weak ranks let it keep the ties the voter expressed, so it invents nothing. IRV can't represent a tie, so it has to make one up (that's its fragility). Borda sits at the far end: it conjures the entire intensity dimension out of pure order.

That asymmetry is why **STAR → ranks works but ranks → STAR doesn't recover anything**: a score ballot *contains* its ranking, but a ranking never contained scores.

## Is Borda "bad," then?

No — Borda is a real, century-old, sometimes-used method (it sits in the **Positional** branch of the [methods family tree](../RCV_IRV/concepts/variants/RCV_methods_family_tree.mermaid)). It's even the engine inside the Condorcet-safe IRV variants [Baldwin and Nanson](../RCV_IRV/concepts/variants/RCV-IRV-Baldwin-Nanson.md), which eliminate by Borda score. The honest rule is just about **labeling**:

> **Manufacturing scores from ranks is fine — call them "Borda / positional points," never "the voter's scores."** The only real error is printing invented numbers next to the word *scores* as if the voter had typed them.

**Two facts that keep the criticism calibrated.** Borda's failures are usually cited without their bounds, so here are both directions:

- **Borda can deny a majority favorite.** Five voters: three rank `a ≻ b ≻ c`, two rank `b ≻ c ≻ a`. With weights `(2,1,0)`, `b` wins **7 to 6** — even though `a` is top-ranked by an outright majority *and* is the [Condorcet winner](../../00_start_here/topics/condorcet/). This is Borda failing the majority criterion in the smallest possible way, and it's why "Borda isn't Condorcet" isn't a technicality. Note also the sympathetic reading, which is genuinely held: some describe Borda as **a compromise that takes minority views into account, even when a majority completely agrees with one another** — whether that's a bug depends on what you think an election is for.
- **But Borda can never elect a Condorcet loser.** A Condorcet winner's Borda score is always *strictly above* the average, and a [Condorcet loser](../../00_start_here/GLOSSARY.md)'s is always *strictly below* it — so a Borda winner, being at or above average, can never be the candidate who loses every head-to-head. That's a real guarantee, and one [Choose-One plurality](../../00_start_here/topics/plurality.md) does **not** have.

## In this repo

- The engine can *optionally* show this on a ranked Ranked Robin ballot — set `options: { show_borda: true }` to annotate each ballot with its positional points, clearly labeled as Borda (not scores, and not what RR actually counts — RR uses pairwise).
- Borda is **not Condorcet** — and that's not an abstract criterion note, it's the objection Condorcet himself raised in 1788, with a worked 11-voter election you can run: [Condorcet's rebuttal to Borda](../../method_comparisons/borda_condorcet_1788/README.md). Borda's Condorcet-fixing cousins are [Baldwin & Nanson](../RCV_IRV/concepts/variants/RCV-IRV-Baldwin-Nanson.md).

## Related

- [Condorcet's 1788 rebuttal to Borda](../../method_comparisons/borda_condorcet_1788/README.md) — the historical counterexample: plurality *and* Borda elect Paul, but Peter beats everyone head-to-head
- [The dark horse](../../method_comparisons/dark_horse_borda/README.md) — Borda's *strategic* pathology, as opposed to the sincere one above
- [Scores vs. ranks](../../00_start_here/scores_and_ranks/scores_vs_ranks.md) — the reverse direction, and why scores are the richer object
- [Strict vs. weak ranks](../../00_start_here/scores_and_ranks/strict_vs_weak_ranks.md) — why ties matter (the ladder above)
- [Ranked Robin vs. Condorcet](../../05_Ranked_Robin/concepts/ranked_robin_vs_condorcet.md) — where the weak-rank reduction shows up live
- [Agenda voting](agenda_voting.md) — the other classic "ranked but not neutral" procedure in this folder
- [Which RCV-IRV?](../RCV_IRV/concepts/variants/RCV_IRV_variants.md) · Glossary: [`Borda`](../../00_start_here/GLOSSARY.md)

## Borda is the pairwise table, added up

A Borda score is not a separate thing from the head-to-head numbers — it *is* them, summed. Writing `M(x,y)` for the margin of `x` over `y`, `n` for ballots and `m` for candidates:

> **Borda(x) = ½ · Σ M(x,y) + n(m−1)/2**

The right-hand term is the same for every candidate, so **the pairwise margins alone fix the entire Borda ranking**. Equivalently and more simply: add up `x`'s head-to-head vote totals against each opponent, and that sum *is* `x`'s Borda score.

This is why Borda sits in Fishburn's **C2** tier — it reads the weighted tournament, exactly like Minimax and Ranked Pairs do, despite not being a Condorcet method. Three conditions: standard equally-spaced points; ties handled by splitting points evenly; and **truncation breaks it** — under the usual "unranked get 0" rule Borda is no longer margin-determined, so real truncated-ballot Borda is not C2.

The structural payoff: because Borda reads the table through a *sum* while Condorcet methods read it through *signs*, their disagreement isn't random — it lives entirely in the [circulating component of the margins](../../00_start_here/topics/cycle_cocycle_decomposition.md). Worked on twelve ballots in [Copeland vs Borda margins](../../method_comparisons/copeland_vs_borda_margins/), and framed in [what a method reads](../../00_start_here/topics/what_a_method_reads.md).
