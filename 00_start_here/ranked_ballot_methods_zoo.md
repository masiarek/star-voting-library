# The ranked-ballot method zoo — many ways to count one ranked ballot

*Robert LeGrand's [ranked-ballot voting calculator](https://cs.angelo.edu/~rlegrand/rbvote/calc.html) offers fifteen-plus methods — Baldwin, Black, Borda, Bucklin, Carey, Coombs, Copeland, Dodgson, Hare, Nanson, Raynaud, Schulze, Simpson, Small, Tideman — all fed **the same ranked ballots**. That single screen is the clearest possible demonstration of this repo's core terminology point: **RCV names a ballot (ranked); it does not name a tabulation.** IRV is just one way to count a ranked ballot; here are a dozen more, and they routinely pick different winners on identical votes.*

→ **Level: Voting 301** — Curriculum [301.10](CURRICULUM.md). Companions: [Ranked Robin vs. the Condorcet winner](RCV_Ranked_Robin/ranked_robin_vs_condorcet.md) · [Cycle resolution — why Minimax, Ranked Pairs, Schulze exist](RCV_Ranked_Robin/cycle_resolution.md) · [Scoring vs. ranked methods](scoring-methods-vs-ranked-voting.md) · terminology canon: [TIPS_terminology](TIPS_terminology.md).

Live tool: **[calculator](https://cs.angelo.edu/~rlegrand/rbvote/calc.html)** · authoritative method write-ups: **[descriptions](https://cs.angelo.edu/~rlegrand/rbvote/desc.html)** (LeGrand). Paste ballots like `14:Alan>Beth>Carl` (14 identical ballots; `=` for equal ranks) and it runs all methods at once — a great sandbox for the examples below.

---

## The one idea to hold onto

Every method on this page takes the *identical* ranked ballot and differs only in **how it counts**. They split into a few families by what information they look at:

- **Positional** methods score a candidate by *where* it sits on each ballot (Borda and its relatives).
- **Sequential-elimination** methods drop a loser and recount, round by round (Hare/IRV, Coombs, Carey).
- **Graduated-majority** methods widen the net until someone crosses 50% (Bucklin).
- **Pairwise (Condorcet)** methods treat the election as every candidate-vs-candidate duel at once (Copeland, Simpson, Schulze, Tideman, and the rest).

With only **two** candidates they all agree (they all elect the majority winner). With **three or more** they diverge — and *that divergence is the whole subject of voting theory.*

---

## Family 1 — Positional (Borda-based)

**Borda** gives each candidate points for its rank position: in LeGrand's form, (times ranked over another) − (times ranked under another). It's often the *best* method when everyone votes sincerely — and *the most easily manipulated* when they don't. Its signature flaw is **clone dependence**: a party can win simply by running extra similar candidates (LeGrand's Eric/Fran/Gary example — Eric has 63% of first places but Borda hands it to Fran because Gary pads her totals). Borda is a **ranked** method but **not** Condorcet-consistent.

Three methods bolt recursive elimination onto Borda and, in doing so, *become* Condorcet-consistent:

- **Nanson** — eliminate *every* candidate with a negative Borda score, recompute, repeat.
- **Baldwin** — eliminate only the *single lowest* Borda score, recompute, repeat.
- **Rouse** — Baldwin with an extra layer of recursion (repeatedly excuse the *highest* Borda candidate from elimination). Present in LeGrand's descriptions; a rarity in practice.

