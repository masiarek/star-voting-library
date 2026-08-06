# At-large elections and the Voting Rights Act

**One line:** the [majority sweep](majority_sweep.md) is not only a design property — in a jurisdiction where a racial or language minority is concentrated in one part of town, it is the exact mechanism federal courts call **vote dilution**, and a 0–5 ballot does nothing to change that, because the dilution comes from filling the seats **at-large**, not from how the ballot is marked.

→ The mechanism, without the law: [the majority sweep](majority_sweep.md) · the family this applies to equally: [Bloc STAR among the at-large methods](bloc_star_vs_other_bloc_methods.md) · what to use instead: [STAR-PR](../../03_STAR_PR/01_Learn/README.md) · the method itself: [Bloc STAR](bloc_star.md)

**Level: 301 · deep dive**

*Not legal advice. This page explains a standard that decides whether a body may use an at-large method at all; a jurisdiction actually facing the question needs counsel, not a docs page.*

---

## The advice is right — the one-liner usually attached to it is not

The recommendation itself is not in dispute, and this library repeats it: **Bloc STAR should never be used where geographic representation matters**, and never in a jurisdiction where a historically marginalized community is clustered in one sector of a multi-seat district. (Source: [starvoting.org/multi_winner](https://www.starvoting.org/multi_winner). That is the campaign's own site — authoritative for what Equal Vote recommends, advocacy-adjacent for anything else, and cited here only for the recommendation.)

The sentence that usually carries the advice is another matter. At-large bloc voting, the claim goes, "was banned in the Voting Rights Act." It wasn't. At-large elections are legal, extremely common, and in use by thousands of American jurisdictions right now. What the Act does is make an at-large system **actionable** — challengeable, and often indefensible — when *in that particular place* it produces dilution.

The correction is worth making rather than waving through, in both directions. A recommendation that overstates its legal authority loses the room the moment somebody in it knows better. And the accurate version is more useful anyway, because the legal test names precisely which jurisdictions the warning is about.

## What Section 2 forbids

Section 2 of the Voting Rights Act (52 U.S.C. §10301) prohibits any voting practice that results in the denial or abridgement of the right to vote on account of race, color, or membership in a language-minority group. Two features of it matter here:

- **It is a results test, not an intent test.** Congress amended §2 in 1982 to say so explicitly, after *City of Mobile v. Bolden* (1980) read the prior text to require proof of discriminatory *purpose*. A jurisdiction that adopted its at-large system for entirely innocent reasons — most did — can still lose a §2 case on what the system now does.
- **It names no methods.** Section 2 does not list at-large voting, block plurality, or anything else. There is no schedule of banned counts to check a method against, which is exactly why "banned in the VRA" misdescribes it.

## The Gingles test, read next to the sweep

*Thornburg v. Gingles*, 478 U.S. 30 (1986), is the case that turned §2 into a workable standard for exactly this situation — it concerned **multimember districts** in the North Carolina General Assembly. It sets three preconditions a vote-dilution claim must clear before a court weighs the totality of the circumstances:

1. The minority group is **sufficiently large and geographically compact** to constitute a majority in a single-member district.
2. The minority group is **politically cohesive**.
3. The majority **votes sufficiently as a bloc** usually to defeat the minority's preferred candidate.

Set that beside [the majority sweep](majority_sweep.md) and it is the same paragraph in a different vocabulary. Precondition 1 is *"districts would have elected somebody here"*. Precondition 2 is the sweep page's **cohesive**, pointed at the minority. Precondition 3 is that same word pointed at the majority — and a cohesive majority winning every seat on the same unchanged ballots is not a side effect of Bloc STAR, it is the thing the method is built to do well.

> **A vocabulary collision worth keeping straight.** "Bloc" in precondition 3 means *voting as a bloc* — people moving together. "Bloc" in *Bloc STAR* means *a bloc of seats* — the count filling several at once. Different senses, and they meet inside the same sentence whenever this topic comes up. Racially polarized voting is the first; the method is the second; the §2 problem is what happens when you run the second on top of the first.

Note what the preconditions do **not** require: they don't require the minority to be small, or the jurisdiction to have meant harm, and they don't make at-large systems illegal per se. *Gingles* is a case-by-case standard. A town where voting isn't polarized, or where no minority community is geographically compact, doesn't fail it.

## Does a scored ballot change the analysis?

No court has considered a STAR ballot in a §2 case, and this page is not predicting how one would come out. But the analysis doesn't run on ballots, so there is not much room for the answer to be interesting:

- **What Bloc STAR genuinely fixes: vote splitting.** Under [Block Plurality](bloc_star_vs_other_bloc_methods.md) a community that runs three candidates for three seats can split its own support and win nothing with the votes to win something — which is a real, separate injury, and one reason at-large plurality is the worst version of this. Scoring one candidate never costs another under STAR, so that failure mode is gone.
- **What it does not fix: the sweep.** Precondition 3 describes a majority that reliably votes against the minority's preferred candidate. Hand that majority a 0–5 ballot and it scores that candidate 0. The scoring round then supplies both finalists from the majority's own slate, the runoff confirms them, and the removal step starts the next seat on the same ballots. Bloc STAR is *better* than plurality at electing what the majority actually wants — which, in the polarized case the preconditions single out, is the entire problem.
- **The honest qualification, and its limit.** STAR does reward crossover support: where voting is *not* polarized, a candidate acceptable across the electorate can win on stars from everyone, and the [score leader / runoff](score_leader_no_seat.md) machinery gives broad acceptability real purchase. That is a genuine virtue. It is not a defense, because preconditions 2 and 3 exist precisely to identify the places where crossover support isn't happening. How a method behaves when voting isn't polarized says nothing about the case where it is.

The short version: the ballot is not the thing under challenge. **At-large counting is.**

## What jurisdictions do about it

Most often, they stop electing at-large: the standard §2 remedy is single-member districts, which is what precondition 1 is measuring the possibility of in the first place.

Where a body wants to stay at-large, courts and consent decrees have accepted **semi-proportional** at-large methods instead — limited voting and cumulative voting both appear in §2 settlements, the long-running example being Chilton County, Alabama, under a 1988 consent decree. That is the same move this library makes at [the multi-winner fork](../../07_Concepts/topics/electing_more_than_one.md), arrived at from the other direction: if you must fill the seats at-large, **stop filling them majoritarian-ly**. The scored and ranked versions of that answer are [STAR-PR](../../03_STAR_PR/01_Learn/README.md) and [STV](../../06_Other/STV/README.md); the older at-large family, including the two remedies just named, is laid out in [Bloc STAR among the at-large methods](bloc_star_vs_other_bloc_methods.md).

## California's version is stricter

The **California Voting Rights Act** (2002) drops the hardest precondition: a CVRA plaintiff need not show that the minority community is geographically compact enough to form a majority in a single district. Racially polarized voting in an at-large system is close to sufficient on its own. Hundreds of California cities, school districts, and special districts have converted from at-large to district elections since — the number in circulation is in the many hundreds, and the exact count depends on who is counting and when.

The practical consequence for anyone drafting a proposal: **"adopt Bloc STAR, keep the seats at-large" is at its most exposed in California**, where the defense that no district could have been drawn is not available.

## The rule this leaves you with

- Filling several seats at-large with a majoritarian count is the risk. Which majoritarian count — plurality, approval, ranked, or STAR — does not change the analysis.
- The warning is aimed at **localized** communities: a minority spread evenly across a jurisdiction fails precondition 1 and gets no help from districts either. That case is an argument for proportional representation, not for districts.
- Bloc STAR is a fine method for a body that is choosing **the best few candidates** — a shortlist, a primary that advances a top set, a club's officers. The exposure begins when the body is meant to **represent a population**.
- If a 45% side holding zero seats would read as a broken election, the method was chosen wrong before any of this was litigated. Go proportional: [Electing more than one, simply](../../07_Concepts/topics/electing_more_than_one.md).

## Sources

- [*Thornburg v. Gingles*, 478 U.S. 30 (1986)](https://en.wikipedia.org/wiki/Thornburg_v._Gingles) — the three preconditions, and the multimember-district context
- [Section 2 of the Voting Rights Act](https://en.wikipedia.org/wiki/Voting_Rights_Act_of_1965#Section_2) — the 1982 results test, after *City of Mobile v. Bolden* (1980)
- [California Voting Rights Act](https://en.wikipedia.org/wiki/California_Voting_Rights_Act) — the 2002 statute and the conversion wave
- [Multi-Winner STAR Voting](https://www.starvoting.org/multi_winner) — Equal Vote's own recommendation, quoted above with its lean disclosed

## See also

- [The majority sweep](majority_sweep.md) — the same mechanism with no law in it
- [Honest limits](bloc_honest_limits.md) — where this sits among everything else Bloc STAR concedes
- [Bloc STAR among the at-large methods](bloc_star_vs_other_bloc_methods.md) — SNTV, limited, cumulative, block plurality, and what each does to a clustered minority
- [Multi-member plurality](../../method_comparisons/multi_member_plurality/multi_member_plurality.md) — the incumbent at-large method, counted side by side
- [Glossary: Bloc STAR terms](glossary_bloc_star.md)
