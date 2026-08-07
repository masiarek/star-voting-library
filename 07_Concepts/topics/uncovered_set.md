---
tags:
  - criteria
  - theory
---

# The uncovered set — "you're beaten by someone who beats everyone you beat"

*The one idea from the [tournament-solutions](tournament_solutions.md) literature that survives contact with a normal audience. Forget cycles and axioms for a moment and ask a much smaller question: **is this candidate redundant?** If somebody beats them head-to-head, and also beats everyone they beat, then yes — strictly, on the pairwise evidence alone. That candidate is **covered**. The **uncovered set** is everybody left — graph theory and Wikipedia call it the **Landau set**, occasionally the **Fishburn set**. It is the weakest structural filter in the field, it has three completely different definitions that turn out to be the same thing, and it is exactly the line between electing a Pareto-optimal candidate and not.*

→ Related: [tournament solutions](tournament_solutions.md) — the family this belongs to · [the Smith set](smith_set.md) — the *other* generalized Condorcet winner, and a **coarser** one · [what a method reads](what_a_method_reads.md) · [pairwise counting](pairwise_counting.md) · **Level: 301 · deep dive**

**Runnable:** [STAR elects a covered candidate](../../method_comparisons/tournament_solutions/cases/cases_pages/star_elects_a_covered_candidate_c4_b5.md) — five ballots, four cities, and the filter that most candidates pass.

---

## The definition, in one sentence

> **A covers B** when A beats B head-to-head **and** A also beats everyone B beats.
>
> **The uncovered set** is every candidate nobody covers.

That's it. If A covers B, then B contributes nothing A doesn't already contribute: any argument for B ("B beats C, B beats D") is an argument A satisfies too, *plus* A beats B. Electing B over A would be hard to defend to the room.

Two properties make it well-behaved, and they are worth stating because most cycle-related concepts lack them:

- **The covering relation is transitive** — even though "beats" isn't. Covering is defined by set inclusion of who-you-beat, and inclusion is transitive. So the covering relation is a genuine partial order sitting *inside* the messy tournament, and the uncovered set is simply its maximal elements.
- **It's never empty.** A cycle can destroy the Condorcet winner; it cannot destroy the uncovered set.

And when a [Condorcet winner](condorcet/README.md) exists, the uncovered set is just that one candidate — they beat everyone, so they cover everyone. Like every tournament solution, this only becomes interesting in a cycle.

## Also called the Landau set and the Fishburn set

Three names, one object — and if you meet either of the other two first, nothing about them tells you they mean this.

| Name | Where you'll meet it | Why that name |
|---|---|---|
| **Uncovered set** | social choice; this repo's term | the covering relation above |
| **Landau set** | graph theory; the title of Wikipedia's article | Landau's tournament work — below |
| **Fishburn set** | occasional, following Wikipedia | Fishburn's independent 1977 definition |

Wikipedia also names the two roles in a covering pair: the coverer is the **Fishburn winner**, the covered candidate the **Fishburn loser**. Nothing here uses that phrasing, for a reason worth stating — see the collision at the end of this section.

**Where "Landau" comes from.** Wikipedia asserts the name and never explains it, and the explanation is the good part. H. G. Landau spent 1951–53 modelling dominance relations in flocks of chickens, and tournament theory has carried his name since. In that literature a **king** is a bird that pecks every other bird either directly or through one intermediary — two steps, which is exactly characterization (2) below. Landau's result: **a bird of maximum score is always a king.** Stephen Maurer's 1980 restatement, "The King Chicken Theorems," is the version people quote.

Don't let that pass as trivia, because **it is a theorem this page already leans on**. "Maximum score ⇒ king" is precisely "Copeland winner ⇒ uncovered" — the guarantee that [Ranked Robin](../../05_Ranked_Robin/01_Learn/ranked_robin.md) never elects a covered candidate. The one-line proof further down and Landau's pecking-order theorem are the same argument, seventy years and one discipline apart.

**Two cautions on the Wikipedia framing,** since that is where most readers arrive:

- **"First discovered by Nicholas Miller"** is too clean. The Handbook credits **Fishburn (1977) and Miller (1980) independently**, building on a covering notion of Gillies (1959). Fishburn is three years earlier — which is *why* "Fishburn set" is a name at all. Miller's is the paper that carried it into voting theory, and the more cited one.
- **"The Pareto frontier … determined by pairwise victories"** is a fair mnemonic and a poor definition. The precise claim is that it's the *coarsest Pareto-optimal* tournament solution, which is a different statement — and the difference is the thing that [gets fumbled constantly](#why-it-matters-the-pareto-line): **covered does not mean Pareto-dominated.**