On the same three ballots these three can each pick a *different* winner (LeGrand's Jana/Kurt/Lisa example: Nanson→Jana, Baldwin→Lisa, Rouse→Jana) — a compact lesson that "Borda-based" is not one method.

**Black** is the simplest hybrid: elect the **Condorcet winner** if one exists, otherwise the **Borda winner**. It is the most *decisive* method in the whole list (it almost never needs a tiebreaker).

## Family 2 — Sequential elimination

- **Hare** is the original name for **Instant-Runoff Voting (IRV)** — in this repo, **RCV-IRV**. Count first choices, eliminate the candidate with the fewest, repeat until someone has a majority. Intuitive, but **not** Condorcet-consistent, and the source of the repo's recurring critiques: **center squeeze**, **non-monotonicity**, and **exhausted ballots**. It looks at the *least* ballot information at any one step.
- **Coombs** is Hare *in reverse*: each round eliminate the candidate with the most **last-place** votes. Often elects a strong compromise candidate, but also **not** Condorcet-consistent.
- **Carey** (a generalization of Craig Carey's three-candidate IFPP) eliminates **all** below-average first-rank candidates each step, not just one. Like Hare, it can **punish sincere voting** — LeGrand's Katy/Luke/Mary example shows both Hare and Carey rewarding strategic ballots.

## Family 3 — Graduated majority

**Bucklin** counts first-place votes; if nobody has a majority it *adds in* every second-place vote, then thirds, and so on until someone crosses 50%. A "median-rank" idea. Notably it can crown a candidate who would *lose head-to-head* to another (LeGrand's Mark/Nell/Owen example: Nell wins on added seconds even though Mark beats her one-on-one) — so Bucklin, too, is **not** Condorcet-consistent.

## Family 4 — Pairwise (Condorcet) methods

These build a **pairwise matrix** in one pass — for every pair, how many voters ranked A over B (a tie counts half each way) — then reason over those duels. When some candidate wins *all* its duels (the **Condorcet winner**), *every* method below elects it (as do Nanson, Baldwin, Rouse, and Black above). They differ only when there's **no** Condorcet winner — a **cycle** (A beats B beats C beats A). How each resolves the cycle is its personality:

- **Copeland** — most pairwise wins (ties = ½). This is exactly the core of the repo's **Ranked Robin (RCV-RR)** (win–loss record). Transparent, but *indecisive* — it ties often, ignoring how *big* each win was.
- **Small** — Copeland, then break Copeland ties by eliminating the non-top-scorers and recomputing until it can't. A more *decisive* Copeland.
- **Dodgson** (Lewis Carroll) — the candidate needing the fewest ballot-swaps to *become* a Condorcet winner; equivalently, smallest **sum** of defeat margins. Rarely, it can pick a **Condorcet loser** (LeGrand's Cora, who loses every duel but each by a hair).
- **Simpson** (a.k.a. **Minimax** / Simpson–Kramer) — smallest **single worst** pairwise defeat. Also rarely picks a Condorcet loser.
- **Raynaud** — elimination on Simpson: repeatedly drop the candidate with the **largest single defeat** until one remains.
- **Schulze** (beatpaths / CSSD) — resolves cycles via **strongest indirect paths** of victories. Clone-independent, monotonic, and **never** picks a Condorcet loser.
- **Tideman** (**Ranked Pairs**) — lock in pairwise victories strongest-first, skipping any that would contradict a stronger, already-locked one. Also clone-independent, monotonic, and never a Condorcet loser.

Minimax (Simpson), Ranked Pairs (Tideman), and Schulze are the three cycle-resolvers the repo treats in depth in **[cycle_resolution.md](RCV_Ranked_Robin/cycle_resolution.md)** — Ranked Robin runs the round-robin and, if a cycle appears, hands off to one of these.

## Beyond single winners — the set-valued three

**Smith**, **Schwartz**, and **Landau** are so *indecisive* they're usually treated as producing a **set** of candidates, not one winner. The **Smith set** (smallest set that beats everyone outside it) is the important one: a method is **"Smith-efficient"** if it always elects from it. It's the formal version of "the group of candidates any of whom has a legitimate claim."

---

## At a glance

| Method | Family | Condorcet winner? | Never elects a Condorcet loser? | Known as / repo tie-in |
|--------|--------|:---:|:---:|--------|
| Borda | positional | ✗ | ✗ | classic point-count; clone-vulnerable |
| Nanson | positional+elim | ✓ | ✓ | below-average Borda cut |
| Baldwin | positional+elim | ✓ | ✓ | lowest-Borda cut |
| Rouse | positional+elim | ✓ | ✓ | Baldwin variant (rare) |
| Black | hybrid | ✓ | ✓ | Condorcet-else-Borda; most decisive |
| Hare | elimination | ✗ | ✗ | **IRV / RCV-IRV** |
| Coombs | elimination | ✗ | ✗ | Hare in reverse (most last-place out) |
| Carey | elimination | ✗ | ✗ | below-average first-place cut (IFPP) |
| Bucklin | graduated majority | ✗ | ✗ | add later ranks until a majority |
| Copeland | pairwise | ✓ | ✓ | **Ranked Robin (RCV-RR)** core |
| Small | pairwise | ✓ | ✓ | decisive Copeland |
| Dodgson | pairwise | ✓ | ✗ (rarely) | fewest swaps to Condorcet |
| Simpson | pairwise | ✓ | ✗ (rarely) | **Minimax** / Simpson–Kramer |
| Raynaud | pairwise | ✓ | ✓ | eliminate largest defeat |
| Schulze | pairwise | ✓ | ✓ | **beatpaths**; clone-proof, monotonic |
| Tideman | pairwise | ✓ | ✓ | **Ranked Pairs**; clone-proof, monotonic |
| Smith / Schwartz / Landau | set-valued | — | — | dominant *sets*, not single winners |

*("Condorcet winner? ✓" means the method always elects the candidate who beats all others head-to-head, when one exists. The last two columns are exactly why the repo prefers Condorcet methods like Ranked Robin that **never** seat a candidate who would lose every duel — a guarantee IRV/Hare, Borda, and Bucklin do not give.)*

---

## Why this belongs in a STAR repo

Three payoffs for our teaching:

1. **It nails the terminology.** One ranked ballot, fifteen tabulations, fifteen possible winners. "RCV" cannot mean a *method* — it names the ballot. IRV/Hare is one child of that ballot; Ranked Robin (Copeland), Ranked Pairs (Tideman), and Schulze are siblings. (House canon: [TIPS_terminology](TIPS_terminology.md), [GLOSSARY](GLOSSARY.md).)
2. **It maps the repo's own engines onto the wider field.** The vendored IRV engine = **Hare**. The Ranked Robin engine = **Copeland** (with the house margin→lot tiebreak). The cycle-resolution page's Minimax/Ranked Pairs/Schulze = **Simpson/Tideman/Schulze** here.
3. **It shows why STAR isn't on this list.** Every method here counts a **ranked** ballot. STAR counts a **scored** (0–5) ballot — a different, more expressive input — so it can't appear on a ranked-only calculator at all. That contrast is the point of [scoring vs. ranked methods](scoring-methods-vs-ranked-voting.md): the ballot comes first, the tabulation second.

**Worked live on BetterVoting.** Two of LeGrand's examples are reproduced end-to-end in this repo — same ballots, tabulated by IRV / Ranked Robin / STV / STAR on BetterVoting and cross-checked against `pref_voting` and LeGrand's calculator: the [center squeeze (BV2137)](../method_comparisons/center_squeeze_bv2137/bv2137_ywckmg_center_squeeze.md) where 13 of 15 methods elect the centrist Condorcet winner that IRV discards, and the [no-Condorcet-winner five-way (BV2138)](../method_comparisons/no_condorcet_bv2138/bv2138_cxrf8v_no_condorcet.md) where the winner genuinely depends on the method.

**A caution, stated plainly:** none of this ranks the methods for you. LeGrand's own descriptions note real trade-offs on every one — Borda is best-when-sincere but most manipulable; Copeland is transparent but indecisive; Dodgson and Simpson can (rarely) crown a Condorcet loser; Schulze and Tideman have the strongest criterion-compliance but are the hardest to hand-count and explain. Which properties matter is the judgment call laid out in [what makes a voting method good?](what_makes_a_voting_method_good.md) — this page is the *catalog*, not the verdict.

## References

- Robert LeGrand, **Ranked-ballot voting calculator** — [calc.html](https://cs.angelo.edu/~rlegrand/rbvote/calc.html) · **method descriptions** — [desc.html](https://cs.angelo.edu/~rlegrand/rbvote/desc.html) (Angelo State University). Source of the definitions and worked examples above.
- electowiki: [Borda](https://electowiki.org/wiki/Borda_count) · [Nanson & Baldwin](https://electowiki.org/wiki/Nanson%27s_method) · [Bucklin](https://electowiki.org/wiki/Bucklin_voting) · [Coombs](https://electowiki.org/wiki/Coombs%27_method) · [Copeland](https://electowiki.org/wiki/Copeland%27s_method) · [Minimax (Simpson)](https://electowiki.org/wiki/Minimax) · [Schulze](https://electowiki.org/wiki/Schulze_method) · [Ranked Pairs (Tideman)](https://electowiki.org/wiki/Ranked_pairs) · [Smith set](https://electowiki.org/wiki/Smith_set)
- In-repo: [Ranked Robin vs. the Condorcet winner](RCV_Ranked_Robin/ranked_robin_vs_condorcet.md) · [Cycle resolution](RCV_Ranked_Robin/cycle_resolution.md) · [The math behind Condorcet](RCV_Ranked_Robin/the_math_behind_condorcet.md) · [What makes a good winner?](what_makes_a_good_winner.md)
