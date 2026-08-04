# rr_tiebreaks — how Ranked Robin breaks a tie (and where engines diverge)

Ranked Robin usually just elects the Condorcet winner. This set is about the **edge**: what happens when Copeland scores tie, how the LH engine resolves it, and where that resolution **differs** from BetterVoting.

| Case (page) | What it shows | Winner | BV-backed? | src |
|------|---------------|:---:|:---:|:--:|
| [Dead heat → lot order](dead_heat_lot_tiebreak.md) | Equal Support + ½-Copeland + the full ladder to **lot** | Ada (by lot) | **No — divergent** | [`.yaml`](cases/dead_heat_lot_tiebreak.yaml) |
| [BV2141 — all four Equal-Vote degrees](bv2141_3r3yf7_four_degree_tie.md) | a Copeland tie that survives three tiebreak degrees; only the 4th (beatpath) separates | Ava (by recorded draw) | **Yes** `3r3yf7` | [`.yaml`](cases/bv2141_3r3yf7_four_degree_tie.yaml) |
| [BV2261 — the random tiebreak is **recorded**](bv2261_y2fbpc_tiebreak_recorded.md) | the export publishes the whole tiebreak order (`perm` / `tieBreakOrder`), stable on re-tally; two races reach the last rung by **draws** and by **cycle** | Anika (both races) | **Yes** `y2fbpc` | [draws](cases/bv2261_y2fbpc_tiebreak_recorded_draws.yaml) · [cycle](cases/bv2261_y2fbpc_tiebreak_recorded_cycle.yaml) |
| [BV2262 — nine-way dead heat](bv2262_2gvwr9_nine_way_dead_heat.md) | the same at **9 candidates**: a nine-deep recorded order, a shuffle that really scrambles, four independent checks | Boris | **Yes** `2gvwr9` | [`.yaml`](cases/bv2262_2gvwr9_nine_way_dead_heat.yaml) |
| [BV2270 — rung 2, where the engines part](bv2270_8h4bvh_head_to_head_vs_margin.md) | a two-way Copeland tie broken **deterministically on both sides** — and to **different winners**: LH on total margin, BV head-to-head. No lot anywhere | **Birch** (LH) · **Alder** (BV) | **Yes** `8h4bvh` | [`.yaml`](cases/bv2270_8h4bvh_head_to_head_vs_margin.yaml) |

**The divergence in one table:**

| | Tiebreak ladder |
|---|---|
| **LH** `run_ranked_robin` | highest **Copeland score** → total **margin** → **lot order** (deterministic) |
| **BetterVoting** `RankedRobin.ts` | highest **Copeland score** → **head-to-head** (2-way only) → **"random"** (a seeded shuffle) |

The two rungs part ways in two different situations, and the set now has one of each. In the **dead-heat** case the two leaders tie head-to-head as well, so BV falls through to its last rung while LH is still on its lot — the ladders differ, but both end up at a rung of last resort. In **[BV2270](bv2270_8h4bvh_head_to_head_vs_margin.md)** neither engine gets that far: both stop on rung 2 with a computed answer, and the answers are **different candidates**. That is the sharper case — and unlike the dead heat it could be minted, because nothing about it turns on a draw. The same divergence was first caught in the wild by [BV2176, the Post-it RCV example](../../../method_comparisons/postit_rcv_example/bv2176_p8dp28_postit_rcv_example.md); BV2270 is the stripped-down bench version, four candidates and nine ballots.

**Careful with "random", though** — BV's last rung is a *seeded* shuffle, not a coin flip. It is deterministic on re-tally and the resulting order is published in the export as `perm`. [BV2261](bv2261_y2fbpc_tiebreak_recorded.md) was built to confirm exactly that on a live election, and [BV2141](bv2141_3r3yf7_four_degree_tie.md) already relies on it. What you *cannot* do is **derive** the order from the ballots — it depends on the ballot count and the race id, not on how anyone voted — which is the real reason the dead-heat case stays **LH-only**. Full write-up + the "cycle" wording nit: [Ranked Robin tie-breaks — LH vs BetterVoting](../../01_Learn/rr_tiebreak_lh_vs_bv.md).

**Concept docs:** [Ranked Robin (the method)](../../01_Learn/ranked_robin.md) · [cycle resolution](../../01_Learn/cycle_resolution.md).

# file: README.md
