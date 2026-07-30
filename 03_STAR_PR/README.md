# 03_STAR_PR — proportional STAR (multi-winner)

The same 0–5 score ballot, counted so that seats reflect the electorate's *proportions* instead of handing every seat to the largest bloc. Three tabulations are represented here, all runnable on the same ballot files by switching `voting_method:`:

**New to multi-winner?** The concept pages for this method live in [`concepts/`](concepts/README.md) — start with [Proportional Representation](concepts/README.md) for the majoritarian-vs-proportional fork, then [the math behind proportional STAR](concepts/STAR_PR/the_math_behind_proportional_star.md). Everything below is the **runnable examples**.

| `voting_method` | Counts as |
|---|---|
| `sss` | Sequentially Spent Score — each voter has a budget of "stars" that elected candidates spend |
| `allocated` | Allocated Score — each winner "uses up" a quota of their strongest supporters |
| `rrv` | Reweighted Range Voting — ballots that already elected someone are down-weighted |

Cases live in [`_main/`](_main) (the `02a/02b/02c` trio counts the SAME 63-ballot election three ways). Majoritarian multi-winner: [`../02_STAR_Bloc/`](../02_STAR_Bloc). STV, the proportional method for *ranked* ballots, lives in [`../06_Other/`](../06_Other).

**Conversation scripts:** the Larry ↔ Adam STAR series is indexed in [Conversation scripts — index](../07_Concepts/about_this_repo/06_conversation_scripts.md).

# file: README.md
