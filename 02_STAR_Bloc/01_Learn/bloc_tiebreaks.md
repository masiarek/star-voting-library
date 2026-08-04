# Ties in Bloc STAR

**One line:** Bloc STAR has no tiebreak rules of its own — it runs [STAR's ladder](../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md) once per seat. What *is* new is the consequence: because each seat is decided in the field the previous seat left behind, a tie broken at seat 1 can change **who wins seat 2**, not merely the order the winners are announced in.

→ The ladder itself: [STAR Tie-Breaking — The Full Chain](../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md) · the mechanics: [Bloc STAR](bloc_star.md) · the case index: [02_STAR_Bloc](../README.md#the-reference-cases)

**Level: 301 · deep dive**

---

## The ladder, briefly

Unchanged from single-winner STAR, and worth re-reading [in full](../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md) rather than from memory:

```text
SCORING ROUND  — tie for the last finalist slot?
  1. PAIRWISE   2. FIVE-STAR   3. LOT ORDER

AUTOMATIC RUNOFF  — the two finalists tied?
  1. SCORE      2. FIVE-STAR   3. LOT ORDER
```

Each round breaks its tie with the *other* round's yardstick, because the measure that tied can't be the one that separates. In a Bloc race this whole apparatus runs **once per seat**, independently — so a 4-seat election can break four ties, in eight different places, by two different rules.

## The Bloc-specific consequence: a seat-1 tie is not confined to seat 1

Here is the part that has no single-winner analogue. Three candidates, two seats, five ballots. Nadia and Omar tie at 15 points; Priya trails at 12. The seat-1 runoff is a dead heat and *every* deterministic rung ties behind it:

--8<-- "02_STAR_Bloc/02_Examples/cases/cases_pages/bloc_lot_path_dependence_b_c3_b5.md:report"
So the lot decides seat 1. Run the same five ballots under the two possible lot orders:

| Published lot | Seat 1 | Seat 2 | **Council** |
|---|---|---|---|
| `[Nadia, Omar, Priya]` | Nadia (by lot) | **Priya** beats Omar 2–1 | **Nadia, Priya** |
| `[Omar, Nadia, Priya]` | Omar (by lot) | **Nadia** beats Priya 3–2 | **Omar, Nadia** |

**Priya sits on the council in one run and not the other, and no ballot changed.** The lot did not reorder the winners; it picked a different set of them.

Why the two seat-2 runoffs go opposite ways: Omar and Priya are scored **5/5** by the two ballots that would otherwise separate them, so Omar carries only 1 of the 3 ballots that express a preference. Nadia and Priya are never tied on any ballot, and Nadia takes 3 of 5. Two near-identical candidates, opposite results against the same third one — which is exactly the kind of asymmetry the removal step exposes.

Run it: [lot A](../02_Examples/cases/cases_pages/bloc_lot_path_dependence_a_c3_b5.md) ([yaml](../02_Examples/cases/bloc_lot_path_dependence_a_c3_b5.yaml)) · [lot B](../02_Examples/cases/cases_pages/bloc_lot_path_dependence_b_c3_b5.md) ([yaml](../02_Examples/cases/bloc_lot_path_dependence_b_c3_b5.yaml))

Contrast a **top-N** method — [Bloc Approval, SNTV, Bloc Ranked Robin](bloc_star_vs_other_bloc_methods.md) all produce one ranking and cut it at N, so a tie there can only ever swap the **last** seat. Bloc STAR is the one at-large method where a coin toss propagates.

## The dead rung, and its opposite

The five-star rung counts votes of the **scale maximum** — literally `score == 5`. Two ways it fails to help, and this repo has a case for each:

- **Inert.** If neither tied candidate holds a single 5, the rung runs, prints `0 – 0`, and settles nothing — the [dead rung](../../01_STAR/01_Learn/Tie_Breaking_STAR/dead_rung_note_for_equal_vote.md). [BV130-r2](../02_Examples/bv130r2_dead_rung_bloc.md) is built for it: six candidates capped at 4, so Ada and Dan tie 15–15 with five-star counts of 0 and 0, and seat 1 goes to the lot.
- **Live and still tied.** In the Nadia/Omar case above both candidates hold **three** 5s. The rung had plenty to weigh and weighed it to a draw. The engine's warning text guesses "usually the dead rung" and tells you to check the counts — do check them, because "the lot decided" and "the five-star rung was empty" are not the same finding.

A lot-decided seat is genuinely rare in a real election. It is *not* rare in a small teaching file, and it is not rare in a race where nobody uses the top of the scale.

## What BetterVoting reports — read the export, not the banner

The Bloc case set is largely a set of tie probes against BetterVoting, and the recurring finding is a **reporting** one rather than a counting one. BV's ordering data is complete and reproducible: the export publishes `perm` (candidates in tiebreak order), each candidate's `tieBreakOrder`, and the `tied[]`/`other[]` lists, and pinning `lot_numbers` to BV's `perm` replays the draw exactly.

The summary on top of it is what misleads:

- **[BV131](../02_Examples/bv131_guido_bloc.md)** — seat 1 is decided by lot, the election is marked "Passed", and the top-level `tieBreakType` reads `none`. Nothing on the results page says a coin was tossed.
- **[BV130-r2](../02_Examples/bv130r2_dead_rung_bloc.md)** — same shape: a genuine random draw settled seat 1 (`perm` puts Dan ahead of Ada), `tieBreakType` still `none`.

So when a Bloc result matters, **read the export's `perm` and `tieBreakOrder`, not the banner.** A reader who trusts `tieBreakType` will believe an election was decided by voters when it was decided by a shuffle.

Two adjacent BV defects the same case set turned up, worth knowing because they change the *count* rather than the label: flat / no-preference ballots being dropped entirely ([BV132](../02_Examples/bv132_verify_votes_bloc.md), [#1073](https://github.com/Equal-Vote/bettervoting/issues/1073)) and an all-identical-ballot election tallying `nTallyVotes: 0` ([BV750](../02_Examples/bv750_tie_breaking_bloc.md), [#1052](https://github.com/Equal-Vote/bettervoting/issues/1052)).

## Reading a Bloc result for ties

1. **Which seat, not whether.** "There was a tie" is not enough — ask which seat it was on, because a seat-1 tie is the one that can move later seats.
2. **Check the tied candidates' five-star counts** before crediting or blaming the rung.
3. **Publish the lot before the ballots.** That is what makes a lot-decided seat auditable instead of merely asserted: `lot_numbers:` in the YAML, `perm` in a BV export.
4. **The seat order is evidence.** It tells you where in the sequence the count stopped being determined by the votes.

## See also

- [STAR Tie-Breaking — The Full Chain](../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md) · [the dead rung](../../01_STAR/01_Learn/Tie_Breaking_STAR/dead_rung_note_for_equal_vote.md) · [BV JSON → YAML mapping](../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking_JSON.md)
- [The Bloc reference cases](../README.md#the-reference-cases) — the full BV id → tie type → issue table
- [Ties](../../07_Concepts/topics/ties/) — the cross-method topic hub
- [Bloc STAR](bloc_star.md) · [honest limits](bloc_honest_limits.md)
