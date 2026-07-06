# Dead heat — Ranked Robin runs the whole tiebreak ladder (LH-only)

*Four score ballots, three candidates, engineered so **every** deterministic rung ties. Ada and Ben tie each other head-to-head **and** tie on total margin, and both beat Cara — so Ranked Robin walks its full ladder (most wins → total margin → **lot order**) and only the pre-published lot settles it. This is the one case in the set that exercises the **Equal Support** column and the **+½ Copeland** credit — and the one case that is **LH-only on purpose**, because it's exactly where the LH and BetterVoting tiebreaks diverge.*

Reference: [`dead_heat_lot_tiebreak.yaml`](dead_heat_lot_tiebreak.yaml) (`expected_winners: [Ada]`). No BetterVoting election — see "Why LH-only" below.

## The ballots

Score ballots (0–5). Two voters are **indifferent** between Ada and Ben (both 5) — that indifference is *Equal Support*, no head-to-head preference:

```text
Ada,Ben,Cara
5,5,0     ← Ada = Ben (Equal Support), both over Cara
5,5,0     ← Ada = Ben (Equal Support), both over Cara
4,3,1     ← Ada > Ben > Cara
3,4,1     ← Ben > Ada > Cara
```

## The tabulation (LH native)

Full report in the [`_tabulated` mirror](rr_tiebreaks_tabulated/dead_heat_lot_tiebreak_tabulated.txt):

```text
Round-Robin — every pair, head-to-head (For – Against):
   Ada   ties  Ben    1 – 1
   Ada   beats Cara   4 – 0
   Ben   beats Cara   4 – 0

--- Pairwise (Round-Robin) Matrix ---
Legend: For - Equal Support - Against   (row vs column)
         |    Ada    |   Ben    |  Cara    |
--------------------------------------------
   Ada > |    ---    |1 - 2 - 1 |4 - 0 - 0 |
   Ben > | 1 - 2 - 1 |   ---    |4 - 0 - 0 |
  Cara > | 0 - 0 - 4 |0 - 0 - 4 |   ---    |

Win–loss record — Copeland score = wins + ½·ties (most wins wins; ties broken by total margin, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  Ada        1–0–1       1.5      +4  Cara
    2  Ben        1–0–1       1.5      +4  Cara
    3  Cara       0–2–0         0      -8  —

Winner — Ranked Robin (RCV-RR): Ada
```

Read the Ada↔Ben cell: **`1 - 2 - 1`** — one voter each way, and **2 Equal Support** (the indifferent voters). For equals Against, so it's a **tie**, worth **½** to each in Copeland (1 win over Cara + ½ = **1.5**). Ada and Ben are identical on wins (1) *and* on margin (+4), so only the pre-published **lot `[Ada, Ben, Cara]`** breaks it → **Ada**.

This is the only case that lights up the Equal Support column and the ½-Copeland credit, and the only one that reaches the **lot** rung — the full deterministic ladder in four ballots.

## Why LH-only (the divergence)

The LH engine and BetterVoting resolve this **differently**, which is the whole reason there's no BV election here:

| | Tiebreak ladder |
|---|---|
| **LH** `run_ranked_robin` | most wins → total **margin** → **lot order** — fully deterministic |
| **BetterVoting** `RankedRobin.ts` | most wins → **head-to-head** (2-way only) → **random** |

Here the two leaders tie *each other* head-to-head, so BV's 2-way rule can't resolve them and it falls through to a **random** pick — which can't be frozen into a reproducible `_bv_export.json`. So this case documents the **LH** ladder specifically; BetterVoting would agree that Ada and Ben are co-leaders but would not deterministically choose between them. Full write-up: [rr_tiebreak_lh_vs_bv.md](../../00_start_here/RCV_Ranked_Robin/rr_tiebreak_lh_vs_bv.md).

### Engine wording

The winner note distinguishes a dead heat from a real cycle:

```text
*** 2 candidates tie for the most wins (Ada, Ben) — a dead heat (they draw head-to-head, not a cycle). Resolved by total margin, then lot order.
```

Ada and Ben both *beat* Cara and *tie* each other (no beat-around-the-loop), so the engine says **dead heat**, not "Condorcet cycle" — the latter is reserved for a genuine directed loop (rock-paper-scissors). See [rr_tiebreak_lh_vs_bv.md](../../00_start_here/RCV_Ranked_Robin/rr_tiebreak_lh_vs_bv.md).

## See also

- Folder overview: [rr_tiebreaks — README](README.md)
- The agreement counterpart (a clean Condorcet winner, all three engines agree): [BV2131 — Tennessee](../rr_vs_irv_plurality/bv2131_tennessee_condorcet_center_vqyqkr.md)
- Cycle resolution in depth: [cycle_resolution.md](../../00_start_here/RCV_Ranked_Robin/cycle_resolution.md)
