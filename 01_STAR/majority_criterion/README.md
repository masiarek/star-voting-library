# 01_STAR/majority_criterion — the Majority Criterion, in two tiny elections

Two 5-voter STAR elections that isolate STAR's **Majority-Criterion** behavior — and, in doing so, demonstrate the **Relaxed Majority Criterion** (the "needs *two* rivals, not one" point). Same voters both times; only the majority's generosity to a *second* candidate changes.

| Case (sheet id) | The majority backs… | Winner | Shows |
|---|---|:--:|---|
| [`mc_01`](mc_01_favorite_survives_one_rival.yaml) · **BV95a** | one rival (Bruno 4, Cleo 0) | **Ada** ✓ | the majority's favorite *survives* — RMC safety |
| [`mc_02`](mc_02_favorite_loses_two_rivals.yaml) · **BV95b** | two rivals (Bruno 4, Cleo 3) | **Bruno** ✗ | the Majority-Criterion *failure* |

Full concept, the Relaxed Majority Criterion, the Later-No-Harm connection, and references: **[Majority Criterion topic hub](../../00_start_here/topics/majority_criterion/README.md)**.

Both files carry `expected_winners` and are checked by `test_single_winner_positive.py`.

# file: README.md
