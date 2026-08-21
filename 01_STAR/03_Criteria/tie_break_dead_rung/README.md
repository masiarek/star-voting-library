# The "dead rung" — when STAR's five-star tiebreaker can't fire

*A dozen tiny constructed elections — plus real BetterVoting races that hit the same thing — isolating one fact: STAR's **five-star** tiebreaker counts votes equal to the **scale maximum (5)**. If none of the tied candidates earned a 5, the rung reads `0–0` and the tie falls through to the **lot** — in **both** rounds.*

Backs the "dead rung" section of the canonical [STAR Tie-Breaking — The Full Chain](../../01_Learn/Tie_Breaking_STAR/tie_breaking.md) (Level 301). Run any file:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py \
  01_STAR/03_Criteria/tie_break_dead_rung/cases/tie_break_01_scoring_five_star_breaks.yaml
```

## The two ladders (recap)

```
SCORING ROUND  finalists:  pairwise → five-star → lot
AUTOMATIC RUNOFF winner:    score    → five-star → lot
```

"Five-star" = votes of score **5** (the scale max), regardless of whether any voter actually used a 5. That's the pivot these four cases turn on.

## The four cases

| File | Round | 5 present? | Second rung (five-star) | Decided by | Winner |
|---|---|:--:|---|---|---|
| [`tie_break_01_scoring_five_star_breaks`](cases/cases_pages/tie_break_01_scoring_five_star_breaks.md) | Scoring | yes | Ben 1, Cara 0 → Ben advances | **five-star** | Alice |
| [`tie_break_02_scoring_no_fives_to_lot`](cases/cases_pages/tie_break_02_scoring_no_fives_to_lot.md)  | Scoring | no  | Ben 0, Cara 0 → still tied | **lot** | Alice |
| [`tie_break_03_runoff_no_fives_to_lot`](cases/cases_pages/tie_break_03_runoff_no_fives_to_lot.md)   | Runoff  | no  | Alice 0, Ben 0 → still tied | **lot** | Alice |
| [`tie_break_04_runoff_five_star_breaks`](cases/cases_pages/tie_break_04_runoff_five_star_breaks.md)  | Runoff  | yes | Alice 1, Ben 0 → Alice wins | **five-star** | Alice |

Cases 01/02 are the **same** tie shape one point apart (5s vs capped at 4); 03/04 likewise. Note the eventual **winner is Alice in all four** — the point isn't who wins these toy races, it's **which rung decides**. In a closer election that difference chooses the winner (see the scale-granularity case in [Scale granularity can flip the winner (a 301 case)](../../../07_Concepts/scores_and_ranks/scale_granularity_flips_the_winner.md)).

## The adversarial set (05–09): the rung must CHANGE the winner

Cases 01–04 teach, but they can't *catch a regression*: Alice wins whether or not the engine consults five-star. Cases 05–09 close that hole — each sets `lot_numbers:` to favor the **wrong** candidate, so the expected winner is only elected if the ladder runs in the right order. If the engine ever skipped a rung (or consulted the lot early), these tests fail.

| File | Round | Rung state | Lot favors | Winner proves |
|---|---|---|---|---|
| [`tie_break_05_scoring_five_star_vs_adversarial_lot`](cases/cases_pages/tie_break_05_scoring_five_star_vs_adversarial_lot.md) | Scoring | alive (Ben 2, Cara 1) | Cara | **Ben** — five-star outranks the lot; Ben then wins the runoff |
| [`tie_break_06_scoring_dead_rung_adversarial_lot`](cases/cases_pages/tie_break_06_scoring_dead_rung_adversarial_lot.md) | Scoring | dead (all ≤ 4) | Cara | **Ann** — lot advances Cara, who loses the runoff to Ann |
| [`tie_break_07_runoff_five_star_vs_adversarial_lot`](cases/cases_pages/tie_break_07_runoff_five_star_vs_adversarial_lot.md) | Runoff | alive (Ann 1, Ben 0) | Ben | **Ann** — five-star outranks the lot |
| [`tie_break_08_runoff_dead_rung_adversarial_lot`](cases/cases_pages/tie_break_08_runoff_dead_rung_adversarial_lot.md) | Runoff | dead (both top out at 4) | Ben | **Ben** — the lot, not column order, resolves it |
| [`tie_break_09_five_star_tied_nonzero`](cases/cases_pages/tie_break_09_five_star_tied_nonzero.md) | Runoff | alive but **non-separating** (one 5 each) | Ben | **Ben** — a rung can run, count real votes, and decide nothing |

05/06 are again the same tie *shape* — Ann leads, Ben and Cara tie for the second finalist slot and tie pairwise — with and without 5s in the tied pair. Here that difference **changes the elected winner** (Ben vs Ann), not just the deciding rung.

Note what 05/06 *can't* be, unlike 01/02 and 03/04: a one-point edit. Handing a tied candidate a 5 also hands them a point, which breaks the very tie the rung is supposed to settle — so an alive/dead pair always has to pay the point back somewhere else (here Cara's `1 → 2` and `4 → 5`). That arithmetic is the dead rung in miniature: **the rung's input and the tie's existence are made of the same numbers.**

Case 09 adds the subtler failure mode: the rung isn't dead, it's *uninformative* — equal nonzero five-star counts fall through to the lot just like `0–0` does.

Every case file in this folder carries `expected_winners:` and is auto-discovered by `test_single_winner_positive.py`.

## The cap ladder — "so what about the 4s?"

The most common confusion: *if the 5s tie, doesn't STAR then look at the 4s?* **No** — the second rung counts **only score-5 votes** and jumps straight to the lot. These three generated files make that concrete by lowering the score **cap** while keeping the exact same tie shape. In every one, the tied pair (Ben, Cara) still ties on points and pairwise, the five-star rung reads `0–0`, and the lot advances the second finalist — the 4s (or 3s, or 2s) never get a say:

| Cap | Ballots (Ann, Ben, Cara) | Five-star rung | Decided by | Page |
|:--:|--------------------------|:--:|---|---|
| 4 | `4,4,1` / `4,0,3` | 0–0 | lot | [cap 4](cases/cases_pages/dead_rung_scoring_dead_cap4.md) |
| 3 | `3,3,1` / `3,0,2` | 0–0 | lot | [cap 3](cases/cases_pages/dead_rung_scoring_dead_cap3.md) |
| 2 | `2,2,1` / `2,0,1` | 0–0 | lot | [cap 2](cases/cases_pages/dead_rung_scoring_dead_cap2.md) |

The top row, running. Nobody in this election scores above a **4**, so watch the **Second tiebreaker**: it counts fives, finds none, prints `Ben 0 / Cara 0`, and hands the tie to the lot — while the 4s sitting right there on both ballots are never consulted.

<!-- report:dead_rung_scoring_dead_cap4 -->
```text
--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 2 ballots.
Ann,Ben,Cara
  4,  4,   1
  4,  0,   3

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Ann           -- 8 -- First place
   Ben           -- 4 -- Tied for second place
   Cara          -- 4 -- Tied for second place
 Ann advances, but there's a two-way tie for second.

