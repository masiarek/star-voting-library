# Ordered majority rule — the opposition decides the A-vs-B race (Toby Pereira's counterexample)

*Generated from [`omr_opposition_decides.yaml`](../omr_opposition_decides.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [RCV-IRV (Instant Runoff)](../../../../00_start_here/RCV_IRV) · **1 seat** · **Expected winner:** B

## Scenario

An abstract counterexample (bare A/B/C, because the mechanism is the whole lesson) to the plain-English selling point of "ordered majority rule" — the criterion the arXiv paper "A Majority Rule Philosophy for Instant Runoff Voting" (arXiv:2308.08430) uses to defend IRV. That summary claims IRV "ensures the election of a candidate from the majority coalition while PREVENTING opposition voters from influencing the choice of candidate from the faction they oppose." Here C is a third bloc that ranks A and B last; A leads on first choices (35 to B's 33). IRV eliminates C, and C's second preferences hand the A-vs-B contest to B (65-35). So the opposition voters DID decide which of the two frontrunners won — contradicting the sentence as worded. (Note: B is also the Condorcet winner here, so IRV is not misfiring on the outcome; the point is narrow and about the marketing claim, not a center-squeeze. The technical criterion permits this because C is "minor" — which is exactly the circularity cfrank flagged: minor/major is defined by the very ordering the criterion is supposed to justify.)

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
35:A>B>C
33:B>A>C
32:C>B>A
```

## What the engine says

Full report from the [`_tabulated` mirror](../cases_tabulated/omr_opposition_decides_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- RCV / Instant-Runoff Voting (single winner) ---
  Ordered majority rule — the opposition decides the A-vs-B race (Toby Pereira's counterexample)
 Tabulating 100 ballots (ranked ballots).

ROUND 1
Candidate      Votes  Status
-----------  -------  --------
A                 35  Hopeful
B                 33  Hopeful
C                 32  Rejected

FINAL RESULT
Candidate      Votes  Status
-----------  -------  --------
B                 65  Elected
A                 35  Rejected
C                  0  Rejected


Winner(s) — RCV / Instant-Runoff Voting (single winner)
  B
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/ordered_majority_rule/cases/omr_opposition_decides.yaml
```

## See also

- [Center squeeze (topic hub)](../../../../00_start_here/topics/center_squeeze/README.md)
- [Condorcet efficiency (topic hub)](../../../../00_start_here/topics/condorcet/README.md)
- [Runoff reversal (worked set)](../../../../01_STAR/runoff_overturns_leader/README.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)
