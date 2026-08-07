# 06_Other/RCV_IRV — ranked-ballot example + the vendored IRV engine

A basic runnable RCV-IRV election and the vendored `pyrankvote`-based engine that counts ranked (`A>C>B`) or score ballots round by round.

**New to RCV-IRV?** The concept pages for this method live in [`concepts/`](concepts/README.md) — start with [Is it RCV or IRV?](concepts/RCV_or_IRV_whats_the_right_word.md) (the terminology that makes the rest read precisely), then [RCV-IRV (Hare)](concepts/RCV-IRV-Hare.md) for the method itself and [center squeeze](concepts/RCV_IRV_center_squeeze.md) for the critique. Everything below is the **runnable example and the engine**. <!-- terminology-ok: bare RCV is inside a linked page title -->

| Case | Page | YAML |
|---|---|---|
| RCV-IRV — a basic ranked-ballot example (3 candidates) | [page](cases/cases_pages/RCV_ballot_example.md) | [`RCV_ballot_example.yaml`](cases/RCV_ballot_example.yaml) |
| Parallel universes — one count, two legal answers (an elimination tie where PUT elects two) | [page](cases/cases_pages/put_two_universes_c3_b4.md) | [`put_two_universes_c3_b4.yaml`](cases/put_two_universes_c3_b4.yaml) |
| Batch elimination empties the field — the perfect cycle (3 voters; Hare *and* Coombs both run out of candidates) | [page](cases/cases_pages/batch_all_out_cycle_c3_b3.md) | [`batch_all_out_cycle_c3_b3.yaml`](cases/batch_all_out_cycle_c3_b3.yaml) |
| …with a Condorcet winner sitting there (one ballot changed; batch IRV still ties three ways, Coombs elects Amy) | [page](cases/cases_pages/batch_all_out_condorcet_c3_b3.md) | [`batch_all_out_condorcet_c3_b3.yaml`](cases/batch_all_out_condorcet_c3_b3.yaml) |
| …and in round *two*, with Pareto keeping the unanimously-last candidate out of the tie | [page](cases/cases_pages/batch_all_out_round2_c4_b6.md) | [`batch_all_out_round2_c4_b6.yaml`](cases/batch_all_out_round2_c4_b6.yaml) |

The three `batch_all_out_*` cases back [Batch elimination — what happens when the batch is *everyone*](../../07_Concepts/topics/ties/batch_elimination.md).

The engine lives in [`RCV_IRV_tabulation_engine/`](RCV_IRV_tabulation_engine/README.md); full audit mirrors are in `RCV_IRV_tabulated/`.
