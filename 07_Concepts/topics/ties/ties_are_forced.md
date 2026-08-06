# Ties Are Forced — the small impossibility theorem behind every tie-break

*Everywhere else in this repo, a tie is treated as an operational problem: it happened, here's the ladder, here's the lot. This page supplies the missing half — **ties are not an engineering wart, they are a theorem.** Three axioms almost nobody would give up (anonymity, neutrality, Pareto) are jointly incompatible with a rule that always names exactly one winner. Worse, the condition is arithmetic and startlingly broad: **for any even electorate, a forced tie exists.** So the real design question was never "how do we avoid ties?" — it's "which axiom do we pay with?", and every engine in this library has already answered it differently.*

Part of the [Ties & Tie-Breaking](README.md) hub · the theory it completes: [Why build "silly" tie elections?](why_contrived_tie_cases.md) · the two-candidate positive result: [May's theorem](../mays_theorem.md) · the axioms: [social welfare function](../social_welfare_function.md).

---

## The three axioms

All three are already in the library; this page is where they collide.

- **Anonymity** — permuting *who* cast which ballot never changes the outcome. One person, one vote, stated as mathematics.
- **Neutrality** — permuting the *names* of the candidates permutes the outcome the same way. No candidate is the default; the rule has no thumb on the scale.
- **Pareto** — if every voter prefers `a` to `b`, then `b` is not elected. See [social welfare function](../social_welfare_function.md) for the full treatment, and [criteria at a glance](../criteria_at_a_glance.md#the-table) for who passes.

Two refinements from Zwicker's chapter that this library hadn't stated:

**Nonimposition** is the weak version of neutrality: a rule is *imposed* if some candidate is simply unelectable — no profile whatsoever makes them the sole winner. Nonimposition forbids that. **Pareto implies nonimposition** (a unanimously top-ranked candidate must win, so nobody is unelectable), which is one reason Pareto is described as the floor rather than a real constraint.

**Why Pareto earns its keep at all** is best seen through the rule it kills. Anonymity and neutrality alone do *not* rule out **reverse Borda** — elect whoever has the **lowest** Borda count. Reverse Borda is perfectly anonymous and perfectly neutral; it is simply insane. Pareto is what excludes it. That's the honest case for an axiom that otherwise looks too weak to matter: it isn't there to pick good winners, it's there to exclude rules that are transparently backwards. (And it stays weak — [a dictatorship is Paretian](../social_welfare_function.md#the-asymmetry-that-keeps-pareto-from-being-oversold), which is exactly why Arrow's conclusion bites.)

## The theorem

> **Proposition (Moulin 1983).** Let `m ≥ 2` be the number of candidates and `n` the number of voters. If `n` is divisible by any integer `r` with `1 < r ≤ m`, then **no** neutral, anonymous, Pareto social choice function is **resolute** (single-valued).

*Resolute* means "always returns exactly one winner." So the theorem says: on those electorate sizes, any rule you'd actually be willing to defend **must** return a tied set on at least one profile. You cannot design your way out. You can only decide what to do afterward.

**The arithmetic, restated memorably.** If `n` has any divisor in `(1, m]`, it has a *prime* divisor in that range. So:

> **Ties are forced exactly when the smallest prime factor of `n` is at most `m`.**

Two consequences worth sitting with:

- **Every even electorate is caught.** If `n` is even its smallest prime factor is 2, and `m ≥ 2` always. There is no candidate count that rescues you. A two-candidate, million-voter election has a forced tie — the 500,000/500,000 split — and that is the *same theorem* as the three-way cycle below, not a special case of it.
- **Escape requires a nearly-prime electorate.** The rule survives as resolute only when *every* factor of `n` exceeds `m` — so `n` odd, with no small factors. `n = 5` voters and `m = 3` candidates escapes (5 is prime, and 5 > 3). `n = 9, m = 3` does not (3 divides 9).

## The witness profile — and this library already runs it

The proof builds a specific profile. With `n = 3k` voters and `m ≥ 3` candidates, split the voters into three equal blocs that **rotate** the top three candidates:

| Voters | Ranking |
|:--:|---|
| k | a > b > c > … |
| k | c > a > b > … |
| k | b > c > a > … |

Symmetry does the rest: any permutation of `{a, b, c}` can be undone by a permutation of the *voters*, so an anonymous, neutral rule cannot distinguish them, and Pareto keeps the winner inside `{a, b, c}`. Therefore the outcome **is** `{a, b, c}` — a genuine three-way tie, forced.

**That profile is already a case file here.** [`reinf_north_c3_b6_rr.yaml`](../../../method_comparisons/reinforcement_paradox/cases/cases_pages/reinf_north_c3_b6_rr.md) is exactly it, with `k = 2`:

<!-- report:reinf_north_c3_b6_rr -->
```text
--- Ranked Robin (RCV-RR / Copeland) Method (single winner) ---
 Tabulating 6 ballots (ranked ballots).

Ballots:
     2 × Ada > Ben > Cara
     2 × Ben > Cara > Ada
     2 × Cara > Ada > Ben

Round-Robin — every pair, head-to-head (For – Against):
   Ada   beats Ben    4 – 2
   Cara  beats Ada    4 – 2
   Ben   beats Cara   4 – 2

--- Pairwise (Round-Robin) Matrix ---
Head-to-head / pairwise comparison — the Ranked Robin tally
Legend: For - Equal Support - Against   (row vs column)
         |    Ada    |   Ben    |  Cara    |
--------------------------------------------
   Ada > |    ---    |4 - 0 - 2 |2 - 0 - 4 |
   Ben > | 2 - 0 - 4 |   ---    |4 - 0 - 2 |
  Cara > | 4 - 0 - 2 |2 - 0 - 4 |   ---    |

Win–loss record — Copeland score = wins + ½·ties (highest score wins; ties broken by total margin, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  Ada        1–1–0         1      +0  Ben
    2  Ben        1–1–0         1      +0  Cara
    3  Cara       1–1–0         1      +0  Ada

Winner — Ranked Robin (RCV-RR): Ada
   *** 3 candidates tie for the most wins (Ada, Ben, Cara) — a Condorcet cycle (no candidate beats all others). Resolved by total margin, then lot order. (This is where Minimax / Ranked Pairs / Schulze differ — see 05_Ranked_Robin/01_Learn/cycle_resolution.md.)
```
<!-- /report -->
`n = 6`, `m = 3`; 2 and 3 both divide 6 and both sit in `(1, 3]`. The theorem says a tie is unavoidable here, and the engine lands on one: three candidates, identical records, identical margins. Ada wins **only** because the lot order says so. Full report: [the generated page](../../../method_comparisons/reinforcement_paradox/cases/cases_pages/reinf_north_c3_b6_rr.md).

**The score-ballot analogue is here too.** [`three_way_dead_rung_A`](../../../01_STAR/03_Criteria/tie_break_dead_rung/three_way_dead_rung_tie/three_way_dead_rung_tie_pages/three_way_dead_rung_A.md) is the same rotation on a STAR ballot — `4,0,0 / 0,4,0 / 0,0,4`, with `n = 3`, `m = 3` — and STAR ties at every rung it has: totals 4–4–4, pairwise 2–2–2, five-star `0–0–0` (the [dead rung](../../../01_STAR/03_Criteria/tie_break_dead_rung/README.md)), then the lot.

> **Scope, stated honestly.** Moulin's proposition is written for **ordinal** social choice functions — profiles of rankings in, a candidate out. STAR takes score ballots, so the proposition as *stated* doesn't literally quantify over it. What transfers is the **argument**: the symmetry that forces the tie is a statement about anonymity and neutrality, not about ballot type, and any anonymous + neutral rule fed a perfectly symmetric profile has nothing left to decide with. The dead-rung case is that argument, run. Don't cite the proposition *at* STAR; cite the symmetry.

## When the theorem bites — worked on this repo's own cases

| Case | `n` | `m` | Divisor in `(1, m]`? | Tie forced? | What actually happened |
|---|:--:|:--:|---|:--:|---|
| [Symmetric cycle (North)](../../../method_comparisons/reinforcement_paradox/README.md) | 6 | 3 | 2, 3 | **yes** | 3-way Copeland tie → lot |
| [Three-way dead rung](../../../01_STAR/03_Criteria/tie_break_dead_rung/three_way_dead_rung_tie/three_way_dead_rung_tie.md) | 3 | 3 | 3 | **yes** | every STAR rung ties → lot |
| [Minimal tilted cycle](../../../method_comparisons/minimal_tilted_cycle/README.md) | 5 | 3 | none (5 is prime) | **no** | Copeland *scores* tie — margin breaks it, no lot needed |

That last row is the sharp one, and it puts a theorem underneath a distinction the [tilted-cycle page](../../../method_comparisons/minimal_tilted_cycle/README.md) already found empirically. At `n = 5, m = 3` the theorem grants **no excuse** — a resolute neutral-anonymous-Pareto rule provably exists at that size — and none is needed, because the profile still carries information to decide with. Both [maximin](../../voting_paradoxes/minimax.md) and LH's own margin rung use it.

**And you can see the difference in the engine output.** Compare the two cycles at the rung where they part:

| Rung | Symmetric 6-voter cycle (**forced**) | Tilted 5-voter cycle (**not forced**) |
|---|---|---|
| Copeland (wins) | 1–1, 1–1, 1–1 — dead | 1–1, 1–1, 1–1 — dead |
| Total margin | `+0 / +0 / +0` — **dead** | `+2 / 0 / −2` — **alive** → Ada |
| Lot | **decides the winner** | never reached |

Both look like three-way ties at the top. Only one of them *is* one. In the six-voter case the symmetry has drained the profile of every asymmetry a rule could grab, and the lot is not a shortcut — it is the only thing left. In the five-voter case the tie is one rung deep and the ballots still distinguish the candidates. **A dead margin row is the theorem showing up in the output.**

## Four ways out — and what each one costs

Zwicker lists the four approaches the literature takes. The useful part is that **every one of them is already implemented in this repo**, and each pays a different price:

| # | Approach | What it costs | Where it lives here |
|:--:|---|---|---|
| 1 | **Fixed ordering** of the candidates | **neutrality** — a pre-published order is a thumb on the scale, by construction | LH's `lot_numbers:`; [STAR's official tiebreak protocol](../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md) |
| 1′ | A **designated voter** breaks all ties | **anonymity** — one ballot now counts differently | not used here (a casting-vote chair does this) |
| 2 | **Randomize** | determinism — the rule becomes *indeterminate*, and "did strategy work?" gets harder to even define | [BetterVoting's `tieBreakType: random`](../../../05_Ranked_Robin/01_Learn/rr_tiebreak_lh_vs_bv.md) |
| 3 | **Return the tied set** | you now need a *set extension principle* to say what a voter prefers between two tied sets — and [Duggan–Schwartz](../gibbard_satterthwaite_theorem.md#allowing-ties-does-not-escape-it-duggan-and-schwartz) proves this buys indecisiveness, not strategyproofness | `pref_voting`'s Copeland, which reports a **leader set** `{Blue, Green}` and stops |
| 4 | **Assume ties don't happen** | nothing, until it decides a seat | the honest default for a first pass at a new concept |

**This reframes the LH-vs-BetterVoting divergence.** [That page](../../../05_Ranked_Robin/01_Learn/rr_tiebreak_lh_vs_bv.md) documents the two engines electing different winners from identical ballots and treats it as a discrepancy to pin down. It is better read as **two defensible answers to a forced choice**: LH took approach 1 and paid in neutrality; BetterVoting took approach 2 and paid in determinism; `pref_voting`, consulted as the third opinion, takes approach 3 and declines to choose at all. Nobody is wrong. The theorem says one of them had to give something up, and they gave up different things.

**All four answer the same question, and there is a second one.** Every approach in the table above resolves a tie at the *end* of the count. A method that **eliminates** a candidate each round can also tie in the *middle* — two candidates tied for last, and whichever one you cut changes every round that follows. None of the four is written for that, and the standard answer to it, [Parallel Universe Tiebreaking](parallel_universe_tiebreaking.md), is not on Zwicker's list: it runs every legal elimination order and elects the union. It does not escape this menu so much as **defer** to it — a PUT winner set with two members lands you back at approach 3, but with the ambiguity now visible in the report instead of buried in round two.

That also explains an operational fact the repo discovered the hard way: a randomly-broken BV tie **cannot be frozen into a `_bv_export.json`**, which is why the [dead-heat case](../../../05_Ranked_Robin/03_Criteria/rr_tiebreaks/dead_heat_lot_tiebreak.md) is LH-only. Approach 2's cost isn't abstract — it shows up as an election you can't reproduce.

## The fixed order really does break neutrality — and we can show it

The [three-way dead-rung trio](../../../01_STAR/03_Criteria/tie_break_dead_rung/three_way_dead_rung_tie/three_way_dead_rung_tie.md) is a demonstration of approach 1's price, not just an illustration of it. Three files, **identical ballots**, differing only in `lot_numbers:` — and three different winners:

| File | `lot_numbers:` | Winner |
|---|---|:--:|
| `three_way_dead_rung_A` | `[A, B, C]` | **A** |
| `three_way_dead_rung_B` | `[B, C, A]` | **B** |
| `three_way_dead_rung_C` | `[C, A, B]` | **C** |

Permute the candidate names and the winner changes in a way that does *not* follow the permutation of the ballots. That is the definition of a neutrality failure, exhibited in three runnable files. It's also the right defense of the practice: the neutrality is spent **publicly and in advance**, which is the whole difference between a lot order and a coin flip after the count.

## Real elections pay this too

The theorem isn't confined to teaching files — statute has to answer it, and the answers map onto the same menu:

- **Coin toss (approach 2).** Several countries mandate lot-drawing for exact ties; the 2013 mayoral election in San Teodoro, Philippines was settled this way.
- **Oldest candidate wins (approach 1).** The French electoral code breaks ties in favor of the **older** candidate — and the documented side effect is that parties, at the margin, prefer older candidates. A tiebreak rule that fires roughly never still reshapes who gets nominated. That's neutrality being spent, and then quietly billed to candidate selection.

The second is the one to remember when someone waves off tie-break design as trivia. **A rule that almost never triggers can still change behavior**, because campaigns optimize against the rule, not against its frequency. Same logic as [strategic incentive analysis](../pvsi_strategic_incentive.md) everywhere else in this library.

## What this changes about the "silly" tie cases

[Why build "silly" tie elections?](why_contrived_tie_cases.md) defends the contrived cases on engineering grounds — they isolate a behavior, pin the spec, become regression tests. All true. This page adds the stronger claim:

> **They aren't contrived. They're the profiles the theorem constructs.**

The rotation that page calls "a perfect rotation: three equal, mutually symmetric camps" is Moulin's `P₄`. Building it wasn't a hunt for a pathological corner — it was, without anyone framing it that way, a reconstruction of the standard witness. And the divisibility condition turns the whole exercise from intuition into a **search rule**: if you want a forced tie at `m` candidates, choose `n` with a prime factor `≤ m`. If you want to test whether a rule ties when it *didn't have to*, choose `n` prime and `> m` — which is precisely what makes the [five-voter tilted cycle](../../../method_comparisons/minimal_tilted_cycle/README.md) diagnostic rather than merely small. A rule that still falls to the lot at `n = 5, m = 3` is discarding information the ballots contain; a rule that falls to the lot at `n = 6` is not.

## The honest limits

Three, because this result is easy to overstate:

1. **"Forced" means *some* profile, not *this* profile.** The theorem is a statement about the rule's domain. It says a tie exists somewhere; it says nothing about probability. In a public election with thousands of ballots, exact ties remain astronomically rare — the [existing caveat](why_contrived_tie_cases.md) stands unchanged. What the theorem removes is the option of claiming your method has *no* tie case.
2. **It doesn't rank methods.** Every method in this library is caught. Nothing here favors STAR over [Ranked Robin](../../../05_Ranked_Robin/01_Learn/README.md) over [RCV-IRV](../../../06_Other/RCV_IRV/concepts/README.md). Methods differ in *how often* ties arise and how gracefully they're resolved — see [Tie-Breaking: STAR vs RCV-IRV](tiebreaking_star_vs_irv.md) — but not in whether they're subject to this.
3. **It's a small impossibility, not Arrow.** It costs you *resoluteness*, which is an inconvenience with four known workarounds. [Arrow](../arrow_theorem_and_star.md) and [Gibbard–Satterthwaite](../gibbard_satterthwaite_theorem.md) cost you things you can't work around. Don't let the shared word "impossibility" flatten that difference — this one is the mild member of the family, and citing it as though it were Arrow is exactly the overreach [criteria at a glance](../criteria_at_a_glance.md) warns about.

## Sources

- Hervé Moulin, *The Strategy of Social Choice* (North-Holland, 1983) — the resoluteness result. **Lean:** neutral; a technical monograph.
- William S. Zwicker, "Introduction to the Theory of Voting," in *Handbook of Computational Social Choice* (Brandt, Conitzer, Endriss, Lang & Procaccia, eds., Cambridge University Press, 2016), §2.3–§2.4 — the framing used throughout this page: the Pareto/neutrality/nonimposition definitions, Proposition 2.1 and the `P₄` construction, the four approaches to ties, and the real-world tie-law examples. Same chapter this library already draws on for [May's theorem](../mays_theorem.md). **Lean:** neutral; the standard academic reference.
- Vilfredo Pareto, *Manuale di economia politica* (1919 edition) — the origin of the Pareto principle. **Lean:** historical.
- J. Duggan & T. Schwartz, "Strategic manipulability without resoluteness or shared beliefs," *Social Choice and Welfare* 17 (2000) — why approach 3 doesn't buy strategyproofness. **Lean:** neutral.

## Related

- [Ties & Tie-Breaking hub](README.md) · [Why build "silly" tie elections?](why_contrived_tie_cases.md) · [Tie-Breaking: STAR vs RCV-IRV](tiebreaking_star_vs_irv.md)
- [May's theorem](../mays_theorem.md) — the two-candidate positive result, whose *positive responsiveness* condition is exactly what breaks the ties this theorem doesn't force
- [Social welfare function](../social_welfare_function.md) — Pareto and IIA stated properly · [Does Arrow apply to STAR?](../arrow_theorem_and_star.md) · [Gibbard–Satterthwaite](../gibbard_satterthwaite_theorem.md)
- [Ranked Robin tiebreaks — LH vs BetterVoting](../../../05_Ranked_Robin/01_Learn/rr_tiebreak_lh_vs_bv.md) · [cycle resolution](../../../05_Ranked_Robin/01_Learn/cycle_resolution.md)
- [The minimal tilted cycle](../../../method_comparisons/minimal_tilted_cycle/README.md) · [the reinforcement paradox pair](../../../method_comparisons/reinforcement_paradox/README.md) · [the three-way dead rung](../../../01_STAR/03_Criteria/tie_break_dead_rung/README.md)
- [Glossary](../../GLOSSARY.md) — anonymity, neutrality, nonimposition, resolute, lot numbers
