# BV2270 — the rung the engine was missing

<!-- case-meta:start — managed by build_yaml_pages.py; edit the YAML, not these lines -->
**Method:** [Ranked Robin (RCV-RR / Copeland)](../../01_Learn/README.md) · **1 seat** · **Expected winner:** Alder · [full count →](cases/cases_pages/bv2270_8h4bvh_head_to_head_vs_margin.md)
<!-- case-meta:end -->

**Level: 301 · deep dive**

*Every other case in this folder ties all the way to the bottom of the ladder, where LH draws a published lot and BetterVoting draws a seeded shuffle. This one stops on the **middle** rung — and for two years the two engines stopped there with different answers. Nine ballots, a two-way Copeland tie, no lot on either side: BetterVoting elected Alder on the head-to-head, this engine elected Birch on total margin. Both were derivable from the ballots; only one was the method's own rule. Ranked Robin's [1st Degree tiebreaker](degrees_of_ties.md) asks for each finalist's margins **over the other finalists**, and with two finalists that is their head-to-head — so BetterVoting had it right, and the engine was corrected on 2026-08-19. Both now elect **Alder**.*

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/8h4bvh) · **[results ↗](https://bettervoting.com/8h4bvh/results)** (election `8h4bvh`).

## The election

Nine voters rank four trees for a street-planting commission.

```
4 × Alder   > Birch   > Cedar   > Dogwood
3 × Dogwood > Cedar   > Birch   > Alder
1 × Birch   > Cedar   > Dogwood > Alder
1 × Dogwood > Alder   > Birch   > Cedar
```

Six matchups, every one of them decisive:

| Match | Result |
|---|---|
| Alder v Birch | **Alder** 5 – 4 |
| Alder v Cedar | **Alder** 5 – 4 |
| Alder v Dogwood | **Dogwood** 5 – 4 |
| Birch v Cedar | **Birch** 6 – 3 |
| Birch v Dogwood | **Birch** 5 – 4 |
| Cedar v Dogwood | **Cedar** 5 – 4 |

| | W–L | Copeland | Margin | Beats |
|---|:---:|:---:|:---:|---|
| **Birch** | 2–1 | **2** | **+3** | Cedar, Dogwood |
| **Alder** | 2–1 | **2** | **+1** | Birch, Cedar |
| Dogwood | 1–2 | 1 | −1 | Alder |
| Cedar | 1–2 | 1 | −3 | Dogwood |

Alder and Birch tie at the top on two wins each. Nothing in the Copeland column separates them, so both engines go to their next rung — and their next rungs are different questions.

## Two questions, and the order they go in

| | The question | Answer here | Elects |
|---|---|---|---|
| **1st Degree** — the protocol's first rung, and BetterVoting's only one | *Who won when these two played each other?* | Alder beat Birch **5 – 4** | **Alder** |
| **2nd Degree** — reached only if the finalists are level against each other | *Who won by more, across all their matches?* | Birch **+3** vs Alder **+1** | Birch, if it were reached |

The engine used to ask the second question first, which is the whole of the bug: it had no finalists-only rung at all.

Both are readings of "strongest", and that is why the disagreement looked respectable for so long. Total margin asks how a candidate did against the **whole field**; the head-to-head asks the narrower question of what happened in the one match that is actually between the two of them. Birch's +3 is built on a 6–3 thrashing of Cedar — a win Alder never had the chance to match — while Alder's claim is that when the two tied candidates met, Alder won. The method settles it: the narrow question comes first, and the wide one is held in reserve for finalists the narrow question cannot separate.

[The dead-heat case](dead_heat_lot_tiebreak.md) is where the ladders still genuinely part: there both degrees are exhausted and each engine falls through to its own rung of last resort — a published lot on one side, a seeded shuffle on the other — which is why it stays LH-only. Here **neither engine reaches for a lot**; both stop with a computed answer, and since the correction it is the same answer.

**This was not the first live case of the disagreement** — [BV2176, the Post-it RCV example](../../../method_comparisons/postit_rcv_example/bv2176_p8dp28_postit_rcv_example.md), got there first, with Green (BV) against Blue (LH) inside a genuine three-way cycle, and it too now resolves to Green on both sides. What BV2270 adds is that it is **purpose-built and minimal**: four candidates, nine ballots, six matchups you can check by hand in a minute, and no other moving part. It was built to display a divergence, and it ended up being the case that proved which side of it was wrong.

## What the neutral third engine says

The repo's rule for Ranked Robin is to check every case three ways, and the third leg is the one nobody here wrote — [`pref_voting`](../../../STARVote_LH_tabulation_engine/tools_adam/pref_voting_tabulation_engine/ranked_robin_report.py)'s independent Copeland:

```
 pref_voting Copeland leader(s): Alder, Birch
 cross-check vs Ranked Robin winner (Alder): CONSISTENT ✓  (LH tie-broke within pref_voting's 2-way Copeland-leader set)
```

It reproduces the tally exactly, reports the **whole leader set**, and declines to pick. That is the honest position for a library that implements the tally and not the tiebreak — and it is what made the case readable while the engines disagreed: they never disagreed about the count. They agreed on all six matchups, on both Copeland scores and on every margin. What they disagreed about was **the rule for what to do next**, which no amount of re-counting could settle. Reading the method's published protocol did.

## Nobody actually wins here

Worth saying plainly, because the win–loss table hides it: this field is a **[Condorcet cycle](../../01_Learn/cycle_resolution.md)**. Alder beats Birch, Birch beats Dogwood, Dogwood beats Alder. There is no [Condorcet winner](../../../07_Concepts/topics/condorcet/README.md), and the [Smith set](../../../07_Concepts/topics/smith_set.md) is **all four candidates** — even Cedar, sitting last on the Copeland table, belongs to the smallest group that beats everyone outside it, because there is no outside.

So the top two rows of the record understate the contention. Ranked Robin is Smith-efficient, so whichever of Alder or Birch is picked is inside the set and the method has done its job; but "who *should* win a cycle" is exactly the question [Minimax, Ranked Pairs and Schulze answer differently](../../01_Learn/cycle_resolution.md), and a tiebreak rung is a very thin place to be answering it — which is an argument about Ranked Robin itself, not about which rung comes first.

(The count embedded below is the lead section only. The engine's Smith-set analysis is one click away, in the folded audit on the [full page](cases/cases_pages/bv2270_8h4bvh_head_to_head_vs_margin.md).)

## Why this election exists — and a warning about its results page

BV2270 was minted to demonstrate a **display** defect in BetterVoting, reported as [bettervoting#1480](https://github.com/Equal-Vote/bettervoting/issues/1480). The results page highlights winners by **row position**, but the winner comes from the ladder — and here those disagree:

<img alt="BetterVoting results for BV2270: the heading reads 'Alder wins!' while the star in the bar chart sits on Birch, both at 67%" src="img/8h4bvh_result.png" width="640">

<img alt="BV2270 detailed results table: the gold-highlighted row is Birch, but the winner is Alder" src="img/8h4bvh_race_details.png" width="640">

**Do not read the star as BetterVoting's answer.** BV's answer is **Alder** — stated in the heading and in the export's `elected` — and the star on Birch is the bug. The candidate rows are sorted by Copeland score and then by BV's `tieBreakOrder`, a shuffle seeded from the ballot count and the race id ([BV2261](bv2261_y2fbpc_tiebreak_recorded.md) is the case that pins down how that works). Here it drew `Cedar 0, Birch 1, Dogwood 2, Alder 3`, so Birch landed in row 0 and collected a decoration meant for the winner.

That the shuffle appears at all is worth being careful about: `tieBreakType` in this export is **`none`**. No random rung fired. The shuffle is only ever deciding *display order* in this election — it has no bearing on who won under either engine.

Two things fall out of that, both useful:

- The three `Dogwood>Cedar>Birch>Alder` ballots are **mirror images** of three of the `Alder>Birch>Cedar>Dogwood` ballots. They were cast on the live election to re-roll the display shuffle, which re-seeds on every vote by design. A ranking and its exact reverse cancel on all six matchups, so the tally you see above is identical to the three-ballot original — every margin, every Copeland score and both engines' winners unchanged. It is a clean way to re-roll a 50/50 draw without touching the election.
- The sibling defect — the Ranked Robin results page starring only **one** winner in a multi-winner race — is [bettervoting#1166](https://github.com/Equal-Vote/bettervoting/issues/1166), fixed in [PR #1479](https://github.com/Equal-Vote/bettervoting/pull/1479).

## The full count

<!-- report:bv2270_8h4bvh_head_to_head_vs_margin -->
```text
--- Ranked Robin (RCV-RR / Copeland) Method (single winner) ---
 Tabulating 9 ballots (ranked ballots).

Ballots:
     4 × Alder > Birch > Cedar > Dogwood
     3 × Dogwood > Cedar > Birch > Alder
     1 × Birch > Cedar > Dogwood > Alder
     1 × Dogwood > Alder > Birch > Cedar

Round-Robin — every pair, head-to-head (For – Against):
   Alder    beats Birch     5 – 4
   Alder    beats Cedar     5 – 4
   Dogwood  beats Alder     5 – 4
   Birch    beats Cedar     6 – 3
   Birch    beats Dogwood   5 – 4
   Cedar    beats Dogwood   5 – 4

--- Pairwise (Round-Robin) Matrix ---
Head-to-head / pairwise comparison — the Ranked Robin tally
Legend: For - Equal Support - Against   (row vs column)
            |   Alder   |  Birch   |  Cedar   | Dogwood  |
----------------------------------------------------------
    Alder > |    ---    |5 - 0 - 4 |5 - 0 - 4 |4 - 0 - 5 |
    Birch > | 4 - 0 - 5 |   ---    |6 - 0 - 3 |5 - 0 - 4 |
    Cedar > | 4 - 0 - 5 |3 - 0 - 6 |   ---    |5 - 0 - 4 |
  Dogwood > | 5 - 0 - 4 |4 - 0 - 5 |4 - 0 - 5 |   ---    |

Win–loss record — Copeland score = wins + ½·ties (highest score wins; ties broken by the Ranked Robin degrees, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  vs finalists  Beats
    1  Alder      2–1–0         2      +1            +1  Birch, Cedar
    2  Birch      2–1–0         2      +3            -1  Cedar, Dogwood
    3  Cedar      1–2–0         1      -3             —  Dogwood
    4  Dogwood    1–2–0         1      -1             —  Alder

Winner — Ranked Robin (RCV-RR): Alder
   *** 2 candidates tie for the most wins (Alder, Birch) — tied on the tally, not a cycle (some of them beat others head-to-head, but no loop closes). Resolved by the 1st Degree tiebreaker: Alder has the greatest sum of win margins over the other finalists (+1).
```
<!-- /report -->

→ page: [`bv2270_8h4bvh_head_to_head_vs_margin.md`](cases/cases_pages/bv2270_8h4bvh_head_to_head_vs_margin.md) · src: [`.yaml`](cases/bv2270_8h4bvh_head_to_head_vs_margin.yaml) · frozen: [`_bv_export.json`](cases/bv2270_8h4bvh_head_to_head_vs_margin_bv_export.json)

**See also:** [Ranked Robin tie-breaks — LH vs BetterVoting](../../01_Learn/rr_tiebreak_lh_vs_bv.md) · [the folder index](README.md) · [BV2261 — the tiebreak is recorded](bv2261_y2fbpc_tiebreak_recorded.md)

# file: bv2270_8h4bvh_head_to_head_vs_margin.md
