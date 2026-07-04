# BV130-r2 — 6 candidates / 3 winners, Bloc STAR: a dead-rung lot tie

*A real BetterVoting election (id `9ff9jk`) built directly from this repo's tuned dead-rung scenario: 6 candidates, 3 seats, 4 ballots, and nothing scored above 4. Seat 1 is a perfect Ada/Dan tie that dies at every deterministic rung and falls to the lot. BetterVoting's random draw elected **Dan, Ada, Eve**; a pre-published order would elect **Ada, Dan, Eve** — same three winners, the tied pair's seats swapped.*

> **Which BV130 is this?** This is **BV130-r2** (the retest, election `9ff9jk`, marked **Passed**) — a *different* election from the original **BV130**, which is a 9-ballot "Someone I Like / Santa Claus / The Lesser Evil" case backing the star-server#731 *reporting* issue (tabs → numbered pages). See [`bv130_bloc_pagination_731.md`](bv130_bloc_pagination_731.md) for that one. This page is purely about the tie behavior; the outcome itself is valid (a random draw among a genuine tie), which is why the tracker marks it Passed.

Reference files: [`bv130r2_dead_rung_bloc.yaml`](bv130r2_dead_rung_bloc.yaml) (`expected_winners: [Dan, Ada, Eve]`) · frozen export [`bv130r2_dead_rung_bloc_bv_export.json`](bv130r2_dead_rung_bloc_bv_export.json) (BV `9ff9jk`). Backs sheet row **BV130-r2**.

## The election

Bloc STAR, 6 candidates, 3 seats, 4 ballots — capped at 4, so no candidate ever holds a five:

```
Ada,Ben,Cara,Dan,Eve,Finn
4,1,2,3,2,0
3,2,1,4,2,1
4,2,1,4,3,2
4,2,1,4,3,1
```

Totals: **Ada 15, Dan 15**, Eve 10, Ben 7, Cara 5, Finn 4. Ada and Dan tie for the top, and because the ceiling is 4 their five-star counts are both 0 — the *dead rung*.

## View 1 — BetterVoting

Elected **Dan, Ada, Eve** (`nAbstentions: 0`, `nTallyVotes: 4` — all four ballots counted). The export's `elected` block confirms Ada and Dan each have `score: 15` and `fiveStarCount: 0`, and its `perm` (the random draw) is:

```
[Finn, Ben, Dan, Eve, Ada, Cara]
```

Dan sits ahead of Ada in that draw, so the seat-1 Ada/Dan tie broke for **Dan**. **But the result's top-level `tieBreakType` is reported as `"none"`** — even though seat 1 was decided by a random draw. A reader of the summary can't tell a seat was settled by chance ([#1379](https://github.com/Equal-Vote/bettervoting/issues/1379) family).

*(Drop a BV screenshot into `img/` as `img/9ff9jk_result.png` to add it here.)*

## View 2 — the LH report (reproducing BV's draw)

Pinning `lot_numbers` to BV's drawn sequence `[Finn, Ben, Dan, Eve, Ada, Cara]` reproduces **Dan, Ada, Eve** exactly. Every deterministic rung in seat 1 ties, the lot decides, and the engine flags it:

```
[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Ada        0  3  1  0  0  0  |    15   3.8
Ben        0  0  0  3  1  0  |     7   1.8
Cara       0  0  0  1  3  0  |     5   1.3
Dan        0  3  1  0  0  0  |    15   3.8
Eve        0  0  2  2  0  0  |    10   2.5
Finn       0  0  0  1  2  1  |     4   1.0

Round 1: Scoring Round
   Ada  -- 15 -- First place
   Dan  -- 15 -- Second place
 Ada and Dan advance.
Round 1: Automatic Runoff Round
   Ada  -- 1 -- Tied for first place
   Dan  -- 1 -- Tied for first place
   Equal Support -- 2              ← runoff tie
Round 1: First tiebreaker (highest score)
   Ada  -- 15 ;  Dan  -- 15        ← score tie
Round 1: Second tiebreaker (most 5s)
   Ada  -- 0 ;  Dan  -- 0          ← five-star DEAD (nothing reaches 5)
[Tiebreaker: Lot Number Priority]
  Tie among: ['Ada', 'Dan']  →  Resolved: ['Dan']   (lot [Finn, Ben, Dan, Eve, Ada, Cara])

[Lot-decided tie — rare]
  ⚠ The ballots did not break this tie ... the LOT order chose the winner.

Round 2: Scoring Round — Ada (15) and Eve (10) advance; Ada wins the runoff 100%.
Round 3: Scoring Round — Eve (10) and Ben (7) advance; Eve wins.

Winners — Bloc STAR Voting Method (3 winners)
 Dan
 Ada
 Eve
```

Full audit copy: [`_main_tabulated/bv130r2_dead_rung_bloc_tabulated.txt`](_main_tabulated/bv130r2_dead_rung_bloc_tabulated.txt).

## Two findings

1. **Non-reproducible (cf. [#1063](https://github.com/Equal-Vote/bettervoting/issues/1063) / [#1417](https://github.com/Equal-Vote/bettervoting/issues/1417)).** With a *published* lot order `[Ada, Ben, Cara, Dan, Eve, Finn]` the seat-1 tie breaks for **Ada**, giving **Ada, Dan, Eve** — the same three winners, but seats 1 and 2 swap between the tied pair. Which candidate takes which seat is decided purely by the draw; BV's `random` happened to pick Dan.
2. **Reporting mislabel.** The result's top-level `tieBreakType: "none"` contradicts a seat that was decided by the lot (cf. [#1379](https://github.com/Equal-Vote/bettervoting/issues/1379)). The summary should surface that a seat was lot-decided.

## Related

- [BV131 — Guido example](bv131_guido_bloc.md) — the other Bloc seat decided by the lot.
- [BV750 — every ballot identical](bv750_tie_breaking_bloc.md) — the extreme flat lot case.
- [BV `jfk7pd`](../../01_STAR/tie_break_dead_rung/lot_random_vs_published_jfk7pd/lot_random_vs_published_jfk7pd.md) — the single-winner original of this exact phenomenon.
- Concept: [The "dead rung" case set](../../01_STAR/tie_break_dead_rung/README.md) · [STAR Tie-Breaking — The Full Chain](../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md).
- [#904](https://github.com/Equal-Vote/bettervoting/issues/904) — the export also labels `votingMethod: "STAR"`, not "Bloc STAR".
