# Bug: SSS silently discards zero-score ballots whenever any ballot exhausts in the same round

> **STATUS: OPEN in this fork (found 2026-08-08, verified 2026-08-09) — fix drafted and proven on a scratch copy, NOT yet applied (awaiting Adam's go). Present in upstream [larryhastings/starvote](https://github.com/larryhastings/starvote) at HEAD (2.1.6); no upstream issue filed yet. Distinct from [#17](https://github.com/larryhastings/starvote/issues/17) (the verbosity bug, fixed in this fork — see [BUG_sss_verbosity.md](BUG_sss_verbosity.md)), but the two interact: fixing #17 by dedenting the allocation block, as this fork did, promotes THIS bug from the verbose-only path to every run.**
>
> **Repo impact: none.** All 5 SSS case files were checked — the trigger condition never fires in any of them, and the full verbose reports are byte-identical under the fix (so no `_tabulated` mirror would change). Verified 2026-08-09; details below.

## Summary

In `sequentially_spent_score()`, the ballot-allocation step rebuilds the remaining-ballots list, but the `remaining_decorated_ballots.append(t)` sits **inside the `if score:` branch** — only ballots that scored the round's winner above 0 are ever appended. The swap to the rebuilt list happens whenever `allocated` is nonzero, i.e. whenever **any** ballot exhausts to 0 stars. Consequence: in any SSS round where at least one supporter exhausts, **every ballot that scored the winner 0 is silently removed too — full remaining budget and all.** Those voters spent nothing and, by the method's definition, keep their stars for later rounds; deleting them changes who wins later seats.

The trigger is narrow but real: a ballot exhausts only when its raw score for the winner is 5 **and** the round has no surplus (weighted spend = `raw × stars/5 ≤ stars`, with equality exactly when raw = 5 and the reduction ratio is 1). When it fires, it can flip the committee.

## Environment

- This fork: `starvote/__init__.py`, `sequentially_spent_score()`, allocation loop at ~L2704–2747 — bug manifests at **every** verbosity (the fork's #17 fix dedented the whole block out of the verbosity guard, structure preserved).
- Upstream starvote **2.1.6** (current HEAD, verified 2026-08-09): same loop at ~L2387–2428, still nested inside `if options.verbosity:` — so upstream manifests this bug at `verbosity>=1` and the #17 bug (no spending at all) at `verbosity=0`.
- Method: `sss` (Sequentially Spent Score), multi-winner.

## Reproduction

7 voters, 3 candidates, 2 seats. Runs against either engine:

```python
import starvote

ballots = [
    {'Amy': 0, 'Bo': 5, 'Cy': 3},
    {'Amy': 5, 'Bo': 0, 'Cy': 0},   # Amy bullet voter — scores Cy 0
    {'Amy': 0, 'Bo': 3, 'Cy': 4},
    {'Amy': 2, 'Bo': 2, 'Cy': 5},   # exhausts in round 1 (raw 5, no surplus)
    {'Amy': 5, 'Bo': 1, 'Cy': 0},   # scores Cy 0
    {'Amy': 0, 'Bo': 0, 'Cy': 4},
    {'Amy': 2, 'Bo': 2, 'Cy': 1},
]

print(sorted(starvote.election(starvote.sss, ballots, seats=2, verbosity=1)))
```

(The YAML form lived at the STAR-PR sprint's scratchpad as `exp_census/cli/quirk_sss.yaml`; the profile above is the same election and is the durable copy.)

### Actual output (this fork, any verbosity; upstream at verbosity>=1)

```
['Bo', 'Cy']
```

### Expected output (textbook SSS)

```
['Amy', 'Cy']
```

Upstream at `verbosity=0` happens to also print `['Amy', 'Cy']` — but only because issue #17 means no stars are spent at all there; round 2 is just bloc score voting minus Cy. Same answer, wrong reasons, and a second live demonstration that upstream's winners depend on the logging flag.

## Hand-trace of the quirk round

Hare score quota = 7·5/2 = 17½. Round 1 scores: Cy 17, Amy 14, Bo 13 → **Cy** seated. 17 < 17½ → no surplus, reduction ratio 1, so each ballot spends its full Cy score:

| Ballot (Amy,Bo,Cy) | Cy score | stars 5 → | fate in the loop |
|---|---|---|---|
| 0,5,3 | 3 | 2 | reweighted to 2/5, appended |
| 5,0,0 | 0 | 5 (untouched) | **never appended** (`if score:` skipped) |
| 0,3,4 | 4 | 1 | reweighted to 1/5, appended |
| 2,2,5 | 5 | 0 | exhausted → `allocated = 1` |
| 5,1,0 | 0 | 5 (untouched) | **never appended** |
| 0,0,4 | 4 | 1 | reweighted to 1/5, appended |
| 2,2,1 | 1 | 4 | reweighted to 4/5, appended |

`allocated` is nonzero, so `decorated_ballots = remaining_decorated_ballots` — and the two Amy bullet voters vanish with 5 unspent stars each. Round 2 with the truncated list: Bo 4⅕ vs Amy 1⅗ → **Bo**. Round 2 with the zero-score ballots kept (textbook): Amy 11⅗ vs Bo 5⅕ → **Amy**. Both arithmetic lines were verified against actual engine runs (current engine → Bo; patched scratch copy → Amy, matching to the fraction).

Counterfactual confirming the trigger: when no ballot exhausts, `allocated` is 0, the rebuilt supporters-only list is *discarded*, and the zero-score ballots survive by luck. The bug needs the exhaustion.

## Why "keep them" is the correct behavior

The [electowiki SSS definition](https://electowiki.org/wiki/Sequentially_Spent_Score) (the method's canonical write-up; Keith Edmonds' method, advocacy-adjacent source but this is a mechanics question, where it's the clearest): the procedure's spend step is *"Each voter spends the amount of stars they gave the elected candidate"* — a voter who gave 0 spends 0, and *"Voters cannot influence subsequent rounds more than the stars they have remaining"* — these voters have all 5 remaining. That is the whole point of Vote Unitarity: influence is spent only in exchange for representation gained.

Decisively, the **reference implementation on that page never removes any ballot**: it keeps the full ballot frame for the whole tabulation and updates budgets with `ballot_weight = (ballot_weight - score_spent).clip(0.0, 1.0)` — a zero-score voter's `score_spent` is 0 and their weight is untouched. (Removing *exhausted* ballots, as the engine does, is a legitimate optimization — weight-0 ballots contribute nothing. The defect is only the removal of the zero-score non-supporters riding along with them.)

BetterVoting offers no SSS tabulator (its score-PR is Allocated Score only — `packages/backend/src/Tabulators/` has no SSS), so there is no BV cross-check to run; electowiki's definition and reference code are the arbiters here.

## How often it matters

From the 2026-08-08 STAR-PR sprint census (2-seat committees, reimplementations validated against the LH engine on 1,800 profile/rule pairs with 0 mismatches): the quirk **changed the elected committee in 25 of 1,783 tie-free impartial-culture profiles (~1.4%)**, and in 0 of ~2,000 spatial-culture (1D/2D) profiles. Rare, systematic, and biased in a describable direction: it strips unspent budget from blocs that abstained on an early winner — exactly the blocs SSS is designed to protect into later rounds.

## Repo impact — checked, none

All 5 repo SSS cases (`coop_board_scores_sss`, `three_neighbors_sss`, `two_officers_sss`, `02b_c5_b63_proportional-sss`, `03b_star_pr_3seats`) were run through an instrumented reimplementation and through a patched scratch copy of the engine (2026-08-09):

- the trigger (a supporter exhausting while a zero-score ballot is still alive) **never fires** in any of them — every allocation round in those files has a surplus, so no ballot ever exhausts;
- winners are unchanged, and the full `verbosity=2` reports are **byte-identical** under the fix — so no `_tabulated` mirror or generated page would shift.

## Suggested fix

Dedent the two append lines out of `if score:` (fork lines ~2742–2743), so non-supporters ride through the rebuild; exhausted supporters still `continue` past the append:

```python
                        if score:
                            ...
                            stars = max(stars - star_reduction, 0)
                            if stars != starting_stars:
                                if not stars:
                                    allocated += 1
                                    continue          # exhausted: still dropped
                                ...reweight t...

                        # zero-score ballots spent nothing and keep their
                        # budget — they must survive the rebuild too.
                        remaining_decorated_ballots.append(t)
                        remaining_weighted_ballots.append(weighted_ballot)
```

Verified on a scratch copy: the repro flips to `['Amy', 'Cy']` at every verbosity, and all 5 repo SSS cases produce byte-identical reports. When applied to the fork, the change lands with: a regression test (the repro profile asserted at verbosities 0/1/2, plus the 5 repo cases pinned — natural home: extend `tests/test_verbosity_invariance.py`'s SSS coverage or a new `tests/test_sss_zero_score_ballots.py`), and a ledger row in [LH_ENGINE_CHANGES.md](LH_ENGINE_CHANGES.md).

## Upstream issue draft (for larryhastings/starvote)

Title: **SSS ballot allocation silently discards ballots that scored the winner 0, whenever any ballot exhausts in the same round**

Body: the Summary, Reproduction, Hand-trace, and Why-keep-them sections above, framed against 2.1.6's line numbers (~L2387–2428), plus this warning: *the bug currently manifests only at `verbosity>=1`, because at `verbosity=0` the entire allocation block is skipped (issue #17). Fixing #17 by dedenting the block — the natural fix — promotes this bug to every run unless the two `remaining_*.append(...)` calls are also dedented out of `if score:` at the same time.* The repro above shows upstream returning `['Amy', 'Cy']` at verbosity 0 and `['Bo', 'Cy']` at verbosity 1 — a second winners-depend-on-verbosity demonstration for #17's thread, and textbook SSS (per electowiki's procedure and reference implementation, which never remove a ballot) says `['Amy', 'Cy']`.
