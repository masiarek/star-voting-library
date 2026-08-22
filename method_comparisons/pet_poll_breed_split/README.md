# Three dogs and a cat — the ballot that decides whether vote splitting shows up

**Level: 201 · deep dive**

*Sixty pet owners. Fifty-seven percent of them are dog people. Ask them "what's the best pet?" and Choose-One elects the **dog**. Ask the same sixty people the same question with **three dog breeds** on the paper instead of one, and Choose-One elects the **cat** — with 33% of the vote.*

*Nobody changed their mind. Nobody was added or removed. The only thing that changed is how many names the dog side had on the ballot.*

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/p2wggg) · **[results ↗](https://bettervoting.com/p2wggg/results)** (election `p2wggg`, Test ID **BV2286** — all seven races, every one agreeing with the LH engine). Sixty voters cast one ballot covering all seven races, so the export itself is the proof that the electorate never changed between the two. (BetterVoting's race titles call them **Ballot A** and **Ballot B**; on this page they are simply the **one-dog ballot** and the **three-dog ballot**.)

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

| | **The one-dog ballot** | **The three-dog ballot** |
|---|---|---|
| **Candidates** | Dog · Cat · Parrot | Labrador · Golden Retriever · German Shepherd · Cat · Parrot |
| **Choose-One first choices** | **Dog 34** · Cat 20 · Parrot 6 | Cat 20 · Labrador 14 · Golden Retriever 12 · German Shepherd 8 · Parrot 6 |
| **Choose-One winner** | **Dog** — 34 of 60, an outright **57% majority** | **Cat** — 20 of 60, **33%**, while 57% of the room are dog people |
| **STAR winner** | **Dog** | **Labrador** |
| **Anything to see?** | No. Every method agrees. | Yes. Four methods, **three different winners.** |

The one-dog ballot *is* the `meta_pets` problem, reproduced in miniature: one name per family, a dominant family, and every method returning the same answer. The three-dog ballot is the same election with the dog side's internal disagreement written onto the paper — which is the normal condition of almost every real primary.

## The three-dog ballot, counted five ways

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

### Run them yourself

| # | Race | Winner | Read · run |
|:-:|------|:------:|:--:|
| 1 | one dog — Choose-One | **Dog** (34/60, 57%) | [page](cases/cases_pages/bv2286_p2wggg_a1_one_dog_plurality.md) · [`.yaml`](cases/bv2286_p2wggg_a1_one_dog_plurality.yaml) |
| 2 | one dog — STAR | **Dog** | [page](cases/cases_pages/bv2286_p2wggg_a2_one_dog_star.md) · [`.yaml`](cases/bv2286_p2wggg_a2_one_dog_star.yaml) |
| 3 | three dogs — Choose-One | **Cat** (20/60, 33%) | [page](cases/cases_pages/bv2286_p2wggg_b1_three_dogs_plurality.md) · [`.yaml`](cases/bv2286_p2wggg_b1_three_dogs_plurality.yaml) |
| 4 | three dogs — RCV-IRV | **Golden Retriever** | [page](cases/cases_pages/bv2286_p2wggg_b2_three_dogs_irv.md) · [`.yaml`](cases/bv2286_p2wggg_b2_three_dogs_irv.yaml) |
| 5 | three dogs — Approval | **Golden Retriever** (34, 57%) | [page](cases/cases_pages/bv2286_p2wggg_b3_three_dogs_approval.md) · [`.yaml`](cases/bv2286_p2wggg_b3_three_dogs_approval.yaml) |
| 6 | three dogs — STAR | **Labrador** | [page](cases/cases_pages/bv2286_p2wggg_b4_three_dogs_star.md) · [`.yaml`](cases/bv2286_p2wggg_b4_three_dogs_star.yaml) |
| 7 | three dogs — Ranked Robin | **Labrador** (4–0–0) | [page](cases/cases_pages/bv2286_p2wggg_b5_three_dogs_ranked_robin.md) · [`.yaml`](cases/bv2286_p2wggg_b5_three_dogs_ranked_robin.yaml) |

Every winner is cross-checked: **LH engine = BetterVoting** on all seven races, and the Ranked Robin result is confirmed a third time by `pref_voting`'s independent Copeland implementation (`AGREE ✓`, unique Copeland winner).

### The scored ballots (three-dog ballot)

<!-- ballots:bv2286_p2wggg_b4_three_dogs_star -->
*(No ballot art for `bv2286_p2wggg_b4_three_dogs_star` — draw it with `build_style_ballot_images.py --from-yaml method_comparisons/pet_poll_breed_split/cases/bv2286_p2wggg_b4_three_dogs_star.yaml`.)*

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:Labrador,Golden Retriever,German Shepherd,Cat,Parrot
14:5,4,3,1,0   # Labrador camp — but any dog beats the cat
12:4,5,3,1,0   # Golden camp
8:3,4,5,0,1    # Shepherd camp
20:2,1,1,5,1   # cat people — the Labrador is the tolerable dog
6:1,2,2,3,5    # parrot people
```
<!-- /ballots -->

### The count that elects the cat

<!-- report:bv2286_p2wggg_b1_three_dogs_plurality -->
```text
--- Choose-One / Plurality Voting Method (single winner) ---
 Tabulating 60 ballots.

                   Labrador  Golden Retriever  German Shepherd   Cat   Parrot 
  14 ×                X             -                 -           -      -    
  12 ×                -             X                 -           -      -    
  8 ×                 -             -                 X           -      -    
  20 ×                -             -                 -           X      -    
  6 ×                 -             -                 -           -      X    

  Count the marks:  Cat 20 · Labrador 14 · Golden Retriever 12 · German Shepherd 8 · Parrot 6

Winner — Choose-One / Plurality Voting Method (single winner)
 Cat   (20 of 60 marks)
```
<!-- /report -->

### The same voters under STAR

The engine's `[Vote-splitting check]` states the verdict in numbers, because the case file declares the three dogs as a bloc:

<!-- report:bv2286_p2wggg_b4_three_dogs_star -->
```text
[Divergence from STAR]
  STAR                   = Labrador
  Choose-One (Plurality) = Cat   (differs from STAR)
  RCV-IRV                = Golden Retriever   (differs from STAR)
  Note: 26 of 60 ballots (43%) had equal non-zero scores, so their ranks
        were decided by candidate priority order. The RCV-IRV result may be
        an artifact of score-to-rank tie-breaking rather than a deep
        difference.
  Note: Ranked Robin (RCV-RR) agrees with STAR, so RCV-IRV is the lone
        outlier — the classic center-squeeze signature.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: cases_tabulated/bv2286_p2wggg_b4_three_dogs_star_RCV-IRV_tabulated.txt

[Vote-splitting check]
  Choose-One first choices: Cat 20, Labrador 14, Golden Retriever 12, German Shepherd 8, Parrot 6
  Plurality winner: Cat (20, 33.3%)
  Bloc 'Dogs' = Labrador, Golden Retriever, German Shepherd: combined 34 (56.7%); winner Cat is OUTSIDE it.
  => VOTE SPLITTING: the 'Dogs' bloc is an outright majority (34 vs Cat's
     20) but split across 3 candidates, so Cat won Choose-One. STAR elected
     Labrador.

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 60 ballots.
Count × Labrador,Golden Retriever,German Shepherd,Cat,Parrot
   20 ×        2,               1,              1,  5,     1
   14 ×        5,               4,              3,  1,     0
   12 ×        4,               5,              3,  1,     0
    8 ×        3,               4,              5,  0,     1
    6 ×        1,               2,              2,  3,     5

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Labrador         -- 188 -- First place
   Golden Retriever -- 180 -- Second place
   German Shepherd  -- 150
   Cat              -- 144
   Parrot           --  58
 Labrador and Golden Retriever advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Labrador         -- 34 -- First place
   Golden Retriever -- 26
   Equal Support    --  0
 Labrador wins.
   Runoff math:
     60  ballots cast
   −  0  Equal Support (no preference between the two finalists)
     ──
     60  voters with a preference  (majority = 31)
           Labrador 34 (57%)  ·  Golden Retriever 26 (43%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Labrador
```
<!-- /report -->

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

**Score-winner ≠ runoff-winner is a feature, not a wart.** A demo where the scoring round and the automatic runoff disagree is showing the audience precisely why the runoff exists: the scoring round finds the most broadly liked option, and the runoff checks it against which one more voters actually *prefer*. On the three-dog ballot they agree (Labrador leads both). On `meta_pets` they don't — and that is worth two sentences, not an apology. See [the STAR scoring round](../../01_STAR/01_Learn/the_count/STAR_Scoring_Round.md) and [what makes a good winner](../../07_Concepts/topics/what_makes_a_good_winner.md).

**This is a constructed electorate.** The sixty ballots below are designed to be plausible, not sampled. They are here to prove the mechanism, not to measure how much America likes Labradors.
