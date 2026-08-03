# Ranked Robin tiebreaks — LH vs. BetterVoting (a documented divergence)

*Ranked Robin (RCV-RR / Copeland) almost always just elects the Condorcet winner, and every engine agrees. But when Copeland scores **tie**, the engines part ways in **how** they break it — and one of them is non-deterministic. This note pins the difference down, with two tested cases: one where everyone agrees, one where they can't.*

→ The method: [Ranked Robin](ranked_robin.md) · cycles in depth: [cycle_resolution.md](cycle_resolution.md) · same-animal-until-a-cycle: [ranked_robin_vs_condorcet.md](ranked_robin_vs_condorcet.md)

## The two ladders

Both engines score Copeland the same way — **win = 1, tie = ½** — and elect the highest. They differ only in the **tiebreak** when the top Copeland score is shared:

> **Fixed 2026-07-26.** LH's rung 1 used to sort on the **raw win count** while printing the wins + ½·ties column beside it, so the two disagreed whenever a pairwise **draw** existed — the report could contradict its own table and elect a candidate it had ranked third. Rung 1 is now the Copeland score, as this table always claimed. Ranking by wins + ½·ties and by wins − losses are affine transforms of each other and always agree; the raw win count was the outlier.

| Rung | **LH** `run_ranked_robin` (`starvote_larry_hastings.py`) | **BetterVoting** `RankedRobin.ts` |
|---|---|---|
| 1 | highest **Copeland score** (wins + ½·ties) | highest **Copeland score** (wins + ½·ties) |
| 2 | total **margin** (sum of For − Against) | **head-to-head** — *only if exactly 2 are tied* |
| 3 | **lot order** (pre-published `lot_numbers`) | **"random"** — a *seeded* shuffle |

Consequence: **LH is fully deterministic** at every rung (margin, then a pre-published lot). **BetterVoting is deterministic only for a clean 2-way tie that the head-to-head resolves** — otherwise (3+ tied, or a 2-way tie whose head-to-head is *itself* a tie) it falls through to its rung of last resort.

> **"Random" is the wrong word for BV's rung 3 — read this before relying on the row above.** BetterVoting's tiebreak is *not* a coin flip. `shuffleCandidatesForRandomTiebreak.ts` says outright that the protocol is written to be deterministic so that re-running the tabulator gives the same result; it seeds TinyRand with `(rawVoteCount + hash(raceId)) >>> 0`, shuffles once, and stores each candidate's index as `tieBreakOrder`. The shuffled order ships in the results JSON as **`perm`**, so the export publishes **the entire tiebreak sequence — winner and runners-up** — and a re-tally reproduces it. Confirmed on a live election built for the purpose: **[BV2261 `y2fbpc`](../03_Criteria/rr_tiebreaks/bv2261_y2fbpc_tiebreak_recorded.md)** (two races, both re-fetched byte-identical), and [BV2141](../03_Criteria/rr_tiebreaks/bv2141_3r3yf7_four_degree_tie.md) has been quietly relying on it all along by pinning `lot_numbers` to a recorded `perm`.
>
> What stays true is the *weaker, sharper* claim: BV's order is **recorded but not derivable**. It is a function of the ballot **count** and the race id, never of how anyone voted — so an independent engine can replay it from the export but can never predict it from the ballots. And because `rawVoteCount` is in the seed, every new ballot re-rolls the order, so a `perm` frozen mid-election describes that moment only. Both properties are why a *tie-deciding* case is still best kept LH-only: LH's lot is the only rung reproducible from published inputs alone.
>
> **Check it yourself rather than taking the above on trust.** [`tools_adam/bv_replay_tiebreak.py`](../../STARVote_LH_tabulation_engine/tools_adam/bv_replay_tiebreak.py) ports TinyRand + the BV shuffle to Python; hand it any frozen `_bv_export.json` and it recomputes each race's `perm` from `(rawVoteCount, raceId)` and diffs it against what BV recorded. It is also the cleanest demonstration of the "not derivable" half — no ballot content is passed in, and the order still comes out right.

> **Neither engine is wrong — and the divergence was unavoidable.** A small impossibility theorem (Moulin, 1983) proves that **no anonymous, neutral, Pareto rule can always name exactly one winner**; on those profiles a tie is forced and the rule *must* reach outside the ballots for something to decide with. The literature offers four ways to do that, and the two engines simply took different ones: **LH takes the fixed-order approach** (a pre-published lot) and pays in **neutrality** — permute the candidates' names and the winner can change. **BetterVoting takes the randomized approach** and pays in **predictability** — its winner is not a function of the ballots. (Not in *determinism*, note: the shuffle is seeded and reproducible, and it is recorded in the export — see the box above. What it can't be is *derived* from how people voted, which is why the dead-heat case below stays LH-only.) (`pref_voting`, consulted as the third opinion, takes a third approach: it returns the whole tied **leader set** and declines to choose.) Read that way, this page documents three defensible answers to a forced choice rather than a discrepancy to be resolved. Theory: [Ties Are Forced](../../07_Concepts/topics/ties/ties_are_forced.md).

