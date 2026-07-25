# Margins matter — RCV-IRV elects the third answer (Cocoa)

*Generated from [`margins_irv.yaml`](../margins_irv.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [RCV-IRV (Instant Runoff)](../../../../00_start_here/RCV_IRV) · **1 seat** · **Expected winner:** Cocoa

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/kdjjkq) · **[results ↗](https://bettervoting.com/kdjjkq/results)** (election `kdjjkq`).

## Scenario

The same twelve gelato ballots, counted by instant runoff. First choices are Almond 5, Cocoa 4, Berry 3, so Berry — the BORDA winner and the margin-weighted Copeland winner — is eliminated FIRST. All three of Berry's ballots rank Cocoa next, so they transfer intact and Cocoa wins 7-5. This is the fourth distinct answer the same electorate produces: Plurality says Almond, RCV-IRV says Cocoa, Borda says Berry, and Copeland says nobody (a three-way tie). Not a center-squeeze case — there is no Condorcet winner for IRV to miss, because the pairwise contests form a cycle.

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
Almond>Berry>Cocoa
Almond>Berry>Cocoa
Almond>Berry>Cocoa
Almond>Berry>Cocoa
Almond>Berry>Cocoa
Berry>Cocoa>Almond
Berry>Cocoa>Almond
Berry>Cocoa>Almond
Cocoa>Almond>Berry
Cocoa>Almond>Berry
Cocoa>Berry>Almond
Cocoa>Berry>Almond
```

## What the engine says

Full report from the [`_tabulated` mirror](../cases_tabulated/margins_irv_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- RCV / Instant-Runoff Voting (single winner) ---
  Margins matter — RCV-IRV elects the third answer (Cocoa)
 Tabulating 12 ballots (ranked ballots).

ROUND 1
Candidate      Votes  Status
-----------  -------  --------
Almond             5  Hopeful
Cocoa              4  Hopeful
Berry              3  Rejected

FINAL RESULT
Candidate      Votes  Status
-----------  -------  --------
Cocoa              7  Elected
Almond             5  Rejected
Berry              0  Rejected


Winner(s) — RCV / Instant-Runoff Voting (single winner)
  Cocoa
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/copeland_vs_borda_margins/cases/margins_irv.yaml
```

## See also

- [Center squeeze (topic hub)](../../../../00_start_here/topics/center_squeeze/README.md)
- [Condorcet efficiency (topic hub)](../../../../00_start_here/topics/condorcet/README.md)
- [Ties & tie-breaking (topic hub)](../../../../00_start_here/topics/ties/README.md)
- [Runoff reversal (worked set)](../../../../01_STAR/runoff_overturns_leader/README.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [margins_paper_exact_304](margins_paper_exact_304.md) · [margins_ranked_robin](margins_ranked_robin.md) · [margins_star](margins_star.md)
