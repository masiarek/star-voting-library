# STAR Tie-Breaking — The Full Chain

**One line:** ties don't get resolved by a coin flip first — they fall through a **fixed ladder** of deterministic tests (pairwise → five-star → …), and only if *every* rung is still tied does a pre-drawn **lot order** decide it. Most elections never reach the lot.

> **Read this first — everything on this page is the *tie* path.** It only runs when a round comes out **exactly tied**. The normal count has no pairwise-vs-score juggling: the **Scoring Round** just adds up the scores (top two advance), and the **Automatic Runoff** is just the head-to-head (the finalist more voters scored higher wins). The ladders below are what happens *only when* one of those two steps is a dead heat — and that context is exactly why each round then borrows the *other* round's measure (see ["Why the swap"](#the-ladder-both-rounds) below).

→ Builds on the **Automatic Runoff** and **Head-to-head / pairwise** glossary entries · cross-method: [Tie-Breaking: STAR vs. RCV-IRV](../../topics/ties/tiebreaking_star_vs_irv.md) (why strict ranks make ties *harder*, not easier) · JSON-side companion: [Tie-Breaking in BetterVoting JSON — Format & Mapping to YAML](tie_breaking_JSON.md) (format & mapping) · related: [How the Count Works — STAR vs RCV-IRV, Step by Step](../../topics/tabulation_star_vs_irv.md) · operational companions: the JSON→YAML converter ([`YAML_library/1_positive/01_convert_json_yaml.py`](../../../YAML_library/1_positive/01_convert_json_yaml.py)) and its tests ([`tests/test_lot_number_tiebreak.py`](../../../STARVote_LH_tabulation_engine/tests/test_lot_number_tiebreak.py)) · Level **301**.

---

## Why tie-breaking gets complicated fast

A STAR election has **two rounds** — a **Scoring Round** (pick the top two finalists) and an **Automatic Runoff** (the two finalists go head-to-head). A tie can happen in **either** round, and each round has its **own** ladder of tiebreakers. So a single election can break ties more than once, in two different places, by two different rules. (The worked example below does exactly that.)

The thing to hold onto: **the random "lot" order is the *last* resort, not the first.** Almost everything is settled by deterministic tests before the lot is ever consulted. The lot exists only so that a genuinely perfect tie still produces a single, *reproducible* winner instead of an error.

---

## The ladder (both rounds)

```
SCORING ROUND  — choose the two finalists
  0. Two highest total scores advance.
  └─ tie for the last finalist slot?
     1. PAIRWISE     — advance whoever is preferred in the most head-to-head matchups
     2. FIVE-STAR    — still tied? advance whoever has the most score-5 votes
     3. LOT ORDER    — still tied? the highest-priority lot number advances

AUTOMATIC RUNOFF  — choose the winner from the two finalists
  0. The finalist preferred head-to-head (more ballots scored higher) wins.
  └─ tie?
     1. SCORE        — the higher total score wins
     2. FIVE-STAR    — still tied? the most score-5 votes wins
     3. LOT ORDER    — still tied? the highest-priority lot number wins
```

Note the two ladders are **not** identical. In the Scoring Round, pairwise is the *first* tiebreaker; in the Runoff, total score is the first tiebreaker. Five-star is the second tiebreaker in both. The lot is the floor of both.

> **Why the swap — the elegant part.** Each round breaks its tie with the *other* round's yardstick, because **the measure that tied can't be the one that separates**. The Scoring Round ranks by *total score*, so a scoring-round tie means the scores are **equal** — score can't break it, so STAR asks the runoff's question instead: *whom do more voters prefer head-to-head?* (**pairwise**). The Runoff decides by *head-to-head preference*, so a runoff tie means the preference is **equal** — preference can't break it, so STAR falls back to the scoring round's measure: *who had the higher total score?* (**score**). (Put differently: pairwise *is* the runoff, so it can't also break the runoff; score *is* the scoring round, so it can't also break the scoring round.) Only after that shared **five-star** rung, and finally the **lot**.

"Five-star" means "votes of the maximum score" (5 on a 0–5 ballot). **Equal Support** in the output is not a candidate — it's the no-preference bucket (ballots that scored the two compared candidates the same), shown so the pairwise math adds up.

---

## Edge case: "five-star" is a *dead rung* when nobody scored the max

The five-star rung counts votes equal to the **scale maximum** — literally `score == 5` on a 0–5 ballot. (In the engine this is `_maximum_score_count_round`, which compares each score to `maximum_score`, the *option* — **not** the highest score any voter actually used.) Two consequences that surprise people:

