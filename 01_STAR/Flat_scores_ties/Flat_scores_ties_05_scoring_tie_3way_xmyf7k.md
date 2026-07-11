# Flat scores 05 — scoring-round 3-way tie (BV555, xmyf7k)

> 🔀 **A documented divergence — deterministic vs random, not a bug.** Three candidates tie at the top of the scoring round and **every score-based tiebreaker stays tied**, so the winner turns entirely on the **terminal tiebreak** — and that is the one rung where LH and BetterVoting genuinely differ: **LH breaks it with a pre-published lot order** (deterministic → advances **A, B**, elects **A**); **BetterVoting breaks it with a random shuffle** (that run: **C, A** → **C**). Same ballots, two published rules, and BV's is **not reproducible**. This is the STAR analog of the Ranked Robin dead-heat case — see [rr_tiebreak_lh_vs_bv.md](../../00_start_here/RCV_Ranked_Robin/rr_tiebreak_lh_vs_bv.md).

> ⚠️ **LH-only / not freezable.** Because BV's terminal tiebreak is random, there is **no stable BV result to record** — so this case has **no `_bv_export.json`** and documents the **LH** ladder specifically. (`xmyf7k` exists on BetterVoting, but its displayed winner can change between runs.)

**Level 201/301.** This is the cleanest possible test of "does your tabulator break a fully-tied race *deterministically*, and does it *show its work*?" The LH reference answer, with the published lot order `[A, B, C, D, E]`, is **A**.

## The two ladders (STAR scoring round)

Both engines agree A, B, C tie at 10 and both stay tied through the 5-star count. They differ only in **how the tie is finally broken**:

| Rung | **LH** `starvote_larry_hastings.py` | **BetterVoting** `Star.ts` / [ties protocol](https://docs.bettervoting.com/help/ties.html) |
|---|---|---|
| 1 | head-to-head **among the tied set** | head-to-head **only if exactly 2 are tied** |
| 2 | most **5-star** ratings | most **5-star** ratings (for 3+ tied, or a h2h tie) |
| 3 | **lot order** (pre-published `lot_numbers`) | **random** shuffle |

**LH is deterministic at every rung.** **BetterVoting is deterministic only for a clean 2-way tie its head-to-head resolves** — a 3+ way tie (this case) deliberately skips head-to-head and, when 5-star also ties, falls through to **random**. That skip is **working-as-intended**, [confirmed on #1379](https://github.com/Equal-Vote/bettervoting/issues/1379) (closing as WAI); LH's rung-1 head-to-head is a **no-op here anyway** (no preference among A/B/C), so what actually separates the two winners is rung 3: **lot vs random**.

## The ballots (2 voters)

```
A, B, C, D, E
5, 5, 5, 4, 4
5, 5, 5, 4, 4
```

Source: [`Flat_scores_ties_05_scoring_tie_3way_xmyf7k.yaml`](Flat_scores_ties_05_scoring_tie_3way_xmyf7k.yaml) · BV: <https://bettervoting.com/xmyf7k/results>.

## Where the two engines diverge

| | LH engine (reference) | BetterVoting (`xmyf7k`) |
|---|---|---|
| Scoring-round tie | A, B, C tied at 10 | A, B, C tied at 10 |
| Head-to-head among tied | applied — **no-op** (all 0) | **skipped** (3-way, per protocol) |
| 5-star count | A 2 = B 2 = C 2 → tied | A 2 = B 2 = C 2 → tied |
| Terminal tiebreak | **lot order** → A, B | **random shuffle** → C, A (that run) |
| Runoff | A vs B → tie → lot → **A** | C vs A → **C** |
| **Winner** | **A** (reproducible) | **random** (was C) |
| Tie-break shown? | **yes — every step printed** | **no explanation in the export** |

Both engines see the same three-way tie. The winners differ **not** because one is wrong on the logic — BV's protocol is deliberate and documented — but because LH resolves the dead heat from a **published lot** while BV resolves it at **random**. Only the LH result is a function of the ballots plus a published order.

## View 1 — BetterVoting (`xmyf7k`)

BV advances two finalists and elects a winner **without showing how the tie was broken**. Because the terminal tiebreak is random, the displayed winner is not stable between runs.

> 📷 _Paste the BetterVoting `xmyf7k` result screenshot here. Keep the filename suffix `_xmyf7k`._

## View 2 — the LH engine (reference)

```
Scoring Round
   A             -- 10 -- Tied for first place
   B             -- 10 -- Tied for first place
   C             -- 10 -- Tied for first place
   D             --  8
   E             --  8
 There's a three-way tie for first.

 First tiebreaker (head-to-head):  A 0 = B 0 = C 0  (Equal Support 2)  → still tied
 Second tiebreaker (most 5s):      A 2 = B 2 = C 2                     → still tied
 [Lot Number Priority] Tie among ['A','B','C'] → Resolved ['A','B'].

Automatic Runoff Round
   A             -- 0 -- Tied for first place
   B             -- 0 -- Tied for first place
   Equal Support -- 2
 There's a two-way tie for first.

 First tiebreaker (highest score):  A 10 = B 10  → still tied
 Second tiebreaker (most 5s):       A  2 = B  2  → still tied
 [Lot Number Priority] Tie among ['A','B'] → Resolved ['A'].

Winner: A
```

Full audit copy: [`_tabulated`](Flat_scores_ties_tabulated/Flat_scores_ties_05_scoring_tie_3way_xmyf7k_tabulated.txt).

## The two open threads on BetterVoting

The tie-break **logic** question is settled — WAI — so what remains is not "fix the winner" but two orthogonal asks:

- **Transparency** — surface the tie-break steps in BV's human-readable report and JSON. BV already builds them internally (`roundResults.logs` + `tieBreakType` in `Star.ts`); the ask is to expose them. Tracked in **[#1432](https://github.com/Equal-Vote/bettervoting/issues/1432)**, which builds on the JSON-v2 export in **[PR #1419](https://github.com/Equal-Vote/bettervoting/pull/1419)**. (The earlier export-of-the-tie-break-sequence work landed in [#1371](https://github.com/Equal-Vote/bettervoting/issues/1371), now closed.)
- **Pre-published lot** — a body-established lot order instead of a post-hoc random shuffle, so a fully-tied race is reproducible across engines. Tracked in **[#1063](https://github.com/Equal-Vote/bettervoting/issues/1063)**.

→ the cascade: [STAR Tie-Breaking](../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md) · [reporting true ties](../../00_start_here/STAR_reporting/reporting_ties.md) · the RR analog: [rr_tiebreak_lh_vs_bv.md](../../00_start_here/RCV_Ranked_Robin/rr_tiebreak_lh_vs_bv.md) · [Flat scores, ties & tie-breaking (all cases)](README.md).

## The takeaway

When every score-based tiebreaker ties, the only thing that lets two independent systems agree is a **shared, deterministic tie-break order**. LH publishes its lot order and prints every step, so its winner (**A**) is reproducible from the ballots plus that order. BetterVoting's protocol is a deliberate, documented compromise — but it resolves this fully-tied case at **random**, so its winner isn't a function of the ballots and **can't be frozen**. That is why this case is **LH-only**. The productive asks are transparency ([#1432](https://github.com/Equal-Vote/bettervoting/issues/1432) / [PR #1419](https://github.com/Equal-Vote/bettervoting/pull/1419)) and a pre-published lot ([#1063](https://github.com/Equal-Vote/bettervoting/issues/1063)) — not a winner "fix."
