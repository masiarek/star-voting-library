# RCV Lab (rcv-lab.org) — an outside engine, and a source of countable ballots

**Level: reference · deep dive**

**One line:** a free ranked-choice voting platform that publishes its sample elections as **downloadable cast vote records**, which makes it something this library can actually use — not another site to link, but a source of real ballots to re-count independently.

→ verified reproduction: [the "Best Cycle-Breaking Rule" cases](../../method_comparisons/cycle_resolution/README.md) · **it also counts *our* cases: [all 64 IRV cases cross-checked](rcv_lab_irv_crosscheck.md)** · sibling referees: [`pref_voting`](cross_checking_with_pref_voting.md) · [BetterVoting](bettervoting_and_the_engine.md) · the other Sankey tool, which counts nothing: [RCVis](rcvis.md).

---

## What it is

[rcv-lab.org](https://rcv-lab.org/) is a ranked-choice election platform: design a ballot, open it for voting by link or token, watch the count, and explore the result through bar charts, Sankey diagrams, a pairwise table, and a per-ballot trace. Voters need no account. It also runs in **analysis-only** mode — upload a CVR or a results file and it will tabulate and visualize without hosting anything.

It is operated by the **Kaphan Foundation**, a Seattle 501(c)(3) private foundation established in 2003 by Shel Kaphan, Amazon's first employee. The service is free, ad-free, and states it does not sell user data. The domain was registered **2026-02-28** and the Terms of Service are marked *"Initial release (soft launch)"* — this is a young platform, and it says so.

**Disclose the lean, per house practice.** The foundation funds democracy-reform causes, and the platform is *RCV*-branded and RCV-shaped: its first-class methods are IRV and STV. It is not a neutral arbiter between ranked and scored ballots, and it does not tabulate STAR. That does not make its arithmetic suspect — our reproduction below says otherwise — but it is a reason to take its **data** and not its **verdicts**.

## The caveats it states about itself

Worth quoting plainly, because they bound what we can cite:

- **Not a certified voting system.** It says explicitly it should not be the system of record for any binding government election.
- **Beta.** *"Tabulation behavior may be updated as algorithms are refined; ballots, accounts, or data may be reset."* A number read off the live site today is not guaranteed to be the number tomorrow.

The practical consequence for this repo: **freeze what you use.** Download the CVR, commit it as a case file, and cite our own count — the same discipline the [BetterVoting exports](bettervoting_and_the_engine.md) get. Never cite a live rcv-lab result as a stable fact.

## What it counts

Single-winner **IRV**; multi-winner **STV** by Meek's method or WIGM; **equal-rank** ballots, where ranking N candidates together splits the ballot's weight N ways. Plurality, approval, and cumulative voting appear as comparison-only counts. No STAR, no Score, no Ranked Robin — for those, this library's own engines remain the only route.

Two features are unusual enough to note. It can **cross-check against RCTab** — the tabulator used by real US jurisdictions — from a second engine on the same ballots, which is the same "two implementations, one election" discipline this repo uses. And the Terms advertise an **API and an MCP server**; neither is publicly documented at any obvious endpoint as of 2026-08-08, so treat it as announced rather than available.

## Getting the raw data

This is the part that earns the page. The samples are **plain static files under a predictable path** — no account, no API key, no scraping:

```
https://rcv-lab.org/sample-data/manifest.json
https://rcv-lab.org/sample-data/<id>/<file>
```

`manifest.json` lists every sample with the exact filenames. Each entry has up to three artifacts: a **CVR** (the ballots), a **config** (RCTab rules JSON), and a **summary** (the tabulated report).

| Sample `id` | Ballots | CVR? | What it is |
|---|--:|:--:|---|
| `minneapolis-park-2013` | 80,101 | `.xlsx` | Real. STV, 3 seats, 11 candidates, 11 rounds |
| `minneapolis-park-2013-hare` | 80,101 | `.xlsx` | The same ballots under the Hare quota instead of Droop — a quota comparison for free |
| `portland-me-mayor-2015` | **99** | `.xlsx` | Named for a real race but ships a **reduced fixture** — see the warning below |
| `minneapolis-mayor-2017` | 105,928 | `.xlsx` | Real. IRV, 19 candidates, 6 rounds. **[Reproduced here](../../method_comparisons/minneapolis_2017/README.md)** |
| `maine-governor-primary-2018` | 132,250 | `.xlsx` | Real. The first statewide RCV election in the US |
| `minnetonka-council-2021` | — | ✗ | Summary only (from rcvis.com) |
| `eastpointe-council-2019` | — | ✗ | Summary only (from rcvis.com) |
| `top-three-cookies` | 1,400 | `.csv` | Synthetic. STV, 3 seats, 10 rounds |
| `favorite-font` | 1,100 | `.csv` | Synthetic. IRV, 8 rounds |
| `best-cycle-breaking-rule` | 999 | `.csv` | Synthetic. **Reproduced below** |

**Check the ballot count before trusting a label.** `portland-me-mayor-2015` is presented in the picker as "2015 Portland, Maine Mayor" — a real municipal election that drew roughly nineteen thousand voters. The published file holds **99 ballots**, and RCV Lab's own summary for it says so. It behaves like a test fixture that kept the real election's candidates and round structure while shrinking the electorate, which is a perfectly reasonable thing to ship and a disastrous thing to cite as turnout. The other three real samples are full size; their row counts match their summaries exactly (verified here by counting rows).

Three full-size real elections with their matching official rules files is still the genuinely valuable part — real ranked CVRs are otherwise scattered across county election sites in inconsistent formats. This sits alongside [PrefLib](../topics/condorcet/condorcet_reading_list.md) as a ballot source, and unlike PrefLib it ships the **rules config** next to the ballots.

Fetch one:

```bash
curl -O https://rcv-lab.org/sample-data/best-cycle-breaking-rule/best-cycle-breaking-rule_cvr.csv
```

The CVR is generic-CSV: one row per ballot, `Ballot ID` then one **column per candidate**, and the cell holds that candidate's **rank** (blank = unranked). Note the transposition — most ranked formats put ranks in the columns and candidates in the cells; this one is the other way round, so a naive reader will silently produce nonsense.

## The output format

The summary JSON is **RCTab-compatible** — same `config` / `results` / `summary` shape, same `tallyResults` with `eliminated` / `elected` / `transfers`, same `inactiveBallots` breakdown — so anything that already reads RCTab output reads this. On top of that it adds a `statistics` block that RCTab has no equivalent for, and that block is the interesting one:

- **`condorcet`** — the full pairwise matrix, the beat-order `tiers`, `condorcetWinner` (`null` when preference cycles), and whether the IRV winner was it. An IRV report that volunteers whether it elected the Condorcet winner is a rare and honest thing.
- **`pluralityCounterfactual`** — would plain plurality have picked the same winner? Answers "did the ranking actually change anything here" in one field.
- **`canonical`** — a run-to-completion accounting that keeps eliminating past the declared win, so every ballot ends either with a winner or exhausted. This is where the fractional numbers come from.
- Ballot-shape histograms: bullet-voting rate, full-ranking rate, equal-rank usage, and cumulative exhaustion by round.

One reading trap in that block. `canonical.exhaustedWeight` for our sample is **555 of 999 — 55.6%** — which is *not* the exhaustion the election actually experienced. It is the figure after the count is forced to run to completion and the winner's surplus is trimmed to quota. The exhaustion at the moment the election was decided is **113**. Both numbers are correct answers to different questions; only the second one describes the count that happened.

## What we verified

The `best-cycle-breaking-rule` sample was converted from its CVR into two case files and re-counted here from scratch. Three independent checks, all passing:

1. **The IRV rounds match.** First choices 315 / 313 / 258 / 61 / 52, the three-way round at 324 / 321 / 262 with 92 exhausted, and the final 492 / 394 with 113 exhausted.
2. **The pairwise matrix matches cell for cell**, computed here from the ballots without reference to theirs.
3. **`pref_voting` agrees** on the Condorcet picture as a neutral third referee.

One difference, and it is presentational: the site reports **four** rounds, knocking out Flip a Coin and then Copeland's Rule one at a time; this repo's engine reports **three**, because 52 + 61 = 113 cannot catch Minimax's 258 and it clears both at once. Every tally appearing in both reports is identical. Round *count* is a reporting convention, not a result — worth knowing before anyone cites "it took N rounds" as a fact about an election.

<!-- report:cycle_vote_on_the_rule_irv_c5_b999 -->
```text
--- RCV / Instant-Runoff Voting (single winner) ---
  Best Cycle-Breaking Rule — a society votes on how to break a cycle, and cycles
 Tabulating 999 ballots (ranked ballots).

ROUND 1
Candidate          Votes  Status
---------------  -------  --------
Ranked Pairs         315  Hopeful
Schulze Method       313  Hopeful
Minimax              258  Hopeful
Copeland's Rule       61  Rejected
Flip a Coin           52  Rejected

ROUND 2
Candidate          Votes  Status
---------------  -------  --------
Ranked Pairs         324  Hopeful
Schulze Method       321  Hopeful
Minimax              262  Rejected
Copeland's Rule        0  Rejected
Flip a Coin            0  Rejected
Blank Votes           92  Rejected

FINAL RESULT
Candidate          Votes  Status
---------------  -------  --------
Ranked Pairs         492  Elected
Schulze Method       394  Rejected
Minimax                0  Rejected
Copeland's Rule        0  Rejected
Flip a Coin            0  Rejected
Blank Votes          113  Rejected


Winner(s) — RCV / Instant-Runoff Voting (single winner)
  Ranked Pairs

--- Transfers and inactive ballots (what the round tables leave out) ---
The tables above give each candidate's round total but not where a
transferred vote came FROM, nor how many ballots stopped counting.
Both are recomputed from the ballots, using the eliminations the
count above actually made.

ROUND 1 — 999 of 999 ballots still active; majority = 500
   Flip a Coin eliminated with 52:
      → (no continuing ranking)     44  ← these ballots go inactive
      → Ranked Pairs              4
      → Minimax                   2
      → Schulze Method            2
   Copeland's Rule eliminated with 61:
      → (no continuing ranking)     48  ← these ballots go inactive
      → Schulze Method            6
      → Ranked Pairs              5
      → Minimax                   2

ROUND 2 — 907 of 999 ballots still active (92 inactive); majority = 454
   Minimax eliminated with 262:
      → Ranked Pairs            168
      → Schulze Method           73
      → (no continuing ranking)     21  ← these ballots go inactive

FINAL ROUND — 886 of 999 ballots still active (113 inactive); majority = 444
   Ranked Pairs            492  (55.5% of the still-active)  ← elected
   Schulze Method          394  (44.5% of the still-active)
   Never exhausted, never transferred:
      348 ballots held by Schulze Method carried a lower ranking that was never read
      (the count stopped here, so those preferences did nothing).

Inactive ballots at the final round: 113 of 999 (11.3%).
   Ranked Pairs's 492 is a majority of the 886 still active but only 49.2% of all 999 cast —
   the 'majority' here is of a shrunken denominator. See
   06_Other/RCV_IRV/concepts/RCV_IRV_exhausted_ballots.md
```
<!-- /report -->

### The real one: Minneapolis 2017

The `minneapolis-mayor-2017` CVR is [reproduced here too](../../method_comparisons/minneapolis_2017/README.md) — 105,928 ballots, 18 candidates plus write-ins, converted from the ESS export under the published RCTab rules. Four independent numbers confirm it, none of them used to build the conversion: the leading first-choice tallies, the 1,369 blank ballots, the 38 ballots truncated by the second-skipped-rank rule, and the final pair 46,704 / 34,970.

It is also the case that keeps this library honest — Jacob Frey wins under Plurality, under RCV-IRV, and as the Condorcet winner 18–0, with no cycle anywhere. Two bookkeeping differences survive: round numbering (they batch-eliminate on a different schedule) and exhausted totals differing by 37 of 105,928. Every candidate tally appearing in both reports is identical.

## Why the cycle sample is worth having

The election is a joke with a real edge: five candidates, all of them **cycle-breaking rules**, and the ballots cycle. Ranked Pairs beats Schulze by 98, Schulze beats Minimax by 201, Minimax beats Ranked Pairs by 53 — no [Condorcet winner](../topics/condorcet/README.md), [Smith set](../topics/smith_set.md) of three. A society convened to adopt a completion rule generated precisely the knot a completion rule exists to untie.

The payoff is that the refined rules turn out to be *unanimous*: Minimax, Ranked Pairs, Schulze, Split Cycle, Stable Voting and RCV-IRV all elect **Ranked Pairs**, with Schulze and Minimax each voting for a rival over itself. The one rule that cannot decide is **Copeland's Rule**, which reads only wins and losses — all three cycle members go 3–1, so it returns a three-way tie. This repo's [Ranked Robin](../../05_Ranked_Robin/01_Learn/ranked_robin.md) *is* Copeland, so it hits that tie and breaks it by total margin, landing on **Schulze Method** — a different winner from every margin-reading rule. That divergence is the clearest demonstration in the library of why the refined rules were invented.

Both cases, and the full family table: [cycle resolution, counted](../../method_comparisons/cycle_resolution/README.md).

## Verdict

**Useful, with the beta caveat.** Take the CVRs — five real elections with their official rules files, freely downloadable, is a real asset and hard to get elsewhere. Take the RCTab-compatible JSON shape as a format reference. Treat the live site as a beta whose numbers may move, freeze anything cited, and remember it counts no scored method at all, so it can never be the whole comparison this library is about.

---

*Up: [tabulation engines](README.md) · [07_Concepts](../README.md) · related: [cross-checking with `pref_voting`](cross_checking_with_pref_voting.md) · [BetterVoting and the engine](bettervoting_and_the_engine.md) · [cycle resolution](../../05_Ranked_Robin/01_Learn/cycle_resolution.md).*
