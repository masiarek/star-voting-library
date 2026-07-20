# 03_STAR_PR / _main — proportional STAR worked examples

The proportional STAR (STAR-PR) cases: the same 0–5 score ballot, counted so seats reflect the electorate's *proportions* rather than handing every seat to the largest bloc. Read the reader-friendly **pages** (`_main_pages/`); the `.yaml` beside each is the tabulatable source, and the always-full audit copy is in `_main_tabulated/`.

Concept first: [STAR-PR — the three methods](../../00_start_here/proportional_representation/STAR_PR/README.md) · [the math behind proportional STAR](../../00_start_here/proportional_representation/STAR_PR/the_math_behind_proportional_star.md) · [STV vs STAR-PR](../../00_start_here/proportional_representation/stv/proportional_stv_vs_star.md). Parent folder: [`03_STAR_PR`](../README.md).

## Same election, three methods (the 63-ballot trio)

The `02a/02b/02c` files count the **same** 5-candidate, 63-ballot election three ways — the cleanest way to see how the reweighting rule changes what's counted (they tend to agree on a clean two-coalition electorate).

- [Allocated Score](cases/cases_pages/02a_c5_b63_proportional-allocated-score.md) — seat the top scorer, then fully spend a quota of their strongest supporters (Equal Vote's recommended STAR-PR) · [`.yaml`](cases/02a_c5_b63_proportional-allocated-score.yaml)
- [Sequentially Spent Score (SSS)](cases/cases_pages/02b_c5_b63_proportional-sss.md) — supporters spend score proportionally toward the quota · [`.yaml`](cases/02b_c5_b63_proportional-sss.yaml)
- [Reweighted Range Voting (RRV)](cases/cases_pages/02c_c5_b63_proportional-rrv.md) — divide each ballot's weight by a growing divisor · [`.yaml`](cases/02c_c5_b63_proportional-rrv.yaml)

## Proportional vs STV, on one shared electorate

- [Same 3-seat electorate as the STV demo](cases/cases_pages/03b_star_pr_3seats.md) — the STAR-PR counterpart to the STV file; STV and all three STAR-PR methods land on the same proportional slate · [`.yaml`](cases/03b_star_pr_3seats.yaml)

## Academic cross-checks (Lackner & Skowron)

- [Shadow STAR-PR — Allocated Score, k=4](cases/cases_pages/lackner_skowron_shadow_star_pr_c7_b12.md) — Lackner & Skowron's running example · [`.yaml`](cases/lackner_skowron_shadow_star_pr_c7_b12.yaml)
- [Shadow STAR-PR — RRV, k=4 (matches PAV)](cases/cases_pages/lackner_skowron_shadow_star_pr_rrv_c7_b12.md) — the same example under RRV, which matches Proportional Approval Voting · [`.yaml`](cases/lackner_skowron_shadow_star_pr_rrv_c7_b12.yaml)
- [RRV sample — three parties (Purple/Orange/Yellow)](cases/cases_pages/rrv_sample_c15_b13_three-parties.md) — 15 candidates, three party blocs · [`.yaml`](cases/rrv_sample_c15_b13_three-parties.yaml)

## Real BetterVoting election

- [BV2130 — Presidential Board (Allocated Score, 7 seats)](cases/cases_pages/bv2130_presidential_board_star_pr.md) — a real BetterVoting STAR-PR election (`bvhchj`), 51 candidates, 102 ballots, cross-checked against the LH engine · [`.yaml`](cases/bv2130_presidential_board_star_pr.yaml) · [results ↗](https://bettervoting.com/bvhchj/results)

# file: README.md
