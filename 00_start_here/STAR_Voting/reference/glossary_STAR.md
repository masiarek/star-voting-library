# Glossary — STAR Voting

Method-specific terms for **STAR** (Score Then Automatic Runoff). Shared, cross-method vocabulary (monotonicity, Condorcet, summability, the Equal Vote criterion, spoiler / vote-splitting…) lives in the [main glossary](../../GLOSSARY.md) — this page only defines what's specific to STAR.

- **STAR** — Score Then Automatic Runoff: score every candidate 0–5; the two highest totals advance to an automatic head-to-head runoff.
- **Scoring round** — STAR's first round: add up each candidate's scores; the top two become finalists. → concept [The Scoring Round](../the_count/STAR_Scoring_Round.md); demo [`equal_support_runoff_demo`](../../../01_STAR/_main/_main_pages/equal_support_runoff_demo.md)
- **Finalists** — the two highest-scoring candidates, who advance to the runoff. → the round that *chooses* them, [The Scoring Round](../the_count/STAR_Scoring_Round.md); the round they *compete* in, [The Automatic Runoff](../the_count/STAR_Automatic_Runoff.md).
- **Automatic runoff** — STAR's second round: each ballot counts as a full vote for whichever finalist it scored higher; the preferred finalist wins.
- **Equal Support** — scoring the two finalists the same; counts as "no preference" between them in the runoff (still fully counted in the scoring round). The aka is documented once in the [main glossary](../../GLOSSARY.md). → ["Aren't Equal-Score Votes Just Discounted?"](are_equal_score_votes_discounted.md)
- **Runoff Reversal** — the Scoring-Round leader **loses** the Automatic Runoff to the finalist more voters prefer (the *score* winner ≠ the *STAR* winner). Not a malfunction — the runoff elects the finalist preferred by the majority (of voters with a preference); the engine flags it with a `[Runoff Reversal]` block. House term: "the runoff overturns the score leader." → walkthrough [Runoff Reversal](../../../01_STAR/runoff_overturns_leader/)
- **Majority finish** — STAR's runoff guarantees the winner beats the runner-up among voters who expressed a preference between them.
- **Three notions of "winner"** — Condorcet / Score / Runoff can name three different candidates in one election; STAR targets the runoff winner by design. → [Three Notions of "Winner" — Condorcet, Score, and Runoff](../properties_and_limits/STAR_three_winner_notions.md)
- **Tiebreak ladder** — resolves ties in each round: Scoring Round *pairwise → five-star → lot*; Runoff *score → five-star → lot*. "Five-star" counts votes of the scale maximum. Full detail: [STAR Tie-Breaking — The Full Chain](../Tie_Breaking_STAR/tie_breaking.md).
- **Five-star rung** — the ladder's second step: "most votes of score **5** (the scale maximum)." It counts *only* 5s — it does **not** step down to 4s.
- **Dead rung** — the five-star rung when no tied candidate scored a 5 (e.g. all scores capped at 4): it reads `0–0`, separates nobody, and the tie **falls through to the lot**. Equal *non-zero* five-star counts do the same. Mnemonics: *"no fives, no rung — drop to the lot"* / *"it counts fives, not fours."* akas: broken / missing / empty / phantom rung. → cases [The "dead rung"](../../../01_STAR/tie_break_dead_rung/) · generator [`generate_dead_rung_scenarios.py`](../../../STARVote_LH_tabulation_engine/tools_adam/generate_dead_rung_scenarios.md)
- **Quorum** — an opt-in *turnout* threshold (`eligible_voters` + `quorum`): enough of the eligible electorate must participate or no winner is declared. → [Quorum — did enough of the electorate show up?](../../topics/quorum.md)
- **Bloc STAR** — multi-winner STAR electing the top N (at-large / majoritarian, **not** proportional). → [02_STAR_Bloc — Bloc STAR (multi-winner, majoritarian)](../../../02_STAR_Bloc/)
- **Proportional STAR** — multi-winner STAR variants (Allocated Score, Sequentially Spent Score, RRV) giving proportional representation. → [03_STAR_PR — proportional STAR (multi-winner)](../../../03_STAR_PR/)

*Shared criteria STAR is judged on — [monotonicity, Condorcet efficiency, summability, later-no-harm, the Equal Vote criterion](../../GLOSSARY.md#properties--criteria) — are in the [main glossary](../../GLOSSARY.md).*

# file: glossary_STAR.md
