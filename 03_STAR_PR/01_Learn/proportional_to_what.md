# Proportional to *what*? — representation without parties

**One line:** party-list PR divides seats among **parties**, so the groups are declared before anyone votes; STAR-PR divides seats among **quotas of voters**, so the constituencies are *emergent* — discovered by the ballots, with nobody registering, naming, or even knowing they are in one.

→ the method: [STAR-PR](STAR_PR/README.md) · seen side by side with the majoritarian count: [Bloc STAR vs Proportional STAR](../../method_comparisons/bloc_vs_pr/README.md) · the harder version of this question: [what "proportional" actually means](what_proportional_means.md)

**Level: 101 · for voters**

---

## The confusion, stated plainly

Proportional representation is almost always explained with parties: *a party with a quarter of the votes gets a quarter of the seats.* That is easy to picture, and most of the world's PR systems work that way.

Then someone says "Proportional STAR", hands you a ballot with nine individual names and no parties on it at all, and the picture stops working. **Proportional to what?** There are no parties to be proportional *to*.

This page is that one question.

## The answer: the unit is a quota of voters

Forget parties. The thing being divided proportionally is not "party vote share" — it is **the voters themselves**.

Three seats, thirty voters. Then one seat is worth ten voters: the [quota](STAR_PR/README.md). Proportional STAR fills the council by repeatedly asking:

> Who is the favourite of some ten voters who don't have a representative yet?

Elect that candidate, mark those ten voters **represented**, and ask again with the voters who are left. Three seats, three groups of ten, everybody's ten got someone.

That is the whole idea, and notice what it never needed: no parties, no slates, no registration, no declared factions. Just *a seat is worth this many voters*.

## The groups are discovered, not declared

This is the part that feels strange coming from party-list PR, so it is worth saying directly.

In a party-list system, the groups exist **before** the election. Parties register, publish lists, and voters pick one. The count divides seats among groups that were named in advance.

In STAR-PR the groups exist **only in the ballots**. A "faction" here is nothing more than *a set of voters who happened to score the same candidate highly*. It has no name, no membership card, no headquarters. It may be:

- an ideological camp, if that is what divides the electorate;
- a neighbourhood, if geography is what people actually vote on;
- everyone who cares about one specific issue;
- something nobody predicted and only shows up in the numbers.

**The ballots reveal which of these was real.** That is why the method works without knowing in advance what the electorate is divided over — and why the same method serves a city council, a co-op board, and a club committee, none of which have parties.

## The worked version

