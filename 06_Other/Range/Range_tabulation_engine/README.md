# Range / Score voting tabulation engine

Tabulates **Range (Score) voting**: every voter grades each candidate on a fixed
0..max scale; the candidate with the **highest total score wins**. No runoff, no
elimination — just sum the grades.

## Engine choice — pref_voting

This wraps **[pref_voting](https://pref-voting.readthedocs.io)** (Eric Pacuit)
via its native `grade_methods.score_voting`. pref_voting was chosen over Votelib
and VoteKit because it is **already this repo's independent cross-check engine**
(see [the pref_voting engine](../../../STARVote_LH_tabulation_engine/tools_adam/pref_voting_tabulation_engine/))
— so range tabulation adds **no new dependency** and reuses an actively-maintained,
well-tested library. Range itself is trivial ("sum the scores"), so we also
compute the totals **by hand and assert the two agree**: the result is
reproducible *and* independently verified. If pref_voting isn't installed the
hand count still runs (the cross-check is skipped with a note).

## Usage

```bash
python 06_Other/Range/Range_tabulation_engine/range_tabulation.py <election.yaml>
```

Reads the library's usual score grid (header row of names, then one 0–max row
per voter; `N ×` / `N:` weights and markers handled). It ignores `voting_method:`
— any score ballot can be read as Range. It writes a full-context
`<stem>_RANGE_tabulated.txt` into the source folder's `<folder>_tabulated/`
mirror (the `RANGE` suffix keeps it from colliding with a STAR mirror of the
same election).

## Where Range sits among the methods

- **Approval** is Range at 1-bit resolution (grades restricted to `{0, max}`).
- **STAR** is Range's score round **plus an automatic runoff** — added precisely
  to fix Range's strategy problem (see below).
- Range is the most *expressive* single-mark method but the most
  **strategy-exposed**: a voter's rational play is often to give max/min only
  (which collapses Range toward Approval). STAR's runoff is the standard answer.

See the teaching page [`00_start_here/Range_Voting/range_voting.md`](../../../00_start_here/Range_Voting/range_voting.md)
for the method overview, pros/cons, and ballot examples, and the
[Black Curtain read as Range](../../../method_comparisons/black_curtain/black_curtain_range.md).
Range is a **non-EVC** method, so its examples live in
[other methods](../../), not a numbered
root folder.

# file: README.md
