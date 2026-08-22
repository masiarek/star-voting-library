# Teach vote splitting — a plan for 101, 201 and 301

**Level: 101 → 301 · for presenters**

*Everything on this page is presenter-facing: what to say, what to show, what the room will ask back. The learner-facing version of the same material is [Vote splitting & the spoiler effect](README.md).*

→ Companion presenter pages: [Teaching STAR Voting](../../01_STAR/01_Learn/hands_on/teaching_star_voting.md) · [Run a paper-ballot demo](../../01_STAR/01_Learn/hands_on/running_a_paper_ballot_demo.md) · [Count a STAR election by hand](../../01_STAR/01_Learn/hands_on/count_star_by_hand.md)

---

## The one rule that determines everything else

**Open in Choose-One. Every time.**

Vote splitting is a *failure of choose-one voting*. STAR cannot demonstrate it, because under STAR nothing splits — so a lesson that opens with STAR is describing a problem the room has never felt, and teaching the cure as a feature rather than as a repair. Let the split happen to your audience first. Then fix it.

And when you fix it, the sentence is **not** *"STAR counts better."* It is:

> **Choose-One did not miscount those votes. It never asked the question whose answer would have changed the result.**

That reframes every reform on the table from *a better calculator* to *a better question* — which is both more accurate and much harder to argue with.

## The three live elections you will use

All three are real BetterVoting elections. Put the results link on screen; the room can follow along on their phones.

