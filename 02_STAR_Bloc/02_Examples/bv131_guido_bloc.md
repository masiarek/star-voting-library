# BV131 — Guido example (Bloc STAR): a hidden lot-decided tie

<!-- case-meta:start — managed by build_yaml_pages.py; edit the YAML, not these lines -->
**Method:** [Bloc STAR (multi-winner, majoritarian)](../../03_STAR_PR/01_Learn) · **2 seats** · **Expected winners:** Cand2, Cand3 · [full count →](cases/cases_pages/bv131_guido_bloc.md)
<!-- case-meta:end -->

*Marked "Passed" in the sheet, but seat 1 is a **perfect lot-decided tie** — the Bloc analog of [`jfk7pd`](../../01_STAR/03_Criteria/tie_break_dead_rung/lot_random_vs_published_jfk7pd/lot_random_vs_published_jfk7pd.md). BetterVoting broke it with a random draw (Cand2), and — the reporting catch — its top-level `tieBreakType` says "none" anyway.*

Reference files: [`bv131_guido_bloc.yaml`](cases/bv131_guido_bloc.yaml) (`expected_winners: [Cand2, Cand3]`) · frozen export [`bv131_guido_bloc_bv_export.json`](cases/bv131_guido_bloc_bv_export.json) (BV `kbh3d9`). Backs sheet row **BV131**.

## The election

Bloc STAR, 3 candidates, 2 seats. Totals: Cand1 = 6, Cand2 = 6, Cand3 = 5.

```
Cand1,Cand2,Cand3
1,5,2
0,0,1
5,1,2
```

## View 1 — BetterVoting

Elected **Cand2, Cand3**. BV's own round-0 logs walk the whole ladder and end at a coin toss:

```
advance_to_runoff_same_score   Cand2, Cand1   (both 6)
runoff_tied                    Cand2, Cand1   (1–1, 1 equal)
runoff_score_tie               Cand2, Cand1   (6–6)
runoff_five_star_tie           Cand2, Cand1   (1–1)
runoff_random                  winner: Cand2          ← coin toss
```

`perm` shows the draw put **Cand2** ahead of Cand1. **But the result's top-level `tieBreakType` is `"none"`** — even though round 0's own `tieBreakType` is `"random"`. A reader of the summary can't tell seat 1 was decided by chance.

## View 2 — the LH report (reproducing BV's draw)

Pinning the lot order to BV's drawn sequence `[Cand2, Cand1, Cand3]` reproduces Cand2. Every deterministic rung ties; the lot decides; the engine flags it:

--8<-- "02_STAR_Bloc/02_Examples/cases/cases_pages/bv131_guido_bloc.md:report"
Full audit copy: [`_main_tabulated/bv131_guido_bloc_tabulated.txt`](cases/cases_tabulated/bv131_guido_bloc_tabulated.txt).

## Two findings

1. **Non-reproducible (cf. [#1063](https://github.com/Equal-Vote/bettervoting/issues/1063) / [#1417](https://github.com/Equal-Vote/bettervoting/issues/1417)).** With the column-order fallback (no lot order) LH elects **Cand1** for seat 1, not Cand2 — same ballots, different winner, decided only by the tie-break order. BV's `random` draw happened to pick Cand2.
2. **Reporting mislabel.** The result's top-level `tieBreakType: "none"` contradicts round 0's `tieBreakType: "random"`. The summary should surface that a seat was lot-decided (cf. [#1379](https://github.com/Equal-Vote/bettervoting/issues/1379) and the results-view transparency ask). So "Passed" is optimistic — the winner was a coin toss, undisclosed at the top level.

## Related

- [BV `jfk7pd`](../../01_STAR/03_Criteria/tie_break_dead_rung/lot_random_vs_published_jfk7pd/lot_random_vs_published_jfk7pd.md) — the single-winner original of this exact phenomenon.
- [STAR Tie-Breaking — The Full Chain](../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md).
- [#904](https://github.com/Equal-Vote/bettervoting/issues/904) — the export also labels `votingMethod: "STAR"`, not "Bloc STAR".
