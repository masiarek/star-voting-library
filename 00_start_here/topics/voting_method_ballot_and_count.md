# What is a voting method? — a ballot **and** a count

*The single most useful idea in this whole topic: a voting method is **two parts**, not one, and you can't judge one without the other.*

→ Spoken version: [What Is a Voting Method? (conversation)](what_is_a_voting_method.md) · primer: [Ballot & terminology basics](ballot_and_terminology_basics.md) · next: [STAR — start here](../STAR_Voting/STAR_start_here.md).

---

## The two parts

A **voting method** is the rule that turns a stack of individual ballots into one collective decision. It has two independent halves:

- **The ballot** — what voters get to *express*: pick one, rank them, score them, or choose several.
- **The count** — how those marks become a *winner*: add them up, simulate a runoff, or check who beats whom head-to-head.

The two are independent: **the same ballot can be counted several different ways, and they can crown different winners.** A ranked ballot can be run as instant-runoff (RCV-IRV), as a Condorcet "who-beats-everyone" count (Ranked Robin), or proportionally (STV). So naming only the ballot — "ranked-choice," "score voting" — leaves out the half that actually decides the election.

That's the whole reason to name both parts. The ballot is the easy, likeable half, the part you're shown. The count is where the winner comes from, and it's the half people get talked into ignoring. **When someone praises a ballot, ask: "fine, now how do you count it?"**

The choice of method is not neutral plumbing — it is part of what *decides* the outcome. Different methods pick different winners from the exact same ballots, and that gap is widest exactly where it matters: when several similar candidates split a shared bloc, and when opinion is polarized. Richer ballots (ranking or scoring) can capture more information than choose-one, and that added expressiveness matters more as the questions get harder. (See [scores vs ranks](../scores_and_ranks/scores_vs_ranks.md).)

## Plurality vs majority — two different bars

These two words name different *winning thresholds*, and keeping them straight is half of understanding voting:

- **Plurality** — the *most* votes wins, even if that's well under half. ("First-past-the-post," "choose-one.")
- **Majority** — *more than half*, 50% + 1.

In a two-way race they're identical: the most votes *is* over half. The gap only opens with **three or more candidates** — and that gap is where the trouble lives.

**A worked example.** 100 voters, three candidates; first choices Andre 40, Blake 35, Carmen 25. Under plurality **Andre wins** — the most votes. But 60 of 100 wanted someone else, so Andre has no majority. And if Blake and Carmen are two flavors of one coalition, choose-one just **split** a 60-vote bloc and crowned the candidate a majority actively opposed — the [spoiler effect](spoiler_effect.md).

A majority rule wouldn't accept that. Since nobody cleared half, it demands another step: a runoff. STAR's [automatic runoff](../STAR_Voting/the_count/STAR_Automatic_Runoff.md) is that step — after scoring, the top two meet head-to-head, and the winner holds a majority *between those two finalists*. That's not proof the winner is everyone's favorite across the whole field, but it's exactly the check plurality never even performs.

## Two takeaways

1. **The framing:** a voting method is a ballot **and** a count — judge them together. The ballot is the part you're shown; the count is where the winner comes from. When someone praises the ballot, ask how it's counted.
2. **The warning:** *"most votes" isn't "over half."* Choose-one plurality is the method that most easily crowns the candidate a majority voted against.

## Where to go next

- The spoken companion, with the demo run live: [What Is a Voting Method? (conversation)](what_is_a_voting_method.md)
- The terminology cluster hiding behind "RCV": [Ballot & terminology basics](ballot_and_terminology_basics.md) · [ballot styles](ballot_styles.md)
- Ballot families: [scores vs ranks](../scores_and_ranks/scores_vs_ranks.md) · the problem this all fixes: [the spoiler effect](spoiler_effect.md)
- The method this library teaches: [STAR — start here](../STAR_Voting/STAR_start_here.md) · [its benefits](../STAR_Voting/getting_started/STAR_benefits.md)
