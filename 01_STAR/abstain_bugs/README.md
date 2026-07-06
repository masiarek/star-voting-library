# 01_STAR / abstain_bugs — BetterVoting abstain-handling reproductions

Real BetterVoting elections that expose the **abstain / blank / zero** handling issues, reproduced and cross-checked against the LH engine. They share one root: BetterVoting's policy ([#884](https://github.com/Equal-Vote/bettervoting/issues/884)) counts an **all-equal** ballot (`0,0` *and* `5,5`) as an abstention, while LH counts an explicit score — even all-0 or all-5 — as a real vote and only abstains a *truly blank* ballot. The winner usually survives (via tiebreak), but the reported tally/abstention **counts diverge**, and BetterVoting's "0 tallied votes yet a winner" is the visible bug.

Full context and the wider ticket map: [BV abstain / blank / zero — issue index](../../00_start_here/tabulation_engines/BV/abstain_issues_index.md) · concept: [abstention vs a zero vs None of the Above](../../00_start_here/STAR_Voting/abstention_vs_zero_vs_nota.md).

| Case | Method | What it shows | Issue |
|---|---|---|:--:|
| [BV11 — full & equal support (5,5)](bv11_6xhfp8_full_equal_support.md) | STAR | `5,5`×3 counted as 3 abstentions (`nTally=0`); UI warns "Abstained" on full support; LH sees a real 15-15 tie | [#1053](https://github.com/Equal-Vote/bettervoting/issues/1053) |
| [BV655 — "equal opposition" (all-0)](bv655_jfrk9t_equal_opposition.md) | STAR | explicit `0,0` labeled "Abstained"; LH treats it as Equal Support, not an abstention | [#1090](https://github.com/Equal-Vote/bettervoting/issues/1090) |
| [BV1570 — undecided plurality](bv1570_6hv7jf_undecided_plurality.md) | Plurality | all-undecided election still declares a winner + wrong voter count (2 vs 3) | [#894](https://github.com/Equal-Vote/bettervoting/issues/894) |

Related NOTA case (a different flavor — a real "None of the Above" candidate): [`bv215_26khr3_nota_wins`](../none_of_the_above/bv215_26khr3_nota_wins.md) ([#1421](https://github.com/Equal-Vote/bettervoting/issues/1421)).

# file: README.md
