# Glossary — STAR Voting

Method-specific terms for **STAR** (Score Then Automatic Runoff). Shared,
cross-method vocabulary (monotonicity, Condorcet, summability, the Equal Vote
criterion, spoiler / vote-splitting…) lives in the
[main glossary](../GLOSSARY.md) — this page only defines what's specific to STAR.

- **STAR** — Score Then Automatic Runoff: score every candidate 0–5; the two
  highest totals advance to an automatic head-to-head runoff.
- **Scoring round** — STAR's first round: add up each candidate's scores; the top
  two become finalists. → concept [`STAR_Scoring_Round.md`](STAR_Scoring_Round.md); demo [`equal_support_runoff_demo`](../../01_STAR/_main/_main_pages/equal_support_runoff_demo.md)
- **Finalists** — the two highest-scoring candidates, who advance to the runoff.
- **Automatic runoff** — STAR's second round: each ballot counts as a full vote
  for whichever finalist it scored higher; the preferred finalist wins.
- **Equal Support** — scoring the two finalists the same; counts as "no preference"
  between them in the runoff (still fully counted in the scoring round). The aka is
  documented once in the [main glossary](../GLOSSARY.md).
  → [`are_equal_score_votes_discounted.md`](are_equal_score_votes_discounted.md)
- **Runoff Reversal** — the Scoring-Round leader **loses** the Automatic Runoff to
  the finalist more voters prefer (the *score* winner ≠ the *STAR* winner). Not a
  malfunction — the runoff enforces majority preference. House term: "the runoff
  overturns the score leader." → walkthrough [Runoff Reversal](../../01_STAR/runoff_overturns_leader/)
- **Majority finish** — STAR's runoff guarantees the winner beats the runner-up
  among voters who expressed a preference between them.
- **Three notions of "winner"** — Condorcet / Score / Runoff can name three
  different candidates in one election; STAR targets the runoff winner by design.
  → [`STAR_three_winner_notions.md`](STAR_three_winner_notions.md)
- **Tiebreak ladder** — resolves ties in each round: Scoring Round *pairwise →
  five-star → lot*; Runoff *score → five-star → lot*. "Five-star" counts votes of
  the scale maximum. Full detail: [`Tie_Breaking_STAR/tie_breaking.md`](Tie_Breaking_STAR/tie_breaking.md).
- **Quorum** — an opt-in *turnout* threshold (`eligible_voters` + `quorum`):
  enough of the eligible electorate must participate or no winner is declared.
  → [`../quorum.md`](../quorum.md)
- **Bloc STAR** — multi-winner STAR electing the top N (at-large / majoritarian,
  **not** proportional). → [`02_STAR_Bloc/`](../../02_STAR_Bloc/)
- **Proportional STAR** — multi-winner STAR variants (Allocated Score, Sequentially
  Spent Score, RRV) giving proportional representation. → [`03_STAR_PR/`](../../03_STAR_PR/)

*Shared criteria STAR is judged on — [monotonicity, Condorcet efficiency,
summability, later-no-harm, the Equal Vote criterion](../GLOSSARY.md#properties--criteria)
— are in the [main glossary](../GLOSSARY.md).*

# file: glossary_STAR.md
