# Topic: Monotonicity (more support shouldn't hurt you)

**Topic hub — a cross-method view.** A method is **monotonic** if ranking or scoring the eventual winner *higher* can never cause them to **lose** (and moving a loser *down* can never make them win). It's the property that makes "vote your honest favorite first" safe.

> **The one idea to take away:** *non-monotonicity comes from sequential **elimination**, not from ranked ballots.* RCV-IRV (Hare) — and the other eliminate-and-transfer variants — can punish a candidate for gaining support, because added first-choices change *who is eliminated when*. Methods that read the whole ballot at once (Ranked Robin, STAR) don't have this hole.

## Which methods are monotonic — and where each is treated

| Method | Monotonic? | Why | Full page |
|--------|:---:|-----|-----------|
| **STAR** | ✅ | scores are added, not eliminated — raising a candidate only helps them | [STAR monotonicity](../../../01_STAR/01_Learn/properties_and_limits/STAR_monotonicity.md) |
| **Ranked Robin / Condorcet** | ✅ | pairwise wins only improve when you rank someone higher | [Ranked Robin](../../../05_Ranked_Robin/01_Learn/ranked_robin.md) |
| **Approval / Score** | ✅ | more approval/points can't hurt | [scoring methods](../scoring-methods-vs-ranked-voting.md) |
| **RCV-IRV (Hare)** | ❌ | added first-choices can change the elimination order and flip the winner | [IRV non-monotonicity](../../../06_Other/RCV_IRV/concepts/RCV_IRV_non_monotonicity.md) |
| **Other IRV variants** (BTR, Coombs, Baldwin, Nanson) | ❌ | same cause — they still eliminate round by round | [Which RCV-IRV?](../../../06_Other/RCV_IRV/concepts/variants/RCV_IRV_variants.md) |

So unlike [center squeeze](../center_squeeze/README.md) (which is *Hare-specific*), non-monotonicity is shared by **all** the sequential-elimination methods — only the non-eliminating methods (STAR, Ranked Robin) escape it.

## The theorems behind that table

Everything above is stated as observed behaviour. It is all theorem-backed, and knowing the theorems tells you where the boundary actually runs.

**Saying it precisely first — "lifting simply."** The loose phrasing "raise the winner on some ballots" hides a condition that has to be there. The precise move (Fishburn, 1982) is that a voter **lifts `x` simply**: `x` moves from below one or more candidates to above them, **and the relative order of every pair that doesn't involve `x` is left untouched.** A *resolute* SCF is **monotonic** if lifting the winner `x` simply always leaves `x` the winner. The italicised clause is what makes the criterion mean anything — without it a "lift" could smuggle in arbitrary other reordering, and a flipped result would prove nothing about support for `x`.

**Why the eliminating methods fail, as a theorem, not a collection of examples.** Smith (1980) proved that **every scoring run-off rule violates monotonicity** — the whole family at once, not RCV-IRV in particular. That is the general statement behind this hub's "shared by all the sequential-elimination methods," and it covers plurality run-off, STV, and the Borda-elimination variants ([Baldwin, Nanson](../../../06_Other/RCV_IRV/concepts/variants/RCV-IRV-Baldwin-Nanson.md)) as well as Hare. The [Alaska 2022](../../../method_comparisons/monotonicity/upward_monotonicity_alaska.md) and [San Francisco D7](../../../method_comparisons/monotonicity/downward_monotonicity_sf.md) cases are not unlucky elections; they are instances of a rule the theorem says must have them.

**Why the others pass, also as a theorem.** There's a clean sufficient condition for score-maximising rules: if lifting `x` simply can never *lower* `x`'s score and never *raise* anyone else's, the rule is monotonic — and stays monotonic if a fixed ordering breaks its ties. That single argument covers **[Copeland](../../../05_Ranked_Robin/01_Learn/ranked_robin.md) (= Ranked Robin), [Simpson/minimax](../../voting_paradoxes/minimax.md), and every proper scoring rule** ([Plurality, Borda, k-approval and the rest](../ranked_ballot_methods_zoo.md)). It also settles the boundary question for STAR: **STAR is not a scoring run-off rule in Smith's sense.** Smith's family eliminates a candidate and *re-tallies* the scores, round after round; STAR scores once, takes the top two, and finishes with a pairwise comparison. It never re-scores, so it sits outside the class the theorem condemns — which is the formal version of this hub's "scores are added, not eliminated."

**And a warning about the criterion itself.** The resolute definition above can be satisfied **vacuously**: take any SCF at all, modify it to add one tied alternative to its outcome on every profile, and the "the winner must not change" test can no longer bite. A criterion that a trivial cosmetic change can buy is not measuring what it appears to. Peleg (1981) proposed the repair, and it is the version worth quoting: after any simple lift of a winning `x`, **`x` remains a winner *and no new winners are added*.** Sanver and Zwicker (2012) argue for exactly this form — it resists the trick, and it is also a better fit for what monotonicity is *for*, since insisting the winning set not change at all is stricter than "the output should move in the same direction as the input." Copeland, Simpson, the proper scoring rules, [sequential majority comparison](../../../06_Other/other_ranked_methods/agenda_voting.md) and Top Cycle all satisfy Peleg's stronger version too.

This is worth filing next to the repo's other [criterion-scepticism](../condorcet/ordered_majority_rule_irv.md) material: **"method M satisfies criterion C" is only as strong as C's definition**, and here is a case, straight from the literature, where the standard definition is gameable by construction. Ask which version of a criterion is being claimed before crediting it.

**Worked real examples — both flavours, both real:**
- **Upward** ("more is less" — raise the winner, she loses): [Alaska 2022](../../../method_comparisons/monotonicity/upward_monotonicity_alaska.md). Ranking the winner Peltola *higher* would have made her *lose*.
- **Downward** ("less is more" — lower a loser, they win): [San Francisco D7 2020](../../../method_comparisons/monotonicity/downward_monotonicity_sf.md). Ranking the loser Engardio *lower* would have made him *win*.

Both are reproduced on the real ballots, and in both, Ranked Robin elects the Condorcet winner — unmoved — while RCV-IRV flips.

Glossary: [`monotonicity`](../../GLOSSARY.md) · [`lifting simply`](../../GLOSSARY.md) · [`Peleg monotonicity`](../../GLOSSARY.md).

## Sources

- J. H. Smith, "Aggregation of preferences with variable electorate," *Econometrica* 41 (1973); and the 1980 result that every scoring run-off rule violates monotonicity. **Lean:** neutral.
- P. C. Fishburn (1982) — the standard "lifting simply" formulation. · B. Peleg (1981) — the irresolute strengthening. · M. R. Sanver & W. S. Zwicker (2012) — the argument for Peleg's version. **Lean:** neutral.
- William S. Zwicker, "Introduction to the Theory of Voting," in *Handbook of Computational Social Choice* (CUP 2016), §2.6 — Definition 2.10 and the surrounding discussion, including the vacuous-satisfaction problem and the score-based sufficient condition. **Lean:** neutral; the standard academic reference.

---

*This is a **topic hub** (cross-method index). The authoritative write-ups live in the per-method folders linked above. See [the topics index](../README.md) for the other topic hubs.*
