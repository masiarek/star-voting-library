# Concepts — deep-dive pages for the important terms

**New here? Start with [Ballot & Terminology Basics](topics/ballot_and_terminology_basics.md)** — a short four-step reading path through the ideas people most often get wrong (terminology, scores vs. ranks, what counts as "ranked," and strict vs. weak ranks).

Not every glossary term needs its own page — most are fine as a one-liner in [Glossary — voting methods & criteria](GLOSSARY.md). This folder holds the handful of concepts that are **load-bearing in debates** and worth a focused page with a worked example and **links to the test-case YAMLs** that demonstrate them.

The pages are grouped to mirror the folders: **general / cross-method** ideas live in [`topics/`](topics/), IRV-specific problems live in [`RCV_IRV/`](RCV_IRV), and STAR's own properties live in [`STAR_Voting/`](STAR_Voting). The top level of this folder keeps only the entry points: the guided start, the curriculum, the glossary, and the authoring canon (TIPS, templates).

**Two ways to browse.** The authoritative pages are organized **by method** (below). Ideas that cut across methods live in [the topics folder](topics/) — flat concept pages plus thin per-topic hubs that link to each method's treatment of one idea (so you can browse by topic in the GitHub file tree, not just by method).

### General & cross-method

| Concept | One line |
|---------|----------|
| [**Ballot & terminology basics**](topics/ballot_and_terminology_basics.md) | the 4 ideas people most often get wrong — start here |
| [**Scores vs. ranks (don't confuse them!)**](scores_and_ranks/scores_vs_ranks.md) | order-only (ranks) vs. order+strength (scores) — relative vs. absolute preference |
| [**Scoring methods aren't RCV**](topics/scoring-methods-vs-ranked-voting.md) | scoring methods (Approval, STAR) rate candidates and sit *outside* the ranked-voting family |
| [**Approval — honest limits**](Approval_Voting/approval_honest_limits.md) | no preference strength/order, the approval-threshold dilemma, bullet-voting; balanced with its equal-vote simplicity |
| [**Strict vs. weak ranks**](scores_and_ranks/strict_vs_weak_ranks.md) | many ranked methods allow equal ranks & compare pairwise — RCV-IRV does neither |
| [**"Preference" (a slippery word)**](topics/preference.md) | everyday opinion vs. technical "ranking"; why "Preferential Voting" is a misnomer |
| [**Ranked Robin / RCV-RR (Consensus Voting; = Copeland)**](RCV_Ranked_Robin/ranked_robin.md) | a Condorcet method: ranks + equal ranks, every pair compared head-to-head; tabulable via the pref_voting engine |
| [**Ranked Robin (RCV-RR) — honest limits**](RCV_Ranked_Robin/RCV_RR_honest_limits.md) | Condorcet cycles need a resolution rule; no preference strength (bland-compromise winner); burial |
| [**Proportional Representation**](proportional_representation/) ([STV vs STAR-PR](proportional_representation/stv/proportional_stv_vs_star.md) · [STAR-PR methods](proportional_representation/STAR_PR/)) | multi-seat — coalitions get proportional seats; STV ≈ STAR-PR, Bloc differs (301) |
| [**Tabulation, step by step (201)**](topics/tabulation_star_vs_irv.md) | the same ballots counted both ways — STAR's 2 steps vs IRV's elimination rounds |
| [**RCV-IRV vs. STAR (side-by-side)**](topics/rcv_irv_vs_star.md) | balanced comparison hub — real strengths on both sides — routing to the facet pages |
| [**Tabulation engines — BV, LH, RCV-IRV**](tabulation_engines/bettervoting_and_the_engine.md) | why an election has two reports (BetterVoting's visual display + the LH engine's text report), how they map, and the convert→validate→test pipeline; hub for the per-engine folders |
| [**STAR Reporting — reading & comparing results**](STAR_reporting/) | how a result is reported: scores, runoff, percentages, Equal Support/abstentions; LH vs BetterVoting and where they differ; the Score Distribution and Preference Matrix up close |
| [**Quorum — did enough show up?**](topics/quorum.md) | a turnout threshold separate from who wins; abstentions count toward it; an unmet quorum means no winner — won the count but not elected |

### RCV-IRV — problems specific to instant-runoff

| Concept | One line |
|---------|----------|
| [**RCV is a confusing name**](RCV_IRV/RCV-IRV-confusing-name.md) | "RCV" is an umbrella for many ranked methods; in the US it usually means RCV-IRV (Hare) |
| [**Is IRV "just plurality"?**](RCV_IRV/RCV_IRV_and_plurality.md) | the defensible kernel (round-by-round first-choice elimination) vs. the overclaim |
| [**Is RCV "simple"? (201)**](RCV_IRV/RCV_IRV_is_simple.md) | ranking is simple to *mark*; IRV's *count* isn't |
| [**Center squeeze**](RCV_IRV/RCV_IRV_center_squeeze.md) | a broadly-liked moderate eliminated early under IRV; STAR avoids it |
| [**IRV non-monotonicity**](RCV_IRV/RCV_IRV_non_monotonicity.md) | under IRV, *more* first-choice support can make the winner **lose** |
| [**Exhausted ballots**](RCV_IRV/RCV_IRV_exhausted_ballots.md) | a validly-cast ranked ballot can stop counting; IRV's "majority" is of active ballots |
| [**IRV isn't summable**](RCV_IRV/RCV_IRV_lack_of_summability.md) | the winner depends on elimination order, so every ballot must be counted centrally |
| [**Fails the Equal Vote**](RCV_IRV/RCV_IRV_equal_vote.md) | opposite voters can't reliably cancel under sequential elimination — the equal-vote / spoiler failure (with an honest "is this fair?" caveat) |

### STAR Voting — STAR's properties & strengths

| Concept | One line |
|---------|----------|
| [**STAR's hybrid nature**](STAR_Voting/STAR_hybrid_nature.md) | expressive scoring to find the finalists + a majority runoff to pick the winner — the design the rest of these pages build on |
| [**The Automatic Runoff Round**](STAR_Voting/STAR_Automatic_Runoff.md) | STAR's second step, end to end — finalists, the For/Against/Equal Support counts, percentages, tie-breaking, and Runoff Reversal; the hub for all runoff topics |
| [**Runoff Reversal — top scorer ≠ winner**](../01_STAR/runoff_overturns_leader/) | the Scoring Round picks two finalists; the Automatic Runoff lets the *majority-preferred* finalist win — even with fewer total stars |
| [**The LH starvote engine**](tabulation_engines/LH_starvote/) | what the engine is (a thin fork + a thick reporting wrapper) and our improvements — the minimal **on-screen report** vs the always-full **`_tabulated`** mirror, the matrix/divergence/runoff-funnel reporting, and multi-method dispatch |
| [**Reading a STAR report (201)**](tabulation_engines/LH_starvote/reading_a_star_report.md) | the full engine report, section by section — matrix, divergence, both rounds, winner — and which parts to show 101 vs 201 vs 301 |
| [**Reading the runoff percentages**](STAR_Voting/runoff_percentages.md) | the same runoff vote shown two ways — % of all voters vs % of the voters *with a preference*; why the winner needs a majority of the decided voters, and where Equal Support goes |
| [**Three notions of "winner"**](STAR_Voting/STAR_three_winner_notions.md) | Condorcet vs Score vs Runoff can name three different candidates in one election |
| [**STAR is monotone**](STAR_Voting/STAR_monotonicity.md) | raising a candidate's score can never make them lose — the failure IRV has, STAR doesn't |
| [**STAR is summable**](STAR_Voting/STAR_summability.md) | tally by adding independent precinct totals; precinct-auditable, meaningful partials |
| [**Residual vote-splitting**](STAR_Voting/residual_vote_splitting.md) | STAR ends *forced* splitting; the narrow leftover is self-inflicted bullet-voting / the chicken dilemma |
| [**Equally Weighted Vote (Equal Vote Criterion)**](STAR_Voting/equally_weighted_vote.md) | every ballot has an exact opposite that cancels it (the Test of Balance) — why STAR fully ends *forced* vote-splitting; Choose-One and RCV-IRV fail it |
| [**STAR — honest limits**](STAR_Voting/STAR_honest_limits.md) | not Condorcet-compliant, not FBC-proof, gives up Later-No-Harm, residual splitting, strategic scoring — stated plainly |
| [**Tie-breaking — the full chain**](STAR_Voting/Tie_Breaking_STAR/tie_breaking.md) | ties fall through pairwise → five-star → lot order, in both rounds |
| [**Tie-breaking in BetterVoting JSON**](STAR_Voting/Tie_Breaking_STAR/tie_breaking_JSON.md) | how a BV export pre-draws the official lot order, and its YAML mapping |

Deeper conversation/debate scripts live beside their topics, indexed in [Conversation scripts — index](about_this_repo/conversation_scripts.md) (e.g. [Favorite Betrayal — Does *Only* RCV Avoid It?](STAR_Voting/favorite_betrayal_voting_301.md), ["Exhausted Ballots" — What FairVote's Word Actually Hides](RCV_IRV/exhausted_ballots_301.md)); these pages are the shorter, reference-style explainers the glossary links to. <!-- terminology-ok: bare RCV is inside linked page titles -->
