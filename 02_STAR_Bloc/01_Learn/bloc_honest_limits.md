# Bloc STAR — Honest Limits

**One line:** Bloc STAR inherits every limit single-winner [STAR](../../01_STAR/01_Learn/properties_and_limits/STAR_honest_limits.md) has, and adds four of its own: it gives a cohesive majority **every** seat, it can shut the score leader out **entirely**, a tie at one seat can change **who wins a later one**, and the sweep it enables rewards **slate discipline**. Say all of that out loud before recommending it — the sweep in particular is not a corner case, it is the method's design.

→ Companion critical pages, so every method gets the same treatment: [STAR's limits](../../01_STAR/01_Learn/properties_and_limits/STAR_honest_limits.md) · [Approval's limits](../../04_Approval/01_Learn/approval_honest_limits.md) · [Ranked Robin's limits](../../05_Ranked_Robin/01_Learn/RCV_RR_honest_limits.md). The method itself: [Bloc STAR](bloc_star.md).

**Level: 201 → 301 · deep dive**

---

## 1. It is not proportional, and cannot be made so

A cohesive majority can take every seat: 55% of the electorate can hold a council 5–0 while 45% holds nothing. There is no threshold, no correction, and no tuning parameter — nothing in the count ever learns that a group has already been served. Worked in full, with the arithmetic, on [the majority sweep](majority_sweep.md).

Stated as a limit it sounds damning; stated as a design goal it is simply what "majoritarian" means. The failure mode isn't the sweep, it's **using Bloc STAR for a body that was supposed to represent people.** If a 45% minority holding zero seats would read as a broken election, the method was chosen wrong — go to [STAR-PR](../../03_STAR_PR/01_Learn/STAR_PR/) or [STV](../../06_Other/STV/README.md). That decision is made when the rules are written and cannot be repaired by the count.

In one class of jurisdiction that is not merely a design mistake but a legal exposure: where a racial or language minority is concentrated in one sector of a multi-seat district, an at-large majoritarian count is the mechanism §2 of the Voting Rights Act calls vote dilution, and the scored ballot does nothing to change the analysis. The law, the *Gingles* test, and what a scored ballot does and does not fix: [at-large elections and the Voting Rights Act](at_large_and_the_vra.md).

## 2. The score leader can win nothing

Every seat is decided by the runoff, so the candidate who leads *every* scoring round can lose *every* runoff and take no seat at all. [BV1835](../02_Examples/bv1835_8h3yrx_score_leader_no_seat.md) is the worked case: Ava leads by 63 points, reaches all four runoffs, loses all four 51–49, and finishes with nothing while the two rival camps split the seats 2–2.

This is [runoff reversal](../../01_STAR/02_Examples/runoff_overturns_leader/) — STAR's signature step, and defensible on its own terms — but the multi-winner version has a sting the single-winner one doesn't. In a one-seat race a reversal costs you *the* seat, which is the deal. Here it costs you all of them, and a body that wanted its compromise figure in the room has no rung anywhere in the method at which "led every round" earns anything. Full argument, both readings: [the score leader can win no seat](score_leader_no_seat.md).

## 3. A tie propagates forward

Because Bloc STAR is **sequential** — elect, remove, re-run — the field for seat 2 depends on how seat 1 came out. So a tie broken at seat 1 doesn't just decide seat 1: it can change **which candidate wins seat 2**. Two engine-verified runs of five identical ballots, differing only in the published lot order, elect two different councils ([lot A](../02_Examples/cases/cases_pages/bloc_lot_path_dependence_a_c3_b5.md) · [lot B](../02_Examples/cases/cases_pages/bloc_lot_path_dependence_b_c3_b5.md)).

Every top-N at-large method — Bloc Approval, SNTV, Bloc Ranked Robin — confines a tie to the last seat. Bloc STAR is the one that lets it travel. Details and the BetterVoting reporting problem that hides it: [ties, seat by seat](bloc_tiebreaks.md).

## 4. It rewards slate discipline

Follow the incentive the sweep creates. A faction large enough to sweep only sweeps if it stays **cohesive** — so the rational move for an organized side is to publish a slate and ask supporters to score it uniformly high and everything else 0. That works, and it is available to organized groups in a way it is not available to unorganized voters. The cost of *not* doing it is [Over 50% — what a landslide actually buys](over_50_percent.md): three voters unanimous about one candidate elect them to seat 1 and then hand seat 2 to a candidate two of the three scored 0.

Two honest caveats on how far to push this claim:

- **It is milder than the plurality family's version.** Under [SNTV](bloc_star_vs_other_bloc_methods.md) a side that runs one candidate too many can lose *everything* to vote splitting, which is why SNTV jurisdictions develop candidate-rationing machines. Bloc STAR has nothing to split — scoring one candidate never costs another — so the pressure is toward *cohesion*, not toward *rationing*. That is a real improvement, not a wash.
- **Bullet voting has a sharper edge here than in a single-winner race.** Giving a rival a generous score can help them win a *later* seat, and there is no reweighting to soften it. The incentive to compress your scores toward 5s and 0s therefore repeats once per seat. Like every method ([Gibbard](../../07_Concepts/topics/gibbard_satterthwaite_theorem.md)), Bloc STAR can be gamed at the margins; what is specific here is that the margin recurs N times.

## 5. Everything single-winner STAR concedes, N times over

Bloc STAR *is* STAR, so all of [STAR's honest limits](../../01_STAR/01_Learn/properties_and_limits/STAR_honest_limits.md) apply unchanged — not Condorcet-compliant, not favorite-betrayal-proof, Later-No-Harm given up by design, a narrow residual of vote splitting. Nothing about filling several seats repairs any of them, and each one gets a fresh chance to bite at every seat.

One practical limit that is genuinely new: **ballot length**. An at-large race with fifteen candidates asks every voter for fifteen considered 0–5 judgments. That is a real cognitive cost, and it is the strongest argument for smaller districts even when you have decided you want a majoritarian body.

## What it does *not* give up

Parity cuts both ways, so the concessions above should be read against what survives the move to multi-winner intact:

- **No vote splitting.** Running a third candidate cannot cost your side a seat. On [Food-Truck Row](../../method_comparisons/food_truck_row/) that is the difference between a 57-voter majority holding both seats and holding none.
- **It is still summable.** Every quantity the count needs — per-candidate score totals, the full For / Equal Support / Against matrix, the five-star counts — is a fixed-size precinct table that **adds**. Removing a seated candidate doesn't change anyone else's totals, so seat 2 is read off the same summed tables as seat 1. Bloc STAR is precinct-auditable in a way [STV is not](../../06_Other/STV/README.md); compare [STAR's summability](../../01_STAR/01_Learn/properties_and_limits/STAR_summability.md).
- **One ballot for every race.** The same 0–5 ballot serves single-winner, bloc and [proportional](../../03_STAR_PR/01_Learn/) races, so a jurisdiction can change what a body is *for* without retraining its voters.

## See also

- [Bloc STAR](bloc_star.md) · [the majority sweep](majority_sweep.md) · [the score leader can win no seat](score_leader_no_seat.md) · [ties, seat by seat](bloc_tiebreaks.md)
- [Bloc STAR among the at-large methods](bloc_star_vs_other_bloc_methods.md)
- [Every voting criterion STAR fails](../../01_STAR/01_Learn/properties_and_limits/star_criteria_failures.md) — the single-winner checklist, with receipts
