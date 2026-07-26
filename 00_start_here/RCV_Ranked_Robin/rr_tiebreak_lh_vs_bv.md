# Ranked Robin tiebreaks — LH vs. BetterVoting (a documented divergence)

*Ranked Robin (RCV-RR / Copeland) almost always just elects the Condorcet winner, and every engine agrees. But when Copeland scores **tie**, the engines part ways in **how** they break it — and one of them is non-deterministic. This note pins the difference down, with two tested cases: one where everyone agrees, one where they can't.*

→ The method: [Ranked Robin](ranked_robin.md) · cycles in depth: [cycle_resolution.md](cycle_resolution.md) · same-animal-until-a-cycle: [ranked_robin_vs_condorcet.md](ranked_robin_vs_condorcet.md)

## The two ladders

Both engines score Copeland the same way — **win = 1, drawn matchup = ½ to each side** — and elect the highest. They differ only in the **tiebreak** when the top Copeland score is shared:

| Rung | **LH** `run_ranked_robin` (`starvote_larry_hastings.py`) | **BetterVoting** `RankedRobin.ts` |
|---|---|---|
| 1 | highest **Copeland score** (win 1, draw ½) | highest **Copeland score** (win +1, tie +0.5) |
| 2 | total **margin** (sum of For − Against) | **head-to-head** — *only if exactly 2 are tied* |
| 3 | **lot order** (pre-published `lot_numbers`) | **random** |

> **Rung 1 used to be the divergence nobody had noticed.** Until 2026-07-25 LH *printed* the Copeland score but *sorted* by the raw win count — identical rankings as long as every matchup had a winner, and silently different the moment one was drawn. On such a profile LH could elect a candidate who had lost head-to-head to the one at the top of its own Copeland column, while BetterVoting and `pref_voting` (whose Copeland is `wins − losses`, the same ordering rescaled) both elected the latter. LH now sorts by the score it prints, so all three agree at rung 1 and the divergence below is genuinely only about rungs 2–3. Regression-locked by `tests/test_ranked_robin.py::test_copeland_score_decides_not_raw_wins`.

Consequence: **LH is fully deterministic** at every rung (margin, then a pre-published lot). **BetterVoting is deterministic only for a clean 2-way tie that the head-to-head resolves** — otherwise (3+ tied, or a 2-way tie whose head-to-head is *itself* a tie) it falls through to a **random** choice.

> **Neither engine is wrong — and the divergence was unavoidable.** A small impossibility theorem (Moulin, 1983) proves that **no anonymous, neutral, Pareto rule can always name exactly one winner**; on those profiles a tie is forced and the rule *must* reach outside the ballots for something to decide with. The literature offers four ways to do that, and the two engines simply took different ones: **LH takes the fixed-order approach** (a pre-published lot) and pays in **neutrality** — permute the candidates' names and the winner can change. **BetterVoting takes the randomized approach** and pays in **determinism** — which is precisely why a randomly-broken BV tie can't be frozen into a `_bv_export.json`, and why the dead-heat case below is LH-only. (`pref_voting`, consulted as the third opinion, takes a third approach: it returns the whole tied **leader set** and declines to choose.) Read that way, this page documents three defensible answers to a forced choice rather than a discrepancy to be resolved. Theory: [Ties Are Forced](../topics/ties/ties_are_forced.md).

## Where they agree — a clean Condorcet winner

When a Condorcet winner exists there's no tie to break, so every engine agrees. The BV-backed **[Tennessee case (BV2131)](../../05_Ranked_Robin/rr_vs_irv_plurality/bv2131_tennessee_condorcet_center_vqyqkr.md)** is the worked example: Nashville is 3–0 (Copeland 3), `tieBreakType: none`, and LH-native, BetterVoting (`RankedRobin.ts`), and `pref_voting`'s independent Copeland **all** elect Nashville. Agreement is the common case — this note is about the exception.

## Where they diverge — a dead heat

