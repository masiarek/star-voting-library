# Tennessee capital by 3-2-1 Voting (blank = Bad)

*Generated from [`321_tennessee_blank_encoding_c4_b100.yaml`](../321_tennessee_blank_encoding_c4_b100.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [3-2-1](../../../../00_start_here) · **1 seat**

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

*(No `_tabulated` mirror found — run the file once to generate it.)*

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 06_Other/three_two_one/cases/321_tennessee_blank_encoding_c4_b100.yaml
```

## See also

- [Runoff reversal (worked set)](../../../../01_STAR/runoff_overturns_leader/README.md)
- [Ballot & terminology basics](../../../../00_start_here/topics/ballot_and_terminology_basics.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)
