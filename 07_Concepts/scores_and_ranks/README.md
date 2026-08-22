# Scores and ranks — the two kinds of ballot data

The single most consequential distinction in ballot design: a **rank** records *order* ("I prefer A to B"), a **score** records *strength* ("A is a 5, B is a 1"). Everything else in the library — why methods disagree, what converts cleanly and what doesn't — builds on getting this pair straight.

**Start here → [Scores vs. Ranks — Don't Confuse Ranks and Ratings](scores_vs_ranks.md)**

## The pages

- [Scores vs. Ranks](scores_vs_ranks.md) — the core distinction: relative vs. absolute preference, and why it has real consequences.
- [Preference vs. Support](preference_vs_support.md) — the vivid special case: `1,0,1,0` and `5,4,5,4` have the *same preference* but *opposite support*, and as ranks they're identical. Which do you like more, vs. how much you like each.
- [The Ranked Ballot](ranked_ballot.md) · [The Score Ballot](score_ballot.md) — one anatomy page per ballot type.
- [Strict ranks](strict_ranks.md) · [Weak ranks](weak_ranks.md) · [Strict vs. Weak Ranks](strict_vs_weak_ranks.md) — not all ranked ballots are the same: whether ties are allowed changes what the ballot can express.
- [The Fidelity Ladder](fidelity_ladder.md) — converting between scores and ranks: which direction loses information, and how much.
- [Scale granularity can flip the winner](scale_granularity_flips_the_winner.md) — a 301 case: the *same* opinions on a 0–5 vs. a wider scale can elect different candidates.
- [A ranking does not determine a score result](ranking_does_not_determine_scores.md) — a 301 deep dive on the step everyone takes silently: converting a ranked profile to scores is an *assumption*, not a translation. 74 voters, one preference order, two legitimate ways of using 0–5, two different winners — plus the sweep that tells you when it matters and when it can't.
- [What the ballot can and cannot say — expressiveness, measured](ballot_expressiveness_measured.md) — a 301 deep dive that counts what each paper can record and then varies the ballot and the counting rule independently: past six candidates the two ballots express *disjoint* sets of orderings, a real (capped) ranked ballot is the least expressive of all, and RCV-IRV can't spend the resolution either way.
- [Grading as a rival primitive](grading_as_a_rival_primitive.md) — Balinski & Laraki's stronger claim: not that ranks are lossy, but that "how good is this one?" is the *more basic* question and ranking was the wrong model to build a century of theory on.
- [electowiki's "Cardinal voting," claim-checked](cardinal_voting_claims_checked.md) — a 301 audit of the best short map of the score-ballot family: what to borrow, two logical errors to skip, and the article's own 51/49 argument run through the engine.
- [ABIF — the all-in-one ballot format](abif_format.md) — the election-methods **interchange** format that writes ranks *and* scores in one grammar (`Allie/5 =Billy/5 >Candace/4`), decoded and weighed honestly against this library's YAML grid.

## Related

- [Alternate ballot styles — one voter, three ballots](../topics/ballot_styles.md) — the same opinion marked on a ranking, Yes/No, and 0–5 ballot, side by side.
