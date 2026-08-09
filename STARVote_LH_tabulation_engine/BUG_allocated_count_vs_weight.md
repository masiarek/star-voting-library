# Bug: Allocated Score fills the quota by ballot COUNT, not ballot weight

> **STATUS: FIXED in this fork (2026-08-09; found 2026-08-08 during the STAR-PR research sprint) — still open upstream ([larryhastings/starvote#20](https://github.com/larryhastings/starvote/issues/20), filed 2026-08-09; latest release 2.1.6 affected at HEAD). BetterVoting's `AllocatedScore.ts` was never affected — it is the engine that had this right, verified live via `/API/Sandbox`. Regression guards: `tests/test_allocated_weight_accounting.py` + the fingerprint case's `expected_winners`; ledger row: [LH_ENGINE_CHANGES.md §1](LH_ENGINE_CHANGES.md); teaching page: [the count-vs-weight divergence](../03_STAR_PR/03_Criteria/allocated_count_vs_weight/README.md).**
>
> **Repo impact: two cases' committees changed with the fix.** All 20 allocated-score case files were audited against BetterVoting production. 18 were unaffected (their allocations never hit a second surplus event on reduced ballots). Two flipped to the correct committee when the fork was patched: `coop_board_scores_allocated` (Dana → **Amy** for seat 3) and `bv2130_presidential_board_star_pr` (Claudia De La Cruz → **Karina Garcia** for seat 7 — resolving that file's year-old "LH-vs-BV divergence to investigate" note). Both `expected_winners`, descriptions, mirrors and dependent pages were updated in the same commit as the fix.

## Summary

In `allocated_score_voting()`'s ballot-allocation round, every quota computation used the score group's **row count** where the method is defined over **ballot weight**:

- `allocation_count = len(supporters) - score_start` — group size as a count;
- `if allocation_count <= quota: … quota -= allocation_count` — a ballot carrying weight 139/205 retired 1.0 of the quota;
- `weight_reduction_ratio = _fraction_or_int(quota, allocation_count)` — the fractional-surplus factor as quota ÷ count.

The two denominations coincide while every weight is 1, so the first allocation of any election is always correct — the bug needs a **second** allocation event touching ballots that already carry fractional weight, i.e. a bloc strong enough to win seats after paying a fractional surplus. When it fires, a solid bloc's ballots are reduced by the same constant factor `1 − quota/n` every round (geometric decay) instead of surrendering one full quota of weight per seat: each additional seat gets cheaper, which is the large-party subsidy quota methods exist to prevent. On party-line profiles the result is D'Hondt's answer instead of the Hamilton answer the method is defined to produce.

## Reproduction (the fingerprint)

Three party-line slates — 41/19/6 voters, 5 seats, Hare quota 13.2. Slate A holds 3.11 quotas.

```python
import starvote

cands = ["A1","A2","A3","A4","B1","B2","B3","C1","C2"]
rows  = [[5,5,5,5,0,0,0,0,0]]*41 + [[0,0,0,0,5,5,5,0,0]]*19 + [[0,0,0,0,0,0,0,5,5]]*6
ballots = [dict(zip(cands, r)) for r in rows]
tb = starvote.predefined_permutation_tiebreaker(cands)
print(sorted(starvote.allocated_score_voting(ballots, seats=5, tiebreaker=tb)))
```

- Upstream 2.1.6 / this fork pre-fix: `['A1','A2','A3','A4','B1']` — **4-1-0** (D'Hondt), with the verbose run printing the giveaway constant `Allocating only 32.20% of these ballots.` (= 13.2/41) in every A round.
- This fork fixed, BetterVoting production, and the reference implementation `starvote` itself ships (`starvote/reference.py`, from the STAR tech spec's original code appendix): `['A1','A2','A3','B1','C1']` — **3-1-1** (Hamilton). Round-by-round the fixed spend factors are 32.20% → 47.48% (13.2/27.8) → 69.47% → 90.41% (13.2/14.6), matching BetterVoting's logged percentages exactly.

Case file: [`count_vs_weight_slates_c9_b66.yaml`](../03_STAR_PR/03_Criteria/allocated_count_vs_weight/cases/count_vs_weight_slates_c9_b66.yaml).

## The fix

In the allocation loop, the score group's weight sum replaces its row count in exactly the three places above:

```python
allocation_weight = _fraction_or_int(
    sum(t[INDEX_WEIGHT] for t in supporters[score_start:])
)
if allocation_weight <= quota:
    del supporters[score_start:]
    quota = _fraction_or_int(quota - allocation_weight)
    ...
weight_reduction_ratio = _fraction_or_int(quota, allocation_weight)
```

Output compatibility: round-1 reports are byte-identical to upstream (weight = count while all weights are 1 — which is also why 18 of 20 repo mirrors didn't change). When the two differ, the report adds one line under the count line: `These ballots carry a remaining weight of W.`

## Notes

- **Which semantics the fix implements:** the crossing-rule reading shared by BetterVoting — highest-scoring supporters are spent first, and the score group straddling the quota boundary is fractionally reduced so that *exactly one quota of weight* is retired per seat. The verbatim pandas reference code has two edge defects of its own (an empty-filter NaN split point, and a `spent_value > 1` masked by `.clip()`) that this loop structure never had; see the teaching page for both.
- The reference implementation's *wrapper* in this package, `allocated_score_voting_reference()`, crashes on any election where #ballots ≠ #candidates (`reference.py:137` builds the DataFrame with `index=candidates`); call `Allocated_Score(K, W, S)` directly. Reported in the tail of starvote#20; not fixed here since nothing in the repo routes through the wrapper.
- Found by running one election through several engines — LH, BetterVoting production, and the shipped reference — which is this repo's standing bug detector. The BetterVoting mislabel that hid this for a year (`tieBreakType: "random"` stamped on every STAR-PR result) is [Equal-Vote/bettervoting#1507](https://github.com/Equal-Vote/bettervoting/issues/1507).
