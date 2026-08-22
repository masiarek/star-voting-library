# Three dogs and a cat — the ballot that decides whether vote splitting shows up

**Level: 201 · deep dive**

*Sixty pet owners. Fifty-seven percent of them are dog people. Ask them "what's the best pet?" and Choose-One elects the **dog**. Ask the same sixty people the same question with **three dog breeds** on the paper instead of one, and Choose-One elects the **cat** — with 33% of the vote.*

*Nobody changed their mind. Nobody was added or removed. The only thing that changed is how many names the dog side had on the ballot.*

→ The concept: [the spoiler effect](../../07_Concepts/topics/spoiler_effect.md) · the runnable set: [vote-splitting & spoilers](../split_voting/README.md) · how often it happens for real: [the 2022 count, read honestly](../split_voting/how_often_does_vote_splitting_happen.md) · the other pet polls: [four methods](../pet_poll_four_methods/README.md) · [four winners](../pet_poll_four_winners/README.md)

---

## Why this page exists

The Equal Vote Coalition's flagship demo poll is **[meta_pets](https://bettervoting.com/meta_pets)** — *"What Makes the Best Pet?"*, the same electorate counted four ways (Choose One, RCV, Approval, STAR). It is a genuinely good demo: approachable, friendly, politics-free. But it has a known disappointment — **most of the methods elect Dog**, so the poll never shows the thing STAR is mainly sold on: that it ends vote splitting.

The usual diagnosis is that the *topic* is wrong — that pets are "really a two-man game between cats and dogs," so a different subject (sodas, snacks, activities) would show more. That diagnosis is half right and half a trap. Here is the whole ballot:

> Bird · Cat · Python · Dog · Fish · Rabbit · Rat

**Seven candidates. Zero clones.** There is exactly one dog on that ballot, exactly one cat, exactly one bird. Vote splitting is what happens when *two or more similar candidates draw from the same pool of voters* and a one-mark ballot forces those voters to pick just one of them. A ballot with one name per family has nothing to split — and **no set of votes can create a split that the candidate list doesn't contain.** You could run a million ballots through `meta_pets` and never see one.

So the fix isn't a new topic. The fix is **clones on the ballot** — and pets can supply them as easily as anything else.

## The same sixty voters, two ballots

Sixty pet owners, fixed opinions. Thirty-four are dog people (a 57% majority), twenty are cat people, six want a parrot. Among the dog people, tastes differ by breed: fourteen lead with a Labrador, twelve with a Golden Retriever, eight with a German Shepherd — but *all thirty-four prefer any dog to any cat.*

| | Ballot A — *one dog on the paper* | Ballot B — *three dogs on the paper* |
|---|---|---|
| **Candidates** | Dog · Cat · Parrot | Labrador · Golden Retriever · German Shepherd · Cat · Parrot |
| **Choose-One first choices** | **Dog 34** · Cat 20 · Parrot 6 | Cat 20 · Labrador 14 · Golden Retriever 12 · German Shepherd 8 · Parrot 6 |
| **Choose-One winner** | **Dog** — 34 of 60, an outright **57% majority** | **Cat** — 20 of 60, **33%**, while 57% of the room are dog people |
| **STAR winner** | **Dog** | **Labrador** |
| **Anything to see?** | No. Every method agrees. | Yes. Four methods, **three different winners.** |

Ballot A *is* the `meta_pets` problem, reproduced in miniature: one name per family, a dominant family, and every method returning the same answer. Ballot B is the same election with the dog side's internal disagreement written onto the paper — which is the normal condition of almost every real primary.

## Ballot B, counted five ways

Rows are candidates, columns are counting rules — one electorate, read five ways ([the same-opinion line-up](../../07_Concepts/tips/TIPS_canonical_elections.md)):

