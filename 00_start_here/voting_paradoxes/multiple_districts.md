# The Reinforcement paradox — winning everywhere, losing overall

*The **Reinforcement postulate**: if two disjoint electorates each elect X, their union must elect X. The **Reinforcement paradox** (a.k.a. the **multiple-districts** or **inconsistency** paradox) is the failure: a candidate wins every district separately, yet loses when the districts are counted together.* (A **conditional** paradox in Felsenthal's taxonomy: the one changed datum is the partition — amalgamate the districts, hold every ballot constant, and the winner changes.)

→ Glossary: [`reinforcement`](../GLOSSARY.md) · Felsenthal's taxonomy: [README](README.md) · related counting property: [the summability demo](../../method_comparisons/summability_demo/README.md)

## The live demonstration (a trio of elections)

Felsenthal's Example 3, run for real: [BV2147 — District I](../../method_comparisons/felsenthal_paradoxes/bv2147_9gdrqg_felsenthal_ex3_district1.md) (17 voters, runoff → **Bruno**), [BV2148 — District II](../../method_comparisons/felsenthal_paradoxes/bv2148_h87k6v_felsenthal_ex3_district2.md) (15 voters, **Bruno** wins round one with 8 of 15 — a majority favorite *and* the district's Condorcet winner), then [BV2149 — Combined](../../method_comparisons/felsenthal_paradoxes/bv2149_byk9v2_felsenthal_ex3_reinforcement.md) (the same 32 voters as one electorate → **Alma**). Two districts say Bruno; their union says Alma.

## Where it comes from

Like [non-monotonicity](non_monotonicity.md), this is a disease of **elimination order**. Plurality-with-runoff (and RCV-IRV generally) decides everything by *who gets deleted*: District I deletes Alma; the combined count deletes Cora; and the deletion determines the final pair. Amalgamating electorates reshuffles the first-choice tallies that drive deletion, so two agreeing districts can produce a disagreeing union. No appeal to a "truer" winner is needed — the procedure contradicts its own two verdicts. (In this construction the combined electorate is a Condorcet cycle, so the inconsistency really is the whole story.)

Methods that sum a single number per candidate from each ballot — Score, Approval, Borda — satisfy reinforcement outright: sums over a union are sums of sums. STAR's runoff stage costs it the formal guarantee, but in this trio STAR elects Bruno in District I, District II, *and* combined (102/98/88 in the union; runoff 18–14). The STAR-side failure is real all the same: [the *Two districts, one mayor* exercise](../../01_STAR/exercises/ex01_two_districts.md) constructs it and runs it live as a second trio — [West](https://bettervoting.com/d3b9wc/results) / [East](https://bettervoting.com/rhbfj7/results) / [Combined](https://bettervoting.com/923q3d/results) (BV2188–90): Avery wins both districts, Carmen wins their union. RCV-IRV also fails the related **summability** property — district subtotals can't even be *added* meaningfully, which is the operational face of the same problem: see [the summability demo](../../method_comparisons/summability_demo/README.md).

## Why it matters

Real elections are counted in precincts, districts, and states, and results are audited by comparing parts to wholes. A method where "won every district" and "won the election" can point at different candidates makes district-level results uninterpretable as evidence — and hands every close loss a ready-made grievance. It takes 32 voters and three BetterVoting elections to show the whole thing end to end.
