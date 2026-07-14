# BV2133 — Pet poll II (RCV-IRV): transfers elect Fish

*Generated from [`bv2133_dyxrbr_pet2_irv.yaml`](../bv2133_dyxrbr_pet2_irv.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [RCV-IRV (Instant Runoff)](../../../00_start_here/RCV_IRV) · **1 seat** · **Expected winner:** Fish

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/dyxrbr) · **[results ↗](https://bettervoting.com/dyxrbr/results)** (election `dyxrbr`).

## Scenario

One of four races in the BV2133 "Pet poll II" (BetterVoting election dyxrbr). RCV-IRV (ranked, instant runoff). Round 1: Dog 13, Fish 10, Bird 9 — eliminate Bird; Bird > Cat, so Cat rises. Then Cat (fewest) is eliminated and its ballots flow to Fish, which beats Dog 19-13. So IRV elects Fish. Same electorate as the Plurality race (Dog), Approval race (Bird) and STAR race (Cat): four methods, four winners. BV also elects Fish. Live results: https://bettervoting.com/dyxrbr/results

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
9:Bird>Cat>Fish>Dog
10:Fish>Cat>Bird>Dog
13:Dog>Cat>Fish>Bird
```

## What the engine says

Full report from the [`_tabulated` mirror](../pet_poll_four_winners_tabulated/bv2133_dyxrbr_pet2_irv_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- RCV / Instant-Runoff Voting (single winner) ---
  BV2133 — Pet poll II (RCV-IRV): transfers elect Fish
 Tabulating 32 ballots (ranked ballots).

ROUND 1
Candidate      Votes  Status
-----------  -------  --------
Dog               13  Hopeful
Fish              10  Hopeful
Bird               9  Rejected
Cat                0  Rejected

FINAL RESULT
Candidate      Votes  Status
-----------  -------  --------
Fish              19  Elected
Dog               13  Rejected
Bird               0  Rejected
Cat                0  Rejected


Winner(s) — RCV / Instant-Runoff Voting (single winner)
  Fish
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/pet_poll_four_winners/bv2133_dyxrbr_pet2_irv.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Runoff reversal (worked set)](../../../01_STAR/runoff_overturns_leader/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [bv2133_dyxrbr_pet2_approval](bv2133_dyxrbr_pet2_approval.md) · [bv2133_dyxrbr_pet2_plurality](bv2133_dyxrbr_pet2_plurality.md) · [bv2133_dyxrbr_pet2_star](bv2133_dyxrbr_pet2_star.md)
