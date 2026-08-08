# 06_Other/Majority_Judgment — Balinski & Laraki's median rule

Majority Judgment: every voter grades every candidate in a **common language of words** — *To Reject, Poor, Acceptable, Good, Very Good, Excellent* — and the candidate with the highest **median** grade wins. Not the total, not the average: the middle grade.

**New to Majority Judgment?** The concept pages for this method live in [`concepts/`](concepts/README.md) — start with [Majority Judgment](concepts/majority_judgment.md) (the ballot, the count, the tie-break, and what the method deliberately gives up). Everything below is the **runnable examples**.

| Case | Read · run |
|---|---|
| Majority Judgment 101 — the highest median grade wins | [`mj_101_c3_b5.yaml`](cases/mj_101_c3_b5.yaml) |
| MJ vs Score — the same ballots, two different winners ([worked here](concepts/majority_judgment.md#how-it-differs-from-score-the-same-ballots-two-winners)) | [`mj_vs_score_c3_b5.yaml`](cases/mj_vs_score_c3_b5.yaml) |

Felsenthal's four §A9 examples — the case *against* the method — live with the rest of that appendix in [Felsenthal's paradox review, worked](../../method_comparisons/felsenthal_paradoxes/README.md), and are worked on [Majority Judgment's paradoxes](../../07_Concepts/voting_paradoxes/majority_judgment.md).

**Why there are no `_tabulated` mirrors or generated pages here.** MJ's ballot holds *words*, which fit neither the LH engine's numeric 0–5 validation nor BetterVoting, and the Balinski–Laraki tie-break exists in neither — so these are **grade-ballot files** carrying a `grades:` block instead of `ballots:`, and the pipeline that mirrors and pages an election YAML never sees them. They are counted by [`grade_methods_report.py`](../../STARVote_LH_tabulation_engine/tools_adam/pref_voting_tabulation_engine/README.md), which computes the median and the tie-break from scratch and cross-checks both against `pref_voting` on every run. The count lives on the concept page.

The ballots themselves *are* drawn — [`build_style_ballot_images.py`](../../STARVote_LH_tabulation_engine/tools_adam/scripts/build_style_ballot_images.py) renders the grade ballot as a third piece of paper alongside the 0–5 STAR grid and the Approval double bubble.

Related: [Grading as a rival primitive](../../07_Concepts/scores_and_ranks/grading_as_a_rival_primitive.md) — the 301 page on *why* Balinski and Laraki think the preference order is the wrong primitive · [Range / Score](../Range/README.md) — the same grade ballot counted by the mean instead.
