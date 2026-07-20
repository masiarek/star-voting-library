# The benefits of STAR Voting

*A scannable reference to **why** STAR (Score Then Automatic Runoff) is worth adopting — each benefit in a sentence or two, with a link to the lesson that proves it. For the narrated versions, see the conversation scripts [What's so good about STAR](../reference/whats_so_good_about_STAR_Voting.md) and [Why do you love STAR](../reference/why_do_you_love_STAR_Voting.md), and the [Why STAR Voting deck](../../topics/Why_STAR_Voting.md).*

→ Start with the mechanics: [STAR — start here](../STAR_start_here.md). Kept honest by: [STAR's honest limits](../properties_and_limits/STAR_honest_limits.md).

<img src="../../img/star_ballot_example.png" width="460" alt="A real STAR ballot: five candidates (Andre, Blake, Carmen, David, Ella) each rated 0–5 stars, with the instructions — give your favorite(s) five stars, your last choice(s) zero; equal scores mean no preference; blanks count as zero; the two highest-scoring candidates are finalists and your full vote goes to the finalist you prefer">

*Here's the whole ballot: rate each candidate 0–5, like a five-star review — equal scores allowed, blanks count as zero. Everything below is what that one simple change buys you.*

---

## A more expressive ballot

You score every candidate 0–5 by how much you support them, instead of picking one name. That captures **order *and* intensity** — "my 2nd choice and I love her" and "my 2nd choice, the lesser evil" are different statements a ranked or choose-one ballot writes down identically. Scores are a superset of ranks: you can always read a ranking off a score ballot, never the reverse. More information in means a more representative winner out. See [the score ballot itself](../../scores_and_ranks/score_ballot.md), [scores vs ranks](../../scores_and_ranks/scores_vs_ranks.md), and [the equally-weighted vote](../properties_and_limits/equally_weighted_vote.md).

## No vote splitting, no spoilers

Because you rate each candidate independently, adding a candidate you like never bleeds support from another candidate you like. Two similar candidates can't divide their shared supporters and hand the win to someone the majority didn't want — the [spoiler effect](../../topics/spoiler_effect.md) that plagues choose-one voting. Honesty becomes your strongest ballot. This is also what **opens the door to new voices**: a fresh candidate or an independent can enter without playing spoiler, so voters can back a new perspective on its merits instead of being warned off "wasting" their vote. (STAR reduces spoilers dramatically rather than perfectly — see [residual vote-splitting](../properties_and_limits/residual_vote_splitting.md).)

## Every winner earns a majority

The automatic runoff means whoever takes office actually beat the runner-up **head-to-head**, among voters who expressed a preference — no more winners with 35% that the other 65% actively opposed. And it's a *real* majority of the electorate — not RCV-IRV's kind, where the reported "majority" is only of the ballots still **left** after eliminations exhaust the rest (a bare-plurality winner re-labeled a majority once enough ballots drop out). See [the Automatic Runoff](../the_count/STAR_Automatic_Runoff.md), [three notions of "winner"](../properties_and_limits/STAR_three_winner_notions.md), and — for the contrast — how RCV-IRV manufactures its majority from [exhausted ballots](../../RCV_IRV/exhausted_ballots_301.md).

## One ballot, not two trips — cost savings and turnout

The runoff is **[automatic](../the_count/STAR_Automatic_Runoff.md)**: it's computed from the ballots already cast, so there's no separate runoff election. Where a jurisdiction currently runs a primary plus a general, or a first round plus a second-round runoff, STAR delivers the runoff for free — **one election instead of two**. That saves the direct cost of administering an extra election, and it spares voters a second trip to the polls. It also sidesteps a well-known problem: separate second-round runoffs typically draw far *lower* turnout than the first round, so the "decisive" round is decided by fewer, less representative voters. STAR's runoff keeps the full electorate.

## Summable and verifiable

STAR is **summable**: each precinct can publish its score totals plus the finalist head-to-head counts, and those subtotals **add up** to the correct statewide result — a fixed, small amount of data per precinct that anyone can re-add by hand. This is a real structural advantage over RCV-IRV, whose eliminate-and-transfer rounds are **not** summable (you generally need every ballot in one place to run the count, and precinct winners needn't predict the whole). See [STAR summability](../properties_and_limits/STAR_summability.md), the [summability topic hub](../../topics/summability/), and — for the contrast — [why RCV-IRV isn't summable](../../RCV_IRV/RCV_IRV_lack_of_summability.md).

## More accurate, more representative results

Feeding the count more information (intensity, equals, full expression) and finishing with a majority runoff tends to elect the candidate [who best represents](../../topics/what_makes_a_good_winner.md) the whole electorate. In large simulation studies STAR ranks among the highest methods on **voter-satisfaction efficiency**, and it elects the head-to-head (Condorcet) winner in the large majority of elections — the broadly-supported compromise that first-choice methods can squeeze out. It does **not** do this every time (no method can be perfect — that's a theorem), so this is a strong tendency, not a guarantee; the exact failure modes are laid out honestly in [STAR's honest limits](../properties_and_limits/STAR_honest_limits.md).

## Better campaigns, broader appeal

To win under STAR you need to be scored well by your *opponents'* supporters too — a 3 or a 4 from someone whose favorite is elsewhere is what carries you into and through the runoff. That changes the incentive: trashing a rival backfires when their voters can lower your score in return, so the rewarded strategy is outreach and coalition-building rather than base-energizing and mudslinging. The tendency is toward broadly-supported [consensus winners](../../topics/what_makes_a_good_winner.md). State this honestly as *what the incentives reward* — the large-scale empirical record is thin because adoption is recent, so it's a well-grounded prediction, not a proven outcome (see the [honest caveat](#the-honest-caveat) below).

## One method for single-winner, multi-winner, and PR

The same 0–5 ballot scales to whatever seat you're filling. **Single-winner STAR** fills one office; **[Bloc STAR](../../../02_STAR_Bloc/)** elects a slate when you want the *most-preferred* set; and **[Proportional STAR](../../proportional_representation/STAR_PR/README.md)** ([PR hub](../../proportional_representation/README.md)) fills a body so that like-minded voters win seats in proportion to their numbers. One ballot voters already know, across the whole ballot. Because single-winner STAR already delivers a majority runoff from one round of voting, it also **removes the usual reason for a separate primary** — though a multi-winner method is the right tool when a body, not a single office, is being chosen.

## Simple and familiar

The ballot is the five-star rating everyone already uses for movies and rideshares: rate each candidate 0–5, equals allowed, blanks allowed. That familiarity means low error rates, few spoiled ballots, and nothing thrown away. See [the STAR ballot & voting styles](../STAR_ballot_voting_styles.md).

---

## The honest caveat

STAR is [strategy-*resistant*, not strategy-*proof*](../../topics/strategic_voting.md); it *usually* elects the head-to-head winner, but not always; and like every method it can be gamed in constructed cases. The repo documents these squarely — see [STAR's honest limits](../properties_and_limits/STAR_honest_limits.md), [residual vote-splitting](../properties_and_limits/residual_vote_splitting.md), and [favorite betrayal (301)](../properties_and_limits/favorite_betrayal_voting_301.md). Overselling a reform is how you get backlash; STAR earns trust by being square about its limits.

## Related

- [STAR — start here](../STAR_start_here.md) · [STAR's hybrid nature](../the_count/STAR_hybrid_nature.md) · [the folder index](../README.md)
- Conversation scripts: [What's so good about STAR](../reference/whats_so_good_about_STAR_Voting.md) · [Why do you love STAR](../reference/why_do_you_love_STAR_Voting.md)
- External: [Equal Vote Coalition — STAR overview](https://www.equal.vote/star)
