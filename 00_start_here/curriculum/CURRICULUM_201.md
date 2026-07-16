# Voting 201 — reading results, comparisons, multi-winner intro

*Audience: engaged learners, officials, the curious. Now we name things precisely, read a full result report, and compare methods honestly.*

**Prereq:** [Voting 101](CURRICULUM_101.md). · Up: [Curriculum hub](../CURRICULUM.md) · Next: [Voting 301](CURRICULUM_301.md).

---

## 201.1 — Reading the results (transparency)

- **Key terms:** preference matrix, For / Equal Support / Against, Condorcet winner, summability, score distribution.
- **See it:** the [display-options example](../../01_STAR/_main/_main_pages/04b_c4_b3_display-options-all.md) with the matrix and Condorcet blocks turned on. The auditable, precinct-summable heart of the count is the **pairwise matrix**.
- **Two reports, one count:** the same election appears both as BetterVoting's visual display and the LH engine's text report — why there are two, how they map, and the convert→validate→test pipeline: [BetterVoting and the LH Engine — One Election, Two Reports](../tabulation_engines/bettervoting_and_the_engine.md).
- **The full audit report:** the generated `_tabulated.txt` siblings carry the complete engine report (preference matrix + score distribution + the rounds). 101.4 showed the *minimal* on-screen view; reading the **full** report of those same elections (e.g. the `_tabulated` mirrors under [Runoff Reversal](../../01_STAR/runoff_overturns_leader/)) is the 201 skill — and *why* the on-screen report is minimal by default (don't overwhelm a beginner).
- **Worked walkthrough:** [How to Read a STAR Result Report](../tabulation_engines/LH_starvote/reading_a_star_report.md) — a full LH report annotated section by section, with a "which parts to show at 101 / 201 / 301" table.
- **Reading the runoff percentages:** [Two Denominators, One Winner](../STAR_Voting/the_count/runoff_percentages.md) — the runoff shown two ways (% of *all* voters vs % of those *with a preference*), and why the majority bar is half of the *decided* voters. Enable in the engine with `options: { show_runoff_percent: true }`. Pairs with 301.3 (Equal Support).
- **A real election, end to end:** [What Makes the Best Pet?](../../01_STAR/pet_real_bv_election/) — a real 461-ballot BetterVoting STAR election, the actual export read section by section (scoring → runoff → runoff % → Condorcet), including the real-ballot difference between an abstention (blank) and an explicit-zero ballot.

## 201.2 — Edge cases & trust

- **Key terms:** unanimous ballots, ties / tiebreaker, abstention, equal-max ballot.
- **See it:** [unanimous ballots](../../01_STAR/_main/_main_pages/05a_c5_b3_unanimous-ballots.md); the tie-break cascade in [Flat scores, ties & tie-breaking](../../01_STAR/Flat_scores_ties/) and the [dead-rung](../../01_STAR/tie_break_dead_rung/) set; abstention handling in [abstain_bugs](../../01_STAR/abstain_bugs/).

## 201.3 — Nomenclature: RCV vs IRV vs RCV-IRV

- **Objective:** stop conflating the ranked *ballot* (RCV) with one *count* (IRV).
- **Material:** [terminology basics](../topics/ballot_and_terminology_basics.md) · [why the name is confusing](../RCV_IRV/RCV-IRV-confusing-name.md).
- **The point:** center squeeze / exhausted ballots are **IRV**-specific, not properties of all ranked methods (Ranked Robin isn't squeezed).

## 201.4 — STAR vs RCV-IRV (the honest comparison)

- **Key terms:** exhausted ballots, center squeeze, wasted votes, the method scorecard.
- **See it:** [RCV-IRV vs STAR](../topics/rcv_irv_vs_star.md); any 4-candidate file with `options: { show_irv: true }` prints the `[Divergence from STAR]` block. The cross-method worked sets live in [the method-comparisons sets](../../method_comparisons/README.md).

## 201.5 — Multi-winner intro: Bloc STAR

- **Start plain:** [Electing more than one, simply](../topics/electing_more_than_one.md) — the majoritarian-vs-proportional fork before any machinery ("do you want the N best, or a body that mirrors the electorate?").
- **Objective:** electing several seats with a majoritarian / at-large method.
- **Key terms:** Bloc STAR, seats, at-large.
- **See it:** [Bloc STAR, 2 seats](../../02_STAR_Bloc/_main/_main_pages/01_c4_b2_bloc-star-2-seats.md) (in [`02_STAR_Bloc/`](../../02_STAR_Bloc/)).
- **The point:** a cohesive majority can *sweep* all seats — which is exactly what motivates 301's proportional methods.
- **Gentle committee intro (approval side):** [Electing a committee — making sure people have a voice](../Approval_Voting/Multiwinner_Approval/abc_rules_intro.md) — a counting-only walk through "most approved" vs "cover everyone" vs proportional, on Lackner & Skowron's steering-committee example.

## 201.6 — What are we optimizing for? (good winner, good method)

- **Objective:** before comparing methods, name the competing ideals of a "good winner" and the criteria of a "good method" — and see there is no single ideal.
- **Key terms:** consensus / Condorcet winner, majoritarian vs. utilitarian winner, VSE, strategy-resistance, summability, "a perfect system will never exist."
- **Pages:** [What makes a good winner?](../topics/what_makes_a_good_winner.md) (four ideals; real Condorcet failures — Alaska '22, Burlington '09) and [What makes a voting method good?](../topics/what_makes_a_voting_method_good.md).
- **The "experts reject RCV-IRV" claim, graded:** [Do the experts really think RCV-IRV is "bad"?](../topics/expert_consensus_and_irv.md) — the pro-cardinal talking point (Smith / Brams / Quinn, VSE) taken seriously and checked.
- **Criteria side by side:** [Criteria at a glance](../topics/criteria_at_a_glance.md) — Approval / STAR / Ranked Robin / RCV-IRV pass/fail across every major criterion, each failure linked to a runnable election (with the "a table is a map, not a verdict" caveat up front).
- **The point:** this is the *map*; the deeper theory (VSE math, Arrow / Gibbard–Satterthwaite, simulation models) is **301**.

---

*Up: [Curriculum hub](../CURRICULUM.md) · Prev: [Voting 101](CURRICULUM_101.md) · Next: [Voting 301 — proportional, criteria, debate theory](CURRICULUM_301.md).*
