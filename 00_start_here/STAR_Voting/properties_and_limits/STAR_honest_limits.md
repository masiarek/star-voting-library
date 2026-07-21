# STAR Voting — Honest Limits

**One line:** STAR is strong but **not perfect**. It is not Condorcet-compliant, not favorite-betrayal-proof, gives up Later-No-Harm by design, can fail the strict Majority Criterion (favoring a broad-consensus winner over a polarizing majority-favorite), leaves a narrow residual of vote-splitting, and — like *every* method ([Gibbard](../../topics/gibbard_satterthwaite_theorem.md)) — can be gamed at the margins. None of these are secret; conceding them honestly is why the rest of the case is trustworthy.

→ **The checklist with receipts:** [Every voting criterion STAR fails](star_criteria_failures.md) — a table of each criterion, a runnable example, and its `.yaml` / BV id / `_bv_export.json`. (This page is the *prose* — the why; that page is the *index* — the where.)

→ Companion critical pages so every method gets the same treatment: [Approval's limits](../../Approval_Voting/approval_honest_limits.md) · [Ranked Robin (RCV-RR) limits](../../RCV_Ranked_Robin/RCV_RR_honest_limits.md) · [RCV-IRV fails the Equal Vote](../../RCV_IRV/RCV_IRV_equal_vote.md). Curriculum: [301.4 — honest limits](../../CURRICULUM.md).

---

## 1. Not Condorcet-compliant

STAR can fail to elect the **[Condorcet winner](../../topics/condorcet/)** (the candidate who beats every other one head-to-head). Its runoff is between the *top two by score*, and the Condorcet winner can be a close third on score and never reach the runoff. **How much it matters:** simulations put STAR's Condorcet-efficiency very high, and when it diverges the STAR winner is someone with very broad support who lost one pairing narrowly. It's a **tradeoff**, not a clean loss — Condorcet methods buy compliance by sometimes electing a weakly-supported compromise nobody is enthusiastic about. See [three notions of "winner"](STAR_three_winner_notions.md). A sharper, mechanical instance: when the electorate has a genuine Condorcet **cycle** (no Condorcet winner at all), STAR's runoff is even **[IIA](../../topics/what_makes_a_voting_method_good.md)-sensitive** — a candidate who cannot win can flip the result by changing which two candidates reach the runoff. Worked, BV-backed, on fully sincere ballots: [the cycle spoiler](../../../01_STAR/iia_cycle_spoiler/bv2212_g3f7r2_cycle_spoiler.md).

## 2. Not favorite-betrayal-proof (rare)

STAR does **not** satisfy the Favorite-Betrayal Criterion: in rare, knife-edge constructions a voter can do better by scoring a front-runner above their true favorite. **How much it matters:** it takes precise knowledge and coordination, and honest scoring is almost always the best strategy — but "eliminates favorite betrayal" would be an overclaim. Neither STAR nor RCV-IRV is FBC-proof (they fail it in different ways). See [favorite betrayal](favorite_betrayal_voting_301.md).

## 3. Gives up Later-No-Harm (by design)

Scoring your second choice can help that candidate **beat your favorite** in the runoff. This is a genuine tradeoff, not an oversight: Later-No-Harm and the Favorite-Betrayal Criterion are provably incompatible with other things we want, so STAR deliberately keeps favorite-betrayal resistance and gives up Later-No-Harm. RCV-IRV makes the opposite choice.

## 4. Residual vote-splitting / the chicken dilemma

STAR ends *forced* vote-splitting, but a **narrow, self-inflicted** residue remains: two allied candidates' supporters can bullet-vote against each other (the "chicken dilemma"). **How much it matters:** it's hard to coordinate and usually self-defeating, far smaller than Choose-One's structural splitting — but non-zero. Full treatment: [residual vote-splitting](residual_vote_splitting.md).

## 5. Strategic scoring / normalization

The 0–5 ballot invites **[min-maxing](../../topics/strategic_voting.md)** — giving 5s and 0s rather than honest intermediate scores — because an exaggerated ballot can carry more weight in the scoring round. STAR's automatic runoff dampens this (your honest order still decides the final round), but doesn't erase it. Gibbard's theorem guarantees **no** method with 3+ candidates is fully strategy-proof; STAR aims for *resistant, not proof*.

## 6. The ballot has a learning curve

A 0–5 grid is more to explain than "pick one," and some voters under-use the scale (only 0s and 5s), losing expressiveness. It's still a familiar five-star pattern, but it is more cognitive load than plurality and a legitimate adoption hurdle.

## 7. Tie-breaking is more machinery

Resolving ties runs a chain (pairwise → most five-star scores → lot), which is more moving parts than "most votes wins." Rare in large electorates, but real complexity to specify and explain. See [tie-breaking](../Tie_Breaking_STAR/).

## 8. Fails the (strict) Majority Criterion

STAR can fail to elect a candidate that an outright **majority scored highest**. This is the objection FairVote raises most often. It happens only in a specific shape: the majority's favorite is **polarizing** (a significant minority scores them near-zero), while a rival is scored highly by *nearly everyone* — so the broadly-liked rival outscores the polarizing favorite (or beats them in the runoff), and the majority-favorite can even miss the top-two entirely. **How much it matters:** this is really the same mechanism as limit #1 — the runoff is between the *top two by score*, so a divisive majority-favorite can lose to a consensus candidate. STAR's designers consider that the *right* outcome (a candidate 40% of voters reject is a weaker representative than one almost everyone likes), but "the majority always wins" is a genuinely intuitive rule that STAR does **not** guarantee, so it's an honest concession, not a bug.

**The defenders' reply.** Equal Vote argues the *strict* criterion over-weights a bare 50.1%-first-choice while ignoring how strongly the other half feels, and proposes a weaker **[Relaxed Majority Criterion](https://www.equal.vote/rmc)** — which STAR *does* satisfy, because its automatic runoff guarantees the winner is the majority-preferred of the two finalists. Whether the strict or relaxed version is the better yardstick is a value judgment, not a settled fact — and the strict criterion is provably incompatible with some other desirable properties, so *some* method must fail it. Full plain-language explainer (with the two-tiny-elections demo, the RMC definition, the Later-No-Harm link, and references): the **[Majority Criterion topic hub](../../topics/majority_criterion/README.md)**. Worked demonstration of the polarizing-favorite-vs-consensus case: the [Black Curtain set](../../../method_comparisons/black_curtain/README.md) (esp. "a polarizing winner" and "a hidden consensus"). Comparison context: [RCV-IRV vs STAR](../../topics/rcv_irv_vs_star.md).

## Keep it in perspective

Every method trades something away — that's [Arrow](../../topics/what_makes_a_good_winner.md) and Gibbard, not a STAR-specific flaw. The honest comparison is *which* tradeoffs, and how often they bite. STAR's limits are mostly rare edge cases or deliberate, well-motivated choices; its opponents' (and peers') limits are laid out just as plainly on the companion pages above, so you can judge the whole board rather than one square.
