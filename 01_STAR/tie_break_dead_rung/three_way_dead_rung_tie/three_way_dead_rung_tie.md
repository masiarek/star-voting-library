# Three candidates, three possible winners — the dead rung scales

*The 3-candidate analog of the BetterVoting `jfk7pd` case. Same phenomenon, one more candidate: a perfectly symmetric tie that no rung can break, so the lot decides — and now there are **three** winners it could pick.*

Backing files: [`_A`](three_way_dead_rung_A.yaml) (elects A) · [`_B`](three_way_dead_rung_B.yaml) (elects B) · [`_C`](three_way_dead_rung_C.yaml) (elects C). Parent set: [The "dead rung"](../README.md).

---

## The ballots

Three voters, each an exact rotation of the others (a "Condorcet-cycle-style" rock-paper-scissors of scores), capped at 4 so **nobody scores a 5**:

```
A, B, C
4, 0, 0     # voter 1 loves A
0, 4, 0     # voter 2 loves B
0, 0, 4     # voter 3 loves C
```

- **Totals:** A = B = C = **4** — a three-way tie for the two finalist slots.
- **Pairwise:** every head-to-head is **1–1** (each candidate beats one rival on one ballot, loses to the other on another, ties on the third).
- **Five-star:** all **0** — a **dead rung** (nobody used the scale max).

Nothing on the ballots distinguishes A, B, or C. The result is decided **entirely by the lot order**:

| Published lot order | Winner |
|---------------------|:------:|
| `[A, B, C]` | **A** |
| `[B, C, A]` | **B** |
| `[C, A, B]` | **C** |

All three verified against the engine. A **random** tie-break (BetterVoting's `tieBreakType: "random"`) would draw one of the three; a **deterministic published** lot fixes it in advance.

---

## Were you surprised two candidates was enough? Here's why more doesn't help.

The lot-decided tie has nothing to do with the *number* of candidates — it's about **symmetry among the tied set**. A tie reaches the lot whenever the ballots can't separate the tied candidates at *any* deterministic rung (pairwise, then five-star). Two candidates was enough because two mirror-image ballots are already perfectly symmetric. Adding candidates doesn't remove that possibility; it just changes the flavors:

1. **The mechanism is identical.** With `k` perfectly-tied candidates, every rung comes back equal and the lot picks the winner. 2, 3, 10 — same story.

2. **A bigger tied set makes the divergence *more* likely, not less.** A random draw agrees with a fixed published order only when it happens to put the same candidate first — probability `1/k`. So a re-count disagrees with probability **`(k − 1)/k`**: 50% for 2 tied, **67% for 3**, 75% for 4, 80% for 5. More tied candidates ⇒ *worse* reproducibility, not better.

3. **More candidates open a *second* place for the lot to bite.** With only two candidates, both are automatically finalists, so the tie can only happen in the runoff. With three or more, the lot can also decide **which two candidates become finalists** (the scoring-round tie) — and that choice can change who ultimately wins. (See the scoring-round dead-rung cases and the adversarial ones in the [parent folder](../README.md).)

4. **The one thing that *does* change: exact ties get rarer by accident.** A perfect tie needs engineered symmetry, and that's harder to hit unintentionally with more candidates and more voters. But "rare" isn't "impossible" — and when it happens in a real public election, a random tie-break means the certified winner isn't reproducible from the ballots. That's the whole point of a **pre-published, deterministic lot** (BetterVoting issue [#1063](https://github.com/Equal-Vote/bettervoting/issues/1063)).

**Bottom line:** more candidates never *fix* the issue — at best they make an accidental tie less frequent, and when a tie does occur they can make the random draw diverge *more* often and in *more* places (finalists as well as the winner).

---

## Reproduce

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py \
  01_STAR/tie_break_dead_rung/three_way_dead_rung_tie/three_way_dead_rung_A.yaml   # -> A
# swap _A for _B (-> B) or _C (-> C): same ballots, different lot, different winner
```

To try it in BetterVoting: build a STAR election with three candidates and these three ballots, export the JSON, and run it through the two-way importer — the same tool used for `jfk7pd` will show BV's drawn winner vs a published-order winner:

```bash
python STARVote_LH_tabulation_engine/tools_adam/two_way_import.py <export.json> --published "A, B, C"
```

Related: the real 2-candidate BetterVoting case [BV `jfk7pd`](../lot_random_vs_published_jfk7pd/lot_random_vs_published_jfk7pd.md) · the [dead-rung concept + cap ladder](../README.md) · generator [`generate_dead_rung_scenarios.py`](../../../STARVote_LH_tabulation_engine/tools_adam/generate_dead_rung_scenarios.md).
