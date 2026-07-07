# BV2147 — Felsenthal Example 3 (I of III): District I elects Bruno

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/9gdrqg) · **[results ↗](https://bettervoting.com/9gdrqg/results)** (election `9gdrqg`).

District I of the Reinforcement-paradox trio (source and full story: **[BV2149 — the combined election](bv2149_byk9v2_felsenthal_ex3_reinforcement.md)**; Felsenthal 2010, Appendix §A2, Example 3). 17 voters:

```
No. of voters    Preference ordering
      4          Alma  > Bruno > Cora
      1          Bruno > Alma  > Cora
      5          Bruno > Cora  > Alma
      6          Cora  > Alma  > Bruno
      1          Cora  > Bruno > Alma
```

No first-round majority (Alma 4, Bruno 6, Cora 7), so plurality-with-runoff (= IRV for three candidates) deletes **Alma**, and **Bruno beats Cora 10–7**. STAR on the same ballots (5/3/1 map: 47/51/55) also elects **Bruno**, runoff 10–7. BV confirms both ([results ↗](https://bettervoting.com/9gdrqg/results)); LH agrees, no tiebreaks.

Worth noticing: this district's pairwise preferences are a Condorcet **cycle** — Alma>Bruno 10–7, Bruno>Cora 10–7, Cora>Alma 12–5 — so no Condorcet winner exists here. (That's also why the trio carries no Ranked Robin race: BV would break the cyclic tie at random, which can't be frozen.)

Bruno also wins [District II](bv2148_h87k6v_felsenthal_ex3_district2.md) outright — and then [the combined electorate](bv2149_byk9v2_felsenthal_ex3_reinforcement.md) elects Alma. Teaching page: [multiple_districts.md](../../00_start_here/voting_paradoxes/multiple_districts.md).

Files: [bv2147_9gdrqg_irv.yaml](bv2147_9gdrqg_irv.yaml) · [bv2147_9gdrqg_star.yaml](bv2147_9gdrqg_star.yaml) · [frozen export](bv2147_9gdrqg_bv_export.json) · mirrors: [IRV](felsenthal_paradoxes_tabulated/bv2147_9gdrqg_irv_tabulated.txt), [STAR](felsenthal_paradoxes_tabulated/bv2147_9gdrqg_star_tabulated.txt).
