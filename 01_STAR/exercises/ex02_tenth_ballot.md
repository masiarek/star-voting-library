# Exercise 2 — The tenth ballot

*A small club elects its coordinator with STAR Voting. Nine ballots are counted and a winner is announced — and then a tenth ballot turns up, cast on time and mislaid in the envelope pile. The tenth voter's favorite is the announced winner. Recount with their ballot included: can anything change?*

**You practice:** the scoring round · the runoff pairing · the **[participation criterion](../../00_start_here/topics/participation/README.md)** (the [no-show paradox](../../00_start_here/voting_paradoxes/no_show.md)) · the runoff-slot [spoiler](../../00_start_here/topics/spoiler_effect.md).

Work each part on paper before opening its solution. The YAML files at the bottom are runnable; their `expected_winners` answer keys are regression-tested, and each `_tabulated` mirror is the full audit report.

## The ballots

Nine voters, five candidates, scores 0–5, three ballot styles (rows are candidates, columns are voter blocs):

| | ×4 voters | ×3 voters | ×2 voters |
|---|:---:|:---:|:---:|
| **Alex** | 3 | 3 | 3 |
| **Bella** | 2 | 5 | 1 |
| **Chris** | 4 | 0 | 4 |
| **Dana** | 5 | 0 | 0 |
| **Eli** | 0 | 4 | 5 |

The **tenth ballot**, found after the count: **Alex 5 · Chris 2 · Bella, Dana, Eli 0**.

## Your task

- **(a)** Tabulate the nine counted ballots (STAR: scoring round, then the automatic runoff). Who wins? Would plain Score voting agree?
- **(b)** The tenth voter's favorite is Alex, scored a full 5. **Write down your prediction** for the 10-ballot recount.
- **(c)** Recount with all ten ballots. What happened — at which step, and by how many points? What does the tenth voter think of the outcome?
- **(d)** Back to the original nine ballots. Suppose instead that Bella had withdrawn before the count (ballots unchanged, her column simply removed). Predict, then tabulate.
- **(e)** Parts (c) and (d) flipped the winner the same way. Name the shared mechanism — and which methods are structurally immune.

## Solutions

<details>
<summary><b>(a) The nine counted ballots</b></summary>

Score totals: Alex 9×3 = **27**, Bella 4×2+3×5+2×1 = **25**, Chris 4×4+2×4 = **24**, Eli 3×4+2×5 = **22**, Dana 4×5 = **20**. Alex and Bella advance; six voters score Alex above Bella (the ×4 and ×2 blocs), three the reverse.

```text
Scoring Round
 The two highest-scoring candidates advance to the next round.
   Alex          -- 27 -- First place
   Bella         -- 25 -- Second place
   Chris         -- 24
   Eli           -- 22
   Dana          -- 20
 Alex and Bella advance.

Automatic Runoff Round
 The candidate preferred in the most head-to-head matchups wins.
   Alex          -- 6 -- First place
   Bella         -- 3
   Equal Support -- 0
 Alex wins.
   Voters with a preference: 9 of 9 (no Equal Support).
   Alex 6 (67%) vs Bella 3 (33%); majority = 5.
```

**Winner: Alex** — and yes, plain Score agrees (Alex leads the totals, 27).

</details>

<details>
<summary><b>(b) The prediction</b></summary>

The trap reads: "the ballot gives Alex the maximum and his rivals almost nothing — it can only help Alex." Write your answer down, then open (c).

</details>

<details>
<summary><b>(c) The recount — helping your favorite hurts him</b></summary>

New totals: Alex 27+5 = **32**, Chris 24+2 = **26**, Bella 25+0 = **25**, Eli 22, Dana 20. Alex's lead *grows* — but the tenth ballot's 2 points for Chris nudge him past Bella (26 vs 25) into the runoff. And the Alex-vs-Chris matchup was never Alex's: the ×4 and ×2 blocs all score Chris 4 > Alex 3.

```text
Automatic Runoff Round
 The candidate preferred in the most head-to-head matchups wins.
   Chris         -- 6 -- First place
   Alex          -- 4
   Equal Support -- 0
 Chris wins.
   Voters with a preference: 10 of 10 (no Equal Support).
   Chris 6 (60%) vs Alex 4 (40%); majority = 6.
```

**Winner: Chris.** The tenth voter cast an honest ballot for their favorite and thereby demoted him from winner to runner-up — had the ballot stayed lost, Alex wins. That is a **participation failure** (the no-show paradox): the ballot didn't change how much voters like Alex (he still tops the scores, 32); it changed **which question the runoff asks** — Alex-vs-Bella became Alex-vs-Chris. Under plain Score voting the recount is harmless: Alex still leads, 32 to 26.

</details>

