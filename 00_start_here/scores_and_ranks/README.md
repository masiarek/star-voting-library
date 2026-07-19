# Scores and ranks — the two kinds of ballot data

The single most consequential distinction in ballot design: a **rank** records *order* ("I prefer A to B"), a **score** records *strength* ("A is a 5, B is a 1"). Everything else in the library — why methods disagree, what converts cleanly and what doesn't — builds on getting this pair straight.

**Start here → [Scores vs. Ranks — Don't Confuse Ranks and Ratings](scores_vs_ranks.md)**

## The pages

- [Scores vs. Ranks](scores_vs_ranks.md) — the core distinction: relative vs. absolute preference, and why it has real consequences.
- [The Ranked Ballot](ranked_ballot.md) · [The Score Ballot](score_ballot.md) — one anatomy page per ballot type.
- [Strict ranks](strict_ranks.md) · [Weak ranks](weak_ranks.md) · [Strict vs. Weak Ranks](strict_vs_weak_ranks.md) — not all ranked ballots are the same: whether ties are allowed changes what the ballot can express.
- [The Fidelity Ladder](fidelity_ladder.md) — converting between scores and ranks: which direction loses information, and how much.
- [Scale granularity can flip the winner](scale_granularity_flips_the_winner.md) — a 301 case: the *same* opinions on a 0–5 vs. a wider scale can elect different candidates.
- [ABIF — the all-in-one ballot format](abif_format.md) — the election-methods **interchange** format that writes ranks *and* scores in one grammar (`Allie/5 =Billy/5 >Candace/4`), decoded and weighed honestly against this library's YAML grid.

## Related

- [Alternate ballot styles — one voter, three ballots](../topics/ballot_styles.md) — the same opinion marked on a ranking, Yes/No, and 0–5 ballot, side by side.
