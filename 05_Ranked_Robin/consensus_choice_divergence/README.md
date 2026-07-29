# Ranked Robin vs Consensus Choice — the same cycle, two different winners

Two organisations promote a Condorcet method for ranked ballots. Equal Vote calls theirs **Ranked Robin**; Better Choices for Democracy calls theirs **Consensus Choice**. They agree on everything that usually matters — same ballot, same head-to-head count, same winner whenever somebody beats everyone. They differ in one place only: **what to do when nobody does.**

That difference is normally invisible, because a cycle is rare. This case makes it visible, and the answer is not academic — on these ballots the two brands elect **different people**.

## The election

32 voters, three candidates, one cycle.

```text
12 : Ana > Bruno > Celia
 6 : Bruno > Celia > Ana
14 : Celia > Ana > Bruno
```

Head-to-head, nobody goes undefeated:

| Matchup | Result | Margin |
|---|---|---|
| Ana vs Bruno | **Ana** 26 – 6 | 20 |
| Bruno vs Celia | **Bruno** 18 – 14 | 4 |
| Celia vs Ana | **Celia** 20 – 12 | 8 |

Everyone finishes **1–1**. Copeland ties all three, the [Smith set](../concepts/../../07_Concepts/topics/smith_set.md) is the whole field, and the cycle rule decides the election by itself.

## Two rules, two winners

| | Tie-break rule | Reads | Elects |
|---|---|---|:--:|
| **Ranked Robin** (Equal Vote) | largest **net win margin** | Ana +12 · Celia +4 · Bruno −16 | **Ana** |
| **Consensus Choice** (Better Choices for Democracy) | **Most Wins, Smallest Loss** | Celia lost by 4 · Ana by 8 · Bruno by 20 | **Celia** |

Ana wins on margins because she *crushes* Bruno by 20 — a big win inflates her net. Celia wins on smallest-loss because she is the one who was *barely* beaten: her single defeat is 4 votes, the mildest in the field. Neither rule is a mistake. They are answering different questions — "who piled up the most net support?" versus "who came closest to going undefeated?"

**This is the whole practical difference between the two brands**, and it only ever surfaces here, inside a cycle.

## Run it

| Case (page) | What it shows | src |
|---|---|:--:|
| [Ranked Robin vs Consensus Choice](cases/cases_pages/rr_vs_mwsl_cycle_c3_b32.md) | the same 32 ballots elect Ana under Ranked Robin and Celia under Consensus Choice | [`.yaml`](cases/rr_vs_mwsl_cycle_c3_b32.yaml) |

The engine computes the **Ranked Robin** answer (it implements Copeland plus the margins tiebreak). The **Consensus Choice** answer is read straight off the same pairwise matrix the engine prints — smallest loss, no extra machinery needed. Full report: [`_tabulated`](cases/cases_tabulated/rr_vs_mwsl_cycle_c3_b32_tabulated.txt).

## An honest footnote on the source

The Most Wins, Smallest Loss rule is stated in Wes Holliday's [*How to Make Every Voter Matter and Make Spoiler Effects Go Away*](https://www.betterchoices.vote/news/how-to-make-every-voter-matter-and-make-spoiler-effects-go-away) (Better Choices for Democracy, 2026), whose appendix works a cycle of its own: Amy beats Cat, Cat beats Ben, Ben beats Amy, with losses of 2,000 / 6,000 / 4,000. **On that example the two rules agree** — Amy has both the smallest loss and the best net margin, so Ranked Robin would elect her too. We had to construct the case above to make them come apart, which is a fair reflection of how close these two proposals are.

Holliday's paper also argues the rule is **immune to spoilers** under a precise definition — if Ana would win without Bruno, and would beat Bruno head-to-head, then adding Bruno cannot make them both lose. That is a real and defensible property, and narrower than the everyday phrase "spoiler-proof" suggests; it is not [independence of irrelevant alternatives](../../07_Concepts/topics/), which no ranked method can have. Worth reading rather than dismissing: he is the co-author of [Split Cycle](../../method_comparisons/split_cycle/).

---

*Concepts: [Ranked Robin vs. Consensus Choice](../concepts/ranked_robin_vs_consensus_choice.md) (the brands compared) · [Cycle resolution](../concepts/cycle_resolution.md) (why Minimax, Ranked Pairs and Schulze exist) · [What should we call this method?](../concepts/what_to_call_this_method.md). Up: [05_Ranked_Robin](../).*

# file: README.md
