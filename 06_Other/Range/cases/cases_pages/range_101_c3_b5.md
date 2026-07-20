# Range / Score Voting 101 — highest total score wins

*Generated from [`range_101_c3_b5.yaml`](../range_101_c3_b5.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [range](../../../../00_start_here) · **1 seat** · **Expected winner:** Beth

## Scenario

The simplest score election. Three candidates, five voters grading 0–5.
Range (Score) voting just SUMS the grades — highest total wins, no runoff and
no elimination. Beth has broad, strong support across both camps and wins on
total score (21), ahead of Cole (15) and Amy (11). Tabulated by the range
engine (pref_voting score_voting, cross-checked against a hand sum).

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Amy,Beth,Cole
5,4,0
5,3,1
0,4,5
1,5,4
0,5,5
```

## What the engine says

*(No `_tabulated` mirror found — run the file once to generate it.)*

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 06_Other/Range/cases/range_101_c3_b5.yaml
```

## See also

- [Runoff reversal (worked set)](../../../../01_STAR/runoff_overturns_leader/README.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [range_sullivan_score_c4_b10](range_sullivan_score_c4_b10.md)