1. **If none of the tied candidates earned a single 5, the rung is inert.** It still runs, and the report still prints it, but every count is `0`, so it can't separate anyone — the tie falls straight through to the **lot**.
2. **It's the scale's max, not the field's max.** On a 0–9 ballot (`maximum_score: 9`) the same rung becomes a *nine-star* count. A cautious electorate that tops out at 4s hands the rung nothing to weigh, so the ladder is effectively one rung shorter: pairwise/score → **lot**.

The same two ballots, capped a single point apart, decide the second finalist by two different rules — five-star in one, the lot in the other:

```
 FIVE-STAR PRESENT (a 5 exists)              NO FIVES (all scores ≤ 4)
   Alice,Ben,Cara                              Alice,Ben,Cara
   5,5,3                                        4,4,2
   5,1,3                                        4,0,2

 Ben & Cara tie 6–6; pairwise 1–1            Ben & Cara tie 4–4; pairwise 1–1
 Second tiebreaker — FIVE-STAR:              Second tiebreaker — FIVE-STAR:
   Ben  1  → advances (Second place)            Ben 0, Cara 0  → STILL TIED
                                              *** No lot numbers provided …
                                              [Tiebreaker: Lot Number Priority]
                                                Resolved: Ben (by lot / column order)
```

The **runoff** ladder does the same thing: when the two finalists are tied head-to-head **and** tied on total score, five-star is consulted — but if neither finalist earned a 5, it reads `0–0` and the **lot** decides. (Constructed cases: `Alice,Ben / 5,1 / 0,4` → five-star breaks it; `Alice,Ben / 4,0 / 0,4` → no fives, lot decides. Both verified against the engine.)

**Why it matters.** The "deterministic tests settle almost everything, the lot is rare" framing holds for typical elections, where leading candidates attract *some* 5s. But in **low-score / conservative-grading** contests — or real data compressed onto a coarse scale that never reaches the top — the five-star rung can quietly do nothing, and the **lot decides more often than the ladder's length suggests**. When you build or read a close example, check whether the tied candidates actually have max-score votes before crediting the outcome to five-star.

Mnemonic worth keeping: **"it counts fives, not fours"** — an equal or absent five-star count never steps down to the 4s, it drops to the lot. (akas for the term: broken / missing / empty / phantom rung.)

**The engine flags it.** When a tie falls all the way to the lot, the LH engine prints a `[Lot-decided tie — rare]` callout — the same spirit as the `[Divergence from STAR]` flag — so this uncommon "the ballots didn't decide, the lot did" event is named, not buried in the tiebreak trace.

Runnable cases (all verified in the test suite): [the dead-rung tie-break cases](../../../01_STAR/tie_break_dead_rung/) — five-star-breaks vs no-fives-→-lot, in both the scoring round and the runoff, including the **cap ladder** (the same tie at cap 4 / 3 / 2, all falling to the lot). Spin up more with the [dead-rung scenario generator](../../../STARVote_LH_tabulation_engine/tools_adam/generate_dead_rung_scenarios.md) (`--rung alive|dead|tied`, `--cap`, `--adversarial-lot`).

---

## Worked example — Ice Cream, 6 flavors (ties in *both* rounds)

