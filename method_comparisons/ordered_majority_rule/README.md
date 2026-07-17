# "Ordered majority rule" — the countable check (LH-only)

The tabulatable evidence behind [Ordered majority rule and the "Condorcet isn't desirable" argument](../../00_start_here/topics/condorcet/ordered_majority_rule_irv.md). The arXiv paper [A Majority Rule Philosophy for Instant Runoff Voting](https://arxiv.org/abs/2308.08430) defends RCV-IRV with a new criterion — *ordered majority rule* — whose plain-English selling point promises to prevent "opposition voters from influencing the choice of candidate from the faction they oppose." Toby Pereira's counterexample (from the [votingtheory.org thread](https://votingtheory.org/forum/post/2853)) shows the sentence failing on its own terms.

**LH-only** — an abstract ranked profile, no BetterVoting election (the lesson is the mechanism, not a live tally).

| Election (source) | What it shows |
|---|---|
| [`omr_opposition_decides.yaml`](omr_opposition_decides.yaml) · [tabulated](ordered_majority_rule_tabulated/omr_opposition_decides_tabulated.txt) | 35 A>B>C, 33 B>A>C, 32 C>B>A. A leads first choices 35–33, but IRV eliminates C and its transfers hand the A-vs-B race to B (65–35). The opposition (C-first voters, who rank both frontrunners last) decided the intra-frontrunner contest. B is also the Condorcet winner, so IRV isn't misfiring — the point is that the marketing claim is false while the technical criterion escapes only by circular relabeling. |

Concept hubs: [Condorcet efficiency](../../00_start_here/topics/condorcet/) · [center squeeze](../../00_start_here/topics/center_squeeze/) · up: [method_comparisons — same ballots, different methods](../)

# file: README.md
