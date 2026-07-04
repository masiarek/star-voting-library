# BV750 — Bloc STAR tie-breaking, every ballot identical · issue [#1052](https://github.com/Equal-Vote/bettervoting/issues/1052) family

*The extreme flat case: a 2-seat Bloc STAR election where all three ballots are `5,5,5`. Nothing separates anyone, so the lot decides both seats — and BetterVoting drops **every** ballot as an abstention (`nTallyVotes: 0`, the "no ballots have been cast" bug). LH and BV both elect **c, a** (via the lot), but LH counts all three ballots.*

Reference files: [`bv750_tie_breaking_bloc.yaml`](bv750_tie_breaking_bloc.yaml) (`expected_winners: [c, a]`) · frozen export [`bv750_tie_breaking_bloc_bv_export.json`](bv750_tie_breaking_bloc_bv_export.json) (BV `3yr2qd`). Backs sheet row **BV750**.

## The election

Bloc STAR, 3 candidates, 2 seats, 3 ballots — all identical:

```
a,b,c
5,5,5
5,5,5
5,5,5
```

Every candidate totals 15; every voter is indifferent among all three.

## View 1 — BetterVoting

Elected **c, a**, `tieBreakType: "random"`, `perm` = [c, a, b] (the draw picks the two finalists and both winners). But its `summaryData` reports `nAbstentions: 3`, `nTallyVotes: 0` — BV classified all three all-equal ballots as **abstentions** and tallied **nothing**, so it shows the "no ballots" state ([#1052](https://github.com/Equal-Vote/bettervoting/issues/1052) / [#1407](https://github.com/Equal-Vote/bettervoting/issues/1407)). An all-equal ballot is a real vote of *no preference*, not an abstention.

## View 2 — the LH report (all three ballots counted)

LH counts every ballot; each candidate really totals 15, and the tie is genuine at every rung, so the lot decides both seats:

```
--- Bloc STAR Voting Method (2 winners) ---
 Tabulating 3 ballots.

[Score Distribution]
   5  4  3  2  1  0  | Total
a  3  0  0  0  0  0  |   15
b  3  0  0  0  0  0  |   15
c  3  0  0  0  0  0  |   15

Round 1: Scoring Round
   a 15 ; b 15 ; c 15                     ← three-way tie
Round 1: First tiebreaker (pairwise)
   a 0 ; b 0 ; c 0 ; Equal Support 3      ← pairwise tied
Round 1: Second tiebreaker (most 5s)
   a 3 ; b 3 ; c 3                        ← five-star tied
[Tiebreaker: Lot Number Priority]  Resolved: ['c', 'a']   (lot [c, a, b])
[Lot-decided tie — rare]
Round 1: Automatic Runoff (c vs a) — tied at every rung → lot → c

Round 2: Scoring Round
   a 15 ; b 15 — a and b advance
Round 2: Automatic Runoff (a vs b) — tied → lot → a

Winners — Bloc STAR Voting Method (2 winners)
 c
 a
```

Full audit copy: [`_main_tabulated/bv750_tie_breaking_bloc_tabulated.txt`](_main_tabulated/bv750_tie_breaking_bloc_tabulated.txt).

## Two findings

1. **Every ballot dropped (#1052/#1407).** `nTallyVotes: 0` — BV treats all-equal ballots as abstentions and tallies none, so it reports "no ballots cast" even though three voters participated. LH keeps them as Equal Support.
2. **Random tie-break → non-reproducible** (cf. [#1063](https://github.com/Equal-Vote/bettervoting/issues/1063) / [#1417](https://github.com/Equal-Vote/bettervoting/issues/1417)). Identical ballots separate nobody, so both seats are a coin toss; `lot_numbers: [c, a, b]` pins BV's draw. The winners can't be affected by the dropped ballots — only by the lot order.

## Related

- [BV126](../../01_STAR/tie_break_dead_rung/bv126_ties_every_step_8fvd2x.md) — the single-winner "ties every step" version (some flat ballots dropped).
- [BV132](bv132_verify_votes_bloc.md) — the Bloc flat-ballot-drop bug with only *some* flat ballots.
- [BV131](bv131_guido_bloc.md) — a Bloc seat decided by the lot.
- [The "dead rung" case set](../../01_STAR/tie_break_dead_rung/README.md) · [why flat ballots don't change the winner](../../00_start_here/topics/ties/why_contrived_tie_cases.md).
