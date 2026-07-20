# Clone independence — can running copies of yourself help you win?

Ranked Robin's headline defense: adding near-identical candidates ("clones") shouldn't change who wins. These cases probe it — first the LH-only pair that shows teaming *on paper*, then the BV-backed pair (BV2142/BV2143) where LH and BetterVoting resolve the resulting Condorcet cycle differently.

## The cases

| Case | Page | YAML |
|---|---|---|
| Before cloning: A, B, C tie in a cycle (LH-only) | [page](cases/cases_pages/clone_teaming_01_pre.md) | [`clone_teaming_01_pre.yaml`](cases/clone_teaming_01_pre.yaml) |
| Teaming: A runs clones, coin flip → win (LH-only) | [page](cases/cases_pages/clone_teaming_02_post.md) | [`clone_teaming_02_post.yaml`](cases/clone_teaming_02_post.yaml) |
| BV2142 — clone independence (1/2): a no-Condorcet cycle, where LH and BV part ways | [lesson](bv2142_4gfwdq_clone_cycle_pre.md) · [page](cases/cases_pages/bv2142_4gfwdq_clone_cycle_pre.md) | [`bv2142_4gfwdq_clone_cycle_pre.yaml`](cases/bv2142_4gfwdq_clone_cycle_pre.yaml) |
| BV2143 — clone independence (2/2): teaming succeeds on LH, fails on BetterVoting | [lesson](bv2143_9pr3wr_teaming_fails.md) · [page](cases/cases_pages/bv2143_9pr3wr_teaming_fails.md) | [`bv2143_9pr3wr_teaming_fails.yaml`](cases/bv2143_9pr3wr_teaming_fails.yaml) |

Frozen BV exports sit next to their yamls; full audit mirrors in `clone_independence_tabulated/`. Why the divergence is possible at all: LH breaks Copeland ties by margin → lot (deterministic), BV by head-to-head → random — see [RR tiebreak, LH vs BV](../../00_start_here/RCV_Ranked_Robin/rr_tiebreak_lh_vs_bv.md).
