---
search:
  exclude: true
---

# BV2208 — Burial in Ranked Robin (1/2): sincere ballots, Beryl beats everyone

*Generated from [`bv2208_7q6by8_burial_sincere.yaml`](../bv2208_7q6by8_burial_sincere.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../../01_Learn/README.md) · **1 seat** · **Expected winner:** Beryl

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/7q6by8) · **[results ↗](https://bettervoting.com/7q6by8/results)** (election `7q6by8` · test `BV2208`).

## Scenario

The sincere half of the repo's worked BURIAL pair — Ranked Robin's signature strategic wart, shown honestly (burial is to Condorcet methods what center squeeze is to IRV). A design club of 42 ranks four gemstones. Beryl is the Condorcet winner: 27-15 over Amber, 33-9 over Coral, 27-15 over Diamond — a clean 3-0 record, no cycle, no tie. Amber runs second at 2-1. Look at WHO builds Beryl's three wins: her 33-9 over Coral and 27-15 over Diamond both contain the 15 Amber-first ballots — support those voters can withdraw — while her 27-15 over Amber contains none of them (they already rank Amber first). Part 2 (bv2209_fxhw6g_burial_pays.yaml) is exactly that withdrawal: rank Beryl LAST, flip the two wins she borrowed, keep the one she owns. Triple-checked: LH native, pref_voting Copeland (unique winner), BetterVoting live (Beryl, no tiebreak). (The live BV description's slim-vs-blowout aside mischaracterizes which wins flip — this file and the case README are the corrected analysis.) Live results: https://bettervoting.com/7q6by8/results

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
15:Amber>Beryl>Coral>Diamond
12:Beryl>Amber>Diamond>Coral
9:Coral>Diamond>Beryl>Amber
6:Diamond>Beryl>Coral>Amber
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
--- Ranked Robin (RCV-RR / Copeland) Method (single winner) ---
 Tabulating 42 ballots (ranked ballots).

Ballots:
    15 × Amber > Beryl > Coral > Diamond
    12 × Beryl > Amber > Diamond > Coral
     9 × Coral > Diamond > Beryl > Amber
     6 × Diamond > Beryl > Coral > Amber

Round-Robin — every pair, head-to-head (For – Against):
   Beryl    beats Amber     27 – 15
   Amber    beats Coral     27 – 15
   Amber    beats Diamond   27 – 15
   Beryl    beats Coral     33 –  9
   Beryl    beats Diamond   27 – 15
   Coral    beats Diamond   24 – 18

--- Pairwise (Round-Robin) Matrix ---
Head-to-head / pairwise comparison — the Ranked Robin tally
Legend: For - Equal Support - Against   (row vs column)
            |    Amber     |   Beryl     |   Coral     |  Diamond    |
----------------------------------------------------------------------
    Amber > |     ---      |15 -  0 - 27 |27 -  0 - 15 |27 -  0 - 15 |
    Beryl > | 27 -  0 - 15 |    ---      |33 -  0 -  9 |27 -  0 - 15 |
    Coral > | 15 -  0 - 27 | 9 -  0 - 33 |    ---      |24 -  0 - 18 |
  Diamond > | 15 -  0 - 27 |15 -  0 - 27 |18 -  0 - 24 |    ---      |

Win–loss record — Copeland score = wins + ½·ties (highest score wins; ties broken by the Ranked Robin degrees, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  Beryl      3–0–0         3     +48  Amber, Coral, Diamond
    2  Amber      2–1–0         2     +12  Coral, Diamond
    3  Coral      1–2–0         1     -30  Diamond
    4  Diamond    0–3–0         0     -30  —

Winner — Ranked Robin (RCV-RR): Beryl
   beats every opponent head-to-head — the Condorcet winner.
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Smith Set (the generalized Condorcet winner) ---
The smallest group whose every member beats every candidate outside it —
the honest answer to "who is even in contention?".
   Smith set (1 of 4): Beryl
   Outside (3):        Amber, Coral, Diamond
   One member ⇒ Beryl is the Condorcet winner, beating every rival head-to-head.
   Ranked Robin (RCV-RR) winner Beryl is INSIDE the Smith set. ✓
      Guaranteed: Ranked Robin (Copeland) is Smith-efficient — every member of
      the set outscores every outsider, so the top of the win–loss table is
      always inside the set, however the tie among them is then broken.
   More: 07_Concepts/topics/smith_set.md
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/bv2208_7q6by8_burial_sincere_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 05_Ranked_Robin/03_Criteria/burial/cases/bv2208_7q6by8_burial_sincere.yaml
```

## See also

- [Center squeeze (topic hub)](../../../../../07_Concepts/topics/center_squeeze/README.md)
- [Condorcet efficiency (topic hub)](../../../../../07_Concepts/topics/condorcet/README.md)
- [Ties & tie-breaking (topic hub)](../../../../../07_Concepts/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)
- [Glossary](../../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [bv2209_fxhw6g_burial_pays](bv2209_fxhw6g_burial_pays.md)