The LH-only **[dead-heat case](../../05_Ranked_Robin/rr_tiebreaks/dead_heat_lot_tiebreak.md)** is engineered to tie every deterministic rung. Ada and Ben each go 1–0–1 (Copeland 1.5), both beat Cara, and their margins are identical (+4). What each engine does:

- **LH:** wins tie (1 = 1) → margin tie (+4 = +4) → **lot order** `[Ada, Ben, Cara]` → **Ada**. Reproducible every run.
- **BetterVoting:** wins tie → tries the 2-way head-to-head… but **Ada vs Ben is itself a tie** (1–1, with 2 Equal Support) → falls through to **random**. Not reproducible; can't be frozen into a `_bv_export.json`.

That's why the dead-heat case has **no BetterVoting election**: there is no stable BV result to record. It documents the **LH** ladder specifically. (BetterVoting would agree Ada and Ben are co-leaders; it just wouldn't deterministically choose between them.)

## Where they diverge — live (BV2176)

The **[Post-it RCV example (BV2176, `p8dp28`)](../../method_comparisons/postit_rcv_example/bv2176_p8dp28_postit_rcv_example.md)** is the first **live** BetterVoting election to land on the divergence — a clean 2-way tie whose head-to-head is decisive, so *both* ladders stay deterministic and simply disagree. (The same race runs live a second time inside the seven-method sweep [BV2177 `v8r66y`](../../method_comparisons/postit_rcv_example/bv2177_v8r66y_seven_methods.md); and the companion [BV2178 `8kg698`](../../method_comparisons/postit_rcv_example/bv2178_8kg698_switch_made_real.md) shows how knife-edge the tie is — two flipped ballots dissolve the cycle into a clean Condorcet winner and both engines snap back to agreement.) Green and Blue each go 2–1 inside a genuine cycle. BetterVoting's rung 2 (head-to-head between the two tied) elects **Green**, who beats Blue 7–4 — confirmed on the live results page and freezable. LH's rung 2 (total margin) elects **Blue** (+5 vs Green's +4). Same ballots, same Copeland tie, two published rules, two winners — `pref_voting`'s independent Copeland reports the leader set {Blue, Green}, and each engine tie-broke inside it consistently with its own ladder.

## Practical guidance

- For **teaching a clean outcome** (a Condorcet winner, or any un-tied Copeland ranking), any engine is fine and they agree — cross-check freely.
- For a case that **turns on the tiebreak**, state which engine's rule you're relying on. Only the **LH** rule (margin → lot) is reproducible from the ballots plus a published lot. If a real BetterVoting election could land on a Copeland tie, its winner may be **random**, not a function of the ballots.
- When you *want* determinism from a tie, pin `lot_numbers` in the YAML and use the LH tally; the printed winner line names the rung that decided it.

## Engine wording (fixed)

The winner line distinguishes a dead heat from a real cycle. `run_ranked_robin` runs
a **DFS over the beat-edges** and only says "cycle" when it finds an actual directed
loop — which it then prints. Two passes: among the tied **leaders** first (the loop
that most directly explains their tie), then across the **whole field**, because a
loop can run through a non-leader — exactly what happens in BV2176 below, where
co-leaders Green and Blue sit inside a cycle that also passes through Purple and Pink:

```
# co-top dead heat (leaders draw each other, both beat the rest):
*** 2 candidates tie for the top Copeland score, 1.5 (Ada, Ben) — a dead heat (they draw head-to-head, not a cycle). Resolved by total margin, then lot order.

# genuine rock-paper-scissors cycle (directed loop, no Condorcet winner):
*** 3 candidates tie for the top Copeland score, 1 (Rock, Scissors, Paper) — a Condorcet cycle (Rock → Scissors → Paper → Rock: no candidate beats all others). Resolved by total margin, then lot order. (… Minimax / Ranked Pairs / Schulze differ — see cycle_resolution.md.)

# a loop that runs through non-leaders (BV2176 — the second DFS pass finds it):
*** 2 candidates tie for the top Copeland score, 2 (Green, Blue) — a Condorcet cycle (Green → Blue → Pink → Purple → Green: no candidate beats all others). Resolved by total margin, then lot order. (…)

# tied on score, no loop anywhere (neither of the above):
*** 2 candidates tie for the top Copeland score, 2 (Ada, Dev) — not a cycle (no loop among them; their wins and draws simply add up the same). Resolved by total margin, then lot order.
```

All four lead with "**tie for the top Copeland score**" — accurate, because that score is what the ranking is on. (They used to lead with "tie for the most wins," which was only true while the sort key was the raw win count.) The earlier draw-only test was a good discriminator but an incomplete one: it caught leaders who *draw each other*, and left a leader **drawn with a non-leader** to fall through to the cycle branch — which is how an acyclic profile could be announced as a Condorcet cycle. Asking the beat-graph directly answers the actual question, in both directions. Locked by `tests/test_ranked_robin.py` (the RPS case asserts "Condorcet cycle"; the dead-heat and acyclic cases assert *not* "Condorcet cycle").

There is one further line, printed whenever the winner has a loss and somebody else went unbeaten — Copeland's half-credit means an unbeaten record full of draws can be tied or out-scored, so the report discloses it rather than passing the candidate over in silence:

```
*** note: Dev is never beaten head-to-head (a weak Condorcet winner) yet did not win — Copeland counts a draw as only half a win, so an unbeaten record full of draws can be tied or out-scored by a candidate who lost a matchup.
```

That is a **disclosure, not a different rule**: forcing the unbeaten candidate through would put LH back out of step with BetterVoting and `pref_voting`, which is the trade this whole page exists to keep honest.

## Tested cases

| Case | Method | Outcome | Engines |
|------|--------|---------|---------|
| [BV2131 — Tennessee](../../05_Ranked_Robin/rr_vs_irv_plurality/bv2131_tennessee_condorcet_center_vqyqkr.md) | RankedRobin | Nashville (Condorcet, no tiebreak) | LH = BV = pref_voting ✓ |
| [Dead heat → lot](../../05_Ranked_Robin/rr_tiebreaks/dead_heat_lot_tiebreak.md) | RankedRobin | Ada (LH lot); BV random | LH deterministic; BV non-deterministic |
| [BV2176 — Post-it RCV example](../../method_comparisons/postit_rcv_example/bv2176_p8dp28_postit_rcv_example.md) | RankedRobin | 2-way tie, decisive head-to-head: **Green (BV) vs Blue (LH)** | both deterministic — the ladder divergence, live |

## Related

- **The tie-break itself can't be made strategyproof** — Brandt, Saile & Stricker, *"Strategyproof social choice when preferences and outcomes may contain ties"* (*Journal of Economic Theory* 202, 2022, [105447](https://doi.org/10.1016/j.jet.2022.105447)) prove that *no* anonymous, Pareto-optimal tie-breaking rule — a fixed order (LH's lot) *or* a coin flip (BV's random) — escapes manipulability once voters may express ties, so the LH-vs-BV choice above is a design trade-off, not a solved problem.
- [Ranked Robin (the method)](ranked_robin.md) · [cycle resolution](cycle_resolution.md) · [ranked_robin_vs_condorcet.md](ranked_robin_vs_condorcet.md)
- **This same Copeland-margin logic is offered as an optional *STAR* tiebreaker** — Equal Vote's [Condorcet Tiebreaker](../STAR_Voting/Tie_Breaking_STAR/condorcet_tiebreaker.md) runs a mini round-robin (most head-to-head wins → margin) among candidates STAR's own rounds left tied. Ranked Robin is this arithmetic as a *whole method*; there it is a *subroutine* firing only on an exact STAR tie.
- BetterVoting tabulation engine notes: [`tabulation_engines/BV/tabulation_engine/README.md`](../tabulation_engines/BV/tabulation_engine/README.md) (the `RankedRobin.ts` row: *"2-way tie → head-to-head; else random"*)
- [Glossary](../GLOSSARY.md)

# file: rr_tiebreak_lh_vs_bv.md
