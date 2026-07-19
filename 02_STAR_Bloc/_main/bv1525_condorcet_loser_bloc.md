# BV1525 — 5 candidates / 4 winners, Bloc STAR: a Condorcet loser ties for seat 1

*Larry Hastings' electowiki Bloc-STAR test election, reproduced as the LH reference for BetterVoting test BV1525 (4 winners, 16 ballots). The candidates are named for their intended finish — First, Condorcet Loser, Second, Third, Fourth. The twist: a **Score co-leader can be a near-Condorcet loser** (loses every head-to-head). Here "Condorcet Loser" ties "First" for the top score and so ties for the seat-1 runoff; the lot alone separates them. Winners: **First, Second, Third, Fourth**.*

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/dkj9dx) · **[results ↗](https://bettervoting.com/dkj9dx/results)** (election `dkj9dx`). On this run BetterVoting drew **First** for seat 1 — matching this file's published-lot outcome. Note the reporting quirk: BV flags the seat-1 round `tieBreakType: random` (correct — its logs walk `runoff_tied → runoff_score_tie → runoff_five_star_tie → runoff_random`), but the **top-level summary still reads `tieBreakType: none`**, the same under-report seen in [BV130-r2](bv130r2_dead_rung_bloc.md) and [BV131](bv131_guido_bloc.md).

Reference file: [`bv1525_condorcet_loser_bloc.yaml`](bv1525_condorcet_loser_bloc.yaml) (`expected_winners: [First, Second, Third, Fourth]`). Backs sheet row **BV1525**. Source: Larry's [`test_election_bloc_star_and_electowiki.starvote`](https://github.com/larryhastings/starvote/blob/master/test_elections/test_election_bloc_star_and_electowiki.starvote).

## The election

Bloc STAR, 5 candidates, **4 seats**, 16 ballots (four distinct ballots, weighted 8 / 5 / 2 / 1):

```
First,Condorcet Loser,Second,Third,Fourth
3,0,1,1,1     × 8
0,4,0,0,0     × 5
0,1,3,2,1     × 2
0,2,5,4,3     × 1
```

```
[Score Distribution] (how many ballots gave each star rating)
                         Score
Candidate         5   4   3   2   1   0  | Total   Avg
First             0   0   8   0   0   8  |    24   1.5
Condorcet Loser   0   5   0   1   2   8  |    24   1.5
Second            1   0   2   0   8   5  |    19   1.2
Third             0   1   0   2   8   5  |    16   1.0
Fourth            0   0   1   0  10   5  |    13   0.8
```

First and Condorcet Loser **tie at 24** for the top score; nothing reaches 5, so the five-star rung is dead.

## Seat 1 — the tie, and why the lot matters

The two top scorers advance, tie 8–8 in the runoff, tie again on score (24–24) and five-star (0–0), and the pre-published permutation `[First, Condorcet Loser, Second, Third, Fourth]` breaks it for **First**:

```
Round 1: Scoring Round — Condorcet Loser (24) and First (24) advance.
Round 1: Automatic Runoff — Condorcet Loser 8 ; First 8   ← tied
Round 1: First tiebreaker (score)   — 24 ; 24             ← tied
Round 1: Second tiebreaker (most 5s) — 0 ; 0              ← dead rung
[Tiebreaker: Lot Number Priority]  Resolved: ['First']    (permutation [First, Condorcet Loser, ...])
[Lot-decided tie — rare]

Round 2: Condorcet Loser (24) & Second (19) advance → Second wins the runoff (11 vs 5).
Round 3: Condorcet Loser (24) & Third  (16) advance → Third  wins the runoff (11 vs 5).
Round 4: Condorcet Loser (24) & Fourth (13) advance → Fourth wins the runoff ( 9 vs 5).

Winners — Bloc STAR Voting Method (4 winners)
 First
 Second
 Third
 Fourth
```

Full audit copy: [`_main_tabulated/bv1525_condorcet_loser_bloc_tabulated.txt`](_main_tabulated/bv1525_condorcet_loser_bloc_tabulated.txt).

## The finding

**Condorcet Loser tops the score in every round yet wins no seat.** Because they lose every head-to-head runoff, they only ever have a *shot* at seat 1 — and only by winning the coin toss. That is exactly the electowiki caution: the Score winner can be a Condorcet loser, so handing a seat to *both* candidates who tie in the first runoff (an option electowiki mentions) would wrongly seat Condorcet Loser. STAR's runoff, plus a tiebreak, prevents it.

**Only two orderings are valid**, decided entirely by the seat-1 lot:

- lot favors First → **First, Second, Third, Fourth** (this file)
- lot favors Condorcet Loser → **Condorcet Loser, First, Second, Third**

A **pre-published permutation** makes which one occurs reproducible. A **random** draw (BetterVoting) does not — it "picks a different list of winners with each run," which is why comparing engines on this ballot set is hard until the tiebreak order is pinned (cf. [#1063](https://github.com/Equal-Vote/bettervoting/issues/1063) / [#1417](https://github.com/Equal-Vote/bettervoting/issues/1417); [#358](https://github.com/Equal-Vote/bettervoting/issues/358)).

## Related

- [BV130-r2 — dead-rung lot tie](bv130r2_dead_rung_bloc.md) and [BV131 — Guido example](bv131_guido_bloc.md) — other Bloc seats decided by the lot.
- [BV `jfk7pd`](../../01_STAR/tie_break_dead_rung/lot_random_vs_published_jfk7pd/lot_random_vs_published_jfk7pd.md) — the single-winner original of the random-vs-published lot point.
- [STAR Tie-Breaking — The Full Chain](../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md) · [why contrived tie cases earn their keep](../../00_start_here/topics/ties/why_contrived_tie_cases.md).
