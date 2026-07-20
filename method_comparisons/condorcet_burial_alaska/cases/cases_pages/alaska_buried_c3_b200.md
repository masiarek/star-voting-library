# Alaska 2022 (Begich buried) — a manufactured cycle; margin methods resist, TTR/Hare doesn't

*Generated from [`alaska_buried_c3_b200.yaml`](../alaska_buried_c3_b200.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [RCV-IRV (Instant Runoff)](../../../../00_start_here/RCV_IRV) · **1 seat** · **Expected winner:** Peltola

## Scenario

The same electorate, but 20 of the 50 Peltola>Begich>Palin voters BURY Begich —
insincerely ranking him last (Peltola>Palin>Begich). That single move flips the
Begich-vs-Palin pairwise from Begich +39 to Palin +1, creating a Condorcet cycle
(Begich>Peltola>Palin>Begich, no Condorcet winner). Now the completion methods
DIVERGE: MinMax / Schulze / Ranked Pairs (margin-based) drop Palin's weak +1
defeat and still elect Begich — the burial FAILS. But Condorcet-Hare / Condorcet-
Top-Two-Runoff (= RCV-IRV in a 3-way cycle) elects Peltola — the burial SUCCEEDS.
rb-j's point: even Condorcet methods can be gamed by burial, and margin-based
completion resists it far better than a runoff/Hare completion.

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
30:Peltola>Begich>Palin
36:Palin>Begich>Peltola
29:Begich>Palin>Peltola
25:Peltola
23:Palin
16:Begich>Peltola>Palin
12:Begich
25:Peltola>Palin>Begich
4:Palin>Peltola>Begich
```

## What the engine says

Full report from the [`_tabulated` mirror](../cases_tabulated/alaska_buried_c3_b200_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- RCV / Instant-Runoff Voting (single winner) ---
  Alaska 2022 (Begich buried) — a manufactured cycle; margin methods resist, TTR/Hare doesn't
 Tabulating 200 ballots (ranked ballots).

ROUND 1
Candidate      Votes  Status
-----------  -------  --------
Peltola           80  Hopeful
Palin             63  Hopeful
Begich            57  Rejected

FINAL RESULT
Candidate      Votes  Status
-----------  -------  --------
Peltola           96  Elected
Palin             92  Rejected
Begich             0  Rejected
Blank Votes       12  Rejected


Winner(s) — RCV / Instant-Runoff Voting (single winner)
  Peltola
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/condorcet_burial_alaska/cases/alaska_buried_c3_b200.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../00_start_here/topics/condorcet/README.md)
- [Runoff reversal (worked set)](../../../../01_STAR/runoff_overturns_leader/README.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [alaska_sincere_c3_b200](alaska_sincere_c3_b200.md)
