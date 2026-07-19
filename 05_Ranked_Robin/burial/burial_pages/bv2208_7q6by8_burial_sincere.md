# BV2208 — Burial in Ranked Robin (1/2): sincere ballots, Beryl beats everyone

*Generated from [`bv2208_7q6by8_burial_sincere.yaml`](../bv2208_7q6by8_burial_sincere.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../00_start_here/RCV_Ranked_Robin) · **1 seat** · **Expected winner:** Beryl

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/7q6by8) · **[results ↗](https://bettervoting.com/7q6by8/results)** (election `7q6by8`).

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

Full report from the [`_tabulated` mirror](../burial_tabulated/bv2208_7q6by8_burial_sincere_tabulated.txt) (regenerated on every run; every analysis forced on):

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

Win–loss record — Copeland score = wins + ½·ties (most wins wins; ties broken by total margin, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  Beryl      3–0–0         3     +48  Amber, Coral, Diamond
    2  Amber      2–1–0         2     +12  Coral, Diamond
    3  Coral      1–2–0         1     -30  Diamond
    4  Diamond    0–3–0         0     -30  —

Winner — Ranked Robin (RCV-RR): Beryl
   beats every opponent head-to-head — the Condorcet winner.
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 05_Ranked_Robin/burial/bv2208_7q6by8_burial_sincere.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Center squeeze (topic hub)](../../../00_start_here/topics/center_squeeze/README.md)
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README.md)
- [Ties & tie-breaking (topic hub)](../../../00_start_here/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [bv2209_fxhw6g_burial_pays](bv2209_fxhw6g_burial_pays.md)
