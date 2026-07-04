<!--
Ready-to-paste GitHub issue for  github.com/Equal-Vote/bettervoting  — UI only.

STATUS: NOT filed. This overlaps with existing coverage:
  * #1417 (the deterministic-lot report) already carries this as recommendation
    #3 ("Surface it in the UI"); and
  * #1379 mentions a missing human-readable tie-break explanation.
So this may be redundant. Keep as the fuller UI spec if a DEDICATED results-view
issue is wanted; otherwise its content can be pasted as a comment on #1379 (or
#1417 rec #3) rather than filed on its own.
When filing/commenting, you can drag-drop the two jfk7pd screenshots.
-->

---

**Title:** Results view doesn't disclose when a STAR winner was decided by a tie-break (and that it was random / non-reproducible)

### Summary

When a STAR result is decided by the tie-break rather than by the ballots, the
results page doesn't make that clear. The header says *"… won after tiebreaker"*
(with an ⓘ icon), but the main result — the score bars and the runoff — shows a
dead-even split with the winner starred, and nothing states **how** the tie was
broken, that the current method is a **random draw**, or that the outcome is
therefore **not reproducible** from the ballots. A voter looking at a 50%–50%
runoff with one candidate marked the winner has no way to know why.

This is a **reporting/UI** ask, distinct from making the tie-break deterministic
(the #1063 report). It's worth doing on its own — and it still matters after
#1063, because even a deterministic lot result should say "decided by lot order,
not by the votes."

### Evidence (election `jfk7pd`)

A real 2-candidate STAR election that tied at every rung (both score 4; runoff
1–1; no 5s), so the winner was drawn at random (`tieBreakType: "random"`,
`perm: [Ben, Ada]`, elected **Ben**).

What the results page shows:

- **Header:** "Ben won after tiebreaker" (+ ⓘ).
- **Scoring Round:** Ben 4, Ada 4.
- **Automatic Runoff:** Ben 50%, Ada 50%, with Ben starred as the winner.

What it does **not** show, at least inline:

- that the tie went all the way to a **random** tie-break (not a deterministic rule);
- **which** step fell through (pairwise → score → five-star → lot);
- the **drawn order** that produced this winner (`[Ben, Ada]`) — even though it's
  in the export (`perm` / `tieBreakOrder`);
- that **re-running the same ballots could elect Ada** (not reproducible under a
  random draw).

Screenshots (result bars and Race Details) and the full breakdown are here:
<https://github.com/masiarek/YAML/blob/master/01_STAR/tie_break_dead_rung/lot_random_vs_published_jfk7pd/lot_random_vs_published_jfk7pd.md>

### Proposed change (results view)

When a race's winner (or a finalist) was determined by the tie-break, surface a
short, plain-language disclosure inline — not only behind the ⓘ icon. For example:

> **Tie resolved by tie-break.** Ben and Ada tied on score (4–4) and in the runoff
> (50%–50%). The winner was chosen by the tie-break order **[Ben, Ada]**
> (currently a random draw), so **Ben** was selected. *Note: with a random draw
> this result is not reproducible from the ballots — see deterministic lot numbers
> (#1063).*

Nice-to-haves: name the rung that decided it ("five-star was 0–0, so the lot
decided"), and badge the runoff bar ("decided by tie-break") so the 50–50 split
isn't visually ambiguous.

### Acceptance criteria

- A race decided by any tie-break shows an inline notice on the results page
  stating (a) that a tie-break was used, (b) the method (random draw today; lot
  order after #1063), and (c) the resulting winner.
- The notice appears for both loci: a **scoring-round** tie (which finalist
  advanced) and an **automatic-runoff** tie (which finalist won).
- A race with a clean, ballot-decided winner shows **no** such notice (no false
  alarms).

### Relationship to other issues

- **#1379** — mentions a missing human-readable tie-break explanation; this issue
  scopes that specifically to the **results view** disclosure (and is happy to be
  folded into #1379 if maintainers prefer).
- **#1063** — deterministic, pre-published lot numbers (the tabulation fix). This
  UI change complements it and is useful before and after it lands.
- **#1371** (closed) — the export already carries the drawn order, so the data
  needed for this disclosure is already available.

### Further reading (background docs)

- Worked example, both views (BV screenshots + the independent report):
  <https://github.com/masiarek/YAML/blob/master/01_STAR/tie_break_dead_rung/lot_random_vs_published_jfk7pd/lot_random_vs_published_jfk7pd.md>
- STAR tie-breaking — the full chain (the ladder + the "dead rung"):
  <https://github.com/masiarek/YAML/blob/master/00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md>