## Where they agree — a clean Condorcet winner

When a Condorcet winner exists there's no tie to break, so every engine agrees. The BV-backed **[Tennessee case (BV2131)](../02_Examples/rr_vs_irv_plurality/bv2131_tennessee_condorcet_center_vqyqkr.md)** is the worked example: Nashville is 3–0 (Copeland 3), `tieBreakType: none`, and LH-native, BetterVoting (`RankedRobin.ts`), and `pref_voting`'s independent Copeland **all** elect Nashville. Agreement is the common case — this note is about the exception.

## Where they diverge — a dead heat

The LH-only **[dead-heat case](../03_Criteria/rr_tiebreaks/dead_heat_lot_tiebreak.md)** is engineered to tie every deterministic rung. Ada and Ben each go 1–0–1 (Copeland 1.5), both beat Cara, and their margins are identical (+4). What each engine does:

- **LH:** Copeland tie (1.5 = 1.5) → margin tie (+4 = +4) → **lot order** `[Ada, Ben, Cara]` → **Ada**. Reproducible every run.
- **BetterVoting:** Copeland tie → tries the 2-way head-to-head… but **Ada vs Ben is itself a tie** (1–1, with 2 Equal Support) → falls through to its **seeded shuffle**. Whatever it draws would be recorded and stable — but it is not predictable from these ballots, so the case can't demonstrate a *rule*, only one draw.

That's why the dead-heat case has **no BetterVoting election**: BV's answer here would be an accident of the seed rather than a consequence of the ballots, so there'd be nothing to *teach* from it. It documents the **LH** ladder specifically. (BetterVoting would agree Ada and Ben are co-leaders; it just wouldn't choose between them *on the evidence of the votes*.) If you want to see what BV records when it does land on that rung, [BV2261](../03_Criteria/rr_tiebreaks/bv2261_y2fbpc_tiebreak_recorded.md) is the case built to show it.

## Where they diverge — live (BV2176)

