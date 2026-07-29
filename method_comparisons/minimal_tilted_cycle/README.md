# The minimal tilted cycle — five voters, and already the methods disagree

*Five voters. Three candidates. Every voter perfectly rational, the electorate not: **Ada beats Ben 4–1, Ben beats Cara 3–2, Cara beats Ada 3–2**. This is the smallest election in existence in which a majority cycle is **lopsided** — and that lopsidedness is exactly what pries the [Condorcet family](../../07_Concepts/topics/condorcet/README.md) apart. [Ranked Robin](../../05_Ranked_Robin/concepts/ranked_robin.md)'s Copeland count still ties all three; the [maximin](../../07_Concepts/voting_paradoxes/minimax.md) family drops Ben. Five ballots is all it takes. This page proves the minimality — by hand and by brute force — and runs every rule on it.*

→ The theorem behind it: [Condorcet-Consistent Choice Among Three Candidates](../../07_Concepts/topics/condorcet/three_candidate_maximin.md) · the collapse it complicates: [three-candidate collapse](../../07_Concepts/topics/condorcet/three_candidate_collapse.md) · the symmetric sibling: [reinforcement paradox — North district](../reinforcement_paradox/README.md) · [cycle resolution at four candidates](../../05_Ranked_Robin/concepts/cycle_resolution.md) · the tie-break shape: [three-way dead rung](../../01_STAR/tie_break_dead_rung/README.md).

---

## The ballots

| Voters | Ranking |
|:--:|---|
| 2 | Ada > Ben > Cara |
| 1 | Ben > Cara > Ada |
| 2 | Cara > Ada > Ben |

Same cast as the [reinforcement pair](../reinforcement_paradox/README.md) on purpose — it is the same paper's three-candidate world, with one thing changed: the cycle is **tilted** instead of symmetric.

## What the cycle looks like

[full report → `cases/cases_pages/tilted_cycle_c3_b5_rr.md`](cases/cases_pages/tilted_cycle_c3_b5_rr.md) · [`_tabulated` mirror](cases/cases_tabulated/tilted_cycle_c3_b5_rr_tabulated.txt)

```
Round-Robin — every pair, head-to-head (For – Against):
   Ada   beats Ben    4 – 1
   Cara  beats Ada    3 – 2
   Ben   beats Cara   3 – 2

Win–loss record — Copeland score = wins + ½·ties:
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  Ada        1–1–0         1      +2  Ben
    2  Cara       1–1–0         1      +0  Ada
    3  Ben        1–1–0         1      -2  Cara

Winner — Ranked Robin (RCV-RR): Ada
   *** 3 candidates tie for the most wins — a Condorcet cycle.
```

Nobody is a [Condorcet winner](../../07_Concepts/topics/condorcet/README.md); nobody is a Condorcet loser. Every individual ballot is transitive. The intransitivity is manufactured purely by aggregation — that is the whole content of the word *cycle*.

## Why five voters, and why 4–1 / 3–2 / 3–2

The numbers are not chosen for teaching convenience. **They are the only numbers available.** Here is the argument in full.

Fix the cycle direction A→B→C→A and look at the three margins along those arcs. Any single voter's ranking is transitive, so it agrees with either **two** of the three arcs or **one** of them (never three — that would be a cyclic ranking, and never zero — that would be the reverse cycle). So each voter contributes to the *sum* of the three cyclic margins:

- agrees with 2 arcs, disagrees with 1 → `(+1) + (+1) + (−1) = +1`
- agrees with 1 arc, disagrees with 2 → `(+1) + (−1) + (−1) = −1`

**Therefore the three cyclic margins always sum to at most *n*** (with equality only when every voter agrees with two arcs). And a second constraint comes free: with *n* voters each pairwise margin is `(votes for) − (votes against)` out of *n*, so **every margin shares *n*'s parity**. Now walk up the electorate sizes, requiring all three margins strictly positive (that is what "cycle" means):

| *n* | margins must be… | and sum ≤ *n*, so… | result |
|:--:|---|---|---|
| 1, 2 | ≥ 1 each, sum ≥ 3 | 3 > 2 | **no cycle possible** |
| **3** | odd, ≥ 1 each, sum ≥ 3 | sum = 3 exactly | **(1,1,1) only** — forced symmetric |
| **4** | even, ≥ 2 each, sum ≥ 6 | 6 > 4 | **no cycle exists at all** |
| **5** | odd, ≥ 1 each, sum ≤ 5 | (1,1,1) or **(3,1,1)** | **first tilted cycle — and only one shape** |
| 6 | even, ≥ 2 each, sum ≤ 6 | (2,2,2) only | forced symmetric again |

