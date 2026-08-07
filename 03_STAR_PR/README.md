# 03_STAR_PR — proportional STAR (multi-winner)

*The same 0–5 ballot as single-winner STAR. Nothing changes for the voter — only the count changes, so that seats reflect the electorate's proportions.*

<img src="../01_STAR/01_Learn/img/star_ballot_official_evc.png" width="460" alt="A STAR Voting ballot: five candidates — Andre, Blake, Carmen, David, Erin — each scored 0 to 5. Instructions at top: give your favorite five stars, give your last choice zero or leave blank, equal scores are allowed, score other candidates as desired. This voter marks Andre 5, Blake 0, Carmen 4, David 4, Erin 1. It is the identical ballot used for single-winner STAR.">

*The ballot ([Equal Vote](https://www.equal.vote/star)) — this is the single-winner STAR ballot, reproduced unchanged, because that is exactly the point: proportional STAR asks nothing new of the voter. Everything that makes it proportional happens after the ballots are in. The same paper counted majoritarian instead: [Bloc STAR](../02_STAR_Bloc/README.md).*

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
