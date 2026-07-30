# Cross-method concepts — the ideas that belong to no single method

**New here? Start with [Ballot & Terminology Basics](topics/ballot_and_terminology_basics.md)** — a short four-step reading path through the ideas people most often get wrong (terminology, scores vs. ranks, what counts as "ranked," and strict vs. weak ranks).

Not every glossary term needs its own page — most are fine as a one-liner in [Glossary — voting methods & criteria](GLOSSARY.md). This folder holds the handful of concepts that are **load-bearing in debates** and worth a focused page with a worked example and **links to the test-case YAMLs** that demonstrate them.

**This folder is the cross-method half of the library.** Ideas that belong to no single method live here — [`topics/`](topics/) (flat concept pages plus thin per-topic hubs), the [voting paradoxes](voting_paradoxes/), [scores and ranks](scores_and_ranks/), the [curriculum](CURRICULUM.md), the [glossary](GLOSSARY.md), the [tabulation engines](tabulation_engines/), and the authoring canon (TIPS, templates).

**Looking for one particular method?** Its pages are *not* here — they live in that method's own folder, alongside its runnable examples, and the folder's README is its start-here:

| Method | Start here | Concept pages |
|---|---|---|
| **STAR** | [01_STAR](../01_STAR/README.md) | [`01_STAR/concepts/`](../01_STAR/concepts/README.md) |
| **Proportional STAR** | [03_STAR_PR](../03_STAR_PR/README.md) | [`03_STAR_PR/concepts/`](../03_STAR_PR/concepts/README.md) |
| **Approval** | [04_Approval](../04_Approval/README.md) | [`04_Approval/concepts/`](../04_Approval/concepts/README.md) |
| **Ranked Robin** | [05_Ranked_Robin](../05_Ranked_Robin/README.md) | [`05_Ranked_Robin/concepts/`](../05_Ranked_Robin/concepts/README.md) |
| **RCV-IRV** | [06_Other/RCV_IRV](../06_Other/RCV_IRV/README.md) | [`06_Other/RCV_IRV/concepts/`](../06_Other/RCV_IRV/concepts/README.md) |
| **Range / Score** | [06_Other/Range](../06_Other/Range/README.md) | [`06_Other/Range/concepts/`](../06_Other/Range/concepts/README.md) |

*(Until 2026-07-29 those pages lived here, in a parallel `07_Concepts/<Method>/` tree — which meant every method had two front doors. Old links still work: every moved page keeps a permanent redirect.)*

### General & cross-method

| Concept | One line |
|---------|----------|
| [**Ballot & terminology basics**](topics/ballot_and_terminology_basics.md) | the 4 ideas people most often get wrong — start here |
| [**Scores vs. ranks (don't confuse them!)**](scores_and_ranks/scores_vs_ranks.md) | order-only (ranks) vs. order+strength (scores) — relative vs. absolute preference |
| [**Scoring methods aren't RCV**](topics/scoring-methods-vs-ranked-voting.md) | scoring methods (Approval, STAR) rate candidates and sit *outside* the ranked-voting family |
| [**Approval — honest limits**](../04_Approval/concepts/approval_honest_limits.md) | no preference strength/order, the approval-threshold dilemma, bullet-voting; balanced with its equal-vote simplicity |
| [**Approval + Top-Two**](../04_Approval/concepts/approval_top_two.md) | the St. Louis package — Approval primary, top-two general; why the runoff must be a *second* election (0/1 ballots re-counted head-to-head just echo the approval count), and how STAR folds it into one ballot |
| [**Strict vs. weak ranks**](scores_and_ranks/strict_vs_weak_ranks.md) | many ranked methods allow equal ranks & compare pairwise — RCV-IRV does neither |
| [**"Preference" (a slippery word)**](topics/preference.md) | everyday opinion vs. technical "ranking"; why "Preferential Voting" is a misnomer |
| [**Ranked Robin / RCV-RR (= Copeland)**](../05_Ranked_Robin/concepts/ranked_robin.md) | a Condorcet method: ranks + equal ranks, every pair compared head-to-head; tabulable via the pref_voting engine |
| [**Ranked Robin (RCV-RR) — honest limits**](../05_Ranked_Robin/concepts/RCV_RR_honest_limits.md) | Condorcet cycles need a resolution rule; no preference strength (bland-compromise winner); burial |
| [**Proportional Representation**](../03_STAR_PR/concepts/) ([STV vs STAR-PR](../03_STAR_PR/concepts/stv/proportional_stv_vs_star.md) · [STAR-PR methods](../03_STAR_PR/concepts/STAR_PR/)) | multi-seat — coalitions get proportional seats; STV ≈ STAR-PR, Bloc differs (301) |
| [**Tabulation, step by step (201)**](topics/tabulation_star_vs_irv.md) | the same ballots counted both ways — STAR's 2 steps vs IRV's elimination rounds |
| [**RCV-IRV vs. STAR (side-by-side)**](topics/rcv_irv_vs_star.md) | balanced comparison hub — real strengths on both sides — routing to the facet pages |
| [**Tabulation engines — BV, LH, RCV-IRV**](tabulation_engines/bettervoting_and_the_engine.md) | why an election has two reports (BetterVoting's visual display + the LH engine's text report), how they map, and the convert→validate→test pipeline; hub for the per-engine folders |
| [**STAR Reporting — reading & comparing results**](../01_STAR/concepts/reporting/) | how a result is reported: scores, runoff, percentages, Equal Support/abstentions; LH vs BetterVoting and where they differ; the Score Distribution and Preference Matrix up close |
| [**The LH starvote engine**](tabulation_engines/LH_starvote/) | what the engine is (a thin fork + a thick reporting wrapper) and our improvements — the minimal **on-screen report** vs the always-full **`_tabulated`** mirror, the matrix/divergence/runoff-funnel reporting, and multi-method dispatch |
| [**Reading a STAR report (201)**](tabulation_engines/LH_starvote/reading_a_star_report.md) | the full engine report, section by section — matrix, divergence, both rounds, winner — and which parts to show 101 vs 201 vs 301 |
| [**Quorum — did enough show up?**](topics/quorum.md) | a turnout threshold separate from who wins; abstentions count toward it; an unmet quorum means no winner — won the count but not elected |

## Method-specific concepts — in the method folders

The per-method concept indexes used to be duplicated here. They aren't any more: each method folder owns its own index, so there is one list per method instead of two that drift apart. Use the table at the top of this page, or go straight to the index you want:

- [STAR](../01_STAR/concepts/README.md) — the count, properties & limits, tie-breaking, hands-on, reporting
- [Ranked Robin](../05_Ranked_Robin/concepts/README.md) — the round robin, cycles, the Condorcet family
- [RCV-IRV](../06_Other/RCV_IRV/concepts/README.md) — the terminology, the count, and the IRV-specific critiques
- [Approval](../04_Approval/concepts/README.md) · [Proportional STAR](../03_STAR_PR/concepts/README.md) · [Range / Score](../06_Other/Range/concepts/README.md)

Deeper conversation/debate scripts live beside their topics, indexed in [Conversation scripts — index](about_this_repo/06_conversation_scripts.md) (e.g. [Favorite Betrayal — Does *Only* RCV Avoid It?](../01_STAR/concepts/properties_and_limits/favorite_betrayal_voting_301.md), ["Exhausted Ballots" — What FairVote's Word Actually Hides](../06_Other/RCV_IRV/concepts/exhausted_ballots_301.md)); these pages are the shorter, reference-style explainers the glossary links to. <!-- terminology-ok: bare RCV is inside linked page titles -->
