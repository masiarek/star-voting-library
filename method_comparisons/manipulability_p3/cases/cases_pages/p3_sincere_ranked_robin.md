# P3 sincere — Ranked Robin elects Edinburgh (the baseline every manipulation attacks)

*Generated from [`p3_sincere_ranked_robin.yaml`](../p3_sincere_ranked_robin.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../../00_start_here/RCV_Ranked_Robin) · **1 seat** · **Expected winner:** Edinburgh

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/4w96tr) · **[results ↗](https://bettervoting.com/4w96tr/results)** (election `4w96tr`).

**Official tie-break (lot) order:** Athens > Bergen > Cork > Dublin > Edinburgh — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

Zwicker's profile P3 (Handbook of Computational Social Choice ch. 2, Definition 2.3), 7 voters and 5 candidates, cast SINCERELY. Edinburgh goes 3-1 head-to-head and is the Copeland/Ranked Robin winner with a symmetric Copeland score of +2; Bergen is -2 and the rest are 0, exactly the numbers the book prints. There is NO Condorcet winner (Dublin beats Edinburgh 5-2, so nobody beats everybody). This is the baseline: the two Athens-first voters are about to see their LAST choice, Edinburgh, win — which is precisely the pressure the book uses to define single-voter manipulability. The manipulated counterparts are p3_manip_reversal_rr.yaml and p3_manip_compromise_rr.yaml.

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
2:Edinburgh>Cork>Athens>Dublin>Bergen
3:Dublin>Edinburgh>Bergen>Cork>Athens
2:Athens>Bergen>Cork>Dublin>Edinburgh
```

## What the engine says

Full report from the [`_tabulated` mirror](../cases_tabulated/p3_sincere_ranked_robin_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Ranked Robin (RCV-RR / Copeland) Method (single winner) ---
 Tabulating 7 ballots (ranked ballots).

Ballots:
     2 × Edinburgh > Cork > Athens > Dublin > Bergen
     3 × Dublin > Edinburgh > Bergen > Cork > Athens
     2 × Athens > Bergen > Cork > Dublin > Edinburgh

Round-Robin — every pair, head-to-head (For – Against):
   Edinburgh  beats Cork        5 – 2
   Edinburgh  beats Athens      5 – 2
   Dublin     beats Edinburgh   5 – 2
   Edinburgh  beats Bergen      5 – 2
   Cork       beats Athens      5 – 2
   Cork       beats Dublin      4 – 3
   Bergen     beats Cork        5 – 2
   Athens     beats Dublin      4 – 3
   Athens     beats Bergen      4 – 3
   Dublin     beats Bergen      5 – 2

--- Pairwise (Round-Robin) Matrix ---
Head-to-head / pairwise comparison — the Ranked Robin tally
Legend: For - Equal Support - Against   (row vs column)
              |  Edinburgh  |   Cork     |  Athens    |  Dublin    |  Bergen    |
---------------------------------------------------------------------------------
  Edinburgh > |     ---     | 5 - 0 - 2  | 5 - 0 - 2  | 2 - 0 - 5  | 5 - 0 - 2  |
       Cork > |  2 - 0 - 5  |    ---     | 5 - 0 - 2  | 4 - 0 - 3  | 2 - 0 - 5  |
     Athens > |  2 - 0 - 5  | 2 - 0 - 5  |    ---     | 4 - 0 - 3  | 4 - 0 - 3  |
     Dublin > |  5 - 0 - 2  | 3 - 0 - 4  | 3 - 0 - 4  |    ---     | 5 - 0 - 2  |
     Bergen > |  2 - 0 - 5  | 5 - 0 - 2  | 3 - 0 - 4  | 2 - 0 - 5  |    ---     |

Win–loss record — Copeland score = wins + ½·ties (most wins wins; ties broken by total margin, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  Edinburgh  3–1–0         3      +6  Cork, Athens, Bergen
    2  Dublin     2–2–0         2      +4  Edinburgh, Bergen
    3  Cork       2–2–0         2      -2  Dublin, Athens
    4  Athens     2–2–0         2      -4  Dublin, Bergen
    5  Bergen     1–3–0         1      -4  Cork

Winner — Ranked Robin (RCV-RR): Edinburgh
   the most head-to-head wins (3).
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/manipulability_p3/cases/p3_sincere_ranked_robin.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../00_start_here/topics/condorcet/README.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [p3_manip_compromise_rr](p3_manip_compromise_rr.md) · [p3_manip_reversal_rr](p3_manip_reversal_rr.md) · [p3_manip_star](p3_manip_star.md) · [p3_sincere_star](p3_sincere_star.md)
