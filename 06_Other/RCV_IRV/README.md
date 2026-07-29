# 06_Other/RCV_IRV — ranked-ballot example + the vendored IRV engine

A basic runnable RCV-IRV election and the vendored `pyrankvote`-based engine that counts ranked (`A>C>B`) or score ballots round by round.

**New to RCV-IRV?** The concept pages for this method live in [`concepts/`](concepts/README.md) — start with [Is it RCV or IRV?](concepts/RCV_or_IRV_whats_the_right_word.md) (the terminology that makes the rest read precisely), then [RCV-IRV (Hare)](concepts/RCV-IRV-Hare.md) for the method itself and [center squeeze](concepts/RCV_IRV_center_squeeze.md) for the critique. Everything below is the **runnable example and the engine**. <!-- terminology-ok: bare RCV is inside a linked page title -->

| Case | Page | YAML |
|---|---|---|
| RCV-IRV — a basic ranked-ballot example (3 candidates) | [page](cases/cases_pages/RCV_ballot_example.md) | [`RCV_ballot_example.yaml`](cases/RCV_ballot_example.yaml) |

The engine lives in [`RCV_IRV_tabulation_engine/`](RCV_IRV_tabulation_engine/README.md); full audit mirrors are in `RCV_IRV_tabulated/`.
