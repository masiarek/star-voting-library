# DRAFT v3 — six vote-splitting scenarios: many candidates, fewest ballots

*Scratch. Nothing registered, linked, indexed, or on BetterVoting. `_notes/` is in the generators' skip list. Pick one (or two) and I'll promote it properly.*

```bash
.venv/bin/python STARVote_LH_tabulation_engine/starvote_larry_hastings.py "_notes/DRAFT_vote_splitting_options/5_fruit_basket.yaml"
```

---

## "As few votes as reasonable" has an exact answer

Vote splitting needs a family of *k* similar candidates plus a rival, where **every family member polls below the rival**. The cheapest way to buy that: give each family member **exactly one** first choice and the rival **two** — two being the smallest number that beats one.

> **Floor: N candidates need N + 1 voters.** One per candidate, plus one for the rival.
> The winner's share is then `2/(N+1)` — so **more candidates makes the number more extreme while the ballot count barely moves.**

Then three demo conditions, checked on all six below:

1. **Every voter fits on one slide** — ≤ ~12 rows.
2. **No ties, no round decided by one vote** — a tiebreak rung invites a question you didn't want to take during a demo.
3. **Zero Equal Support in the runoff** — otherwise the first question is "what's that row?" instead of "wait, why did *banana* win?"

**All six have zero Equal Support.**

---

## The six

| | Scenario | Cands | Voters | Choose-One elects | on | STAR | Runoff | Rival's rank on score |
|---|---|:--:|:--:|---|:--:|---|:--:|:--:|
| **5** | [**The fruit basket**](5_fruit_basket.yaml) ⭐ | **8** | **9** | **Banana** | **22%** | Gala | 6–3 | **last of 8** |
| 1 | [Ice cream counter](1_ice_cream_counter.yaml) | 8 | 9 | Vanilla | 22% | Milk Chocolate | 6–3 | last of 8 |
| **6** | [**Left1 / Center1 / Right1**](6_factions.yaml) ⭐ | 7 | 9 | **Right1** | 33% | Center1 | 5–4 | 4th of 7 |
| 4 | [Pizza toppings](4_pizza_toppings.yaml) | 7 | 8 | Mushroom | 25% | Pepperoni | 7–1 | last of 7 |
| 2 | [Coffee menu](2_coffee_menu.yaml) | 7 | 8 | Drip Coffee | 25% | Latte | 7–1 | last of 7 |
| **3** | [**Fizzy or sweet?**](3_fizzy_or_sweet.yaml) + [3b](3b_fizzy_label.yaml) ⭐ | 7 | **7** | Diet Cola | 29% | Cola | 4–3 | 4th of 7 |

---

## 5 — The fruit basket ⭐ *the pick*

**Seven apples and a banana. Nine people.** Every apple eater has a different variety, so each apple collects exactly one first choice. The two banana eaters agree.

```text
First choices:  Banana 2  ·  every apple 1
                -> Banana wins Choose-One with 2 of 9 — 22% —
                   while 7 of the 9 (78%) came in wanting an apple.

Scoring round:  Gala 29 · Granny Smith 24 · Fuji 17 · Honeycrisp 16 · McIntosh 16
                Pink Lady 13 · Red Delicious 12 · Banana 11   <- LAST of eight
Runoff:         Gala 6 · Granny Smith 3 · Equal Support 0
```

**This supersedes option 1.** Identical arithmetic — same 22%, same 8 candidates, same 9 ballots, same 6–3 runoff, rival last on score — but the family membership is **not arguable**. "Is Rocky Road really chocolate?" is a debate someone will start during your demo. "Is a Honeycrisp really an apple?" is not. That single difference is worth the swap, and it's the objection I flagged against the ice cream version.

It also survives the hostile reading. *"You rigged it — seven apples and one banana!"* Yes: and under Choose-One that is a real, permanent disadvantage for apples, which is the entire lesson. **Choose-one voting punishes the side that gives voters more options.**

## 6 — Left1 / Center1 / Right1 ⭐ *your abstract-labels idea, and it works*

**Nine voters, seven candidates, names that do their own explaining.** Two on the left, four in the centre, one on the right. Every candidate except Right1 has exactly one first-choice supporter; the right is consolidated and all three of its voters mark Right1.