Two ballots, six flavors. This is the canonical "it tied twice" case — and, importantly, **the lot order is never reached**; deterministic tests settle everything. It is now a **live, BV-backed case:** **[Ice cream ladder — BV2180, `fp62p2`](../../../01_STAR/tie_break_ladder/bv2180_fp62p2_ice_cream_ladder.md)** ([results ↗](https://bettervoting.com/fp62p2/results)) — LH and BetterVoting agree, precisely because no random rung is reached.

```
Ballots:
Chocolate,Chocolate Chip,Fudge Brownie,Vanilla,Strawberry,Mango
        4,             5,            4,      1,         2,    -
        1,             0,            0,      4,         5,    4

Tabulation:
        
[Scoring Round]  The two highest-scoring candidates advance.
   Strawberry     -- 7 -- First place
   Chocolate      -- 5 -- Tied for second place
   Chocolate Chip -- 5 -- Tied for second place
   Vanilla        -- 5 -- Tied for second place
   Fudge Brownie  -- 4
   Mango          -- 4
   → Strawberry advances; three-way tie for second.

[Scoring Round: First tiebreaker]  Most head-to-head matchups (PAIRWISE).
   Chocolate      -- 2
   Chocolate Chip -- 2
   Vanilla        -- 2
   → still a three-way tie.

[Scoring Round: Second tiebreaker]  Most score-5 votes (FIVE-STAR).
   Chocolate Chip -- 1 -- Second place
   Chocolate      -- 0
   Vanilla        -- 0
   → Chocolate Chip advances. Finalists: Strawberry, Chocolate Chip.

[Automatic Runoff Round]  Preferred head-to-head wins.
   Chocolate Chip -- 1 -- Tied for first
   Strawberry     -- 1 -- Tied for first
   → two-way tie for first.

[Automatic Runoff Round: First tiebreaker]  Highest total score (SCORE).
   Strawberry     -- 7 -- First place
   Chocolate Chip -- 5
   → Strawberry wins.
```

So this election tied **twice** — a three-way tie for the second finalist slot, then a two-way tie in the runoff — and resolved both *without* the lot: five-star settled the first, total score settled the second. The file's `lot_numbers:` was present (carried over from BetterVoting) but **never consulted**. That is the normal case.

The lot only decides when pairwise **and** score **and** five-star are *all* tied — e.g. a perfect symmetric election.

---

## The lot order (the floor of both ladders)

When the ladder bottoms out, the engine consults a **lot order**: a list of candidates in **priority order, highest first**. The tied candidate that appears *earliest* in the list wins. (In code this is the `LotNumberTiebreaker`; `index 0 = highest priority = wins ties`.)

This mirrors how real STAR elections handle a true tie: officials draw a random order **once**, publish it, and use it for any tie that arises. Publishing it up front is what makes the result **reproducible and auditable** — anyone can re-run the count and get the same winner.

---

## Where the order comes from (imported elections)

For elections imported from BetterVoting, the lot order isn't ours to draw — BetterVoting pre-draws it and ships it in the export, and the converter carries it into the YAML's `lot_numbers:` so our re-tabulation reproduces their official winner. The export records it as `Results[].perm` (or per-candidate `tieBreakOrder`), the converter translates those UUIDs to our `cand_id`s, and a generated file ends up with a line like:

```yaml
lot_numbers: [Strawberry, Fudge Brownie, Mango, Chocolate Chip, Vanilla, Chocolate]
```

The exact JSON fields, the field-by-field mapping, the fallbacks, and the worked Ice Cream mapping are in the companion page: **[Tie-Breaking in BetterVoting JSON — Format & Mapping to YAML](tie_breaking_JSON.md)**.

---

## What you may set in a hand-written YAML

`lot_numbers:` is **optional**. Two cases:

**You provide it.** Write an inline list of `cand_id`s in priority order, highest first:

```yaml
lot_numbers: [Strawberry, Fudge Brownie, Mango, Chocolate Chip, Vanilla, Chocolate]
```

- Entries must be existing `cand_id`s — i.e. the names in the ballot header.
- Only the relative order among the *tied* candidates matters, but listing **all** candidates is the clear, safe habit (and matches what the converter writes).
- It can sit at the **race** level (normal) or the **election** level; the race value wins if both are present.

**You omit it.** The engine **assumes the CSV ballot-column order** as the lot priority — i.e. left-to-right, so the **first column wins** a pure lot tie. This is a deliberate, deterministic fallback, not randomness.

### When to set it vs. omit it

| Situation | Recommendation |
|---|---|
| Imported real election (BetterVoting) | **Always carry the provider's order.** The converter does this automatically — don't hand-edit it. Reproducibility/audit depends on it. |
| Hand-written teaching demo | **Usually omit.** Keep the example small enough that ties resolve before the lot (the Ice Cream case), or accept column order as the tiebreak. |
| Demo that *shows* a lot-decided tie | **Set it explicitly**, so the lesson is pinned and obvious (a symmetric tie where only the lot can decide). |

The practical upshot: for most hand-built examples you never write `lot_numbers` at all, because well-chosen small ballots either avoid a lot tie or the column-order fallback is exactly what you want.

---

## Quick rules

- **Lot order is last.** Pairwise / score / five-star resolve almost everything first. Don't reach for `lot_numbers` to explain a winner unless the output literally shows a lot tiebreaker firing.
- **Index 0 wins.** Earliest in `lot_numbers` (or leftmost ballot column, if omitted) = highest priority = wins the tie.
- **Two rounds, two ladders.** Scoring Round: pairwise → five-star → lot. Runoff: score → five-star → lot. An election can break ties in both.
- **Five-star needs actual 5s.** That rung counts votes of the *scale maximum* (5). If no tied candidate earned one, it reads 0–0 and the tie drops to the lot — common in low-score elections. See "dead rung" above.
- **Imported files carry the order; hand-written files usually don't need to.**
- **`-` / blank = 0.** A blank or marker cell counts as score 0 (no support); it doesn't affect the tiebreak ladder beyond its zero contribution.

---

## LH vs BetterVoting — where the two STAR ladders differ

The ladder above is the **LH** ladder. BetterVoting follows its own [official protocol](https://docs.bettervoting.com/help/ties.html), and for **most** elections the two agree — they only part on a genuinely tied race, and even then only at two rungs. It's worth pinning down, because it decides whether a tie case can be cross-checked against a live BetterVoting election or is **LH-only**.

| Rung | **LH** `starvote_larry_hastings.py` | **BetterVoting** `Star.ts` / [ties protocol](https://docs.bettervoting.com/help/ties.html) |
|---|---|---|
| Scoring 1 | head-to-head **among the tied set** (any N) | head-to-head **only if exactly 2 are tied**; a 3+ way tie **skips** it |
| Scoring 2 | most **five-star** votes | most **five-star** votes |
| Scoring 3 (floor) | **lot order** (pre-published) — *deterministic* | **random** shuffle — *non-deterministic* |
| Runoff 1 | higher total **score** | higher total **score** |
| Runoff 2 | most **five-star** votes | most **five-star** votes |
| Runoff 3 (floor) | **lot order** — *deterministic* | **random** shuffle — *non-deterministic* |

Two consequences:

1. **The 3+ way scoring tie.** LH runs a head-to-head *among the tied set* before five-star; BetterVoting's protocol **deliberately skips** head-to-head once more than two candidates are tied and goes straight to five-star. This is **working-as-intended on BetterVoting's side** — a deliberate complexity/ability trade-off, [confirmed on #1379](https://github.com/Equal-Vote/bettervoting/issues/1379). (Often the extra LH rung changes nothing, because a symmetric dead heat ties head-to-head too.)
2. **The floor is different.** LH bottoms out at a **published lot** (reproducible from the ballots plus that order); BetterVoting bottoms out at a **random** shuffle. So when a race ties all the way down, **only the LH winner is a function of the ballots** — BetterVoting's is a coin toss that can't be frozen into a `_bv_export.json`.

**Practical upshot — the same rule as the Ranked Robin analog:** a case that *turns on the terminal tiebreak* is **LH-only** — state which engine's rule you're relying on, pin `lot_numbers`, and use the LH tally for a reproducible winner. The worked STAR example is **[Flat scores 05 — the 3-way scoring tie (BV555, `xmyf7k`)](../../../01_STAR/Flat_scores_ties/Flat_scores_ties_05_scoring_tie_3way_xmyf7k.md)**: every score-based rung ties, LH's lot elects **A**, BetterVoting's random shuffle picked **C** — same ballots, and BV's result isn't reproducible. The Ranked Robin version of exactly this story (deterministic margin→lot vs BV's random) is **[rr_tiebreak_lh_vs_bv.md](../../RCV_Ranked_Robin/rr_tiebreak_lh_vs_bv.md)**.

Separately, BetterVoting doesn't yet *show* which rung fired in its human-readable report or JSON export (the data exists internally as `roundResults.logs` + `tieBreakType`); surfacing it is tracked in **[#1432](https://github.com/Equal-Vote/bettervoting/issues/1432)** (building on the JSON-v2 export in [PR #1419](https://github.com/Equal-Vote/bettervoting/pull/1419)), with a pre-published lot (vs random floor) tracked in **[#1063](https://github.com/Equal-Vote/bettervoting/issues/1063)**.

---

## See also

- **BetterVoting's official tie-breaking protocol** (BetterVoting's own ladder — the source of the "shuffle the candidates" random order our `lot_numbers` carries, and *close but not identical* to the LH ladder above; see the divergence section just above): <https://docs.bettervoting.com/help/ties.html>
- Glossary: **Tiebreaker**, **Head-to-head / pairwise**, **Automatic runoff**, **Equal Support** — [Glossary — voting methods & criteria](../../GLOSSARY.md)
- Equal-score handling in the runoff: ["Aren't Equal-Score Votes Just Discounted?"](../are_equal_score_votes_discounted.md) · demo [`equal_support_runoff_demo.yaml`](../../../01_STAR/_main/equal_support_runoff_demo.yaml)
- Converter + engine wiring and the full test matrix (perm, `tieBreakOrder`, no-sequence, manual override, column-order fallback, and the non-vacuous self-check): [`tests/test_lot_number_tiebreak.py`](../../../STARVote_LH_tabulation_engine/tests/test_lot_number_tiebreak.py)
