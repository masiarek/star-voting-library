# One Ranked Electorate, Many Tabulations — the winner depends on the method (BV2138)

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/cxrf8v) · **[results ↗](https://bettervoting.com/cxrf8v/results)** (election `cxrf8v`).

*Robert LeGrand's flagship "the method decides everything" example, from his [ranked-ballot calculator](https://cs.angelo.edu/~rlegrand/rbvote/calc.html). 921 voters rank five candidates, and there is **no Condorcet winner** — a top cycle. Across the ~15 ranked methods the win splits **five ways**. Run through the four tabulations BetterVoting supports, one electorate yields **two different winners** — and for two years it looked like three, because this repo's engine broke the Ranked Robin tie by the wrong rung.*

→ **Level: 301 · deep dive** — Curriculum [301.11](../../07_Concepts/CURRICULUM.md). See also: [the ranked-ballot method zoo](../../07_Concepts/topics/ranked_ballot_methods_zoo.md) · [cycle resolution](../../05_Ranked_Robin/01_Learn/cycle_resolution.md) · [degrees of ties](../../05_Ranked_Robin/03_Criteria/rr_tiebreaks/degrees_of_ties.md).

## The electorate

921 voters, five candidates (Abby, Brad, Cora, Dave, Erin):

```
 98:Abby>Cora>Erin>Dave>Brad     124:Cora>Abby>Erin>Dave>Brad
 64:Brad>Abby>Erin>Cora>Dave      76:Cora>Erin>Abby>Dave>Brad
 12:Brad>Abby>Erin>Dave>Cora      21:Dave>Abby>Brad>Erin>Cora
 98:Brad>Erin>Abby>Cora>Dave      30:Dave>Brad>Abby>Erin>Cora
 13:Brad>Erin>Abby>Dave>Cora      98:Dave>Brad>Erin>Cora>Abby
125:Brad>Erin>Dave>Abby>Cora     139:Dave>Cora>Abby>Brad>Erin
                                   23:Dave>Cora>Brad>Abby>Erin
```

There is **no Condorcet winner**: the pairwise contests form a cycle (the **Smith set** — the smallest set that beats everyone outside it — is {Abby, Brad, Dave, Erin}). With no candidate beating all others, each method's cycle-handling personality picks a different winner.

## The result: five methods, five winners (four on BetterVoting)

| Method | Winner | Engines |
|---|---|---|
| **IRV (Hare)** | **Dave** | LeGrand · pref_voting · LH · **BV** |
| **STV, 1 seat** | **Dave** | LeGrand · LH · **BV** (= IRV single-winner) |
| **Ranked Robin (Copeland)** | **Brad** | LH · **BV** — *a Copeland tie, broken below* |
| **STAR (ranks→scores)** | **Brad** | LH · **BV** |
| Borda, Coombs, Baldwin, Raynaud, Schulze | Abby | LeGrand · pref_voting |
| Nanson, Tideman (Ranked Pairs), Small | Brad | LeGrand · pref_voting |
| Dodgson, Simpson (Minimax) | Cora | LeGrand · pref_voting |
| Bucklin | Erin | LeGrand · pref_voting |

Every candidate in the Smith set wins under *some* method, and even the Condorcet **loser** Cora wins under Dodgson/Simpson (she loses every duel, but only barely). This is the strongest possible statement of the repo's thesis: **with no Condorcet winner, "who won?" has no method-independent answer.**

## The Ranked Robin tie — and the "divergence" that turned out to be our bug

Copeland (Ranked Robin's core) **ties Abby and Brad**: each goes 3–1, beating three of the other four. The tally cannot separate them, so the tie goes to Ranked Robin's published [degrees of ties](../../05_Ranked_Robin/03_Criteria/rr_tiebreaks/degrees_of_ties.md) — and with exactly two finalists the **1st Degree is their own head-to-head**:

```
   Abby  beats Cora   461 – 460      Brad  beats Abby   463 – 458
   Abby  beats Erin   511 – 410      Brad  beats Cora   461 – 460
   Abby  beats Dave   485 – 436      Brad  beats Erin   623 – 298
```

**Brad beats Abby 463–458**, so Brad wins the tie at the first rung, +5 to −5. That is what BetterVoting has published on this election all along.

This page used to tell a different story. Until 2026-08-19 the LH engine had **no 1st Degree rung at all** — it ranked a Copeland tie by *total margin over the whole field*, which is the protocol's **2nd Degree**, and on these ballots Abby's +146 dwarfs Brad's +34. Not because Abby's wins are bigger — Brad's 623–298 over Erin is the largest margin anyone posts — but because Brad also absorbs a 312–609 hammering from Dave, who is not in the tie at all. So the engine elected the candidate who had lost the finalists' own match, on the strength of how a non-finalist had treated him, and the disagreement with BetterVoting was written up here as a difference of convention between two defensible ladders. It wasn't. One implementation was following the spec and the other was skipping a rung, and the one skipping it was ours. Two independent engines disagreeing is evidence that somebody is wrong — worth remembering the next time this repo finds a divergence and reaches for the word "convention."

The lesson that survives is about method definitions, not about BetterVoting: **"break the tie by margins" is not a rule until you say margins over what.** Note also that STAR's automatic runoff resolves Abby-vs-Brad by the same head-to-head → Brad, so on this electorate Ranked Robin and STAR now agree, and the split is IRV/STV's Dave against everyone else's Brad.

## The rank→score conversion (STAR race)

As in [BV2137](../center_squeeze_bv2137/bv2137_ywckmg_center_squeeze.md), the STAR race maps each ranking to 0–5 scores linearly, **top → 5, bottom → 1**:

> `score(rank) = round( 1 + 4·(N − rank) / (N − 1) )`  → for N = 5 candidates: **5, 4, 3, 2, 1**.

STAR then gives Abby the top score total (2836) but the automatic runoff flips to **Brad**, who beats Abby head-to-head 463–458 — a compact demonstration that STAR's runoff, not its score round, decides.

## Which methods are on BetterVoting — and which aren't

BetterVoting natively runs **four** of the ~15 methods (IRV, Ranked Robin, STV, STAR-via-scores). The other eleven — Borda, Bucklin, Coombs, Dodgson, Simpson, Schulze, Tideman, Nanson, Baldwin, Raynaud, Small — have no BetterVoting equivalent and are verified with [`pref_voting`](../../07_Concepts/tabulation_engines/cross_checking_with_pref_voting.md) and LeGrand's calculator. That's why the table above lists more winners than BetterVoting alone can show: it's a limit of BV's method menu, not of the election.

## Sources

- Robert LeGrand, ranked-ballot calculator — [calc.html](https://cs.angelo.edu/~rlegrand/rbvote/calc.html) · [method descriptions](https://cs.angelo.edu/~rlegrand/rbvote/desc.html)
- Live results: [bettervoting.com/cxrf8v/results](https://bettervoting.com/cxrf8v/results) · frozen export: [`bv2138_cxrf8v_bv_export.json`](cases/bv2138_cxrf8v_bv_export.json)
- Tabulatable sources: [IRV](cases/bv2138_cxrf8v_irv.yaml) · [Ranked Robin](cases/bv2138_cxrf8v_ranked_robin.yaml) · [STV](cases/bv2138_cxrf8v_stv.yaml) · [STAR](cases/bv2138_cxrf8v_star.yaml) · full detail in the sibling `_tabulated` mirrors
