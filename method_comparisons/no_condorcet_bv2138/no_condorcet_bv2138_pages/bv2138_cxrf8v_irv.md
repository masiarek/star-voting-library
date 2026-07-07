# No Condorcet Winner — IRV (Hare): Dave wins by elimination

*Generated from [`bv2138_cxrf8v_irv.yaml`](../bv2138_cxrf8v_irv.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [RCV-IRV (Instant Runoff)](../../../00_start_here/RCV_IRV) · **1 seat** · **Expected winner:** Dave

## Scenario

One of four races in the 'One Ranked Electorate, Many Tabulations' election (BV2138, bvid cxrf8v; BV-confirmed). 921 voters, five candidates, NO Condorcet winner (Smith set = Abby, Brad, Dave, Erin). Robert LeGrand's flagship 'the method decides' example: across ~15 methods the win splits five ways. IRV → Dave.

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
98:Abby>Cora>Erin>Dave>Brad
64:Brad>Abby>Erin>Cora>Dave
12:Brad>Abby>Erin>Dave>Cora
98:Brad>Erin>Abby>Cora>Dave
13:Brad>Erin>Abby>Dave>Cora
125:Brad>Erin>Dave>Abby>Cora
124:Cora>Abby>Erin>Dave>Brad
76:Cora>Erin>Abby>Dave>Brad
21:Dave>Abby>Brad>Erin>Cora
30:Dave>Brad>Abby>Erin>Cora
98:Dave>Brad>Erin>Cora>Abby
139:Dave>Cora>Abby>Brad>Erin
23:Dave>Cora>Brad>Abby>Erin
```

## What the engine says

Full report from the [`_tabulated` mirror](../no_condorcet_bv2138_tabulated/bv2138_cxrf8v_irv_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- RCV / Instant-Runoff Voting (single winner) ---
  No Condorcet Winner — IRV (Hare): Dave wins by elimination
 Tabulating 921 ballots (ranked ballots).

ROUND 1
Candidate      Votes  Status
-----------  -------  --------
Brad             312  Hopeful
Dave             311  Hopeful
Cora             200  Rejected
Abby              98  Rejected
Erin               0  Rejected

FINAL RESULT
Candidate      Votes  Status
-----------  -------  --------
Dave             609  Elected
Brad             312  Rejected
Cora               0  Rejected
Abby               0  Rejected
Erin               0  Rejected


Winner(s) — RCV / Instant-Runoff Voting (single winner)
  Dave
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/no_condorcet_bv2138/bv2138_cxrf8v_irv.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README.md)
- [Vote splitting (worked set)](../../split_voting/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [bv2138_cxrf8v_ranked_robin](bv2138_cxrf8v_ranked_robin.md) · [bv2138_cxrf8v_star](bv2138_cxrf8v_star.md) · [bv2138_cxrf8v_stv](bv2138_cxrf8v_stv.md)
