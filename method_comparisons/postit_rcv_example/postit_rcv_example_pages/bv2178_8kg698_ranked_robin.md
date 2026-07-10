# The Post-it switch, made real — Ranked Robin: Blue, now the outright Condorcet winner

*Generated from [`bv2178_8kg698_ranked_robin.yaml`](../bv2178_8kg698_ranked_robin.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../00_start_here/RCV_Ranked_Robin) · **1 seat** · **Expected winner:** Blue

**Official tie-break (lot) order:** Purple > Green > Blue > Pink — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

One of four races in the Post-it switch election (BV2178, bvid 8kg698;
BV-confirmed) — the BV2176/BV2177 electorate with two of the six
Green>Blue>Pink voters flipping their top two (Blue>Green>Pink). In the
original election the pairwise picture was a Condorcet cycle with Green and
Blue tied 2-1 — the race where BetterVoting (head-to-head rung: Green) and
LH (margin rung: Blue) famously part ways. The two-ballot flip dissolves
all of it: Blue now beats Green 6-5 as well as Purple 10-9 and Pink 10-3 —
a clean 3-0 CONDORCET WINNER. No tie, no ladder, no divergence: LH,
BetterVoting, and pref_voting's independent Copeland all elect Blue.
Cycles are knife-edges; two ballots is all it took to go from "two engines,
two defensible winners" to unanimity. See the fairness lesson page:
postit_video_fair_and_balanced.md.

Live results: https://bettervoting.com/8kg698/results
Companion races: bv2178_8kg698_star.yaml, bv2178_8kg698_irv.yaml.
Overview page: bv2178_8kg698_switch_made_real.md

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
Blue>Green>Pink
Blue>Green>Pink
Blue>Pink
Blue>Pink
Blue>Green>Pink
Blue>Purple
Pink>Green>Purple
Pink>Purple
Pink
```

## What the engine says

Full report from the [`_tabulated` mirror](../postit_rcv_example_tabulated/bv2178_8kg698_ranked_robin_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Ranked Robin (RCV-RR / Copeland) Method (single winner) ---
 Tabulating 20 ballots (ranked ballots).

Ballots:
     7 × Purple
     4 × Green > Blue > Pink
     3 × Blue > Green > Pink
     2 × Blue > Pink
     1 × Blue > Purple
     1 × Pink > Green > Purple
     1 × Pink > Purple
     1 × Pink

Round-Robin — every pair, head-to-head (For – Against):
   Purple  beats Green     9 –  8
   Blue    beats Purple   10 –  9
   Pink    beats Purple   12 –  8
   Blue    beats Green     6 –  5
   Green   beats Pink      7 –  5
   Blue    beats Pink     10 –  3

--- Pairwise (Round-Robin) Matrix ---
Head-to-head / pairwise comparison — the Ranked Robin tally
Legend: For - Equal Support - Against   (row vs column)
           |    Purple    |   Green     |    Blue     |    Pink     |
---------------------------------------------------------------------
  Purple > |     ---      | 9 -  3 -  8 | 9 -  1 - 10 | 8 -  0 - 12 |
   Green > |  8 -  3 -  9 |    ---      | 5 -  9 -  6 | 7 -  8 -  5 |
    Blue > | 10 -  1 -  9 | 6 -  9 -  5 |    ---      |10 -  7 -  3 |
    Pink > | 12 -  0 -  8 | 5 -  8 -  7 | 3 -  7 - 10 |    ---      |

Win–loss record — Copeland score = wins + ½·ties (most wins wins; ties broken by total margin, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  Blue       3–0–0         3      +9  Green, Purple, Pink
    2  Green      1–2–0         1      +0  Pink
    3  Purple     1–2–0         1      -4  Green
    4  Pink       1–2–0         1      -5  Purple

Winner — Ranked Robin (RCV-RR): Blue
   beats every opponent head-to-head — the Condorcet winner.
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/postit_rcv_example/bv2178_8kg698_ranked_robin.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README.md)
- [Ties & tie-breaking (topic hub)](../../../00_start_here/topics/ties/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [bv2176_p8dp28_irv](bv2176_p8dp28_irv.md) · [bv2176_p8dp28_ranked_robin](bv2176_p8dp28_ranked_robin.md) · [bv2176_p8dp28_star](bv2176_p8dp28_star.md) · [bv2177_v8r66y_approval](bv2177_v8r66y_approval.md) · [bv2177_v8r66y_plurality](bv2177_v8r66y_plurality.md) · [bv2178_8kg698_irv](bv2178_8kg698_irv.md) · [bv2178_8kg698_star](bv2178_8kg698_star.md)
