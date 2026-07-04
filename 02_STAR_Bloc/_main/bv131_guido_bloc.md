# BV131 — Guido example (Bloc STAR): a hidden lot-decided tie

*Marked "Passed" in the sheet, but seat 1 is a **perfect lot-decided tie** — the Bloc analog of [`jfk7pd`](../../01_STAR/tie_break_dead_rung/lot_random_vs_published_jfk7pd/lot_random_vs_published_jfk7pd.md). BetterVoting broke it with a random draw (Cand2), and — the reporting catch — its top-level `tieBreakType` says "none" anyway.*

Reference files: [`bv131_guido_bloc.yaml`](bv131_guido_bloc.yaml) (`expected_winners: [Cand2, Cand3]`) · frozen export [`bv131_guido_bloc_bv_export.json`](bv131_guido_bloc_bv_export.json) (BV `kbh3d9`). Backs sheet row **BV131**.

## The election

Bloc STAR, 3 candidates, 2 seats. Totals: Cand1 = 6, Cand2 = 6, Cand3 = 5.

```
Cand1,Cand2,Cand3
1,5,2
0,0,1
5,1,2
```

## View 1 — BetterVoting

Elected **Cand2, Cand3**. BV's own round-0 logs walk the whole ladder and end at a coin toss:

```
advance_to_runoff_same_score   Cand2, Cand1   (both 6)
runoff_tied                    Cand2, Cand1   (1–1, 1 equal)
runoff_score_tie               Cand2, Cand1   (6–6)
runoff_five_star_tie           Cand2, Cand1   (1–1)
runoff_random                  winner: Cand2          ← coin toss
```

`perm` shows the draw put **Cand2** ahead of Cand1. **But the result's top-level `tieBreakType` is `"none"`** — even though round 0's own `tieBreakType` is `"random"`. A reader of the summary can't tell seat 1 was decided by chance.

## View 2 — the LH report (reproducing BV's draw)

Pinning the lot order to BV's drawn sequence `[Cand2, Cand1, Cand3]` reproduces Cand2. Every deterministic rung ties; the lot decides; the engine flags it:

```
--- Bloc STAR Voting Method (2 winners) ---
 Tabulating 3 ballots.

[Score Distribution]
       5  4  3  2  1  0  | Total
Cand1  1  0  0  0  1  1  |   6
Cand2  1  0  0  0  1  1  |   6
Cand3  0  0  0  2  1  0  |   5

Round 1: Scoring Round
   Cand1  -- 6 -- First place
   Cand2  -- 6 -- Second place
 Cand1 and Cand2 advance.
Round 1: Automatic Runoff Round
   Cand1  -- 1 -- Tied for first place
   Cand2  -- 1 -- Tied for first place
   Equal Support -- 1              ← runoff tie
Round 1: First tiebreaker (highest score)
   Cand1  -- 6 ;  Cand2  -- 6      ← score tie
Round 1: Second tiebreaker (most 5s)
   Cand1  -- 1 ;  Cand2  -- 1      ← five-star tie
[Tiebreaker: Lot Number Priority]
  Tie among: ['Cand1', 'Cand2']  →  Resolved: ['Cand2']   (lot [Cand2, Cand1, Cand3])

[Lot-decided tie — rare]
  ⚠ The ballots did not break this tie ... the LOT order chose the winner.

Round 2: Scoring Round
   Cand1  -- 6 -- First place
   Cand3  -- 5 -- Second place
Round 2: Automatic Runoff Round
   Cand3  -- 2 -- First place
   Cand1  -- 1
 Cand3 wins.

Winners — Bloc STAR Voting Method (2 winners)
 Cand2
 Cand3
```

Full audit copy: [`_main_tabulated/bv131_guido_bloc_tabulated.txt`](_main_tabulated/bv131_guido_bloc_tabulated.txt).

## Two findings

1. **Non-reproducible (cf. [#1063](https://github.com/Equal-Vote/bettervoting/issues/1063) / [#1417](https://github.com/Equal-Vote/bettervoting/issues/1417)).** With the column-order fallback (no lot order) LH elects **Cand1** for seat 1, not Cand2 — same ballots, different winner, decided only by the tie-break order. BV's `random` draw happened to pick Cand2.
2. **Reporting mislabel.** The result's top-level `tieBreakType: "none"` contradicts round 0's `tieBreakType: "random"`. The summary should surface that a seat was lot-decided (cf. [#1379](https://github.com/Equal-Vote/bettervoting/issues/1379) and the results-view transparency ask). So "Passed" is optimistic — the winner was a coin toss, undisclosed at the top level.

## Related

- [BV `jfk7pd`](../../01_STAR/tie_break_dead_rung/lot_random_vs_published_jfk7pd/lot_random_vs_published_jfk7pd.md) — the single-winner original of this exact phenomenon.
- [STAR Tie-Breaking — The Full Chain](../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md).
- [#904](https://github.com/Equal-Vote/bettervoting/issues/904) — the export also labels `votingMethod: "STAR"`, not "Bloc STAR".
