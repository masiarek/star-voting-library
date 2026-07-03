# Glossary — voting methods & criteria

One-line definitions for the keywords used across these lessons — STAR and every
method it's compared against. Grouped from beginner vocabulary to advanced theory.
Most entries end with **→** quick jumps to the demo election's page (ballots +
results) and/or the interview episode that show the term in action.

> **Why one glossary?** Most of the vocabulary below — monotonicity, Condorcet,
> summability, center squeeze, vote-splitting, the Equal Vote criterion — is the
> *shared* language used to *compare* methods, so it doesn't belong to any single
> method. Method-specific terms are grouped by method (STAR mechanics; Other
> methods) with stable anchors, so a method page can deep-link to just its slice.

## Per-method glossaries

Method-specific terms also live next to each method, cross-referencing the shared
vocabulary here:

- [**STAR**](STAR_Voting/glossary_STAR.md) — scoring round, finalists, automatic runoff, Equal Support, runoff reversal, Bloc / Proportional STAR
- [**Approval**](Approval_Voting/glossary_approval.md) — the approval line, double-bubble, SPAV/PAV
- [**Range / Score**](Range_Voting/glossary_range.md) — total-score win, exaggeration strategy, scale granularity
- [**Ranked Robin & Condorcet**](RCV_Ranked_Robin/glossary_ranked_robin.md) — Copeland, cycles, Ranked Pairs / Schulze / Minimax
- [**RCV-IRV**](RCV_IRV/glossary_rcv_irv.md) — IRV, exhausted ballots, center squeeze, STV, Hare

The **shared** criteria (monotonicity, Condorcet, summability, center squeeze, the
Equal Vote criterion, spoiler / vote-splitting…) stay below — they're the language
for *comparing* methods, so they belong to no single one.

## Core vocabulary

- **STAR** — Score Then Automatic Runoff: score every candidate 0–5; the two highest totals advance to an automatic head-to-head runoff. → episode [`whats_so_good_about_STAR_Voting.md`](../interviews_conversations/whats_so_good_about_STAR_Voting.md)
- **Score / star rating** — a 0–5 value expressing *how much* you support a candidate (like a five-star review).
- **Scoring round** — STAR's first round: add up each candidate's scores; the top two become finalists. → demo [`equal_support_runoff_demo`](../01_STAR/_main/_main_pages/equal_support_runoff_demo.md)
- **Finalists** — the two highest-scoring candidates, who advance to the runoff.
- **Automatic runoff** — STAR's second round: each ballot counts as a full vote for whichever finalist it scored higher; the preferred finalist wins. (Deep-dive deck: **Automatic Runoff** — see [`LINKS.md`](../interviews_conversations/LINKS.md).) → demo [`equal_support_runoff_demo`](../01_STAR/_main/_main_pages/equal_support_runoff_demo.md); episode [`are_equal_score_votes_discounted.md`](../interviews_conversations/are_equal_score_votes_discounted.md)
- **Head-to-head / pairwise** — a direct comparison of two candidates: which one more ballots scored higher.
- **Equal Support / Equal Preference** — scoring two candidates the same; counts as "no preference" between them in the runoff. Covers two honest cases — scored both finalists high ("loved both") or both low ("neither") — both still counted in the scoring round. → episode [`are_equal_score_votes_discounted.md`](../interviews_conversations/are_equal_score_votes_discounted.md) → demo [`equal_support_runoff_demo`](../01_STAR/_main/_main_pages/equal_support_runoff_demo.md); episode [`are_equal_score_votes_discounted.md`](../interviews_conversations/are_equal_score_votes_discounted.md)
- **Scored (cardinal) ballot** — rates each candidate independently 0–5; equal ratings allowed. The ballot behind the **scored family** (Approval → Range → STAR). → concept [`scores_vs_ranks.md`](scores_and_ranks/scores_vs_ranks.md); the score↔rank conversion is the [`fidelity_ladder.md`](scores_and_ranks/fidelity_ladder.md)
- **Ranked (ordinal) ballot** — orders candidates 1st, 2nd, 3rd; conveys *order* but not *degree* of support. **One ballot, several tabulations** — RCV-IRV, Ranked Robin (Condorcet), STV — so it's shared ballot-family vocabulary, kept here rather than folded into any one method. Whether equal ranks are allowed distinguishes **strict vs weak** ranks: [`strict_vs_weak_ranks.md`](scores_and_ranks/strict_vs_weak_ranks.md). → concept [`scores_vs_ranks.md`](scores_and_ranks/scores_vs_ranks.md); per-method [`glossary_rcv_irv.md`](RCV_IRV/glossary_rcv_irv.md) and [`glossary_ranked_robin.md`](RCV_Ranked_Robin/glossary_ranked_robin.md)

