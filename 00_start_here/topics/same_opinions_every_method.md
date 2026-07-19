# Same opinions, every method — the line-up

*The clearest way to see what a voting method is *for*: hold the voters' honest opinions fixed, change only the counting rule, and watch where each one lands. Nobody changes their mind; the only variable is how much of the ballot the method reads. Line the results up, and the virtues show themselves.*

→ Its ballot-side twin — the *same voter* on three ballot styles: [one voter, three ballots](ballot_styles.md). The core distinction underneath both: [scores vs. ranks](../scores_and_ranks/scores_vs_ranks.md).

---

## One electorate, honest opinions

Five coworkers pick the team lunch — Sushi, Tacos, or Pizza. Everyone scores each option 0–5, honestly (this is the repo's [canonical lunch vote](../../01_STAR/_main/_main_pages/bv2184_fyy886_lunch_vote.md), [runnable](../../01_STAR/_main/bv2184_fyy886_lunch_vote.yaml) · [live on BetterVoting ↗](https://bettervoting.com/fyy886/results)):

| Voter | Sushi | Tacos | Pizza |
|---|:--:|:--:|:--:|
| Sofia | 5 | 0 | 3 |
| Sam | 5 | 0 | 3 |
| Tara | 0 | 5 | 3 |
| Theo | 0 | 5 | 3 |
| Pat | 3 | 1 | 5 |

Read it and the shape is plain: **two love Sushi, two love Tacos, and everybody is happy with Pizza** — nobody scores it below 3. Pizza is the option the *whole table* can live with; Sushi and Tacos each split the room in half.

## The same opinions, as each ballot

Those honest scores contain every other ballot inside them. The *voters didn't change* — only what the ballot lets them say:

| Voter | Choose-One (top pick) | Ranking (their order) | Approval (all they're OK with) | Score |
|---|:--:|:--|:--:|:--:|
| Sofia | Sushi | Sushi › Pizza › Tacos | Sushi, Pizza | 5·0·3 |
| Sam | Sushi | Sushi › Pizza › Tacos | Sushi, Pizza | 5·0·3 |
| Tara | Tacos | Tacos › Pizza › Sushi | Tacos, Pizza | 0·5·3 |
| Theo | Tacos | Tacos › Pizza › Sushi | Tacos, Pizza | 0·5·3 |
| Pat | Pizza | Pizza › Sushi › Tacos | Sushi, Tacos, Pizza | 3·1·5 |

First choices alone: **Sushi 2, Tacos 2, Pizza 1.** Notice Pizza looks *weakest* by first choices — precisely because it's everyone's happy *second*, not their passion.

## The line-up — who wins under each method

Now count the *same* five ballots every way. (Every winner here is engine-verified on the runnable file above.)

| Method | What it reads | Winner |
|---|---|:--:|
| **Choose-One (Plurality)** | first choices only | Sushi |
| **RCV-IRV (Hare)** | first choices, then eliminate the lowest | Sushi |
| **Approval** | how many are OK with each | 🍕 **Pizza** |
| **[Ranked Robin](../RCV_Ranked_Robin/why_ranked_robin.md)** | every head-to-head matchup | 🍕 **Pizza** |
| **[STAR](Why_STAR_Voting.md)** | total scores, then an automatic runoff | 🍕 **Pizza** |

## What the line-up shows

Three different whole-ballot methods — Approval, Ranked Robin, STAR — **independently land on Pizza**, the choice the whole table is happy with. The two methods that look only at *first choices* pick **Sushi**, which two of the five coworkers rated a flat **0**.

Nobody voted strategically. Nobody changed their opinion. The *entire* difference is **how much of the ballot the method reads**:

- **Choose-One and IRV** decide on first choices, so the broadly-liked compromise — nobody's #1 — never gets its due, and the winner is an option half the room rejected.
- **Approval, Ranked Robin, and STAR** read the whole ballot — approval thresholds, every head-to-head, or scores plus a runoff — and each finds the candidate with real, *broad* support.

That's the case for expressive ballots and whole-ballot counts, in one lunch order: **give voters room to say what they think, then count all of it, and the winner is the one a majority is genuinely glad about.** STAR and Ranked Robin are two roads to that same destination.

---

## Use this view anywhere

The line-up is a *reusable lens*, not a one-off. Any election in this library can be run through it — the point is always the same: hold the opinions fixed, vary the count, and let the method reveal itself. Bigger, real-world line-ups:

- **[Alaska 2022 — one electorate, four counts](../../method_comparisons/alaska_2022/README.md)** — a real federal race where the methods *split* (STAR & Ranked Robin find the consensus candidate; the first-choice methods don't), and its [general-election counterpart](../../method_comparisons/alaska_2022_general/README.md) where they all *agree*.
- **[Burlington 2009](../../method_comparisons/burlington_2009/README.md)** — the same lens on real ranked ballots.
