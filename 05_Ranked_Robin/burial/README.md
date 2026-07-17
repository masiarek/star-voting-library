# 05_Ranked_Robin/burial — the worked burial pair

**Burial is to Condorcet methods what [center squeeze](../../00_start_here/topics/center_squeeze/README.md) is to IRV: the signature strategic wart.** Rank the frontrunner *last* — below candidates you honestly like less — manufacture a cycle, and win on the record. This repo shows IRV's wart loudly and often, so it shows Ranked Robin's the same way: a sincere election a compromise wins cleanly, and the coordinated lie that takes it from her. Live, triple-checked, deterministic on every engine.

**▶ Live on BetterVoting:**
- Part 1, sincere: [vote](https://bettervoting.com/7q6by8) · **[results ↗](https://bettervoting.com/7q6by8/results)** (election `7q6by8`, Test ID BV2208)
- Part 2, buried: [vote](https://bettervoting.com/fxhw6g) · **[results ↗](https://bettervoting.com/fxhw6g/results)** (election `fxhw6g`, Test ID BV2209)

## The electorate

A design club of 42 ranks four gemstones: **Amber**, **Beryl**, **Coral**, **Diamond**.

| Count | sincere ranking |
|:---:|---|
| 15 | Amber > **Beryl** > Coral > Diamond — *the buriers-to-be; Beryl is their honest second* |
| 12 | Beryl > Amber > Diamond > Coral |
| 9 | Coral > Diamond > Beryl > Amber |
| 6 | Diamond > Beryl > Coral > Amber |

## Part 1 — sincere: Beryl beats everyone

```text
Round-Robin — every pair, head-to-head (For – Against):
   Beryl    beats Amber     27 – 15
   Amber    beats Coral     27 – 15
   Amber    beats Diamond   27 – 15
   Beryl    beats Coral     33 –  9
   Beryl    beats Diamond   27 – 15
   Coral    beats Diamond   24 – 18

Win–loss record:
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  Beryl      3–0–0         3     +48  Amber, Coral, Diamond
    2  Amber      2–1–0         2     +12  Coral, Diamond
    3  Coral      1–2–0         1     -30  Diamond
    4  Diamond    0–3–0         0     -30  —

Winner — Ranked Robin (RCV-RR): Beryl
   beats every opponent head-to-head — the Condorcet winner.
```

Clean 3–0, no cycle, no tie. But look at **who builds Beryl's three wins**. Her 33–9 over Coral and her 27–15 over Diamond both contain the 15 Amber-first ballots — support those voters can *withdraw*. Her 27–15 over Amber contains none of them (they already rank Amber first). That accounting is the whole strategy.

## Part 2 — the burial: fifteen voters rank the leader last

The 15 Amber-first voters switch to `Amber > Coral > Diamond > Beryl` — Beryl, their honest second choice, now ranked below two gems they like less. That is burial, and its reach is exactly the buriers' own weight inside the victim's coalitions:

- Beryl over Coral, 33–9 → **flips to Coral 24–18** (15 of her 33 were the buriers).
- Beryl over Diamond, 27–15 → **flips to Diamond 30–12** (same reason).
- Beryl over Amber, 27–15 → **survives untouched** (zero burier ballots in it — they can't withdraw support they never gave).

```text
Round-Robin — every pair, head-to-head (For – Against):
   Amber    beats Coral     27 – 15
   Amber    beats Diamond   27 – 15
   Beryl    beats Amber     27 – 15
   Coral    beats Diamond   24 – 18
   Coral    beats Beryl     24 – 18
   Diamond  beats Beryl     30 – 12

Win–loss record:
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  Amber      2–1–0         2     +12  Coral, Diamond
    2  Coral      2–1–0         2      +0  Diamond, Beryl
    3  Diamond    1–2–0         1      +0  Beryl
    4  Beryl      1–2–0         1     -12  Amber

Winner — Ranked Robin (RCV-RR): Amber
   *** 2 candidates tie for the most wins (Amber, Coral) — a Condorcet cycle
   (no candidate beats all others). Resolved by total margin, then lot order.
```

Beryl falls from 3–0 to 1–2. Amber and Coral tie on top at 2–1 — and **Amber takes the tie on every metric**: total pairwise margin +12 vs 0 (the LH engine's rung), the direct head-to-head 27–15 (BetterVoting's rung), first choices 15 vs 9. Note the fine print of the mechanics: Amber *never beats Beryl directly* — the buriers can demolish Beryl's record but cannot flip her win over their own candidate. Burial wins through the standings, not the matchup.

**The buriers turned Beryl's win into Amber's win.** Their honest second choice lost to their first — mission accomplished, criterion violated (Ranked Robin, like every Condorcet method, fails strategic-nomination-adjacent honesty here; sincere ranking was not their best ballot).

## The triple-check

Per this repo's [cross-checking habit](../../00_start_here/tabulation_engines/cross_checking_with_pref_voting.md), both halves ran through three independent tabulators:

| Half | LH native | pref_voting Copeland | BetterVoting live |
|---|---|---|---|
| sincere | Beryl (3–0) | Beryl (unique leader) | **Beryl**, `tieBreakType: none` |
| buried | Amber (margin rung) | leader set {Amber, Coral} | **Amber**, `tieBreakType: none` |

The buried half stays freezable *despite* the known LH/BV tiebreak divergence ([rr_tiebreak_lh_vs_bv.md](../../00_start_here/RCV_Ranked_Robin/rr_tiebreak_lh_vs_bv.md)) because a **2-way** record tie resolves deterministically on both ladders — LH by total margin (+12 vs 0), BV by the direct head-to-head (27–15) — and both point at Amber. Contrast [BV2142](../clone_independence/bv2142_4gfwdq_clone_cycle_pre.md), where a **3-way** tie sent BetterVoting to a random draw. (One erratum for the record: the *live BV descriptions* of this pair carry a slim-vs-blowout aside that mislabels which wins flip; BV descriptions are permanent, so this page and the yamls are the corrected analysis.)

## Reading this fairly

- **Burial leaves fingerprints.** Sincere ballots showed no cycle; the buried ballots show one. A cycle appearing in a race whose polling showed a clear Condorcet winner *is* the anomaly — the printed round-robin table is where you'd catch it.
- **It needs a lot to go right:** a large bloc (here 15 of 42 — over a third of the electorate) sitting *inside* the leader's own majorities, coordination, decent polling, and a willingness to rank a liked candidate last. Fail any of those and the burial fizzles or backfires (bury into the wrong cycle and you elect Coral, the buriers' *third* choice — one mis-aim away).
- **Every method has its wart.** IRV: [center squeeze](../../00_start_here/topics/center_squeeze/README.md). STAR: the [runoff-born favorite-betrayal sliver](../../01_STAR/favorite_betrayal/README.md). Approval: the [threshold dilemma](../../01_STAR/exercises/ex13_draw_the_line.md). Ranked Robin and all Condorcet methods: burial. The honest comparison is *which warts are systematic and which need a heist* — this one is a heist, but a real one.

## Run it yourself

```
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 05_Ranked_Robin/burial/bv2208_7q6by8_burial_sincere.yaml
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 05_Ranked_Robin/burial/bv2209_fxhw6g_burial_pays.yaml
```

Sources: [bv2208_7q6by8_burial_sincere.yaml](bv2208_7q6by8_burial_sincere.yaml) · [bv2209_fxhw6g_burial_pays.yaml](bv2209_fxhw6g_burial_pays.yaml). Full mirrors: [`burial_tabulated/`](burial_tabulated/).

---

**Where this comes from.** Ballots and cast are this repo's own, built so the burial's anatomy is visible in the pairwise table (which wins the buriers sit inside, which they don't). Method home: [Ranked Robin](../README.md) · cycle handling: [cycle_resolution.md](../../00_start_here/RCV_Ranked_Robin/cycle_resolution.md) · the LH-vs-BV tiebreak caveat: [rr_tiebreak_lh_vs_bv.md](../../00_start_here/RCV_Ranked_Robin/rr_tiebreak_lh_vs_bv.md).

# file: README.md
