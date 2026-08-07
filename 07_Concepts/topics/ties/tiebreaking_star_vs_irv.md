# Tie-Breaking: STAR vs. RCV-IRV — Fewer Ties, or Easier Ties?

**One line:** RCV-IRV (Hare) has *fewer places* a tie can occur, but its **strict ranks carry less information**, so a genuine tie is *harder* to resolve deterministically — and more often falls to a lot or coin toss. STAR's richer score data gives it more deterministic tiebreakers before the lot. So the ranked method has the simpler-looking *rule*, but not the easier *problem*.

It's natural to assume that because RCV-IRV uses plain rankings, breaking a tie should be simpler than in a score method. The reverse is closer to the truth, for three reasons: **where** ties happen, **what** you have to break them with, and **how much** a tie changes the outcome.

→ Companion to [STAR Tie-Breaking — The Full Chain](../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md) and [Strict vs. Weak Ranks](../../scores_and_ranks/strict_vs_weak_ranks.md). Part of the [Ties & Tie-Breaking](README.md) topic hub. Level **301**.

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

An **IRV elimination tie decides who gets removed** — and removing a different candidate **transfers different ballots**, which can change every later round and **flip the winner**. This is the same order-sensitivity that produces IRV's [non-monotonicity](../../../method_comparisons/monotonicity/README.md) and [center squeeze](../../../06_Other/RCV_IRV/concepts/RCV_IRV_center_squeeze.md). So the one tie RCV-IRV has tends to matter more, and is harder to reason about, than either of STAR's.

## 4. The unavoidable floor

To be fair to both: a **perfectly symmetric** tie can't be broken from the ballots by *any* method. STAR reaches the lot; RCV-IRV coin-tosses the elimination; neither can do better, because the voters genuinely said nothing to separate the candidates. (See the real [BetterVoting `jfk7pd` case](../../../01_STAR/03_Criteria/tie_break_dead_rung/lot_random_vs_published_jfk7pd/lot_random_vs_published_jfk7pd.md) and its [three-candidate analog](../../../01_STAR/03_Criteria/tie_break_dead_rung/three_way_dead_rung_tie/three_way_dead_rung_tie.md).) The *difference between methods* shows up in **near-ties**: STAR's extra signals can separate candidates who tie on one measure but differ on another; strict-rank RCV-IRV more often has nothing left but chance.

## 5. Reproducibility and consistency

Random tie-breaks are **not** a STAR-specific wart. RCV-IRV jurisdictions commonly break elimination ties **by lot**, so "same ballots, different winner on a re-count" happens there too. And there is **no single canonical RCV-IRV tie-break rule** — it varies by statute, so two jurisdictions can resolve the *identical* tie differently. STAR (as specified by the Equal Vote Coalition) publishes **one** deterministic cascade (pairwise → five-star → lot); the remaining reproducibility gap is only whether the lot order is drawn and **published in advance** (the point of the `jfk7pd` writeup).

**And the academic literature is no tidier — the question is openly described as vexing and often simply ignored.** Two named proposals, both with real costs, both worth knowing because they show the problem isn't a drafting oversight:

