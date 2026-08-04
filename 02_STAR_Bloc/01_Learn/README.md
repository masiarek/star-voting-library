# Bloc STAR — concept pages

Everything explaining **Bloc STAR** — multi-winner STAR for filling several seats at once with the same 0–5 ballot. It fills N seats by running the whole single-winner count N times: elect a winner, remove them from the field, re-run on the same unchanged ballots. It is the **majoritarian** multi-winner method — it asks "who does the majority most want?" for every seat — and its proportional cousin is [STAR-PR](../../03_STAR_PR/01_Learn/).

New here? Start with **[Bloc STAR](bloc_star.md)** — the ballot, the elect–remove–re-run loop, and how to read the report. Newer than that? Learn [single-winner STAR](../../01_STAR/01_Learn/STAR_start_here.md) first; Bloc STAR is that method, once per seat.

Not sure you want a majoritarian method at all? That's the bigger decision, and it comes first: [Electing more than one, simply](../../07_Concepts/topics/electing_more_than_one.md).

## The method

- [**Bloc STAR**](bloc_star.md) — the count, the removal step, and what it does *not* do (start here)
- [The majority sweep](majority_sweep.md) — a cohesive majority can take *every* seat: why it happens, when that's the right answer, and when it means you wanted proportional
- [Over 50% — what a landslide actually buys](over_50_percent.md) — the sweep's mirror image: a majority that runs *one* candidate wins *one* seat, and the next one goes to a candidate most voters scored 0
- [The score leader can win no seat](score_leader_no_seat.md) — Bloc STAR is not "top N by points"; the runoff decides every seat, so the point leader can be shut out entirely
- [Ties in Bloc STAR](bloc_tiebreaks.md) — the STAR ladder once per seat, plus the wrinkle no top-N method has: a tie at seat 1 can change *who* wins seat 2
- [Bloc STAR among the at-large methods](bloc_star_vs_other_bloc_methods.md) — SNTV, Limited, Block Plurality, Bloc Approval, Bloc Ranked Robin, and why ranked ballots don't buy proportionality
- [Honest limits](bloc_honest_limits.md) — the four limits it adds to STAR's own, and the three properties it keeps

## Worked examples — run them yourself

Every claim on these pages has a runnable election behind it. The full case index, with the BetterVoting id / tie type / issue table, is in [the folder overview](../README.md#the-reference-cases); the ones the concept pages lean on:

- [The baseline](../02_Examples/cases/cases_pages/00_c3_b3_bloc-baseline-2-seats.md) — the smallest Bloc election that decides anything, counted in full
- [BV1835 — the score leader wins no seat](../02_Examples/bv1835_8h3yrx_score_leader_no_seat.md) — 100 voters, 4 seats; the compromise candidate leads every round and takes nothing
- [Exercise 12 — bloc vs. proportional](../../01_STAR/05_Practice/ex12_bloc_vs_proportional.md) — ten ballots, two seats, counted both ways: 60% takes the board, then earns half of it
- [Food-Truck Row](../../method_comparisons/food_truck_row/) — one 100-voter electorate, five counts, three different outcomes
- [Lot A](../02_Examples/cases/cases_pages/bloc_lot_path_dependence_a_c3_b5.md) / [Lot B](../02_Examples/cases/cases_pages/bloc_lot_path_dependence_b_c3_b5.md) — identical ballots, one seat-1 coin toss, two different councils
- [BV130-r2 — the dead-rung lot tie](../02_Examples/bv130r2_dead_rung_bloc.md) — every deterministic rung inert, and BetterVoting still reporting `tieBreakType: none`

## Reference

- Glossary: [Bloc STAR terms](glossary_bloc_star.md)

*(Parallel method hubs: [STAR Voting](../../01_STAR/01_Learn/README.md) · [STAR-PR](../../03_STAR_PR/01_Learn/README.md) · [Approval](../../04_Approval/01_Learn/README.md) · [Ranked Robin](../../05_Ranked_Robin/01_Learn/README.md). Curriculum: [201.5](../../07_Concepts/curriculum/CURRICULUM_201.md). Up: the docs hub [`00_START_HERE`](../../07_Concepts/00_START_HERE.md).)*
