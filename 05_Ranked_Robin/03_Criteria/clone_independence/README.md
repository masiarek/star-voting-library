# Clone independence — can running copies of yourself help you win?

Ranked Robin's headline defense: adding near-identical candidates ("clones") shouldn't change who wins. These cases probe it — first the LH-only pair that shows the clones reshaping the finalist set, then the BV-backed pair (BV2142/BV2143) that pinned the same election on a live BetterVoting count. Both engines elect **C** after the cloning; the interesting part is that the clones still changed the outcome, just not in their own faction's favour.

## The cases

| Case | Page | YAML |
|---|---|---|
| Before cloning: A, B, C tie in a cycle (LH-only) | [page](cases/cases_pages/clone_teaming_01_pre.md) | [`clone_teaming_01_pre.yaml`](cases/clone_teaming_01_pre.yaml) |
| Teaming: A runs clones, and the win goes to C (LH-only) | [page](cases/cases_pages/clone_teaming_02_post.md) | [`clone_teaming_02_post.yaml`](cases/clone_teaming_02_post.yaml) |
| BV2142 — clone independence (1/2): a no-Condorcet cycle, where LH and BV part ways | [lesson](bv2142_4gfwdq_clone_cycle_pre.md) · [page](cases/cases_pages/bv2142_4gfwdq_clone_cycle_pre.md) | [`bv2142_4gfwdq_clone_cycle_pre.yaml`](cases/bv2142_4gfwdq_clone_cycle_pre.yaml) |
| BV2143 — clone independence (2/2): the clones change the outcome, and hand it to C | [lesson](bv2143_9pr3wr_teaming_fails.md) · [page](cases/cases_pages/bv2143_9pr3wr_teaming_fails.md) | [`bv2143_9pr3wr_teaming_fails.yaml`](cases/bv2143_9pr3wr_teaming_fails.yaml) |

Frozen BV exports sit next to their yamls; full audit mirrors in `clone_independence_tabulated/`. These pages read as an LH-vs-BetterVoting divergence until 2026-08-19, when the engine's tiebreak ladder was corrected: Ranked Robin resolves a two-way tie on the finalists' own head-to-head (its 1st Degree) before it looks at margins over the field (its 2nd Degree), and the engine had only the second. See [degrees of ties](../rr_tiebreaks/degrees_of_ties.md) and [RR tiebreak, LH vs BV](../../01_Learn/rr_tiebreak_lh_vs_bv.md).
