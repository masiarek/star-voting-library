# BV2149 — Felsenthal Example 3 (III of III): Bruno won both districts; Alma wins the whole

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/byk9v2) · **[results ↗](https://bettervoting.com/byk9v2/results)** (election `byk9v2`).

Bruno wins District I ([BV2147](bv2147_9gdrqg_felsenthal_ex3_district1.md)). Bruno wins District II ([BV2148](bv2148_h87k6v_felsenthal_ex3_district2.md)) — outright, with a first-round majority. Put the two electorates together, change nothing else, and plurality-with-runoff elects **Alma**. That is the **Reinforcement paradox** (multiple-districts / inconsistency paradox): the procedure disagrees with itself when electorates that agree are combined.

## Source

Dan S. Felsenthal, *"Review of Paradoxes Afflicting Various Voting Procedures Where One Out of m Candidates (m ≥ 2) Must Be Elected"*, University of Haifa / LSE, revised 26 May 2010 (Leverhulme Trust *Voting Power in Practice* workshop, Château du Baffy, Normandy). Appendix §A2, **Example 3**.

## The three electorates

Felsenthal's *a, b, c* → cast as **Alma, Bruno, Cora** (same cast across the trio — it's one story):

```
District I (17)                District II (15)               Combined (32)
 4  Alma  > Bruno > Cora        6  Alma  > Cora  > Bruno       4  Alma  > Bruno > Cora
 1  Bruno > Alma  > Cora        8  Bruno > Cora  > Alma        6  Alma  > Cora  > Bruno
 5  Bruno > Cora  > Alma        1  Cora  > Alma  > Bruno       1  Bruno > Alma  > Cora
 6  Cora  > Alma  > Bruno                                     13  Bruno > Cora  > Alma
 1  Cora  > Bruno > Alma                                       7  Cora  > Alma  > Bruno
                                                               1  Cora  > Bruno > Alma
```

Under plurality-with-runoff (= IRV for three candidates): District I has no first-round majority (4/6/7) → Alma deleted → **Bruno beats Cora 10–7**. District II: **Bruno wins round one** (8 of 15, an absolute majority). Combined: no majority (Alma 10, Bruno 14, Cora 8) → **Cora** deleted → **Alma beats Bruno 17–15**.

## Why this is the Reinforcement paradox

The Reinforcement postulate says: if two disjoint electorates each elect X, their union must elect X. Both districts elected Bruno; the union elects Alma. Nothing subjective is needed to call this wrong — the procedure contradicts *its own* two verdicts. The mechanism is the elimination step again: amalgamation flips *who gets deleted* (Alma in District I, Cora in the combined count), and the deletion decides the final pair. Teaching page: [multiple_districts.md](../../00_start_here/voting_paradoxes/multiple_districts.md).

A subtlety the case pages flag: District I and the Combined electorate are Condorcet **cycles** (combined: Alma>Bruno 17–15, Bruno>Cora 18–14, Cora>Alma 21–11), so there's no "true winner" to appeal to — which is exactly why the paradox is stated as self-inconsistency, not as missing a Condorcet winner. (District II does have a Condorcet winner: Bruno. No Ranked Robin races in this trio — BV would resolve the cyclic ties at random, which can't be frozen; see the [BV2142 caveat](../../05_Ranked_Robin/clone_independence/bv2142_4gfwdq_clone_cycle_pre.md).)

## STAR on the same ballots

Ranks mapped 5/3/1. Combined: **Alma 88, Bruno 98, Cora 102** — Cora and Bruno advance, **Bruno wins the runoff 18–14**. With Districts I and II also electing Bruno ([BV2147](bv2147_9gdrqg_felsenthal_ex3_district1.md): 47/51/55, runoff 10–7; [BV2148](bv2148_h87k6v_felsenthal_ex3_district2.md): 41/47/47, runoff 8–7), STAR is consistent across all three counts *in this election* — though runoff-bearing methods are not reinforcement-proof in general.

## View 1 — BetterVoting

Live results: **[bettervoting.com/byk9v2/results ↗](https://bettervoting.com/byk9v2/results)**. BV elects **Alma** (IRV) and **Bruno** (STAR) — matching LH, no tiebreaks.

## View 2 — LH engine

Runoff/IRV race ([bv2149_byk9v2_irv.yaml](bv2149_byk9v2_irv.yaml)):

```
 Tabulating 32 ballots (ranked ballots).

ROUND 1
Candidate      Votes  Status
-----------  -------  --------
Bruno             14  Hopeful
Alma              10  Hopeful
Cora               8  Rejected

FINAL RESULT
Candidate      Votes  Status
-----------  -------  --------
Alma              17  Elected
Bruno             15  Rejected
Cora               0  Rejected

Winner(s) — RCV / Instant-Runoff Voting (single winner)
  Alma
```

STAR race ([bv2149_byk9v2_star.yaml](bv2149_byk9v2_star.yaml)) → **Bruno** (102/98/88; runoff 18–14). Full detail: [IRV mirror](felsenthal_paradoxes_tabulated/bv2149_byk9v2_irv_tabulated.txt) · [STAR mirror](felsenthal_paradoxes_tabulated/bv2149_byk9v2_star_tabulated.txt).

## Agreement

| Election | Race | BetterVoting | LH engine | Agree? |
|---|---|---|---|---|
| BV2147 District I | Runoff (IRV) | Bruno | Bruno | ✓ |
| BV2147 District I | STAR | Bruno | Bruno | ✓ |
| BV2148 District II | Runoff (IRV) | Bruno | Bruno | ✓ |
| BV2148 District II | STAR | Bruno | Bruno | ✓ |
| BV2149 Combined | Runoff (IRV) | **Alma** | **Alma** | ✓ |
| BV2149 Combined | STAR | Bruno | Bruno | ✓ |

Frozen export: [bv2149_byk9v2_bv_export.json](bv2149_byk9v2_bv_export.json) · The districts: [BV2147](bv2147_9gdrqg_felsenthal_ex3_district1.md) · [BV2148](bv2148_h87k6v_felsenthal_ex3_district2.md).
