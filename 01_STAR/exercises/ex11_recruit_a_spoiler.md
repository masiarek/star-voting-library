# Exercise 11 — Recruit a spoiler

*You manage Brett's campaign, and the polling is grim: Alba leads the two-way race 5–4 and every voter is locked in. Then an intern slides a memo across the table: "We can't flip a single voter — so let's add a **candidate**. Recruit Axl, who's practically Alba with a different haircut. Alba's five voters will split, our four hold, we win." Your job: game out the memo under three counting rules before deciding whether the trick is worth it.*

**▶ Live on BetterVoting:** base race [vote](https://bettervoting.com/ggg7hd) · **[results ↗](https://bettervoting.com/ggg7hd/results)** · clone added [vote](https://bettervoting.com/93gjx6) · **[results ↗](https://bettervoting.com/93gjx6/results)** (elections `ggg7hd` / `93gjx6`, Test IDs BV2197–98; the clone election runs all four methods — watch Choose-One fall for it live while RCV-IRV, STAR, and Ranked Robin hold).

**You practice:** the **[spoiler effect](../../00_start_here/topics/spoiler_effect.md)** as a *design property* — predicting which ballot designs a vote-splitting attack actually works against — and reading an Equal-Support runoff line. (Concept home: [vote-splitting](../../method_comparisons/split_voting/README.md); glossary: [clone independence](../../00_start_here/GLOSSARY.md).)

Work each part on paper before opening its solution. Both YAMLs are runnable; their `expected_winners` keys are regression-tested, and the `_tabulated` mirrors are the full audit reports. (Axl shares Alba's initial *on purpose* — they're clones; the distinct-initials naming rule yields to the lesson.)

## The ballots

**Base race** — nine voters, two candidates: Alba's camp of five scores (Alba 5, Brett 0); Brett's camp of four scores (Alba 0, Brett 5).

**After the memo** — same nine voters, three names. Alba's camp splits its *first preferences* over the clones but scores both high; Brett's camp is unchanged:

| | ×3 Alba camp | ×2 Alba camp | ×4 Brett camp |
|---|:---:|:---:|:---:|
| **Alba** | 5 | 4 | 0 |
| **Axl** | 4 | 5 | 0 |
| **Brett** | 0 | 0 | 5 |

## Your task

- **(a)** Confirm the base race: who wins under Choose-One, Score, and STAR?
- **(b)** The memo assumes Choose-One counting. Does the trick work there? Show the count.
- **(c)** Now the town uses **STAR**. Predict, then tabulate: who reaches the runoff, what does the runoff line say, who wins? Where exactly does the memo's logic die?
- **(d)** Try it under **RCV-IRV**. Does the spoiler work there? (Careful — the answer may not flatter your favorite talking point.)
- **(e)** Write the one-paragraph reply you'd send back with the memo, as a matter of *ballot design* rather than ethics.

## Solutions

<details>
<summary><b>(a) The base race — Alba, everywhere</b></summary>

Choose-One: 5–4 Alba. Score: 25–20 Alba. STAR: finalists by necessity, runoff **Alba 5–4**. When there are only two names, every reasonable method is the same method: majority rule.

</details>

<details>
<summary><b>(b) Under Choose-One, the memo works</b></summary>

First choices after Axl enters: **Alba 3, Axl 2, Brett 4 — Brett wins** with the *same nine opinions* that preferred Alba's camp 5–4. No voter changed their mind; the ballot design simply cannot hear "either clone over Brett." That's the spoiler effect in its purest form — the attack Choose-One invites, and the reason this repo's [split-voting set](../../method_comparisons/split_voting/README.md) exists.

</details>

<details>
<summary><b>(c) Under STAR, the memo dies in the scoring round</b></summary>

```text
Scoring Round
 The two highest-scoring candidates advance to the next round.
   Alba          -- 23 -- First place
   Axl           -- 22 -- Second place
   Brett         -- 20
 Alba and Axl advance.

Automatic Runoff Round
 The candidate preferred in the most head-to-head matchups wins.
   Alba          -- 3 -- First place
   Axl           -- 2
   Equal Support -- 4
 Alba wins.
   Voters with a preference: 5 of 9 (4 Equal Support).
   Alba 3 (60%) vs Axl 2 (40%); majority = 3.
```

The camp's 4s and 5s pile onto *both* clones — Alba 23, Axl 22, **Brett 20 and third**. The runoff isn't even Alba-vs-Brett: **the camp keeps both finalist slots**, and the election finishes as an intramural Alba-vs-Axl vote, 3–2, with Brett's four voters standing aside as Equal Support (they scored the clones 0–0 — the line `5 of 9 (4 Equal Support)` is [exercise 7](ex07_vanishing_votes.md)'s lesson making a cameo). The memo's premise — "splitting first choices splits *power*" — is false on a ballot where support isn't exclusive.