```text
First choices:  Right1 3  ·  everyone else 1
                -> Right1 wins Choose-One with 3 of 9 (33%) — the one candidate
                   the other six voters rank at or near the bottom.

Scoring round:  Center1 25 · Center2 23 · Center3 21 · Center4 21
                Right1 17  <- 4th of seven · Left1 15 · Left2 15
Runoff:         Center1 5 · Center2 4 · Equal Support 0
```

**Why it's genuinely good:** the labels remove every argument about who is similar to whom, which is the weakness of *all* the food scenarios — and it's the case people actually care about. It also shows something the food ones can't: the Choose-One winner isn't merely "not the majority's pick", it's the candidate **most of the room likes least**.

**Two honest notes.** The engine reports the Centre bloc as *"more than the plurality winner (4 vs 3)"* rather than *"an outright majority"* — 4 of 9 is 44%. The stronger framing is available in the same ballots: **Left + Centre = 6 of 9 (67%) rank Right1 last.** And the house style reserves abstract names for academic illustrations, because a learner meets "Center2" as a variable, not a person — so this is the *debater's* version, not the 101 version. I'd run it as the companion to 5, not instead of it.

## 3 — Fizzy or sweet? ⭐ *the page, not the slide*

**Seven drinks, seven people, two groupings that are exactly the same size.**

| | fizzy | still |
|---|---|---|
| **sugar** | Cola, Root Beer | Lemonade, Sweet Tea |
| **no sugar** | Diet Cola, Sparkling Water | Unsweet Tea |

Fizzy holds 4 of 7 first choices. Sugar holds 4 of 7. Both majorities, both spread across four candidates. From outside, the same situation.

**Choose-One elects Diet Cola on 2 of 7 (29%).** The sugar majority really split and really lost. The fizzy majority never split — it was never a bloc. A Diet Cola drinker doesn't want a Cola; they score it a 1.

```text
Scoring round:  Cola 17 · Lemonade 17 · Sweet Tea 16 · Diet Cola 15  <- the Choose-One
                Root Beer 14 · Unsweet Tea 13 · Sparkling Water 12      winner, 4th of 7
Runoff:         Cola 4 · Lemonade 3 · Equal Support 0
```

Files 3 and 3b are **byte-identical elections** differing only in which grouping `blocs:` names, so the engine prints opposite verdicts on the same seven ballots:

```text
3   'Sugar (a real clone set)'          4 (57.1%)   winner OUTSIDE  => VOTE SPLITTING
3b  'Fizzy (a label, not a clone set)'  4 (57.1%)   winner INSIDE   (no spoiler)
```

Same size, same spread, opposite verdict. **A clone set is made of voters, not categories** — which is why you cannot read a spoiler off a candidate list, and why "the fizzy vote will split" is the kind of confident claim that comes out backwards. Nothing in the library says this yet.

## 4 and 2 — pizza toppings, coffee menu

Both work and both are at the floor (7 candidates, 8 voters, 25%, rival last on score). Pizza's family is unarguable in the way fruit's is — meat is meat. Coffee's is the better joke: latte, cappuccino, flat white, cortado and macchiato are the same two ingredients in different ratios.

**Shared weakness:** both produce a **7–1 runoff**. Decisive, but after a 27–21 scoring round it reads as "why bother with the runoff?" — where 5's 6–3 and 6's 5–4 keep the second round looking like it did work.

---

## Recommendation

1. **Build 5 (fruit basket)** as the demo/slide case — smallest ballot count, most extreme number, and the only food cast whose family nobody can dispute.
2. **Build 6 (factions)** alongside it as the debater-facing companion — same lesson, political vocabulary, no argument about who is a clone.
3. **Build 3 (fizzy/sweet)** as the 201 page. It's the one that teaches something new.
4. **Drop 1, 2 and 4** — 5 strictly dominates 1, and 2 and 4 add a cast without adding a lesson.

Keeping [`02_icecream_chocolate_split`](../../method_comparisons/split_voting/_main/02_icecream_chocolate_split.yaml) as-is; these are the small-ballot versions, not a replacement.

**Then:** `07_Concepts/tips/TIPS_vote_splitting_demos.md`, in the shape of [TIPS_canonical_elections.md](../../07_Concepts/tips/TIPS_canonical_elections.md) — the rules, the N+1 floor, the recipe, a table of every splitting demo in the repo with its job, and how to diagnose a real race.