## The problem STAR addresses

- **Choose-One / Plurality / First-Past-The-Post** — vote for exactly one candidate; most votes wins. Accurate only with two candidates. → episode [`our_voting_system_is_broken.md`](../interviews_conversations/our_voting_system_is_broken.md)
- **Vote splitting** — similar candidates divide their shared supporters, letting a less-preferred candidate win. → demos [`split_voting/`](../method_comparisons/split_voting); episode [`our_voting_system_is_broken.md`](../interviews_conversations/our_voting_system_is_broken.md)
- **Spoiler effect** — a candidate who cannot win still changes who does, by splitting another's support. → demo [`04_star_wars_vote_split`](../method_comparisons/split_voting/_main/_main_pages/04_star_wars_vote_split.md); episode [`whats_so_good_about_STAR_Voting.md`](../interviews_conversations/whats_so_good_about_STAR_Voting.md) (Seg 1)
- **Favorite betrayal** — being pressured to score/rank a front-runner above your true favorite. → episode [`favorite_betrayal_voting_301.md`](../interviews_conversations/favorite_betrayal_voting_301.md)
- **Lesser-evil voting** — backing a tolerable front-runner instead of your favorite to block a worse outcome. → episode [`our_voting_system_is_broken.md`](../interviews_conversations/our_voting_system_is_broken.md)
- **Wasted vote** — a vote that has no effect on the result.
- **Two-round system** — separate primary + general/runoff elections; STAR does both jobs on one ballot.
- **Plurality / minority winner** — a winner with the most votes but less than majority support. → episode [`our_voting_system_is_broken.md`](../interviews_conversations/our_voting_system_is_broken.md)

## Mechanics

- **Equal scores allowed** — you may give two candidates the same score; you're never forced to invent a preference. → demo [`03a_c3_b3_style-bullet-vote`](../01_STAR/_main/_main_pages/03a_c3_b3_style-bullet-vote.md)
- **Exhausted ballot** — (an **RCV-IRV** term; IRV-specific, *not* all ranked methods — Ranked Robin / Condorcet counts read every rank) a ballot set aside mid-count because all its ranked candidates were eliminated. FairVote's single word covers several very different cases (voter-side vs method-caused); STAR's runoff never eliminates anyone, so it doesn't discard ballots this way. → episode [`exhausted_ballots_301.md`](../interviews_conversations/exhausted_ballots_301.md)
- **Tiebreaker** — a rule that resolves ties (for the finalists or the runoff); here, candidate priority / lot order. The full ladder (pairwise → five-star → lot, in both rounds), plus what BetterVoting JSON carries and what you may set in a hand-written YAML, is in [`tie_breaking.md`](STAR_Voting/Tie_Breaking_STAR/tie_breaking.md).
- **Undervote / abstention** — a ballot that scores no one (blank or `~`); counts as turnout but supports no candidate. It stays in the **quorum** numerator (still participated) but drops out of the runoff percentage (no preference). → [`quorum.md`](quorum.md)
- **Quorum** — a *turnout* threshold (separate from who wins): enough of the **eligible electorate** must participate or no winner is declared. Opt-in via `eligible_voters` + `quorum`; default is a majority (>50%) of eligible voters; participation includes abstentions. → page [`quorum.md`](quorum.md); demo [`quorum_demo_c3_b6`](../01_STAR/_main/_main_pages/quorum_demo_c3_b6.md)

