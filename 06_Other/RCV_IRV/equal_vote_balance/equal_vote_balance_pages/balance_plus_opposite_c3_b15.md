# Equal-vote balance — plus 3 opposite pairs (IRV flips to Ada)

*Generated from [`balance_plus_opposite_c3_b15.yaml`](../balance_plus_opposite_c3_b15.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [RCV-IRV (Instant Runoff)](../../../../00_start_here/RCV_IRV) · **1 seat** · **Expected winner:** Ada

## Scenario

The base election plus three exact-opposite ballot pairs (each Ada>Bruno>Cyrus
matched by its reverse Cyrus>Bruno>Ada). The pairs are perfectly balanced — under
Condorcet / Ranked Robin / STAR they cancel and Bruno stays the winner (margins
just grow to 9-6 and 10-5). But RCV-IRV counts only first-choices, so the six new
ballots pile onto the extremes (Ada +3, Cyrus +3) and none onto the center
(Bruno +0): Bruno now has the fewest first-choices, is eliminated first, and Ada
wins 10-5. Balanced ballots that should cancel instead flip the winner — RCV-IRV
fails the Test of Balance, by the center-squeeze mechanism. Lesson:
00_start_here/RCV_IRV/RCV_IRV_equal_vote.md

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
4:Bruno>Ada>Cyrus
6:Ada>Bruno>Cyrus
5:Cyrus>Bruno>Ada
```

## What the engine says

Full report from the [`_tabulated` mirror](../equal_vote_balance_tabulated/balance_plus_opposite_c3_b15_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- RCV / Instant-Runoff Voting (single winner) ---
  Equal-vote balance — plus 3 opposite pairs (IRV flips to Ada)
 Tabulating 15 ballots (ranked ballots).

ROUND 1
Candidate      Votes  Status
-----------  -------  --------
Ada                6  Hopeful
Cyrus              5  Hopeful
Bruno              4  Rejected

FINAL RESULT
Candidate      Votes  Status
-----------  -------  --------
Ada               10  Elected
Cyrus              5  Rejected
Bruno              0  Rejected


Winner(s) — RCV / Instant-Runoff Voting (single winner)
  Ada
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 06_Other/RCV_IRV/equal_vote_balance/balance_plus_opposite_c3_b15.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Center squeeze (topic hub)](../../../../00_start_here/topics/center_squeeze/README.md)
- [Condorcet efficiency (topic hub)](../../../../00_start_here/topics/condorcet/README.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [balance_base_irv_c3_b9](balance_base_irv_c3_b9.md)
