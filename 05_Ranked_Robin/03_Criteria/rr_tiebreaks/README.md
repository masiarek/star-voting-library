# rr_tiebreaks — how Ranked Robin breaks a tie

Ranked Robin usually just elects the Condorcet winner. This set is about the **edge**: what happens when Copeland scores tie, what the method's own protocol says to do about it, and how far each engine actually follows that protocol.

**Start with [Degrees of ties](degrees_of_ties.md)** — the four-rung ladder Ranked Robin publishes, the two ways the engines departed from it, and what the departure cost. The rest of this folder is the case set behind it.

| Case (page) | What it shows | Winner | BV-backed? | src |
|------|---------------|:---:|:---:|:--:|
| [Dead heat → lot order](dead_heat_lot_tiebreak.md) | Equal Support + ½-Copeland + the full ladder to **lot** | Ada (by lot) | **No — divergent** | [`.yaml`](cases/dead_heat_lot_tiebreak.yaml) |
| [BV2141 — all four Equal-Vote degrees](bv2141_3r3yf7_four_degree_tie.md) | a Copeland tie that survives three tiebreak degrees; only the 4th (beatpath) separates | Ava (by recorded draw) | **Yes** `3r3yf7` | [`.yaml`](cases/bv2141_3r3yf7_four_degree_tie.yaml) |
| [BV2261 — the random tiebreak is **recorded**](bv2261_y2fbpc_tiebreak_recorded.md) | the export publishes the whole tiebreak order (`perm` / `tieBreakOrder`), stable on re-tally; two races reach the last rung by **draws** and by **cycle** | Anika (both races) | **Yes** `y2fbpc` | [draws](cases/bv2261_y2fbpc_tiebreak_recorded_draws.yaml) · [cycle](cases/bv2261_y2fbpc_tiebreak_recorded_cycle.yaml) |
| [BV2262 — nine-way dead heat](bv2262_2gvwr9_nine_way_dead_heat.md) | the same at **9 candidates**: a nine-deep recorded order, a shuffle that really scrambles, four independent checks | Boris | **Yes** `2gvwr9` | [`.yaml`](cases/bv2262_2gvwr9_nine_way_dead_heat.yaml) |
| [BV2270 — the tie that showed the ladder was wrong](bv2270_8h4bvh_head_to_head_vs_margin.md) | a two-way Copeland tie broken deterministically on both sides. It elected **different** candidates until the engine's missing 1st Degree rung was added; now both say Alder | **Alder** (both) | **Yes** `8h4bvh` | [`.yaml`](cases/bv2270_8h4bvh_head_to_head_vs_margin.yaml) |
| [The 1st Degree counts the finalists only](degrees_of_ties.md) | three tied finalists where margins-over-finalists and margins-over-the-field elect **different** candidates — the case that separates the two rungs | Alma | No — LH-only | [`.yaml`](cases/rr_degrees_finalists_vs_field.yaml) |
| [A three-way cycle has a deterministic answer](degrees_of_ties.md) | eleven ballots, one cycle, a 1st Degree answer of +6 — and BetterVoting draws lots for it ([#1469](https://github.com/Equal-Vote/bettervoting/issues/1469)) | Frank | No — LH-only | [`.yaml`](cases/rr_degrees_three_way_cycle.yaml) |
| [What counts as a win](degrees_of_ties.md#the-rung-below-the-ladder-what-counts-as-a-win) | four ballots, two drawn matchups: scoring a draw as **half a win** (every engine) elects the undefeated Bella, scoring it as **nothing** (the spec's own sentence) elects Dana, who lost to her — an open question about the rule *above* the ladder | Bella | No — LH-only | [`.yaml`](cases/rr_degrees_what_counts_as_a_win.yaml) |

**The ladders in one table:**

| | Tiebreak ladder |
|---|---|
| **The protocol** ([electowiki](https://electowiki.org/wiki/Ranked_Robin#Degrees_of_ties)) | **Copeland score** → **1st Degree** (margins over the other finalists) → **2nd Degree** (margins over all candidates) → a lot or a re-run |
| **LH** `run_ranked_robin` | the same three rungs, then a published **lot order** — since 2026-08-19 |
| **BetterVoting** `RankedRobin.ts` | **Copeland score** → **head-to-head** (2-way only) → **"random"** (a seeded shuffle) |

Read the middle rungs and both engines' bugs are visible at once. BetterVoting's head-to-head *is* the 1st Degree, but only for exactly two tied candidates — three or more skip both degrees and land on the shuffle ([#1469](https://github.com/Equal-Vote/bettervoting/issues/1469)), which for a three-candidate field means every cycle. LH had the 2nd Degree and used it in the 1st's place, so it overrode the finalists' own head-to-head with margins run up against candidates outside the tie. **[BV2270](bv2270_8h4bvh_head_to_head_vs_margin.md)** is where that showed: the two engines elected different candidates from the same nine ballots, and the protocol says BetterVoting had it right. The same disagreement was first caught in the wild by [BV2176, the Post-it RCV example](../../../method_comparisons/postit_rcv_example/bv2176_p8dp28_postit_rcv_example.md); BV2270 is the stripped-down bench version, four candidates and nine ballots. Both now agree — the full account is in [degrees of ties](degrees_of_ties.md).

What still genuinely differs is the **bottom** rung: when neither degree separates the finalists, LH draws a pre-published lot and BetterVoting a seeded shuffle. That is the [dead-heat case](dead_heat_lot_tiebreak.md), and no fix removes it — a tie that the ballots do not break has to be decided by something outside them.

And the **top** rung — the Copeland score every ladder above starts from — is not fully settled either. All three engines score a drawn matchup as half a win; the protocol's own one-line definition says *"beats the greatest number of candidates"*, which counts wins alone, and its worked example scores a candidate with three wins and a draw as 3 rather than 3.5. Usually that makes no difference, because the two readings agree whenever every matchup is decided — but it decides who is even *in* the tie, so it can change the winner. This repo follows the half-point and records the disagreement as an open question rather than a defect: [what counts as a win](degrees_of_ties.md#the-rung-below-the-ladder-what-counts-as-a-win).

**Careful with "random", though** — BV's last rung is a *seeded* shuffle, not a coin flip. It is deterministic on re-tally and the resulting order is published in the export as `perm`. [BV2261](bv2261_y2fbpc_tiebreak_recorded.md) was built to confirm exactly that on a live election, and [BV2141](bv2141_3r3yf7_four_degree_tie.md) already relies on it. What you *cannot* do is **derive** the order from the ballots — it depends on the ballot count and the race id, not on how anyone voted — which is the real reason the dead-heat case stays **LH-only**. Full write-up + the "cycle" wording nit: [Ranked Robin tie-breaks — LH vs BetterVoting](../../01_Learn/rr_tiebreak_lh_vs_bv.md).

**Concept docs:** [Ranked Robin (the method)](../../01_Learn/ranked_robin.md) · [cycle resolution](../../01_Learn/cycle_resolution.md).

# file: README.md