⚠️ **"Fishburn" is overloaded in this repo, and the two senses are unrelated.** Everywhere else here, *Fishburn* means the **[C1 / C2 / C3 informational basis](what_a_method_reads.md)** — which statistic a rule actually reads — and it comes out of the *same* 1977 paper. "Fishburn C1" is a **class of methods**; the "Fishburn set" is a **set of candidates**. Same author, same year, different objects. House usage: say **uncovered set**, and keep *Fishburn* for the informational tiers.

## Three definitions, one set

This is the part that makes the uncovered set feel less like an arbitrary construction. It was proposed independently by Fishburn (1977) and Miller (1980), out of a game-theoretic notion of Gillies (1959), and it has three characterizations that look unrelated:

1. **Covering.** Nobody beats you who also beats everyone you beat.
2. **Reachability in two steps.** You can get from yourself to *every* rival along at most two arrows — "I beat you, or I beat somebody who beat you." Every excuse is one hop deep. (Shepsle & Weingast, 1984.) In graph theory these vertices are the **kings** of the tournament, and they form its **center**.
3. **Winning a sub-election.** You are a Condorcet winner of some inclusion-maximal subtournament that has one (Brandt, 2011).

The equivalence of (1) and (2) is a two-line argument: if nobody covers you, then for each candidate `b` who beats you there must be somebody you beat who beats `b` — otherwise `b` would cover you — and that "somebody" is your second hop. It also hands you the algorithm: reachability in ≤ 2 steps is a statement about `M(T)² + M(T) + I` having no zero entries, so the uncovered set falls out of one matrix multiplication, `O(m^2.38)`.

Characterization (2) is the one to say out loud. "Every candidate who beat me was beaten by someone I beat" is a sentence a voter can check by hand on a printed pairwise table.

## Why it matters: the Pareto line

Here is the result that turns the uncovered set from a curiosity into a criterion.

> **The uncovered set is the *coarsest* Pareto-optimal tournament solution** (Brandt et al., 2015). Equivalently: a tournament solution is Pareto-optimal **if and only if** it is a refinement of the uncovered set.

So "stay inside the uncovered set" is not one taste among many — it is precisely the condition for never electing a Pareto-dominated candidate while reading only the win-loss graph. Everything sharper than the uncovered set (Banks, bipartisan, Copeland, Slater, Markov) inherits Pareto-optimality for free; anything coarser (the Smith set, the top cycle, Condorcet non-losers) does not.

**One precision that matters, and gets fumbled constantly:** *covered* does **not** mean *Pareto-dominated*. Pareto domination means every single voter ranks the other candidate higher — much rarer, and much stronger. A covered candidate can be many voters' genuine favourite. The theorem says the uncovered set is the coarsest solution that *excludes* Pareto-dominated candidates; it does not say the candidates it excludes are Pareto-dominated. Our runnable case is exactly this: the covered city is nobody's Pareto-dominee, and one ballot scores it top.

Where it sits relative to the [Smith set](smith_set.md), which the repo already covers:

| Filter | Asks | Strength |
|---|---|---|
| Condorcet non-losers | is anyone *worse* than you in every matchup? | weakest |
| Top cycle / **Smith set** | are you in the club that beats all outsiders? | weak |
| **Uncovered set** | is anyone strictly redundant-making you? | weak — **but** the Pareto line |
| Copeland, Banks, bipartisan, Slater… | sharper, various | strong |

Uncovered ⊆ Smith, always. The Smith set answers *who is in contention*; the uncovered set answers *who isn't redundant*.

## What our methods do with it

**Ranked Robin never elects a covered candidate.** The Copeland set is always a subset of the uncovered set, and the proof is one line: if B covers A then B beats everything A beats *plus* A itself, so B's win count is strictly greater than A's, so A cannot have the maximum win count. Verified as a sanity check over 300,000 random tournaments — zero violations.

That is a genuine, citable virtue of [Ranked Robin](../../05_Ranked_Robin/01_Learn/ranked_robin.md), and via the Pareto theorem above it means **Ranked Robin is Pareto-optimal in the tournament sense**. It's a better thing to say about the method than any axiom scorecard, because a voter can follow it.

