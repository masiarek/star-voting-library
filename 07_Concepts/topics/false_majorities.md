# False majorities — when a legislature's majority isn't one

**Level: 201 · for debaters**

**One line:** a party can hold over half the seats on well under half the votes, this happens routinely in every winner-take-all system, independent redistricting does not fix it — and neither does changing the single-winner method, which is the part reformers on this side of the argument most need to say out loud.

Part of [Concepts by topic](README.md). This page is the **legislature-level** majority problem. For the single-seat version — a winner elected on 34% of the vote — see [minority winner](../../method_comparisons/minority_winner/README.md) and [five senses of "majority candidate"](majority_criterion/majority_and_minority_candidates.md). Prompted by [CES's "Majority Illusion," claim-checked](majority_criterion/the_majority_illusion_claim_checked.md).

---

## The definition

A **false majority** — also *manufactured majority* — is when a party wins **more than half the seats** in a legislature while winning **fewer than half the votes**. Nobody cheated; no district was miscounted. Every seat was won fair and square by whoever led that district. The distortion is produced by the *aggregation*, not by any individual contest.

The mirror case has a name too: a **natural majority** is a seat majority backed by an actual vote majority, and it is the rarer animal in multiparty winner-take-all systems.

## Four that check out

| Election | Winning party | Vote share | Seats | Seat share |
|---|---|--:|--:|--:|
| **Canada 2011** | Conservative | 39.6% | 166 / 308 | **53.9%** |
| **Canada 2015** | Liberal | 39.5% | 184 / 338 | **54.4%** |
| **UK 2005** | Labour | 35.2% | 355 / 646 | **55.0%** |
| **UK 2024** | Labour | **33.7%** | 411 / 650 | **63.2%** |

UK 2024 is the extreme modern case and the clearest one to quote: **a third of the vote, nearly two-thirds of the seats** — and only 1.6 points more vote share than the same party won in 2019, for 32 more points of seats. That last comparison is the one that shows the mechanism, because the *voters* barely moved.

## Why it happens

Each district asks its own separate question and reports a single bit: who came first here. Everything else that was said on those ballots — the size of the margin, the second-place party's support, the votes for everyone else — is discarded before the results are added up. A party whose support is *efficiently distributed* (narrow wins in many districts) converts votes to seats far better than one whose support is concentrated (huge wins in few districts) or evenly thin (near-misses everywhere).

So the national seat count isn't a tally of national opinion. It's a count of how many separate small samples a party happened to lead — a **sloppy sample of the electorate**, and one whose bias has nothing to do with anyone's intentions.

## Redistricting reform does not fix it

This is the finding worth carrying into an argument, because the intuitive response — *"that's gerrymandering, draw fairer maps"* — is wrong, and Canada is the clean experiment.

Canada has drawn its federal boundaries through **independent, judge-chaired commissions since 1964**, under the [Electoral Boundaries Readjustment Act](https://en.wikipedia.org/wiki/Electoral_Boundaries_Readjustment_Act) — one commission per province, chaired by a judge appointed by the provincial chief justice, explicitly designed to be insulated from political interference. Gerrymandering is essentially ruled out. Canada manufactured majorities in 2011 and again in 2015 anyway.

Gerrymandering **makes this worse** — deliberately, and that's its purpose. But the effect exists without it. Independent commissions treat a symptom.

## How often? — the honest answer

You will see two figures quoted, both traced to Douglas Amy's *Real Choices/New Voices*: that winner-take-all systems produce a false majority **close to half the time**, and that proportional systems do so **less than 10%** of the time.

**Treat both as unverified.** They circulate widely (the CES article is one vector), the direction is not in doubt, but the numbers themselves are quoted secondhand and I could not locate them in an accessible source — and the CES piece itself gives "more than 40%" in one place and "close to half" in another for what should be the same statistic. If you need a citable frequency, the primary academic reference is:

> Blais, A. & Massicotte, L. (1986). "The impact of electoral formulae on the creation of majority governments." *Electoral Studies* **5**(3): 209–218.

Quote the four verified elections above instead. They are stronger than a contested percentage, and nobody can wave them away.

## The part this library has to say out loud

**Changing the single-winner method does not fix false majorities.** Run STAR, or Ranked Robin, or Approval, in every district in the country, and you will elect a better representative in each one — and still hand a party 63% of the seats on 34% of the vote, because the distortion lives in *electing one person per district and adding up the winners*, not in how each district picks its one person.

That is not a small caveat, and it's not one to bury. The single-winner methods this repo teaches solve the [spoiler effect](spoiler_effect.md), [center squeeze](center_squeeze/README.md), [vote splitting](../../method_comparisons/split_voting/README.md), and [minority winners](../../method_comparisons/minority_winner/README.md) — all real problems, all inside a district. Proportionality is a *different* problem with a different fix: elect multiple seats together, proportionally. That's [STAR-PR](../../03_STAR_PR/01_Learn/README.md), [STV](../../03_STAR_PR/01_Learn/stv/proportional_stv_vs_star.md), and the party-list systems most democracies use.

Anyone claiming a better single-winner ballot will make legislatures representative is overselling. Anyone claiming proportional representation will fix a *single* office — a governor, a mayor, a president — is overselling in the other direction. They are two levers on two different machines, and the honest reform case names both.

## Related

- [Two-party dominance](two_party_dominance.md) — Duverger, and the other thing single-member districts do
- [Wasted votes](wasted_votes.md) — the per-ballot view of the same arithmetic
- [Electing more than one](electing_more_than_one.md) — bloc vs. proportional, and why the distinction decides everything here
- [STAR-PR](../../03_STAR_PR/01_Learn/README.md) · [proportional STV vs STAR](../../03_STAR_PR/01_Learn/stv/proportional_stv_vs_star.md)
- [Douglas Amy, *Behind the Ballot Box*](../books/electoral_systems_and_pr.md) — the citizen-level case for PR, with its lean disclosed
- ["The Majority Illusion," claim-checked](majority_criterion/the_majority_illusion_claim_checked.md) — where this page came from