<details>
<summary><b>(d) Bella withdraws — the shield effect</b></summary>

Remove Bella's column from the original nine ballots and nothing else moves: Alex **27**, Chris **24**, Eli 22, Dana 20. Chris inherits the second runoff slot — and beats Alex head-to-head 6–3.

```text
Scoring Round
 The two highest-scoring candidates advance to the next round.
   Alex          -- 27 -- First place
   Chris         -- 24 -- Second place
   Eli           -- 22
   Dana          -- 20
 Alex and Chris advance.

Automatic Runoff Round
 The candidate preferred in the most head-to-head matchups wins.
   Chris         -- 6 -- First place
   Alex          -- 3
 Chris wins.
```

**Winner: Chris.** Bella was never going to win, yet her *presence* decided who does — she occupied the runoff slot that Chris wins from. The familiar spoiler is a loser whose presence *hurts* a similar candidate; Bella is the mirror image, a loser whose presence *protected* the winner. Same family: the outcome depended on an (irrelevant) alternative.

</details>

<details>
<summary><b>(e) The shared mechanism — and who is immune</b></summary>

Both flips are **runoff-slot events**: nothing changed Alex's standing in the scoring round (he leads it in all three variants), but a one-or-two-point perturbation — one extra ballot, one withdrawn also-ran — swapped **who he must face**, and Chris beats him head-to-head in every variant. The runoff is the same feature that gives STAR its majoritarian bite (see [Runoff Reversal](../runoff_overturns_leader/README.md)); these are the criteria it costs.

Structurally immune to participation failures: the pure point-summing methods — **Score** and **Approval** (and Choose-One) — where an extra supportive ballot can only add to your favorite's total. Score elects Alex in all three variants of this exercise. Not immune: STAR, RCV-IRV, top-two runoffs, and Condorcet methods. The honest scorecard, including how *rarely* STAR's version bites compared to IRV's elimination machinery, is the [Participation topic hub](../../00_start_here/topics/participation/README.md)'s job — and note the repo's live multi-method pair ([participation_no_show](../../method_comparisons/participation_no_show/README.md)), where the *same* sincere ballots reward the voters under STAR and punish them under RCV-IRV. This exercise is the deliberately-constructed counterpoint: the rare STAR-side failure, so the claim "STAR fails participation too, far more rarely" comes with a runnable example instead of a hand-wave.

</details>

## Five methods, four winners

A closing curiosity from the engine's `[Divergence from STAR]` block on the *base* nine ballots: this little electorate splits the methods four ways — Choose-One elects **Dana**, RCV-IRV elects **Bella**, Ranked Robin elects **Eli**, and STAR (with Score agreeing) elects **Alex**. Engineered ballots disagree loudly; which notion of "best winner" should prevail is [three winner notions](../../00_start_here/STAR_Voting/properties_and_limits/STAR_three_winner_notions.md)' question.

## Reading this fairly

A constructed classroom electorate with one-point margins — it demonstrates the *mechanism* honestly and says nothing about *frequency*. Every method fails something; what matters is which failures, how often, under sincere votes. Apply [the four-part test](../../method_comparisons/paradoxes_and_whoops/reading_these_fairly.md) before turning any single construction into a verdict, and see [STAR's honest limits](../../00_start_here/STAR_Voting/properties_and_limits/STAR_honest_limits.md) for the balanced scorecard.

## Run it yourself

```
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/exercises/ex02_nine_ballots.yaml
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/exercises/ex02_tenth_ballot.yaml
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/exercises/ex02_bella_exits.yaml
```

Sources: [ex02_nine_ballots.yaml](ex02_nine_ballots.yaml) · [ex02_tenth_ballot.yaml](ex02_tenth_ballot.yaml) · [ex02_bella_exits.yaml](ex02_bella_exits.yaml). Full audit reports: [nine ballots](exercises_tabulated/ex02_nine_ballots_tabulated.txt) · [ten ballots](exercises_tabulated/ex02_tenth_ballot_tabulated.txt) · [Bella withdraws](exercises_tabulated/ex02_bella_exits_tabulated.txt).

---

**Where these ballots come from.** Adapted (candidates renamed, prose our own) from a worked example published on [RangeVoting.org](https://rangevoting.org) — a Score-voting advocacy site, so its framing favors Score; the arithmetic is method-neutral — and posed as an add-a-voter exercise in Brendan W. Sullivan, *An Introduction to the Math of Voting Methods* (619 Wreath Publishing, 2022), ch. 5, a method-neutral general-education textbook whose practice-problems-with-solutions format this exercises set borrows.

*Back to [the exercises set](README.md) · curriculum home: [Voting 301](../../00_start_here/curriculum/CURRICULUM_301.md)*

# file: ex02_tenth_ballot.md
