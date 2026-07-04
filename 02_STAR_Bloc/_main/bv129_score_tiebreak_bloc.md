# BV129 — Bloc STAR, 3 cand / 2 winners: seat 2 by the score tiebreaker

*A clean Bloc STAR result where the second seat is decided by the **score**
tiebreaker (deterministic — no lot). LH and BetterVoting agree: **Carmen, Andre**.
BV129's "Failed" is only the method-name label ([#1086](https://github.com/Equal-Vote/bettervoting/issues/1086)),
not the count.*

Reference files: [`bv129_score_tiebreak_bloc.yaml`](bv129_score_tiebreak_bloc.yaml)
(`expected_winners: [Carmen, Andre]`) · frozen export
[`bv129_score_tiebreak_bloc_bv_export.json`](bv129_score_tiebreak_bloc_bv_export.json)
(BV `btmydt`). Backs sheet row **BV129**.

## The election

Bloc STAR, 3 candidates, 2 seats, 5 ballots. Totals: Andre = 17, Blake = 16,
Carmen = 25.

```
Andre,Blake,Carmen
3,3,5
4,4,5
3,1,5
4,4,5
3,4,5
```

## What makes it interesting

Seat 1 is a landslide for Carmen (every ballot scores her 5). Seat 2 is the
lesson: with Carmen removed, Andre and Blake **tie 1–1 in the runoff** (three of
five ballots are Equal Support). The tie falls to the first runoff rung — **highest
total score** — and Andre (17) edges Blake (16). It's fully deterministic: the
score rung separates them, so the lot is never reached. BetterVoting resolves it
identically (round-1 `tieBreakType: "score"`, elected Carmen, Andre).

## View 1 — BetterVoting

Elected **Carmen, Andre**. Round-1 (seat 2) `tieBreakType: "score"`. The result is
correct; the recorded failure is the **method-name label** — the export reports
`votingMethod: "STAR"` rather than "Bloc STAR"
([#1086](https://github.com/Equal-Vote/bettervoting/issues/1086), same family as
[#904](https://github.com/Equal-Vote/bettervoting/issues/904)).

## View 2 — the LH report (inline)

```
--- Bloc STAR Voting Method (2 winners) ---
 Tabulating 5 ballots.

[Score Distribution]
        5  4  3  2  1  0  | Total
Andre   0  2  3  0  0  0  |   17
Blake   0  3  1  0  1  0  |   16
Carmen  5  0  0  0  0  0  |   25

Round 1: Scoring Round
   Carmen  -- 25 -- First place
   Andre   -- 17 -- Second place
   Blake   -- 16
 Carmen and Andre advance.
Round 1: Automatic Runoff Round
   Carmen  -- 5 -- First place
   Andre   -- 0
 Carmen wins.   (5 of 5, no Equal Support)

Round 2: Scoring Round
   Andre   -- 17 -- First place
   Blake   -- 16 -- Second place
 Andre and Blake advance.
Round 2: Automatic Runoff Round
   Andre   -- 1 -- Tied for first place
   Blake   -- 1 -- Tied for first place
   Equal Support -- 3               ← runoff tie (1-1, 3 no-preference)
Round 2: First tiebreaker (highest score)
   Andre  -- 17 -- First place      ← score rung breaks it: Andre (17) > Blake (16)
   Blake  -- 16
 Andre wins.

Winners — Bloc STAR Voting Method (2 winners)
 Carmen
 Andre
```

Full audit copy:
[`_main_tabulated/bv129_score_tiebreak_bloc_tabulated.txt`](_main_tabulated/bv129_score_tiebreak_bloc_tabulated.txt).

## Related

- [BV1815](bv1815_bloc_3c2s_basic.md) — the other Bloc score-tiebreak reference (also Passed on the count).
- [BV131](bv131_guido_bloc.md) — by contrast, a seat decided by the *lot* (all rungs tied).
- [#1086](https://github.com/Equal-Vote/bettervoting/issues/1086) / [#904](https://github.com/Equal-Vote/bettervoting/issues/904) — the "STAR" vs "Bloc STAR" method-name label.
- [STAR Tie-Breaking — The Full Chain](../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md).
