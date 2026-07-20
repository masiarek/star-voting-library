# The Post-it RCV example (20 voters) — Ranked Robin: a cycle, a 2-1 tie, and two ladders

*Generated from [`bv2176_p8dp28_ranked_robin.yaml`](../bv2176_p8dp28_ranked_robin.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../../00_start_here/RCV_Ranked_Robin) · **1 seat** · **Expected winner:** Blue

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/p8dp28) · **[results ↗](https://bettervoting.com/p8dp28/results)** (election `p8dp28`).

**Official tie-break (lot) order:** Purple > Green > Blue > Pink — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

One of three races in the Post-it RCV example (BV2176, bvid p8dp28;
BV-confirmed). The same 20 ranked ballots as the RCV-IRV race, compared
every-pair head-to-head. The pairwise picture is a genuine Condorcet cycle —
Purple beats Green 9-8, Green beats Blue 7-4, Blue beats Purple 10-9 (and
Pink beats Purple 12-8) — so no candidate beats all others, and Green and
Blue tie on record at 2-1 (Copeland 2). This is the documented spot where
the two engines' tiebreak ladders part ways
(00_start_here/RCV_Ranked_Robin/rr_tiebreak_lh_vs_bv.md), and BOTH stay
deterministic here: BetterVoting's ladder (exactly 2 tied -> their own
head-to-head) elects GREEN, who beats Blue 7-4 — BV-confirmed, freezable;
the LH ladder below (total margin, then lot) elects BLUE (+5 vs Green's +4).
Same ballots, same 2-1 tie, two defensible winners — the first live
BetterVoting election to exhibit the ladder divergence. expected_winners
records the LH result (Blue); the frozen BV export records Green.

Live results: https://bettervoting.com/p8dp28/results
Companion races: bv2176_p8dp28_star.yaml, bv2176_p8dp28_irv.yaml.
Overview page: bv2176_p8dp28_postit_rcv_example.md

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
Purple
Purple
Purple
Purple
Purple
Purple
Purple
Green>Blue>Pink
Green>Blue>Pink
Green>Blue>Pink
Green>Blue>Pink
Green>Blue>Pink
Green>Blue>Pink
Blue>Pink
Blue>Pink
Blue>Green>Pink
Blue>Purple
Pink>Green>Purple
Pink>Purple
Pink
```

## What the engine says

Full report from the [`_tabulated` mirror](../cases_tabulated/bv2176_p8dp28_ranked_robin_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Ranked Robin (RCV-RR / Copeland) Method (single winner) ---
 Tabulating 20 ballots (ranked ballots).

Ballots:
     7 × Purple
     6 × Green > Blue > Pink
     2 × Blue > Pink
     1 × Blue > Green > Pink
     1 × Blue > Purple
     1 × Pink > Green > Purple
     1 × Pink > Purple
     1 × Pink

Round-Robin — every pair, head-to-head (For – Against):
   Purple  beats Green     9 –  8
   Blue    beats Purple   10 –  9
   Pink    beats Purple   12 –  8
   Green   beats Blue      7 –  4
   Green   beats Pink      7 –  5
   Blue    beats Pink     10 –  3

--- Pairwise (Round-Robin) Matrix ---
Head-to-head / pairwise comparison — the Ranked Robin tally
Legend: For - Equal Support - Against   (row vs column)
           |    Purple    |   Green     |    Blue     |    Pink     |
---------------------------------------------------------------------
  Purple > |     ---      | 9 -  3 -  8 | 9 -  1 - 10 | 8 -  0 - 12 |
   Green > |  8 -  3 -  9 |    ---      | 7 -  9 -  4 | 7 -  8 -  5 |
    Blue > | 10 -  1 -  9 | 4 -  9 -  7 |    ---      |10 -  7 -  3 |
    Pink > | 12 -  0 -  8 | 5 -  8 -  7 | 3 -  7 - 10 |    ---      |

Win–loss record — Copeland score = wins + ½·ties (most wins wins; ties broken by total margin, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  Blue       2–1–0         2      +5  Purple, Pink
    2  Green      2–1–0         2      +4  Blue, Pink
    3  Purple     1–2–0         1      -4  Green
    4  Pink       1–2–0         1      -5  Purple

Winner — Ranked Robin (RCV-RR): Blue
   *** 2 candidates tie for the most wins (Green, Blue) — a Condorcet cycle (no candidate beats all others). Resolved by total margin, then lot order. (This is where Minimax / Ranked Pairs / Schulze differ — see 00_start_here/RCV_Ranked_Robin/cycle_resolution.md.)
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/postit_rcv_example/cases/bv2176_p8dp28_ranked_robin.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../00_start_here/topics/condorcet/README.md)
- [Ties & tie-breaking (topic hub)](../../../../00_start_here/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [bv2176_p8dp28_irv](bv2176_p8dp28_irv.md) · [bv2176_p8dp28_star](bv2176_p8dp28_star.md) · [bv2177_v8r66y_approval](bv2177_v8r66y_approval.md) · [bv2177_v8r66y_plurality](bv2177_v8r66y_plurality.md) · [bv2178_8kg698_irv](bv2178_8kg698_irv.md) · [bv2178_8kg698_ranked_robin](bv2178_8kg698_ranked_robin.md) · [bv2178_8kg698_star](bv2178_8kg698_star.md)
