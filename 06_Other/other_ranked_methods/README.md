# Other ranked methods — the shelf, not a method

**This folder is not a voting method.** Its siblings in [06_Other](../README.md) each *are* one — [Plurality](../Plurality/README.md), [RCV-IRV](../RCV_IRV/README.md), [STV](../STV/README.md), [Range](../Range/README.md), [3-2-1](../three_two_one/README.md) — and each earned a folder by having runnable `cases/` to put in it. This is the shelf for ranked methods that don't yet: one concept page apiece, no YAML, no tabulation.

| Page | What it is | Why it's here and not in its own folder |
|---|---|---|
| [Borda count](borda.md) | positional scoring — 1st place = N−1 points, 2nd = N−2, … — and what it means that those "scores" are **manufactured** from ranks the voter never rated | the repo teaches Borda as the *reverse* of [scores vs. ranks](../../07_Concepts/scores_and_ranks/scores_vs_ranks.md), a concept move rather than a method to run; the LH engine has no Borda tabulation |
| [Agenda voting](agenda_voting.md) | sequential pairwise majority votes down a fixed list — change the agenda, change the winner, same ballots | a parliamentary *procedure* for motions, not a candidate election; it has no canonical result to freeze, because the agenda is a parameter |

**The graduation rule:** the day one of these gets runnable cases, it moves out into its own `06_Other/<Method>/` folder with a `README.md` and a `cases/` subfolder, like every other method here — and leaves a [redirect](../../07_Concepts/about_this_repo/website_build.md) behind. Until then, a folder holding one Markdown file and no ballots would be worse than the file.

Neither page is a dead end. Borda lives on inside methods that *are* runnable — the Borda-elimination family, [Baldwin & Nanson](../RCV_IRV/concepts/variants/RCV-IRV-Baldwin-Nanson.md) — and agenda voting is the foil for [Ranked Robin](../../05_Ranked_Robin/01_Learn/ranked_robin.md), which runs *every* pairwise matchup symmetrically instead of a hand-picked sequence of them.

# file: README.md
