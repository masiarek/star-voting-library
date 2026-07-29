# The cycle–cocycle decomposition — how much of an election is rock-paper-scissors?

*Take any election's pairwise margins and draw them as arrows with numbers — the margin graph. A short theorem (Zwicker, 1991) says that picture is always, uniquely, the sum of two ingredients that carry none of each other's information: a **cocycle part** — a pure "these candidates are better, by this much" signal, fully explained by one quality number per candidate — and a **cycle part** — pure rock-paper-scissors circulation that says nothing about who is better. [Borda](../../06_Other/other_ranked_methods/borda.md) reads exactly the first ingredient and is structurally deaf to the second; [Copeland / Ranked Robin](../../05_Ranked_Robin/concepts/ranked_robin.md) reads the *sign* of each summed arrow, which a strong enough circulation can point against the quality order. That is the entire mechanism behind [the gelato case](../../method_comparisons/copeland_vs_borda_margins/README.md)'s four verdicts from twelve ballots.*

→ Related: [the minimal tilted cycle](../../method_comparisons/minimal_tilted_cycle/README.md) · [cycle resolution](../../05_Ranked_Robin/concepts/cycle_resolution.md) · [Condorcet hub](condorcet/README.md) · [the Smith set](smith_set.md) · [ties are forced](ties/ties_are_forced.md).

---

## The margin graph is a flow

Vertices are candidates. For each pair, count `Net(x,y)` = (voters preferring `x`) − (voters preferring `y`) and label the arrow with that margin. To do algebra on these pictures, fix a reference direction for each edge once and for all and let the number carry the sign: a `−1` on an edge drawn `d → c` just means the actual majority runs `c → d`. Negative labels are bookkeeping, not substance. An edge-labeling like this is called a **flow**, and the flows on `m` candidates form a plain vector space — you can add two electorates' margin graphs edge-by-edge (that's what pooling their ballots does), scale them, and decompose them.

## The two atoms (Figure 2.2 of Zwicker's Handbook chapter)

Zwicker's figure shows the two kinds of building block on four candidates `a, b, c, d`. In table form:

| edge (reference direction) | **basic cocycle at `d`** | **basic cycle `d→b→c→d`** |
|---|---:|---:|
| `d → a` | 1 | 0 |
| `d → b` | 1 | 1 |
| `d → c` | 1 | −1 |
| `a → b` | 0 | 0 |
| `b → c` | 0 | 1 |
| `c → a` | 0 | 0 |

**The basic cocycle at `d`** puts `+1` on every edge *out of* `d` and `0` everywhere else: `d` up by one against every rival, no other pair moved. Three equivalent ways to see the same object, all standard: it is the **star** of `d` (every edge touching `d`, pointed away from it); it is the **cut** separating `{d}` from everybody else (`+1` per crossing edge); and it is a **potential difference** — give `d` the quality score `1` and everyone else `0`, then label each edge with (tail's score − head's score). It is also a ballot you already know: one voter voting `d` above the rest and leaving the rest equal adds exactly this to the margin graph. A basic cocycle is what **pure endorsement with zero circulation** looks like, and the general cocycles — sums and scalings of the basic ones — are precisely the margin graphs that some assignment of one number per candidate explains completely.

**The basic cycle** is one unit of flow circulating `d → b → c → d`, zero elsewhere. (The `−1` on `d → c` is the bookkeeping above: the circulation traverses that edge against its drawn arrow.) At every vertex, inflow equals outflow — the circulation hands no candidate any net support, so it contains **no information about who is better**, only about incoherence between pairs. It too is an electorate you already know: three voters `d>b>c`, `b>c>d`, `c>d>b` produce exactly this margin graph among those three candidates. The basic cycle is the Condorcet-paradox atom.

**Why "co"?** The two kinds of flow are mutually perpendicular in the honest dot-product sense — multiply the two columns above edge-by-edge and add: `1·0 + 1·1 + 1·(−1) + 0 + 0 + 0 = 0`. That is general: a circulation enters a vertex as often as it leaves, so against that vertex's star the `+1`s and `−1`s cancel. In graph-theory language the span of the stars is the **cut space**, the circulations form the **cycle space**, and the two are orthogonal complements — each is exactly what the other is not. "Cocycle" is the older, duality-flavored name for the cut side, and it is the one Zwicker's voting work uses.