**RCV-IRV can, and often does.** Over 120,000 random tie-free four-candidate ranked profiles, IRV elected a covered candidate 9.1% of the time — 61.6% of the time when there was no Condorcet winner. Two honest caveats on that number, both cutting the same way: uniform-random profiles ("impartial culture") produce far more cycles than real electorates do — 14.8% here, against the [2-in-182 rate observed in real IRV elections](../../06_Other/RCV_IRV/concepts/README.md) — so treat 9.1% as *what the failure looks like when cycles are common*, not as a forecast for any real jurisdiction. When there is a Condorcet winner, no method that elects them can elect a covered candidate.

**STAR can too — and here it is.** Five ballots, four cities, every ballot using four distinct scores so nothing is a tie-breaking artifact ([full case](../../method_comparisons/tournament_solutions/cases/cases_pages/star_elects_a_covered_candidate_c4_b5.md)):

<!-- report:star_elects_a_covered_candidate_c4_b5 -->
```text
[Divergence from STAR]
  STAR                   = Denver
  Choose-One (Plurality) = Chicago   (differs from STAR)
  RCV-IRV                = Chicago   (differs from STAR)
  Approval               = Austin   (differs from STAR)
  RCV-RR                 = Chicago   (differs from STAR)
  Note: no ballots had tied scores, so RCV-IRV vs STAR here is a genuine
        method difference, not a tie-breaking artifact.
  Note: Ranked Robin (RCV-RR) sides with RCV-IRV, so STAR is the outlier
        here — STAR need not elect the Condorcet candidate.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: cases_tabulated/star_elects_a_covered_candidate_c4_b5_RCV-IRV_tabulated.txt
  RCV-RR round-robin: cases_tabulated/star_elects_a_covered_candidate_c4_b5_RCV-RR_tabulated.txt

[Runoff Reversal]
 - Score Round Winner(s) = (Austin)
 - Runoff Round Winner   = (Denver)
  Candidate Austin earned the highest total score, but
  Candidate Denver won the automatic runoff — not a malfunction,
  STAR working as designed: the runoff elects the finalist preferred
  by the majority (of voters with a preference).

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 5 ballots.
Austin,Boston,Chicago,Denver
     0,     4,      2,     1
     2,     1,      3,     0
     4,     1,      0,     5
     5,     2,      0,     1
     3,     1,      5,     4

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Austin        -- 14 -- First place
   Denver        -- 11 -- Second place
   Chicago       -- 10
   Boston        --  9
 Austin and Denver advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Denver        -- 3 -- First place
   Austin        -- 2
   Equal Support -- 0
 Denver wins.
   Runoff math:
     5  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     5  voters with a preference  (majority = 3)
           Denver 3 (60%)  ·  Austin 2 (40%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Denver
```
<!-- /report -->
Read the grid for Denver. **Chicago beats Denver** — and Austin, the only city Denver beats, **is also beaten by Chicago**. Chicago does everything Denver does and more, so Denver is covered, and the uncovered set is `{Austin, Boston, Chicago}`. Three of four cities clear the bar. STAR elects the fourth.

Both halves of that, because the repo doesn't get to keep only the flattering one:

- **Against STAR.** No rule reading only the win-loss graph would elect Denver, and the objection travels in one sentence to a lay audience. Plurality, RCV-IRV and Ranked Robin all elect Chicago here; STAR is the outlier, and the engine says so in its own divergence block.
- **For STAR.** Covering is a purely *ordinal* verdict, and STAR is deliberately reading what the tournament throws away. Denver is **not** Pareto-dominated — ballot 3 scores Denver 5 and Chicago 0 — and Denver outscores both Boston and Chicago. The ordinal evidence says "redundant"; the cardinal evidence says "more support." That disagreement *is* the score-versus-pairwise argument, in five ballots.

Ranked Robin, as guaranteed, stays inside: Copeland ties Boston and Chicago at 2–1, both uncovered. At four candidates that tie is unavoidable — a unique Copeland winner and a Condorcet winner are the same thing there (exhaustively true over all 64 four-candidate tournaments), so a cycle forces a tie. LH's margin rung then elects **Chicago** (+1 vs Boston's −1); BetterVoting's head-to-head rung would elect **Boston** (3–2). Deterministic on both sides, and [they disagree](../../05_Ranked_Robin/01_Learn/rr_tiebreak_lh_vs_bv.md) — and the disagreement isn't arbitrary on either side: the sharpest solution in the family, the **Slater set, returns `{Boston}`**, siding with BetterVoting's rung. Two engines, two published tiebreaks, and each has a tournament solution behind it.

