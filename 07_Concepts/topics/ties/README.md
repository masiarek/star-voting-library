# Topic: Ties & Tie-Breaking

**Topic hub — a cross-method view.** Real elections occasionally produce **exact ties** — two candidates with the same score, the same pairwise record, or the same first-choice count. Every method needs a defined, reproducible rule for resolving them; the rules (and how often ties even arise) differ by method.

> **The one idea to take away:** *a tie-break should be **deterministic and disclosed**, not a coin toss after the fact.* This repo uses an official **lot-number** order (`lot_numbers:`) so any tie resolves the same way every run — auditable, not arbitrary.

## Where ties happen — and where each is treated

| Method | Where a tie can occur | How it's resolved | Full page |
|--------|-----------------------|-------------------|-----------|
| **STAR** | scoring round (which two advance) **or** the automatic runoff | official tiebreak protocol, then lot order | [Tie-breaking in STAR](../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md) |
| **STAR (reporting)** | how a tie is *displayed* in the result | reported explicitly, not hidden | [reporting ties](../../../01_STAR/01_Learn/reporting/reporting_ties.md) |
| **RCV-IRV (Hare)** | which candidate to eliminate when two are tied for last | by statute — lot / prior round | [Which RCV-IRV? § tie-breaks](../../../06_Other/RCV_IRV/concepts/variants/RCV_IRV_variants.md) |
| **Ranked Robin** | a pairwise tie, or a Condorcet **cycle** | the published *degrees of ties* — 1st Degree, then 2nd Degree, then lot order | [degrees of ties](../../../05_Ranked_Robin/03_Criteria/rr_tiebreaks/degrees_of_ties.md) · [cycle resolution](../../../05_Ranked_Robin/01_Learn/cycle_resolution.md) |

**The engine-by-engine reference:** [Tiebreak ladders — every method, every engine](../../tabulation_engines/tiebreak_ladders.md) states every implementation's ladder rung by rung — LH, BetterVoting, `pyrankvote`, RCTab, `pref_voting`, `abcvoting` — with the four floors a ladder can end on and the disclosure differences. This hub says *where* ties happen; that page says exactly what each engine *does* about them.

**The "dead rung" gotcha (STAR).** STAR's ladder is *pairwise → five-star → lot*, and the **five-star** step counts only votes of score **5** (the scale max). If the tied candidates have no 5s (or equal 5s), that rung reads `0–0` — a **dead rung** — and the tie drops straight to the lot; it never steps down to the 4s. So on a low-scoring or coarse ballot the lot decides earlier and more often than the ladder's length suggests. Mnemonic: *"it counts fives, not fours."* → [The "dead rung"](../../../01_STAR/03_Criteria/tie_break_dead_rung/README.md).

**"Break the tie by margins" is not a rule until you say margins over *what* (Ranked Robin).** [Degrees of ties](../../../05_Ranked_Robin/03_Criteria/rr_tiebreaks/degrees_of_ties.md) — the tied candidates become **finalists**, and the published protocol then asks two different questions in order: the **1st Degree** wants the greatest sum of win margins over *the other finalists*, the **2nd Degree** the same sum over *the whole field*. The pool moves between the rungs, and that alone changes winners. For exactly two finalists the 1st Degree simply **is** their head-to-head. Neither engine in this library implemented the ladder, and they failed in opposite directions: this one had no 1st Degree rung at all until 2026-08-19 — adding it changed the winner on 11 of the repo's 100 Ranked Robin cases — while BetterVoting has no rung for three or more tied candidates, so every three-candidate cycle drops straight to its shuffle.

Runnable tie cases (flat-score ballots engineered to tie) live in [`Flat_scores_ties/`](../../../01_STAR/09_Parked/Flat_scores_ties/README.md) — useful for seeing exactly when each round produces a tie and how the lot order settles it — and the [dead-rung cases](../../../01_STAR/03_Criteria/tie_break_dead_rung/README.md) isolate the five-star-vs-lot step (with a [generator](../../../STARVote_LH_tabulation_engine/tools_adam/generate_dead_rung_scenarios.md) for more).

**Cross-method deep dive:** [Tie-Breaking: STAR vs. RCV-IRV — Fewer Ties, or Easier Ties?](tiebreaking_star_vs_irv.md) — why RCV-IRV's strict ranks make a tie *harder* to resolve deterministically (fewer signals, bigger consequence), not easier.

**Why the contrived cases?** [Why Build "Silly" Tie Elections?](why_contrived_tie_cases.md) — the value of deliberately-degenerate probes (`5,5,5 / 4,4,4`, rotations), plus a flow-chart map of every single-winner STAR tie case and the test that covers it.

**When the tie strikes mid-count:** [Parallel Universe Tiebreaking](parallel_universe_tiebreaking.md) — every method above resolves a tie at the *end* of the count, but an elimination method can tie over **who to eliminate**, and whichever candidate you cut changes every round after it. PUT refuses to choose: it runs every legal elimination order and elects the union of the winners. A four-voter case where standard RCV-IRV reports one winner and PUT reports two — cross-checked against `pref_voting` — plus what our own IRV engine's `random.seed(0)` really buys.

**When the batch is everyone:** [Batch elimination](batch_elimination.md) — the tie clause most statements of instant-runoff leave out. "Eliminate the candidate with the fewest first choices" is undefined when several are tied for fewest; one standard answer removes **all** of them at once. Push it and every remaining candidate can be tied, the batch takes the whole field, and the count stops with **all of them tied for the win** — which on a symmetric profile is the only answer a fair rule is allowed to give. Three runnable cases, the Coombs mirror, the case where it declares a tie in an election that has a clear Condorcet winner, and the six row-orderings that show our own engine deciding by data-entry order instead.

**When the coin flip is doing real work:** [The load-bearing tiebreak](load_bearing_tiebreak.md) — a 34-voter election where an IRV first-round tie decides the winner, and the two legal branches turn out to be the answers of *two different families of voting theory*: eliminate A and you get Coombs' winner, eliminate B and you get what every Condorcet cycle-resolution rule elects. The profile is a cycle, so no outside standard can adjudicate — and Coombs reaches its answer with no tie at all, which is what proves the indeterminacy belongs to IRV's elimination criterion rather than to the ballots. Three engines, three different disclosure behaviours, and only the certified one prints that it broke a tie.

**Why ties exist at all:** [Ties Are Forced](ties_are_forced.md) — the small impossibility theorem (Moulin 1983) proving that anonymity + neutrality + Pareto cannot coexist with always naming one winner, and that **every even electorate has a forced tie**. It supplies the theory the rest of this hub assumes: the four ways out, what each one costs, and why LH (fixed lot order), BetterVoting (random) and `pref_voting` (returns the tied set) are three defensible answers to a choice the theorem makes unavoidable.

Glossary: [`lot numbers`](../../GLOSSARY.md) · [`dead rung`](../../GLOSSARY.md).

---

*This is a **topic hub** (cross-method index). The authoritative write-ups live in the per-method folders linked above. See [the topics index](../README.md) for the other topic hubs.*
