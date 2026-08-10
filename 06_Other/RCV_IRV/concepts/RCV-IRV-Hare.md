# RCV-IRV (Hare) — the method US "RCV" actually means

*The single-winner instant-runoff method on the Hare elimination rule: drop the candidate with the **fewest first choices**, transfer, repeat. When an American ballot or statute says "Ranked Choice Voting," **this** is almost always it.*

→ Family overview: [Which RCV-IRV?](variants/RCV_IRV_variants.md) · why the name confuses: [RCV vs. IRV vs. RCV-IRV](RCV-IRV-confusing-name.md) · where it came from: [origins & spread](case_studies/RCV_IRV_history.md)

---

## In one line

Count everyone's first choices. If someone has **more than half**, they win. Otherwise **eliminate the candidate with the fewest first choices**, hand each of those ballots to its next still-standing choice, and repeat until a candidate holds a majority of the **active** (non-exhausted) ballots — or only two remain.

The rule is named for **Thomas Hare** (1857). "Hare" doesn't describe the ballot; it describes *which candidate is eliminated each round* — the fewest-first-choices one. That single design choice is what separates Hare from every other method on this [variants page](variants/RCV_IRV_variants.md).

## How the count works, step by step

1. Tally each ballot's **top** choice.
2. Does any candidate have **> 50%** of the active ballots? If yes → **winner**.
3. If no, **eliminate** the candidate with the **fewest** first choices.
4. Each eliminated ballot moves to its **next ranked, still-standing** candidate. A ballot whose choices are all eliminated is **exhausted** and sits out the rest.
5. Go back to step 2.