## The caveat before you quote this at a real election

Covering is defined on a **tournament**, which assumes *no pairwise ties*. Real ballots tie, and then the object is a *weak* tournament — and the covering relation stops having one obvious meaning. There are at least four published extensions (Gillies, Fishburn, Bordes, McKelvey), identical on tie-free tournaments and genuinely different once a tie appears. They disagreed on 125,435 of the weak tournaments we sampled. A four-candidate example, with A and B tied and everything else decided:

```text
edges:  A>C   D>A   B>C   B>D   D>C        tie:  A=B

  Gillies    {A, B}
  Fishburn   {B}
  Bordes     {B, D}
  McKelvey   {A, B, D}
```

Four defensible answers to "who is redundant here," from one election. So: **"the uncovered set" is unambiguous only when every head-to-head is decided.** Say which variant you mean otherwise. (Our own pairwise report is a For / **Equal Support** / Against table — strictly richer than a tournament, which is what makes this resolvable in principle for our cases, but it does not pick a variant for you.) The exhibit above is tie-free by construction, and all four variants agree on it.

## Sources

- **Felix Brandt, Markus Brill & Paul Harrenstein, "Tournament Solutions,"** §3.3.2 of ch. 3 in the [Handbook of Computational Social Choice](https://procaccia.info/wp-content/uploads/2020/03/comsoc.pdf) (CUP 2016) — the definition, the two-step equivalence, the matrix algorithm, Theorem 3.6, and the Pareto result. **Lean:** neutral / academic.
- Peter C. Fishburn, "Condorcet Social Choice Functions," *SIAM J. Appl. Math.* 33(3), 1977, and Nicholas R. Miller, "A New Solution Set for Tournaments and Majority Voting," *AJPS* 24(1), 1980 — the two independent origins. **Lean:** neutral.
- Kenneth A. Shepsle & Barry R. Weingast, "Uncovered Sets and Sophisticated Voting Outcomes with Implications for Agenda Institutions," *AJPS* 28(1), 1984 — the two-step / kings characterization. **Lean:** neutral.
- H. G. Landau, "On dominance relations and the structure of animal societies," *Bulletin of Mathematical Biophysics*, 1951–53 — the pecking-order work the name "Landau set" descends from; and [Stephen B. Maurer, "The King Chicken Theorems," *Mathematics Magazine* 53(2), 1980](https://www.tandfonline.com/doi/abs/10.1080/0025570X.1980.11976831) — the readable restatement of "a maximum-score bird is a king." **Lean:** neutral / academic.
- [Wikipedia, "Landau set"](https://en.wikipedia.org/wiki/Landau_set) — cited **for the aliases only**, which is what it's good for. It is thin on the rest: it credits Miller alone, never explains the Landau name, and glosses the set as a Pareto frontier. **Lean:** neutral but underdeveloped; prefer the Handbook for anything load-bearing.
- The choice sets, rates and counterexamples here were computed with Eric Pacuit & Wesley Holliday's `pref_voting` (its four covering variants) and cross-checked against the LH engine; the exhibit is reproducible via [`tournament_solutions_report.py`](../../STARVote_LH_tabulation_engine/tools_adam/pref_voting_tabulation_engine/tournament_solutions_report.py). Nothing here is asserted from memory.

## Related

- [Tournament solutions](tournament_solutions.md) — the whole C1 family, and where Ranked Robin sits in it
- [The Smith set](smith_set.md) — the coarser sibling · [the math behind Condorcet](../../05_Ranked_Robin/01_Learn/the_math_behind_condorcet.md)
- [Tournament solutions, counted](../../method_comparisons/tournament_solutions/README.md) — the runnable exhibits
- [Ranked Robin](../../05_Ranked_Robin/01_Learn/ranked_robin.md) · [its honest limits](../../05_Ranked_Robin/01_Learn/RCV_RR_honest_limits.md) · [STAR's properties and limits](../../01_STAR/01_Learn/properties_and_limits/README.md)