[STAR Voting: Scoring Round: First tiebreaker]
 The candidate preferred in the most head-to-head matchups advances.
   Ben           -- 1 -- Tied for second place
   Cara          -- 1 -- Tied for second place
   Equal Support -- 0
 There's still a two-way tie for second.

[STAR Voting: Scoring Round: Second tiebreaker]
 The candidate with the most votes of score 5 advances.
   Ben           -- 0 -- Tied for second place
   Cara          -- 0 -- Tied for second place
 There's still a two-way tie for second.

*(Ties are resolved by choosing the tied candidate with the highest-priority official lot number.)*
    Lot-number priority order: ['Ann', 'Ben', 'Cara']

[Tiebreaker: Lot Number Priority]
  Tie among: ['Ben', 'Cara']
  Resolved: ['Ben'] (selected by lot-number priority).

[Lot-decided tie — rare]
  ⚠ The ballots did not break this tie: the deterministic rungs
    (pairwise / score, then five-star) all came back equal, so the
    pre-published LOT order chose among the tied candidates — the
    result here was set by lot, not by the votes. Usually the
    "dead rung": no tied candidate held a score-5 vote (five-star
    counts fives, not fours). Verify the tied candidates' 5-counts.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Ann           -- 1 -- First place
   Ben           -- 0
   Equal Support -- 1
 Ann wins.
   Runoff math:
     2  ballots cast
   − 1  Equal Support (no preference between the two finalists)
     ─
     1  voters with a preference  (majority = 1)
           Ann 1 (100%)  ·  Ben 0 (0%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Ann
```
<!-- /report -->

Only an actual **5** revives the rung (that's the `alive` case). These were built with [`generate_dead_rung_scenarios.py`](../../../STARVote_LH_tabulation_engine/tools_adam/generate_dead_rung_scenarios.py) (`--round scoring --rung dead --cap {4,3,2}`); see its [write-up](../../../STARVote_LH_tabulation_engine/tools_adam/generate_dead_rung_scenarios.md) for the alive/tied/adversarial variants.

## A real one from BetterVoting — `jfk7pd` (random vs. published lot)

A live BetterVoting election that hit exactly this: two candidates, two ballots (Ada 4/0, Ben 0/4), tied at every rung with **no 5s** (a dead rung), which BV resolved by a **random** draw (`tieBreakType: random`) and elected Ben. Import the same ballots with a deterministic **published** lot order and Ada wins — same votes, different winner. Written up as a shareable brief for the BV team: [A lot-decided STAR tie in BetterVoting (jfk7pd)](lot_random_vs_published_jfk7pd/lot_random_vs_published_jfk7pd.md) — with the frozen export and both tabulatable YAMLs ([BV-order → Ben](lot_random_vs_published_jfk7pd/lot_random_vs_published_jfk7pd_bv_order.yaml), [published → Ada](lot_random_vs_published_jfk7pd/lot_random_vs_published_jfk7pd_published_order.yaml)).

**Does it scale past two candidates?** Yes — the phenomenon is about *symmetry*, not candidate count. The [three-way dead-rung tie](three_way_dead_rung_tie/three_way_dead_rung_tie.md) (A 4/0/0, B 0/4/0, C 0/0/4) is the 3-candidate analog: three candidates, **three** possible winners by lot, and a random draw now diverges from a published order **2/3** of the time — `(k−1)/k` for a `k`-way tie. More candidates never fix it; they can make the divergence worse and add a second place (the finalist choice) for the lot to bite.

**And one where every rung dies, not just this one.** [BV126 — ties at every step](bv126_ties_every_step_8fvd2x.md) is a real BetterVoting race running case 09's failure mode at full length: three candidates tie at 29 points, tie pairwise 2–2–2, and hold **five 5s each** — so the five-star rung runs, counts real votes, separates nobody, and the lot picks both finalists. Then the runoff ties too, and the same three rungs die again in the same order. A ladder can be fully alive and still decide nothing. It also shows the second half of the problem: BetterVoting drops the five flat `5,5,5` ballots as abstentions, so the two engines agree on **Amy** only because those ballots couldn't have changed it.

> **Why build these deliberately-degenerate elections at all?** They're *probes*, not forecasts — the fastest way to isolate one tie behavior, make a real bug reproducible, pin the spec, and lock a regression test. See [Why Build "Silly" Tie Elections?](../../../07_Concepts/topics/ties/why_contrived_tie_cases.md) (with a flow-chart map of every tie case).

## Why it matters

The usual framing — "deterministic tests settle almost everything; the lot is rare" — assumes leading candidates attract some 5s. In **low-score / conservative-grading** elections, or data compressed onto a coarse scale that never reaches the top, the five-star rung quietly does nothing and the **lot decides earlier and more often than the ladder's length suggests**. On a 0–9 ballot the same rung is a *nine-star* count; a field that tops out at 7 gives it nothing to weigh.

*Cases 02 and 03 set `lot_numbers:` explicitly so the lot outcome is pinned and obvious; 01 and 04 never reach the lot.*

# file: README.md