- **Drop them all** (Taylor & Pacelli, 2006): eliminate *every* candidate sharing the lowest plurality score. Clean and deterministic — but if `k ≥ 3` survivors are all tied it removes all of them at once, so no candidate ever reaches majority support. The rule only terminates if you abandon stop-when-someone-has-a-majority and declare everyone eliminated in the final round to be co-winners. **This is the convention the reference implementations use** — Pacuit's SEP entry states both Hare and Coombs this way, and `pref_voting` implements it — and the co-winners clause is not a patch but the point: on a symmetric profile an all-candidate tie is the only outcome an anonymous, neutral rule may return. Worked in full, with three runnable cases: [Batch elimination — what happens when the batch is *everyone*](batch_elimination.md).
- **Parallel universes** (Conitzer et al., 2009): at each stage eliminate *one* of the tied candidates, but explore **every possible elimination sequence**, compute the winner of each, and declare a tie among all winners found. Arguably the most principled answer — it refuses to let an arbitrary choice decide — and it is the [set-valued approach](ties_are_forced.md#four-ways-out-and-what-each-one-costs) applied to IRV. The cost is combinatorial: the number of sequences explodes with the number of tied candidates, and this style of tiebreak is known to be computationally hard in general. Some real RCV statutes specify something of this shape.

Both reinforce section 3's point from the other direction. In STAR a tie is a question about *who wins*; in IRV it's a question about *who is eliminated*, which then changes every subsequent round — so an IRV tiebreak doesn't resolve one comparison, it forks the entire count. That's why the literature ends up enumerating universes.

## 6. In fairness to RCV-IRV

The single-rule simplicity is a **real virtue**: "eliminate the candidate with the fewest votes, break ties by lot" is easy to explain to voters and to legislate, whereas STAR's three-rung cascade is more to teach and to display. And exact ties are rare in both methods at any real scale. The claim here is **not** that RCV-IRV is "worse at ties" — it's the narrower, more interesting point: **strict ranks do not make tie-breaking easier.** They trade a simpler rule for *less resolving power* and a *more consequential* tie, and they lean on chance sooner.

**And a ranked ballot has more left in it than "lot" suggests — implementations use it.** The comparison above describes IRV *as legislated*, where a tie for last typically does go straight to a draw. It is not what a good implementation has to do. Our own vendored engine's ladder is **most second choices → thirds → fourths → coin** — the same shape as STAR's cascade, and for the same reason: keep reading the ballot while it still says something. So the honest version of the row below is that ranks carry **fewer** rungs than scores, not that they carry one; the gap is in resolving power, not in whether anybody bothered. Where the two ladders genuinely converge is at the bottom: STAR's [dead rung](../../../01_STAR/03_Criteria/tie_break_dead_rung/README.md) and a ranked ladder exhausted at every rank are the same dead end, and both hand the result to something outside the ballots. What differs there is disclosure — see [batch elimination](batch_elimination.md#what-this-repos-engine-does-instead-a-ladder-then-a-coin), where our engine's dead ladder quietly lets the *ballot file order* decide.

## Side by side

| | STAR | RCV-IRV (Hare) |
|---|---|---|
| Places a tie can occur | 2 (scoring round, runoff) | 1 (elimination) |
| Information to break it | scores → pairwise, five-star, then lot | ranks only → prior rounds / lot by statute; *later ranks*, then chance, in implementations |
| Deterministic rungs before chance | several | few (statute) — more in practice, but capped by the number of ranks |
| How often chance decides | **less often** | sooner |
| Rule complexity | higher (an explicit cascade) | lower per step, but non-canonical |
| What the tie decides | usually which finalist advances | who is eliminated → cascades, can flip the winner |
| Canonical rule? | one published cascade | varies by jurisdiction |

## See also

- [STAR Tie-Breaking — The Full Chain](../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md) — STAR's two ladders and the "dead rung."
- [Which RCV-IRV? — variants & tie-breaks](../../../06_Other/RCV_IRV/concepts/variants/RCV_IRV_variants.md) — how ranked-ballot methods differ, including tie handling.
- [Strict vs. Weak Ranks](../../scores_and_ranks/strict_vs_weak_ranks.md) — why RCV-IRV's strict ranks carry less information than scores.
- [How the Count Works — STAR vs RCV-IRV](../tabulation_star_vs_irv.md) — the two counts side by side (the non-tie case).
- Worked lot-decided ties: [BetterVoting `jfk7pd`](../../../01_STAR/03_Criteria/tie_break_dead_rung/lot_random_vs_published_jfk7pd/lot_random_vs_published_jfk7pd.md) · [the dead-rung set](../../../01_STAR/03_Criteria/tie_break_dead_rung/README.md).