| | Election | Size | The number | Level |
|---|---|:--:|---|:--:|
| **BV2294** | [The smallest spoiler ↗](https://bettervoting.com/vjp3fj/results) · [vote](https://bettervoting.com/vjp3fj) | 3 cand × 7 | Vanilla wins on **43%** | 101 |
| **BV2293** | [Seven apples and a banana ↗](https://bettervoting.com/vq78wk/results) · [vote](https://bettervoting.com/vq78wk) | 8 cand × 9 | Banana wins on **22%** | 201 |
| **BV2295** | [Fizzy or sweet? ↗](https://bettervoting.com/8xrpyp/results) · [vote](https://bettervoting.com/8xrpyp) | 7 cand × 7 | Two same-size groups, opposite verdicts | 301 |

Every race is cross-checked: **BetterVoting and the LH engine agree on all eleven.**

---

## 101 — feel the split, then fix it

**Objective:** the room can explain, in their own words, why a group that agrees can lose to a group that is smaller.

**Level: 101 · for voters**

| # | Rung | Use | What they should feel |
|:-:|---|---|---|
| 1 | Two candidates — nothing can split | [`07a`](_main/_main_pages/07a_apples_two_candidates.md) | Majority rule. Every method agrees. *This is the baseline.* |
| 2 | The smallest spoiler | [`08a`](_main/_main_pages/08a_smallest_spoiler_plurality.md) · [BV ↗](https://bettervoting.com/vjp3fj/results) | Vanilla wins on 43% — and every chocolate lover had it **last** |
| 3 | The same seven friends, scoring | [`08b`](_main/_main_pages/08b_smallest_spoiler_star.md) | The information was there all along; the ballot just never collected it |

**They can now do:** spot the shape (several similar options, one distinct one) on a real ballot, and say why the winner's percentage matters.

**Do not yet introduce:** Condorcet winners, center squeeze, IIA, or any method beyond Choose-One and STAR. Rung 3 is the payoff; stop there.

## 201 — when does it actually bite?

**Objective:** the room can tell a *spoiled* election from a merely *sub-majority* one — and knows that the difference cannot be read off the result sheet.

**Level: 201 · deep dive**

This level is the one most explanations skip, and skipping it is what makes the whole argument fragile.

| # | Rung | Use | The point |
|:-:|---|---|---|
| 1 | Six names: the vote splits and **costs nothing** | [`07b`](_main/_main_pages/07b_apples_six_candidates.md) | Gala wins on **33%**, apple vote divided five ways, and nothing went wrong. **Splitting ≠ spoiled.** |
| 2 | Eight names: now it costs everything | [`07c`](_main/_main_pages/07c_apples_full_menu.md) | Banana on **22%** while 78% wanted an apple |
| 3 | Name the spoilers | same | Pink Lady and McIntosh got **one vote each**. Neither could win. Both changed who did. *That is the definition.* |
| 4 | The same nine voters, expressively | [`07d` STAR](_main/_main_pages/07d_apples_full_menu_star.md) · [`07e` Approval](_main/_main_pages/07e_apples_full_menu_approval.md) · [`07f` RCV-IRV](_main/_main_pages/07f_apples_full_menu_irv.md) | All of them elect Gala. Under STAR, Banana finishes **last of eight** |
| 5 | The control | [`06`](_main/_main_pages/06_sub_majority_not_spoiled.md) | A 41% winner that nothing spoiled — same warning signs, opposite verdict |
| 6 | STAR's own limit | [`05a`](_main/_main_pages/05a_residual_split_bullet-voting.md) → [`05b`](_main/_main_pages/05b_residual_split_expressive-fix.md) | A faction that bullet-votes can still split itself. The cure is in the voters' hands |

**They can now do:** look at "winner took 34%" in a news report and say *"that's a screening flag, not a finding — you'd need the preference data to know."*

**The fairness beat, and do not skip it:** rung 4 shows **RCV-IRV fixing this spoiler**. It does. Ending the classic spoiler is what instant-runoff was built for. Its own well-known failure is [center squeeze](../../06_Other/RCV_IRV/concepts/RCV_IRV_center_squeeze.md) — a *different* thing — and this election is not an example of it. A room that catches you overselling stops believing the parts that are true.

## 301 — you cannot read a spoiler off a candidate list

**Objective:** the room can explain why a clone set is defined by voters rather than by categories, and why that makes spoilers unpredictable in advance.

**Level: 301 · for debaters**

| # | Rung | Use | The point |
|:-:|---|---|---|
| 1 | Two groupings, same size | [`09a`](_main/_main_pages/09a_clones_are_voters_not_labels.md) · [BV ↗](https://bettervoting.com/8xrpyp/results) | Fizzy 4/7, sugar 4/7 — Choose-One elects Diet Cola on 29% |
| 2 | The same ballots, grouped the other way | [`09b`](_main/_main_pages/09b_same_ballots_grouped_by_label.md) | Identical election, **opposite verdict**. A category is not a clone set |
| 3 | Spoiler ≠ IIA ≠ center squeeze | [spoiler effect](../../07_Concepts/topics/spoiler_effect.md) | Three distinct things routinely conflated in argument — in both directions |
| 4 | Deliberate splitting | [ex11 — recruit a spoiler](../../01_STAR/05_Practice/ex11_recruit_a_spoiler.md) | Run it as a *strategy* problem: which ballot designs is the attack worth mounting against? |
| 5 | How often, honestly | [the 2022 count](how_often_does_vote_splitting_happen.md) | 11.9% of US primaries had the *setup*. That is not a count of spoiled elections |

**They can now do:** argue the case without overclaiming — including conceding the cases where nothing was spoiled.

---

## The ten-minute demo, beat by beat

No slides needed. A whiteboard and seven imaginary friends.

**0:00 — Set it up.** *"Seven of us are splitting a tub of ice cream. Three flavours: milk chocolate, dark chocolate, vanilla. Everybody gets one vote. Fair?"* Wait for the nods. Everyone agrees this is fair, and you want that on the record.

**1:00 — Show the room, not the ballot.** Write the seven people's actual opinions on the board:

```text
2 friends:  milk chocolate first, dark chocolate a close second, no vanilla
2 friends:  dark chocolate first, milk chocolate a close second, no vanilla
3 friends:  vanilla, and they don't much like chocolate
```

Ask: *"Before we vote — what does this group want?"* Let someone say "chocolate." **Four of the seven want chocolate. Say the number out loud.**

**2:30 — Vote.** One mark each. Write the tally as it comes:

```text
Vanilla          3
Milk Chocolate   2
Dark Chocolate   2
```

**3:30 — The pause.** Do not explain yet. Ask: *"Who won?"* Then: *"Who did this room want?"* Let the gap sit there for a beat. Someone will say it before you do.

**4:30 — Name it.** *"Four of you wanted chocolate. All four ranked vanilla last. Vanilla won with three. Nobody cheated, nobody miscounted, nobody voted strategically. The chocolate four were simply not allowed to say they'd take either one."*

**6:00 — The key sentence.** *"Choose-One didn't count your votes wrong. It never asked the question whose answer would have changed the result."*

**6:30 — Fix it.** Same seven friends, score every flavour 0–5:

```text
Milk Chocolate  20      Dark Chocolate  18      Vanilla  15
Runoff:  Milk Chocolate 4  ·  Vanilla 3
```

*"Same people. Same opinions. Nothing added except the ability to say 'I'd take either.'"*

**8:00 — Land it.** *"Now imagine that's not ice cream."* Stop. Do not name a party or a candidate — the room will do it themselves, and it lands far harder when they do.

**9:00 — Take questions.** See the objections list below.

### The one moment this demo fails, and the recovery

Someone says: **"But those two chocolates are basically the same thing — of course that's a stupid ballot."**

They are right, and it is the best thing that can happen to you. Do not defend the ballot. Say:

> *"Exactly — and that's the whole problem. Under choose-one voting, offering people more of what they want is a disadvantage. That's why parties spend so much effort clearing their own primary field, and why a good candidate gets told not to run. The ballot punishes the side with more choices."*

That turns the objection into your strongest point. Have it ready; you will get it most times you run this.

---

## The forty-five minute workshop

**Materials:** printed ballots (see [Run a paper-ballot demo](../../01_STAR/01_Learn/hands_on/running_a_paper_ballot_demo.md) for the generator), a whiteboard, the three BV links on screen.

| Time | What |
|:--:|---|
| 0–10 | The ten-minute demo above, run live with the room's own votes on paper |
| 10–20 | **Hand-count it together.** Choose-One first (stacks of paper), then the scoring round, then the runoff pile-sort — three piles: *prefers A*, *prefers B*, *[Equal Support](../../07_Concepts/GLOSSARY.md)*. The pile-sort is the fastest way to make the runoff physical |
| 20–30 | **The ladder**, on screen: [BV2293 ↗](https://bettervoting.com/vq78wk/results). Two names → six names → eight names. Ask them to predict the winner at each step *before* you reveal it. Most rooms get rung 2 wrong — they expect the split to bite immediately, and it doesn't |
| 30–38 | **What each method does** with the same nine ballots — STAR, Approval, RCV-IRV, Ranked Robin, all electing Gala. Say plainly that RCV-IRV fixes this one |
| 38–45 | **The honest half:** the control case (a 41% winner nothing spoiled) and STAR's residual split. Close on what splitting does *before* anyone votes |

**If you only have 20 minutes:** demo + hand-count. Drop the ladder.
**If you only have 5:** rungs 2 and 3 of 101. The tally and the fix. Nothing else.

---

## What splitting does before anyone votes

The arithmetic is the setup. The damage is behavioural, and it is worth two minutes at the end of any session:

1. **Voters abandon their favourite.** "Don't waste your vote" is not cynicism — under choose-one it is *correct advice*, which is what makes it corrosive. (→ [favorite betrayal](../../01_STAR/01_Learn/properties_and_limits/favorite_betrayal_voting_301.md))
2. **Parties ration candidates.** Clearing the field, pressuring people out of primaries, endorsing early — all of it is rational defence against splitting, and all of it narrows what voters get to choose from.
3. **Good candidates never run at all.** The deepest harm, and the only one that leaves no trace in any result sheet. Say so honestly: it cannot be measured, which is exactly why it goes unmentioned.

Point (3) is the strongest closing line available and the easiest to overclaim. State it as what it is — a structural incentive whose effects are invisible by construction — not as a statistic.

---

## Objections, and fair answers

Concede the true part first, every time. A defensive answer loses the room faster than the objection did.

**"You rigged the ballot — two chocolates and one vanilla."**
Yes. And under choose-one that rigging is *real and permanent*: the side offering more options is at a disadvantage. That is the finding, not a trick in the setup.

**"That's just independence of irrelevant alternatives, a theoretical criterion."**
[IIA](../../07_Concepts/GLOSSARY.md) and the spoiler effect are genuinely different things and it is fair to insist on the distinction. But the distinction cuts both ways: what happened here is not a theoretical axiom violation, it is four people who wanted chocolate getting vanilla. Whether a criterion is "theoretical" is decided by whether it changes real outcomes, and this one did.

**"RCV already fixes this."**
For this election, it does — and our own ranked count elects Gala. Say so. Instant-runoff was built to end the classic spoiler and it ends it. The open question is a different failure ([center squeeze](../../06_Other/RCV_IRV/concepts/RCV_IRV_center_squeeze.md)), plus what happens to ballots that stop counting. Do not blur the two to win a point.

**"So STAR is immune to vote splitting?"**
No, and the honest version is better: STAR removes **forced** splitting — you are never made to choose between allies. A faction that bullet-votes can still split *itself* ([`05a`](_main/_main_pages/05a_residual_split_bullet-voting.md)). The cure is in the voters' hands, which is a real difference from choose-one, where it isn't.

**"This never happens in real elections."**
About 11.9% of 2022 US primaries had a multi-candidate field and a sub-majority winner — the *setup*. That is not a count of spoiled elections, and anyone quoting it as one is overreaching. [The honest reading](how_often_does_vote_splitting_happen.md).

**"The winner got 34%, so that election was spoiled."**
Not necessarily, and this is where the argument is usually lost. A sub-majority winner may be exactly who the majority preferred — see the [control case](_main/_main_pages/06_sub_majority_not_spoiled.md). Telling the two apart needs preference data that a one-mark ballot never collects.

**"Just hold a runoff / a primary."**
A top-two runoff fixes it only if the right two make the top two — and vote splitting is precisely what decides who does. A primary moves the split earlier rather than removing it; that is why parties work so hard to manage their own.

**"Wouldn't people just coordinate?"**
They do, constantly — that *is* the coordination cost. Endorsements, withdrawals, "electability" arguments and lesser-evil voting are all the system working as designed. The question is whether that work should be forced on voters and parties, or done by the ballot.

**"Isn't this just about third parties?"**
No — it is about *any* two similar candidates, which is most often two candidates of the same party in a primary. Framing it as a third-party problem understates it.

---

## Checks for understanding

**101** — 1. Four of seven wanted chocolate. Who won, and why? · 2. Did anyone vote dishonestly? · 3. What could the chocolate voters *not* say on the choose-one ballot? · 4. What changed between the two counts — the people, or the ballot? · 5. Why can't this happen with only two candidates?

**201** — 1. At rung 2 the winner had 33% and the vote was split five ways. Was that election spoiled? *(No — the apple side still won.)* · 2. Which two candidates spoiled rung 3, and how many votes did each get? *(Pink Lady and McIntosh, one each.)* · 3. Banana won under Choose-One and finished last of eight under STAR. Is that a contradiction? *(No — different questions.)* · 4. Does RCV-IRV fix this election? *(Yes.)* · 5. Name one thing that would make you say a sub-majority winner was *not* spoiled. · 6. How could a STAR election still split a faction? *(Bullet-voting.)*

**301** — 1. Fizzy and sugar both hold 4 of 7 first choices. Why is only one a clone set? · 2. Could you have predicted the spoiler from the candidate list alone? *(No — you need the ballots.)* · 3. Give a case that is a spoiler but not a center squeeze, and one that is the reverse. · 4. Someone says "the fizzy vote will split three ways." What do you ask for? *(The ballots.)* · 5. Why is "STAR is immune to vote splitting" wrong, and what is the accurate claim?

**The question that separates memorisation from understanding** is 201.1 and 201.5. A learner who answers "yes, spoiled" to a 33% winner has learned a slogan. A learner who asks for the preference data has learned the concept.
