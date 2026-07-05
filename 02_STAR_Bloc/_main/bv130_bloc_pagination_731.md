# BV130 — 6 candidates / 3 winners, Bloc STAR (original; star-server#731)

*The original BV130: a clean, tie-free 3-seat Bloc STAR election (6 candidates, 9 ballots). It backs [star-server#731](https://github.com/Equal-Vote/star-server/issues/731) — a **reporting/UI** issue (Bloc results are shown as browser **tabs**, one per round, and should use **numbered pages** instead). The tabulation is correct; LH and BetterVoting agree on the winners. The bug is purely how the three rounds are displayed, not the math.*

> **Which BV130 is this?** The **original** BV130 (this page). Not to be confused with **BV130-r2** (election `9ff9jk`), a separate 4-ballot retest built around a dead-rung lot tie — see [`bv130r2_dead_rung_bloc.md`](bv130r2_dead_rung_bloc.md). Same family name, different elections; keep them apart.

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/yhxy7q) · **[results ↗](https://bettervoting.com/yhxy7q/results)** (election `yhxy7q`). Recreated via the API so the reporting bug has a live election to point at; BV agrees with LH — Someone I Like, Santa Claus, The Lesser Evil — and reports `tieBreakType: none` correctly (there is no tie here).

Reference file: [`bv130_bloc_pagination_731.yaml`](bv130_bloc_pagination_731.yaml) (`expected_winners: [Someone I Like, Santa Claus, The Lesser Evil]`). Backs sheet row **BV130**.

## The election

Bloc STAR, 6 candidates, 3 seats, 9 ballots (three distinct ballots, weighted 3 / 4 / 2):

```
Johnny Cash,Elvis Presley,Santa Claus,The Lesser Evil,Someone I Like,Apocalypse Now
0,2,4,3,5,0      × 3
2,1,3,4,3,2      × 4
1,1,5,2,5,0      × 2
```

Scores separate everyone cleanly — Someone I Like 37, Santa Claus 34, The Lesser Evil 29, Elvis 12, Johnny 10, Apocalypse 8 — so no tiebreak is ever consulted. Bloc fills the seats by running STAR three times (elect, remove, repeat).

## What star-server#731 is (and isn't)

[#731](https://github.com/Equal-Vote/star-server/issues/731) asks BetterVoting to stop rendering the Bloc rounds as **tabs** and use the **Pagination** component (numbered pages at the bottom, as the proportional viewer already does). It is a **presentation** change to the results view — the winners and the round-by-round numbers are already correct. So this case's job is to pin the *correct* tabulation as the reference the UI must keep matching; there is no LH↔BV result divergence to show — LH and the live BV election (`yhxy7q`) agree on all three winners.

## The LH report (the correct tabulation)

```
[Score Distribution] (how many ballots gave each star rating)
                      Score
Candidate        5  4  3  2  1  0  | Total   Avg
Johnny Cash      0  0  0  4  2  3  |    10   1.1
Elvis Presley    0  0  0  3  6  0  |    12   1.3
Santa Claus      2  3  4  0  0  0  |    34   3.8
The Lesser Evil  0  4  3  2  0  0  |    29   3.2
Someone I Like   5  0  4  0  0  0  |    37   4.1
Apocalypse Now   0  0  0  4  0  5  |     8   0.9

Round 1: Someone I Like (37) & Santa Claus (34) advance; Someone I Like wins the runoff (3 vs 0, 6 Equal Support).
Round 2: Santa Claus (34) & The Lesser Evil (29) advance; Santa Claus wins the runoff 5 vs 4.
Round 3: The Lesser Evil (29) & Elvis Presley (12) advance; The Lesser Evil wins 9 vs 0.

Winners — Bloc STAR Voting Method (3 winners)
 Someone I Like
 Santa Claus
 The Lesser Evil
```

Full audit copy: [`_main_tabulated/bv130_bloc_pagination_731_tabulated.txt`](_main_tabulated/bv130_bloc_pagination_731_tabulated.txt).

## Related

- [BV130-r2 — dead-rung lot tie](bv130r2_dead_rung_bloc.md) (`9ff9jk`) — the retest, a different election with a genuine tie.
- The Bloc mechanic these seats use: [02_STAR_Bloc README](../README.md).
- [#904](https://github.com/Equal-Vote/bettervoting/issues/904) — the export also labels `votingMethod: "STAR"` rather than "Bloc STAR".
