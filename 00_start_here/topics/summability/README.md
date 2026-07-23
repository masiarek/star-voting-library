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

### The cryptographic payoff — summable means *encryptable*

Summability has a consequence that rarely gets stated: it is what makes a method cheap to make **end-to-end verifiable** with cryptography.

[Additively homomorphic encryption](https://en.wikipedia.org/wiki/Homomorphic_encryption) lets you **add encrypted numbers without decrypting them** — combine every voter's encrypted ballot into an encrypted total, then decrypt only the *total*. Each voter can confirm their own ballot was included, and anyone can verify the tally, while no individual ballot is ever opened. That is precisely [Microsoft's ElectionGuard](https://github.com/Election-Tech-Initiative/electionguard) (open source; homomorphic ElGamal, designed by Josh Benaloh), and it works because a plurality tally **is just addition**.

The asymmetry that follows:

- **Summable methods (STAR, Approval, Score, Choose-One)** — the tally is a fixed set of sums, known in advance. They map directly onto additive encryption; only **partial** homomorphic encryption is needed (adding, not multiplying), which is decades-old, well-understood maths. STAR's scoring round is the same construction as ElectionGuard's, just with scores 0–5 instead of 0/1.

  **STAR's runoff needs one extra step, and it's worth knowing.** The runoff asks a *comparison* — "did this ballot score A above B?" — which addition alone can't compute, and the finalist pair isn't known until the scoring round is decrypted. The fix: have each ballot also carry an encrypted **1/0 indicator for every candidate pair** ("I scored i above j"), proved consistent with the scores. Then the runoff for *any* pair is again just a sum, decided in one shot with no second round of decryption. It costs n(n−1) extra values — 20 for five candidates — and it hands you the whole [pairwise preference matrix](../pairwise_counting.md) for free, so the Condorcet check and [Ranked Robin](../../RCV_Ranked_Robin/README.md) come along at no extra cost. STAR therefore stays inside partial homomorphic encryption end to end; it never needs the heavier machinery below.
- **Non-summable methods (RCV-IRV, STV)** — the count is **sequential and adaptive**: you cannot know what to tally in round 3 until rounds 1–2 are decrypted. There is no fixed sum to compute homomorphically, so verifiable implementations fall back on **mixnets** — shuffling and then decrypting individual ballots with proofs that the shuffle was honest. That is heavier machinery, and it means individual ballots *do* get opened.

So the [central-tabulation](../central_tabulation.md) cost of non-summability shows up a second time in cryptography. It's the same structural property, and it's an argument for summable methods that has nothing to do with who wins.

*Caveat, stated plainly:* none of this makes **internet** voting safe. Homomorphic tallying protects the *count*; it does nothing about malware on the voter's own device, or about coercion and vote-buying when people vote unobserved. The [US Vote Foundation's E2E-V study](https://www.usvotefoundation.org/E2E-VIV) (2015) and the National Academies' *Securing the Vote* (2018) both concluded internet voting is not ready for public elections **even with** end-to-end verifiability. The technology is far better suited to in-person paper systems and to lower-stakes organizational elections.

---

*This is a **topic hub** (cross-method index). The authoritative write-ups live in the per-method folders linked above; this page just gathers the summability angle in one place for folks browsing by topic. See [the topics index](../) for the other topic hubs.*
