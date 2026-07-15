# Concepts — deep-dive pages for the important terms

**New here? Start with [Ballot & Terminology Basics](topics/ballot_and_terminology_basics.md)** — a short four-step reading path through the ideas people most often get wrong (terminology, scores vs. ranks, what counts as "ranked," and strict vs. weak ranks).

Not every glossary term needs its own page — most are fine as a one-liner in [Glossary — voting methods & criteria](GLOSSARY.md). This folder holds the handful of concepts that are **load-bearing in debates** and worth a focused page with a worked example and **links to the test-case YAMLs** that demonstrate them.

The pages are grouped to mirror the folders: **general / cross-method** ideas live in [`topics/`](topics/), IRV-specific problems live in [`RCV_IRV/`](RCV_IRV), and STAR's own properties live in [`STAR_Voting/`](STAR_Voting). The top level of this folder keeps only the entry points: the guided start, the curriculum, the glossary, and the authoring canon (TIPS, templates).

**Two ways to browse.** The authoritative pages are organized **by method** (below). Ideas that cut across methods live in [the topics folder](topics/) — flat concept pages plus thin per-topic hubs that link to each method's treatment of one idea (so you can browse by topic in the GitHub file tree, not just by method).

### General & cross-method

| Concept | One line | Page |
|---------|----------|------|
| **Ballot & terminology basics** | the 4 ideas people most often get wrong — start here | [Ballot & terminology basics](topics/ballot_and_terminology_basics.md) |
| **Scores vs. ranks (don't confuse them!)** | order-only (ranks) vs. order+strength (scores) — relative vs. absolute preference | [Scores vs. ranks](scores_and_ranks/scores_vs_ranks.md) |
| **Scoring methods aren't RCV** | scoring methods (Approval, STAR) rate candidates and sit *outside* the ranked-voting family | [Scoring methods aren't RCV](topics/scoring-methods-vs-ranked-voting.md) |
| **Approval — honest limits** | no preference strength/order, the approval-threshold dilemma, bullet-voting; balanced with its equal-vote simplicity | [Approval — honest limits](Approval_Voting/approval_honest_limits.md) |
| **Strict vs. weak ranks** | many ranked methods allow equal ranks & compare pairwise — RCV-IRV does neither | [Strict vs. weak ranks](scores_and_ranks/strict_vs_weak_ranks.md) |
| **"Preference" (a slippery word)** | everyday opinion vs. technical "ranking"; why "Preferential Voting" is a misnomer | ["Preference" — a slippery word](topics/preference.md) |
| **Ranked Robin / RCV-RR (Consensus Voting; = Copeland)** | a Condorcet method: ranks + equal ranks, every pair compared head-to-head; tabulable via the pref_voting engine | [Ranked Robin / RCV-RR](RCV_Ranked_Robin/ranked_robin.md) |
| **Ranked Robin (RCV-RR) — honest limits** | Condorcet cycles need a resolution rule; no preference strength (bland-compromise winner); burial | [Ranked Robin — honest limits](RCV_Ranked_Robin/RCV_RR_honest_limits.md) |
| **Proportional Representation** | multi-seat — coalitions get proportional seats; STV ≈ STAR-PR, Bloc differs (301) | [Proportional representation](proportional_representation/) ([STV vs STAR-PR](proportional_representation/stv/proportional_stv_vs_star.md) · [STAR-PR methods](proportional_representation/STAR_PR/)) |
| **Tabulation, step by step (201)** | the same ballots counted both ways — STAR's 2 steps vs IRV's elimination rounds | [Tabulation, step by step](topics/tabulation_star_vs_irv.md) |
| **RCV-IRV vs. STAR (side-by-side)** | balanced comparison hub — real strengths on both sides — routing to the facet pages | [RCV-IRV vs. STAR](topics/rcv_irv_vs_star.md) |
| **Tabulation engines — BV, LH, RCV-IRV** | why an election has two reports (BetterVoting's visual display + the LH engine's text report), how they map, and the convert→validate→test pipeline; hub for the per-engine folders | [Tabulation engines](tabulation_engines/bettervoting_and_the_engine.md) |
| **STAR Reporting — reading & comparing results** | how a result is reported: scores, runoff, percentages, Equal Support/abstentions; LH vs BetterVoting and where they differ; the Score Distribution and Preference Matrix up close | [STAR reporting](STAR_reporting/) |
| **Quorum — did enough show up?** | a turnout threshold separate from who wins; abstentions count toward it; an unmet quorum means no winner — won the count but not elected | [Quorum](topics/quorum.md) |

### RCV-IRV — problems specific to instant-runoff

