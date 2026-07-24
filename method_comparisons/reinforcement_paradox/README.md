# Reinforcement paradox — when both halves pick Ada, but the whole picks Cara

*Two districts. Ada wins both. Merge them, and **Cara** wins — the one thing a voting rule's "reinforcement" (a.k.a. **consistency**) promise says can't happen. This is a live, countable demonstration of a theorem from [Brandt, Dong & Peters, "Condorcet-Consistent Choice Among Three Candidates"](../../00_start_here/topics/condorcet/three_candidate_maximin.md) (2024): **every** [Condorcet method](../../00_start_here/topics/condorcet/README.md) must show this paradox once there are ≥ 8 voters. The lesson is fair to a fault — it cuts against STAR too, and shows exactly which methods keep the promise and which don't.*

**▶ Live on BetterVoting:** _(pending — a combined STAR + Ranked Robin election is being minted; results link will be added here.)_

→ The theorem behind it: [Condorcet-Consistent Choice Among Three Candidates](../../00_start_here/topics/condorcet/three_candidate_maximin.md) · related: [the No-Show paradox](../../00_start_here/voting_paradoxes/no_show.md) · [multiple-districts / consistency](../../00_start_here/voting_paradoxes/multiple_districts.md) · [cycle resolution](../../00_start_here/RCV_Ranked_Robin/cycle_resolution.md) · [Runoff Reversal](../../01_STAR/runoff_overturns_leader/teaching_runoff_reversal.md).

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

- **Score, Approval, and Plurality just *add points* across ballots.** A candidate's combined score is her South score plus her North score. Ada leads South and ties North, so she leads the sum — always. This is [Young's theorem (1975)](../../00_start_here/topics/condorcet/three_candidate_maximin.md): additive scoring rules satisfy reinforcement *by construction*. No electorate can ever paradox them.

- **Condorcet methods count *head-to-head majorities*, which don't add up.** Merging two electorates can create a pairwise majority that existed in neither half — here, Cara's 5–4 edges over both rivals emerge only in the union. Brandt, Dong & Peters prove this is **unavoidable**: at three candidates, *every* Condorcet extension shows the reinforcement paradox once there are ≥ 8 voters (found via a SAT solver; the bound is tight).

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
2. **It's not a bug in Ranked Robin — it's a theorem about all of Condorcet.** The [three-candidate maximin result](../../00_start_here/topics/condorcet/three_candidate_maximin.md) is the rigorous frame; this is its smallest concrete instance.
3. **Fairness cuts both ways.** The same page that credits Condorcet methods for guaranteeing the head-to-head winner has to concede they break consistency — and that STAR, via its runoff, can too. That candor is the repo's whole method.

---

*Cases (all engine-verified): [`reinf_north_c3_b6_rr.yaml`](cases/reinf_north_c3_b6_rr.yaml) · [`reinf_south_c3_b3_rr.yaml`](cases/reinf_south_c3_b3_rr.yaml) · [`reinf_combined_c3_b9_rr.yaml`](cases/reinf_combined_c3_b9_rr.yaml) · [`reinf_combined_c3_b9_star.yaml`](cases/reinf_combined_c3_b9_star.yaml). Source: Felix Brandt, Chris Dong & Dominik Peters, "Condorcet-Consistent Choice Among Three Candidates" (arXiv:2411.19857, 2024); profiles P1/P2 from the Theorem 2 proof, cast as Ada/Ben/Cara across North/South towns.*