The **[Post-it RCV example (BV2176, `p8dp28`)](../../method_comparisons/postit_rcv_example/bv2176_p8dp28_postit_rcv_example.md)** is the first **live** BetterVoting election to land on the divergence — a clean 2-way tie whose head-to-head is decisive, so *both* ladders stay deterministic and simply disagree. (The same race runs live a second time inside the seven-method sweep [BV2177 `v8r66y`](../../method_comparisons/postit_rcv_example/bv2177_v8r66y_seven_methods.md); and the companion [BV2178 `8kg698`](../../method_comparisons/postit_rcv_example/bv2178_8kg698_switch_made_real.md) shows how knife-edge the tie is — two flipped ballots dissolve the cycle into a clean Condorcet winner and both engines snap back to agreement.) Green and Blue each go 2–1 inside a genuine cycle. BetterVoting's rung 2 (head-to-head between the two tied) elects **Green**, who beats Blue 7–4 — confirmed on the live results page and freezable. LH's rung 2 (total margin) elects **Blue** (+5 vs Green's +4). Same ballots, same Copeland tie, two published rules, two winners — `pref_voting`'s independent Copeland reports the leader set {Blue, Green}, and each engine tie-broke inside it consistently with its own ladder.

## Practical guidance

- For **teaching a clean outcome** (a Condorcet winner, or any un-tied Copeland ranking), any engine is fine and they agree — cross-check freely.
> **Confirmed by Equal Vote — and scheduled to change (as of 2026-07-29).** On [electowiki's Ranked Robin talk page](https://electowiki.org/wiki/Talk:Ranked_Robin) in 2025, Sara Wolk wrote that BetterVoting "currently has a random tiebreaker in place, but the plan is to allow users to select from a handful of tiebreaker options (Smith-Minimax, Copeland-Margins, Simple Favorite) before it goes to random." So the divergence this page documents is real and acknowledged by the people who built the other engine — **and it has an expiry date**. If BetterVoting ships a selectable Copeland-Margins option, its rung 1–2 could line up with LH's and the dead-heat case below may stop being LH-only. Re-check before relying on the table above.

- For a case that **turns on the tiebreak**, state which engine's rule you're relying on. Only the **LH** rule (margin → lot) is reproducible from the ballots plus a published lot. If a real BetterVoting election lands on a Copeland tie, its winner is stable and recorded — but it is decided by the seed, **not a function of the ballots**, so no argument about *how people voted* can rest on it.
- When you *want* determinism from a tie, pin `lot_numbers` in the YAML and use the LH tally; the printed winner line names the rung that decided it.

## Engine wording (fixed)

The winner line now distinguishes a dead heat from a real cycle. `run_ranked_robin`
tests whether the tied leaders **draw** their head-to-heads (dead heat) or **beat
around a loop** (cycle):

```
# co-top dead heat (leaders draw each other, both beat the rest):
*** 2 candidates tie on the highest Copeland score (1.5): Ada, Ben — a dead heat (they draw head-to-head, not a cycle). Resolved by total margin, then lot order.

# genuine rock-paper-scissors cycle (directed loop, no Condorcet winner):
*** 3 candidates tie for the most wins (Rock, Scissors, Paper) — a Condorcet cycle (no candidate beats all others). Resolved by total margin, then lot order. (… Minimax / Ranked Pairs / Schulze differ — see cycle_resolution.md.)
```

Both lead with the *tie*, not a verdict; "cycle" is reserved for a genuine loop. The lead phrasing adapts: with no **draws** among the leaders it says "**tie for the most wins**" (then tying on Copeland *is* tying on wins), and once a draw is in play — as in the dead heat above, where Ada and Ben draw each other — it names the **Copeland score** instead, because "most wins" would no longer be true. Locked by `tests/test_ranked_robin.py` (the RPS case asserts "Condorcet cycle"; the dead-heat case asserts "dead heat" and *not* "Condorcet cycle").

## Tested cases

| Case | Method | Outcome | Engines |
|------|--------|---------|---------|
| [BV2131 — Tennessee](../02_Examples/rr_vs_irv_plurality/bv2131_tennessee_condorcet_center_vqyqkr.md) | RankedRobin | Nashville (Condorcet, no tiebreak) | LH = BV = pref_voting ✓ |
| [Dead heat → lot](../03_Criteria/rr_tiebreaks/dead_heat_lot_tiebreak.md) | RankedRobin | Ada (LH lot); BV random | LH deterministic; BV non-deterministic |
| [BV2176 — Post-it RCV example](../../method_comparisons/postit_rcv_example/bv2176_p8dp28_postit_rcv_example.md) | RankedRobin | 2-way tie, decisive head-to-head: **Green (BV) vs Blue (LH)** | both deterministic — the ladder divergence, live |
| [BV2261 — the tiebreak is recorded](../03_Criteria/rr_tiebreaks/bv2261_y2fbpc_tiebreak_recorded.md) | RankedRobin ×2 | 3-way tie twice (by draws, then by cycle) → Anika both times | BV's `perm` replayed as LH's lot: winner **and full order** match; `pref_voting` returns the leader set |
| [BV2262 — nine-way dead heat](../03_Criteria/rr_tiebreaks/bv2262_2gvwr9_nine_way_dead_heat.md) | RankedRobin | 9 candidates all 4–4–0, margin +0 → Boris (6th in list order) | the scale check: nine-deep `perm`, LH matches all nine positions, shuffle independently recomputed, `pref_voting` consistent |

## Related

- **The tie-break itself can't be made strategyproof** — Brandt, Saile & Stricker, *"Strategyproof social choice when preferences and outcomes may contain ties"* (*Journal of Economic Theory* 202, 2022, [105447](https://doi.org/10.1016/j.jet.2022.105447)) prove that *no* anonymous, Pareto-optimal tie-breaking rule — a fixed order (LH's lot) *or* a coin flip (BV's random) — escapes manipulability once voters may express ties, so the LH-vs-BV choice above is a design trade-off, not a solved problem.
- [Ranked Robin (the method)](ranked_robin.md) · [cycle resolution](cycle_resolution.md) · [ranked_robin_vs_condorcet.md](ranked_robin_vs_condorcet.md)
- **This same Copeland-margin logic is offered as an optional *STAR* tiebreaker** — Equal Vote's [Condorcet Tiebreaker](../../01_STAR/01_Learn/Tie_Breaking_STAR/condorcet_tiebreaker.md) runs a mini round-robin (most head-to-head wins → margin) among candidates STAR's own rounds left tied. Ranked Robin is this arithmetic as a *whole method*; there it is a *subroutine* firing only on an exact STAR tie.
- BetterVoting tabulation engine notes: [`tabulation_engines/BV/tabulation_engine/README.md`](../../07_Concepts/tabulation_engines/BV/tabulation_engine/README.md) (the `RankedRobin.ts` row: *"2-way tie → head-to-head; else random"*)
- [Glossary](../../07_Concepts/GLOSSARY.md)

# file: rr_tiebreak_lh_vs_bv.md
