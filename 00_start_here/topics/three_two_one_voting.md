# 3-2-1 Voting — the "Good / OK / Bad" method, and how it compares to STAR

*A well-regarded rated method designed by **Jameson Quinn** (Center for Election Science). Voters rate every candidate **Good**, **OK**, or **Bad**; the winner is found in three steps — **3** semifinalists, then **2** finalists, then **1** winner. It dodges the same strategic traps STAR does (no center squeeze, a non-slippery chicken dilemma, a built-in dark-horse guard), which is why it keeps coming up as a serious reform option. This page explains it fairly and lays it next to STAR — they're close cousins, with real trade-offs either way.*

→ Related: [the strategic pathologies (five Molochs)](strategic_pathologies.md) · [the chicken/Burr dilemma](../../method_comparisons/chicken_dilemma/) · [scores vs. ranks](../scores_and_ranks/scores_vs_ranks.md) · [Approval voting](../Approval_Voting/approval_voting.md).

---

## The ballot and the three steps

**Ballot:** rate each candidate **Good**, **OK**, or **Bad** (a 3-level rated ballot — coarser than STAR's 0–5, finer than Approval's yes/no).

1. **3 — Semifinalists.** Take the **three** candidates with the most **Good** ratings.
2. **2 — Finalists.** Of those three, keep the **two** with the fewest **Bad** ratings.
3. **1 — Winner.** Of those two, the winner is the one rated higher on **more ballots** — the pairwise winner (Good > OK > Bad).

**Two guard rules on the *third* semifinalist** (they're what make 3-2-1 more than a toy):

- **Clone guard:** the third semifinalist can't be a near-duplicate of the first two (not the same party as both, or — nonpartisan — don't count its "Good"s on ballots that also rated the first semifinalist Good). Stops a party from cloning its way into the finals.
- **Dark-horse guard:** the third semifinalist must have at least **½ as many Good ratings** as the top semifinalist. If none qualifies, skip step 2. This is what keeps a [dark horse](../../method_comparisons/dark_horse_borda/) — a nobody with almost no real support — out of the finals.

## Worked example — it resolves the chicken dilemma (usually)

Take the [chicken/Burr scenario](../../method_comparisons/chicken_dilemma/): allies **A** and **B** must beat **C**, whom the majority opposes (35 prefer A>B, 25 prefer B>A, 40 back C). If the A/B voters use **OK** to separate their favorite from their ally (A-voters: A Good, B OK; B-voters: B Good, A OK; C-voters: C Good, both allies Bad):

```
             Good   Bad
   A          35     40
   B          25     40
   C          40     60
Step 1  → semifinalists A, B, C (only three candidates)
Step 2  → finalists A, B        (fewest Bad; C's 60 Bad knocks it out)
Step 3  → A beats B, 35 to 25   → A wins
```

3-2-1 elects **A** — the honest pairwise winner — and the majority-opposed C is knocked out in the finalist step. Same answer STAR gives, and no slippery slope.

**The honest catch — granularity.** If those same A/B voters rate *both* allies **Good** (both are genuinely liked, after all), then no voter distinguishes A from B, step 3 is a **0–0 tie**, and 3-2-1 falls back to a coin flip — a milder echo of Approval's chicken tie. 3-2-1 only cleanly resolves the finals when voters spend the **OK** level to rank their top two. STAR's 0–5 ballot sidesteps this: scoring A **5** and B **4** is natural and low-stakes, so the runoff almost always has a real preference to read. This is the [preference-vs-support / scale-granularity](../scores_and_ranks/preference_vs_support.md) point in miniature: more levels means the final step can actually decide.

## What 3-2-1 is good at

- **No center squeeze** — the finalist step is by fewest-Bad, not fewest-first-choices, so a broadly-liked centrist isn't eliminated for lacking first-place love the way [IRV](../RCV_IRV/RCV_IRV_center_squeeze.md) does.
- **Non-slippery chicken** — like STAR, a few defectors can't start an avalanche (a final head-to-head means small defections don't snowball).
- **Explicit dark-horse and clone guards** — where STAR resists dark horse *implicitly* (via support-reading), 3-2-1 bolts on rules that do it explicitly.
- **Genuinely explainable** — "your worst candidate gets knocked out before the finals" is an intuitive, even chantable pitch; several people find it the easiest good method to explain across the aisle.
- **Summable** — precincts can report Good tallies, Bad tallies, and the pairwise matrix; the winner is computable from those aggregates (no need to centralize raw ballots). Same virtue STAR has.

## 3-2-1 vs. STAR — close cousins, real trade-offs

| | **STAR** | **3-2-1** |
|---|---|---|
| Ballot | 0–5 (6 levels) | Good / OK / Bad (3 levels) |
| Tabulation | add scores → top 2 → pairwise runoff (**2 steps**) | most-Good → fewest-Bad → pairwise (**3 steps** + 2 guard rules) |
| Center squeeze | avoids | avoids |
| Chicken dilemma | non-slippery | non-slippery (but see the tie caveat) |
| Dark horse | resisted implicitly (reads support) | resisted explicitly (½-Good guard) |
| Summable | yes (score totals + matrix) | yes (Good + Bad tallies + matrix) |
| Granularity | finer — breaks near-ties in the runoff | coarser — top two can tie unless voters use "OK" |
| Spec complexity | simpler to state — no special-case rules | needs the clone / dark-horse rules to behave |
| Backed by | Equal Vote Coalition | Center for Election Science / Quinn |

Neither is strictly better. **STAR** is finer-grained and structurally simpler (two clean steps, no special cases), and its extra levels break the exact tie that can trip 3-2-1. **3-2-1** answers voters who find 0–5 daunting with just three words, and it hard-codes the dark-horse and clone protections that STAR gets for free from its scores. Both are honest, summable, center-squeeze-free rated methods — worlds better than plurality or IRV, and disagreeing mainly at the margins.

## Honest limits

- **Not strategy-proof** — [Gibbard](gibbard_satterthwaite_theorem.md) forbids that for any method. Quinn notes 3-2-1 becomes tactical with **four or more** serious candidates.
- **The guard rules are real complexity** — the "third semifinalist" clone and dark-horse conditions are fiddly to write into law and to explain in full, even if the top-line pitch is simple.
- **Three levels can under-resolve** — the finalist tie above; a Good/OK/Bad ballot simply carries less information than 0–5.
- **Not in public use** — 3-2-1 is a **proposed** method (no governmental adoption we know of) and is **not** offered by [BetterVoting](../tabulation_engines/BV/), so this library can't back a 3-2-1 case with a live election the way it does STAR / Approval / Ranked Robin / IRV. The example above is worked by hand; the LH engine does not tabulate 3-2-1.

## Sources

- [3-2-1 voting — electowiki](https://electowiki.org/wiki/3-2-1_voting) — the clearest mechanics reference for this niche/branded method (**advocacy-adjacent**: electowiki leans reformer, and 3-2-1 is a Center for Election Science proposal — cite it for *how it works*, not for verdicts).
- Jameson Quinn, *The Six Voting Molochs* — where 3-2-1 is proposed as the non-slippery fix to the [chicken dilemma](../../method_comparisons/chicken_dilemma/); Quinn is CES-aligned (Approval/3-2-1), which is exactly why his praise of methods he *didn't* design carries weight.
- Contrast within this library: [STAR](../STAR_Voting/STAR_start_here.md) · [Approval](../Approval_Voting/approval_voting.md) · [Ranked Robin](../RCV_Ranked_Robin/README.md) · glossary [`3-2-1 voting`](../GLOSSARY.md).
