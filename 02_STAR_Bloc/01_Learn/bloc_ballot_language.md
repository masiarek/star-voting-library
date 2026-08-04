# The Bloc STAR ballot and the official definitions

**One line:** the ballot does not change when a race fills several seats — same 0–5 stars, same instructions, nothing to ration — and this page is the official voter-facing wording for a Bloc race, what each sentence of it actually commits to, and the naming rule that makes an unqualified "Multi-Winner STAR Voting" mean *this* method.

→ the count behind the instructions: [Bloc STAR](bloc_star.md) · every legal way to fill a STAR ballot in: [The STAR Ballot](../../01_STAR/01_Learn/voting_styles/README.md) · running one on paper: [Running a paper-ballot demo](../../01_STAR/01_Learn/hands_on/running_a_paper_ballot_demo.md)

**Level: 201 · for voters**

---

## The official ballot text

Equal Vote publishes instruction text for all three STAR variants, so that a paper ballot can state both how to vote and how the count works. The Bloc one reads:

> **Bloc STAR Voting: Score - Then - Automatic - Runoffs.**
>
> Bloc STAR Voting elects majority preferred winners for multi-winner elections.
>
> * This election will elect X winners. Give your favorite five stars. Give your last choice zero or leave blank. Equal scores are allowed. Score other candidates as desired.
> * The two highest scoring candidates are finalists. Your full vote goes to the finalist you prefer. The candidate with the most votes is elected. This process repeats with remaining candidates until all seats are filled.

Source: the paper-ballot guidance published on [docs.bettervoting.com](https://docs.bettervoting.com/help/paper_ballots.html) and [starvoting.org](https://www.starvoting.org/multi_winner). Those are Equal Vote's own materials — which is exactly what makes them authoritative for this method's own ballot language, and worth reading with the lean in mind for anything evaluative.

Two things to notice about the text as a whole before the line-by-line. It is **four sentences long**, which is the practical case for the scored family in a multi-winner race: no rationing rule, no "pick up to three", no ranking discipline to explain. And it states the count on the ballot itself — the second bullet is a complete description of the tabulation, which very few real-world ballots can manage.

## What each sentence commits to

**"This election will elect X winners."** The seat count belongs on the ballot even though it changes nothing about how you mark it. That is the point: under [SNTV or block plurality](bloc_star_vs_other_bloc_methods.md) the seat count *is* your marking rule — three seats, three marks — so a voter arriving from those methods will look for the rule and needs to be told there isn't one.

**"Give your favorite five stars. Give your last choice zero or leave blank."** Identical to single-winner STAR. Blank scores as zero for the totals; where blank and 0 genuinely differ is in what the ballot is understood to *say*, which is [abstention vs. zero vs. NOTA](../../01_STAR/01_Learn/properties_and_limits/abstention_vs_zero_vs_nota.md).

**"Equal scores are allowed."** No ranking to satisfy, so two candidates can share a 5 or share a 0. When two candidates you scored equally meet in a runoff, your ballot lands in **Equal Support** — that means "I don't tip this particular matchup", not "my ballot was discounted"; your scores already did full work choosing the finalists ([the long answer](../../01_STAR/01_Learn/reference/are_equal_score_votes_discounted.md)).

**"The two highest scoring candidates are finalists. Your full vote goes to the finalist you prefer."** *Full* vote is the load-bearing word: the [automatic runoff](../../01_STAR/01_Learn/the_count/STAR_Automatic_Runoff.md) is one voter, one vote, no matter how big the gap between your two scores. A 5-vs-4 preference pushes exactly as hard as 5-vs-0.

**"The candidate with the most votes is elected."** The one sentence that misleads if read quickly: **"votes" here means runoff preferences, not stars.** The candidate with the most stars is not necessarily elected, and in a multi-seat race the point leader can be shut out of every seat — [the score leader can win no seat](score_leader_no_seat.md).

**"This process repeats with remaining candidates until all seats are filled."** The removal step, and the whole of the multi-winner machinery, in eleven words. "Remaining candidates" is doing quiet work: the *ballots* don't change between seats, the *field* does. Nothing is spent, reweighted, or transferred — that is [STAR-PR](../../03_STAR_PR/01_Learn/)'s job, and the reason the two methods answer different questions.

## What it is called, and by whom

| Where | The name | Notes |
|---|---|---|
| STAR Voting technical specifications, §1.c | **Bloc STAR Voting**, aka **Basic Multi-Winner STAR Voting** | conducted by repeating the STAR process until every seat is filled |
| Technical specifications, §1.e | **Multi-Winner STAR Voting** | may mean bloc or proportional — but **unless otherwise specified, assume bloc** |
| BetterVoting, race setup | **Basic Multi-Winner** | the STAR ballot with more than one winner |
| BetterVoting, stored data | `votingMethod: "STAR"` + `num_winners` | the name "Bloc STAR" is never written down — it is implied by ballot + seat count ([BV129 note](../02_Examples/bv129_1086_method_name_note.md)) |
| This library | `voting_method: Bloc STAR` | aliases `bloc`, `bloc star`; house style spells out the method |

The §1.e default is the one to remember. "Multi-Winner STAR Voting" in a bylaw, a press release, or a ballot measure means **Bloc** unless the document says proportional — so a body that meant to adopt proportional representation and wrote "multi-winner STAR" has, on the published specification, adopted the majoritarian method instead. (The specification is served as a PDF, currently v1.3, from [starvoting.org/technical_specifications](https://www.starvoting.org/technical_specifications).)

## Filling it out well

The advice is the same as single-winner STAR, because the ballot is: **score honestly.** Favorites at 5, the candidates you least want at 0 or blank, and the scores in between carrying both your order of preference and how strongly you support each one.

The one tactic that specifically backfires in a multi-seat race is **padding the top score to the seat count**. If nine seats are up, giving five stars to nine candidates does not hand you nine votes — it surrenders your say in *which* of those nine win and in what order the seats fill, because your ballot registers Equal Support in every runoff among them. If you would honestly be content with any of the nine, that is an honest ballot and a good one. If you have favorites among them, score the favorites highest and give the others the number of stars you actually think they deserve.

Two supports for that, from different directions: [Over 50%](over_50_percent.md) shows how little a unanimous majority buys when it is unanimous about a *candidate* rather than a slate, and [honest limits](bloc_honest_limits.md) is candid about the opposite pressure — a cohesive slate scoring uniformly is a real strategy in this method, and it recurs once per seat. Neither changes the advice for an individual voter; both are worth knowing before recommending the method to a body.

The longer public version of this answer, written for a real 2021 multi-winner reorganization election, is the [Multnomah County Democrats' STAR Voting FAQ](https://medium.com/countydemocratreader/faq-for-the-2021-multdems-star-voting-reorg-election-e0a811f66b29) — advocacy-adjacent, and the clearest thing published on how to *vote* in a Bloc race rather than how to count one.

## See also

- [Bloc STAR](bloc_star.md) — the count these instructions describe
- [The STAR Ballot — and every legal way to fill it out](../../01_STAR/01_Learn/voting_styles/README.md) — the single-winner gallery, all of which is legal here too
- [Ties in Bloc STAR](bloc_tiebreaks.md) — what happens when a seat's runoff comes out level
- [At-large elections and the Voting Rights Act](at_large_and_the_vra.md) — the one setting where none of this ballot language is the issue
- [Exercise 12 — bloc vs. proportional](../../01_STAR/05_Practice/ex12_bloc_vs_proportional.md) — the same ten ballots counted both ways
- [Glossary: Bloc STAR terms](glossary_bloc_star.md)
