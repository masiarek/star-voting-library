# Topic: Summability (precinct-summable / additive counts)

**Topic hub — a cross-method view.** A method is **summable** if you can split the ballots into precincts, tally each precinct into a small fixed-size table, and **add those tables** to get the statewide winner — no pooling of ballots, no central recount. Summability is what makes a method **precinct-auditable**, gives meaningful partial/early results, and runs on existing equipment.

> **The one idea to take away:** *summability is a property of the **count**, not the ballot.* The same ranked ballot is summable under Ranked Robin (add the pairwise matrix) and **not** summable under IRV (the winner depends on the elimination order). So "ranked ballots can't be summed" is a myth — it's **IRV's count** specifically that can't.

## Which methods are summable — and where each is treated

| Method | Summable? | The summable artifact (what precincts publish & add) | Full page |
|--------|:---:|------------------------------------------------------|-----------|
| **STAR** | ✅ | score totals **+** the For/Equal/Against pairwise matrix | [STAR is summable](../../STAR_Voting/properties_and_limits/STAR_summability.md) |
| **Ranked Robin / Condorcet** | ✅ | the pairwise matrix (adds cell by cell) | [RR is summable](../../RCV_Ranked_Robin/RCV_RR_summability.md) |
| **Approval** | ✅ | one approval count per candidate | [scoring methods](../scoring-methods-vs-ranked-voting.md) |
| **Plurality** | ✅ | one vote count per candidate | — |
| **RCV-IRV (Hare)** | ❌ | *none exists* — needs every ballot centrally | [IRV isn't summable](../../RCV_IRV/RCV_IRV_lack_of_summability.md) |

What "needs every ballot centrally" costs in practice — the courier runs, the single point of failure, the heavier audit, and the real incidents (Maine's process, NYC 2021, Alameda 2022) — is its own page: [**Central tabulation — when every ballot must travel**](../central_tabulation.md).

## See it both ways (runnable)

The same two-district example, counted two ways — [`summability_demo/`](../../../method_comparisons/summability_demo):

- **IRV (not summable):** B wins both districts, but is *eliminated* when they merge — no subtotal predicts it. → [worked example](../../RCV_IRV/RCV_IRV_lack_of_summability.md#worked-example-two-districts-both-won-by-b-merged-b-loses)
- **STAR (summable):** precinct score totals *and* the pairwise matrix add to the combined result. → [worked example](../../STAR_Voting/properties_and_limits/STAR_summability.md#worked-example-two-districts-subtotals-that-add-up)
- **Ranked Robin (summable):** the *same ranked ballots* IRV couldn't combine — the pairwise matrices add cell by cell and recover the winner. → [RR is summable](../../RCV_Ranked_Robin/RCV_RR_summability.md#worked-example-the-same-ballots-irv-couldnt-combine)

## How much summing? (order of summability, and multi-winner)

The examples above are all **single-winner**, where the summable artifact is tiny — one score/approval total per candidate, or one pairwise matrix. Formally that's **first-order summability**: precincts publish `O(candidates)` numbers that add up, independent of how many people voted. (Formal definition: the [summability criterion](https://electowiki.org/wiki/Summability_criterion).)

**Multi-winner is harder.** Most proportional methods are *not* first-order summable, but many can be made **k-th order summable** by **seat capping** — limiting an election to at most `k` seats, so precincts publish `O(candidatesᵏ)` totals that still add. The trade-off is practical, not theoretical: capping at 3 seats keeps the totals manageable (and 3-seat districts already give decent proportionality); capping at 7 technically qualifies but generates far too many totals to publish usefully.

There's an asymmetry that matters for this repo's [PR comparison](../../proportional_representation/stv/proportional_stv_vs_star.md): the **STAR-PR family** (Allocated Score, Sequentially Spent Score, RRV) *is* compatible with seat capping, so it can be made summable to a small order — but **STV is not**, because it eliminates never-elected candidates to free up their votes for transfer, and no fixed precinct total can anticipate which. So STV's non-summability runs deeper than IRV's: even the seat-capping workaround can't rescue it, whereas the STAR-PR methods it's usually compared against can be made precinct-verifiable at 3-seat districts.

→ Technique + bit-complexity analysis: BTernaryTau, ["Precinct-summability through seat capping"](https://bternarytau.github.io/miscellaneous/voting-theory/precinct-summability-through-seat-capping) (an enthusiast write-up; the formal criterion itself is on [electowiki](https://electowiki.org/wiki/Summability_criterion)).

## Verifiable, too

Summability makes a result locally checkable; the [`pref_voting` cross-check](../../tabulation_engines/cross_checking_with_pref_voting.md) independently confirms the pairwise/runoff math the summable artifact depends on.

External: [Is STAR Voting Precinct Summable? (starvoting.org)](https://www.starvoting.org/summable). Glossary: [`summability`](../../GLOSSARY.md).

---

*This is a **topic hub** (cross-method index). The authoritative write-ups live in the per-method folders linked above; this page just gathers the summability angle in one place for folks browsing by topic. See [the topics index](../) for the other topic hubs.*
