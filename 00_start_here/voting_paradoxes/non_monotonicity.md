# Non-monotonicity — losing by gaining support

*A voting method is **monotone** if ranking or scoring a candidate higher can never hurt them, and lower can never help. **Non-monotonicity** (Felsenthal: lack of monotonicity; a.k.a. the more-is-less or additional-support paradox) is the failure: a candidate loses because voters raised them, or wins because voters lowered them.* (The model **conditional** paradox: one datum changes — a few voters raise a candidate — everything else held constant, and the outcome flips against the raise.)

→ Glossary: [`monotonicity`](../GLOSSARY.md) · Felsenthal's taxonomy: [README](README.md)

## The 17-voter demonstration (live pair)

[BV2145](../../method_comparisons/felsenthal_paradoxes/bv2145_6fj2kg_felsenthal_ex2.md) → [BV2146](../../method_comparisons/felsenthal_paradoxes/bv2146_krk2px_felsenthal_ex2_monotonicity.md) is Felsenthal's Example 2, run for real on BetterVoting. Under plurality-with-runoff (= IRV for three candidates), **Ben wins** the first election. Then two voters raise Ben from `Cleo>Ben>Ada` to `Ben>Cleo>Ada` — and **Ben loses**: his extra first-choice votes drain Cleo below Ada, the elimination flips from Ada to Cleo, and Ada beats Ben 9–8 in the final pair. More support, worse result.

The repo also has a standalone constructed pair: [the monotonicity set](../../method_comparisons/monotonicity/monotonicity_pages/monotonicity_irv_after.md) (RCV-IRV flips; STAR, on the same story, doesn't).

## Where it comes from

Non-monotonicity is a disease of **elimination order**. In RCV-IRV (and plurality-with-runoff) the candidate eliminated early hands their transfers to the finalists — so raising a candidate can demote a *useful loser* out of the elimination slot and reshuffle the final pair. This is IRV-specific, not a property of ranked ballots: Ranked Robin counts the same ballots pairwise and is fully monotone, and in the BV2145/46 pair both Ranked Robin and STAR elect Ada before *and* after the raise. (In BV2146's STAR race the raise does change the *finalist pair* — Ben displaces Cleo — but Ada still wins the runoff; score totals move *with* the voter's change, never against the raised candidate.)

## Why it matters

A method that can punish a candidate for being liked more punishes voters for voting sincerely — it makes "should I really rank my favorite first?" a live strategic question, which is precisely what a good ballot is supposed to end. And unlike the [Condorcet winner paradox](condorcet_winner_paradox.md), non-monotonicity is invisible in any single election result: it only shows when you compare the two worlds, which is why a frozen, re-runnable pair like BV2145/46 is the right teaching object.
