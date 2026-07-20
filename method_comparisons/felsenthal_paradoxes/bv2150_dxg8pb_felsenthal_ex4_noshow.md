# BV2150 — Felsenthal Example 4 (1 of 2): everyone votes, and their worst choice wins

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/dxg8pb) · **[results ↗](https://bettervoting.com/dxg8pb/results)** (election `dxg8pb`).

11 voters, three candidates. The four `Andy>Beth>Carl` voters all show up and vote sincerely — and get **Carl**, their *last* choice. Part 2 ([BV2151](bv2151_97hbpw_felsenthal_ex4_noshow.md)) shows the sting: had two of them stayed home, their side would have gotten Beth. Three races on the same electorate: Runoff/IRV → **Carl**; Ranked Robin → **Beth**; STAR → **Beth**.

## Source

Dan S. Felsenthal, *"Review of Paradoxes Afflicting Various Voting Procedures Where One Out of m Candidates (m ≥ 2) Must Be Elected"*, University of Haifa / LSE, revised 26 May 2010 (Leverhulme Trust *Voting Power in Practice* workshop, Château du Baffy, Normandy). Appendix §A2, **Example 4** — demonstrating the No-Show and (weak) Twin paradoxes.

## The election

```
No. of voters    Preference ordering
      4          Andy > Beth > Carl
      3          Beth > Carl > Andy
      1          Carl > Andy > Beth
      3          Carl > Beth > Andy
```

First choices: **Andy 4, Beth 3, Carl 4** — no majority, so plurality-with-runoff (= IRV for three candidates) deletes **Beth**, and Carl beats Andy **7–4**. Meanwhile **Beth is the Condorcet winner** (beats Andy 6–5, Carl 7–4) — so the runoff race also exhibits the [Condorcet winner paradox](../../00_start_here/voting_paradoxes/condorcet_winner_paradox.md), electing Carl, whom Beth beats 7–4.

## The paradoxes this pair demonstrates

The **[No-Show paradox](../../00_start_here/voting_paradoxes/no_show.md)** (conditional): the four `Andy>Beth>Carl` voters would have done *better* if two of them hadn't voted — see [BV2151](bv2151_97hbpw_felsenthal_ex4_noshow.md), where the same procedure elects Beth. The **Twin paradox** (weak form) is the same pair read forward: start from the 9-voter electorate and add two "twins" identical to the Andy pair — their arrival elects Carl, the twins' common worst choice. Both live on one teaching page: [no_show.md](../../00_start_here/voting_paradoxes/no_show.md).

## View 1 — BetterVoting

Live results: **[bettervoting.com/dxg8pb/results ↗](https://bettervoting.com/dxg8pb/results)**. BV elects **Carl** (IRV), **Beth** (Ranked Robin), **Beth** (STAR) — matching LH on all three, no tiebreaks.

## View 2 — LH engine

Runoff/IRV race ([bv2150_dxg8pb_irv.yaml](cases/bv2150_dxg8pb_irv.yaml)):

```
 Tabulating 11 ballots (ranked ballots).

ROUND 1
Candidate      Votes  Status
-----------  -------  --------
Carl               4  Hopeful
Andy               4  Hopeful
Beth               3  Rejected

FINAL RESULT
Candidate      Votes  Status
-----------  -------  --------
Carl               7  Elected
Andy               4  Rejected
Beth               0  Rejected

Winner(s) — RCV / Instant-Runoff Voting (single winner)
  Carl
```

Ranked Robin ([bv2150_dxg8pb_ranked_robin.yaml](cases/bv2150_dxg8pb_ranked_robin.yaml)) elects **Beth** — 2 pairwise wins (6–5, 7–4), the Condorcet winner. STAR ([bv2150_dxg8pb_star.yaml](cases/bv2150_dxg8pb_star.yaml)) with the 5/3/1 map: **Andy 29, Beth 37, Carl 33**; Beth wins the automatic runoff **7–4**. Full detail: [IRV mirror](cases/cases_tabulated/bv2150_dxg8pb_irv_tabulated.txt) · [RR mirror](cases/cases_tabulated/bv2150_dxg8pb_ranked_robin_tabulated.txt) · [STAR mirror](cases/cases_tabulated/bv2150_dxg8pb_star_tabulated.txt).

## Agreement

| Race | BetterVoting | LH engine | Agree? |
|---|---|---|---|
| Runoff (IRV) | Carl | Carl | ✓ |
| Ranked Robin | Beth | Beth | ✓ |
| STAR (ranks→scores) | Beth | Beth | ✓ |

Frozen export: [bv2150_dxg8pb_bv_export.json](cases/bv2150_dxg8pb_bv_export.json) · Part 2: [BV2151 — two supporters stay home](bv2151_97hbpw_felsenthal_ex4_noshow.md).
