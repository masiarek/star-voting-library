# Center Squeeze — Ranked Robin (Copeland): the Condorcet winner survives

*Generated from [`bv2137_ywckmg_ranked_robin.yaml`](../bv2137_ywckmg_ranked_robin.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../00_start_here/RCV_Ranked_Robin) · **1 seat** · **Expected winner:** Anderson

**Official tie-break (lot) order:** Anderson > Carter > Reagan — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

One of four races in the Center Squeeze election (BV2137, bvid ywckmg; BV-confirmed). 100 voters, three candidates, ONE ranked electorate tabulated four ways. Anderson is the Condorcet winner (beats Reagan 55–45, Carter 65–35) but holds the fewest first-choices (20). Ranked Robin counts head-to-heads: Anderson beats BOTH rivals, so RR → Anderson — the Condorcet winner IRV threw away.

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
45:Reagan>Anderson>Carter
20:Anderson>Carter>Reagan
35:Carter>Anderson>Reagan
```

## What the engine says

Full report from the [`_tabulated` mirror](../center_squeeze_bv2137_tabulated/bv2137_ywckmg_ranked_robin_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Ranked Robin (RCV-RR / Copeland) Method (single winner) ---
 Tabulating 100 ballots (ranked ballots).

Ballots:
    45 × Reagan > Anderson > Carter
    20 × Anderson > Carter > Reagan
    35 × Carter > Anderson > Reagan

Round-Robin — every pair, head-to-head (For – Against):
   Anderson  beats Reagan     55 – 45
   Carter    beats Reagan     55 – 45
   Anderson  beats Carter     65 – 35

--- Pairwise (Round-Robin) Matrix ---
Head-to-head / pairwise comparison — the Ranked Robin tally
Legend: For - Equal Support - Against   (row vs column)
             |    Reagan    |  Anderson   |   Carter    |
---------------------------------------------------------
    Reagan > |     ---      |45 -  0 - 55 |45 -  0 - 55 |
  Anderson > | 55 -  0 - 45 |    ---      |65 -  0 - 35 |
    Carter > | 55 -  0 - 45 |35 -  0 - 65 |    ---      |

Win–loss record — Copeland score = wins + ½·ties (most wins wins; ties broken by total margin, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  Anderson   2–0–0         2     +40  Carter, Reagan
    2  Carter     1–1–0         1     -20  Reagan
    3  Reagan     0–2–0         0     -20  —

Winner — Ranked Robin (RCV-RR): Anderson
   beats every opponent head-to-head — the Condorcet winner.
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/center_squeeze_bv2137/bv2137_ywckmg_ranked_robin.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Center squeeze (topic hub)](../../../00_start_here/topics/center_squeeze/README.md)
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [bv2137_ywckmg_irv](bv2137_ywckmg_irv.md) · [bv2137_ywckmg_star](bv2137_ywckmg_star.md) · [bv2137_ywckmg_stv](bv2137_ywckmg_stv.md)