So: three voters give you a cycle but a perfectly symmetric one, in which no rule can prefer anyone. Four voters give you no cycle whatsoever. **Five voters is the first electorate that can tilt a cycle, and `(3,1,1)` — margins of 3, 1, 1, i.e. 4–1, 3–2, 3–2 — is the only tilted shape it can produce.** That is why the paper reaches for exactly this profile: it is not *a* small example, it is *the* minimal one, uniquely determined.

The charming coda is *n* = 6: still forced symmetric, `(2,2,2)` — which is precisely the [North district's rock-paper-scissors tie](../reinforcement_paradox/README.md). The first *even* electorate that can tilt is eight.

### Machine-checked

`minimality_check.py` in this folder enumerates every profile of strict rankings over three candidates for *n* = 1…8 — no engine, no library, pure standard library — and reports the margin shapes that actually occur:

```
n   cycles found   distinct margin shapes (largest first)
--  ------------   ---------------------------------------
1   0              —
2   0              —
3   2              (1, 1, 1)
4   0              —
5   12             (3, 1, 1), (1, 1, 1)
6   2              (2, 2, 2)
7   42             (5, 1, 1), (3, 3, 1), (3, 1, 1), (1, 1, 1)
8   12             (4, 2, 2), (2, 2, 2)
```

```bash
python3 method_comparisons/minimal_tilted_cycle/minimality_check.py
```

Exhaustive search agrees with the parity argument line for line.

## What the tilt buys: the methods split

Every winner below is computed, not asserted — Ranked Robin and RCV-IRV by the [LH engine](../../STARVote_LH_tabulation_engine/) (the two `cases/` files), the rest by [`pref_voting`](../../STARVote_LH_tabulation_engine/tools_adam/pref_voting_tabulation_engine/) as an independent witness.

| Rule | Winner(s) | Reads | Why |
|---|:--|:--:|---|
| **Copeland / [Ranked Robin](../../05_Ranked_Robin/concepts/ranked_robin.md)** | Ada, Ben, Cara — *a three-way tie* | wins | every record is 1–1 |
| ↳ LH's Ranked Robin, after tie-break | **Ada** | +margins | total margin +2 / 0 / −2 |
| **Minimax** (maximin) | **Ada, Cara** | margins | worst loss −1 each; Ben's is −3 |
| **Ranked Pairs** | Ada, Cara | margins | the [three-candidate collapse](../../07_Concepts/topics/condorcet/three_candidate_collapse.md) — |
| **Schulze** (beat path) | Ada, Cara | margins | at *m* = 3 these are |
| **Split Cycle** | Ada, Cara | margins | one and the same rule |
| **Stable Voting** | Ada, Cara | margins | as maximin |
| **Kemeny–Young** | Ada, Cara | margins | ditto |
| **Dodgson** | Ada, Cara | margins | ditto |
| **Leximax** (leximin) | **Ada** | margins | tied at −1, then +3 beats +1 |
| **Nanson** — strict | **Cara** | Borda | Ben out (4 < avg 5), then Cara beats Ada 3–2 |
| **Nanson** — weak | **Ada** | Borda | Ben *and* Cara out (≤ avg), Ada left standing |
| **Borda** | Ada | points | 6 / 5 / 4 |
| **Bucklin** · **Coombs** | Ada | ranks | — |
| **Plurality** | Ada, Cara | 1st choices | 2 / 2 / 1 |
| **[RCV-IRV](../../06_Other/RCV_IRV/concepts/README.md)** | **Cara** | 1st choices | Ben out on 1, transfers to Cara → 3–2 |

Two things to take from that table.

**First, the headline: Copeland is not in the maximin family, and five voters proves it.** On the *symmetric* cycle every one of these Condorcet rules returns all three names — indistinguishable. Tilt by a single voter and the margin-reading rules immediately see that Ben's worst defeat (−3) is far worse than anybody else's (−1) and drop him, while Copeland — which counts only *whether* you won, never *by how much* — still reports 1–1, 1–1, 1–1. That is the practical content of "[Ranked Robin](../../05_Ranked_Robin/concepts/ranked_robin.md) doesn't inherit maximin's no-show immunity": it is a different rule, and this is the smallest election where you can watch it be different.

**Second, and fairly: nobody here is wrong.** Ada, Cara, and the {Ada, Cara} set are all defensible answers, and IRV's Cara is a perfectly legitimate reading — in a cycle there is no Condorcet winner to miss, so none of these rules can be accused of missing one. What the profile shows is the *cost* of a cycle: five ballots, and reasonable rules already land in different places. Note too that strict and weak Nanson — two spellings of the same rule — disagree with each other (Cara vs Ada), though both stay inside maximin's {Ada, Cara}. Precision about tie-breaks is not pedantry; it changes the winner.

## The "three-way dead rung" connection

Ranked Robin's tie here has the shape of [the three-way dead rung](../../01_STAR/tie_break_dead_rung/README.md) — every candidate tied on the deciding measure — but only **one rung deep**:

| Rung | Symmetric 6-voter cycle | **This tilted 5-voter cycle** |
|---|---|---|
| Copeland (wins) | 1–1, 1–1, 1–1 — **dead** | 1–1, 1–1, 1–1 — **dead** |
| Total margin | 0 / 0 / 0 — **dead** | +2 / 0 / −2 — **alive** → Ada |
| Lot | decides the winner | never reached |

So the tilt is doing double duty: it is what lets maximin separate the candidates, *and* it is what lets Ranked Robin finish deterministically instead of falling to a coin. The dead rung is real but shallow.

**And there's a theorem under that table.** The six-voter tie isn't merely deeper — it is **mathematically forced**: no anonymous, neutral, Pareto rule can name a single winner whenever the voter count `n` has a divisor `r` with `1 < r ≤ m` candidates (Moulin, 1983). At `n = 6, m = 3` both 2 and 3 qualify, so *every* defensible rule ties there and the lot isn't a shortcut — it's the only thing left. At **`n = 5, m = 3` nothing is forced** (5 is prime and exceeds 3), which is exactly why five voters is the interesting number: the ballots still carry an asymmetry, and a rule that *can't* find it is discarding information rather than running out of it. That's the difference between the dead margin row and the live one. Full treatment: [Ties Are Forced](../../07_Concepts/topics/ties/ties_are_forced.md).

## Why this case is LH-only

No BetterVoting election backs it, deliberately. A Copeland three-way tie is precisely the case where [BV breaks the tie at **random**](../../05_Ranked_Robin/concepts/rr_tiebreak_lh_vs_bv.md) (head-to-head, then random) while LH breaks it by margin, then lot. A random BV result cannot be frozen into a stable teaching artifact, so minting a permanent public election here would produce an unreproducible page. The [tie-break divergence page](../../05_Ranked_Robin/concepts/rr_tiebreak_lh_vs_bv.md) covers that difference on its own terms.

## The cases

| Case | Method | Winner | Page | Source |
|---|---|:--:|---|---|
| Tilted cycle, Ranked Robin | Ranked Robin (Copeland) | Ada *(after margins tie-break)* | [page](cases/cases_pages/tilted_cycle_c3_b5_rr.md) | [yaml](cases/tilted_cycle_c3_b5_rr.yaml) |
| Tilted cycle, RCV-IRV | RCV-IRV | Cara | [page](cases/cases_pages/tilted_cycle_c3_b5_irv.md) | [yaml](cases/tilted_cycle_c3_b5_irv.yaml) |

Reproduce the wider table:

```bash
uv run STARVote_LH_tabulation_engine/tools_adam/pref_voting_tabulation_engine/cycle_resolution_report.py method_comparisons/minimal_tilted_cycle/cases/tilted_cycle_c3_b5_rr.yaml
```

---

*Source: Felix Brandt, Chris Dong & Dominik Peters, ["Condorcet-Consistent Choice Among Three Candidates"](https://arxiv.org/abs/2411.19857) (arXiv:2411.19857, 2024; [author PDF](https://dominik-peters.de/publications/maximinpara.pdf)) — neutral academic social-choice theory, summarized [here](../../07_Concepts/topics/condorcet/three_candidate_maximin.md). Cross-checks by [`pref_voting`](https://github.com/voting-tools/pref_voting) (Eric Pacuit & Wesley Holliday). Glossary: [`Condorcet cycle`](../../07_Concepts/GLOSSARY.md) · [`Copeland`](../../07_Concepts/GLOSSARY.md).*
