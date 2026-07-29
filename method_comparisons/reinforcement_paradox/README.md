# Reinforcement paradox — when both halves pick Ada, but the whole picks Cara

*Two districts. Ada wins both. Merge them, and **Cara** wins — the one thing a voting rule's "reinforcement" (a.k.a. **consistency**) promise says can't happen. This is a live, countable demonstration of a theorem from [Brandt, Dong & Peters, "Condorcet-Consistent Choice Among Three Candidates"](../../07_Concepts/topics/condorcet/three_candidate_maximin.md) (2024): **every** [Condorcet method](../../07_Concepts/topics/condorcet/README.md) must show this paradox once there are ≥ 8 voters. The lesson is fair to a fault — it cuts against STAR too, and shows exactly which methods keep the promise and which don't.*

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/t4by6x) · **[results ↗](https://bettervoting.com/t4by6x/results)** (election `t4by6x`, BV2254) — the combined 9-voter electorate as two races (STAR + Ranked Robin); both elect **Cara**, matching the counts below.

→ The theorem behind it: [Condorcet-Consistent Choice Among Three Candidates](../../07_Concepts/topics/condorcet/three_candidate_maximin.md) · related: [the No-Show paradox](../../07_Concepts/voting_paradoxes/no_show.md) · [multiple-districts / consistency](../../07_Concepts/voting_paradoxes/multiple_districts.md) · [cycle resolution](../../05_Ranked_Robin/concepts/cycle_resolution.md) · [Runoff Reversal](../../01_STAR/runoff_overturns_leader/teaching_runoff_reversal.md).

---

## The whole story in one table

Nine voters in two towns choosing among **Ada**, **Ben**, and **Cara**. Every winner below is engine-verified (the four `cases/` files):

| Electorate | Score/Range | Approval | Plurality | **STAR** | **Ranked Robin** (Condorcet) |
|---|:--:|:--:|:--:|:--:|:--:|
| **South** (3 voters) | Ada | Ada | Ada | Ada | Ada |
| **North** (6 voters) | tie | tie | tie | tie | tie (a 3-way cycle) |
| **Combined** (9) | **Ada** ✅ | **Ada** ✅ | **Ada** ✅ | **Cara** ⚠️ | **Cara** ⚠️ |

**Reinforcement** (consistency) says: *if a candidate wins two separate electorates, she must win their union.* Ada wins South outright and is a co-winner of North's dead heat — she is a winner in **both**. So reinforcement demands Ada win the combined election. Three methods keep that promise; two break it. The rest of this page is *why*.

## The three counts

**South (3 voters) — Ada is the clear Condorcet winner.** [full report → `cases/reinf_south_c3_b3_rr.yaml`](cases/cases_tabulated/reinf_south_c3_b3_rr_tabulated.txt)

```
   Ada  beats Cara   2 – 1
   Ada  beats Ben    3 – 0
   Cara beats Ben    3 – 0
Winner — Ranked Robin: Ada (beats every opponent head-to-head — the Condorcet winner)
```

**North (6 voters) — a perfect rock-paper-scissors tie.** Ada, Ben, and Cara each win one matchup and lose one; every method ties them (Ranked Robin's Copeland count is 1–1 all round). Ada is among the winners. [full report → `cases/reinf_north_c3_b6_rr.yaml`](cases/cases_tabulated/reinf_north_c3_b6_rr_tabulated.txt)

```
   Ada  beats Ben    4 – 2
   Ben  beats Cara   4 – 2
   Cara beats Ada    4 – 2      → 3-way tie (a Condorcet cycle)
```

**Combined (9 voters) — a *new* Condorcet winner appears: Cara.** [full report → `cases/reinf_combined_c3_b9_rr.yaml`](cases/cases_tabulated/reinf_combined_c3_b9_rr_tabulated.txt)

```
   Ada  beats Ben    7 – 2
   Cara beats Ada    5 – 4
   Cara beats Ben    5 – 4
Winner — Ranked Robin: Cara (beats every opponent head-to-head — the Condorcet winner)
```

Cara now beats *everyone* head-to-head, so every Condorcet method elects her — and Ada, the only candidate who won both halves, loses. **That is the reinforcement paradox.**

## Why additive methods keep the promise — and Condorcet methods can't

The split is not an accident of these numbers; it's structural.

- **Score, Approval, and Plurality just *add points* across ballots.** A candidate's combined score is her South score plus her North score. Ada leads South and ties North, so she leads the sum — always. This is [Young's theorem (1975)](../../07_Concepts/topics/condorcet/three_candidate_maximin.md): additive scoring rules satisfy reinforcement *by construction*. No electorate can ever paradox them.

- **Condorcet methods count *head-to-head majorities*, which don't add up.** Merging two electorates can create a pairwise majority that existed in neither half — here, Cara's 5–4 edges over both rivals emerge only in the union. Brandt, Dong & Peters prove this is **unavoidable**: at three candidates, *every* Condorcet extension shows the reinforcement paradox once there are ≥ 8 voters (found via a SAT solver; the bound is tight).

### Two older theorems that sharpen both halves

The Brandt–Dong–Peters result above is a *tight three-candidate* statement. The classical literature bounds the same two claims more broadly, and the pair is worth having side by side.

**The Condorcet half generalizes past three candidates.** Zwicker's **Proposition 2.5** states it without any ceiling: *all Condorcet extension SCFs for **three or more** alternatives violate reinforcement.* The proof is elementary — no SAT solver — and it runs on **exactly the profiles in this folder**: the symmetric 6-voter cycle as one electorate, a 3-voter district with a clear Condorcet winner as the other. (The convergence is worth noting: two papers three decades apart reach for the same construction. It is the canonical witness, which is why the same ballots keep reappearing.) So what BDP add is *tightness at m = 3*; what Zwicker adds is *no upper limit on m* — with Pareto assumed, extending the proof to four or more candidates is straightforward.

**The additive half is an exact characterization, not just "scoring rules pass."** The version usually quoted — Young's — runs one direction: additive scoring rules are reinforcing. The full result is an **iff**, and it names the whole class:

> **Theorem (Smith 1973; Young 1975).** The anonymous, neutral, and reinforcing SCFs are **exactly the compound scoring rules.**

A **compound scoring rule** allows a cascade of [score vectors](../../07_Concepts/topics/ranked_ballot_methods_zoo.md): ties under `w₁` are broken by score differences under a second vector `w₂` (say, plurality score to separate tied Borda winners), a third if any remain, and so on for any finite number. Add one further axiom — **continuity**, aka the **Archimedean property** (for any `s` and any `t` with a unique winner `x`, enough copies of `t` eventually carry the merged election: `f(s + j·t) = {x}` for all large `j`) — and the class narrows to the *simple*, one-vector scoring rules.

That converse is what makes this page's verdict sharp rather than anecdotal. **STAR fails reinforcement, so STAR is provably not a compound scoring rule** — no cascade of score vectors, however elaborate, reproduces it. Its scoring round is a scoring rule; the automatic runoff is not, and the theorem says that is exactly the step where the promise had to break. Same for [Ranked Robin](../../05_Ranked_Robin/concepts/ranked_robin.md), [RCV-IRV](../../06_Other/RCV_IRV/concepts/), and every other method here with an elimination or runoff stage. Conversely it explains why Score, Approval and Plurality can *never* be paradoxed this way: they are simple scoring rules, and the theorem covers them by construction.

## Whichever way the cycle falls — the other two branches

One detail the table above glosses, and it matters for anyone reproducing this.

North is a **perfect three-way tie**, so an anonymous, neutral rule can only return *all three* candidates as co-winners — and then the single South district above is enough, because Ada is inside that set. But the LH engine is **resolute**: it must print one name, and it gets there by spending neutrality on a published lot order (the [`lot_numbers`](../../07_Concepts/topics/ties/ties_are_forced.md) field). With `[Ada, Ben, Cara]` it prints **Ada** — which is why the original trio works.

Change the lot and the original South no longer springs the trap: if North resolved to Ben, then North and South would share no winner at all, reinforcement's hypothesis would never fire, and nothing would look wrong. That is not a hole in the theorem — Zwicker's proof handles it by permuting the second district — but it *is* a hole in a demonstration built from one pair. So the other two branches are now built too. North is unchanged and invariant under the rotation Ada→Ben→Cara→Ada, so rotating South gives each branch:

| If the cycle resolves to… | South district | South elects | **Merged 9 voters elect** |
|---|---|:--:|:--:|
| **Ada** | [`reinf_south_c3_b3_rr`](cases/reinf_south_c3_b3_rr.yaml) | Ada | **Cara** ⚠️ |
| **Ben** | [`reinf_south_ben_c3_b3_rr`](cases/reinf_south_ben_c3_b3_rr.yaml) | Ben | **Ada** ⚠️ |
| **Cara** | [`reinf_south_cara_c3_b3_rr`](cases/reinf_south_cara_c3_b3_rr.yaml) | Cara | **Ben** ⚠️ |

Every row is engine-verified, and every merged winner is a *strict* Condorcet winner with the same 5–4 / 5–4 / 7–2 signature, rotated:

```
Ben branch  (cases/reinf_combined_ben_c3_b9_rr.yaml)
   Ada   beats Ben    5 – 4
   Ada   beats Cara   5 – 4
   Ben   beats Cara   7 – 2
Winner — Ranked Robin: Ada   (both halves had said Ben)

Cara branch (cases/reinf_combined_cara_c3_b9_rr.yaml)
   Ben   beats Ada    5 – 4
   Ben   beats Cara   5 – 4
   Cara  beats Ada    7 – 2
Winner — Ranked Robin: Ben   (both halves had said Cara)
```

So the failure does not depend on a lucky lot draw. **Whichever candidate the cycle is resolved to, there is a South district that agrees with that choice and a merged electorate that overturns it** — which is the case analysis in Zwicker's proof, made runnable.

## Where STAR lands — and the honest catch

STAR is a score ballot **plus** an automatic runoff, so it's half-and-half — and this case pins down exactly which half wins. On the combined 9 ballots:

```
Scoring Round
   Ada   -- 29 -- First place     ← the pure Score result: Ada. Consistent. No paradox here.
   Cara  -- 27 -- Second place
   Ben   -- 16
Automatic Runoff Round
   Cara  -- 5 -- First place       ← the runoff is a pairwise step, and it
   Ada   -- 4                         catches Cara's head-to-head win — flips to Cara.
 Cara wins.

[Runoff Reversal]  Score Round Winner = Ada, Runoff Winner = Cara
[Condorcet Winner] Cara — matches the STAR winner
[Divergence from STAR] Choose-One = Ada, Approval = Ada (both differ from STAR)
```

STAR's **scoring round elects Ada** — the consistent, additive answer. But STAR's **runoff re-imports the very pairwise flip** that trips the Condorcet methods, and elects **Cara**. So STAR does *not* escape this paradox: it inherits it through the runoff. Saying so plainly is the point — STAR buys a majority-honest final round, and the price is that the final round can side with a merge-created majority against the additive winner. (Pure Score would have kept Ada; STAR's runoff is where consistency gives way.)

Want the whole count? Full LH report → [`cases/cases_tabulated/reinf_combined_c3_b9_star_tabulated.txt`](cases/cases_tabulated/reinf_combined_c3_b9_star_tabulated.txt).

## What to take away

1. **"Both halves agreed, so the whole must agree" is a promise only some methods keep.** Additive point methods (Score, Approval, Plurality) keep it; Condorcet methods provably cannot at ≥ 8 voters; STAR keeps it in the scoring round but can lose it in the runoff.
2. **It's not a bug in Ranked Robin — it's a theorem about all of Condorcet.** The [three-candidate maximin result](../../07_Concepts/topics/condorcet/three_candidate_maximin.md) is the rigorous frame; this is its smallest concrete instance.
3. **Fairness cuts both ways.** The same page that credits Condorcet methods for guaranteeing the head-to-head winner has to concede they break consistency — and that STAR, via its runoff, can too. That candor is the repo's whole method.

---

*Cases (all engine-verified) — the original trio: [`reinf_north_c3_b6_rr.yaml`](cases/reinf_north_c3_b6_rr.yaml) · [`reinf_south_c3_b3_rr.yaml`](cases/reinf_south_c3_b3_rr.yaml) · [`reinf_combined_c3_b9_rr.yaml`](cases/reinf_combined_c3_b9_rr.yaml) · [`reinf_combined_c3_b9_star.yaml`](cases/reinf_combined_c3_b9_star.yaml); the two rotated branches: [`reinf_south_ben_c3_b3_rr.yaml`](cases/reinf_south_ben_c3_b3_rr.yaml) · [`reinf_combined_ben_c3_b9_rr.yaml`](cases/reinf_combined_ben_c3_b9_rr.yaml) · [`reinf_south_cara_c3_b3_rr.yaml`](cases/reinf_south_cara_c3_b3_rr.yaml) · [`reinf_combined_cara_c3_b9_rr.yaml`](cases/reinf_combined_cara_c3_b9_rr.yaml).*

*Sources: Felix Brandt, Chris Dong & Dominik Peters, "Condorcet-Consistent Choice Among Three Candidates" (arXiv:2411.19857, 2024) — profiles P1/P2 from the Theorem 2 proof, cast as Ada/Ben/Cara across North/South towns; the tight ≥ 8-voter bound at three candidates. **Lean:** neutral. · William S. Zwicker, "Introduction to the Theory of Voting," in *Handbook of Computational Social Choice* (CUP 2016), §2.6 — Proposition 2.5 (no ceiling on the candidate count) and Theorem 2.4 (Smith 1973; Young 1975), the compound-scoring-rule characterization and the continuity/Archimedean axiom. **Lean:** neutral.*
