# Free riding in Proportional STAR

*Withhold one star from a candidate who is going to win anyway, and Allocated Score hands you back your entire ballot.*

**Level: 301 · deep dive**

→ the method: [STAR-PR](../../01_Learn/STAR_PR/README.md) · the three tabulations: [Allocated Score](../../01_Learn/STAR_PR/allocated_score.md) · [SSS](../../01_Learn/STAR_PR/sequentially_spent_score.md) · [RRV](../../01_Learn/STAR_PR/reweighted_range_voting.md) · the other honest limit: [the Alabama paradox](../alabama_paradox/README.md) · what proportionality does and doesn't promise: [what "proportional" actually means](../../01_Learn/what_proportional_means.md)

---

## The short answer

**Yes — Allocated Score and SSS are vulnerable, and more cheaply than the literature's usual framing suggests.** In the election below, a bloc of voters flips the second seat by scoring a landslide winner **4 instead of 5**. She wins anyway, by 92 to 48. The strategists give up nothing they can measure and double their weight in the round that decides the seat they care about.

**RRV resists that same move**, and the reason is structural rather than lucky: it has no score groups to jump between.

Three qualifiers, all demonstrated further down: the strategy **achieves nothing** if you misjudge who is above you in the spend order, it **backfires outright** if you push it too far, and it **cancels itself** the moment the other side attempts it too. This is a real incentive with real teeth, not a reason to abandon the method — but it is not the "weak pull" that [the voter FAQ](../../01_Learn/star_pr_faq.md) describes for bullet voting, and it deserves its own name.

---

## What free riding is

The strategy is a byproduct of the mechanism that makes a method proportional in the first place. Any PR method has to stop a popular winner from also deciding every *later* seat, so it charges the ballots that elected them — spending, exhausting, or reweighting. Free riding is the move that dodges the charge: **withhold support from someone who is going to win without you, so that your ballot survives to fight the next round.**

The literature splits it in two:

- **Hylland free riding** — bury a candidate whose election is certain, so your ballot is not spent electing them. In ranked methods this means ranking a riskier candidate *above* the sure thing.
- **Woodall free riding** — rank a candidate you expect to be *eliminated*, so your vote is never sitting on someone who exceeds the quota.

Woodall's version needs elimination and vote transfer, so it has no clean analogue in a scored method — nothing gets eliminated in STAR-PR. **Hylland's version is the one that applies here**, and the general result is not encouraging: all Droop-proportional ordinal methods, and *all cardinal methods with proportional party-list cases that pass the Pareto criterion*, are vulnerable to it. STAR-PR sits squarely inside that class. So the question this page can usefully answer is not *whether* the incentive exists — theory already says it does — but **how cheap it is**, which theory does not say, and which a runnable library can measure.

