# Range / Score Voting — Sullivan's Example 5.2 (0–10 scale)

*Generated from [`range_sullivan_score_c4_b10.yaml`](../range_sullivan_score_c4_b10.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [range](../../../../00_start_here) · **1 seat** · **Expected winner:** C

## Scenario

A worked Score (Range) election on a 0–10 scale, adapted from Brendan W.
Sullivan, "An Introduction to the Math of Voting Methods" (2022), Example 5.2
(used here for method comparison, with attribution). Ten voters grade four
candidates A, B, C, D from 0 (worst) to 10 (best); Range voting sums the grades
and the highest total wins. Totals: C 70, A 61, D 58, B 47 — C wins, powered by
many 10s (broad AND strong support). The teaching value is the comparison across
cardinal methods on ONE electorate: the mean (Range) winner is C; the median
(greatest-median) winner is also C (median 8.5); STAR agrees too (C leads scoring
70 and wins the runoff over A, 6–3); but Approval — a 1-bit cardinal ballot —
picks A in Sullivan's companion Example 5.1 (A has 8 approvals to C's 7). Same
voters, and the ballot's resolution changes the winner. Tabulated by the range
engine (pref_voting score_voting, cross-checked against a hand sum).
Source: Brendan W. Sullivan, An Introduction to the Math of Voting Methods
(2022), ISBN 978-1-958469-03-3.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
A,B,C,D
10,0,0,0
5,7,10,8
0,4,10,8
7,7,1,10
7,9,7,4
6,6,9,4
8,3,10,3
0,8,5,5
8,0,10,6
10,3,8,10
```

## What the engine says

*(No `_tabulated` mirror found — run the file once to generate it.)*

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 06_Other/Range/cases/range_sullivan_score_c4_b10.yaml
```

## See also

- [Runoff reversal (worked set)](../../../../01_STAR/runoff_overturns_leader/README.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [range_101_c3_b5](range_101_c3_b5.md)
