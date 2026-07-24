# Cycle Resolution — why Minimax, Ranked Pairs, and Schulze exist

> **Status: draft / Level 301.** A learning page on what happens to Condorcet methods when there's *no* Condorcet winner — and why a whole family of methods exists just to answer that. All examples below are verified with the `pref_voting` engine.
>
> **For the underlying math** — tournaments as graphs, the Smith & Schwartz sets, and each method mapped to its math (Floyd–Warshall, game theory, NP-hardness) — see [The Math Behind Condorcet](the_math_behind_condorcet.md).
>
> **For the wider field** — where Minimax/Ranked Pairs/Schulze sit among *all* the ranked tabulations (Borda, Bucklin, Coombs, Copeland, Dodgson…), see [The ranked-ballot method zoo](../topics/ranked_ballot_methods_zoo.md).

**One line:** when a [Condorcet winner](../GLOSSARY.md) exists, **every** Condorcet method elects them — Ranked Robin, Minimax, Ranked Pairs, Schulze all agree. They differ *only* when majority preference forms a **cycle** (A beats B, B beats C, C beats A, with no one beating all). "Cycle resolution" is the rule a method uses to pick a winner in that case — and it's the *entire* difference between these methods.

→ the cycle itself: [BV2157 — Condorcet cycle (rock-paper-scissors)](../../method_comparisons/paradoxes_and_whoops/bv2157_mmcmpy_condorcet_cycle_rps.md) · the base method: [Ranked Robin](ranked_robin.md) · [`GLOSSARY`](../GLOSSARY.md).

> **Both profiles on this page are now runnable** — [method_comparisons/cycle_resolution](../../method_comparisons/cycle_resolution/README.md). Every winner below is printed by `cycle_resolution_report.py`, which runs all six rules through `pref_voting`; nothing here is asserted from memory.

---

## The problem: majority rule can eat its own tail

Usually one candidate beats every other head-to-head — the **Condorcet winner** — and the choice is obvious. But majority preference isn't guaranteed to be transitive. Sometimes:

> a majority prefers **A > B**, a majority prefers **B > C**, *and* a majority prefers **C > A**.

There is no "beats everyone" candidate — the result is a **cycle** (the [Condorcet paradox](../../method_comparisons/paradoxes_and_whoops/bv2157_mmcmpy_condorcet_cycle_rps.md), known since the 1780s). Now "elect the candidate the majority prefers" has *no* answer, and a method has to break the tie somehow. *How* it breaks it is what separates the methods.

## Why Ranked Robin / Copeland is tie-prone

[Ranked Robin (Copeland)](ranked_robin.md) scores by **pairwise wins − losses**. That's beautifully simple — but in a cycle, candidates tend to share the same record, so it often **can't pick a unique winner**. Concrete example (21 voters, 4 candidates; verified):

```
10 : A>B>C>D       Head-to-heads in the top cycle:
 6 : B>C>A>D            A beats B by 9      B beats C by 11      C beats A by 1
 5 : C>A>B>D       (everyone ranks D last, so A, B, C each beat D)
```

Win–loss record: **A +1, B +1, C +1**, D −3 → **Copeland ties A, B, and C.** The simple count throws up its hands. That tie-proneness is exactly why the refined methods below exist: they look at *how strong* each defeat is, not just who-beat-whom.

## The cycle-resolution methods (same ballots, different rule)

On that same example, each refined method gives a **unique** winner — here, all four pick **A** (the candidate whose only loss, to C, is the smallest at margin 1):

**Minimax** *(simplest)* — elect the candidate whose **worst single defeat is the least bad**. A's biggest loss is just 1; B's is 9; C's is 11 → **A wins.** Intuition: "least strongly beaten." (Caveat: in 4+ candidate fields Minimax can occasionally pick a candidate outside the top cycle / Smith set.)

**Ranked Pairs (Tideman)** — sort every pairwise victory by margin, **largest first**, and "lock in" each one *unless* it would create a cycle with the ones already locked. Here: lock B>C (11), then A>B (9); C>A (1) would close a cycle, so **skip it**. The locked relations read A > B > C → **A wins.**

**Schulze (beatpath)** — A "beats" B if the **strongest chain of defeats** from A to B (its weakest link is its strength) is stronger than the strongest chain back. Follow the strong links and **A wins** here too. (Widely used in practice — Debian, Wikimedia, Ubuntu.)