</details>

<details>
<summary><b>(d) Under RCV-IRV, the memo also fails — credit where due</b></summary>

First choices: Alba 3, Axl 2, Brett 4. **Axl is eliminated first**, and both of his ballots transfer straight back to Alba (she's ranked next on them): final round **Alba 5, Brett 4**. Pure-clone *crowding* is the vote-splitting variant RCV-IRV genuinely handles — its transfers exist for exactly this case, and the honest scorecard says so (the glossary's [clone-independence entry](../../00_start_here/GLOSSARY.md) gives IRV this point). IRV's spoiler trouble is the *non-clone* case — a competitive third candidate who squeezes the middle ([exercise 5](ex05_center_squeeze.md)) — not this one.

</details>

<details>
<summary><b>(e) The reply memo</b></summary>

"The plan only works if the town counts Choose-One ballots — the one design where a voter's support for Axl is *subtracted* from Alba. Under STAR the clones pool rather than split (both finalist slots go to their camp and we finish third); under RCV-IRV the transfers just reassemble Alba's five. And if anyone audits *why* we recruited a candidate we hope loses, we've handed the story to the opposition. Recommend we spend the budget persuading an actual voter — under every ballot here, that's worth strictly more than a fake candidate." — The general lesson, minus the intrigue: *how much a spoiler can extract is a property of the ballot*, which is why [the Equal Vote criterion](../../00_start_here/STAR_Voting/properties_and_limits/equally_weighted_vote.md) centers on it.

</details>

## Reading this fairly

A *strategic* construction, flagged as such per the [four-part test](../../method_comparisons/paradoxes_and_whoops/reading_these_fairly.md) — and run symmetrically: the attack succeeds against Choose-One, and fails against **both** STAR and RCV-IRV, each for its own structural reason. Real clone politics is messier than two candidates with interchangeable haircuts (imperfect clones leak preferences — the fuller story is the [split-voting set](../../method_comparisons/split_voting/README.md) and the glossary's teaming-vs-crowding distinction).

## Run it yourself

```
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/exercises/cases/ex11_two_way_base.yaml
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/exercises/cases/ex11_spoiler_added.yaml
```

Sources: [ex11_two_way_base.yaml](cases/ex11_two_way_base.yaml) · [ex11_spoiler_added.yaml](cases/ex11_spoiler_added.yaml). Full audit reports: [base](cases/cases_tabulated/ex11_two_way_base_tabulated.txt) · [spoiler added](cases/cases_tabulated/ex11_spoiler_added_tabulated.txt).

---

**Where this comes from.** Original to this repo (ballots, cast, and the intern). Concept homes: [the spoiler effect](../../00_start_here/topics/spoiler_effect.md), [the split-voting set](../../method_comparisons/split_voting/README.md), and [the equally weighted vote](../../00_start_here/STAR_Voting/properties_and_limits/equally_weighted_vote.md).

*Back to [the exercises set](README.md) · curriculum home: [Voting 301](../../00_start_here/curriculum/CURRICULUM_301.md)*

# file: ex11_recruit_a_spoiler.md
