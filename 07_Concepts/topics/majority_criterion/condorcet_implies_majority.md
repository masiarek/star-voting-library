# Condorcet implies majority — why STAR's two famous failures are one failure

*Two criteria get listed side by side on every comparison chart, as though a method could fail them independently: the **majority criterion** and the **Condorcet criterion**. They are not independent. One implies the other, which means **failing the first guarantees failing the second** — so STAR's two most-quoted criterion failures are a single failure counted twice. This page proves it in one line, shows it on five ballots, and marks the one precondition that does all the work.*

**Level: 301 · for debaters** → Companions: [the majority criterion hub](README.md) · [majority & minority candidates](majority_and_minority_candidates.md) · [the Condorcet hub](../condorcet/README.md) · [criteria at a glance](../criteria_at_a_glance.md) (the chart this page is a warning about) · [STAR's honest limits](../../../01_STAR/01_Learn/properties_and_limits/STAR_honest_limits.md). Curriculum: [301](../../CURRICULUM.md).

---

## The implication

> **Condorcet criterion ⟹ majority criterion.** Any method that always elects the beats-all winner also always elects a majority's favorite.

**The proof is one sentence.** Suppose more than half of voters rank X first. Then for *every* other candidate Y, that same majority ranks X above Y — so X beats Y head-to-head. X therefore beats everyone, X is the [Condorcet winner](../../GLOSSARY.md#properties-criteria), and a Condorcet-consistent method elects X. ∎

This is [Wikipedia's own formulation](../condorcet/condorcet_criterion_claim_check.md) and it is correct as stated. It is also the single most useful sentence on that page, for reasons the article doesn't draw out.

## The converse is false — and that's where people invert it

Satisfying the majority criterion does **not** make a method Condorcet-consistent. Two methods prove it:

| Method | Majority criterion | Condorcet criterion |
|---|:--:|:--:|
| **[Choose-One / Plurality](../plurality.md)** | ✅ | ❌ |
| **[RCV-IRV](../../../06_Other/RCV_IRV/concepts/RCV-IRV-Hare.md)** | ✅ | ❌ |
| **[Ranked Robin](../../../05_Ranked_Robin/01_Learn/ranked_robin.md), Ranked Pairs, Schulze** | ✅ | ✅ |
| **[STAR](../../../01_STAR/01_Learn/STAR_start_here.md)** | ❌ | ❌ |

IRV satisfies the majority criterion trivially — a candidate with over half the first choices wins in round one, before any elimination happens. And it fails Condorcet spectacularly, which is the whole of [center squeeze](../../../06_Other/RCV_IRV/concepts/RCV_IRV_center_squeeze.md) and of [Alaska 2022](../../../06_Other/RCV_IRV/concepts/case_studies/RCV_IRV_alaska_2022.md).

So **"satisfies the majority criterion" is a weak badge** — the weakest ranked methods in common use carry it. When a comparison chart gives it a green check, that check is doing far less work than its neighbours.

## The contrapositive is the payload

Flip the implication and you get the version that matters in an argument:

> **A method that fails the majority criterion must also fail the Condorcet criterion.**

STAR fails the majority criterion. **Therefore STAR's Condorcet failure is not a second, independent demerit — it is entailed by the first.** There was never a world in which STAR failed one and passed the other.

Two consequences, pointing in opposite directions, which is why the fact is worth holding:

- **Don't defend them separately.** They are one design decision — STAR picks its finalists by *score total* rather than by beating everyone — with two names in the criteria literature. A defence that answers the majority-criterion charge has already answered the Condorcet one.
- **Don't let an opponent bill them as two.** A chart showing STAR with two red X's beside a Condorcet method's two green checks is showing you one difference twice. That is not dishonest — the criteria really are both defined, and both really do fail — but the *rhetorical* weight of "fails two criteria" overstates the underlying disagreement.

## Watch it happen on five ballots

[**BV95b**](../../../01_STAR/03_Criteria/majority_criterion/bv95b_7pdq3r_favorite_loses_two_rivals.md) is the smallest election that shows both failures at once. Three of five voters make **Ada** their unique favorite — a strict majority — and Ada also beats both rivals head-to-head:

<!-- report:bv95b_7pdq3r_favorite_loses_two_rivals -->
```text
[Divergence from STAR]
  STAR                   = Bruno
  Choose-One (Plurality) = Ada   (differs from STAR)
  RCV-IRV                = Ada   (differs from STAR)
  RCV-RR (Condorcet)     = Ada   (differs from STAR)
  Note: 2 of 5 ballots (40%) had equal non-zero scores, so their ranks were
        decided by candidate priority order. The RCV-IRV result may be an
        artifact of score-to-rank tie-breaking rather than a deep
        difference.
  Note: Ranked Robin (RCV-RR) sides with RCV-IRV, so STAR is the outlier
        here — STAR need not elect the Condorcet candidate.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: cases_tabulated/bv95b_7pdq3r_favorite_loses_two_rivals_RCV-IRV_tabulated.txt
  RCV-RR round-robin: cases_tabulated/bv95b_7pdq3r_favorite_loses_two_rivals_RCV-RR_tabulated.txt

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 5 ballots.
Count × Ada,Bruno,Cleo
    3 ×   5,    4,   3
    2 ×   0,    5,   5

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Bruno         -- 22 -- First place
   Cleo          -- 19 -- Second place
   Ada           -- 15
 Bruno and Cleo advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Bruno         -- 3 -- First place
   Cleo          -- 0
   Equal Support -- 2
 Bruno wins.
   Runoff math:
     5  ballots cast
   − 2  Equal Support (no preference between the two finalists)
     ─
     3  voters with a preference  (majority = 2)
           Bruno 3 (100%)  ·  Cleo 0 (0%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Bruno
```
<!-- /report -->

Read the two failures off the same five rows. **Majority:** Ada is scored strictly highest by 3 of 5 voters and does not win. **Condorcet:** Ada beats Bruno 3–2 and Cleo 3–2, and does not win. Same ballots, same losing candidate, same cause — Ada's 15 points are beaten by Bruno's 22 in the scoring round, so Ada never reaches the runoff she would have won. **One mechanism, two criterion names.**

## The precondition that does all the work

The proof needs "ranked first by a majority" to mean **strictly above every other candidate**. On a ranked ballot that is automatic. On a **score ballot it is not** — a voter may give 5 to two candidates at once, and then that voter's "first choice" is shared and contributes no pairwise preference between them.

This is not a technicality. It is the difference between the two cases in this folder:

| | Majority's top rating | Strict majority favorite? | STAR elects the Condorcet winner? |
|---|---|:--:|:--:|
| [**BV95b**](../../../01_STAR/03_Criteria/majority_criterion/bv95b_7pdq3r_favorite_loses_two_rivals.md) | 3 of 5 rate Ada 5, everyone else lower | **Yes** — Ada | ❌ **No** — Condorcet winner Ada, STAR elects Bruno |
| [**51/49**](../../../01_STAR/03_Criteria/majority_criterion/cases/cases_pages/majority_vs_consensus_51_49.md) | 51 of 100 rate Alma 5 — but **3 of them also rate Celia 5** | **No** — only 48 rank Alma strictly first | ✅ **Yes** — Condorcet winner Celia, STAR elects Celia |

In the 51/49 election the "majority" is a majority only in the *shared-top-rating* sense. Strip out the three voters who rate Alma and Celia equally and just 48 of 100 strictly prefer Alma — not a majority at all. So the **strict** majority criterion is never violated there, the implication is never triggered, and STAR duly elects the Condorcet winner. The engine confirms it: `Condorcet Winner: Celia — matches the STAR winner`.

**That contrast is the whole argument over the [Relaxed Majority Criterion](https://www.equal.vote/rmc)**, compressed into two elections. Equal Vote's position is that the strict criterion over-weights a bare 50.1% of first choices while ignoring how the other half feels; the counter-position is that a majority's favorite should win, full stop. What the pair shows is that the two sides are partly arguing about *which reading of "first choice" a rated ballot licenses* — a definitional question — and only partly about values. Both halves are real; keep them apart.

## What this does not show

Keep the claim inside its bounds:

- **It is not an argument that STAR is fine.** BV95b is a genuine double failure and Ada genuinely should have a strong claim on that seat. "It's only one failure" changes the *count*, not the *severity*.
- **It says nothing about frequency.** The implication is a logical fact about criteria, not a statement about how often either failure occurs. On that, see [Condorcet efficiency measured](../condorcet/condorcet_efficiency_measured.md) — STAR runs 74–99% depending on the electorate model.
- **It does not collapse every criterion pair.** Most criteria on a comparison chart genuinely are independent. This one implication is worth knowing precisely *because* it is the exception that a chart's grid layout hides.
- **It runs the other way too.** Any method advertising Condorcet-consistency gets the majority criterion for free and should not be credited twice for it either. The rule is symmetric; apply it to Ranked Robin's column as readily as to STAR's.

## The short version

- **Condorcet ⟹ majority.** One line: a majority's strict favorite beats everyone pairwise.
- **The converse fails** — Plurality and IRV both satisfy the majority criterion. It's a weak badge.
- **Contrapositive:** fail majority ⟹ fail Condorcet. STAR's two headline criterion failures are one.
- **Precondition:** "first choice" must be *strict*. On a score ballot it can be shared, which is why the 51/49 election fails the loose majority criterion and satisfies both the strict one and Condorcet.
- **Symmetric discipline:** don't double-count STAR's failure, and don't double-count Ranked Robin's pass.

---

## See also

- [The majority criterion](README.md) — the hub: what it says, why STAR fails it, the Relaxed Majority Criterion, and the two-tiny-elections demo
- [Majority & minority candidates](majority_and_minority_candidates.md) — what "a majority candidate" even means when almost nobody wins an arithmetic majority
- [Criteria at a glance](../criteria_at_a_glance.md) — the comparison grid, and the other trap in reading one (only Pareto is an Arrow condition)
- [Wikipedia's "Condorcet winner criterion," claim-checked](../condorcet/condorcet_criterion_claim_check.md) — where this implication is stated, alongside three other claims and one bad citation
- [STAR's honest limits](../../../01_STAR/01_Learn/properties_and_limits/STAR_honest_limits.md) · [three notions of "winner"](../../../01_STAR/01_Learn/properties_and_limits/STAR_three_winner_notions.md)

# file: condorcet_implies_majority.md
