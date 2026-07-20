# Exercise 12 — Two seats, one neighborhood

*A neighborhood association elects a two-seat board. The north side — six voters of ten — runs Asa and Bram; the south side's four voters run Cleo and Dane. Everyone votes honestly. Count the same ten ballots two ways and you get two different boards. Neither count is broken. The exercise is deciding what a "fair" committee even means.*

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/89wwvr) · **[results ↗](https://bettervoting.com/89wwvr/results)** (election `89wwvr`, Test ID BV2199 — both races in one election; BV agrees on both seat pairs, and banners the STAR-PR race "Tied!" — a documented serializer quirk, see solution (d)).

**You practice:** [multi-winner thinking](../../00_start_here/topics/electing_more_than_one.md) — **Bloc STAR** (run STAR once per seat) versus **Allocated Score** (STAR-PR: winners *spend* their supporters' ballot weight) — and the majoritarian-vs-proportional design question underneath.

Work each part on paper before opening its solution. Both YAMLs are runnable (the same ballots, different `voting_method`); the `_tabulated` mirrors are the full audit reports.

## The ballots

Ten voters, four candidates, two seats, scores 0–5:

| | ×6 north side | ×4 south side |
|---|:---:|:---:|
| **Asa** | 5 | 0 |
| **Bram** | 4 | 0 |
| **Cleo** | 0 | 5 |
| **Dane** | 0 | 4 |

## Your task

- **(a)** **Bloc STAR, seat 1:** run ordinary single-winner STAR on all ten ballots. Who wins — and what's odd about the runoff tally?
- **(b)** **Bloc STAR, seat 2:** remove the seat-1 winner and run STAR again. Who joins the board? Characterize the final board in one sentence.
- **(c)** Before touching the proportional count, decide: is (b)'s outcome a *bug*? Write down your answer and your reason.
- **(d)** **Allocated Score:** seat 1 goes to the top scorer, and then a **quota** (10 voters ÷ 2 seats = 5 ballots' worth) of that winner's strongest supporters is *spent*. Work out what's left, then award seat 2. Who's on this board?
- **(e)** Two counts, two boards, zero mistakes. State the rule for choosing between them.

## Solutions

<details>
<summary><b>(a) Seat 1 — Asa, with a 6–0 runoff</b></summary>

```text
Round 1: Scoring Round
   Asa           -- 30 -- First place
   Bram          -- 24 -- Second place
   Cleo          -- 20
   Dane          -- 16
 Asa and Bram advance.

Round 1: Automatic Runoff Round
   Asa           -- 6 -- First place
   Bram          -- 0
   Equal Support -- 4
 Asa wins.
   Voters with a preference: 6 of 10 (4 Equal Support).
```

Both finalists are north-siders, so the runoff is an intramural affair: all six northerners prefer Asa 5 > 4, and the four southerners — who scored the finalists 0–0 — stand aside as Equal Support ([exercise 7](ex07_vanishing_votes.md)'s lesson again). **Asa takes seat 1.**

</details>

<details>
<summary><b>(b) Seat 2 — Bram. The board is a sweep</b></summary>

```text
Round 2: Scoring Round
   Bram          -- 24 -- First place
   Cleo          -- 20 -- Second place
   Dane          -- 16
 Bram and Cleo advance.

Round 2: Automatic Runoff Round
   Bram          -- 6 -- First place
   Cleo          -- 4
 Bram wins.
```

With Asa removed, the north's second choice Bram (24) still outpolls the south's first choice Cleo (20), and the runoff is the neighborhood's raw 6–4 split. **Board: Asa and Bram — the 60% side holds 100% of the seats.** That is Bloc STAR working exactly as specified: every seat answers to the same majority.

</details>

<details>
<summary><b>(c) Is the sweep a bug?</b></summary>

Trick question — it's a *specification*, not a defect. If this board must act as one voice (an executive, a negotiating team), electing the majority's whole slate is defensible and arguably correct. If the board is supposed to *represent the neighborhood*, a 10-voter body where 4 voters have zero seats is malrepresentation by construction. The count didn't decide that; whoever chose the count did. Hold your answer and check it against (e).

</details>

<details>
<summary><b>(d) Allocated Score — the north pays for Asa, and Cleo takes seat 2</b></summary>

```text
Round 1
 The highest-scoring candidate wins a seat.
   Asa           -- 30 -- First place
 Asa wins a seat.

Round 1: Ballot allocation round
 Allocating 6 ballots at score 5.
 This allocation overfills the quota.  Returning fractional surplus.
 Allocating only 83.33% of these ballots.
 Keeping these ballots, but multiplying their weights by 1/6.

Round 2
 The highest-scoring candidate wins a seat.
   Cleo          -- 20 -- First place
   Dane          -- 16
   Bram          --  4
 Cleo wins a seat.
```

Asa wins seat 1 as before — but now his six 5-star supporters are charged a quota of 5 ballots for it. Six ballots share the bill, so each keeps only 1/6 of its weight (the engine narrates the fractional surplus exactly). In round 2 the north's leftover sliver gives Bram just 6 × 1/6 × 4 = **4** points, while the south's four *untouched* ballots give Cleo **20**. **Board: Asa and Cleo — one seat per side**, matching the 60/40 weight of the room. The deeper mechanics (quotas, reweighting, the whole PR family): [the math behind proportional STAR](../../00_start_here/proportional_representation/STAR_PR/the_math_behind_proportional_star.md).

*A live-copy footnote:* BetterVoting's page banners this race "**Tied!** Asa and Cleo won after tiebreaker" — there is no tie. Its `STAR_PR` results object marks the elected pair as "tied" with no round detail on *every* STAR-PR election (the repo's older `jwxr3j` case shows the identical pattern), while the underlying scores here are a clean 30, then 20/16/4. A display quirk of BV's serializer, worth knowing before someone quotes the banner as evidence of anything.

</details>

<details>
<summary><b>(e) The rule</b></summary>

**Ask what the body is for, then pick the count — never the reverse.** Bodies that must *act* (a mayor's office, a bargaining team) suit majoritarian fills like [Bloc STAR](../../02_STAR_Bloc/README.md); bodies that must *deliberate and represent* (a council, this association board) suit proportional fills like [Allocated Score and its siblings](../../03_STAR_PR/README.md). The ten ballots contain both answers; the seat-filling rule is a constitutional choice about whose voice a seat is. Arguing "which board won" without first answering "what is the board for" is the category error this exercise exists to vaccinate against.

</details>

## Reading this fairly

Two clean factions and near-clone running mates — engineered so the philosophies separate perfectly (real electorates blur the boundary and the methods converge accordingly). Note what was *not* varied: same ballots, same honest voters, same engine; the only change was `voting_method`. Per the [four-part test](../../method_comparisons/paradoxes_and_whoops/reading_these_fairly.md), neither result is a "whoops" — this is the rare exercise where both outcomes are working as designed.

## Run it yourself

```
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/exercises/cases/ex12_bloc_sweep.yaml
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/exercises/cases/ex12_proportional_share.yaml
```

Sources: [ex12_bloc_sweep.yaml](cases/ex12_bloc_sweep.yaml) · [ex12_proportional_share.yaml](cases/ex12_proportional_share.yaml). Full audit reports: [bloc](cases/cases_tabulated/ex12_bloc_sweep_tabulated.txt) · [allocated](cases/cases_tabulated/ex12_proportional_share_tabulated.txt).

---

**Where this comes from.** Original to this repo (ballots and cast). Concept homes: [electing more than one](../../00_start_here/topics/electing_more_than_one.md), [Bloc STAR](../../02_STAR_Bloc/README.md), [proportional STAR](../../03_STAR_PR/README.md).

*Back to [the exercises set](README.md) · curriculum home: [Voting 301](../../00_start_here/curriculum/CURRICULUM_301.md)*

# file: ex12_bloc_vs_proportional.md