| Concept | One line | Page |
|---------|----------|------|
| **RCV is a confusing name** | "RCV" is an umbrella for many ranked methods; in the US it usually means RCV-IRV (Hare) | [RCV is a confusing name](RCV_IRV/RCV-IRV-confusing-name.md) |
| **Is IRV "just plurality"?** | the defensible kernel (round-by-round first-choice elimination) vs. the overclaim | [Is IRV "just plurality"?](RCV_IRV/RCV_IRV_and_plurality.md) |
| **Is RCV "simple"? (201)** | ranking is simple to *mark*; IRV's *count* isn't | [Is RCV "simple"?](RCV_IRV/RCV_IRV_is_simple.md) |
| **Center squeeze** | a broadly-liked moderate eliminated early under IRV; STAR avoids it | [Center squeeze](RCV_IRV/RCV_IRV_center_squeeze.md) |
| **IRV non-monotonicity** | under IRV, *more* first-choice support can make the winner **lose** | [IRV non-monotonicity](RCV_IRV/RCV_IRV_non_monotonicity.md) |
| **Exhausted ballots** | a validly-cast ranked ballot can stop counting; IRV's "majority" is of active ballots | [Exhausted ballots](RCV_IRV/RCV_IRV_exhausted_ballots.md) |
| **IRV isn't summable** | the winner depends on elimination order, so every ballot must be counted centrally | [IRV isn't summable](RCV_IRV/RCV_IRV_lack_of_summability.md) |
| **Fails the Equal Vote** | opposite voters can't reliably cancel under sequential elimination — the equal-vote / spoiler failure (with an honest "is this fair?" caveat) | [Fails the Equal Vote](RCV_IRV/RCV_IRV_equal_vote.md) |

### STAR Voting — STAR's properties & strengths

| Concept | One line | Page |
|---------|----------|------|
| **STAR's hybrid nature** | expressive scoring to find the finalists + a majority runoff to pick the winner — the design the rest of these pages build on | [STAR's hybrid nature](STAR_Voting/STAR_hybrid_nature.md) |
| **The Automatic Runoff Round** | STAR's second step, end to end — finalists, the For/Against/Equal Support counts, percentages, tie-breaking, and Runoff Reversal; the hub for all runoff topics | [The Automatic Runoff Round](STAR_Voting/STAR_Automatic_Runoff.md) |
| **Runoff Reversal — top scorer ≠ winner** | the Scoring Round picks two finalists; the Automatic Runoff lets the *majority-preferred* finalist win — even with fewer total stars | [Runoff Reversal](../01_STAR/runoff_overturns_leader/) |
| **The LH starvote engine** | what the engine is (a thin fork + a thick reporting wrapper) and our improvements — the minimal **on-screen report** vs the always-full **`_tabulated`** mirror, the matrix/divergence/runoff-funnel reporting, and multi-method dispatch | [The LH starvote engine](tabulation_engines/LH_starvote/) |
| **Reading a STAR report (201)** | the full engine report, section by section — matrix, divergence, both rounds, winner — and which parts to show 101 vs 201 vs 301 | [Reading a STAR report](tabulation_engines/LH_starvote/reading_a_star_report.md) |
| **Reading the runoff percentages** | the same runoff vote shown two ways — % of all voters vs % of the voters *with a preference*; why the winner needs a majority of the decided voters, and where Equal Support goes | [Reading the runoff percentages](STAR_Voting/runoff_percentages.md) |
| **Three notions of "winner"** | Condorcet vs Score vs Runoff can name three different candidates in one election | [Three notions of "winner"](STAR_Voting/STAR_three_winner_notions.md) |
| **STAR is monotone** | raising a candidate's score can never make them lose — the failure IRV has, STAR doesn't | [STAR is monotone](STAR_Voting/STAR_monotonicity.md) |
| **STAR is summable** | tally by adding independent precinct totals; precinct-auditable, meaningful partials | [STAR is summable](STAR_Voting/STAR_summability.md) |
| **Residual vote-splitting** | STAR ends *forced* splitting; the narrow leftover is self-inflicted bullet-voting / the chicken dilemma | [Residual vote-splitting](STAR_Voting/residual_vote_splitting.md) |
| **Equally Weighted Vote (Equal Vote Criterion)** | every ballot has an exact opposite that cancels it (the Test of Balance) — why STAR fully ends *forced* vote-splitting; Choose-One and RCV-IRV fail it | [Equally Weighted Vote](STAR_Voting/equally_weighted_vote.md) |
| **STAR — honest limits** | not Condorcet-compliant, not FBC-proof, gives up Later-No-Harm, residual splitting, strategic scoring — stated plainly | [STAR — honest limits](STAR_Voting/STAR_honest_limits.md) |
| **Tie-breaking — the full chain** | ties fall through pairwise → five-star → lot order, in both rounds | [Tie-breaking — the full chain](STAR_Voting/Tie_Breaking_STAR/tie_breaking.md) |
| **Tie-breaking in BetterVoting JSON** | how a BV export pre-draws the official lot order, and its YAML mapping | [Tie-breaking in BetterVoting JSON](STAR_Voting/Tie_Breaking_STAR/tie_breaking_JSON.md) |

Deeper conversation/debate scripts live beside their topics, indexed in [Conversation scripts — index](about_this_repo/conversation_scripts.md) (e.g. [Favorite Betrayal — Does *Only* RCV Avoid It?](STAR_Voting/favorite_betrayal_voting_301.md), ["Exhausted Ballots" — What FairVote's Word Actually Hides](RCV_IRV/exhausted_ballots_301.md)); these pages are the shorter, reference-style explainers the glossary links to. <!-- terminology-ok: bare RCV is inside linked page titles -->
