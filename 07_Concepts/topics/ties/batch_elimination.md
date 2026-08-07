# Batch elimination — what happens when the batch is *everyone*

*Every statement of instant-runoff voting says "eliminate the candidate with the fewest first choices." Almost none of them say what to do when **two** candidates are tied for fewest. One standard answer — the one the Stanford Encyclopedia uses, and the one `pref_voting` implements — is to remove **all** of them in a single step. That reads like a harmless shortcut, and usually it is. But push it and it does something startling: sometimes **every remaining candidate** is tied for last, the batch takes the whole field, and the count stops with nobody to elect. The convention's answer is that **all of them tie for the win** — and on a perfectly symmetric profile that is not a cop-out, it is the only answer a fair rule is allowed to give.*

**Level: 301 · deep dive**

Part of the [Ties & Tie-Breaking](README.md) hub · the theorem underneath it: [Ties Are Forced](ties_are_forced.md) · the sibling convention: [Parallel Universe Tiebreaking](parallel_universe_tiebreaking.md) · the methods affected: [RCV-IRV (Hare)](../../../06_Other/RCV_IRV/concepts/RCV-IRV-Hare.md) · [Coombs](../../../06_Other/RCV_IRV/concepts/variants/RCV-IRV-Coombs.md)

*In the literature this rule is **"drop them all"** (Taylor & Pacelli, 2006), listed alongside Parallel Universe Tiebreaking in [Tie-Breaking: STAR vs RCV-IRV § 5](tiebreaking_star_vs_irv.md#5-reproducibility-and-consistency). That page names it in a sentence; this one works it.*

---

## The idea in three steps

The whole thing is one clause with two consequences, and it is much easier to follow if the three are separated:

1. **The tie clause.** "Eliminate the candidate with the fewest first choices" is undefined when several are tied for fewest. Batch elimination defines it: **remove them all, in one step.**
2. **The batch can be total.** Nothing stops "all candidates tied for fewest" from meaning *all candidates*. When it does, the elimination step empties the field.
3. **The stopping rule.** With nobody left, the count halts and reports **every candidate in that final batch as tied for the win.**

Step 3 is the one that surprises people, and it is the one with a real argument behind it. It is not "the method broke." On the profiles where it usually fires, a tie is the *only* result an [anonymous and neutral](ties_are_forced.md#the-three-axioms) rule can produce.

## Step 1 — the tie clause the textbooks skip

[Ties Are Forced](ties_are_forced.md) catalogues four ways to resolve a tie **at the end** of a count. [Parallel Universe Tiebreaking](parallel_universe_tiebreaking.md) covers the harder one: a tie **in the middle**, over who to eliminate, where the choice reshapes every round after it. That page lists three answers, and batch elimination is the second:

| Answer | What it does | What it costs |
|---|---|---|
| **Pick one** | break the tie by lot, statute, or a seeded RNG, then continue down that single path | the result is arbitrary, and the arbitrariness is invisible in the report |
| **Batch-eliminate** | remove **all** candidates tied for last in one step | can delete a candidate who would have survived — and, as below, can delete *everybody* |
| **PUT** | branch on every legal elimination, union the winners | the winner set can grow; the search is combinatorial |

Batch elimination's appeal is that it needs no lot, no seed, and no statute. It is a *rule*, not a coin, so it keeps the method anonymous and neutral. That is exactly why the strange behaviour below is the price of something worth having, rather than an oversight.

## Step 2 — the smallest election where the batch takes everything

Three voters, three candidates, rotating ballots — the runnable case is [`batch_all_out_cycle_c3_b3`](../../../06_Other/RCV_IRV/cases/cases_pages/batch_all_out_cycle_c3_b3.md):

| Voter | Ballot |
|:--:|---|
| 1 | Amy > Bruno > Clara |
| 2 | Bruno > Clara > Amy |
| 3 | Clara > Amy > Bruno |

```text title="Abridged for the lesson — not verbatim engine output"
First choices:  Amy 1 · Bruno 1 · Clara 1      majority = 2 of 3 → nobody has it
Fewest first choices: Amy, Bruno and Clara      ← all three, tied
Batch-eliminate all of them  →  no candidates remain  →  STOP
Result: Amy, Bruno and Clara TIE for the win
```

That is the entire mechanism. There is no round two, because there is nothing to transfer to.

**And Coombs empties too, by the mirror route.** [Coombs](../../../06_Other/RCV_IRV/concepts/variants/RCV-IRV-Coombs.md) eliminates the candidate ranked **last** by the most voters instead of first by the fewest. On these ballots each candidate is last exactly once — Clara on ballot 1, Amy on ballot 2, Bruno on ballot 3 — so Coombs' batch is the whole field as well. Both ends of the ballot give up at the same moment, which is a good sign that what is running out is not the *rule* but the *information*.

## Step 3 — why "everybody ties" is the correct answer here, not a shrug

Look at the three ballots again and rename the candidates: Amy → Bruno, Bruno → Clara, Clara → Amy. The ballots become `Bruno>Clara>Amy`, `Clara>Amy>Bruno`, `Amy>Bruno>Clara` — **the same three ballots**, listed in a different order.

That is the whole argument:

- **Anonymity** says reordering the ballots cannot change the outcome. So the relabelled election must produce the same result as the original.
- **Neutrality** says relabelling the candidates must *permute* the outcome the same way. So if Amy won the original, Bruno must win the relabelled one.

Both cannot hold with a single winner. The only outcome that satisfies both is the set `{Amy, Bruno, Clara}` — a genuine three-way tie, forced by symmetry alone. This is [Moulin's proposition](ties_are_forced.md#the-theorem) at its smallest, and this repo already runs the six-voter version of the same profile as [`reinf_north_c3_b6_rr`](../../../method_comparisons/reinforcement_paradox/cases/cases_pages/reinf_north_c3_b6_rr.md), where [Ranked Robin](../../../05_Ranked_Robin/01_Learn/ranked_robin.md) reaches the same dead end from the pairwise direction and falls to the lot.

So when someone says a total batch is "the only result possible for an anonymous and neutral voting method," **on this profile they are right** — and it is worth being precise about which profiles that covers.

## What it costs — a three-way tie in an election that has a clear winner

Change exactly one ballot. Voter 2 now says `Bruno>Amy>Clara` instead of `Bruno>Clara>Amy` — the runnable case is [`batch_all_out_condorcet_c3_b3`](../../../06_Other/RCV_IRV/cases/cases_pages/batch_all_out_condorcet_c3_b3.md):

| Voter | Ballot |
|:--:|---|
| 1 | Amy > Bruno > Clara |
| 2 | **Bruno > Amy > Clara** |
| 3 | Clara > Amy > Bruno |

That swap breaks the cycle and hands the election an undisputed [Condorcet winner](../condorcet/README.md): **Amy beats Bruno 2–1 and beats Clara 2–1.** She is preferred head-to-head to everybody.

It changes nothing about the instant-runoff count. First choices are still 1–1–1, nobody has a majority, all three are still tied for fewest — so the batch is still total, and batch IRV still reports a **three-way tie**.

| Count | Result |
|---|---|
| Batch instant-runoff | **{Amy, Bruno, Clara}** — total batch, tie |
| [Coombs](../../../06_Other/RCV_IRV/concepts/variants/RCV-IRV-Coombs.md) | **{Amy}** — Clara is last on 2 ballots to Bruno's 1 and Amy's 0, so exactly one candidate is cut and the count proceeds |
| [Ranked Robin](../../../05_Ranked_Robin/01_Learn/ranked_robin.md) / Copeland | **{Amy}** |

**This is the honest cost, and it is precise.** The symmetry defence from step 3 does *not* apply here, because this profile is not symmetric — a fair rule can absolutely name a winner, and two of them do. Batch elimination declines to, because its tie clause looks only at first-choice counts and this profile is tied there. The convention's problem is not that it produces ties; it is that it produces them **in elections that did not need one**.

Note which way the Hare/Coombs comparison falls here. Coombs is usually sold as the [center-squeeze](../../../06_Other/RCV_IRV/concepts/RCV_IRV_center_squeeze.md) fix; this is a second, quieter advantage — reading the bottom of the ballot gives the elimination step a different signal to work with, so it runs out of information less often.

## It is not a round-one curiosity

The field can empty at any round. [`batch_all_out_round2_c4_b6`](../../../06_Other/RCV_IRV/cases/cases_pages/batch_all_out_round2_c4_b6.md) adds a fourth candidate whom **every** voter ranks dead last:

```text title="Abridged for the lesson — not verbatim engine output"
Round 1:  Alex 2 · Bella 2 · Colin 2 · Dev 0    Dev is the unique fewest → out alone
                                                 (nobody ranked Dev first → nothing transfers)
Round 2:  Alex 2 · Bella 2 · Colin 2            majority = 4 of 6 → nobody has it
                                                 all three tied for fewest → batch takes the field
Result: Alex, Bella and Colin tie.  Dev does not.
```

**Dev's exclusion is what [Pareto](ties_are_forced.md#the-three-axioms) buys you.** Every voter prefers all three others to Dev, so no rule worth defending can seat him — which is exactly the job Pareto does in Moulin's proposition: anonymity and neutrality force a tie among the symmetric candidates, and Pareto is what keeps a universally-rejected candidate out of it. Without it, "we could not separate the good candidates" would slide into "so let's call it a four-way tie."

## What this repo's engine does instead — a ladder, then a coin

Our vendored [RCV-IRV engine](../../../06_Other/RCV_IRV/RCV_IRV_tabulation_engine/rcv_irv_tabulation.py) (pyrankvote) does not batch. It has a **tiebreak ladder**, and it is a better one than it usually gets credit for — `_cmp_candidate_vote_counts` in `pyrankvote/helpers.py` breaks a first-choice tie on **most second choices**, then third, then fourth, and only falls to `random.choice` once it runs out of ranks. Structurally that is STAR's ladder: use the ballots while they still say something, and flip a coin only when they have stopped.

So the honest statement is narrower than "the engine flips a coin on ties." It is: **the coin is reached only when the candidates are tied at *every* rank** — which is exactly the profile this page is about, and exactly the [dead rung](../../../01_STAR/03_Criteria/tie_break_dead_rung/README.md) by another name.

The control case proves the ladder works. Run all six row-orderings of the [Condorcet-winner profile](#what-it-costs-a-three-way-tie-in-an-election-that-has-a-clear-winner) above, where second choices are Amy 2, Bruno 1, Clara 0 — **all six elect Amy.** The ladder has information, it uses it, and the row order is irrelevant.

Now the perfect cycle, where each candidate holds exactly one first, one second and one third choice, so the ladder is dead on arrival:

<!-- report:batch_all_out_cycle_c3_b3 -->
```text
--- RCV / Instant-Runoff Voting (single winner) ---
  Batch elimination empties the field — the perfect cycle
 Tabulating 3 ballots (ranked ballots).

ROUND 1
Candidate      Votes  Status
-----------  -------  --------
Amy                1  Hopeful
Bruno              1  Hopeful
Clara              1  Rejected

FINAL RESULT
Candidate      Votes  Status
-----------  -------  --------
Amy                2  Elected
Bruno              1  Rejected
Clara              0  Rejected


Winner(s) — RCV / Instant-Runoff Voting (single winner)
  Amy
```
<!-- /report -->

**Amy, cleanly and reproducibly — and for no reason found on the ballots.** Run the identical three ballots in a different row order and the answer changes. All six orderings, same votes, same voters, only the typing order different:

| Row order | Winner |
|---|:--:|
| Amy · Bruno · Clara | **Amy** |
| Amy · Clara · Bruno | **Amy** |
| Bruno · Amy · Clara | **Bruno** |
| Bruno · Clara · Amy | **Bruno** |
| Clara · Amy · Bruno | **Clara** |
| Clara · Bruno · Amy | **Clara** |

The winner is always the **first row's first choice**. That is not a neutrality failure — it is an **anonymity** failure, the more basic of the two: *who cast which ballot* is supposed to be the one thing a voting rule provably ignores, and here the data-entry order decides the election.

**The mechanism, since "it's random" would be the wrong summary.** The engine sets `random.seed(0)` so counts reproduce run to run, and they do. But `sorted()` feeds the comparator pairs in an order determined by the input list, and that list is built in order of each candidate's **first appearance across the ballot rows**. A fixed seed therefore pins the *sequence of coin flips*, not the *candidate* each flip lands on. Seeding buys reproducibility across runs and buys nothing at all across ballot orderings — and nothing in the report says which of the two you are looking at.

This reframes the comparison the [PUT page](parallel_universe_tiebreaking.md#three-answers-and-what-each-conceals) sets up. Its table warns that batch elimination "can delete a candidate who would have survived" — true, and this page adds the other half: **once the ladder is dead, the alternatives are worse.** A published [lot order](../../GLOSSARY.md) spends neutrality *in advance and in public*, which is defensible. Spending anonymity by accident, on whichever ballot happened to be typed first, is not.

Stated fairly, then: the defect is not the ladder and not the seed. It is that the report draws no distinction between a winner the ballots chose and a winner the file order chose. → [engine limitations](../../../06_Other/RCV_IRV/RCV_IRV_tabulation_engine/README.md#known-limitation-elimination-ties).

## Cross-checked against an engine nobody here wrote

Per this library's [standing rule](../../tabulation_engines/cross_checking_with_pref_voting.md), the claims above are confirmed against `pref_voting` (Holliday & Pacuit), whose `instant_runoff` and `coombs` both implement the batch convention:

| Profile | `instant_runoff` | `coombs` | `copeland` | LH engine |
|---|---|---|---|---|
| Perfect cycle (3 voters) | **{Amy, Bruno, Clara}** | **{Amy, Bruno, Clara}** | {Amy, Bruno, Clara} | Amy — row-order dependent |
| Condorcet winner present (3 voters) | **{Amy, Bruno, Clara}** | **{Amy}** | {Amy} | Amy |
| Round-2 batch (6 voters, 4 candidates) | **{Alex, Bella, Colin}** | **{Alex, Bella, Colin}** | {Alex, Bella, Colin} | Alex |

```bash
uv run python -c "from pref_voting.profiles import Profile; from pref_voting.iterative_methods import instant_runoff, coombs; p=Profile([[0,1,2],[1,0,2],[2,0,1]]); print(instant_runoff(p), coombs(p))"
```

## The honest limits

1. **This is a small-electorate and simulation concern.** A total batch needs every remaining candidate to hold *exactly* the same first-choice count. Among thousands of ballots that is astronomically rare, and the same [caveat](why_contrived_tie_cases.md) the rest of this hub carries applies here undiminished. What it is not is a curiosity you can define away — see the theorem.
2. **It is a convention, not a law.** Real statutes overwhelmingly pick one candidate by lot and continue. Batch elimination is the convention of the academic literature and the reference implementations; do not describe it as "how IRV works" without saying which IRV. [Which RCV-IRV?](../../../06_Other/RCV_IRV/concepts/variants/RCV_IRV_variants.md) catalogues the others.
3. **It fixes none of IRV's real problems.** [Center squeeze](../center_squeeze/README.md), [non-monotonicity](../monotonicity/README.md) and exhausted ballots come from the elimination *structure*, not from its tie clause. Citing the batch convention as a repair would be exactly the overreach this library warns against.
4. **"Batch elimination" also names a different thing.** In statute — North Carolina's, for one — it usually means dropping every candidate who is *mathematically out of reach* at once, purely to speed a hand count. That is a different rule with a different justification; see [Hare § batch](../../../06_Other/RCV_IRV/concepts/RCV-IRV-Hare.md). This page is about the tie clause.

## Sources

- Alan D. Taylor & Allison M. Pacelli, *Mathematics and Politics* (2nd ed., Springer, 2006) — the named statement of the rule, "drop them all," together with the observation that it only terminates if you declare everyone eliminated in the final round to be co-winners. This library already cited it in [Tie-Breaking: STAR vs RCV-IRV § 5](tiebreaking_star_vs_irv.md#5-reproducibility-and-consistency); this page is the worked version. **Lean:** neutral; a textbook.
- Eric Pacuit, "Voting Methods," *Stanford Encyclopedia of Philosophy* — states Hare and Coombs with the batch convention, removing all of the poorly-performing candidates in each round. **Lean:** neutral; the standard reference.
- Wesley H. Holliday & Eric Pacuit, [`pref_voting`](https://pref-voting.readthedocs.io/) — `instant_runoff`, `coombs` and their `_put` variants; the cross-check engine used above. **Lean:** neutral; an academic library.
- Hervé Moulin, *The Strategy of Social Choice* (North-Holland, 1983) — the forced-tie proposition behind step 3. Via [Ties Are Forced](ties_are_forced.md).
- Clyde Coombs, *A Theory of Data* (1964) — the Coombs rule. Via [RCV-IRV (Coombs)](../../../06_Other/RCV_IRV/concepts/variants/RCV-IRV-Coombs.md).

## Related

- [Ties & Tie-Breaking hub](README.md) · [Ties Are Forced](ties_are_forced.md) — the theorem that makes step 3 an argument rather than an excuse
- [Parallel Universe Tiebreaking](parallel_universe_tiebreaking.md) — the other answer to a mid-count tie, and the four-voter case where it and batch elimination disagree
- [Why build "silly" tie elections?](why_contrived_tie_cases.md) · [Tie-Breaking: STAR vs RCV-IRV](tiebreaking_star_vs_irv.md)
- [RCV-IRV (Coombs)](../../../06_Other/RCV_IRV/concepts/variants/RCV-IRV-Coombs.md) · [RCV-IRV (Hare)](../../../06_Other/RCV_IRV/concepts/RCV-IRV-Hare.md) · [Which RCV-IRV?](../../../06_Other/RCV_IRV/concepts/variants/RCV_IRV_variants.md)
- [Cycle resolution in Ranked Robin](../../../05_Ranked_Robin/01_Learn/cycle_resolution.md) · [The Smith set](../smith_set.md) · [Glossary](../../GLOSSARY.md)