*Sourcing note: the Hylland/Woodall taxonomy and that vulnerability claim come from [electowiki](https://electowiki.org/wiki/Free_riding), which is the clearest write-up of a niche topic but is advocacy-adjacent — it is a hub for cardinal-method advocates. Nothing on this page rests on it: the definitions are theirs, every number below is this library's own count, and the one electowiki claim that bears directly on STAR-PR turns out to need a correction (see [the RRV section](#the-same-ballots-under-rrv-where-the-strategy-fails)).*

---

## The election

A neighbourhood association is filling **two board seats**. Anika is the beloved incumbent — all 20 voters score her 5. The 12-voter majority wants Bruno for the second seat; the 8-voter minority wants Camila.

<!-- ballots:free_ride_honest_allocated -->
The ballots as marked — the filled bubble is the score given, and the score is the number in its column:

| Ballot as marked | Anika | Bruno | Camila |
|:--|:--:|:--:|:--:|
| <img src="cases/img/free_ride_honest_allocated_ballot_1.png" width="330" style="min-width:330px" alt="A 0–5 STAR ballot — 12 voters — 12-voter majority: Anika 5, Bruno for seat 2: Anika 5, Bruno 4, Camila 0."> | 5 | 4 | 0 |
| <img src="cases/img/free_ride_honest_allocated_ballot_2.png" width="330" style="min-width:330px" alt="A 0–5 STAR ballot — 8 voters — 8-voter minority, honest: Anika 5, Camila for seat 2: Anika 5, Bruno 0, Camila 5."> | 5 | 0 | 5 |
<!-- /ballots -->

The minority is 40% of the electorate and there are two seats, so on the face of it they have a claim to one of them. Whether they get it turns entirely on a number they are free to choose.

### The honest count

<!-- report:free_ride_honest_allocated -->
```text
--- Allocated Score Voting Method (2 winners) ---

[Allocated Score Voting]
 Tabulating 20 ballots to fill 2 seats.
Count × Anika,Bruno,Camila
   12 ×     5,    4,     0
    8 ×     5,    0,     5

[Allocated Score Voting: Round 1]
 The highest-scoring candidate wins a seat.
   Anika         -- 100 -- First place
   Bruno         --  48
   Camila        --  40
 Anika wins a seat.

[Allocated Score Voting: Round 1: Ballot allocation round]
 Allocating 10 ballots.

[Allocated Score Voting: Round 1: Ballot allocation round: Round 1]
 Allocating 20 ballots at score 5.
 This allocation overfills the quota.  Returning fractional surplus.
 Allocating only 50.00% of these ballots.
 Keeping these ballots, but multiplying their weights by 1/2.
 20 ballots reweighted from 1 to 1/2.

[Allocated Score Voting: Round 2]
 The highest-scoring candidate wins a seat.
   Bruno         -- 24 -- First place
   Camila        -- 20
 Bruno wins a seat.

[Allocated Score Voting: Winners — Allocated Score Voting Method (2 winners)]
 Anika
 Bruno
```
<!-- /report -->

Anika takes seat 1 with 100 points. Then the Hare quota of 10 ballots has to be charged — and **every one of the 20 ballots is in her 5-star group**, so the charge falls on all of them equally: each keeps half its weight. The 12-to-8 split survives into round 2 untouched, and Bruno wins the second seat 24 to 20. The minority is outvoted in exactly the proportion it was outnumbered.

### The free ride

Now the 8 minority voters score Anika **4** instead of 5. Nothing else changes. They still like her; they simply notice she does not need them.

<!-- ballots:free_ride_hylland_allocated -->
The ballots as marked — the filled bubble is the score given, and the score is the number in its column:

| Ballot as marked | Anika | Bruno | Camila |
|:--|:--:|:--:|:--:|
| <img src="cases/img/free_ride_hylland_allocated_ballot_1.png" width="330" style="min-width:330px" alt="A 0–5 STAR ballot — 12 voters — 12-voter majority: unchanged, still honest: Anika 5, Bruno 4, Camila 0."> | 5 | 4 | 0 |
| <img src="cases/img/free_ride_hylland_allocated_ballot_2.png" width="330" style="min-width:330px" alt="A 0–5 STAR ballot — 8 voters — 8-voter minority FREE RIDING: Anika 4, not 5: Anika 4, Bruno 0, Camila 5."> | 4 | 0 | 5 |
<!-- /ballots -->

<!-- report:free_ride_hylland_allocated -->
```text
--- Allocated Score Voting Method (2 winners) ---

[Allocated Score Voting]
 Tabulating 20 ballots to fill 2 seats.
Count × Anika,Bruno,Camila
   12 ×     5,    4,     0
    8 ×     4,    0,     5

[Allocated Score Voting: Round 1]
 The highest-scoring candidate wins a seat.
   Anika         -- 92 -- First place
   Bruno         -- 48
   Camila        -- 40
 Anika wins a seat.

[Allocated Score Voting: Round 1: Ballot allocation round]
 Allocating 10 ballots.

[Allocated Score Voting: Round 1: Ballot allocation round: Round 1]
 Allocating 12 ballots at score 5.
 This allocation overfills the quota.  Returning fractional surplus.
 Allocating only 83.33% of these ballots.
 Keeping these ballots, but multiplying their weights by 1/6.
 12 ballots reweighted from 1 to 1/6.

[Allocated Score Voting: Round 2]
 The highest-scoring candidate wins a seat.
   Camila        -- 40 -- First place
   Bruno         --  8
 Camila wins a seat.

[Allocated Score Voting: Winners — Allocated Score Voting Method (2 winners)]
 Anika
 Camila
```
<!-- /report -->

**Camila takes the second seat, 40 to 8.** One star.

---

## Why one star was enough — the cliff

Allocated Score does not charge supporters evenly. It sorts them by the score they gave and spends the quota **from the top down**, which in [the engine](../../../STARVote_LH_tabulation_engine/starvote/__init__.py) is two lines: ballots that scored the winner `0` are set aside as non-supporters and never charged at all, and the rest are sorted so the highest scores are spent first.

That first half is not an accident — it is a design principle with a name. **[Vote unitarity](../vote_unitarity/README.md)** holds that influence should be spent *only in exchange for representation gained*, so a voter who scored the winner 0 pays nothing. It is a genuinely good rule, and it is why the [backfire case](#2-push-harder-and-it-backfires) below can guarantee itself an exemption by burying a candidate. The uncomfortable part is that the same rule which protects an honest non-supporter also protects a strategic one, and the count cannot tell them apart — a ballot marked 0 looks identical either way.

That makes your exposure a **step function** of the score you gave:

| | 5-star group | 4-star group | round-2 weight of the minority |
|---|---|---|---|
| **Honest** (minority gives 5) | all 20 ballots — charged 50% | *empty* | **1/2** |
| **Free ride** (minority gives 4) | 12 majority ballots — charged 83.33% | 8 minority ballots — **never reached** | **1** |

The quota of 10 is overfilled by the 12 majority ballots on their own, so the count stops before it ever reaches the 4-star group. The free riders are not charged a reduced amount — they are charged **nothing**.

And the move is doubly effective, because it does not just help the strategists. It *concentrates the entire cost of electing Anika on the voters who were honest about her*: the majority's weight falls from 1/2 to 1/6. Bruno drops from 24 to 8 while Camila climbs from 20 to 40. Both halves of that swing come from a single star.

The price paid is the part worth sitting with: Anika falls from 100 points to 92, against a runner-up on 48. **There is no plausible world in which those 8 stars decided her seat**, and the strategists could see that before voting. That is what makes this cheap rather than merely possible.

---

## The same ballots under RRV — where the strategy fails

[Reweighted Range Voting](../../01_Learn/STAR_PR/reweighted_range_voting.md) counts the identical free-riding ballots and **does not break**:

<!-- report:free_ride_hylland_rrv -->
```text
--- Reweighted Range Voting Method (2 winners) ---

[Reweighted Range Voting]
 Tabulating 20 ballots to fill 2 seats.
Count × Anika,Bruno,Camila
   12 ×     5,    4,     0
    8 ×     4,    0,     5

[Reweighted Range Voting: Round 1: Score round]
 The highest-scoring candidate wins a seat.
   Anika         -- 92 -- First place
   Bruno         -- 48
   Camila        -- 40
 Anika wins a seat.

[Reweighted Range Voting: Round 1: Reweighing Ballots]
 Reweighted 20 ballots:
   12 ballots reweighted from 1 to 1/2.
   8 ballots reweighted from 1 to 5/9.

[Reweighted Range Voting: Round 2: Score round]
 The highest-scoring candidate wins a seat.
   Bruno         -- 24     -- First place
   Camila        -- 22+2/9
 Bruno wins a seat.

[Reweighted Range Voting: Winners — Reweighted Range Voting Method (2 winners)]
 Anika
 Bruno
```
<!-- /report -->

Bruno keeps the seat. RRV has no score groups and no spend order; a ballot's weight is a smooth function of what it gave, `1 / (1 + score ÷ max_score)`. Dropping Anika from 5 to 4 moves a free rider from 1/2 to **5/9** — about 11% more weight, not 100% more — and leaves the majority's weight alone at 1/2. Camila rises from 20 to 22.22 and still loses to 24.

The difference is the [Balinski–Young](../../01_Learn/STAR_PR/the_math_behind_proportional_star.md) trade showing up in a new place. RRV is a **divisor** method: continuous, with no cliff to jump. Allocated Score and SSS are **quota** methods: they spend discretely, and a discrete spend has an edge you can stand just past.

This also sharpens a claim worth correcting. electowiki says that in reweighted score systems "it is riskier to free ride than ranking because they do not transfer votes but reweight." That is a fair description of **RRV** and is confirmed above — but it does not generalise to the cardinal PR family, and in particular it is **wrong about Allocated Score**, the method Equal Vote actually recommends and the one BetterVoting runs as `STAR_PR`. Allocated Score reweights *and* has a cliff, and the cliff is what carries the strategy.

### All three methods, same two ballot sets

| | Allocated Score | SSS | RRV |
|---|---|---|---|
| **Honest** (Anika 5 from everyone) | [Anika + Bruno](cases/cases_pages/free_ride_honest_allocated.md) | [Anika + Bruno](cases/cases_pages/free_ride_honest_sss.md) | [Anika + Bruno](cases/cases_pages/free_ride_honest_rrv.md) |
| **Free ride** (minority gives Anika 4) | [Anika + **Camila**](cases/cases_pages/free_ride_hylland_allocated.md) | [Anika + **Camila**](cases/cases_pages/free_ride_hylland_sss.md) | [Anika + Bruno](cases/cases_pages/free_ride_hylland_rrv.md) |
| **Strategy pays?** | **yes** | **yes** | no |

SSS spends score from the top down just as Allocated Score does, so it inherits the same cliff. It is not a defence.

---

## Why it is not a free lunch

A page that stopped there would be advocacy. Three things limit the strategy, and all three are runnable.

### 1. It achieves nothing if you misjudge the queue

A second election, deliberately arranged so the strategists are wrong about their position. Amara is the *minority's* favourite (they score her 5) but the majority is only lukewarm — 3 stars — and wants Boris.

| | honest | minority scores Amara 4 | minority scores Amara 0 |
|---|---|---|---|
| **Winners** | [Amara + Boris](cases/cases_pages/misjudged_queue_honest.md) | [Amara + Boris](cases/cases_pages/misjudged_queue_hylland.md) | [**Boris + Cleo**](cases/cases_pages/misjudged_queue_bury.md) |

Dropping to 4 changes **nothing at all**. At 4 stars the minority is *still* the highest score group — the majority only gave Amara 3 — so they are spent first and in full, exactly as before. Free riding pays only if it puts somebody else above you in the spend order, and **a voter cannot know that without knowing how everyone else scored.** The strategy needs information a real electorate does not have.

### 2. Push harder and it backfires

Having gained nothing at 4, the same voters try 0 — which under Allocated Score is the one move that *guarantees* exemption, since ballots scoring the winner 0 are set aside entirely:

<!-- report:misjudged_queue_bury -->
```text
[Divergence from STAR]
  STAR     = Boris
  Approval = Amara   (differs from STAR)

--- Allocated Score Voting Method (2 winners) ---

[Allocated Score Voting]
 Tabulating 20 ballots to fill 2 seats.
Count × Amara,Boris,Cleo
   12 ×     3,    5,   0
    8 ×     0,    0,   4

[Allocated Score Voting: Round 1]
 The highest-scoring candidate wins a seat.
   Boris         -- 60 -- First place
   Amara         -- 36
   Cleo          -- 32
 Boris wins a seat.

[Allocated Score Voting: Round 1: Ballot allocation round]
 Allocating 10 ballots.

[Allocated Score Voting: Round 1: Ballot allocation round: Round 1]
 Allocating 12 ballots at score 5.
 This allocation overfills the quota.  Returning fractional surplus.
 Allocating only 83.33% of these ballots.
 Keeping these ballots, but multiplying their weights by 1/6.
 12 ballots reweighted from 1 to 1/6.

[Allocated Score Voting: Round 2]
 The highest-scoring candidate wins a seat.
   Cleo          -- 32 -- First place
   Amara         --  6
 Cleo wins a seat.

[Allocated Score Voting: Winners — Allocated Score Voting Method (2 winners)]
 Boris
 Cleo
```
<!-- /report -->

The exemption works perfectly and costs them the election. Without their 40 points Amara falls to 36 and **loses seat 1 to Boris**; the quota is then charged to *his* supporters, and Cleo takes seat 2 on the minority's untouched ballots. Their honest haul was Amara, whom they scored 5. Their strategic haul is Cleo, whom they scored 4. They are **strictly worse off**, and the board has lost the one candidate every voter liked.

### 3. It cancels itself

If both blocs free ride — all 20 voters scoring Anika 4 — everyone is back in a single score group, the quota is charged evenly again, and [Bruno wins exactly as he did under honest voting](cases/cases_pages/free_ride_arms_race_allocated.md). The gain is **positional, not absolute**. It exists only while the other side declines to take it, which is the main reason strategies of this shape stay rare in practice rather than becoming universal.

---

## So how worried should a voter be?

Honestly: **mildly, and less than a strategist would like.** The exploit needs a candidate whose victory is beyond doubt, a reliable read on how *other* factions will score that same candidate, and an opposing bloc that does not do the same thing. Miss on the second and you have wasted your vote; miss on the first and you have thrown away a candidate you liked.

But it should not be waved away either, and two things make it more serious than the arithmetic alone suggests:

- **It is legible.** "Don't give five stars to someone who's already winning" is a rule of thumb a campaign can print on a leaflet. It does not require anyone to understand quotas.
- **Its organised form has a track record.** Party-level free riding is [vote management](../../../07_Concepts/GLOSSARY.md), long practised under [STV](../../../06_Other/STV/README.md) in Malta and Ireland and under Japan's old SNTV. Free riding is what one voter does; vote management is what a disciplined party does with the same insight.

The fair summary is the one the [Alabama paradox](../alabama_paradox/README.md) page reaches about a different flaw: this is a **structural price of the quota guarantee**, not a bug anyone can patch out. A method that guarantees a quota-sized faction a seat must charge the ballots that took one, and any charge that can be dodged will be worth dodging.

---

## What this page does not settle

- **Whether the honest outcome was even the right one.** The free ride here produced Anika + Camila, which gives each faction a distinct voice, against an honest count that gave the 60% majority both seats. Because Anika is a *consensus* winner drawn from every ballot, who "deserves" seat 2 is genuinely contested — and it is uncomfortable that in this instance the strategy arguably improved representation. That does not make it acceptable: a method whose good outcomes depend on voters gaming it is not one you can recommend honestly. But the page should not pretend the honest result was obviously better.
- **Whether Droop actually helps.** Both [Allocated Score](../../01_Learn/STAR_PR/allocated_score.md) and [the STAR-PR overview](../../01_Learn/STAR_PR/README.md) state that swapping Hare for Droop "mitigates free-riding." **Nobody here has tested that**, and the engine has no Droop option to test it with — Allocated Score is Hare-only. A smaller quota means a smaller charge, which cuts both ways: fewer ballots are spent, but the top score group is also exhausted sooner. The claim is inherited from the STV literature and is currently taken on faith in this repo. Implementing a `quota:` option would make it checkable in an afternoon.
- **How often it arises in real electorates.** Everything here is constructed. The natural companion is the simulation treatment the Alabama paradox already has — sweep random electorates, ask in what fraction a faction could have flipped a seat by shading one candidate, and by how many stars. That is the measurement the literature is missing, and this library is unusually well placed to produce it.

---

## Run these yourself

```bash
.venv/bin/python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 03_STAR_PR/03_Criteria/free_riding/cases/free_ride_hylland_allocated.yaml
```

All ten cases are linked from the tables above — the two elections are [the beloved incumbent](cases/cases_pages/free_ride_honest_allocated.md) and [the misjudged queue](cases/cases_pages/misjudged_queue_honest.md), each counted under the variations that matter. Every case carries `expected_winners:` and is run by the harness on every commit, so the numbers on this page cannot silently drift.

---

## See also

- [Allocated Score](../../01_Learn/STAR_PR/allocated_score.md) — the method this bites hardest, and the one Equal Vote recommends
- [RRV](../../01_Learn/STAR_PR/reweighted_range_voting.md) — the divisor method that resists it, and pays elsewhere
- [The Alabama paradox in Proportional STAR](../alabama_paradox/README.md) — the other structural price of the quota guarantee
- [STAR-PR — a voter's FAQ](../../01_Learn/star_pr_faq.md) — the bullet-voting question, which is the *opposite* move to this one
- [Strategic voting](../../../07_Concepts/topics/strategic_voting.md) — the single-winner picture, where STAR's runoff makes most strategies backfire

Sources: [Free riding — electowiki](https://electowiki.org/wiki/Free_riding) (definitions and the vulnerability class; advocacy-adjacent, see the note above) · Markus Schulze, ["Free riding"](https://www.votingmatters.org.uk/ISSUE18/I18P2.PDF), *Voting Matters* 18 (the original STV treatment)

# file: README.md
