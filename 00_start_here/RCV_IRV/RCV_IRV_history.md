# RCV-IRV — origins and spread

*Where instant-runoff voting came from, and why it looks the way it does. Short
version: **counting the whole ballot came first; IRV was the hand-countable
workaround.***

→ Method page: [RCV-IRV (Hare)](RCV-IRV-Hare.md) · the naming tangle:
[RCV vs. IRV vs. RCV-IRV](RCV-IRV-confusing-name.md)

---

## Whole-ballot counting came first

There are **several ways to tally a ranked ballot**, and the *first* idea was the
thorough one: read the entire ranking and elect the candidate **preferred over every
other head-to-head** — what we now call the **Condorcet winner**. The Marquis de
Condorcet formalized this in **1785** (Jean-Charles de Borda had proposed his own
rank-points method a few years earlier; the idea traces back to Ramon Llull centuries
before that).

These methods use *all* the rankings, so they tend to elect a broadly-preferred
candidate — but tallying every pairwise matchup **by hand** is laborious. That
tallying cost is exactly the problem the next idea set out to solve. (The modern,
practical version of "count the whole ballot" is [Ranked Robin](../RCV_Ranked_Robin/ranked_robin.md).)

## IRV: a hand-countable workaround (~150 years ago)

**Instant-runoff voting** — eliminate the candidate with the fewest first choices,
transfer those ballots, repeat — was designed as a procedure you *could* run by hand.
The single-winner rule is usually credited to **William Robert Ware** at MIT around
**1871**; **Thomas Hare** (1857) had already designed the multi-winner transferable
vote (STV) it descends from. So the elimination *shape* is roughly **150 years old**.

The trade it makes: rounds of simple first-choice counts are easy to hand-tally, but
eliminating on first choices alone can cut a broadly-liked middle candidate who would
beat every rival one-on-one — so IRV is **not Condorcet-efficient**. That's the
[center squeeze](RCV_IRV_center_squeeze.md). In other words, IRV bought
hand-countability at the cost of some representativeness that whole-ballot counting had.

## A century of use in Australia

Australia adopted the **Alternative Vote** — its name for single-winner IRV — for
House of Representatives elections in **1918**, and has used it ever since: **over 100
years** of real-world experience (the Senate uses STV, the multi-winner cousin).

## US momentum — the last ~20 years

- **Local:** San Francisco (2004), Minneapolis, and New York City (2021 primaries),
  plus dozens of other cities.
- **Statewide:** Maine (the first state, 2018) and Alaska (2022, paired with a
  top-four primary).

Adoption has continued to expand city by city; check
[FairVote's "where it's used"](https://fairvote.org/our-reforms/ranked-choice-voting-information/)
for the current list.

## Synonyms

"Instant Runoff Voting," "Alternative Vote" (UK / Australia), and "Preferential
Voting" (Australia) all name the same single-winner method that US usage calls "RCV."
Why those names mislead — and why "preferential" is itself a misnomer — is in
[the naming problem](RCV-IRV-confusing-name.md).

Sources: [Instant-runoff voting — Wikipedia](https://en.wikipedia.org/wiki/Instant-runoff_voting),
[Condorcet method — Wikipedia](https://en.wikipedia.org/wiki/Condorcet_method),
[Where RCV is used — FairVote](https://fairvote.org/our-reforms/ranked-choice-voting-information/)

# file: RCV_IRV_history.md