Look at the [Left / Centre / Right example](../../method_comparisons/bloc_vs_pr/README.md#the-same-thing-at-readable-scale-left-centre-right) with this in mind. It is *drawn* as three camps because that makes it readable — but the count never sees a camp.

Ten voters, three seats, so a quota is 3.33 voters. Proportional STAR elects **C1, L1, L2**, and each of those results is about voters, not parties:

- **L1 and L2** win because the six left-leaning voters are worth about two quotas. Two seats. The count did not know they were "the left" — it saw six ballots that scored the same three names highly.
- **C1** wins on **breadth**, not on a bloc. The two centre voters are below quota on their own and could not elect anybody. But left and right voters *also* gave the centre candidates 1s and 2s, and those partial scores accumulate. C1 is nobody's favourite and many people's acceptable choice.
- **The right camp wins nothing**, and that is the system working. Two voters is below the 3.33 quota. They have not earned a seat and no proportional method owes them one.

C1 is the case that makes the point. There is no "centre party" doing anything. C1 is elected by a group of voters who never coordinated, never registered, and are spread across all three camps — a group that exists *only* as a pattern in the scores.

## What "represented" actually means — and a correction worth making

The natural way to describe the mechanism is: *"if you scored the winner highly, your ballot is reduced; if you scored them 0, it keeps full weight."*

**That describes [Reweighted Range Voting](STAR_PR/README.md), not Proportional STAR.** The distinction is the single most confusable thing on this page, and it is the difference between the two schools:

| | How it decides who is "represented" | Your ballot after your favourite wins |
|---|---|---|
| **Allocated Score** (the recommended STAR-PR) | A **quota's worth of ballots** is spent outright — 5-star supporters first, then 4-star, and so on until the quota is full | **Either fully spent or fully untouched.** If the quota filled before reaching your score group, you keep 100% weight even though you scored the winner 5 |
| **Reweighted Range Voting** | *Every* ballot is shaded in proportion to the support it gave | Reduced — a bit, or a lot, depending how highly you scored them |

So under STAR-PR proper, being "represented" is not a matter of degree that everyone shares a little of. It is closer to a seat at a table: **a quota of voters is seated with each winner**, and everyone else walks away with a full vote still in hand. The only voters who lose a *fraction* are those in the score group that straddles the quota boundary — [fractional surplus handling](STAR_PR/README.md) splits the remaining need evenly among them, precisely so that voters who scored the winner identically are treated identically.

That also answers the sharpest version of the question: **if you gave the winner 3 stars and they won, were you represented?** Only if the quota was still unfilled when allocation reached the 3-star group. Score groups are consumed from the top down; a big enough winner never reaches you, and your ballot goes into the next round intact.

### The questions worth asking next

These are the right ones, and the honest answers are mixed:

- **How steep is the reweighting?** Steepness is the entire design dial. Too steep and a cohesive majority loses seats it genuinely earned; too shallow and it sweeps. Allocated Score answers with a quota rather than a curve, which is *why* it passes the [Hare Quota Criterion](what_proportional_means.md) — a quota-sized group can always force a seat.
- **Does it punish honesty?** The real question, and not fully settled. If scoring a backup highly can get your ballot spent on them, there is a theoretical pull toward bullet voting to preserve weight. It is weaker under Allocated Score than under continuous reweighting — being spent requires the quota to actually reach your score group — but "weaker" is not "absent", and the honest position is that this deserves testing rather than assertion. It is one of the open items on the [committee's own list](what_proportional_means.md).
- **What happens to surplus?** Nothing is wasted: the group on the quota boundary gets the excess returned and shared evenly, keeping partial influence in later rounds.
- **Can a human audit it?** This is the weakest point and the repo says so elsewhere: STAR-PR is **not batch-summable**. Precincts cannot be tallied separately and added, because reweighting depends on individual ballots. Central tabulation is required — which is [an honest cost](STAR_PR/README.md) of proportionality, not of STAR.

## Why a 0–5 ballot matters here

A choose-one ballot can only tell you which single candidate each voter picked. That records group membership and nothing else — which is why choose-one systems drift toward needing parties to be meaningful.

A 0–5 ballot records **how much** each voter likes each candidate, so it can see:

- partial support (the 2s that got C1 elected),
- overlapping membership — a voter can be part of the group backing L1 *and* part of the group that finds C1 acceptable,
- degree of representation, not just its presence.

Real electorates look like that. People are not cleanly sorted, and a ballot that only records sorting cannot represent people who aren't sorted.

## What you give up

Being honest about the trade, because this is the cost of dropping parties:

With party lists you can *promise* a specific proportionality — this party got 25% of the vote and will get 25% of the seats, checkable afterwards by anyone. **Non-partisan PR cannot make that promise about any named group.** It guarantees representation to cohesive groups of voters large enough to reach a quota, but it cannot promise that any particular characteristic — party, geography, demographic — ends up proportional, because it never measured that characteristic in the first place.

That is not a defect being hidden; it is the direct consequence of letting the ballots decide what the electorate is divided over. The longer version, including what the research does and doesn't support, is [what "proportional" actually means](what_proportional_means.md).

## See also

- [Bloc STAR vs Proportional STAR](../../method_comparisons/bloc_vs_pr/README.md) — the same ballots counted both ways, starting from a two-ballot example
- [STAR-PR — the three methods](STAR_PR/README.md) — quotas and reweighting, and how the three tabulations differ
- [What "proportional" actually means](what_proportional_means.md) — the 201/301 version: quota vs threshold, and what proportionality does not promise
- [The majority sweep](../../02_STAR_Bloc/01_Learn/majority_sweep.md) — what happens instead when you *don't* use a proportional count
- [Electing more than one, simply](../../07_Concepts/topics/electing_more_than_one.md) — the plain-language fork between majoritarian and proportional
