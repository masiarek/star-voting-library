# Voting 401 — failure modes & the safety check

*Audience: anyone about to **choose or adopt** a method — officials, reformers, committee chairs, and the seriously curious. You've learned how the methods work (101), read their results and properties (201/301); this is the responsible last step before you'd stake an election on one: **walk its failure modes with clear eyes.** There is no perfect method, so the skill isn't finding a flawless one — it's knowing exactly which whoops you're signing up for, and how often they actually bite.*

**Prereq:** [101](CURRICULUM_101.md) + [201](CURRICULUM_201.md) + [301](CURRICULUM_301.md). · Up: [Curriculum hub](../CURRICULUM.md).

> **The one idea:** *every* voting method fails *some* reasonable criterion — that's a theorem, not an opinion. 401 is the safety check: for the method you like, find out **how** it fails, whether the failure is real-world or lab-grade, and whether you can live with it.

---

## 401.1 — Why there's no perfect method (the frame)

- **Objective:** internalize that a flawless method is mathematically impossible, so "method X has a flaw" is the beginning of the analysis, not the end.
- **Key terms:** Arrow's impossibility theorem (ordinal methods), Gibbard–Satterthwaite (all methods are manipulable), VSE / Bayesian regret.
- **Material:** [Arrow's theorem & STAR](../topics/arrow_theorem_and_star.md) (why cardinal ballots escape Arrow but **not** Gibbard) and [Gibbard–Satterthwaite](../topics/gibbard_satterthwaite_theorem.md).
- **The point:** the honest question is never "which method is flawless?" (none is) but **"which failures can I tolerate, and how often do they occur?"** Everything below serves that question.

## 401.2 — The tool: reading a claimed failure honestly

- **Objective:** be able to weigh any "method X fails!" claim — including the ones aimed at the method you favor.
- **Key terms:** the four-part test — *structural / sincere / realistic / really-happened*.
- **Material:** [Reading these fairly — the test for an honest "whoops"](../../method_comparisons/paradoxes_and_whoops/reading_these_fairly.md) and [criteria at a glance](../topics/criteria_at_a_glance.md).
- **The point:** a failure that is structural, triggered by *sincere* votes, on a realistic electorate — and that has actually happened — is a serious mark against a method. A contrived, strategic, knife-edge construction never seen in the wild is the weakest, muddiest angle (and applies to *every* method via Gibbard). Grade every whoops on that scale.

## 401.3 — The safety datasheets (each method's honest limits)

- **Objective:** read the conceded failure list for each method straight from its own honest-limits page — the fair 401, method by method.
- **Material:**
  - **STAR** → [STAR's honest limits](../STAR_Voting/properties_and_limits/STAR_honest_limits.md) (the *why*) and [every criterion STAR fails](../STAR_Voting/properties_and_limits/star_criteria_failures.md) (the *index, with a runnable example + BV id for each*): not Condorcet-compliant; trades Later-No-Harm; rare majority / participation / mono-raise-delete / IIA / consistency failures.
  - **Ranked Robin / Condorcet** → [RR's honest limits](../RCV_Ranked_Robin/RCV_RR_honest_limits.md) (cycles; blind to intensity — the sincere dark horse).
  - **RCV-IRV** → [non-monotonicity](../RCV_IRV/RCV_IRV_non_monotonicity.md), [center squeeze](../RCV_IRV/RCV_IRV_center_squeeze.md), [exhausted ballots](../RCV_IRV/RCV_IRV_exhausted_ballots.md).
  - **Approval / Score** → [the chicken/Burr dilemma](../../method_comparisons/chicken_dilemma/) and the "where do you draw the line?" threshold question ([are equal-score votes discounted?](../STAR_Voting/reference/are_equal_score_votes_discounted.md)).
  - **Plurality / Choose-One** → the [spoiler effect](../topics/spoiler_effect.md) and [wasted votes](../topics/wasted_votes.md) — the failures the whole reform movement exists to fix.
- **The point:** a method that lists its own limits out loud is more trustworthy, not less. Candor is the credibility (it's [301](CURRICULUM_301.md)'s rule, carried to the capstone).

## 401.4 — The failures that actually happened

- **Objective:** separate real-world failures from lab constructions — the top of the four-part test.
- **Material:** [Burlington 2009](../../method_comparisons/burlington_2009/) (center squeeze + non-monotonicity on certified ballots → IRV repealed), [Alaska 2022](../../method_comparisons/alaska_2022/) (Condorcet failure, spoiler, upward monotonicity, exhaustion — one real race), and [San Francisco D7 2020](../../method_comparisons/monotonicity/downward_monotonicity_sf.md) (downward monotonicity).
- **The point:** these are IRV's, and they're *structural and sincere* — which is why they carry weight that a contrived STAR gotcha doesn't. Keep the [rarity](../../method_comparisons/alaska_2022/alaska_301.md) in view too (2 Condorcet failures in 182 US RCV elections): real, predictable, but not constant.

## 401.5 — The criterion-failure gallery (runnable)

- **Objective:** see each named criterion fail on a real, re-runnable election — the concrete counterpart to 401.1's theorems.
- **Material:** [monotonicity](../../method_comparisons/monotonicity/) (raise the winner → they lose), [reversal symmetry](../../method_comparisons/reversal_symmetry/) (best = worst), [the Dark Horse](../../method_comparisons/dark_horse_borda/) (Borda elects a nobody), [the chicken dilemma](../../method_comparisons/chicken_dilemma/), and [favorite betrayal](../../method_comparisons/favorite_betrayal_irv/).
- **The mean twin:** the [**Mudroom**](../../method_comparisons/mudroom/) collects these as deliberately *unfair*, one-sided per-method hit-reels — fun, clearly labeled, and **not for citing.** Use it to appreciate that *no method is spared*; use the fair pages above for the actual analysis.
- **The point:** the impossibility theorems say failures must exist; these make them tangible — and, seen across every method, prove the failures are universal, not a mark of one "bad" method.

## 401.6 — Reading the advocacy (claim-checking)

- **Objective:** apply the safety check to the *literature*, not just the methods — every camp's white paper leans, and each is worth checking with the ballots in hand.
- **Material:** the worked claim-checks — [FairVote's official position on STAR](../../method_comparisons/fairvote_star_whitepaper/) (pro-RCV), the [FairVote Condorcet article](../topics/condorcet/fairvote_condorcet_claim_check.md), and the [rangevoting.org "IRV logic" critique](../RCV_IRV/RCV_IRV_non_monotonicity.md#a-sharper-critique-and-where-it-overreaches-reading-advocacy-critically) (pro-Range). Each concedes the valid core, runs the testable claims, flags the overreach, discloses the lean — and lets the fairness cut against STAR too.
- **The point:** the same discipline that grades a *method's* failure grades an *argument's*: concede the kernel, test it, name the overclaim, disclose who's talking.

## 401.7 — The synthesis: choosing responsibly

- **Objective:** turn the failure inventory into an actual decision.
- **Material:** [what makes a good winner?](../topics/what_makes_a_good_winner.md), [what makes a voting *method* good?](../topics/what_makes_a_voting_method_good.md), and the VSE foundations in [301](CURRICULUM_301.md).
- **The point:** weigh the failure modes by **severity × frequency**, not by count. A method with a *rare, lab-only* seam beats one with a *common, sincere, real-world* one — even if a checklist shows each "failing" something. STAR and Ranked Robin trade a few contrived, seldom-seen failures for the elimination-order disasters IRV suffers sincerely; all three tower over Choose-One. That comparison — made honestly, with the whoops on the table — is the whole point of the library, and the reason to run the safety check *before* you adopt, not after.

---

*Up: [Curriculum hub](../CURRICULUM.md) · Prev: [Voting 301](CURRICULUM_301.md). The unfair, for-sport companion to this page is the [Mudroom](../../method_comparisons/mudroom/) — same failure modes, no bedside manner.*
