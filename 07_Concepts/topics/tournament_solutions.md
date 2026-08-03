# Tournament solutions — the theory of the win-loss graph

*Throw away everything about an election except **who beat whom** head-to-head. No margins, no first choices, no scores — just arrows. What's left is a **tournament**: a complete directed graph. A **tournament solution** is a rule for picking the winners out of that graph, and there is a whole academic literature on it, because the graph can cycle and then "the best" has no obvious meaning. This page is the map: what the field is, why it exists, and exactly how much of it touches [Ranked Robin](../../05_Ranked_Robin/01_Learn/ranked_robin.md), [STAR](../../01_STAR/01_Learn/) and [Approval](../../04_Approval/01_Learn/).*

→ Related: [what a method reads](what_a_method_reads.md) — the C1/C2/C3 tiers this page is the C1 half of · [the math behind Condorcet](../../05_Ranked_Robin/01_Learn/the_math_behind_condorcet.md) · [the Smith set](smith_set.md) · [cycle resolution](../../05_Ranked_Robin/01_Learn/cycle_resolution.md) — what the **C2** methods do with the margins tournament solutions discard · **Level: Voting 301**

**Runnable:** [Tournament solutions, counted](../../method_comparisons/tournament_solutions/) — five defensible winners from a three-ballot election, both engines agreeing.

---

## "Is this graph theory or voting theory?" — genuinely both, and that's the point

It's voting theory that has been **completely translated into graph theory**, so thoroughly that the papers read like combinatorics. Every concept has two names:

| Voting theory says | Graph theory says |
|---|---|
| Copeland score (head-to-head wins) | **outdegree** of the vertex |
| Condorcet winner | vertex with an arrow to everyone (a source) |
| the pairwise-results table | **adjacency matrix** `M(T)` |
| top cycle / Smith set | top **strongly connected component** |
| uncovered set | the **kings** of the tournament — its *center* |
| Slater's rule | **minimum feedback arc set** (NP-hard) |
| Markov set | essentially **PageRank** on the win graph |
| bipartisan set | support of the **Nash equilibrium** of a zero-sum game |

The graph theory is where the *answers* come from; the voting theory is where the *questions* come from — which set of candidates a democratic society should regard as the legitimate winners. Neither half is decoration. And it means a fact proved about tournaments is a fact about elections, which is why this literature can be unusually crisp about things voting arguments usually hand-wave.

## Why the field exists: majority rule eats its own tail

