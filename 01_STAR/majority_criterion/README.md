# 01_STAR/majority_criterion — the Majority Criterion, in two tiny elections

Two 5-voter STAR elections that isolate STAR's **Majority-Criterion** behavior — and, in doing so, demonstrate the **Relaxed Majority Criterion** (the "needs *two* rivals, not one" point). Same voters both times; only the majority's generosity to a *second* candidate changes.

| Case (sheet id) | The majority backs… | Winner | Shows |
|---|---|:--:|---|
| [`mc_01`](mc_01_favorite_survives_one_rival.yaml) · **BV95a** | one rival (Bruno 4, Cleo 0) | **Ada** ✓ | the majority's favorite *survives* — RMC safety |
| [`mc_02`](mc_02_favorite_loses_two_rivals.yaml) · **BV95b** | two rivals (Bruno 4, Cleo 3) | **Bruno** ✗ | the Majority-Criterion *failure* |

Full concept, the Relaxed Majority Criterion, the Later-No-Harm connection, and references: **[Majority Criterion topic hub](../../00_start_here/topics/majority_criterion/README.md)**.

**Confirmed on BetterVoting.** Both were reproduced live on bettervoting.com and BV agrees with the LH result: BV95a → [`9m6rxr`](https://bettervoting.com/9m6rxr) elects **Ada**; BV95b → [`7pdq3r`](https://bettervoting.com/7pdq3r) elects **Bruno** (5 ballots each, `nTallyVotes 5`). Frozen exports: [`mc_01…_bv_export.json`](mc_01_favorite_survives_one_rival_bv_export.json) · [`mc_02…_bv_export.json`](mc_02_favorite_loses_two_rivals_bv_export.json). (Created via [`tools_adam/create_bv_test_election.py`](../../STARVote_LH_tabulation_engine/tools_adam/create_bv_test_election.py).)

Both files carry `expected_winners` and are checked by `test_single_winner_positive.py`.

# file: README.md
