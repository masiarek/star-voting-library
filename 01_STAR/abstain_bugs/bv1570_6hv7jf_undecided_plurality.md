# BV1570 — undecided plurality election still declares a winner

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/6hv7jf) · **[results ↗](https://bettervoting.com/6hv7jf/results)** (election `6hv7jf`) · issue [Equal-Vote/bettervoting#894](https://github.com/Equal-Vote/bettervoting/issues/894)

A Plurality ("choose one") race where every ballot is effectively empty — yet BetterVoting shows a winner **and** the wrong voter count.

## What it teaches

1. **An "undecided" election shouldn't crown anyone.** All three voters decline to pick: one deselects Approve, one leaves everything blank, one deselects Reject. BetterVoting counts all three as abstentions (`nTallyVotes = 0`) but still declares **Approve** the winner ([#894](https://github.com/Equal-Vote/bettervoting/issues/894)).
2. **The voter count is wrong too** — the results view showed **2** voters when there were **3** (part of #894).
3. **LH diverges on the count.** Only the fully-blank ballot abstains; the two ballots carrying an explicit `0` are real tally votes (both options score 0). So LH sees `nTallyVotes = 2`, `nAbstentions = 1`, a **0–0 tie**, resolved to Approve by lot. Same winner, different count — LH counts an explicit `0` as a cast vote (the #884 dispute).

## The ballots

Options: **Approve, Reject** (choose-one). `&` = the BetterVoting `null` (left blank).

| Voter | Approve | Reject | Meaning |
|---|:-:|:-:|---|
| 1 | 0 | `&` | deselected Approve |
| 2 | `&` | `&` | fully blank (true abstention) |
| 3 | `&` | 0 | deselected Reject |

## The result

**Approve is elected** — as a **0–0 tie broken by lot**, from 2 tally votes (not 0).

```text
 Tabulating 3 ballots. Note: 1 of 3 ballots is marked as an abstention.
   Approve -- 0 -- Tied for first place
   Reject  -- 0 -- Tied for first place
   Resolved: ['Approve'] (selected by lot-number priority: CSV column order).

Winner  (Plurality)
 Approve
```

BetterVoting result: `elected: ["Approve"]`, `nTallyVotes: 0`, `nAbstentions: 3`, results view "2 voters".

Full engine detail: [`bv1570_6hv7jf_undecided_plurality_tabulated.txt`](cases/cases_tabulated/bv1570_6hv7jf_undecided_plurality_tabulated.txt) · source [`.yaml`](cases/bv1570_6hv7jf_undecided_plurality.yaml). Part of the [BV abstain issue index](../../00_start_here/tabulation_engines/BV/abstain_issues_index.md).