Start from the most appealing democratic primitive there is: **A is socially better than B if more people prefer A to B.** [May's theorem](mays_theorem.md) says that for *two* candidates this is essentially the only sensible rule. So the pairwise "beats" relation looks like bedrock.

It isn't transitive. A beats B, B beats C, C beats A — the [Condorcet paradox](../../method_comparisons/paradoxes_and_whoops/) — and then there is no maximal element at all. "Elect the best" has no referent. Tournament solutions are the response: **give up on maximality, and define a replacement.** Each one is a different answer to "what should 'best' mean when 'beats' goes in circles."

Two structural facts frame everything else:

- **McGarvey's theorem (1953).** *Every* complete pairwise pattern is realizable — for any tournament you can draw, some electorate produces exactly it (with at most `m(m−1)` voters; later improved to about `m/log m`). So there is no hidden regularity to exploit. The graph can be as perverse as you like, and real voters can produce it. This is also why the runnable cases in this library can be built at all: draw the graph you want to teach, then find the ballots.
- **A "tournament" assumes no pairwise ties.** With an odd number of voters and complete ballots, every head-to-head has a winner. Real elections tie, and then the object is a *weak* tournament, where these rules become generalizations with **no canonical extension** — the chapter spends a whole section on it. Worth knowing before quoting a theorem at a real election. Our own pairwise report is a For / **Equal Support** / Against table, which is strictly richer than a tournament *and* richer than margins.

## The solutions, coarse to fine

All of them agree — trivially — whenever a [Condorcet winner](../../05_Ranked_Robin/01_Learn/ranked_robin_vs_condorcet.md) exists: every one returns just that candidate. They only differ in a cycle, which is the recurring theme of this whole subject.

| Solution | Picks | Cost |
|---|---|---|
| **Top cycle** (Smith set) | the smallest group that beats everyone outside it | linear |
| **[Uncovered set](uncovered_set.md)** | everyone who reaches every rival in **≤ 2 steps** — "I beat you, or I beat someone who beat you" | polynomial |
| **Banks set** | the tops of the maximal transitive sub-tournaments | **NP-complete** |
| **Bipartisan set** | the support of the win-graph game's unique Nash equilibrium | polynomial (LP) |
| **Copeland set** | **most head-to-head wins** ← this one is Ranked Robin | linear |
| **Slater set** | the tops of the closest linear orderings (fewest arrows reversed) | **NP-hard** |
| **Markov set** | who wins most often in a stay-at-the-table tournament (≈ PageRank) | polynomial |

Two things a newcomer should take from that table. First, **"how hard is it to compute" varies wildly and doesn't track how sensible the rule is** — Banks and Slater are both intellectually respectable and both intractable, while Copeland is linear-time. Second, **most of these return a *set*, not a winner.** That's not a failure; irresoluteness is the normal state here. Getting to one name always takes information from outside the graph, or a lot.

The three axioms the literature actually argues about:

- **Monotonicity** — gaining a win never costs you your place in the choice set. Nearly everything satisfies it. (This is a much weaker condition than [monotonicity as we use it elsewhere](monotonicity/).)
- **Stability** — chosen from `B` and chosen from `C` if and only if chosen from `B ∪ C`. Demanding; fails for most solutions.
- **Composition-consistency** — "choose the best from the best components," the strong form of [clone-independence](../../05_Ranked_Robin/01_Learn/rr_clone_independence.md). Satisfied by the uncovered, Banks and bipartisan sets. **Failed by Copeland**, which is the interesting part for us.

## What this has to do with Ranked Robin: everything

**Ranked Robin *is* a tournament solution.** It is the Copeland set — most head-to-head wins — the rule the chapter introduces as "perhaps the first idea that comes to mind." So this entire literature is the theory of the family Ranked Robin belongs to, and our engine already prints the object it operates on: the pairwise matrix in an RR report is `M(T)`, and the win-loss column is the outdegrees.

Which means the literature's verdicts on Copeland land directly on Ranked Robin, and they're mixed — honestly, that's the value of reading it:

- **Copeland is monotonic, Condorcet-consistent, and linear-time.** For a public method that has to be explained in one sentence and hand-counted, those are the properties that matter, and it's why Ranked Robin is the repo's practical recommendation.
- **Copeland is coarse.** It ties easily in a cycle, because cycling candidates tend to share a win-loss record — [already documented here](../../05_Ranked_Robin/01_Learn/cycle_resolution.md), and the reason the refined methods exist.
- **Copeland fails composition-consistency, and even the weak version.** This is the theoretical name for Ranked Robin's one real clone weakness, [teaming](../../05_Ranked_Robin/01_Learn/rr_clone_independence.md) — and it only bites in a cycle.
- **Copeland is not stable** — it isn't even idempotent: applying it to its own output can shrink the set again.

And one sharp point that falls out of the runnable case, which we haven't stated anywhere else in the repo:

> **The moment Ranked Robin breaks a Copeland tie by margin, it has stopped being a tournament solution.** Margins are not in the tournament. LH's tiebreak ladder (wins → total margin → lot) is C1 for the first rung and **C2 from the second rung on**.

That is not a criticism — a rule that has to name one winner needs something, and margin is a defensible and deterministic something. But it means "Ranked Robin is a C1 method" is only true up to the tie, and a careful critic will notice.

### The three-ballot election with five defensible winners

Three voters, four candidates — one ranking, rotated ([runnable](../../method_comparisons/tournament_solutions/cases/five_answers_one_election_c4_b3.yaml); this is the chapter's own Figure 3.3, converted back into ballots):

```
A>B>C>D
B>C>D>A
D>A>B>C
```

A beats B and C; B beats C and D; C beats D; **D beats A** — so the top cycles and there is no Condorcet winner. Now every rule above, computed by `pref_voting` and cross-checked against the chapter's caption:

| Solution | Choice set |
|---|---|
| Top cycle / Schwartz | `{A, B, C, D}` — everyone |
| Uncovered = Banks = bipartisan | `{A, B, D}` — C is **covered**: B beats C *and* beats everything C beats, so C is strictly redundant |
| **Copeland (= Ranked Robin)** | `{A, B}` — both win 2 |
| Slater = Markov | `{A}` |

Five answers, three ballots, every one of them published and defended. And then our engine has to pick one:

```
Win–loss record — Copeland score = wins + ½·ties:
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  B          2–1–0         2      +3  D, C
    2  A          2–1–0         2      +1  B, C
    3  D          1–2–0         1      -1  A
    4  C          1–2–0         1      -3  D

Winner — Ranked Robin (RCV-RR): B
   *** 2 candidates tie for the most wins (A, B) — a Condorcet cycle. Resolved by total margin, then lot order.
```

**Ranked Robin elects B. Slater and Markov elect A.** Same ballots. B wins only because of the margin rung — the C2 step — and A beats B head-to-head. Neither answer is wrong; they optimize different things, and there is no fact of the matter to appeal to. Full report → [the runnable case](../../method_comparisons/tournament_solutions/README.md).

## What this has to do with STAR: less than you'd hope, and precisely so

**STAR is not a tournament solution, and it has no Fishburn class at all** — not "C3," not "beyond C2." The reason is stronger than "STAR uses different ballots":

> Two score profiles can induce the *identical* ranked profile — hence the identical tournament, the identical margins, everything — and elect **different STAR winners**. ([Worked, with ballots.](what_a_method_reads.md))

A function must return the same answer on the same input. STAR's winner is not a function of the tournament, so there is nothing here for a tournament solution to classify. The whole apparatus — McGarvey, the uncovered set, composition-consistency, the NP-hardness results — simply doesn't reach STAR. Any table that assigns STAR a class is wrong, and hedging it ("roughly C3") is worse, because readers strip hedges.

That said, there is one real and rather elegant connection worth teaching:

> **STAR's runoff consults exactly one edge of the tournament.** The scoring round uses cardinal information the graph doesn't contain to choose *which* head-to-head to read; then it reads that one arrow and obeys it.

So STAR isn't outside pairwise reasoning — it uses a single pairwise comparison, chosen by score. That's why STAR can be *diagnosed* in this language even though it can't be classified by it: when people say "STAR elected someone who loses a head-to-head," they mean STAR's chosen edge wasn't the graph's top, and our reports print the matrix that shows it. The [Condorcet tiebreaker](../../01_STAR/01_Learn/Tie_Breaking_STAR/condorcet_tiebreaker.md) — Equal Vote's optional STAR add-on — is literally a mini Copeland run, i.e. a tournament solution used as a subroutine.

## What this has to do with Approval: outside too, with one footnote

Approval's winner is the highest approval count, which the tournament does not determine — same story, same reason. Approval isn't in Fishburn's domain either, since that domain is ranked profiles.

The footnote a critic will find, so here it is: on the **Brams–Fishburn dichotomous-preference domain** — every voter splits the field into "acceptable" and "not," with no preferences inside either group — Approval *is* a genuine social choice function on preference profiles, and it is determined by the majority tournament, hence C1-like. That's a theoretical domain, not real approval ballots, where voters do have inner preferences they're compressing. Interesting; not a licence to put Approval in the C1 column.

## Is any of this useful, or is it seminar furniture?

Honest answer: mostly the second, with three exceptions that are genuinely load-bearing.

1. **It names Ranked Robin's limits precisely.** "Copeland fails composition-consistency and isn't idempotent" is a real, citable statement about the method this repo recommends, and it is better to say it ourselves than to be told it. It also pins where the limits *aren't*: monotonic, Condorcet-consistent, linear-time, and every one of these failures needs a cycle to fire.
2. **The uncovered set is the one concept with a plain-language payoff.** "Nobody should win who is *covered* — beaten by someone who also beats everyone they beat" is an argument a normal person accepts on hearing, it is equivalent to being reachable-in-two-steps, and it is exactly the line between Pareto-optimal and not. If you take one idea from the chapter, take that one — **it has [its own page](uncovered_set.md)**, with the three equivalent definitions, the Pareto theorem, the proof that Ranked Robin never elects a covered candidate, and a five-ballot election where STAR does.
3. **It disciplines claims.** "Method X uniquely satisfies criterion Y" arguments are common in voting debates and often [built to fit the method](condorcet/ordered_majority_rule_irv.md). This literature is where you learn how many mutually incompatible "reasonable" answers a single election admits — five, in a three-ballot example — which is a permanent inoculation against anyone claiming their rule is *the* answer.

What it is **not** good for: choosing a voting method for a real jurisdiction. Nothing in the chapter argues for a public method, and most of its refinements are unexplainable at a town-hall meeting or intractable to compute. Ranked Robin's case rests on being explainable and summable, not on winning an axiom scorecard.

## Sources

- **Felix Brandt, Markus Brill & Paul Harrenstein, "Tournament Solutions,"** ch. 3 of the [Handbook of Computational Social Choice](https://procaccia.info/wp-content/uploads/2020/03/comsoc.pdf) (CUP 2016, free from co-editor Ariel Procaccia) — the source for this page: definitions, the axioms, Theorems 3.1–3.7, and Figures 3.1–3.5, two of which are [runnable here](../../method_comparisons/tournament_solutions/). **Lean:** neutral / academic. Dense but self-contained.
- Peter C. Fishburn, "Condorcet Social Choice Functions," *SIAM J. Appl. Math.* 33(3), 1977 — where C1 is defined, and one of two independent origins of the uncovered set. **Lean:** neutral.
- David C. McGarvey, "A Theorem on the Construction of Voting Paradoxes," *Econometrica* 21(4), 1953. **Lean:** neutral.
- The choice sets on this page are computed by [`tournament_solutions_report.py`](../../STARVote_LH_tabulation_engine/tools_adam/pref_voting_tabulation_engine/tournament_solutions_report.py) via Eric Pacuit & Wesley Holliday's `pref_voting`, and cross-checked against the LH engine's own Ranked Robin. Nothing here is asserted from memory.

## Related

- [The uncovered set](uncovered_set.md) — the one member of this family with a plain-language payoff, in full
- [What a method reads](what_a_method_reads.md) — C1/C2/C3, and why STAR has no class · [the Condorcet reading list](condorcet/condorcet_reading_list.md)
- [The math behind Condorcet](../../05_Ranked_Robin/01_Learn/the_math_behind_condorcet.md) — the Smith/Schwartz half · [the Smith set](smith_set.md)
- [Cycle resolution](../../05_Ranked_Robin/01_Learn/cycle_resolution.md) — the C2 methods that read the margins these rules throw away
- [Ranked Robin](../../05_Ranked_Robin/01_Learn/ranked_robin.md) · [its honest limits](../../05_Ranked_Robin/01_Learn/RCV_RR_honest_limits.md) · [clone independence](../../05_Ranked_Robin/01_Learn/rr_clone_independence.md)
