---
search:
  exclude: true
---

# The same electorate under plurality block voting — the ranked ballot changed nothing

*Generated from [`bpv_bakery_block_plurality_c4_b12.yaml`](../bpv_bakery_block_plurality_c4_b12.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [plurality](../../../../07_Concepts/README.md) · **2 seats** · **Expected winners:** Almond, Brioche

## Scenario

The third count of the bakery co-op board: the ranks thrown away and each voter
simply marking as many candidates as there are seats (2) — plurality block
voting, the method block preferential voting is usually proposed as an
improvement on.
Each voter marks their own side's two: the 7-voter majority marks Almond and
Brioche, the 5-voter minority marks Croissant and Danish. Almond 7, Brioche 7,
Croissant 5, Danish 5 — Almond and Brioche take both seats.
That is the SAME board block preferential voting produced from the full
rankings (bpv_bakery_seat1_c4_b12.yaml + bpv_bakery_seat2_c3_b12.yaml). The
ranked ballot bought a fairer-looking count and an identical result, which is
Wikipedia's summary of the method: it "regularly produces complete landslide
majorities." What actually moves the seats is the quota — see
bpv_bakery_stv_c4_b12.yaml.
Lesson: 06_Other/RCV_IRV/concepts/variants/RCV-IRV-block-preferential.md

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:Almond,Brioche,Croissant,Danish
7: 1,1,0,0
5: 0,0,1,1
```

## What the engine says

Full report from the [`_tabulated` mirror](../cases_tabulated/bpv_bakery_block_plurality_c4_b12_tabulated.txt) (regenerated on every run; every analysis forced on):

<!-- --8<-- [start:report] -->
```text
--- Block Voting (plurality-at-large) — 2 winners ---
 Tabulating 12 ballots (2 votes/voter).

Votes (most votes fill the seats):
   Almond        7  <- Elected
   Brioche       7  <- Elected
   Croissant     5
   Danish        5

Winners — Block Voting (plurality-at-large), 2 seats:
   1. Almond   (7 votes)
   2. Brioche   (7 votes)
```
<!-- --8<-- [end:report] -->

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/block_preferential/cases/bpv_bakery_block_plurality_c4_b12.yaml
```

## See also

- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [bpv_bakery_seat1_c4_b12](bpv_bakery_seat1_c4_b12.md) · [bpv_bakery_seat2_c3_b12](bpv_bakery_seat2_c3_b12.md) · [bpv_bakery_stv_c4_b12](bpv_bakery_stv_c4_b12.md)
