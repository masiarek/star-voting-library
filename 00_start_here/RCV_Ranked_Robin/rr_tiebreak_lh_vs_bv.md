# Ranked Robin tiebreaks — LH vs. BetterVoting (a documented divergence)

*Ranked Robin (RCV-RR / Copeland) almost always just elects the Condorcet winner, and every engine agrees. But when Copeland scores **tie**, the engines part ways in **how** they break it — and one of them is non-deterministic. This note pins the difference down, with two tested cases: one where everyone agrees, one where they can't.*

→ The method: [Ranked Robin](ranked_robin.md) · cycles in depth: [cycle_resolution.md](cycle_resolution.md) · same-animal-until-a-cycle: [ranked_robin_vs_condorcet.md](ranked_robin_vs_condorcet.md)

## The two ladders

Both engines score Copeland the same way — **win = 1, tie = ½** — and elect the highest. They differ only in the **tiebreak** when the top Copeland score is shared:

| Rung | **LH** `run_ranked_robin` (`starvote_larry_hastings.py`) | **BetterVoting** `RankedRobin.ts` |
|---|---|---|
| 1 | most head-to-head **wins** | most head-to-head **wins** (Copeland) |
| 2 | total **margin** (sum of For − Against) | **head-to-head** — *only if exactly 2 are tied* |
| 3 | **lot order** (pre-published `lot_numbers`) | **random** |

Consequence: **LH is fully deterministic** at every rung (margin, then a pre-published lot). **BetterVoting is deterministic only for a clean 2-way tie that the head-to-head resolves** — otherwise (3+ tied, or a 2-way tie whose head-to-head is *itself* a tie) it falls through to a **random** choice.

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

The winner line now distinguishes a dead heat from a real cycle. `run_ranked_robin`
tests whether the tied leaders **draw** their head-to-heads (dead heat) or **beat
around a loop** (cycle):

```
# co-top dead heat (leaders draw each other, both beat the rest):
*** 2 candidates tie for the most wins (Ada, Ben) — a dead heat (they draw head-to-head, not a cycle). Resolved by total margin, then lot order.

# genuine rock-paper-scissors cycle (directed loop, no Condorcet winner):
*** 3 candidates tie for the most wins (Rock, Scissors, Paper) — a Condorcet cycle (no candidate beats all others). Resolved by total margin, then lot order. (… Minimax / Ranked Pairs / Schulze differ — see cycle_resolution.md.)
```

Both lead with "**tie for the most wins**" (accurate); "cycle" is reserved for a genuine loop. Locked by `tests/test_ranked_robin.py` (the RPS case asserts "Condorcet cycle"; the dead-heat case asserts "dead heat" and *not* "Condorcet cycle").

## Tested cases

| Case | Method | Outcome | Engines |
|------|--------|---------|---------|
| [BV2131 — Tennessee](../../05_Ranked_Robin/rr_vs_irv_plurality/bv2131_tennessee_condorcet_center_vqyqkr.md) | RankedRobin | Nashville (Condorcet, no tiebreak) | LH = BV = pref_voting ✓ |
| [Dead heat → lot](../../05_Ranked_Robin/rr_tiebreaks/dead_heat_lot_tiebreak.md) | RankedRobin | Ada (LH lot); BV random | LH deterministic; BV non-deterministic |
| [BV2176 — Post-it RCV example](../../method_comparisons/postit_rcv_example/bv2176_p8dp28_postit_rcv_example.md) | RankedRobin | 2-way tie, decisive head-to-head: **Green (BV) vs Blue (LH)** | both deterministic — the ladder divergence, live |

## Related

- [Ranked Robin (the method)](ranked_robin.md) · [cycle resolution](cycle_resolution.md) · [ranked_robin_vs_condorcet.md](ranked_robin_vs_condorcet.md)
- **This same Copeland-margin logic is offered as an optional *STAR* tiebreaker** — Equal Vote's [Condorcet Tiebreaker](../STAR_Voting/Tie_Breaking_STAR/condorcet_tiebreaker.md) runs a mini round-robin (most head-to-head wins → margin) among candidates STAR's own rounds left tied. Ranked Robin is this arithmetic as a *whole method*; there it is a *subroutine* firing only on an exact STAR tie.
- BetterVoting tabulation engine notes: [`tabulation_engines/BV/tabulation_engine/README.md`](../tabulation_engines/BV/tabulation_engine/README.md) (the `RankedRobin.ts` row: *"2-way tie → head-to-head; else random"*)
- [Glossary](../GLOSSARY.md)

# file: rr_tiebreak_lh_vs_bv.md
