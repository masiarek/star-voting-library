---
name: engine-rendering
description: What the STAR engine prints by default and why — the DEFAULT_OPTIONS house style that replaced per-file `options` blocks, its auto-gates, --full and the always-full _tabulated mirror, the self-reconciling runoff summary, the Smith set block and its shared classifier, and the RCV-IRV transfer block. Load before changing engine output, adding an options override to a case file, or editing any of those blocks or their wording tests.
---

# What the engine prints

*Migrated out of `CLAUDE.md` on 2026-09-12 so it loads on demand instead of in every session. The rules below are unchanged.*

- **Case files carry NO `options:` block (settled 2026-08-09).** The display flags
  were maintainer conveniences that had accreted into ~10 lines of noise per file —
  a quarter of a median case file — and a case file should read as a plain-text
  election scenario: title → description → method → ballots → expected winners.
  The engine's own defaults ARE the house on-screen style now — one
  `DEFAULT_OPTIONS` dict in `starvote_larry_hastings.py`: finalists matrix ON, the
  self-reconciling runoff summary ON, description / Condorcet / score-distribution
  OFF, ballots collapsed with `×`. Two auto-gates cover what files used to
  hand-set: the matrix switches itself off for **multi-winner** races (a "Top 2
  Finalist" grid is a single-winner concept, misleading for PR/Bloc) and for
  **2-candidate** races (it would just echo the runoff); and **Ranked Robin prints
  its pairwise table by default** (the round-robin table IS the method; the Smith
  block stays a separate opt-in). The saved `_tabulated` copy still renders
  **maximum info automatically**, and the **`--full`** CLI flag puts that same
  everything-on render on screen — with one seam (closed 2026-08-09): for a
  **multi-winner** race the forced-on grid prints as a plain, unmarked
  **"Preference Matrix"** (the "Top 2 Finalist" markers came from a silent
  seats=1 STAR analysis; an "Informational only — not part of the N-winner
  count" legend line replaces them, and the same unmarked grid is what a
  `show_matrix: true` override puts on screen). Consequences:
  - **Don't add an `options:` block to a case file.** A lesson that wants a heavier
    section on the page (score distribution, full grid, Smith set) links the case's
    generated page / `_tabulated` mirror — which force everything on — or pastes
    from a `--full` run; it does not flip flags in the yaml.
  - A file MAY still set `options:` to override any default. That is **reserved**
    for the option-demo files (`04b_…display-options-all`, `display_options_demo`,
    and the engine's `options_examples.yaml` reference — they exist to showcase the
    feature) and rare deliberate special renders. When one is used, booleans are
    the long `true` / `false` form (the parser also accepts t/f/y/n/etc.).
  - The `[Divergence from STAR]` block prints whenever methods differ, regardless
    of options — comparative demos keep their punch with no flags at all.
  - History: before 2026-08-09 every case file restated a 10-line "house minimal
    block" (501 files, ~5,000 lines); the sweep deleted them all, and the render
    diffs were machine-verified (no winner line changed). `show_irv` was already
    vestigial — the divergence block always prints — and survives only so old
    blocks still parse. The defaults + auto-gates are locked by
    `tests/test_default_render.py`.
- **`show_runoff_percent`** (engine default **`true`** since 2026-08-09): prints the
  two-line, **self-reconciling** runoff summary under the Automatic Runoff winner —
  e.g. `Voters with a preference: 363 of 461 (98 Equal Support). Dog 190 (52%) vs
  Cat 173 (48%); majority = 182` — using the **decided-voters** denominator (Equal
  Support excluded) but stating it against the total ballots with the Equal Support
  gap named inline, so the denominator never has to be inferred. The always-full
  `_tabulated` copy expands it into a "Runoff math" funnel (`461 − 98 = 363`,
  majority) — don't hand-set that. The wording/funnel/default are locked by
  `tests/test_runoff_percent.py`; change them together.
- **`show_smith_set`** (Ranked Robin only): still **opt-in on screen** (engine
  default `false`) and **always forced on in the `_tabulated` mirror** —
  deliberately NOT dragged along by RR's default-on matrix (a dedicated `smith`
  gate in the RR echo keeps them separate). Prints the **Smith set** (the smallest
  group whose every member beats every candidate outside it), says whether that's a
  lone Condorcet winner, a top **cycle**, an all-draws **dead heat**, or a **mixed**
  group held open by draws (some members beat others but no loop closes — "not all
  draws" does NOT imply "cycle"), and whether the winner landed inside it. The shape
  call is one shared classifier (`_group_shape`, on `_all_pairs_draw` + the
  beats-loop DFS) asked by both the RR winner line and the Smith block, so the two
  lines can't contradict each other about the same matrix — keep it shared.
  **RCV-IRV mirrors get the same block automatically** (no option — the IRV path
  has no options plumbing). The two uses are opposite: RR is Smith-efficient so the
  block is descriptive; RCV-IRV is not, so it's a genuine pass/fail. Wording locked
  by `tests/test_smith_set.py`; concept page `07_Concepts/topics/smith_set.md`.
- **The RCV-IRV transfer block** (added 2026-08-10, no option — mirror-always,
  screen under `--full`, same contract as the Smith block). `pyrankvote` prints
  each round as a column of totals, which omits the two numbers this repo's
  exhausted-ballot and center-squeeze pages are *about*: where a transferred vote
  came FROM, and how many ballots have stopped counting — so IRV's "majority" can
  finally be reconciled against all ballots cast instead of asserted. Built by
  `build_transfer_block()` in `rcv_irv_tabulation.py`. Three rules it encodes:
  **the eliminations are read back from `pyrankvote`, never recomputed** (else the
  block can contradict the table above it on a tie settled by the second-choices
  ladder); **the final round transfers nothing** whatever its Status column says —
  the runner-up is marked "Rejected" but the count has already stopped, so instead
  of inventing a round the block names the ballots that stayed active to the end
  and still had a lower ranking go unread (the *nonexhausted-untransferred* case);
  and **STV gets no block at all**, because surplus transfers are fractional and
  are not modelled — silence beats a plausible wrong number. Verified against
  **RCTab 2.0.0**, which reports the same transfers and the same shrinking
  thresholds. Wording locked by `tests/test_irv_transfers.py`. Changing the block
  means re-running every ranked case (179 files) and rebuilding pages.
