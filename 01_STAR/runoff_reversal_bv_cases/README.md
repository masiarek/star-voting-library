# Runoff Reversal — the BetterVoting case series

Real BetterVoting elections that demonstrate a **Runoff Reversal** — the Scoring-Round leader *loses* the Automatic Runoff to the finalist more voters prefer (the *score* winner ≠ the *STAR* winner). Each is a **two-view lesson**: BetterVoting's own screenshots beside the Larry Hastings engine report, so you see both how the result *looks* in the BV UI and how it *tallies* in the engine.

New to the idea itself? Start with the concept folder next door — **[When the top-scoring candidate isn't the winner](../runoff_overturns_leader/README.md)** (the plain explanation + small teaching demos with no live BetterVoting election) — and the presenter's guide, [Teaching Runoff Reversal](../runoff_overturns_leader/teaching_runoff_reversal.md). Concept hub: [The Automatic Runoff Round](../../00_start_here/STAR_Voting/the_count/STAR_Automatic_Runoff.md).

> **When to use two views (house principle).** Show BetterVoting beside the open-source engine's report (the "LH" tabulator) only where the two **diverge** (the discrepancy is the lesson, e.g. `Runoff_07`) or where reading **BV's own UI** is the point (this set — the screenshots teach how a STAR result *looks*). When BV and LH simply agree and there's no UI to teach, LH-only is enough (see the [vote-splitting set](../../method_comparisons/split_voting/)).

Read them in order — the *how much vs how many* arc, smallest reversal first:

| # | Lesson | Level | What it shows |
|---|--------|:---:|---------------|
| 01 | [confirms the leader](Runoff_01_confirms_leader_r2pvc9.md) | 101 | control — leader leads **and** wins (baseline) |
| 02 | [the atom](Runoff_02_atom_reversal_yx9447.md) | 101 | smallest reversal — broadly-liked runner-up loses |
| 03 | [enthusiasts vs majority](Runoff_03_enthusiasts_vs_majority_rkgtpk.md) | 201 | intense minority leads stars, majority wins (5 cand) |
| 04 | [reversal at scale](Runoff_04_reversal_at_scale_bfjqmg.md) | 101 | the atom blown up — 67/33, not a fluke |
| 05 | [reversal with Equal Support](Runoff_05_reversal_with_equal_support_xgkw3w.md) | 201 | "no preference" voters → the two-denominator bridge |
| 06 | [confirms at scale](Runoff_06_confirms_at_scale_d664xw.md) | 101 | control bookend — leader confirmed 4–1 |
| 07 ⚠️ | [flat ballot / BV bug **(WIP)**](Runoff_07_flat_ballot_bv_bug_tf73v9.md) | 201/301 | the one case where the reports *disagree* — a flat ballot BV mis-files as an abstention ([#1407](https://github.com/Equal-Vote/bettervoting/issues/1407)) |
| 08 | [CA Governor, a real field of 61 **(BV2181, `gvdy42`)**](Runoff_08_ca_governor_reversal_gvdy42.md) | 201/301 | the largest live case — Lapp (R) tops the score, **Steyer (D)** wins the runoff 98–80; also the Equal-Support reconciliation (141 = 124 + 17 abstentions) and the #1390 graph bug ([PR #1431](https://github.com/Equal-Vote/bettervoting/pull/1431)) |

↔ **BV QA tracker:** this set is the runnable home for **BV90** (scoring/runoff divergence) and **BV205** (top-scoring candidate ≠ winner) — the "Runoff Reversal" scenarios.

Each case is a trio — the two-view `.md` lesson, the tabulatable `.yaml`, and the frozen `_bv_export.json` — with the BetterVoting screenshots in `img/` (prefixed by the election's `bvid`). The auto-generated reader pages and full `_tabulated` reports live in `runoff_reversal_bv_cases_pages/` and `runoff_reversal_bv_cases_tabulated/`.
