# Equal-vote balance — base (IRV elects the Condorcet winner, Bruno)

*Generated from [`balance_base_irv_c3_b9.yaml`](../balance_base_irv_c3_b9.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [RCV-IRV (Instant Runoff)](../../../../00_start_here/RCV_IRV) · **1 seat** · **Expected winner:** Bruno

## Scenario

Three candidates on a line — Ada (left), Bruno (center), Cyrus (right). Bruno is
the Condorcet winner (beats Ada 6-3, Cyrus 7-2) and RCV-IRV elects him too:
Cyrus has the fewest first-choices and is eliminated, his ballots flow to Bruno,
who wins 6-3. The twin file adds three EXACT-OPPOSITE ballot pairs; they cancel
under Condorcet / Ranked Robin / STAR (Bruno stays the winner) but under RCV-IRV
they squeeze Bruno out and elect Ada — so RCV-IRV fails the Equal Vote / Test of
Balance. Lesson: 00_start_here/RCV_IRV/RCV_IRV_equal_vote.md

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
4:Bruno>Ada>Cyrus
3:Ada>Bruno>Cyrus
2:Cyrus>Bruno>Ada
```

## What the engine says

Full report from the [`_tabulated` mirror](../equal_vote_balance_tabulated/balance_base_irv_c3_b9_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- RCV / Instant-Runoff Voting (single winner) ---
  Equal-vote balance — base (IRV elects the Condorcet winner, Bruno)
 Tabulating 9 ballots (ranked ballots).

ROUND 1
Candidate      Votes  Status
-----------  -------  --------
Bruno              4  Hopeful
Ada                3  Hopeful
Cyrus              2  Rejected

FINAL RESULT
Candidate      Votes  Status
-----------  -------  --------
Bruno              6  Elected
Ada                3  Rejected
Cyrus              0  Rejected


Winner(s) — RCV / Instant-Runoff Voting (single winner)
  Bruno
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 06_Other/RCV_IRV/equal_vote_balance/balance_base_irv_c3_b9.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Condorcet efficiency (topic hub)](../../../../00_start_here/topics/condorcet/README.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [balance_plus_opposite_c3_b15](balance_plus_opposite_c3_b15.md)
