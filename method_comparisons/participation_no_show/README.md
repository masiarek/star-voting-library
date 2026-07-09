# Participation / no-show paradox — one electorate, told twice (BV2174 / BV2175, live)

The tabulatable evidence behind the [Participation topic hub](../../00_start_here/topics/participation/). Eight April fans decide whether to vote; **three races on each election** (STAR, RCV-IRV, Choose-One) show what their sincere ballots buy under each method: Choose-One and STAR reward them (Celia→April and Bruno→April), **RCV-IRV punishes them** — Bruno→Celia, their second choice replaced by their last. "Vote — it can only help" is a promise RCV-IRV structurally can't make.

**▶ Live on BetterVoting:**
- **BV2174** (8 fans stay home) — [vote](https://bettervoting.com/yyhr66) · **[results ↗](https://bettervoting.com/yyhr66/results)** (election `yyhr66`)
- **BV2175** (8 fans vote) — [vote](https://bettervoting.com/9dhv8y) · **[results ↗](https://bettervoting.com/9dhv8y/results)** (election `9dhv8y`)

No Ranked Robin races: both electorates are a Condorcet cycle (that's the soil the paradox grows in), and BV resolves a Copeland tie at random — not freezable. The LH engine's margin tiebreak resolves it deterministically (Celia in BV2174, April in BV2175); see the `_tabulated` mirrors and [LH vs BV on RR ties](../../00_start_here/RCV_Ranked_Robin/rr_tiebreak_lh_vs_bv.md).

Read the reader-friendly **pages** (`participation_no_show_pages/`); the `.yaml` beside each is the tabulatable source.

| Page (read this) | What it shows | src |
|---|---|:--:|
| [BV2174 — the baseline (54 voters)](participation_no_show_pages/bv2174_yyhr66_noshow_baseline.md) | RCV-IRV → Bruno; STAR → Bruno via a Runoff Reversal (Celia tops scores 136/122/120, loses the runoff 34–20); Choose-One → Celia; pairwise = a perfect cycle | [`.yaml`](bv2174_yyhr66_noshow_baseline.yaml) |
| [BV2175 — the 8 fans show up (62 voters)](participation_no_show_pages/bv2175_9dhv8y_noshow_showup.md) | Choose-One → April (helped), STAR → April (favorite wins), RCV-IRV → **Celia** (their extra first-choice votes got their own fallback eliminated — the no-show paradox, and the Twin paradox read forward) | [`.yaml`](bv2175_9dhv8y_noshow_showup.yaml) |

Concept hubs: [Participation](../../00_start_here/topics/participation/) · [monotonicity](../../00_start_here/topics/monotonicity/) (same elimination machinery) · the paradox-catalog page: [no-show](../../00_start_here/voting_paradoxes/no_show.md) · up: [method_comparisons — same ballots, different methods](../)

# file: README.md