**Split Cycle** *(newest)* — in **every** cycle, throw away that cycle's **weakest defeat**, then elect whoever is left undefeated. Here the only cycle is A>B>C>A, its weakest link is C>A (margin 1), so it goes — and **A wins**, undefeated. The rule comes from [Holliday & Pacuit (2023)](../topics/condorcet/split_cycle.md), and its defining habit shows up in the next section: when the discarding leaves *two* candidates undefeated, Split Cycle **returns both** instead of picking one.

→ runnable: [the 21-voter profile](../../method_comparisons/cycle_resolution/cases/cycle_copeland_ties_c4_b21.yaml) (cast: Alder / Birch / Cedar / Dogwood).

## …but they don't always agree

In the example above all four landed on A. They **needn't.** A second profile — 40 voters, four candidates, [runnable](../../method_comparisons/cycle_resolution/cases/cycle_schulze_vs_ranked_pairs_c4_b40.yaml) as Ana / Bruno / Chloe / Diego — splits them:

```
 7 : A>B>C>D      B beats A by 4     A beats C by 18
 8 : B>A>C>D      A beats D by 12    B beats C by 18
14 : D>B>A>C      D beats B by 10    C beats D by 12
11 : C>A>D>B
```

| Method | Winner | Why |
|---|---|---|
| Ranked Robin / **Copeland** | **A, B** (tie) | both are 2–1 |
| **Minimax** | **A** | A's worst defeat is 4, the field's mildest |
| **Schulze** | **A** | strongest beatpaths run A's way |
| **Ranked Pairs** | **B** | locks the 18s and 12s first, and they favor B |
| **Split Cycle** | **A, B** | discarding each cycle's weakest defeat leaves *both* undefeated |

Same ballots, and the two "serious" cycle-resolvers **disagree outright** — Schulze elects A, Ranked Pairs elects B. That's the whole point of this page in one table.

**Split Cycle's answer is the interesting one**, and it isn't indecision: its winner set is always a **superset** of Schulze's and Ranked Pairs'. Where those two produce a single name, Split Cycle is claiming they did so by *convention* rather than by evidence — the ballots here genuinely fail to separate A from B, and it hands that back rather than resolving it silently. Whether that's honesty or buck-passing is a real disagreement, and it's the subject of [its own page](../topics/condorcet/split_cycle.md).

A nastier **five-candidate** cycle drives the point home — 77 voters, [runnable](../../method_comparisons/cycle_resolution/cases/cycle_family_splits_c5_b77.yaml) as Ava / Ben / Cole / Dana / Ezra, with **no** Condorcet winner and a Smith set of *all five*:

| Method | Winner | |
|---|---|---|
| Ranked Robin / **Copeland** | **Ava** | Copeland ties Ava & Ben (both 3–1); the margin tiebreak picks Ava (+76 vs +24) |
| **Minimax** | **Ava** | her worst defeat (to Ben, by 3) is the field's mildest |
| **Schulze** | **Ava** | strongest beatpaths run Ava's way |
| **Ranked Pairs** | **Ben** | locks the biggest margins first, and they carry Ben |
| **Split Cycle** | **Ava, Ben** | discarding each cycle's weakest defeat leaves both |

Same ballots, and **Ranked Pairs stands alone at Ben** while every other rule leans Ava — the two "serious" cycle-resolvers, Schulze and Ranked Pairs, disagree outright again. This is the whole point: "Condorcet method" names a *family*, and once you're inside a cycle, the family splits. (Outside cycles — i.e. almost always — they're identical.)

