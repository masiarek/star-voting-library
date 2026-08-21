# 01_STAR/03_Criteria/majority_criterion — the Majority Criterion, in two tiny elections

**Level: 201 · for debaters**

Two 5-voter STAR elections that isolate STAR's **Majority-Criterion** behavior — and, in doing so, demonstrate the **Relaxed Majority Criterion** (the "needs *two* rivals, not one" point). Same voters both times; only the majority's generosity to a *second* candidate changes.

| Case (sheet id) | The majority backs… | Winner | Shows |
|---|---|:--:|---|
| **BV95a** — [page](bv95a_9m6rxr_favorite_survives_one_rival.md) · [yaml](cases/bv95a_9m6rxr_favorite_survives_one_rival.yaml) | one rival (Bruno 4, Cleo 0) | **Ada** ✓ | the majority's favorite *survives* — RMC safety |
| **BV95b** — [page](bv95b_7pdq3r_favorite_loses_two_rivals.md) · [yaml](cases/bv95b_7pdq3r_favorite_loses_two_rivals.yaml) | two rivals (Bruno 4, Cleo 3) | **Bruno** ✗ | the Majority-Criterion *failure* |

A third, larger case asks the *other* question — not "does STAR pass?" but **"what does passing cost?"**

| Case | Setup | Majority-criterion methods | Whole-ballot methods |
|---|---|:--:|:--:|
| **[Majority vs. consensus, 51/49](cases/cases_pages/majority_vs_consensus_51_49.md)** · [yaml](cases/majority_vs_consensus_51_49.yaml) | a polarized electorate + a candidate everyone is content with | **Alma** (Choose-One, RCV-IRV) | **Celia** (Score, STAR, Ranked Robin) |

It's the standard argument *against* the majority criterion, made runnable — and it doubles as the verification behind [electowiki's cardinal-voting article, claim-checked](../../../07_Concepts/scores_and_ranks/cardinal_voting_claims_checked.md).

Full concept, the Relaxed Majority Criterion, the Later-No-Harm connection, and references: **[Majority Criterion topic hub](../../../07_Concepts/topics/majority_criterion/README.md)**.

**Confirmed on BetterVoting.** Both were reproduced live on bettervoting.com and BV agrees with the LH result: BV95a → [`9m6rxr`](https://bettervoting.com/9m6rxr) elects **Ada**; BV95b → [`7pdq3r`](https://bettervoting.com/7pdq3r) elects **Bruno** (5 ballots each, `nTallyVotes 5`). Frozen exports: [`bv95a…_bv_export.json`](cases/bv95a_9m6rxr_favorite_survives_one_rival_bv_export.json) · [`bv95b…_bv_export.json`](cases/bv95b_7pdq3r_favorite_loses_two_rivals_bv_export.json). (Created via [`tools_adam/create_bv_test_election.py`](../../../STARVote_LH_tabulation_engine/tools_adam/create_bv_test_election.py).)

Both files carry `expected_winners` and are checked by `test_single_winner_positive.py`.

# file: README.md
