# The Majority Criterion (and the Relaxed Majority Criterion)

*Plain-language first, jargon and references at the very bottom. This is the "a majority scored them highest but they still lost?!" idea — the objection FairVote raises most against STAR — and Equal Vote's answer to it.*

Part of the [Concepts by topic](../README.md) hub. Closely tied to [Later-No-Harm](#the-same-fork-as-later-no-harm) and [STAR's honest limits #8](../../STAR_Voting/STAR_honest_limits.md).

---

## The plain-English version

A **majority** just means *more than half the voters*. The **Majority Criterion** is a simple fairness rule people expect from an election:

> If more than half of voters like candidate X best, X should win.

Choose-One (plurality) and RCV-IRV always obey this rule. **STAR does not always obey it** — and that's the thing critics point at. It sounds damning until you see *when* it happens, because it turns out STAR only breaks the rule in a very specific, arguably-healthy situation.

## The whole idea in two tiny elections

Five voters. Three of them (a **60% majority**) love **Ada** — they give her the top score, 5. The other two can't stand Ada (they give her 0) but love **Bruno** and **Cleo** (5 each). The only thing we change between the two elections is *how generous Ada's own supporters are to everyone else.*

**Election A — Ada's majority backs only ONE other candidate** ([`bv95a`](../../../01_STAR/majority_criterion/bv95a_9m6rxr_favorite_survives_one_rival.md)). They give Bruno a 4 and Cleo a 0:

```
Ada,Bruno,Cleo
5,4,0   ← the 3-voter majority (×3)
0,5,5   ← the 2-voter minority (×2)

Totals: Ada 15, Bruno 22, Cleo 10
Finalists (top two by score): Bruno & Ada  →  runoff: Ada beats Bruno  →  ADA WINS ✓
```

Ada's majority got their favorite. Supporting *one* compromise candidate cost them nothing.

**Election B — the same majority also backs a SECOND candidate** ([`bv95b`](../../../01_STAR/majority_criterion/bv95b_7pdq3r_favorite_loses_two_rivals.md)). Everything identical except they now give Cleo a 3 instead of 0:

```
Ada,Bruno,Cleo
5,4,3   ← the 3-voter majority (×3)
0,5,5   ← the 2-voter minority (×2)

Totals: Ada 15, Bruno 22, Cleo 19
Finalists (top two by score): Bruno & Cleo  →  Ada never reaches the runoff  →  BRUNO WINS ✗
```

Now Ada — the top choice of a clear majority — **loses**. That's the Majority-Criterion failure in one move.

## The point everyone misses

Look at *what it took* to make Ada lose: her own majority had to spread real support across **two** other candidates. If they'd backed only one (Election A), Ada was safe. STAR's failure needs the majority to be generous to a *second* rival — which is a much narrower, harder-to-trigger situation than it first sounds.

And notice *why* Ada loses in Election B: **almost everyone likes Bruno** (the majority gave him a 4, the minority a 5), while 40% of voters actively reject Ada. STAR is deciding that a broadly-liked candidate nobody hates (Bruno) is a better representative than a divisive one that 40% score at rock bottom (Ada). Whether that's a bug or a feature is the whole debate. FairVote sees "the majority was overruled." Equal Vote sees "a polarizing candidate was correctly passed over for a consensus one."

## The Relaxed Majority Criterion — Equal Vote's answer

Equal Vote argues the *strict* rule is the wrong yardstick, and proposes a gentler one that captures what actually matters. Their **Relaxed Majority Criterion (RMC)** asks: can a majority safely give their second choice a *high-but-not-top* score without accidentally sinking their favorite?

> "A voting system satisfies the **Relaxed Majority Criterion** if a majority faction of voters can express a non-zero 'maximum support − 1' to a second choice candidate, and still guarantee that the majority faction's 'maximum supported' first choice wins." — Mark Frohnmayer, Equal Vote, 2017

In our example: Ada's majority gave Bruno a 4 (that's "max − 1", one below the top). RMC asks whether that alone can cost them Ada. It can't — it took a *second* supported candidate. So **STAR passes the Relaxed Majority Criterion.** Score and Approval voting **fail** it — with those methods, supporting a single second candidate can already sink your favorite. RMC is thus the line Equal Vote draws between "acceptably mild" and "genuinely broken."

Methods that **pass** RMC: RCV-IRV, **STAR**, Unified Primary, 3-2-1. Methods that **fail** RMC: Score, Approval.

## The same fork as Later-No-Harm

