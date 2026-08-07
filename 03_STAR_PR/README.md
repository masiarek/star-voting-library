# 03_STAR_PR — proportional STAR (multi-winner)

*The same 0–5 scoring grid, counted so that seats mirror the electorate. For bodies where representing different viewpoints matters more than finding the single slate most voters prefer.*

<img src="01_Learn/img/ballot_proportional_star.png" width="460" alt="A Proportional STAR Voting ballot. Heading: Proportional STAR Voting. Above the race: This election will elect 3 winners. Instructions: score all candidates from 0 to 5 stars; those you leave blank receive a zero; if you don't have a preference you can give candidates the same scores. A 0-5 grid with one row per candidate, marked Abby 4, Ben 5, Carmen 3, DeAndre 5, Eric 0. Below the grid: winners in Proportional STAR Voting are selected in rounds; each round elects the candidate with the highest total score and then designates that candidate's strongest supporters as represented; subsequent rounds include all voters who are not yet represented.">

*The ballot — drawn from [Equal Vote](https://www.equal.vote/)'s own Proportional STAR ballot. **The scoring grid is identical to [single-winner STAR](../01_STAR/README.md)'s** — 0–5, one row per candidate, nothing rationed, so a voter who can fill in one can fill in the other. What differs is printed above and below it: the seat count, and a footer describing a completely different count — **rounds**, each electing the highest scorer and then marking that winner's strongest supporters as represented, so later rounds belong to the voters not yet spoken for. The same paper counted majoritarian instead: [Bloc STAR](../02_STAR_Bloc/README.md).*

The same 0–5 score ballot, counted so that seats reflect the electorate's *proportions* instead of handing every seat to the largest bloc. Three tabulations are represented here, all runnable on the same ballot files by switching `voting_method:`:

**New to multi-winner?** The concept pages for this method live in [`01_Learn/`](01_Learn/README.md) — start with [Proportional Representation](01_Learn/README.md) for the majoritarian-vs-proportional fork, then [the math behind proportional STAR](01_Learn/STAR_PR/the_math_behind_proportional_star.md). Everything below is the **runnable examples**.

| `voting_method` | Counts as | The same 63 ballots, counted this way |
|---|---|---|
| `allocated` | **[Allocated Score](01_Learn/STAR_PR/README.md)** — each winner "uses up" a quota of their strongest supporters. Equal Vote's recommended STAR-PR ([electowiki](https://electowiki.org/wiki/Allocated_Score)) | [02a — the count in full](02_Examples/cases/cases_pages/02a_c5_b63_proportional-allocated-score.md) |
| `sss` | **[Sequentially Spent Score](01_Learn/STAR_PR/README.md)** — each voter has a budget of "stars" that elected candidates spend ([electowiki](https://electowiki.org/wiki/Sequentially_Spent_Score)) | [02b — the count in full](02_Examples/cases/cases_pages/02b_c5_b63_proportional-sss.md) |
| `rrv` | **[Reweighted Range Voting](01_Learn/STAR_PR/README.md)** — ballots that already elected someone are down-weighted. The one that does **not** pass the [Hare Quota Criterion](01_Learn/what_proportional_means.md) ([electowiki](https://electowiki.org/wiki/Reweighted_Range_Voting)) | [02c — the count in full](02_Examples/cases/cases_pages/02c_c5_b63_proportional-rrv.md) |

Cases live in [`02_Examples/`](02_Examples/README.md) (the `02a/02b/02c` trio in the right-hand column above counts the SAME 63-ballot election three ways — the fastest way to see where the three methods agree and where they part). Majoritarian multi-winner: [Bloc STAR](../02_STAR_Bloc/README.md). STV, the proportional method for *ranked* ballots, lives in [06_Other](../06_Other/README.md).

## Start here

- **[Proportional to *what*?](01_Learn/proportional_to_what.md)** (101) — no parties on the ballot, so what is being made proportional? Answer: quotas of *voters*, with the factions discovered by the ballots instead of declared beforehand.
- **[What "proportional" actually means](01_Learn/what_proportional_means.md)** — read before advocating for any of this. Exact proportionality is the only unambiguous definition and almost no election meets it; a quota is a guarantee, not a price; and without parties there is no longer an obvious thing to be proportional *to*.
- **[Bloc STAR vs Proportional STAR — the same ballots, two councils](../method_comparisons/bloc_vs_pr/README.md)** (101) — two voters, three candidates, two seats. The smallest election in which the majoritarian and proportional counts fill a council differently, checkable in your head.
- **[STAR-PR — the three methods](01_Learn/STAR_PR/README.md)** — quota + reweighting, and how `allocated` / `sss` / `rrv` differ.
- **[Simulating proportional systems](01_Learn/simulating_pr.md)** (401) — where the quantitative claims about PR come from, and what to demand of a study before believing one.

**Conversation scripts:** the Larry ↔ Adam STAR series is indexed in [Conversation scripts — index](../07_Concepts/about_this_repo/conversation_scripts.md).

# file: README.md
