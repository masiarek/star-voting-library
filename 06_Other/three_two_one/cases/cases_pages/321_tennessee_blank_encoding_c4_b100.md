---
search:
  exclude: true
---

# Tennessee capital by 3-2-1 Voting (blank = Bad)

*Generated from [`321_tennessee_blank_encoding_c4_b100.yaml`](../321_tennessee_blank_encoding_c4_b100.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [3-2-1](../../../../07_Concepts) · **1 seat** · **Expected winner:** Nashville

## Scenario

The classic Tennessee-capital electorate (100 voters, four cities), cast as
3-2-1 Good/OK/Bad ballots. Each faction rates its own city Good, its nearer
neighbours OK, and the far city Bad — and here **Bad is left blank**, to show
3-2-1's blank encoding: an unrated candidate counts as Bad.

Memphis has the most first-choice support (42) and would win Choose-One. But
3-2-1 filters on Bad ratings: Memphis is Bad (blank) on 58 ballots, so it is
eliminated at the finalist step. The consensus capital, Nashville — never
rated Bad by anyone — wins the runoff. This is the same "centrist consensus
winner" result most non-plurality methods give on this electorate.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Memphis,Nashville,Chattanooga,Knoxville
42 × 2,1,,
26 × ,2,1,1
15 × ,1,2,1
17 × ,1,1,2
```

## What the engine says

Full report from the [`_tabulated` mirror](../cases_tabulated/321_tennessee_blank_encoding_c4_b100_321_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- 3-2-1 Voting ---
 Tabulating 4 candidates, Good=2 / OK=1 / Bad=0 (blank = Bad).

Ratings tally (Good / OK / Bad):
   Memphis        Good   42 | OK    0 | Bad   58
   Nashville      Good   26 | OK   74 | Bad    0
   Chattanooga    Good   15 | OK   43 | Bad   42
   Knoxville      Good   17 | OK   41 | Bad   42

Step 1 — Semifinalists (most Good): Memphis (42), Nashville (26), Knoxville (17)
Step 2 — Finalists (fewest Bad): Nashville (Bad 0), Knoxville (Bad 42)
Step 3 — Runoff: Nashville 68 vs Knoxville 17 (15 rated equal)

Winner — 3-2-1 Voting: Nashville
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 06_Other/three_two_one/cases/321_tennessee_blank_encoding_c4_b100.yaml
```

## See also

- [Runoff reversal (worked set)](../../../../01_STAR/02_Examples/runoff_overturns_leader/README.md)
- [Ballot & terminology basics](../../../../07_Concepts/topics/ballot_and_terminology_basics.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)
