<!--
Ready-to-paste GitHub issue for  github.com/Equal-Vote/bettervoting
How to file: open a NEW issue and paste everything below the line. It cross-
references #1063 (deterministic lot numbers) — if maintainers prefer, this can
instead be posted as a comment on #1063 with the worked example as evidence.
The links point at the public masiarek/YAML repo so the ballots, export, and
independent tabulations are inspectable.
-->

---

**Title:** STAR `random` tie-break yields a non-reproducible winner — reproducible example (election `jfk7pd`), and the case for deterministic pre-published lot numbers (#1063)

### Summary

On a genuine STAR tie, BetterVoting resolves the final tie-break **at random**
(`tieBreakType: "random"`). That means the **same ballots can certify a different
winner on a re-count** — an auditability gap for a public-election tool. I have a
tiny, fully-reproducible real election (`jfk7pd`) where the winner was a coin
flip, and I can reconstruct *either* outcome from the exported ballots with an
independent STAR engine. This is the concrete case for **deterministic,
pre-published lot numbers** (already tracked in #1063); filing it with the worked
example and an acceptance test.

The tabulation itself is correct STAR — the issue is **reproducibility**, not the
math.

### Environment

- bettervoting.com, STAR, single winner.
- Election id: **`jfk7pd`** ("The BV recipe — the crazy scenario").

### Steps to reproduce

1. Create a STAR election with two candidates, **Ada** and **Ben**.
2. Cast two ballots:

   | Voter | Ada | Ben |
   |-------|:---:|:---:|
   | 1 | 4 | 0 |
   | 2 | 0 | 4 |

3. Tabulate and export the result JSON.

Both candidates end with **total score 4** and **`fiveStarCount: 0`** (nobody
used a 5). The election is perfectly symmetric — nothing on the ballots
distinguishes Ada from Ben.

### What happens (from the exported result)

BetterVoting's own `roundResults[0].logs` walk the tie-break ladder and stop at a
random draw:

```
advance_to_runoff_same_score   Ben, Ada     (both advance, score 4)
runoff_tied                    Ben, Ada     (head-to-head 1–1)
runoff_score_tie               Ben, Ada     (score tiebreak: 4–4)
runoff_five_star_tie           Ben, Ada     (five-star tiebreak: 0–0)   ← dead rung
runoff_random                  winner: Ben                              ← coin flip
runoff_tiebreak                winner: Ben
```

```json
"tieBreakType": "random",
"perm": ["c-h28", "c-63w"],          // the order THIS run drew: Ben, then Ada
"elected": [{ "name": "Ben", "score": 4, "fiveStarCount": 0, ... }]
```

So the deterministic rungs (pairwise → score → five-star) all tied, and the
winner was chosen **at random**, drawing Ben ahead of Ada.

### Expected vs. actual

- **Expected:** re-running the certified ballots always yields the same winner.
- **Actual:** because the final tie-break is random, a re-count has a 50% chance
  of electing **Ada** instead of **Ben** — from the identical ballots.

### Independent verification (either winner is reproducible)

Tabulating the *same* `jfk7pd` ballots with an independent STAR engine that
resolves final ties by a **published lot order** (rather than a random draw):

| Lot order fed to the engine | Winner |
|-----------------------------|:------:|
| `[Ben, Ada]` (BV's drawn `perm`) | **Ben** — reproduces BV's certified result |
| `[Ada, Ben]` (a deterministic published order) | **Ada** |

Same two ballots, opposite winner, decided entirely by the tie-break order. Files
(ballots, the frozen export, and both tabulations) are here:

- Frozen export: <https://github.com/masiarek/YAML/blob/master/01_STAR/tie_break_dead_rung/lot_random_vs_published_jfk7pd/lot_random_vs_published_jfk7pd_bv_export.json>
- Write-up + both tabulations: <https://github.com/masiarek/YAML/blob/master/01_STAR/tie_break_dead_rung/lot_random_vs_published_jfk7pd/lot_random_vs_published_jfk7pd.md>

### Root cause (not a bug in the count)

This is the [**"dead rung"**](https://github.com/masiarek/YAML/blob/master/00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md#edge-case-five-star-is-a-dead-rung-when-nobody-scored-the-max)
case: STAR's second tie-break rung counts votes equal to the scale maximum (5),
and here nobody scored a 5, so it reads 0–0 and can't separate the candidates.
That's expected and correct. The remaining question — who wins a genuine tie — is
answered by `random`, which is the reproducibility problem.

### Proposed fix / acceptance criteria

1. **Deterministic, pre-published lot numbers (#1063).** Draw the candidate lot
   order *before* counting and publish it; resolve every remaining tie by that
   fixed order instead of `random`.
   - **Acceptance test:** tabulating the same ballot set twice must always
     produce the same winner. For `jfk7pd` with a published order `[Ada, Ben]`,
     the winner is deterministically **Ada** every run; with `[Ben, Ada]`,
     deterministically **Ben**. (I can provide these as fixtures.)
2. **Keep exporting the sequence (#1371, done).** The `perm` / `tieBreakOrder`
   fields already let an outside engine reproduce a given result — please keep
   them. (That's how the table above reconstructs BV's Ben.)
3. **Surface it in the UI (relates to #1379).** When a result is decided by the
   lot rather than the ballots, show a plain-language note — e.g. *"Tie resolved
   by lot order: Ben over Ada"* — and ideally which rung fell through. A silent
   random tie-break is what makes a valid result look arbitrary.

### Further reading (background docs)

Fuller write-ups behind this report, in case they're useful:

- **STAR Tie-Breaking — the full chain** (the ladder, the "dead rung", and why
  each round breaks its tie with the *other* round's measure):
  <https://github.com/masiarek/YAML/blob/master/00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md>
- **This case, in full** (View 1 = BV screenshots, View 2 = the independent
  report, plus the reproduction commands):
  <https://github.com/masiarek/YAML/blob/master/01_STAR/tie_break_dead_rung/lot_random_vs_published_jfk7pd/lot_random_vs_published_jfk7pd.md>
- **The dead-rung case set** (the concept + a "cap ladder" showing the rung
  ignores 4s):
  <https://github.com/masiarek/YAML/blob/master/01_STAR/tie_break_dead_rung/README.md>
- **Does it scale past two candidates?** A 3-candidate analog — three candidates,
  three possible winners by lot; divergence is `(k−1)/k`:
  <https://github.com/masiarek/YAML/blob/master/01_STAR/tie_break_dead_rung/three_way_dead_rung_tie/three_way_dead_rung_tie.md>
- **Generate more of these** (any `k`, plus "less obvious" ties buried in
  realistic-looking ballots):
  <https://github.com/masiarek/YAML/blob/master/STARVote_LH_tabulation_engine/tools_adam/generate_dead_rung_scenarios.md>

### Related issues

- #1063 — deterministic lot-number tie-breaking (the core fix this documents).
- #1371 — export the tie-break sequence (closed; keep it — enables reconstruction).
- #1379 — finalist/winner divergence + missing human-readable tie-break explanation.
- #1052, #1035 — reporting-side siblings on the same family of tie elections
  ("no ballots have been cast"; `NaN` on equal ties/preferences).

Happy to provide additional cases — including 3+ candidate and "less obvious"
variants where the tie is buried in a realistic-looking ballot set — and the
fixtures for the acceptance test.

> **Companion issue (UI):** separate from this tabulation fix, the results view
> doesn't disclose that a winner was decided by a (random) tie-break. Filed
> separately — see
> [`bv_github_issue_ui_tiebreak_transparency.md`](https://github.com/masiarek/YAML/blob/master/01_STAR/tie_break_dead_rung/lot_random_vs_published_jfk7pd/bv_github_issue_ui_tiebreak_transparency.md).
