# Choose-One (Plurality) — the simplest count there is

*Mark one box. Count the marks. Most marks wins. That's the whole method — and this folder is about what it can and cannot do, using an election small enough to fit on a napkin.*

Choose-One (also **Plurality**, **First-Past-The-Post**, or just "the ballot you already know") is the method almost every reader grew up with. It earns its place: it is the easiest to explain, the easiest to hand-count, and nobody needs a lesson to fill it out. Everything else on this page is about the price of that simplicity.

---

## The silly election

Five coworkers are picking lunch. Three options. One box each.

```
                   Sushi  Tacos  Pizza
  Sushi-lover        X      -      -
  Sushi-lover        X      -      -
  Taco-lover         -      X      -
  Taco-lover         -      X      -
  Pizza-fan          -      -      X

  Count the marks:  Sushi 2 · Tacos 2 · Pizza 1
```

And that is the entire count. **Sushi 2, Tacos 2 — a dead tie**, and the ballots have nothing left to say. There is no second round to run, no second preference to look at, no head-to-head to check, because none of that was ever collected. A choose-one ballot holds exactly one bit per voter, and both bits are spent.

So the winner is decided by the **pre-published lot order**:

```
 A 2-way tie for first: Sushi, Tacos — 2 mark(s) each.
   Counting the marks is all a choose-one ballot can do, so the ballots cannot break it;
   the pre-published lot order decides: ['Sushi', 'Tacos', 'Pizza'].

[Lot-decided tie — rare]
  ⚠ The result here was set by lot, not by the votes.

Winner — Choose-One / Plurality Voting Method (single winner)
 Sushi   (2 of 5 marks, by lot)
```

Five people, one lunch, and the answer came out of a hat.

**Run it:** [reader page](cases/cases_pages/lunch_choose_one_dead_tie.md) · [`lunch_choose_one_dead_tie.yaml`](cases/lunch_choose_one_dead_tie.yaml)

## The voter who could have fixed it

Look again at the Pizza-fan. Theirs is the only ballot that could break the tie — they are the one person in the room with no stake in Sushi-vs-Tacos, so their opinion is exactly the tiebreaker the election needs.

**The ballot gave them no way to say it.** Their single mark went to Pizza, who cannot win, and about the two who *can* win they were never asked. That isn't a bad voter or a bad strategy; it is the ballot refusing to carry the information.

## The same five people, on a ballot that asks more

These are the [canonical team-lunch voters](../../01_STAR/_main/cases/cases_pages/bv2184_fyy886_lunch_vote.md) — same people, same opinions, no strategy anywhere. Hand them a 5-star ballot and they say considerably more:

| Voter | Sushi | Tacos | Pizza |
|---|:--:|:--:|:--:|
| Sushi-lover | 5 | 0 | 3 |
| Sushi-lover | 5 | 0 | 3 |
| Taco-lover | 0 | 5 | 3 |
| Taco-lover | 0 | 5 | 3 |
| Pizza-fan | 3 | 1 | 5 |

Now the Pizza-fan's *"Sushi over Tacos"* is on the ballot, and so is everyone's quiet **"…Pizza is fine, actually"** — four voters rate it a 3. [STAR](../../00_start_here/STAR_Voting/STAR_start_here.md) elects **Pizza**, the one lunch nobody objects to, and no lot is needed. Same electorate, same opinions: the entire difference is **how much the ballot let them say.**

That's the honest comparison to draw here — not "Choose-One is stupid." It counted its ballots perfectly. It just wasn't given much to count.

## What to take away

- **Choose-One is not wrong, it is thin.** One bit per voter. Every method downstream of that ballot has the same one bit to read.
- **Ties are structural, not bad luck.** With no preference data there is nothing to break a tie with, so small elections land on the lot more often than you'd guess.
- **The fix is the ballot, not the arithmetic.** Ask voters for order, or for strength, and the same people resolve the same election themselves.
- **Publish the lot order in advance.** If the ballots *can't* decide, something has to — and it must be a rule set before the vote, not a coin found afterwards.

## Related

- [Plurality — the topic page](../../00_start_here/topics/plurality.md) — the family, the terms, the failure modes
- [Minority winner](../../method_comparisons/minority_winner/README.md) — the other classic Choose-One story: 34% wins while two-thirds wanted someone else
- [Same matrix, different plurality](../../method_comparisons/same_matrix_different_plurality/README.md) — three electorates that look identical to Choose-One
- [Multi-member plurality](../../method_comparisons/multi_member_plurality/README.md) — Block Voting, Limited Voting, SNTV
- [The traditional voting style](../../00_start_here/STAR_Voting/voting_styles/traditional.md) — what happens when voters bring the choose-one habit to a 5-star ballot

---

Up: [06_Other — other methods & engines](../README.md)

# file: README.md
