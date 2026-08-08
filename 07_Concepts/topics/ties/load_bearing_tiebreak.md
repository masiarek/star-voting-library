# The load-bearing tiebreak — when a coin flip picks between two methods' answers

**Level: 301 · deep dive**

**One line:** in a 34-voter election, an IRV first-round tie decides the winner — and the two legal branches are not two arbitrary names but the answers of *two different families of voting theory*, which is why "our engine and theirs disagree" turned out to be the least interesting thing about it.

The case: [`coombs_ex20_district1`](../../../method_comparisons/felsenthal_paradoxes/cases/cases_pages/coombs_ex20_district1.md) ([yaml](../../../method_comparisons/felsenthal_paradoxes/cases/coombs_ex20_district1.yaml)). Found by [cross-checking against rcv-lab.org](../../tabulation_engines/rcv_lab_irv_crosscheck.md#the-one-disagreement-and-it-was-ours), confirmed by [RCTab](../../tabulation_engines/rctab.md).

---

## The election

Felsenthal's Example 20, District I — 34 voters, three candidates, Felsenthal's own A/B/C labels:

<!-- ballots:coombs_ex20_district1 -->
Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
9:A>B>C
9:B>C>A
11:C>A>B
5:C>B>A
```
<!-- /ballots -->

First choices: **C 16, A 9, B 9.** A majority is 18, so nobody has one and somebody must be eliminated. IRV eliminates the fewest first choices — and A and B are level on 9.

## The deadlock, and the two branches

There is no rule left to appeal to. Both eliminations are legal, and they do not merely shuffle the margin — they elect different people:

| Eliminate | Their ballots go to | Result | Winner |
|---|---|---|---|
| **A** (9 × `A>B>C`) | B | B 18, C 16 | **B** |
| **B** (9 × `B>C>A`) | C | C 25, A 9 | **C** |

Note who is *not* in that column. The tie is between **A and B**, and A cannot win on either branch — eliminate A and B wins; eliminate B and C wins. A is a kingmaker who can never be king. The coin flip is nominally about A-versus-B and actually about **B-versus-C**, which is why reading only the tied pair tells you nothing about what is at stake.

Our engine's count, which takes the first branch:

<!-- report:coombs_ex20_district1 -->
```text
--- RCV / Instant-Runoff Voting (single winner) ---
  Coombs Ex.20 — District I: 34 voters, Coombs elects B
 Tabulating 34 ballots (ranked ballots).

ROUND 1
Candidate      Votes  Status
-----------  -------  --------
C                 16  Hopeful
B                  9  Hopeful
A                  9  Rejected

FINAL RESULT
Candidate      Votes  Status
-----------  -------  --------
B                 18  Elected
C                 16  Rejected
A                  0  Rejected


Winner(s) — RCV / Instant-Runoff Voting (single winner)
  B
```
<!-- /report -->

## Three engines, three different disclosures

Same ballots, same rules, three implementations:

| Engine | Eliminates | Winner | Says it broke a tie? |
|---|---|---|:--:|
| this repo's vendored `pyrankvote` | A | **B** | ❌ no |
| [rcv-lab.org](../../tabulation_engines/rcv_lab_irv_crosscheck.md) | B | **C** | ❌ no |
| [RCTab 2.1.0](../../tabulation_engines/rctab.md) (VVSG-tested) | B | **C** | ✅ yes |

Only the certified tabulator prints it:

```text title="Abridged for the lesson — RCTab audit lines, not a full report"
INFO: Candidate "B" lost a tie-breaker in round 1 against "A".
      Each candidate had 9 vote(s). The selected candidate appeared latest in
      the tie-breaking permutation list.
```

And because RCTab's tiebreak is a *declared* setting rather than an accident, the branch can be steered on purpose. Sweeping its candidate order over all six permutations returns **C three times and B three times** — both answers reachable, neither privileged. (The mechanics of declared-versus-accidental tiebreaks are [batch elimination § what a certified tabulator does instead](batch_elimination.md#what-a-certified-tabulator-does-instead); this page is about what the two branches *mean*.)

A fourth reading is worth adding, because it does not pick a branch at all. `pref_voting`'s `instant_runoff` uses the [batch convention](batch_elimination.md) — eliminate *everyone* tied for last — so it removes **A and B together**, leaving C standing alone:

```text title="Abridged for the lesson — a one-liner, not a full report"
instant_runoff       -> ['C']         # batch: A and B both eliminated at once
instant_runoff_put   -> ['B', 'C']    # every legal order, union of the winners
coombs               -> ['B']         # no tie to break; see below
```

So of the four IRV readings available, **three reach C and only ours reaches B** — and [Parallel Universe Tiebreaking](parallel_universe_tiebreaking.md), which refuses to choose and returns the union of every legal elimination order, names exactly the two candidates this page is about.

## Why this tie is load-bearing

Here is the part that makes it a 301 rather than a curiosity. **The profile is a Condorcet cycle:**

| Pair | Winner | Margin |
|---|---|---:|
| A vs B | A | 6 (20–14) |
| B vs C | B | 2 (18–16) |
| C vs A | C | 16 (25–9) |

A beats B, B beats C, C beats A. There is **no Condorcet winner**, and the [Smith set](../smith_set.md) is the whole field — so there is no outside standard the tiebreak can be checked against. That is what "both are legal" really means here: it is not that we lack information about the right answer, it is that the profile does not contain one.

But the two branches are not therefore equivalent, and this is the substantive finding: **each branch is the answer of a different family of methods.**

| Branch | Winner | Who else lands there |
|---|---|---|
| eliminate A | **B** | **Coombs** — and IRV under our tiebreak |
| eliminate B | **C** | **Minimax, Ranked Pairs, Schulze, Split Cycle, Stable Voting** — every C2 cycle-resolution rule in the library |

The Condorcet family's agreement on C has a clean mechanism, and it is worth being able to state rather than assert. Take each candidate's **worst pairwise loss**: A loses to C by 16, B loses to A by 6, C loses to B by 2. C's worst defeat is the mildest in the field, so [Minimax](../../../method_comparisons/felsenthal_paradoxes/README.md) elects it, and on a three-candidate cycle the other C2 rules follow. Meanwhile [Copeland / Ranked Robin](../../../05_Ranked_Robin/01_Learn/cycle_resolution.md) reports **{A, B, C}** — a genuine three-way tie, because in a perfect 3-cycle every candidate is 1–1.

So the coin flip is not choosing between two names. It is silently choosing between *"elect the candidate whose worst defeat is smallest"* and *"elect the candidate the elimination order happens to spare."* An arbitrary rule is arbitrating a real disagreement in social choice theory, and no report mentions that it did.

## The contrast that proves the tie belongs to IRV, not to the ballots

Coombs elects **B** here too — and it gets there **without any tie at all**. Coombs eliminates the candidate with the most *last*-place votes, and those are decisive:

| | first places | last places |
|---|---:|---:|
| A | 9 | **14** |
| B | 9 | 11 |
| C | 16 | 9 |

A is the unique maximum on 14, so Coombs deletes A by its own rule, B reaches 18 of 34, and the count is over. Read from the **top** the field is deadlocked 9–9; read from the **bottom** it is 14–11–9 and perfectly decisive.

That is the sharpest available demonstration that the indeterminacy is a property of *the elimination criterion*, not of the electorate. The voters expressed enough to separate these candidates. IRV's rule looks at the one end of the ballot where they happen to be level, and then needs a coin. This is the same asymmetry [Tie-breaking: STAR vs RCV-IRV](tiebreaking_star_vs_irv.md) argues in general — strict ranks give a tiebreak *fewer signals to work with*, so a tie is harder to resolve and costlier when it lands.

**Keep the scope honest, though.** Coombs is not being recommended here — it is the case's own subject precisely because it *fails* reinforcement, electing B in both districts and A over their union. Neither does this show IRV picking a bad winner: in a cycle, "bad" has no referent. What it shows is narrower and more useful: the count reached its answer by a route the ballots did not determine, and a different legal route was one line of config away.

## What this means for cross-checking

The IRV sweep against RCTab reported **68 of 69 cases agreeing**. The temptation is to read that as 68 determinate results. It isn't:

- **Agreement is not determinacy.** Eight of the 69 needed a tiebreak to reach an answer at all. Where two engines happen to break a tie the same way, a cross-check prints a green check and conceals exactly the fragility this page is about.
- **The disagreement was the useful output.** One case out of 69 disagreed, and it turned out to be the only one whose fragility anybody had written down. That is the correct ratio to expect from a good corpus, not a defect rate.
- **The fix is to sweep the lever, not to add engines.** A fourth implementation would most likely just pick a branch. What actually exposes a load-bearing tie is re-running the *same* engine under every declared tiebreak order — `--candidate-orders all` — and seeing whether the winner moves.

The general form: **a silent tiebreak is indistinguishable from a determinate result.** Any teaching page that leans on an IRV elimination order in a small hand-built electorate is worth re-reading with that in mind — which is how this one was caught.

## Honest limits

1. **Small electorates only.** An exact first-choice tie among 34 voters is unremarkable; among 34,000 it is vanishingly unlikely. This is a hazard of *hand-built teaching cases* first and of real elections a distant second — the same caveat [the rest of this hub carries](why_contrived_tie_cases.md).
2. **The paradox the case exists for is untouched.** District II and the amalgamated file have no tie and elect B and A outright, so Coombs' [reinforcement failure](../../voting_paradoxes/coombs.md) stands exactly as published. Only the incidental claim *"IRV elects B here too"* needed narrowing to *"IRV elects B under our tiebreak."*
3. **None of this is an argument against IRV as such.** [Center squeeze](../../../06_Other/RCV_IRV/concepts/RCV_IRV_center_squeeze.md), [non-monotonicity](../../../06_Other/RCV_IRV/concepts/RCV_IRV_non_monotonicity.md) and [exhausted ballots](../../../06_Other/RCV_IRV/concepts/RCV_IRV_exhausted_ballots.md) are structural; this is a tie clause, and [every method has one](ties_are_forced.md). The criticism that lands is about *disclosure* — two of three engines resolved a decisive tie without saying so — and it is a criticism of implementations and reports, not of instant runoff.

## Sources

- Dan S. Felsenthal (2010), *Review of paradoxes afflicting procedures for electing a single candidate*, Appendix A7, Example 20 — the source profile. **Lean:** neutral; an academic survey.
- [RCTab](https://www.rcvresources.org/rctab) v2.1.0, Bright Spots / Ranked Choice Voting Resource Center — the VVSG-tested tabulator whose audit log prints the tie. **Lean:** RCV-advocacy-adjacent publisher, but the artifact is certified software and the log line is a fact about the count.
- [`pref_voting`](https://pref-voting.readthedocs.io/) (Holliday & Pacuit) — the Condorcet-family winners and the Coombs count, via [`cycle_resolution_report.py`](../../tabulation_engines/cross_checking_with_pref_voting.md). **Lean:** neutral; an academic library.
- Reproduce every number here with [`rctab_sweep.py` / `rctab_crosscheck.py`](../../../STARVote_LH_tabulation_engine/tools_adam/rctab_tabulation_engine/README.md).

## Related

- [Ties & Tie-Breaking hub](README.md) · [Ties Are Forced](ties_are_forced.md) — why no rule can always name one winner
- [Batch elimination](batch_elimination.md) — the other answer to a mid-count tie, and the declared-vs-accidental tiebreak comparison
- [Parallel Universe Tiebreaking](parallel_universe_tiebreaking.md) — the method that refuses to pick a branch and reports the union instead; it would return **{B, C}** here
- [Cycle resolution in Ranked Robin](../../../05_Ranked_Robin/01_Learn/cycle_resolution.md) · [The Smith set](../smith_set.md) · [Coombs' paradoxes](../../voting_paradoxes/coombs.md)
- [Cross-checking against rcv-lab.org](../../tabulation_engines/rcv_lab_irv_crosscheck.md) · [RCTab](../../tabulation_engines/rctab.md)
