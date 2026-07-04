# BV1815 — Bloc STAR, 3 candidates, 2 seats (seat 2 by score tiebreak)

*A real BetterVoting election (id `fk38pk`, marked **Passed**) labeled "basic /
simple" — but it quietly exercises the **score tiebreaker** at the second seat.
LH and BetterVoting agree: winners **A, C**.*

Reference files: [`bv1815_bloc_3c2s_basic.yaml`](bv1815_bloc_3c2s_basic.yaml)
(`expected_winners: [A, C]`) · frozen export
[`bv1815_bloc_3c2s_basic_bv_export.json`](bv1815_bloc_3c2s_basic_bv_export.json)
(BV `fk38pk`). Backs sheet row **BV1815**.

## The election

Bloc STAR, 3 candidates, 2 seats, 3 ballots:

```
A,B,C
4,1,0
3,0,2
5,0,0
```

Totals: A = 12, B = 1, C = 2.

## What makes it interesting

Seat 1 is a clean win for A. Seat 2 is **not** clean: with A removed, B and C each
total near-nothing and **tie 1–1 in the runoff** (one voter prefers B, one prefers
C, one is Equal Support). The tie falls to the first runoff rung — **highest total
score** — and C (2) beats B (1). BetterVoting resolves it the same way
(`tieBreakType: "score"`, elected A, C), which is why this "basic" case is a clean
**Pass** and a useful reference that the score tiebreaker works in Bloc.

## View 1 — BetterVoting

Result: **A and C win** (2 seats). `nAbstentions: 0`, `nTallyVotes: 3` (all
ballots counted), `tieBreakType: "score"`. *(Aside: the export labels
`votingMethod: "STAR"` rather than "Bloc STAR" — [#904](https://github.com/Equal-Vote/bettervoting/issues/904).)*

*(Drop a BV screenshot into `img/` as `img/fk38pk_result.png` to add it here.)*

## View 2 — the LH report (inline)

```
--- Bloc STAR Voting Method (2 winners) ---
 Tabulating 3 ballots.
A,B,C
4,1,0
3,0,2
5,0,0

[Score Distribution] (number of ballots giving each score)
   5  4  3  2  1  0  | Total   Avg
A  1  1  1  0  0  0  |    12   4.0
B  0  0  0  0  1  2  |     1   0.3
C  0  0  0  1  0  2  |     2   0.7
 Want to fill 2 seats.

Round 1: Scoring Round
   A  -- 12 -- First place
   C  --  2 -- Second place
   B  --  1
 A and C advance.
Round 1: Automatic Runoff Round
   A  -- 3 -- First place
   C  -- 0
 A wins.   (3 of 3, no Equal Support)

Round 2: Scoring Round
   C  -- 2 -- First place
   B  -- 1 -- Second place
 C and B advance.
Round 2: Automatic Runoff Round
   B  -- 1 -- Tied for first place
   C  -- 1 -- Tied for first place
   Equal Support -- 1               ← runoff TIE (1-1)
Round 2: Automatic Runoff Round: First tiebreaker
 The highest-scoring candidate wins.
   C  -- 2 -- First place           ← score rung breaks it: C (2) > B (1)
   B  -- 1
 C wins.

Winners — Bloc STAR Voting Method (2 winners)
 A
 C
```

Full audit copy:
[`_main_tabulated/bv1815_bloc_3c2s_basic_tabulated.txt`](_main_tabulated/bv1815_bloc_3c2s_basic_tabulated.txt).

## Related

- The pure no-tie control: [`00_c3_b3_bloc-baseline-2-seats.yaml`](00_c3_b3_bloc-baseline-2-seats.yaml)
  (both seats decided by the ballots, no rung consulted).
- The tie-break ladder these seats descend:
  [STAR Tie-Breaking — The Full Chain](../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md).
- [#904](https://github.com/Equal-Vote/bettervoting/issues/904) — the method-name
  label ("STAR" vs "Bloc STAR").
