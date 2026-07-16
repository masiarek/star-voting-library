# RCV-IRV — concept pages

Everything explaining **RCV-IRV** — ranked ballots counted by **instant runoff** (IRV): rank the candidates, eliminate the last-place candidate each round, transfer their ballots, repeat until someone has a majority of continuing ballots.

**First, the word.** "RCV" names a *ballot* (ranked); "IRV" names *one tabulation* of it. Start here so the rest reads precisely:

- [Is it RCV or IRV? (and why "RCV-IRV")](RCV_or_IRV_whats_the_right_word.md) — the house-terminology page
- [RCV vs. IRV vs. RCV-IRV — a note on terminology](RCV-IRV-confusing-name.md)
- [RCV-IRV (Hare)](RCV-IRV-Hare.md) — the specific method US "RCV" almost always means

## How it counts

- [Is RCV "simple"? — which half?](RCV_IRV_is_simple.md) — the ballot is simple; the count is not
- [Is RCV-IRV "just plurality in sequence"?](RCV_IRV_and_plurality.md)
- [Exhausted (inactive) ballots](RCV_IRV_exhausted_ballots.md) — ballots that drop out of the count mid-tally

## The IRV-specific critiques

These are properties of **IRV the tabulation**, not of ranked ballots in general (Ranked Robin isn't squeezed) — keep them attached to IRV:

- [Center squeeze](RCV_IRV_center_squeeze.md) — the moderate eliminated early
- [Non-monotonicity](RCV_IRV_non_monotonicity.md) — when *more* support makes you lose
- [Not summable](RCV_IRV_lack_of_summability.md) — every ballot must be counted centrally, and [that central count has costs](../topics/central_tabulation.md)
- [Fails the Equal Vote criterion](RCV_IRV_equal_vote.md)
- [Exhausted ballots (301)](exhausted_ballots_301.md) · [forced vs. voluntary exhaustion](forced_vs_voluntary_exhaustion.md)
- [Misconceptions & false claims — an index](rcv_irv_false_claims.md)

## Variants — other tabulations of the ranked ballot

The [**variants/**](variants/) subfolder — same ranked ballot, different elimination rule:

- [Which RCV-IRV? — the variants & tie-breaks](variants/RCV_IRV_variants.md) · [family tree](variants/RCV_methods_family_tree.mermaid)
- [BTR](variants/RCV-IRV-BTR.md) · [Baldwin & Nanson](variants/RCV-IRV-Baldwin-Nanson.md) (Borda-elimination, Condorcet-safe) · [Coombs](variants/RCV-IRV-Coombs.md) (eliminates on last choices) · [Contingent & Supplementary](variants/RCV-IRV-contingent-supplementary.md)

## Case studies — RCV-IRV in the wild

The [**case_studies/**](case_studies/) subfolder — real elections:

- [Alaska 2022](case_studies/RCV_IRV_alaska_2022.md) — spoiler + center squeeze + non-monotonicity in one federal race
- [The Alternative Vote in Australia](case_studies/RCV_IRV_australia.md) — a century, assessed evenhandedly
- [North Carolina](case_studies/RCV_IRV_north_carolina.md) · [History](case_studies/RCV_IRV_history.md)

## Reference

- Glossary: [RCV-IRV & ranked-ballot terms](glossary_rcv_irv.md)

*(Other tabulations of the same ranked ballot: [Ranked Robin](../RCV_Ranked_Robin/README.md) (Condorcet/consensus), [STV](../proportional_representation/) (proportional). Up: the docs hub [`00_START_HERE`](../00_START_HERE.md).)*
