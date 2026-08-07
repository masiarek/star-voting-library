# 03_STAR_PR — proportional STAR (multi-winner)

*The same 0–5 scoring grid, counted so that seats mirror the electorate. For bodies where representing different viewpoints matters more than finding the single slate most voters prefer.*

<img src="01_Learn/img/ballot_proportional_star.png" width="460" alt="A Proportional STAR Voting ballot. Heading: Proportional STAR Voting. Above the race: This election will elect 3 winners. Instructions: score all candidates from 0 to 5 stars; those you leave blank receive a zero; if you don't have a preference you can give candidates the same scores. A 0-5 grid with one row per candidate, marked Abby 4, Ben 5, Carmen 3, DeAndre 5, Eric 0. Below the grid: winners in Proportional STAR Voting are selected in rounds; each round elects the candidate with the highest total score and then designates that candidate's strongest supporters as represented; subsequent rounds include all voters who are not yet represented.">

*The ballot — drawn from [Equal Vote](https://www.equal.vote/)'s own Proportional STAR ballot. **The scoring grid is identical to [single-winner STAR](../01_STAR/README.md)'s** — 0–5, one row per candidate, nothing rationed, so a voter who can fill in one can fill in the other. What differs is printed above and below it: the seat count, and a footer describing a completely different count — **rounds**, each electing the highest scorer and then marking that winner's strongest supporters as represented, so later rounds belong to the voters not yet spoken for. The same paper counted majoritarian instead: [Bloc STAR](../02_STAR_Bloc/README.md).*

The same 0–5 score ballot, counted so that seats reflect the electorate's *proportions* instead of handing every seat to the largest bloc. Three tabulations are represented here, all runnable on the same ballot files by switching `voting_method:`:

**New to multi-winner?** The concept pages for this method live in [`01_Learn/`](01_Learn/README.md) — start with [Proportional Representation](01_Learn/README.md) for the majoritarian-vs-proportional fork, then [the math behind proportional STAR](01_Learn/STAR_PR/the_math_behind_proportional_star.md). Everything below is the **runnable examples**.

| `voting_method` | Counts as |
|---|---|
| `sss` | Sequentially Spent Score — each voter has a budget of "stars" that elected candidates spend |
| `allocated` | Allocated Score — each winner "uses up" a quota of their strongest supporters |
| `rrv` | Reweighted Range Voting — ballots that already elected someone are down-weighted |

Cases live in [`02_Examples/`](02_Examples/README.md) (the `02a/02b/02c` trio counts the SAME 63-ballot election three ways). Majoritarian multi-winner: [Bloc STAR](../02_STAR_Bloc/README.md). STV, the proportional method for *ranked* ballots, lives in [06_Other](../06_Other/README.md).

**Conversation scripts:** the Larry ↔ Adam STAR series is indexed in [Conversation scripts — index](../07_Concepts/about_this_repo/conversation_scripts.md).

# file: README.md
