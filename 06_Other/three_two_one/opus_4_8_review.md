# 3-2-1 Voting — an AI assessment

*An opinionated review of [3-2-1 voting](README.md) written by **Claude Opus 4.8** on 2026-07-23, at Adam's request. This page is **commentary, not repo canon** — it contains judgements, not measurements. Everything factual in it is sourced below; everything evaluative is one model's read and should be argued with.*

> **How to read this page.** The rest of the library states things it can verify — a tabulation, a criterion, a simulated rate with its model attached. This page does something different: it *judges*. Judgements can't be regression-tested, so they're quarantined here, signed and dated, rather than mixed into the concept pages. If you want the neutral treatment, read [3-2-1 voting](../../00_start_here/topics/three_two_one_voting.md) and [the method folder](README.md) instead.

## Provenance and lean (read first)

- **What I read:** this repo's [3-2-1 concept page](../../00_start_here/topics/three_two_one_voting.md), [the folder README](README.md) with Quinn's spec, and the [clean-room engine](three_two_one_tabulation.py) verified against Quinn's own reference vectors.
- **What I did *not* read:** the [electowiki 3-2-1 article](https://electowiki.org/wiki/3-2-1_voting) — it returned HTTP 403 when fetched. That is the method's primary public definition and it may raise criticisms I haven't weighed. **This is a real gap in the review.**
- **My lean:** I formed this view largely from pages written in a STAR-advocating house style, so it likely under-sells 3-2-1. I've tried to correct for that and probably haven't fully.
- **Bottom line I'd defend:** 3-2-1 is a good method; I'd take it over RCV-IRV without hesitation; I'd take STAR over it, but I hold that last preference loosely.

## What's genuinely good

**The explicit guards are underrated.** The ½-Good dark-horse rule and the fewest-Bad finalist step mean that when someone asks *"what stops a nobody from winning?"*, you point at a rule. STAR answers the same question correctly but **emergently** — the scores simply happen to prevent it. In a legislative hearing, a rule you can point at beats a property you have to derive. That is a real political asset, and STAR advocates tend to treat it as a wart.

**Good / OK / Bad is more legible than 0–5** to a genuinely skeptical audience. Three words, no arithmetic implied. I think the STAR world underestimates how much *"score each candidate 0 to 5"* reads as **homework** to people who aren't already interested in voting theory. 3-2-1's ballot has no such tax.

**The outcomes are fine.** No [center squeeze](../../00_start_here/RCV_IRV/RCV_IRV_center_squeeze.md), a non-slippery [chicken dilemma](../../method_comparisons/chicken_dilemma/), [summable](../../00_start_here/topics/summability/), high VSE. It's in STAR's league, and both are in a different league from IRV and plurality.

## Where I think it's wrong

### 1. It simplifies the wrong end

3-2-1 pairs a simple ballot with a **three-stage count containing special cases** — the ½-Good threshold, the skip-step-2 conditional. STAR trades the other way: a slightly richer ballot, then *add the scores and hold one runoff*.

Voters touch the ballot **once**, in private, with instructions in front of them. Officials, auditors, journalists, judges and opponents touch the **count** forever. And the count is precisely where RCV-IRV bleeds — [summability](../../00_start_here/RCV_IRV/RCV_IRV_lack_of_summability.md), central tabulation, *"explain to me why my candidate was eliminated."*

Optimizing ballot simplicity while adding count complexity is spending your simplicity budget on the easy problem.

### 2. The granularity tie is structural, not an edge case

Three levels means **the deciding step often has nothing to read**. If two allies are both honestly *Good*, no voter distinguishes them, and step 3 is a coin flip — the repo's own [worked example](../../00_start_here/topics/three_two_one_voting.md) shows exactly this.

STAR's fix is free: scoring your favorite **5** and your ally **4** is natural and costs nothing emotionally. 3-2-1 needs voters to spend the *OK* level **strategically** — to demote someone they actually like — for the final step to function. That's a small honesty tax baked into the design, and it lands on exactly the cooperative voters a good method should protect.

### 3. Bolt-on constants age badly

*"At least ½ as many Good ratings"* invites the obvious question: **why one half?** There is no principled answer, only a tuned one. Every such constant is a surface for an opponent to attack, and a thing that can be wrong for a particular electorate. I'd rather have properties that fall out of the mechanism than parameters someone chose.

(To be fair to Quinn: he was a statistician who tuned constants against simulation, which is a *better* reason than intuition. The objection is about political durability, not rigor.)

## The strategic reality

3-2-1 is an **orphan**. Quinn designed it and [died in March 2025](../../00_start_here/topics/in_memoriam_jameson_quinn.md); the Center for Election Science campaigns for Approval, the Equal Vote Coalition for STAR and Ranked Robin. Nobody is carrying it.

That is not a criticism of the method — plenty of good ideas lack a campaign — but it means the practical choice essentially never comes down to *"STAR or 3-2-1."* Its live role is as a **reference point that sharpens how you argue for the others**, which is exactly why this repo keeps a working engine for it.

## What I actually take from it

The most valuable thing about 3-2-1 isn't the method. It's that 3-2-1 is the **cleanest illustration that "simplicity" is two axes, not one** — a simple ballot bolted to a comparatively involved count. The neutral treatment, with every method placed on both axes, is [What makes a voting method good? §2](../../00_start_here/topics/what_makes_a_voting_method_good.md) (see also [Is RCV "simple"? — which half?](../../00_start_here/RCV_IRV/RCV_IRV_is_simple.md)).

Once you hold the axes apart, the STAR-vs-3-2-1 disagreement stops being *"which is simpler?"* — unanswerable, since each side points at a different axis — and becomes *"which kind of simplicity is worth more?"*, which you can actually argue.

My answer: **count simplicity is worth more**, because it's the axis that determines whether officials can administer the method, auditors can verify it, and opponents can misrepresent it. Ballot complexity is a one-time explanation cost. Count complexity is a permanent attack surface.

Reasonable people land differently on that, and if you think voter comprehension is the binding constraint on adoption, 3-2-1 beats STAR on your own terms.

---

*Written by Claude Opus 4.8, 2026-07-23. Opinion, openly biased toward the repo's house methods, and offered as something to disagree with. Corrections and rebuttals are more useful to the library than agreement — if a claim here is wrong, fix the page rather than preserving it.*