> **Batch elimination** is a common shortcut: in one step, drop *every* candidate who is mathematically out of reach (their total plus all transferable votes below them can't catch the next candidate up). It usually yields the same winner as one-at-a- time Hare and just speeds the count; North Carolina's "instant runoff" statute is written this way.

## Worked example — the 27-voter center squeeze

The repo's minimal squeeze, all on ranked ballots:

```
12  Left   > Center > Right
 9  Right  > Center > Left
 6  Center > Left   > Right
```

First choices: **Left 12, Right 9, Center 6** (27 total; majority = 14).

- Nobody has 14. The fewest first choices is **Center (6)** → eliminate Center.
- Center's 6 ballots have **Left** next → Left 12 + 6 = **18**, Right 9.
- Left has 18 of 27 → **Left wins.**

But look who got cut: **Center is the Condorcet winner** — Center beats Left 15–12 *and* beats Right 18–9 head-to-head. Hare eliminated the one candidate a majority preferred over each rival, because Center was too few voters' *first* pick. That's [center squeeze](RCV_IRV_center_squeeze.md), and it is specific to this Hare rule — [BTR](variants/RCV-IRV-BTR.md), [Coombs](variants/RCV-IRV-Coombs.md), and [Baldwin/Nanson](variants/RCV-IRV-Baldwin-Nanson.md) all elect Center on these very ballots.

*(Verified on the engine: `06_Other/RCV_IRV/RCV_IRV_tabulation_engine` elects Left; STAR and Ranked Robin elect Center.)*

## What your 2nd choice actually does — and when it does nothing

This is the part of Hare that most people never get told plainly, so here it is on its own.

**Your ballot sits in exactly one candidate's stack at a time** — the highest-ranked candidate on it who is still in the race. It is *one* vote, in *one* pile. Your 2nd choice is not half a vote for anyone. It is an **instruction**: *"if my 1st choice is knocked out, move me here."* An instruction that never fires does nothing at all.

So while your favorite is still standing, **the rest of your ballot is not being counted. It is not being counted a little. It is not there.** It becomes real only at the moment your favorite is eliminated, and if that never happens, nobody ever reads it.

That has a consequence people find genuinely surprising: a candidate can be ranked 2nd by a huge number of voters and receive **nothing** from them. There is a worked instance of exactly that in the next section — 20 voters rank Birch second, Birch wins the election, and not one of those 20 rankings contributes a single vote to Birch's total.

**The same fact is also Hare's best feature**, which is why it is worth understanding rather than just complaining about. Because your lower rankings are never read while your favorite survives, adding them **can never hurt your favorite** — that is [later-no-harm](../../../07_Concepts/GLOSSARY.md), the property Hare advocates most prize, and STAR does not have it. Invisibility and the guarantee are one mechanism seen from two sides: IRV protects your first choice by ignoring the rest of your ballot, and [scored](../../../01_STAR/README.md) and [pairwise](../../../05_Ranked_Robin/README.md) methods read all of it and give up that protection. Which trade you prefer is the real argument; pretending either side gets both is not.

## Worked example — five rounds, and the bar keeps dropping

The 27-voter squeeze above finishes in **one** elimination, which is the smallest an IRV count can be. Crowded real fields are not like that, and the difference is not cosmetic — it is where "the ballot is simple, the count is not" ([is RCV simple?](RCV_IRV_is_simple.md)) stops being an assertion.

A town picks one species for its main street. Six on the ballot, 100 voters, and most people rank only the one or two they actually care about — which is what voters do in a crowded field.

```text
20 × Ash>Birch>Cedar        10 × Cedar>Birch      5 × Elm>Birch
10 × Ash                     8 × Cedar            4 × Elm
24 × Birch>Dogwood           8 × Dogwood>Birch    4 × Fir>Elm
                             4 × Dogwood          3 × Fir
```

<!-- report:street_trees_five_rounds_c6_b100 -->
```text
--- RCV / Instant-Runoff Voting (single winner) ---
  Street trees — five rounds, and the bar keeps dropping
 Tabulating 100 ballots (ranked ballots).

ROUND 1
Candidate      Votes  Status
-----------  -------  --------
Ash               30  Hopeful
Birch             24  Hopeful
Cedar             18  Hopeful
Dogwood           12  Hopeful
Elm                9  Hopeful
Fir                7  Rejected

ROUND 2
Candidate      Votes  Status
-----------  -------  --------
Ash               30  Hopeful
Birch             24  Hopeful
Cedar             18  Hopeful
Elm               13  Hopeful
Dogwood           12  Rejected
Fir                0  Rejected
Blank Votes        3  Rejected

ROUND 3
Candidate      Votes  Status
-----------  -------  --------
Birch             32  Hopeful
Ash               30  Hopeful
Cedar             18  Hopeful
Elm               13  Rejected
Dogwood            0  Rejected
Fir                0  Rejected
Blank Votes        7  Rejected

ROUND 4
Candidate      Votes  Status
-----------  -------  --------
Birch             37  Hopeful
Ash               30  Hopeful
Cedar             18  Rejected
Elm                0  Rejected
Dogwood            0  Rejected
Fir                0  Rejected
Blank Votes       15  Rejected

FINAL RESULT
Candidate      Votes  Status
-----------  -------  --------
Birch             47  Elected
Ash               30  Rejected
Cedar              0  Rejected
Elm                0  Rejected
Dogwood            0  Rejected
Fir                0  Rejected
Blank Votes       23  Rejected


Winner(s) — RCV / Instant-Runoff Voting (single winner)
  Birch

--- Transfers and inactive ballots (what the round tables leave out) ---
The tables above give each candidate's round total but not where a
transferred vote came FROM, nor how many ballots stopped counting.
Both are recomputed from the ballots, using the eliminations the
count above actually made.

ROUND 1 — 100 of 100 ballots still active; majority = 51
   Fir eliminated with 7:
      → Elm                       4
      → (no continuing ranking)      3  ← these ballots go inactive

ROUND 2 — 97 of 100 ballots still active (3 inactive); majority = 49
   Dogwood eliminated with 12:
      → Birch                     8
      → (no continuing ranking)      4  ← these ballots go inactive

ROUND 3 — 93 of 100 ballots still active (7 inactive); majority = 47
   Elm eliminated with 13:
      → (no continuing ranking)      8  ← these ballots go inactive
      → Birch                     5

ROUND 4 — 85 of 100 ballots still active (15 inactive); majority = 43
   Cedar eliminated with 18:
      → Birch                    10
      → (no continuing ranking)      8  ← these ballots go inactive

FINAL ROUND — 77 of 100 ballots still active (23 inactive); majority = 39
   Birch                    47  (61.0% of the still-active)  ← elected
   Ash                      30  (39.0% of the still-active)
   Never exhausted, never transferred:
      20 ballots held by Ash carried a lower ranking that was never read
      (the count stopped here, so those preferences did nothing).

Inactive ballots at the final round: 23 of 100 (23.0%).
   Birch's 47 is a majority of the 77 still active but only 47.0% of all 100 cast —
   the 'majority' here is of a shrunken denominator. See
   06_Other/RCV_IRV/concepts/RCV_IRV_exhausted_ballots.md
```
<!-- /report -->

Three things happen here that a three-candidate example structurally cannot show.

**1. The lead changes hands.** Ash leads rounds 1 and 2 on 30 first choices. Birch passes Ash in round 3 — 32 to 30 — and is never headed again. **Reporting this election from its first-choice totals would have named the loser**, which is why RCV-IRV results must always be read to the final round.

**2. The majority bar moves — down.** Every ballot whose ranked species are all eliminated stops counting (the report files these under "Blank Votes"; the precise taxonomy is at [exhausted ballots](RCV_IRV_exhausted_ballots.md)). The active pile shrinks, and the bar shrinks with it:

| After round | Active ballots | Majority needed | Leader |
|:--:|:--:|:--:|---|
| 1 | 100 | **51** | Ash 30 |
| 2 | 97 | **49** | Ash 30 |
| 3 | 93 | **47** | **Birch 32** |
| 4 | 85 | **43** | Birch 37 |
| final | 77 | **39** | **Birch 47 — elected** |

**Birch wins on 47 votes. The election opened needing 51.** The winner never reached the bar the contest started with; the bar came down to meet him. That is not a trick — it is arithmetically correct and it is how every IRV election works — but it is why "majority winner" needs reading carefully: 47 of the 77 ballots still active is 61%, while 47 of the 100 people who voted is **47%**. (What that word is doing: [false majorities](../../../07_Concepts/topics/false_majorities.md). Whether voters *chose* to stop ranking or were *capped* by the ballot is a separate and important distinction: [forced vs voluntary exhaustion](forced_vs_voluntary_exhaustion.md).)

**3. Twenty second-place rankings that never counted.** Look at the `20 × Ash>Birch>Cedar` bloc — a fifth of the electorate, ranking the eventual winner second. Ash is never eliminated, so those ballots sit in Ash's pile from the first count to the last and **their Birch ranking is never read**. Birch's 47 contains none of them. Change all 20 to `Ash>Cedar` and the count is identical, round for round. That is the previous section made concrete.

**Read this fairly — it is not a pathology case.** Birch is the [Condorcet winner](../../../07_Concepts/topics/condorcet/README.md) here, beating every rival head-to-head, so Hare landed on the same species STAR or Ranked Robin would. **The complaint on this page is about the cost of following the count, not about a wrong winner** — which is precisely what makes it worth handing to someone who likes RCV-IRV. For the case where the count also gets the *answer* wrong, that's the [27-voter squeeze](#worked-example-the-27-voter-center-squeeze) above.

Full report and the pairwise audit: [`street_trees_five_rounds_c6_b100.md`](../cases/cases_pages/street_trees_five_rounds_c6_b100.md) · run it yourself: [`.yaml`](../cases/street_trees_five_rounds_c6_b100.yaml) · the same count set beside STAR's two steps: [How the count works, step by step](../../../07_Concepts/topics/tabulation_star_vs_irv.md).

## Strengths

- **Familiar and adopted.** It's the method actually in use — Maine, Alaska, New York City, San Francisco, and dozens of US cities — so "RCV" reform usually means Hare.
- **Beats plain plurality** at the spoiler problem: a trailing similar candidate is eliminated and transfers, instead of splitting the vote outright.
- **Later-no-harm:** ranking a lower choice can never hurt your top choice (a property Hare advocates prize — though it's the flip side of the squeeze).

## Weaknesses

- **Center squeeze** — eliminates a broadly-liked moderate who'd win every head-to-head ([center squeeze](RCV_IRV_center_squeeze.md)).
- **Not monotonic** — *ranking a candidate higher can cause them to lose* ([non-monotonicity](RCV_IRV_non_monotonicity.md)).
- **Not Condorcet** — can fail to elect a candidate who beats all others pairwise.
- **Not summable** — precincts can't just add up totals; ballots must be centralized to run the rounds ([summability](RCV_IRV_lack_of_summability.md); what the central count costs in practice — logistics, audits, trust: [central tabulation](../../../07_Concepts/topics/central_tabulation.md)).
- **Exhausted ballots** when rankings are limited ([exhausted ballots](RCV_IRV_exhausted_ballots.md)).

→ The full run-down of IRV's limitations and the claims made *for* it that don't hold up: [RCV-IRV misconceptions & false claims](rcv_irv_false_claims.md). Head-to-head vs STAR: [RCV-IRV vs. STAR](../../../07_Concepts/topics/rcv_irv_vs_star.md).

## Where it's used

US single-winner "RCV" (Maine statewide, Alaska, NYC primaries, SF, ~50 cities); internationally it's Australia's **Alternative Vote** for the House of Representatives and was the UK's 2011 AV referendum proposal. The multi-winner relative is **[STV](variants/RCV_IRV_variants.md)**.

## Related concept pages

- [Which RCV-IRV? — Hare and the other variants](variants/RCV_IRV_variants.md)
- [RCV vs. IRV vs. RCV-IRV — the naming problem](RCV-IRV-confusing-name.md)
- [Origins & spread — where IRV came from](case_studies/RCV_IRV_history.md)
- [Center squeeze](RCV_IRV_center_squeeze.md) · [Non-monotonicity](RCV_IRV_non_monotonicity.md) · [Exhausted ballots](RCV_IRV_exhausted_ballots.md) · [Lack of summability](RCV_IRV_lack_of_summability.md)

Sources: [Instant-runoff voting — Wikipedia](https://en.wikipedia.org/wiki/Instant-runoff_voting), [Where RCV is used — FairVote](https://fairvote.org/our-reforms/ranked-choice-voting-information/), [NYC Board of Elections — RCV](https://www.vote.nyc/page/ranked-choice-voting)