| | [Choose-One](../../07_Concepts/topics/plurality.md) | [RCV-IRV](../../06_Other/RCV_IRV/concepts/README.md) | [Approval](../../04_Approval/01_Learn/README.md) | [STAR](../../01_STAR/01_Learn/README.md) | [Ranked Robin](../../05_Ranked_Robin/01_Learn/ranked_robin.md) |
|---|:--:|:--:|:--:|:--:|:--:|
| **Labrador** (dog) | — | — | — | **WINS** | **WINS** |
| **Golden Retriever** (dog) | — | **WINS** | **WINS** | — | — |
| **German Shepherd** (dog) | — | — | — | — | — |
| **Cat** | **WINS** | — | — | — | — |
| **Parrot** | — | — | — | — | — |
| *dog side : cat side (57 : 33)* | **loses** | holds | holds | holds | holds |

**Choose-One is the only rule that hands the win to the cat**, and it does it for the textbook reason: 34 dog voters were allowed one mark each and had three names to spread it over, so their largest pile (14) came in under the cat's undivided 20.

**Labrador is the [Condorcet winner](../../07_Concepts/topics/condorcet/README.md)** — it beats every other candidate head-to-head, including the cat 34–26 — and STAR and Ranked Robin both find it. RCV-IRV lands on the Golden Retriever: the Labrador is eliminated in the third round with 14 first choices, one round before it would have won. Approval also elects the Golden Retriever, the dog with the broadest reach across the three breed camps.

## The recipe, if you want to build one of these

A demo poll shows vote splitting when — and only when — its **candidate list** has this shape. The topic is nearly irrelevant; the arithmetic is not:

1. **One family that is a majority of the room** — 55–65% is the comfortable range.
2. **Two or three near-substitutes from that family on the ballot**, none of them dominant on its own.
3. **One consolidated rival from the minority family**, larger than any single member of the majority family.

That's it. Given (1)–(3), Choose-One elects the rival and every ballot that lets a voter support more than one name elects a member of the majority family. It works with pets, and it works with anything else:

| Topic | The majority family, split | The consolidated rival |
|---|---|---|
| **Pets** | Labrador · Golden Retriever · German Shepherd | Cat |
| **Coffee order** | Latte · Cappuccino · Flat White | Drip coffee |
| **Pizza** | Pepperoni · Sausage · Meat Lovers | Margherita |
| **Ice cream** | Dark Chocolate · Chocolate Chip · Chocolate Fudge | Vanilla |

The ice-cream row is not hypothetical — it is live on BetterVoting as **[BV2186 ↗](https://bettervoting.com/2wfth7)**, an eight-flavor STAR poll built around exactly that three-chocolate cluster. What it is missing is a **parallel Choose-One race**, which is where the whole punch lives: the split only becomes visible when the audience sees the two counts side by side.

## The honest caveats

**A designed ballot is not a rigged one, but say so out loud.** Putting three dogs and one cat on a ballot looks lopsided, and an audience will notice. That reaction is the lesson, not an objection to it: under Choose-One the lopsidedness is real, and it cuts *against* the side with more choices. Naming that before someone else does turns the awkward moment into the point — **choose-one voting punishes the side that offers voters more options**, which is why real parties spend so much effort clearing their own primary fields.

**A live poll can't be made to split by voting in it.** If a demo's candidate list has no clones, no pattern of incoming ballots will produce vote splitting — the most you can manufacture is a *method divergence* (a score winner who loses the runoff), which is a different lesson and a weaker one. Splitting has to be designed into the candidate list before the first vote is cast.

**Score-winner ≠ runoff-winner is a feature, not a wart.** A demo where the scoring round and the automatic runoff disagree is showing the audience precisely why the runoff exists: the scoring round finds the most broadly liked option, and the runoff checks it against which one more voters actually *prefer*. On Ballot B they agree (Labrador leads both). On `meta_pets` they don't — and that is worth two sentences, not an apology. See [the STAR scoring round](../../01_STAR/01_Learn/the_count/STAR_Scoring_Round.md) and [what makes a good winner](../../07_Concepts/topics/what_makes_a_good_winner.md).

**This is a constructed electorate.** The sixty ballots below are designed to be plausible, not sampled. They are here to prove the mechanism, not to measure how much America likes Labradors.