## The theorem

**Every margin graph splits, uniquely and orthogonally, into a cocycle part plus a cycle part** (Zwicker 1991). No choices, no approximation — it is the graph version of splitting a force field into gradient plus curl. The dimension count says how much room each side has: `m` candidates give `m(m−1)/2` margins, of which the cocycle side accounts for `m − 1` dimensions (one quality number per candidate, minus one because only differences matter) and the cycle side the remaining `(m−1)(m−2)/2`. For the figure's four candidates: `6 = 3 + 3`. For three candidates: `3 = 2 + 1` — the whole cycle part is a single number, the strength `λ` of the one triangle circulation, and it has a closed form: **`λ` = the average of the three margins signed around the loop**.

## Which part your method reads

The symmetric Borda score of `x` is `Σ_y Net(x,y)` — the **net outflow** of the margin graph at `x`. Circulations have zero net outflow everywhere, so **Borda cannot see the cycle part even in principle**; conversely, the cocycle part's quality scores *are* the symmetric Borda scores, divided by the number of candidates. "Discard the circulation, then read off the signal" is not an approximation of Borda — it **is** Borda.

Copeland / Ranked Robin and the other [Condorcet methods](condorcet/README.md) instead read the **sign** of each summed margin — each pairwise contest is a majority *verdict*, not a score. Each sign goes to whichever part is locally bigger. When circulation is weak — the usual case in real electorates — every sign follows the quality signal, the tournament is transitive, a Condorcet winner exists, and the two readings broadly agree. When circulation overpowers some pair, that arrow points *against* the quality order, and the readings come apart.

Neither reading is a mistake. Treating every pairwise majority as a verdict regardless of size is a principled stance — it is majority rule, applied pairwise. Trusting margin *sizes* as strength of preference is a different principled stance. The decomposition doesn't referee the dispute; it makes exact what each side has chosen to see.

## Worked: the gelato loop, decomposed

[The BV2251 case](../../method_comparisons/copeland_vs_borda_margins/README.md): twelve transitive ballots, margins `Almond → Berry +2`, `Berry → Cocoa +4`, `Cocoa → Almond +2`. Around the loop:

```
cycle part     λ = (2 + 4 + 2)/3 = 8/3           circulating A → B → C → A

cocycle part   A→B: −2/3      B→C: +4/3      C→A: −2/3
  = quality    Berry +2/3 · Almond 0 · Cocoa −2/3    (×3 = symmetric Borda: +2, 0, −2)

check          A→B: −2/3 + 8/3 = +2 ✓   B→C: +4/3 + 8/3 = +4 ✓   C→A: −2/3 + 8/3 = +2 ✓
```

Read it off: the quality signal says **Berry > Almond > Cocoa**, but it is worth at most `4/3` of a vote per pair, and a circulation of strength `8/3` runs over the top of it — so *all three* head-to-head signs follow the circulation. Almond "beats" Berry even though the signal says Berry is the better candidate, and Berry's one blowout (8–4) is exactly the pair where signal and circulation pull the same way. Copeland reads the three signs and ties everybody; Borda strips the circulation and says Berry. Four methods, four verdicts, one decomposition. *(Full ballots, all four races, and the live BetterVoting election are on the case page.)*

## Even one honest ballot contains a circulation

The cycle part is **not** a symptom of irrational voters. Decompose a single perfectly transitive ballot `d > a > b > c` — margin `+1` on all six pairs, in ranking direction — and its quality signal comes out `(+¾, +¼, −¼, −¾)` for `(d, a, b, c)`, with the remainder a **half-strength circulation** around `d → a → b → c → d`. A lone ballot never *shows* its circulation, because its own signal outweighs it on every pair; but it is there. A Condorcet cycle in an electorate is what happens when voters' circulations line up while their quality signals cancel — which is exactly how the gelato case manufactures a loop from twelve individually transitive ballots. The far end of the same spectrum: the rotation profiles of [Ties Are Forced](ties/ties_are_forced.md), where the signals cancel to exactly zero and *only* circulation remains.

