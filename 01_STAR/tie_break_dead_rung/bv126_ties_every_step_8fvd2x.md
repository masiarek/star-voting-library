# BV126 — ties at every step (single-winner STAR) · issue [#1052](https://github.com/Equal-Vote/bettervoting/issues/1052)

*The worst case for the tie-break ladder: three candidates tie at **every** step, so the lot decides — and BetterVoting also drops the five flat ballots as abstentions. LH and BV agree on the winner (**Amy**), but only because the flat ballots can't change it.*

Reference files: [`bv126_ties_every_step_8fvd2x.yaml`](bv126_ties_every_step_8fvd2x.yaml) (`expected_winners: [Amy]`) · frozen export [`bv126_ties_every_step_8fvd2x_bv_export.json`](bv126_ties_every_step_8fvd2x_bv_export.json) (BV `8fvd2x`). Backs sheet row **BV126** (single-winner STAR, despite the sheet's "STAR Bloc" label).

## The election

Single-winner STAR, 3 candidates, 7 ballots — five of them flat `5,5,5`:

```
Amy,Brian,Chuck
3,2,1
5,5,5
5,5,5
1,2,3
5,5,5
5,5,5
5,5,5
```

Totals: **29 = 29 = 29**. A perfect three-way tie, and it stays tied at every rung.

## View 1 — BetterVoting

Elected **Amy**, `tieBreakType: "random"`, `perm` = [Amy, Chuck, Brian]. Its round-0 logs walk the whole ladder and hit the coin toss twice (once to pick the two finalists, once for the runoff):

```
score_tied                 Amy, Chuck, Brian  (all 4*)
pairwise_too_many_candidates
five_star_tied             Amy, Chuck, Brian  (0 votes*)
random_first  -> Amy       random_second -> Chuck     ← lot picks the finalists
runoff_tied / runoff_score_tie / runoff_five_star_tie
runoff_random -> Amy                                   ← lot picks the winner
```

`* nAbstentions: 5, nTallyVotes: 2` — BV counted **only the two non-flat ballots**, dropping the five `5,5,5` as abstentions (issue [#1052](https://github.com/Equal-Vote/bettervoting/issues/1052); same family as [#1407](https://github.com/Equal-Vote/bettervoting/issues/1407)). That's why its scores read `4-4-4` and five-star `0-0-0` instead of the real `29-29-29` / `5-5-5`.

## View 2 — the LH report (all seven ballots)

LH counts every ballot (the five flat ones register as Equal Support), yet still lands on the lot because the tie is genuine at every rung:

```
--- STAR Voting Method (single winner) ---
 Tabulating 7 ballots.

[Score Distribution]
       5  4  3  2  1  0  | Total
Amy    5  0  1  0  1  0  |   29
Brian  5  0  0  2  0  0  |   29
Chuck  5  0  1  0  1  0  |   29

Scoring Round
   Amy    -- 29 -- Tied for first place
   Brian  -- 29 -- Tied for first place
   Chuck  -- 29 -- Tied for first place
 There's a three-way tie for first.
Scoring Round: First tiebreaker (pairwise)
   Amy 2 ; Brian 2 ; Chuck 2 ; Equal Support 5     ← pairwise tied
Scoring Round: Second tiebreaker (most 5s)
   Amy 5 ; Brian 5 ; Chuck 5                        ← five-star tied
[Tiebreaker: Lot Number Priority]
  Tie among: ['Amy', 'Brian', 'Chuck']  →  Resolved: ['Amy', 'Chuck']   (lot [Amy, Chuck, Brian])

[Lot-decided tie — rare]  ⚠ the LOT chose the finalists, not the votes.

Automatic Runoff Round
   Amy 1 ; Chuck 1 ; Equal Support 5                ← runoff tied
   (score 29-29, five-star 5-5) → lot → Amy

Winner — STAR Voting Method (single winner)
 Amy
```

Full audit copy: [`tie_break_dead_rung_tabulated/bv126_ties_every_step_8fvd2x_tabulated.txt`](tie_break_dead_rung_tabulated/bv126_ties_every_step_8fvd2x_tabulated.txt).

## Two findings

1. **Flat ballots dropped (#1052).** BV tallies 2 of 7 (`nAbstentions: 5`), producing a wrong count and the misleading "no ballots"-style message. The five `5,5,5` ballots are real votes; LH keeps them (as Equal Support). The winner is unaffected — a flat ballot adds equally to everyone — but the reported turnout, percentages, and any quorum are wrong.
2. **Random tie-break → non-reproducible** (cf. [#1063](https://github.com/Equal-Vote/bettervoting/issues/1063) / [#1417](https://github.com/Equal-Vote/bettervoting/issues/1417)). The three-way tie is broken by a coin toss; BV drew Amy, but a different draw elects Brian or Chuck. `lot_numbers: [Amy, Chuck, Brian]` pins BV's draw so the reference is deterministic.

## Related

- [BV `jfk7pd`](lot_random_vs_published_jfk7pd/lot_random_vs_published_jfk7pd.md) and [BV131](../../02_STAR_Bloc/_main/bv131_guido_bloc.md) — the same random-tie phenomenon (single-winner and Bloc).
- [BV132](../../02_STAR_Bloc/_main/bv132_verify_votes_bloc.md) — the flat-ballot-drop bug in Bloc.
- [The "dead rung" case set](README.md) · [Flat scores, ties & tie-breaking](../Flat_scores_ties/README.md) — this case is the real-election version of both.
