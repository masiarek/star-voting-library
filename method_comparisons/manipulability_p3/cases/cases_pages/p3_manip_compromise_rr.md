# P3 manipulated — the mild version: three adjacent swaps, no burial, same result

*Generated from [`p3_manip_compromise_rr.yaml`](../p3_manip_compromise_rr.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../../00_start_here/RCV_Ranked_Robin) · **1 seat** · **Expected winner:** Dublin

**Official tie-break (lot) order:** Athens > Bergen > Cork > Dublin > Edinburgh — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

The manipulation that should worry us more than the book's. The complete reversal is a curiosity — no real voter submits their preferences backwards. But the SAME voter can achieve the SAME outcome with ordinary compromising: submit Dublin>Athens>Bergen>Cork>Edinburgh. That is three adjacent swaps. Nothing is buried, the sincere last choice Edinburgh stays last, and only the compromise candidate Dublin is lifted. Dublin goes 4-0 and wins outright. Exhaustively, 52 of the 119 alternative rankings available to this voter strictly improve their result (44 decided outright or by margin, 8 more only after the lot). Note this is COMPROMISING, not burial — Ranked Robin's documented resistance to burial is untouched and remains true, which makes this worse news rather than better, because compromising is the strategy ordinary voters actually reach for.

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
2:Edinburgh>Cork>Athens>Dublin>Bergen
3:Dublin>Edinburgh>Bergen>Cork>Athens
1:Athens>Bergen>Cork>Dublin>Edinburgh
1:Dublin>Athens>Bergen>Cork>Edinburgh
```

## What the engine says

Full report from the [`_tabulated` mirror](../cases_tabulated/p3_manip_compromise_rr_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Ranked Robin (RCV-RR / Copeland) Method (single winner) ---
 Tabulating 7 ballots (ranked ballots).

Ballots:
     2 × Edinburgh > Cork > Athens > Dublin > Bergen
     3 × Dublin > Edinburgh > Bergen > Cork > Athens
     1 × Athens > Bergen > Cork > Dublin > Edinburgh
     1 × Dublin > Athens > Bergen > Cork > Edinburgh

Round-Robin — every pair, head-to-head (For – Against):
   Edinburgh  beats Cork        5 – 2
   Edinburgh  beats Athens      5 – 2
   Dublin     beats Edinburgh   5 – 2
   Edinburgh  beats Bergen      5 – 2
   Cork       beats Athens      5 – 2
   Dublin     beats Cork        4 – 3
   Bergen     beats Cork        5 – 2
   Dublin     beats Athens      4 – 3
   Athens     beats Bergen      4 – 3
   Dublin     beats Bergen      6 – 1

--- Pairwise (Round-Robin) Matrix ---
Head-to-head / pairwise comparison — the Ranked Robin tally
Legend: For - Equal Support - Against   (row vs column)
              |  Edinburgh  |   Cork     |  Athens    |  Dublin    |  Bergen    |
---------------------------------------------------------------------------------
  Edinburgh > |     ---     | 5 - 0 - 2  | 5 - 0 - 2  | 2 - 0 - 5  | 5 - 0 - 2  |
       Cork > |  2 - 0 - 5  |    ---     | 5 - 0 - 2  | 3 - 0 - 4  | 2 - 0 - 5  |
     Athens > |  2 - 0 - 5  | 2 - 0 - 5  |    ---     | 3 - 0 - 4  | 4 - 0 - 3  |
     Dublin > |  5 - 0 - 2  | 4 - 0 - 3  | 4 - 0 - 3  |    ---     | 6 - 0 - 1  |
     Bergen > |  2 - 0 - 5  | 5 - 0 - 2  | 3 - 0 - 4  | 1 - 0 - 6  |    ---     |

Win–loss record — Copeland score = wins + ½·ties (highest score wins; ties broken by total margin, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  Dublin     4–0–0         4     +10  Edinburgh, Cork, Athens, Bergen
    2  Edinburgh  3–1–0         3      +6  Cork, Athens, Bergen
    3  Cork       1–3–0         1      -4  Athens
    4  Athens     1–3–0         1      -6  Bergen
    5  Bergen     1–3–0         1      -6  Cork

Winner — Ranked Robin (RCV-RR): Dublin
   beats every opponent head-to-head — the Condorcet winner.
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/manipulability_p3/cases/p3_manip_compromise_rr.yaml
```

## See also

- [Exhausted ballots (conversation)](../../../../00_start_here/RCV_IRV/exhausted_ballots_301.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [p3_manip_reversal_rr](p3_manip_reversal_rr.md) · [p3_manip_star](p3_manip_star.md) · [p3_sincere_ranked_robin](p3_sincere_ranked_robin.md) · [p3_sincere_star](p3_sincere_star.md)
