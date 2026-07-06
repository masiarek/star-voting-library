# rr_tiebreaks — how Ranked Robin breaks a tie (and where engines diverge)

Ranked Robin usually just elects the Condorcet winner. This set is about the **edge**: what happens when Copeland scores tie, how the LH engine resolves it, and where that resolution **differs** from BetterVoting.

| Case (page) | What it shows | Winner | BV-backed? | src |
|------|---------------|:---:|:---:|:--:|
| [Dead heat → lot order](dead_heat_lot_tiebreak.md) | Equal Support + ½-Copeland + the full ladder to **lot** | Ada (by lot) | **No — divergent** | [`.yaml`](dead_heat_lot_tiebreak.yaml) |

**The divergence in one table:**

| | Tiebreak ladder |
|---|---|
| **LH** `run_ranked_robin` | most wins → total **margin** → **lot order** (deterministic) |
| **BetterVoting** `RankedRobin.ts` | most wins → **head-to-head** (2-way) → **random** |

The dead-heat case is exactly the input where these part ways (the two leaders tie head-to-head too, so BV goes random), which is why it's **LH-only** — a random BV result can't be frozen. Full write-up + the "cycle" wording nit: [rr_tiebreak_lh_vs_bv.md](../../00_start_here/RCV_Ranked_Robin/rr_tiebreak_lh_vs_bv.md).

**Concept docs:** [Ranked Robin (the method)](../../00_start_here/RCV_Ranked_Robin/ranked_robin.md) · [cycle resolution](../../00_start_here/RCV_Ranked_Robin/cycle_resolution.md).

# file: README.md
