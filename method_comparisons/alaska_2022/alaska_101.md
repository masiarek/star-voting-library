# Alaska 2022 · 101 — what happened, in plain language

*The goal of this page: understand the basic story with **zero jargon**. If you finish it and can explain "why the guy who beat everyone still lost" to a friend, it worked. The [201 page](alaska_201.md) then shows the exact vote math, and [301](alaska_301.md) goes deep (and asks whether this is fair to point out).*

Companion: run it yourself → [the four-count model](README.md) · see the real election → Equal Vote's [Real RCV](https://realrcv.equal.vote/alaska22).

---

## The cast

August 2022, Alaska's one seat in the US House. Three candidates, lined up left to right by politics:

- **Mary Peltola** — the left / Democrat
- **Nick Begich** — the center-right
- **Sarah Palin** — the right

Voters ranked them (1st, 2nd, 3rd). The method was **RCV-IRV** — ranked ballots, counted by *instant runoff*.

## The one rule you need

Instant runoff works like a reality-show elimination:

> Each round, **whoever has the fewest 1st-place votes is eliminated.** Their ballots move to each voter's next choice. Repeat until someone has more than half.

That's it. The whole story below follows from that one rule.

## What happened, step by step

**Round 1 — count everyone's 1st choice:**

| Candidate | 1st-place votes (model) |
|---|---:|
| Peltola | 80 |
| Palin | 63 |
| **Begich** | **57 ← fewest** |

Begich has the fewest first-place votes, so **Begich is eliminated.**

**Round 2 — Begich's ballots move to their next choice.** Now it's just Peltola vs Palin, and **Peltola wins.**

So the winner is **Peltola.** Simple enough. Here's the problem.

## The twist — Begich beat *both* of them

Ask a different question — not "who has the most firsts," but **"in a one-on-one race, who wins?"**

- **Begich vs Peltola?** Palin's voters mostly prefer the center guy over the left one, so **Begich wins.**
- **Begich vs Palin?** Peltola's voters mostly prefer the center guy over the right one, so **Begich wins.**

Begich beats **each** opponent head-to-head. A majority preferred him to Peltola, *and* a majority preferred him to Palin. By that measure he's the candidate the most people actually wanted.

**But instant runoff never ran those one-on-one races.** It eliminated Begich in Round 1 — before he could face anyone one-on-one — just because he had the fewest *first* choices.

## Why the middle candidate had so few firsts

This is the whole idea, so slow down here:

Peltola and Palin are the **exciting, polarizing** picks — each has a devoted base that ranks them #1. Begich is the **compromise** — the guy lots of people put **2nd**. "I love my side's candidate, but I can live with Begich."

Being everyone's acceptable **second choice** wins you *head-to-head* matchups… but it earns you very few **first**-place votes. And instant runoff only looks at first choices when it decides who to eliminate. So the compromise candidate gets knocked out **early** — before his mountain of second-choice support ever gets counted.

That's called the **center squeeze**: the broadly-liked middle is "squeezed out" between two stronger wings.

## The one-sentence version

> **Instant runoff rewards being someone's *favorite*, not being *everyone's acceptable choice* — so it eliminated the candidate a majority actually preferred, before he ever got a head-to-head vote.**

## Would other methods do the same?

No — and that's the point of this whole library:

- **[Ranked Robin](../../00_start_here/RCV_Ranked_Robin/ranked_robin.md)** (a different way to count the *same* ranked ballots) checks every one-on-one matchup directly. It sees Begich beat both → **Begich wins.**
- **[STAR](../../00_start_here/STAR_Voting/STAR_start_here.md)** (a scored ballot) adds up how highly everyone rated each candidate. Begich's pile of "2nd-choice" support shows up as lots of 4s → he reaches the final → **Begich wins.**

Same voters, same opinions. The **ballot** wasn't the problem; the **way IRV counts it** — eliminating on first choices — was.

---

## Challenge your understanding

Try to answer before opening each one.

<details><summary><strong>Q1.</strong> In one sentence, why was Begich eliminated first?</summary>

Because instant runoff eliminates whoever has the fewest **first**-place votes, and Begich — the compromise candidate most people ranked *second* — had the fewest firsts (57, vs Peltola 80 and Palin 63).
</details>

<details><summary><strong>Q2.</strong> Begich lost the election, yet he "beat both other candidates." How can both be true?</summary>

Two different questions. **The election** was run by instant runoff, which eliminated him in Round 1 on first-choice counts. **"Beat both"** means head-to-head: in a one-on-one Begich-vs-Peltola race a majority picks Begich, and in Begich-vs-Palin a majority picks Begich. IRV simply never held those one-on-one races, because it removed Begich before the final.
</details>

<details><summary><strong>Q3.</strong> Why did the compromise candidate have so few first-place votes?</summary>

Because a compromise is rarely anyone's *passion*. Peltola and Palin each had a devoted base ranking them #1; Begich was the guy both sides put **2nd** ("I can live with him"). Broad acceptability earns second-place rankings, not first-place ones — and IRV eliminates on firsts.
</details>

<details><summary><strong>Q4.</strong> Would Ranked Robin or STAR have elected Peltola too?</summary>

No — both elect **Begich**. Ranked Robin checks every head-to-head (Begich beats both), and STAR adds up scores (Begich's broad second-choice support piles up and carries him through the runoff). The difference is that neither one eliminates candidates on first-choice counts, which is the step that squeezed Begich out.
</details>

**Got all four?** Move on to [201 — the exact vote math](alaska_201.md), where we count the real rounds and the head-to-head numbers.