## Graph theory, or voting theory?

Fair question — the *vocabulary* (flows, cycle space, cut space, orthogonal complements) is graph theory, and an algebraic-graph-theory text covers it without an election in sight. But the theorem as used here is voting theory in the same sense [May](mays_theorem.md) and [Arrow](arrow_theorem_and_star.md) are: Zwicker built the decomposition specifically to explain the Borda–Condorcet split and the voters' paradox (that is his 1991 title), it is taught as core material in the standard modern introduction to voting theory (the Handbook chapter whose Figure 2.2 this page tabulates), and the same mathematics runs modern statistical ranking under the name HodgeRank. The graph theory is the grammar; the sentence it is used to say — *the two great families of pairwise methods are reading two orthogonal components of the same electorate* — is about voting. That is why it lives in `topics/` beside the other theorems rather than being waved off as background math.

## Sources

- William S. Zwicker, "The voters' paradox, spin, and the Borda count," *Mathematical Social Sciences* 22(3), 1991, pp. 187–227 — the decomposition, built for voting from the start. **Lean:** neutral; peer-reviewed mathematics. (**"Spin" is Zwicker's own name for the magnitude of the circulation** — the `λ` this page computes. Worth knowing, since it's the word the literature uses for the quantity.)

**One thing this page must not overstate.** Borda ignores the circulation, but it is **not the only rule that does** — in Saari's profile decomposition *every positional rule*, plurality included, is blind to the cyclic direction. What Zwicker's uniqueness result adds is narrower and sharper: a rule that reads only the weighted tournament, is **linear**, and ignores the circulation must in effect *be* Borda. Drop either qualifier and the uniqueness goes away. (Relatedly, Zwicker and Saari are two different decompositions that map onto each other — Zwicker splits the *weighted tournament* in two, Saari splits *profile space* in four — so "the Zwicker/Saari decomposition" as a single named object is a conflation worth avoiding.)
- William S. Zwicker, "Introduction to the Theory of Voting," in *Handbook of Computational Social Choice* (Brandt, Conitzer, Endriss, Lang & Procaccia, eds., Cambridge University Press, 2016) — its Figure 2.2 is the two-atoms picture tabulated above. **Lean:** neutral; the standard academic reference.
- Jiang, Lim, Yao & Ye, "Statistical ranking and combinatorial Hodge theory," *Mathematical Programming* 127(1), 2011 — the same split done as a graph Helmholtz/Hodge decomposition ("HodgeRank"), including what changes when some pairs go uncompared. **Lean:** neutral.
- [Cycle space (Wikipedia)](https://en.wikipedia.org/wiki/Cycle_space) — the pure graph theory of circulations and their orthogonal cut space. **Lean:** neutral.
- Donald Saari's profile decompositions (*Basic Geometry of Voting*, 1995) tell a parallel story one level up — decomposing ballot *profiles* rather than margin graphs, with his "Condorcet portion" generating the cycle part seen here. **Lean:** Saari argues *for* Borda from this mathematics; the decomposition is neutral, that conclusion is his.

## Related

- [Copeland vs Borda — margins matter (the gelato loop, BV2251)](../../method_comparisons/copeland_vs_borda_margins/README.md) — the worked case · [the minimal tilted cycle](../../method_comparisons/minimal_tilted_cycle/README.md) — five voters, the smallest lopsided loop · [Condorcet's 1788 rebuttal to Borda](../../method_comparisons/borda_condorcet_1788/README.md) — the price of reading only the signal
- [Cycle resolution](../../05_Ranked_Robin/concepts/cycle_resolution.md) — what Condorcet methods *do* about the cycle part once it flips a sign · [the Smith set](smith_set.md) · [Ties are forced](ties/ties_are_forced.md) — pure-circulation electorates
- [Curriculum 301](../curriculum/CURRICULUM_301.md) · [Glossary](../GLOSSARY.md)