## Properties & criteria

- **Majority finish** — STAR's runoff guarantees the winner beats the runner-up among voters who expressed a preference between them. → demo [`06b_c9_runoff-overturns-leader`](../01_STAR/_main/_main_pages/06b_c9_runoff-overturns-leader.md) (runoff overturns the score leader); full walkthrough [`runoff_overturns_leader/`](../01_STAR/runoff_overturns_leader/README_runoff_overturns_leader.md) (why the top-scoring candidate isn't always the winner, as a 3→9-candidate progression)
- **Runoff Reversal** — the STAR outcome where the **Scoring-Round leader loses the Automatic Runoff** to the finalist more voters prefer (the *score* winner ≠ the *STAR* winner). Not a malfunction — the runoff is enforcing majority preference between the two finalists. The plain-language house term is "the runoff overturns the score leader." → walkthrough [`runoff_overturns_leader/`](../01_STAR/runoff_overturns_leader/README_runoff_overturns_leader.md)
- **Three notions of "winner"** — Condorcet (beats all head-to-head), Score (most total stars), and Runoff (majority pick between finalists) can name three *different* candidates in one election; STAR targets the runoff winner by design. → page [`STAR_three_winner_notions.md`](STAR_Voting/STAR_three_winner_notions.md); demo [`three_winners_cw_score_runoff`](../01_STAR/_main/_main_pages/three_winners_cw_score_runoff.md)
- **Condorcet winner** — the candidate who beats every other head-to-head; STAR usually (not always) elects them. → demo [`equal_support_runoff_demo`](../01_STAR/_main/_main_pages/equal_support_runoff_demo.md) (`show_condorcet`)
- **Condorcet efficiency** — how often a method elects the Condorcet winner (STAR's is very high).
- **Condorcet loser** — the candidate who loses every head-to-head.
- **Condorcet compliance** — *always* electing the Condorcet winner; STAR is **not** compliant (a deliberate tradeoff).
- **Center squeeze** — a broadly-liked moderate eliminated early for lacking first-choice support; an RCV-IRV failure STAR avoids. *(aka **"core collapse"** — one author's ([elsim](https://github.com/endolith/elsim/blob/collapse_2d/examples/README.md)) label for the extreme case where successive elimination returns the **next-worst** candidate; noted by Nanson, 1882. Non-standard coinage — a vivid name for worst-case center squeeze, **not** a separate phenomenon.)* → page [`RCV_IRV_center_squeeze.md`](RCV_IRV/RCV_IRV_center_squeeze.md); demos: RCV-IRV [`squeeze`](../method_comparisons/center_squeeze/center_squeeze_pages/center_squeeze_irv.md) / STAR [`fix`](../method_comparisons/center_squeeze/center_squeeze_pages/center_squeeze_star.md)
- **Later-no-harm** — adding a lower preference never hurts your top choice; RCV-IRV has it, STAR intentionally does not. → episode [`favorite_betrayal_voting_301.md`](../interviews_conversations/favorite_betrayal_voting_301.md)
- **Equal Vote Criterion / Equally Weighted Vote** — every ballot must have an equal-and-opposite ballot that cancels it (the *Test of Balance*, Mark Frohnmayer). STAR, Score, and Approval pass; Choose-One and RCV-IRV fail — the structural root of vote-splitting. → pages [`equally_weighted_vote.md`](STAR_Voting/equally_weighted_vote.md) (STAR passes) / [`RCV_IRV_equal_vote.md`](RCV_IRV/RCV_IRV_equal_vote.md) (RCV-IRV fails, stated fairly)
- **Monotonicity** — raising a candidate on your ballot never causes them to lose (and vice versa). → page [`RCV_IRV_non_monotonicity.md`](RCV_IRV/RCV_IRV_non_monotonicity.md); demos: RCV-IRV [`before`](../method_comparisons/monotonicity/monotonicity_pages/monotonicity_irv_before.md)/[`after`](../method_comparisons/monotonicity/monotonicity_pages/monotonicity_irv_after.md) (X loses), STAR [`before`](../method_comparisons/monotonicity/monotonicity_pages/monotonicity_star_before.md)/[`after`](../method_comparisons/monotonicity/monotonicity_pages/monotonicity_star_after.md) (X holds)
- **Participation criterion** — voting honestly never yields a worse result than not voting.
- **Favorite-betrayal criterion** — you never gain by scoring someone above your favorite. → episode [`favorite_betrayal_voting_301.md`](../interviews_conversations/favorite_betrayal_voting_301.md)
- **Summability / precinct-summable** — results can be computed by adding independent precinct totals (STAR can; RCV-IRV cannot). → page [`STAR_summability.md`](STAR_Voting/STAR_summability.md); demo [`04b_c4_b3_display-options-all`](../01_STAR/_main/_main_pages/04b_c4_b3_display-options-all.md)
- **Pairwise (For / Equal / Against) matrix** — the summable head-to-head table the runoff and audits use. → demo [`04b_c4_b3_display-options-all`](../01_STAR/_main/_main_pages/04b_c4_b3_display-options-all.md) (`show_matrix`)
- **Strategyproofness** — no voter can ever gain by voting insincerely; impossible for any method (Gibbard).
- **Gibbard / Gibbard–Satterthwaite theorems** — proofs that every reasonable voting method is manipulable.
- **Strategy resistance** — how rarely and riskily strategy pays; STAR is resistant, not proof.
- **Equal Vote / Test of Balance** — any support a ballot expresses can be exactly cancelled by an opposite ballot; STAR's precise sense of equal weight.
- **One-person-one-vote** — equal voting weight. (Caution: the constitutional OPOV doctrine governs district population, not ballot expressiveness.)
- **Utilitarian vs majoritarian** — maximizing total support vs guaranteeing a majority; STAR blends both.

## Other methods (for contrast)

- **Approval voting** — score each candidate 0 or 1 (approve / not); most approvals wins. → demo [`approval_101_c3_b5`](../04_Approval/_main/_main_pages/approval_101_c3_b5.md) (0/1 marks are also legal on a STAR ballot — [`star_ala_approval`](../01_STAR/_main/_main_pages/star_ala_approval.md))
- **Score voting (pure)** — score 0–5; highest total/average wins, with no runoff (more manipulable than STAR).
- **RCV (Ranked-Choice Voting)** — a ranked *ballot* type (rank candidates 1st, 2nd, 3rd). A **family**, not one method; in the US it's commonly (loosely) used to mean IRV specifically. → [`TIPS_terminology.md`](TIPS_terminology.md); episode [`RCV_or_IRV_whats_the_right_word.md`](../interviews_conversations/RCV_or_IRV_whats_the_right_word.md)
- **IRV (Instant-Runoff Voting)** — *one tabulation* of a ranked ballot: eliminate the lowest, transfer, repeat until a majority. The single-winner method usually meant by "RCV."
- **RCV-IRV** — disambiguating label for "the RCV that is IRV"; preferred in this repo for STAR-vs-method comparisons so it's clear we mean the eliminate-and-transfer method, not the ballot family. → [`TIPS_terminology.md`](TIPS_terminology.md); episodes [`RCV_or_IRV_whats_the_right_word.md`](../interviews_conversations/RCV_or_IRV_whats_the_right_word.md), [`exhausted_ballots_301.md`](../interviews_conversations/exhausted_ballots_301.md)
- **Ranked Robin (RCV-RR / "Consensus")** — a Condorcet tabulation of the *same* ranked ballot (most head-to-head wins, Copeland-style). Has no center squeeze; do not lump it with IRV.
- **STV (Single Transferable Vote)** — the proportional, multi-winner tabulation of ranked ballots (the proportional cousin of IRV, not IRV itself). → demo [`03a_stv_3seats`](../other_methods/_main/_main_pages/03a_stv_3seats.md); page [`proportional_representation/stv/proportional_stv_vs_star.md`](proportional_representation/stv/proportional_stv_vs_star.md)
- **Condorcet method** — any ranked method that *always* elects the candidate who beats every other head-to-head (the Condorcet winner) when one exists. A **family**: Ranked Robin, Ranked Pairs, Schulze, Minimax, Copeland. → family tree in [`TIPS_terminology.md`](TIPS_terminology.md)
- **Ranked Pairs (Tideman)** — a Condorcet method: lock in the strongest pairwise victories first, skipping any that would create a cycle.
- **Schulze (beatpath)** — a Condorcet method that decides via the strongest "beatpaths" between candidates.
- **Minimax (Simpson–Kramer)** — a Condorcet method electing the candidate whose *worst* pairwise loss is the smallest.
- **Borda** — a positional ranked method (points by rank position). A ranked method but **not** Condorcet-compliant.
- **Bucklin (Grand Junction)** — a ranked, median-style method (add lower ranks until someone has a majority). Ranked but **not** Condorcet. (Spelled *Bucklin*, not "Buckling".)
- **Hare** — historically the ranked-transfer idea; single-winner = **IRV**, multi-winner = **STV** (Hare quota).
- **ballot vs tabulation** — the ballot is *what the voter marks* (ranked, or scored); the tabulation is *how it's counted* (IRV / Ranked Robin / STV for ranked; STAR / Approval / Score for scored). "RCV" names a ballot; "IRV" names a tabulation. → [`TIPS_terminology.md`](TIPS_terminology.md); episode [`RCV_or_IRV_whats_the_right_word.md`](../interviews_conversations/RCV_or_IRV_whats_the_right_word.md)
- **Bloc STAR** — multi-winner STAR that elects the top N candidates (at-large / majoritarian — *not* proportional). → demo [`01_c4_b2_bloc-star-2-seats`](../02_STAR_Bloc/_main/_main_pages/01_c4_b2_bloc-star-2-seats.md); majoritarian-vs-proportional contrast in [`proportional_representation/stv/proportional_stv_vs_star.md`](proportional_representation/stv/proportional_stv_vs_star.md); [`CURRICULUM.md`](CURRICULUM.md) (201.5)
- **Proportional STAR** — multi-winner methods (Reweighted Range Voting, Allocated Score, Sequentially Spent Score) that give proportional representation. → demo [`03b_star_pr_3seats`](../03_STAR_PR/_main/_main_pages/03b_star_pr_3seats.md); page [`proportional_representation/stv/proportional_stv_vs_star.md`](proportional_representation/stv/proportional_stv_vs_star.md) (STV vs STAR-PR); [`CURRICULUM.md`](CURRICULUM.md) (301.1)

## Civic / adoption

- **[Equal Vote Coalition](https://equal.vote)** — the organization that developed and advocates STAR Voting.
- **[BetterVoting.com](https://bettervoting.com)** — site to try a STAR ballot and run your own elections. The visual result it shows is one of two reports of an election in this repo — the other is the LH engine's text report; how they relate is [BetterVoting and the LH engine](tabulation_engines/bettervoting_and_the_engine.md).
- **LH engine (`starvote`)** — Larry Hastings' STAR tabulator (this repo's fork), which prints the full text audit report and the generated `_tabulated.txt` copies; handles the score methods (STAR, Bloc / Proportional STAR, Approval). Ranked ballots go to a separate vendored **RCV-IRV** engine (pyrankvote). Upstream: [GitHub](https://github.com/larryhastings/starvote) · [PyPI](https://pypi.org/project/starvote/). See [BetterVoting and the LH engine](tabulation_engines/bettervoting_and_the_engine.md).

---

See also: [00_START_HERE.md](00_START_HERE.md) (teaching sequence) ·
[Why_STAR_Voting.md](Why_STAR_Voting.md) (presentation + debate prep) ·
[CURRICULUM.md](CURRICULUM.md) (lesson outline).
