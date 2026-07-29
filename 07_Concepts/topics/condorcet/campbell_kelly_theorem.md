# The Campbell–Kelly Theorem — "May's Theorem for three or more alternatives"

*[May's Theorem](../mays_theorem.md) leaves an obvious question hanging: it proves majority rule is uniquely right for **two** alternatives, and its content evaporates at three. So which rule inherits the mantle? On the **full domain** the honest answer is nobody — no completely satisfactory extension of May exists. But **restrict the domain to profiles where a Condorcet winner exists**, and a uniqueness theorem comes back: electing the head-to-head winner is resolute, anonymous, neutral, and **strategyproof** — and for an odd number of voters it is the **only** such rule. This is the strongest positive result in the Condorcet family's favour, and it is worth stating at full strength before stating its limit.*

→ Level: **Voting 301** ([301.19](../../curriculum/CURRICULUM_301.md)) · the two-candidate original: [May's theorem](../mays_theorem.md) · the impossibility it does *not* contradict: [Gibbard–Satterthwaite](../gibbard_satterthwaite_theorem.md) · the family it characterises: [the Condorcet hub](README.md) · this repo's Condorcet method: [Ranked Robin](../../../05_Ranked_Robin/concepts/ranked_robin.md).

---

## The question, and the negative half of the answer

Every method in this library reduces to majority rule at two candidates — [STAR, RCV-IRV, Ranked Robin and Approval all collapse to it](../mays_theorem.md#at-two-candidates-every-method-here-collapses-to-majority-rule) — and each does so naturally. So on that basis almost any rule could claim to be "majority rule, generalised."

**For social choice functions on the full domain, no rule wins the mantle.** There is no completely satisfactory extension of May's Theorem to three or more alternatives — the four conditions simply stop pinning anything down once `m ≥ 3`. (Extensions *do* exist in other voting contexts, and for rules on restricted domains, which is the door this page walks through.)

So the trick is to stop asking for a rule that behaves well on *every* profile.

## Two definitions that make the restriction precise

**Pairwise Majority Rule (PMR)** elects the [Condorcet winner](README.md) — the candidate who beats every rival head-to-head — and is simply **undefined** when no Condorcet winner exists. That makes PMR not a normal voting rule but *an SCF with a restricted domain*.

**The Condorcet domain** `𝒟_Condorcet` is the set of profiles for which a Condorcet winner exists. And an SCF `f` is a **Condorcet extension** (or *Condorcet consistent*) if it selects the Condorcet winner alone for every profile in `𝒟_Condorcet` — that is, it agrees with PMR wherever PMR has an opinion, and does something of its own devising on the rest.

That's the definition the repo has been using informally all along, now with the part that matters made explicit: **"Condorcet extension" constrains a method only on `𝒟_Condorcet`, and says nothing whatsoever about cycles.** [Ranked Robin / Copeland qualifies](#why-copeland-qualifies-the-one-line-proof); so do Minimax, Ranked Pairs, Schulze, Baldwin and Nanson. [STAR does not](#what-this-means-for-star).

## The theorem

> **Theorem (Campbell & Kelly, 2003).** Consider SCFs with domain `𝒟_Condorcet`, for three or more alternatives. Pairwise Majority Rule is **resolute, anonymous, neutral, and strategyproof**; for an odd number of voters, it is the **unique** such rule.

Set that beside May and the parallel is exact — same axioms, one substitution:

| | **May (1952)** | **Campbell–Kelly (2003)** |
|---|---|---|
| Alternatives | exactly 2 | 3 or more |
| Domain | full | `𝒟_Condorcet` only |
| Axioms | resolute, anonymous, neutral, **monotonic** | resolute, anonymous, neutral, **strategyproof** |
| Odd `n` | required for this form | required for uniqueness |
| Unique rule | majority rule | Pairwise Majority Rule |

**And the substitution isn't really a substitution.** At `m = 2`, monotonicity **is** strategyproofness — with only two options, the sole way to manipulate is to vote for the one you like less, and monotonicity is exactly what makes that pointless. So Campbell–Kelly keeps May's fourth axiom and merely writes it in the form that still has teeth at three candidates. That is what earns it the name.

**Why PMR is strategyproof** is a one-line argument worth knowing, because it explains the whole result. Suppose `x` is the Condorcet winner and you sincerely prefer `y` to `x`. To get `y` elected you would have to overturn `x`'s pairwise majority over `y` — and that majority is composed of *other voters' ballots*. Changing your own ballot cannot reverse it. Your vote was already counted against `x` in that matchup; there is nothing left to withhold. Manipulation has no lever to pull.

**The published result is stronger than the version above.** Campbell and Kelly assume **nonimposition** and **nondictatoriality** in place of anonymity and neutrality — weaker hypotheses, so a stronger theorem. A second version of their result assumes **group** strategyproofness (no coalition can gain by coordinating) and then drops the odd-`n` requirement entirely.

### Why Copeland qualifies — the one-line proof

A Condorcet winner beats all `m − 1` rivals, so their [Copeland score](../../../05_Ranked_Robin/concepts/ranked_robin.md) is `m − 1` — the maximum possible, and no one else can reach it (they lost to the Condorcet winner). Uniquely highest ⇒ Copeland elects them ⇒ **Copeland, and therefore [Ranked Robin](../../../05_Ranked_Robin/concepts/ranked_robin.md), is a Condorcet extension.** Two sentences, no case analysis.

## The honest limits — read these before citing it

This is a real theorem and a genuinely strong card. It is also routinely overstated, in four specific ways.

**1. The restriction is doing enormous work.** `𝒟_Condorcet` is precisely the set of *easy* profiles — the ones where an obvious answer exists. The theorem says: **when there is an obvious answer, taking it is uniquely well-behaved.** True, valuable, and much narrower than "Condorcet methods are optimal." Every genuine dispute in this library lives *outside* the domain: [cycles](../../../05_Ranked_Robin/concepts/cycle_resolution.md), the [minimal tilted cycle](../../../method_comparisons/minimal_tilted_cycle/README.md), how to resolve the [Smith set](../smith_set.md). On exactly the profiles where methods disagree, Campbell–Kelly is silent by construction.

**2. It cannot choose among Condorcet methods.** Every Condorcet extension agrees with PMR on `𝒟_Condorcet` — that *is* the definition — so the theorem cannot distinguish Ranked Robin from [Minimax](../../voting_paradoxes/minimax.md) from Ranked Pairs from Schulze. It characterises the **family** on the easy profiles and offers nothing on the hard ones, which is where the entire cycle-resolution literature lives.

**3. It does not contradict Gibbard–Satterthwaite — and the reason is the useful lesson.** [G–S](../gibbard_satterthwaite_theorem.md) says every reasonable full-domain rule for `m ≥ 3` is manipulable. Campbell–Kelly exhibits a strategyproof rule for `m ≥ 3`. Both are true because strategyproofness *on a restricted domain* requires the sincere profile **and** the manipulated one to lie inside that domain — a voter who could push the electorate into a cycle is doing something the theorem never quantified over. The takeaway is worth stating plainly:

> **Gibbard–Satterthwaite's bite comes from the full domain, not from having three or more candidates.**

That corrects a common sloppy reading in which G–S is treated as a curse that switches on at three candidates. It switches on when you insist the rule answer *every* profile.

**4. Condorcet consistency is a plausible axiom, not a self-evident one.** Some treat it as absolutely required of a voting rule; that view is not universal, and the honest classification puts it among the **plausible axioms that cannot all be satisfied at once** — the same bucket as [later-no-harm](../criteria_at_a_glance.md), [participation](../participation/), and [consistency](../../voting_paradoxes/multiple_districts.md). Adopting it is a choice with a price, not a free win. [Ranked Robin pays for it](../criteria_at_a_glance.md#what-the-pattern-actually-says) in participation, consistency and clone-independence.

## What this means for STAR

Stated plainly, because this repo's rule is that [fairness has to cut against STAR too](../../../method_comparisons/paradoxes_and_whoops/reading_these_fairly.md):

**STAR is not a Condorcet extension.** It can and does miss the Condorcet winner on some profiles — that's a documented, runnable fact here, not a concession extracted under pressure. So on the axis Campbell–Kelly characterises, **STAR is outside the characterised set and Ranked Robin is inside it.** A Condorcet advocate citing this theorem against STAR is citing it correctly.

Three things worth saying alongside that, none of which are dodges:

- **The theorem's axis is one axis.** It says nothing about [center squeeze](../center_squeeze/), [distortion](../distortion.md), expressiveness, or [strategic incentive](../pvsi_strategic_incentive.md) in the full-domain world elections actually inhabit. STAR's case has never rested on Condorcet efficiency, and this theorem doesn't move it.
- **STAR's Condorcet efficiency is empirically high** — it elects the Condorcet winner on the large majority of realistic profiles ([measured](condorcet_efficiency_measured.md): 74–99%, depending on the field size and the electorate model) — so "not a Condorcet extension" is a statement about a guarantee, not about typical behaviour. Guarantee ≠ frequency, in both directions; that cuts against overstating STAR's misses *and* against overstating the guarantee's practical value.
- **This is exactly why [Ranked Robin is the olive branch](../../../05_Ranked_Robin/concepts/ranked_robin.md)** in this library's comparisons. If Condorcet consistency is the property you can't give up, there's a method here that has it, on the same ranked ballot, without IRV's elimination pathologies. Campbell–Kelly is the formal statement of what that buys.

## The bookend

Read the three theorems in order and they say something none of them says alone:

| | Result | What it settles |
|---|---|---|
| **May** | majority rule is *the* rule | at **two** alternatives, full domain |
| **Campbell–Kelly** | PMR is *the* rule | at **three or more**, but only on `𝒟_Condorcet` |
| **[Gibbard–Satterthwaite](../gibbard_satterthwaite_theorem.md)** | *no* rule is strategyproof | at **three or more**, full domain |

> **Uniqueness survives the jump to three candidates only if you also give up answering every profile.** Ask for a rule that always decides, and strategyproofness goes with it.

Which is the same shape as [Ties Are Forced](../ties/ties_are_forced.md) one level down: there, insisting on always naming *one* winner costs you an axiom; here, insisting on always naming a winner *at all* costs you strategyproofness. Both are the price of a total function.

## Sources

- D. E. Campbell & J. S. Kelly, "A strategy-proofness characterization of majority rule," *Economic Theory* 22 (2003), pp. 557–568 — Theorem 1; the nonimposition/nondictatoriality and group-strategyproofness variants. **Lean:** neutral; a characterization result.
- William S. Zwicker, "Introduction to the Theory of Voting," in *Handbook of Computational Social Choice* (Cambridge University Press, 2016), §2.4 — Definitions 2.7–2.8, Theorem 2.3 and the framing used here, including the "no satisfactory full-domain extension of May" observation and the treatment of Condorcet consistency as a plausible-but-not-mandatory axiom. **Lean:** neutral; the standard academic reference.
- K. O. May, "A Set of Independent Necessary and Sufficient Conditions for Simple Majority Decision," *Econometrica* 20(4), 1952. **Lean:** neutral.

## Related

- [May's theorem](../mays_theorem.md) — the two-candidate original · [Gibbard–Satterthwaite](../gibbard_satterthwaite_theorem.md) — the full-domain impossibility · [Ties Are Forced](../ties/ties_are_forced.md) — the same price, one level down
- [The Condorcet hub](README.md) · [three-candidate collapse](three_candidate_collapse.md) · [the Smith set](../smith_set.md) · [cycle resolution](../../../05_Ranked_Robin/concepts/cycle_resolution.md)
- [Ranked Robin](../../../05_Ranked_Robin/concepts/ranked_robin.md) · [criteria at a glance](../criteria_at_a_glance.md) · [social welfare function](../social_welfare_function.md)
- [Glossary](../../GLOSSARY.md) — Condorcet domain, Condorcet extension, strategyproofness, resolute