Here's the deep connection — the Majority-Criterion failure and STAR's **Later-No-Harm** failure ([honest limit #3](../../STAR_Voting/STAR_honest_limits.md)) are *the same event*, described two ways.

- **Later-No-Harm** (a voter's-eye view): "scoring my *later* choices should never hurt my favorite." STAR breaks this.
- **Majority Criterion** (the electorate's view): "a majority's favorite should win." STAR can break this.

In Election B, the majority's honest 3 for Cleo (a *later* preference) is exactly what pushed Ada out of the finals. Their later support harmed their favorite — a Later-No-Harm failure — and *because* it did, the majority's favorite lost — a Majority-Criterion failure. **They are one phenomenon.** If Ada's voters had "bullet voted" (Ada 5, everyone else 0), both rules would hold — Ada would win. STAR's failures here happen *only because voters honestly expressed support they were told was safe to give.*

This is a deliberate design fork, and it also explains [why STAR isn't Condorcet-compliant](../condorcet/) (honest limit #1):

| | keeps Later-No-Harm + Majority Criterion | rewards broad / consensus support |
|---|:--:|:--:|
| **RCV-IRV** (only counts first choices) | ✅ | ❌ (center squeeze) |
| **STAR** (runoff weighs strength & breadth) | ❌ | ✅ (resists center squeeze) |

You cannot have both columns at once — that's a theorem, not a preference (see references). STAR picks the right column; IRV picks the left. Everything else follows.

## Which methods, and where

| Method | Majority Criterion | Relaxed Majority Criterion | Detailed treatment |
|--------|:--:|:--:|--------------------|
| Choose-One (plurality) | ✅ | ✅ | [plurality](../plurality.md) |
| RCV-IRV | ✅ | ✅ | [rcv_irv_vs_star](../rcv_irv_vs_star.md) |
| **STAR** | ❌ *(needs 2 rivals)* | ✅ | [STAR honest limits #8](../../STAR_Voting/STAR_honest_limits.md) |
| Score | ❌ *(1 rival)* | ❌ | [range voting](../../Range_Voting/range_voting.md) |
| Approval | ❌ *(1 rival)* | ❌ | [approval](../../Approval_Voting/) |

Worked demonstrations in this repo — each with its own per-election page: [BV95a — favorite survives](../../../01_STAR/majority_criterion/bv95a_9m6rxr_favorite_survives_one_rival.md) / [BV95b — favorite loses](../../../01_STAR/majority_criterion/bv95b_7pdq3r_favorite_loses_two_rivals.md), plus the [Black Curtain set](../../../method_comparisons/black_curtain/README.md) (a polarizing "winner" vs a hidden consensus). Both BV95 elections were also reproduced live on BetterVoting — [`9m6rxr`](https://bettervoting.com/9m6rxr) elects Ada, [`7pdq3r`](https://bettervoting.com/7pdq3r) elects Bruno — so the demo is verified on the real platform, not just the LH engine.

---

## Formal definitions, jargon & literature

Now the precise, technical statements (for readers who want them):

**Majority criterion (formal).** *If a strict majority of voters rank a single candidate first (or, for cardinal ballots, give one candidate a strictly higher score than every other), that candidate must be elected.* For rated ballots it's often stated as the **majority-favorite criterion**. STAR, Score, and Approval fail it; plurality, IRV, and all Condorcet methods pass it.

**Bullet voting / factional bullet voting.** Casting a ballot that supports *only* one candidate (max for your favorite, zero for all others), forgoing honest support for compromise candidates — the strategic response the strict criterion is hypothesized to encourage.

**Relaxed Majority Criterion (RMC).** Frohnmayer's weakening (above): a majority may give a second candidate a score of `max − 1` and still be guaranteed their `max`-scored favorite wins. Passed by IRV, STAR, Unified Primary, 3-2-1; failed by Score and Approval. It formalizes "how *severe* is the majority-criterion failure" rather than the binary "does it ever occur."

**Later-No-Harm (LNH).** *Adding a lower preference to your ballot must not decrease the probability that a candidate you rank higher wins.* Satisfied by IRV; failed by STAR/Score/Approval by construction (the runoff/total can promote your second choice over your first).

**The incompatibility.** No monotonic method can satisfy both **Later-No-Harm** and the **Condorcet criterion** (Woodall); more broadly, Arrow's and Gibbard–Satterthwaite's theorems guarantee every deterministic method with ≥3 candidates trades away *some* desirable property and has *some* scenario rewarding insincere voting. So "STAR fails the majority criterion" is not a unique defect — it is one face of a universal set of trade-offs.

**References.**

- Majority criterion — Wikipedia: <https://en.wikipedia.org/wiki/Majority_criterion>
- Frohnmayer, M. (2017), *The Relaxed Majority Criterion*, Equal Vote Coalition: <https://www.equal.vote/rmc>
- STAR Voting / complete ranking & Condorcet-loser note — electowiki: <https://electowiki.org/wiki/STAR_voting>
- Later-no-harm criterion — Wikipedia: <https://en.wikipedia.org/wiki/Later-no-harm_criterion>
- Woodall, D. (1997), *Monotonicity of single-seat preferential election rules* (Later-no-harm ⊥ Condorcet).
- Gibbard (1973) / Satterthwaite (1975); Arrow (1951) — impossibility & strategy-proofness.
- FairVote's majority-criterion argument against Score/Approval (the piece RMC responds to): <https://www.fairvote.org/why-approval-voting-is-unworkable-in-contested-elections>

> **Balance.** FairVote's objection is real: STAR genuinely fails a criterion many find intuitive, and "we prefer the relaxed version" is a value judgment, not a proof. The counter is equally real: the failure is mild (needs two supported rivals), the resulting winner has broad support, and *no* method escapes the underlying impossibility results. Judge the whole board, not one square.
