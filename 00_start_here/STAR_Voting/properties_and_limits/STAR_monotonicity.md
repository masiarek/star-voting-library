# STAR Is Monotone — More Support Never Backfires

**One line:** under **STAR**, raising a candidate's score can **never** cause them to lose, and lowering it can never cause them to win. Honest support always helps the candidate it's given to. STAR satisfies the **monotonicity** criterion.

→ The method that *fails* this is RCV-IRV — see [`IRV non-monotonicity`](../../RCV_IRV/RCV_IRV_non_monotonicity.md) (where more first-place votes can defeat the winner). Glossary: [`monotonicity`](../../GLOSSARY.md).

---

## Why STAR can't fail it

STAR's winner comes entirely from **sums**: add up each candidate's scores to find the two finalists, then take the pairwise majority between those two. There is **no elimination order** to perturb.

- Raising a candidate's score can only **increase** their total, so it can never push them *out* of the top two.
- In the runoff, scoring a finalist higher can only move your vote **toward** them, never away.

Because every step is additive and there's nothing to "transfer," the backwards paradox that hits IRV simply has no mechanism to occur.

## Worked example — the same profile that breaks IRV

Take the exact ballots that make RCV-IRV fail (see the IRV page), translated to 0–5 scores (1st → 5, 2nd → 3, unranked → 0), and run STAR before and after **4 voters raise X**:

→ [`monotonicity_star_before.yaml`](../../../method_comparisons/monotonicity/monotonicity_star_before.yaml) · [`monotonicity_star_after.yaml`](../../../method_comparisons/monotonicity/monotonicity_star_after.yaml)

```
            BEFORE                         AFTER (4 voters raise X)
  12: 5,3,0  (X>Y)               16: 5,3,0  (X>Y)
  12: 0,5,3  (Y>Z)                8: 0,5,3  (Y>Z)
  10: 3,0,5  (Z>X)               10: 3,0,5  (Z>X)
  STAR winner: X                  STAR winner: X
```

STAR elects **X both before and after** — raising the winner can't hurt them. The *after* file's `[Divergence from STAR]` block makes the contrast self-documenting on the very same ballots:

```
STAR    = X
RCV-IRV = Z   (differs from STAR)
```

Same voters, same change: RCV-IRV flips X → Z; STAR doesn't budge. (Verified on the engine: STAR elects X in both files.)

## The 301 nuance — a *stronger* variant STAR doesn't pass

Everything above is the standard **monotonicity criterion** (formally *mono-raise*: raising a candidate's score, and changing nothing else, never hurts them). STAR passes it without exception. But mathematician D. R. Woodall catalogued *several* monotonicity properties, and STAR fails a stronger one, **mono-raise-delete**: *"a candidate X should not be harmed if X is raised on some ballots **and** all candidates now below X on those ballots are deleted from them"* (for a score ballot, "deleted" means "dropped to the lowest score").

The catch is that this bundles **two** moves — raise X *and* bury everyone the voter placed below X — and only the first is safe. Raising X's own score can never push X out of the top two; but *which candidate joins X in the runoff* depends on **everyone's** totals. Burying the also-rans can change X's runoff **opponent** — from a Y that X beats to a Z that beats X. X was "raised," yet ended up losing. The soft spot isn't the arithmetic of X's own score; it's **finalist selection**.

This doesn't walk back STAR's monotonicity. The everyday promise — *"score your favorite at the top, it can only help them"* — holds exactly, because that's the standard criterion, and voters don't perform the composite raise-and-delete operation. It's simply the honest, precise statement: **STAR satisfies mono-raise; it does not satisfy every stronger monotonicity variant.** (The same care cuts the other way for IRV — which fails even plain mono-raise, the far more damaging failure.)

**See it, runnable:** a worked before/after pair where raising X and deleting the loser below X flips the winner from X to Z — [`mono_raise_delete_before.yaml`](../../../method_comparisons/monotonicity/mono_raise_delete_before.yaml) (X wins) · [`mono_raise_delete_after.yaml`](../../../method_comparisons/monotonicity/mono_raise_delete_after.yaml) (X raised, Y deleted → **Z** wins). The only change is nine ballots going `Z=5,X=3,Y=2` → `Z=5,X=4,Y=0`; burying Y drops it below Z, so the runoff becomes X vs Z, which X loses.

*Source: D. R. Woodall, ["Monotonicity and Single-Seat Election Rules"](http://www.votingmatters.org.uk/ISSUE6/P4.HTM), Voting Matters, Issue 6 (1996).*

## Why this matters

Monotonicity is what lets you tell a voter, truthfully, *"score your favorite at the top — it can only help them."* Under IRV that advice can backfire; under STAR it always holds. It's a quieter virtue than the spoiler story, but it's the one that keeps honest voting safe.

Sources: [monotonicity criterion (Wikipedia)](https://en.wikipedia.org/wiki/Monotonicity_criterion).
