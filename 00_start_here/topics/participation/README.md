# Topic: Participation (can showing up to vote ever hurt you?)

**Topic hub — a cross-method view.** The **Participation criterion**: adding sincere ballots that prefer X over Y must never change the winner *from* X *to* Y. A method that fails it has the **no-show paradox** — an electorate where some voters get a *better* result by staying home than by casting an honest ballot. Read forward, the same failure is the **Twin paradox**: new voters who agree with you exactly arrive, and your group's outcome gets *worse*.

> **The one idea to take away:** *"vote — it can only help your side" is a promise a voting method can keep or break.* Pure score-summing methods keep it structurally; every method with an elimination or runoff stage — RCV-IRV, Coombs, plurality-runoff, **and STAR** — plus every Condorcet-consistent method (Moulin's theorem) can break it in some electorate. The differences are *how often* and *how visibly*.

## The live demonstration — one electorate, told twice (BV2174 / BV2175)

The centerpiece pair: 8 voters who love April (sincere ranking April > Bruno > Celia) decide whether to show up. Same three candidates, same everyone-else, **three races on each election** — and the methods split:

| Method | 8 fans stay home ([BV2174 ↗](https://bettervoting.com/yyhr66/results)) | 8 fans vote ([BV2175 ↗](https://bettervoting.com/9dhv8y/results)) | Showing up… |
|---|---|---|---|
| Choose-One | Celia | **April** | ✅ helped — last choice → favorite |
| STAR | Bruno | **April** | ✅ helped — favorite wins (more sincere support moved the result their way) |
| **RCV-IRV** | Bruno | **Celia** | ❌ **HURT — 2nd choice replaced by LAST choice** |
| Ranked Robin (LH) | Celia | April | ✅ helped *(LH-only — see below)* |

The IRV mechanism, in one sentence: the 8 extra April-first ballots keep April alive past round one, which gets **Bruno — the 8 voters' own fallback — eliminated instead**, and Bruno's transfers elect Celia, their last choice, 38–24. Their honest votes for their favorite bought their worst outcome; staying home (BV2174) keeps Bruno. Case pages with full engine reports: [baseline](../../../method_comparisons/participation_no_show/participation_no_show_pages/bv2174_yyhr66_noshow_baseline.md) · [show-up](../../../method_comparisons/participation_no_show/participation_no_show_pages/bv2175_9dhv8y_noshow_showup.md).

Two footnotes on the pair, both deliberate:

- **Both electorates are a Condorcet cycle** (April > Bruno > Celia > April) — that's the soil no-show paradoxes grow in, and it's why there is **no Ranked Robin race on BetterVoting**: a Copeland three-way tie resolves by *random draw* there (not freezable), while the LH engine's margin tiebreak resolves it deterministically (Celia before, April after — see the `_tabulated` mirrors, and [LH vs BV on RR ties](../../RCV_Ranked_Robin/rr_tiebreak_lh_vs_bv.md)).
- **BV2174's STAR count is a [Runoff Reversal](../../GLOSSARY.md)** — Celia tops the scores 136/122/120, Bruno wins the runoff 34–20. One pair, two lessons.

## Which methods can punish participation — and where each is treated

| Method | Participation? | Notes | Full treatment |
|--------|:---:|------|-----------|
| **Score / Approval** | ✅ immune | a sincere added ballot only adds support where the voter intends — summation can't backfire | [scoring methods vs ranked](../scoring-methods-vs-ranked-voting.md) |
| **Choose-One (Plurality)** | ✅ immune | more votes for your favorite never hurts your favorite | [plurality](../plurality.md) |
| **STAR** | ❌ rare | the *runoff stage* costs the formal guarantee — live flip: [BV2165→BV2166 (Coombs Ex.19)](../../../method_comparisons/felsenthal_paradoxes/bv2166_b7b8dv_coombs_noshow.md), shown honestly | [STAR's honest limits](../../STAR_Voting/STAR_honest_limits.md) |
| **Ranked Robin / all Condorcet methods** | ❌ provably | **Moulin's theorem**: Condorcet consistency ⇒ no-show paradoxes exist; see also Edelman's join-consistency argument | [Edelman, tabulated](../condorcet/edelman_condorcet_myth.md) |
| **RCV-IRV / plurality-runoff / Coombs** | ❌ readily | the elimination machinery — same root as [non-monotonicity](../monotonicity/) | [no-show paradox](../../voting_paradoxes/no_show.md) |

**The honest scorecard, spelled out:** this page's live pair shows IRV failing while STAR passes — but on *other* electorates STAR fails too ([BV2165/66](../../../method_comparisons/felsenthal_paradoxes/bv2166_b7b8dv_coombs_noshow.md): two abstainers do better under STAR's runoff as well as Coombs'). No elimination-or-runoff method — and no Condorcet method — carries a participation *guarantee*. The structural difference: STAR's failures need a finalist to flip **and** the runoff to reverse (rare, constructed), IRV's need only an elimination-order flip (the everyday center-squeeze machinery). Only pure summation (Score, Approval) and Choose-One are immune outright — and they pay for it elsewhere ([what makes a good winner?](../what_makes_a_good_winner.md)).

## The paradox catalog & the theory

- [**The No-Show paradox — when staying home beats voting (and its Twin)**](../../voting_paradoxes/no_show.md) — the Felsenthal-taxonomy page: BV2150/51 (plurality-runoff, 11 voters) and the STAR flip BV2165/66.
- [**Edelman's "Myth of the Condorcet Winner," tabulated**](../condorcet/edelman_condorcet_myth.md) — Young's join-consistency theorem (two groups both choose C; combined they choose B) and why the no-show family is *inherent* to Condorcet consistency.
- [**Reading these fairly**](../../../method_comparisons/paradoxes_and_whoops/reading_these_fairly.md) — the honest-limits framing: every method fails *something*; the question is which failures, how often, how visibly.

Glossary: [`no-show paradox`](../../GLOSSARY.md).

---

*This is a **topic hub** (cross-method index). The authoritative write-ups live in the per-method folders and the paradox catalog linked above. See [the topics index](../) for the other topic hubs.*

# file: README.md
