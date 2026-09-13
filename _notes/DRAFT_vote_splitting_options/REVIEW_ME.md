# DRAFT — vote-splitting scenarios: what landed, what is still open

*Status as of 2026-09-13.* Five of the six options in this draft (written 2026-08-21) were promoted the **same day**, in `d9e8e70` and `8368790`, into [`method_comparisons/split_voting/`](../../method_comparisons/split_voting/README.md). Their yamls were deleted from here because the ballots were byte-identical to the committed cases. The one open item is **option 6**, below.

| Option | Where it went |
|---|---|
| **5 — the fruit basket** ⭐ | The **ladder** [`07a`–`07g`](../../method_comparisons/split_voting/README.md#when-does-it-actually-bite): 2 → 6 → 8 names under Choose-One, then STAR / Approval / RCV-IRV / Ranked Robin on the full menu. Live as **BV2293** `vq78wk`. The STAR case is [`07d_apples_full_menu_star.yaml`](../../method_comparisons/split_voting/_main/07d_apples_full_menu_star.yaml). |
| **3 / 3b — fizzy or sweet** ⭐ | [`09a`](../../method_comparisons/split_voting/_main/09a_clones_are_voters_not_labels.yaml) / [`09b`](../../method_comparisons/split_voting/_main/09b_same_ballots_grouped_by_label.yaml): byte-identical elections, opposite `blocs:` verdicts. Live as **BV2295** `8xrpyp`. |
| 1 — ice cream counter | Dropped: 5 strictly dominates it (this draft's own recommendation). The 101 set-piece is instead the seven-ballot `08a`–`08c` (**BV2296** `9cff2d`). |
| 2 — coffee menu · 4 — pizza toppings | Dropped: a cast without a new lesson. |
| **6 — Left1 / Center1 / Right1** ⭐ | **Not built.** The debater-facing companion to 5 — see below. |

The `TIPS_vote_splitting_demos.md` page this draft proposed has not been written either; check [`teaching_vote_splitting.md`](../../method_comparisons/split_voting/teaching_vote_splitting.md) first, since the presenter's plan may already cover the recipe.

```bash
.venv/bin/python STARVote_LH_tabulation_engine/starvote_larry_hastings.py "_notes/DRAFT_vote_splitting_options/6_factions.yaml"
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

