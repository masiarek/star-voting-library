# Topic: Ties & Tie-Breaking

**Topic hub — a cross-method view.** Real elections occasionally produce **exact ties** — two
candidates with the same score, the same pairwise record, or the same first-choice count.
Every method needs a defined, reproducible rule for resolving them; the rules (and how often
ties even arise) differ by method.

> **The one idea to take away:** *a tie-break should be **deterministic and disclosed**, not
> a coin toss after the fact.* This repo uses an official **lot-number** order
> (`lot_numbers:`) so any tie resolves the same way every run — auditable, not arbitrary.

## Where ties happen — and where each is treated

| Method | Where a tie can occur | How it's resolved | Full page |
|--------|-----------------------|-------------------|-----------|
| **STAR** | scoring round (which two advance) **or** the automatic runoff | official tiebreak protocol, then lot order | [Tie-breaking in STAR](../../STAR_Voting/Tie_Breaking_STAR/tie_breaking.md) |
| **STAR (reporting)** | how a tie is *displayed* in the result | reported explicitly, not hidden | [reporting ties](../../STAR_reporting/reporting_ties.md) |
| **RCV-IRV (Hare)** | which candidate to eliminate when two are tied for last | by statute — lot / prior round | [Which RCV-IRV? § tie-breaks](../../RCV_IRV/RCV_IRV_variants.md) |
| **Ranked Robin** | a pairwise tie, or a Condorcet **cycle** | total margin, then lot order | [cycle resolution](../../RCV_Ranked_Robin/cycle_resolution.md) |

**The "dead rung" gotcha (STAR).** STAR's ladder is *pairwise → five-star → lot*, and the
**five-star** step counts only votes of score **5** (the scale max). If the tied candidates
have no 5s (or equal 5s), that rung reads `0–0` — a **dead rung** — and the tie drops straight
to the lot; it never steps down to the 4s. So on a low-scoring or coarse ballot the lot decides
earlier and more often than the ladder's length suggests. Mnemonic: *"it counts fives, not
fours."* → [The "dead rung"](../../../01_STAR/tie_break_dead_rung/).

Runnable tie cases (flat-score ballots engineered to tie) live in
[`Flat_scores_ties/`](../../../01_STAR/Flat_scores_ties) — useful for seeing exactly
when each round produces a tie and how the lot order settles it — and the
[dead-rung cases](../../../01_STAR/tie_break_dead_rung/) isolate the five-star-vs-lot step
(with a [generator](../../../STARVote_LH_tabulation_engine/tools_adam/generate_dead_rung_scenarios.md)
for more).

Glossary: [`lot numbers`](../../GLOSSARY.md) · [`dead rung`](../../GLOSSARY.md).

---

*This is a **topic hub** (cross-method index). The authoritative write-ups live in the
per-method folders linked above. See [the topics index](../) for the other topic hubs.*
