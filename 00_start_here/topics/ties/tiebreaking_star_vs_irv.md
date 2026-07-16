# Tie-Breaking: STAR vs. RCV-IRV — Fewer Ties, or Easier Ties?

**One line:** RCV-IRV (Hare) has *fewer places* a tie can occur, but its **strict ranks carry less information**, so a genuine tie is *harder* to resolve deterministically — and more often falls to a lot or coin toss. STAR's richer score data gives it more deterministic tiebreakers before the lot. So the ranked method has the simpler-looking *rule*, but not the easier *problem*.

It's natural to assume that because RCV-IRV uses plain rankings, breaking a tie should be simpler than in a score method. The reverse is closer to the truth, for three reasons: **where** ties happen, **what** you have to break them with, and **how much** a tie changes the outcome.

→ Companion to [STAR Tie-Breaking — The Full Chain](../../STAR_Voting/Tie_Breaking_STAR/tie_breaking.md) and [Strict vs. Weak Ranks](../../scores_and_ranks/strict_vs_weak_ranks.md). Part of the [Ties & Tie-Breaking](README.md) topic hub. Level **301**.

---

## 1. Where a tie can occur

**STAR — two rounds, so two loci.** A tie can appear in the **Scoring Round** (two candidates with the same total score, tied for a finalist slot) or in the **Automatic Runoff** (the two finalists preferred by an equal number of voters). Each has its own tiebreak ladder.

**RCV-IRV — rounds of elimination, so essentially one locus.** The tie that matters is the **elimination tie**: two or more candidates tied for the *fewest* current top-choice votes — which one do you drop? (A final-round tie for the win reduces to the same coin-flip question.)

On this axis alone, RCV-IRV *is* simpler: one kind of tie, not two.

## 2. What you have to break the tie with — the part that flips the intuition

**STAR has more to work with, because scores carry more than order.** When STAR hits a tie it can consult, in order, real deterministic tests before any randomness:

- **pairwise** — of the tied candidates, whom do more voters prefer head-to-head;
- **five-star** — who has the most maximum-score votes;
- only then the **lot**.

**RCV-IRV has only the ranks.** When two candidates are tied for last, nothing *cardinal* distinguishes them — there's no "strength of support" to look at. Real statutes therefore reach for ad-hoc rules: who had fewer votes in a **prior round**, forward/backward elimination, occasionally a Borda-style total — and, very commonly, **drawing lots**. (Equal ranks aren't available to help either: IRV uses *strict* ranks, so a voter can't even mark two candidates the same — see [Strict vs. Weak Ranks](../../scores_and_ranks/strict_vs_weak_ranks.md).)

The headline: **more information means more deterministic rungs, so the lot is reached *less* often.** Strict ranks give fewer tools, so the coin comes out *sooner*. STAR's tiebreak rules look more elaborate precisely *because* it has more data to spend before giving up to chance — and that spending pays off.

## 3. The consequence of a tie is bigger in RCV-IRV

A STAR **scoring-round** tie usually just decides *which of two finalists advances*; the runoff still runs, and the winner is whichever finalist more voters prefer. The tie rarely decides the winner by itself.

An **IRV elimination tie decides who gets removed** — and removing a different candidate **transfers different ballots**, which can change every later round and **flip the winner**. This is the same order-sensitivity that produces IRV's [non-monotonicity](../../../method_comparisons/monotonicity/README.md) and [center squeeze](../../RCV_IRV/RCV_IRV_center_squeeze.md). So the one tie RCV-IRV has tends to matter more, and is harder to reason about, than either of STAR's.

## 4. The unavoidable floor

To be fair to both: a **perfectly symmetric** tie can't be broken from the ballots by *any* method. STAR reaches the lot; RCV-IRV coin-tosses the elimination; neither can do better, because the voters genuinely said nothing to separate the candidates. (See the real [BetterVoting `jfk7pd` case](../../../01_STAR/tie_break_dead_rung/lot_random_vs_published_jfk7pd/lot_random_vs_published_jfk7pd.md) and its [three-candidate analog](../../../01_STAR/tie_break_dead_rung/three_way_dead_rung_tie/three_way_dead_rung_tie.md).) The *difference between methods* shows up in **near-ties**: STAR's extra signals can separate candidates who tie on one measure but differ on another; strict-rank RCV-IRV more often has nothing left but chance.

## 5. Reproducibility and consistency

Random tie-breaks are **not** a STAR-specific wart. RCV-IRV jurisdictions commonly break elimination ties **by lot**, so "same ballots, different winner on a re-count" happens there too. And there is **no single canonical RCV-IRV tie-break rule** — it varies by statute, so two jurisdictions can resolve the *identical* tie differently. STAR (as specified by the Equal Vote Coalition) publishes **one** deterministic cascade (pairwise → five-star → lot); the remaining reproducibility gap is only whether the lot order is drawn and **published in advance** (the point of the `jfk7pd` writeup).

## 6. In fairness to RCV-IRV

The single-rule simplicity is a **real virtue**: "eliminate the candidate with the fewest votes, break ties by lot" is easy to explain to voters and to legislate, whereas STAR's three-rung cascade is more to teach and to display. And exact ties are rare in both methods at any real scale. The claim here is **not** that RCV-IRV is "worse at ties" — it's the narrower, more interesting point: **strict ranks do not make tie-breaking easier.** They trade a simpler rule for *less resolving power* and a *more consequential* tie, and they lean on chance sooner.

## Side by side

| | STAR | RCV-IRV (Hare) |
|---|---|---|
| Places a tie can occur | 2 (scoring round, runoff) | 1 (elimination) |
| Information to break it | scores → pairwise, five-star, then lot | ranks only → prior rounds / lot |
| Deterministic rungs before chance | several | few |
| How often chance decides | **less often** | sooner |
| Rule complexity | higher (an explicit cascade) | lower per step, but non-canonical |
| What the tie decides | usually which finalist advances | who is eliminated → cascades, can flip the winner |
| Canonical rule? | one published cascade | varies by jurisdiction |

## See also

- [STAR Tie-Breaking — The Full Chain](../../STAR_Voting/Tie_Breaking_STAR/tie_breaking.md) — STAR's two ladders and the "dead rung."
- [Which RCV-IRV? — variants & tie-breaks](../../RCV_IRV/variants/RCV_IRV_variants.md) — how ranked-ballot methods differ, including tie handling.
- [Strict vs. Weak Ranks](../../scores_and_ranks/strict_vs_weak_ranks.md) — why RCV-IRV's strict ranks carry less information than scores.
- [How the Count Works — STAR vs RCV-IRV](../tabulation_star_vs_irv.md) — the two counts side by side (the non-tie case).
- Worked lot-decided ties: [BetterVoting `jfk7pd`](../../../01_STAR/tie_break_dead_rung/lot_random_vs_published_jfk7pd/lot_random_vs_published_jfk7pd.md) · [the dead-rung set](../../../01_STAR/tie_break_dead_rung/README.md).