> *An earlier draft here showed an unsourced "100-voter Heitzig" profile from memory; it's replaced by this one, [built by search and verified with `pref_voting`](../../method_comparisons/cycle_resolution/README.md). If you want a **named** profile from the literature, the canonical Schulze-vs-Ranked-Pairs disagreement examples live in [Schulze's own paper](https://arxiv.org/abs/1804.02973) and on [electowiki](https://electowiki.org/wiki/Schulze_method).*

## What they share (the good news)

- **Condorcet-consistent:** all elect the Condorcet winner whenever one exists — which, with many voters and realistic preferences, is the overwhelming majority of elections.
- **Smith-efficient (the good ones):** Ranked Pairs, Schulze, and Copeland always elect from the **[Smith set](../topics/smith_set.md)** (the smallest group that beats everyone outside it). Minimax can miss it.
- **Clone-independent & monotone:** Ranked Pairs, Schulze **and Split Cycle** add these guarantees; that robustness is why they're the "serious" cycle-resolvers despite being harder to explain.
- **Where they part company on criteria:** Split Cycle additionally satisfies *immunity to spoilers* and *positive/negative involvement*, which Schulze and Ranked Pairs fail — the price being those multi-winner answers. The [Split Cycle page](../topics/condorcet/split_cycle.md) checks that trade with a tabulated election in which a candidate **no voter ranks above the winner** still flips Schulze's result.

## Where Ranked Robin and STAR fit

- **Ranked Robin (Equal Vote)** is essentially **Copeland + a margins tiebreak** — a pragmatic choice: cycles are rare, so the simple win-loss count plus a sum-of-margins fallback is usually plenty. (Consensus Choice uses a different fallback, "Most Wins, Smallest Loss" — same family, different cycle rule.) See [Ranked Robin (aka Consensus Voting) — RCV-RR](ranked_robin.md).
- **STAR is *not* a Condorcet method** and doesn't try to resolve cycles at all. Its score-then-runoff just produces a winner, which *can* differ from the Condorcet winner ([BV2156 (STAR's miss)](../../method_comparisons/paradoxes_and_whoops/bv2156_3grpbb_star_misses_condorcet.md)). The trade: these ranked methods capture *pure majority preference* but ignore *intensity*; STAR captures intensity (how much, not just which) at the cost of strict Condorcet guarantees. Neither is "the" right answer — it's a values choice.

## How often do cycles even happen?

Rarely, but not never. Cycles get likelier in **small, sharply three-way-divided** races and much rarer as the electorate grows and preferences spread along a spectrum. As with the [runoff-reversal frequency](../../01_STAR/runoff_overturns_leader/) caveat: any rate you quote depends on the voter model, so state the assumptions rather than a bare number.

## Try it yourself / verify

Both profiles on this page ship as runnable YAMLs in [method_comparisons/cycle_resolution](../../method_comparisons/cycle_resolution/README.md). The repo tool prints every rule at once:

```bash
uv run STARVote_LH_tabulation_engine/tools_adam/pref_voting_tabulation_engine/cycle_resolution_report.py method_comparisons/cycle_resolution/cases/cycle_schulze_vs_ranked_pairs_c4_b40.yaml
```

It reports the margins, the Smith set, and Copeland / Minimax / Ranked Pairs / Schulze / Split Cycle / Stable Voting side by side, all computed by `pref_voting` ([cross-check engine](../tabulation_engines/cross_checking_with_pref_voting.md)). The LH engine itself runs only the Copeland column — that's Ranked Robin. For a quick manual run without the repo, paste a `count:A>B>C` block into [LeGrand's calculator](https://www.cs.angelo.edu/~rlegrand/rbvote/calc.html), which reports Minimax, Ranked Pairs, Schulze, Copeland and more side by side.

## Learn more (external)

- Ranked Pairs — [Wikipedia](https://en.wikipedia.org/wiki/Ranked_pairs) · [electowiki](https://electowiki.org/wiki/Ranked_Pairs)
- Schulze method — [Wikipedia](https://en.wikipedia.org/wiki/Schulze_method) · [electowiki](https://electowiki.org/wiki/Schulze_method)
- Minimax — [Wikipedia](https://en.wikipedia.org/wiki/Minimax_Condorcet_method) · [electowiki](https://electowiki.org/wiki/Minimax)
- Split Cycle — [Holliday & Pacuit, arXiv:2004.02350](https://arxiv.org/abs/2004.02350) (in this repo: [Split Cycle, claim-checked](../topics/condorcet/split_cycle.md))
- Smith set — [Wikipedia](https://en.wikipedia.org/wiki/Smith_set)
- The whole family's literature, with leans marked — [Condorcet reading list](../topics/condorcet/condorcet_reading_list.md)

---

*Draft — open question to refine later: decide whether this lives here (Condorcet-family folder) or graduates to a `topics/` hub if we add more cross-method deep-dives. (The "add runnable YAMLs for the two worked profiles" item is done — see [method_comparisons/cycle_resolution](../../method_comparisons/cycle_resolution/README.md).)*
