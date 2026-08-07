# RCV-IRV — the ranked-ballot tabulation (for comparison)

STAR uses **score** ballots (rate each candidate 0–5). The other family taught in this repo uses **ranked** ballots, counted by **instant-runoff (IRV)** — what the US usually calls "RCV." It's a genuinely different count: eliminate the candidate with the fewest first choices, transfer those ballots to their next choice, and repeat until one candidate has a majority of the still-active ballots.

Because the count is different, so are its failure modes — center squeeze, exhausted ballots, non-monotonicity — none of which are STAR's. In this repo, ranked ballots are tabulated by a **separate** engine; STAR / score files never touch it, and vice versa.

This folder is the RCV-IRV slot in the tabulation-engines hub, next to [the BetterVoting reader](../BV/README.md) (BetterVoting's display) and [reading a STAR report](../LH_starvote/reading_a_star_report.md) (the LH STAR report). The substantive RCV-IRV explainers live with the other concept pages:

- [RCV is a confusing name](../../../06_Other/RCV_IRV/concepts/RCV-IRV-confusing-name.md)
- [Is IRV "just plurality"?](../../../06_Other/RCV_IRV/concepts/RCV_IRV_and_plurality.md)
- [Center squeeze](../../../06_Other/RCV_IRV/concepts/RCV_IRV_center_squeeze.md)
- [IRV non-monotonicity](../../../06_Other/RCV_IRV/concepts/RCV_IRV_non_monotonicity.md)
- [Exhausted ballots](../../../06_Other/RCV_IRV/concepts/RCV_IRV_exhausted_ballots.md)
- [IRV isn't summable](../../../06_Other/RCV_IRV/concepts/RCV_IRV_lack_of_summability.md)

Side-by-side with STAR: [STAR vs RCV-IRV, step by step](../../topics/tabulation_star_vs_irv.md) · [RCV-IRV vs. STAR](../../topics/rcv_irv_vs_star.md).

**Before you trust a close count from this engine**, read its [known limitation on elimination ties](../../../06_Other/RCV_IRV/RCV_IRV_tabulation_engine/README.md#known-limitation-elimination-ties). The vendored pyrankvote breaks a tie for last on later ranks — second choices, then thirds — which is a real ballot-based ladder. But when that ladder runs out (every candidate tied at every rank), the winner falls out of the **order the ballot rows are written in**, and the report does not say so. Rare in practice, and worth knowing exists: [Batch elimination — what happens when the batch is *everyone*](../../topics/ties/batch_elimination.md).
