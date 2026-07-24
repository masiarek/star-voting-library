# Topic: Condorcet Efficiency (electing the head-to-head winner)

**Topic hub — a cross-method view.** A **Condorcet winner** is a candidate who beats every other candidate one-on-one (by majority). A method is **Condorcet-efficient** if it elects that candidate whenever one exists. (Sometimes nobody qualifies — the pairwise results form a **cycle** — which is a separate, rarer problem.)

> **The one idea to take away:** *the Condorcet winner is the "majority's head-to-head choice."* Some methods guarantee it, some get it almost always, and RCV-IRV (Hare) can miss it precisely because of [center squeeze](../center_squeeze/).

## Which methods elect the Condorcet winner — and where each is treated

| Method | Condorcet winner? | Notes | Full page |
|--------|:---:|------|-----------|
| **Ranked Robin / Copeland** | ✅ always | it *is* a Condorcet method — most pairwise wins | [Ranked Robin](../../RCV_Ranked_Robin/ranked_robin.md) |
| **BTR / Baldwin / Nanson** | ✅ always | Condorcet-safe IRV variants | [Which RCV-IRV?](../../RCV_IRV/variants/RCV_IRV_variants.md) |
| **STAR** | ⚠️ very often | highly Condorcet-efficient, not guaranteed; the runoff usually recovers it | [STAR automatic runoff](../../STAR_Voting/the_count/STAR_Automatic_Runoff.md) |
| **RCV-IRV (Hare)** | ❌ not guaranteed | can eliminate the Condorcet winner before the final round | [Center squeeze](../../RCV_IRV/RCV_IRV_center_squeeze.md) |
| **Approval / Plurality** | ❌ | don't use the full pairwise picture | [scoring methods](../scoring-methods-vs-ranked-voting.md) |

When there's **no** Condorcet winner (a cycle), the principled "still in contention" list is [the Smith set](../smith_set.md), and methods differ in how they pick from it — see [cycle resolution](../../RCV_Ranked_Robin/cycle_resolution.md). The repo's [divergence ledger](../../../method_comparisons/divergence_review/INDEX.md) catalogs real library elections where STAR, IRV, and the Condorcet winner disagree.

> **"Isn't the Condorcet criterion just a guarantee for moderates?"** No — that's the load-bearing error of a much-cited FairVote article. The Condorcet winner is defined *by* the electorate and moves with it (a majority-first-choice landslide candidate is automatically the Condorcet winner). The article, quoted and checked claim by claim against tabulated elections — including its own 40/15/40 hypothetical, where RCV-IRV eliminates the very moderate it discusses: [FairVote's Condorcet article, claim-checked](fairvote_condorcet_claim_check.md).

> **"So is the Condorcet winner sacrosanct, then?"** Also no — and the serious version of that argument deserves a serious reading. Edelman's ["Myth of the Condorcet Winner," tabulated](edelman_condorcet_myth.md) (BV2173, live): a "cancellation" profile going back to Condorcet himself where every majoritarian count elects one candidate and every positional count (Borda, score sum) elects another, 41 voters to 40 — plus the join-consistency/no-show theorems. The anti-Condorcet argument that *survives* tabulation.

> **"Isn't Ranked Robin the same as Condorcet?"** Almost — they're identical when a Condorcet winner exists, and part ways only in a cycle (Condorcet goes blank, Ranked Robin still picks the best record). Worked through with a real example in [Ranked Robin vs. the Condorcet winner](../../RCV_Ranked_Robin/ranked_robin_vs_condorcet.md).

> **"But a paper proves Condorcet, IIA, and monotonicity aren't even desirable?"** That's the most sophisticated form of the argument — an arXiv paper defining "ordered majority rule" and claiming IRV uniquely satisfies it. The catch: the property is IRV's own algorithm restated, defined circularly, so the "uniqueness" is a mirror. Taken apart (with the honest core — the case for *cardinal* ballots — kept) in [Ordered majority rule and the "Condorcet isn't desirable" argument](ordered_majority_rule_irv.md).

> **"Isn't there a slick new system that puts the head-to-head matchups right on the ballot?"** Yes — **Better Choices**, a Top-3 Condorcet method whose final ballot is three bubble matchups instead of a ranking, completed by Minimax. Explained fairly and claim-checked (including the wrinkle that its cycle behavior is Minimax's, *not* Copeland/Ranked Robin's, and the intransitive-ballot cost of independent bubbles): [Better Choices — the pairwise-ballot Condorcet method](better_choices_pairwise_ballot.md).

> **"Which Condorcet rule is *best* — is that even answerable?"** For **exactly three candidates**, yes, and there's a neutral 2024 theorem for it: Brandt, Dong & Peters prove that **maximin and its refinements** (leximin, Nanson) are the *uniquely* best-defended Condorcet extensions against the no-show and reinforcement paradoxes — the tractable small case where [Moulin's impossibility](../../voting_paradoxes/no_show.md) hasn't yet bitten. Summarized with the fine print (3-candidate-only; it's the tie-broken refinements that are characterized; STAR isn't a Condorcet extension so it's out of scope): [Condorcet-Consistent Choice Among Three Candidates](three_candidate_maximin.md).

> **"When there's no Condorcet winner, who decides — the ballots or the rule?"** In a cycle the family splits, and the newest member says so out loud: [Split Cycle, claim-checked](split_cycle.md) discards each cycle's weakest defeat and *returns every candidate left undefeated*, rather than applying a convention. Includes a tabulated election where a candidate **no voter ranks above the winner** still flips Schulze's result — plus the four things that case doesn't show.

> **"Where do I go to read about this properly?"** [Condorcet methods — a reading list](condorcet_reading_list.md): the books, papers, and free surveys worth your time, each with its lean marked — and, first, the one taxonomy (Fishburn's C1/C2/C3) that makes the family's names stop sliding. Start there if the *nomenclature* is what's blocking you.

Glossary: [`Condorcet`](../../GLOSSARY.md).

---

*This is a **topic hub** (cross-method index). The authoritative write-ups live in the per-method folders linked above. See [the topics index](../) for the other topic hubs.*
