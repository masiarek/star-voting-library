# Bloc STAR

**One line:** Bloc STAR fills **N seats** by running ordinary single-winner STAR **N times** on the same ballots — elect a winner, remove them from the field, re-run the count on who's left. Same 0–5 ballot, same two rounds, repeated once per seat.

→ Prerequisite: [STAR — start here](../../01_STAR/01_Learn/STAR_start_here.md) · the fork this sits on one side of: [Electing more than one, simply](../../07_Concepts/topics/electing_more_than_one.md) · the proportional alternative: [STAR-PR](../../03_STAR_PR/01_Learn/) · Glossary: [Bloc STAR](../../07_Concepts/GLOSSARY.md) · Curriculum: [201.5](../../07_Concepts/curriculum/CURRICULUM_201.md)

**Level: 201 · for voters**

---

## The ballot: nothing changes

You score every candidate **0 to 5**, exactly as in single-winner STAR. There is no "pick three for three seats" instruction, no ranking, nothing to ration. Whether the race fills one seat or five, the ballot in your hand is the same — which is the practical argument for the whole scored family: **voters learn one ballot** and it serves every kind of race.

That matters more than it sounds. Under [SNTV / Bloc Plurality](bloc_star_vs_other_bloc_methods.md) the ballot itself changes with the seat count and forces you to spend a scarce mark; here your score for one candidate never costs another candidate anything.

## The count: elect, remove, re-run

To fill **N** seats:

1. **Scoring round.** Add up every candidate's stars. The two highest advance.
2. **Automatic runoff.** Of those two finalists, whoever more voters scored higher wins the seat.
3. **Remove the winner** from the field and go back to step 1 with the *same, unchanged* ballots.
4. Repeat until N seats are filled.

Each seat is a complete little STAR election. Nothing is reweighted, spent, or transferred between seats — that is the single difference from [STAR-PR](../../03_STAR_PR/01_Learn/STAR_PR/), and the reason this method is majoritarian rather than proportional.

**Worked — the baseline case.** 3 candidates, 2 seats, 3 ballots (the smallest Bloc election that actually decides anything: with 2 candidates for 2 seats nobody can lose):

```text
--- Bloc STAR Voting Method (2 winners) ---
 Tabulating 3 ballots to fill 2 seats.
Alice,Bruno,Clara
    5,    3,    1
    4,    5,    2
    5,    4,    0

Round 1: Scoring Round
 The two highest-scoring candidates advance to the next round.
   Alice         -- 14 -- First place
   Bruno         -- 12 -- Second place
   Clara         --  3
 Alice and Bruno advance.

Round 1: Automatic Runoff Round
 The candidate preferred in the most head-to-head matchups wins.
   Alice         -- 2 -- First place
   Bruno         -- 1
   Equal Support -- 0
 Alice wins.
   Voters with a preference: 3 of 3 (no Equal Support).
   Alice 2 (67%) vs Bruno 1 (33%); majority = 2.

──────────────────────────────────────────────────
Round 2: Scoring Round
 The two highest-scoring candidates advance to the next round.
   Bruno         -- 12 -- First place
   Clara         --  3 -- Second place
 Bruno and Clara advance.

Round 2: Automatic Runoff Round
 The candidate preferred in the most head-to-head matchups wins.
   Bruno         -- 3 -- First place
   Clara         -- 0
   Equal Support -- 0
 Bruno wins.
   Voters with a preference: 3 of 3 (no Equal Support).
   Bruno 3 (100%) vs Clara 0 (0%); majority = 2.

Winners — Bloc STAR Voting Method (2 winners)
 Alice
 Bruno
```

Want the whole count? See the full LH report → [`00_c3_b3_bloc-baseline-2-seats`](../02_Examples/cases/cases_pages/00_c3_b3_bloc-baseline-2-seats.md) ([yaml](../02_Examples/cases/00_c3_b3_bloc-baseline-2-seats.yaml)).

## What "remove" does — and what it doesn't

The removal step is the one place people expect more machinery than there is. Removing a seated candidate **only takes them out of the running.** It does not touch anyone's ballot, discount anyone's scores, or change any other candidate's total.

Look at the baseline count above: Bruno scores **12** in round 1 and **12** again in round 2, and Clara scores **3** both times. The whole of round 2 is round 1 with one column deleted. In the 100-voter [BV1835](../02_Examples/bv1835_8h3yrx_score_leader_no_seat.md) case the same thing runs four times: Ava's 294 points are re-printed, untouched, in every one of the four scoring rounds.

Two consequences worth holding onto:

- **The scoring round is decided once, in effect.** Score order never changes between seats; candidates just drop off the top of it. All the seat-to-seat action is in the runoff, which compares a *different pair* each round.
- **Nothing punishes a voter for having been "represented" already.** If your favorites take seats 1 and 2, your ballot is exactly as loud for seat 3 as it was for seat 1. That is precisely what a proportional method refuses to allow — see [the majority sweep](majority_sweep.md).

## Running it

```yaml
voting_method: Bloc STAR     # aliases: bloc, "bloc star"
num_winners: 2
```

House style spells it **`Bloc STAR`** rather than the vaguer `bloc` — the count is a specific method, not a generic mode. Everything else in the file is an ordinary STAR file. Multi-winner races use the house minimal `options:` block with `show_matrix: false` and `matrix_finalists_only: false`: a "Top 2 Finalist" matrix is a single-winner idea and prints misleadingly across several seats.

```bash
.venv/bin/python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 02_STAR_Bloc/02_Examples/cases/00_c3_b3_bloc-baseline-2-seats.yaml
```

## Reading the report

Each seat prints as a numbered **Round** with its own scoring round and automatic runoff, separated by a horizontal rule, then a single **Winners** block listing the seats **in the order they were filled**. That order is real information — it is a rough strength ranking of the winners, and when a tie is broken it says *which seat* the coin decided. It is not, however, a ranking of anything about the losers.

The `_tabulated` mirror adds what the on-screen report leaves out: the score distribution, the full pairwise matrix, the Condorcet notes, and the runoff-math funnel for every seat.

## Where to go next

Three things separate Bloc STAR from what people assume it does. In the order they bite:

1. **[The majority sweep](majority_sweep.md)** — a cohesive majority can take *every* seat. Majoritarian by design; the reason to reach for [STAR-PR](../../03_STAR_PR/01_Learn/) when you want representation instead.
2. **[The score leader can win no seat](score_leader_no_seat.md)** — Bloc STAR is *not* "top N by points." Seats go to whoever is **preferred head-to-head**, so a broadly-liked compromise candidate who leads every scoring round can be shut out entirely.
3. **[Ties, seat by seat](bloc_tiebreaks.md)** — the single-winner ladder runs once per seat, and a tie broken at seat 1 changes the field every later seat is decided in.

Then: [honest limits](bloc_honest_limits.md), and [how it compares to the other at-large methods](bloc_star_vs_other_bloc_methods.md).
