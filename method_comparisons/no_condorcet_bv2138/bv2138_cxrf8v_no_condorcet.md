# One Ranked Electorate, Many Tabulations — the winner depends on the method (BV2138)

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/cxrf8v) · **[results ↗](https://bettervoting.com/cxrf8v/results)** (election `cxrf8v`).

*Robert LeGrand's flagship "the method decides everything" example, from his [ranked-ballot calculator](https://cs.angelo.edu/~rlegrand/rbvote/calc.html). 921 voters rank five candidates, and there is **no Condorcet winner** — a top cycle. Across the ~15 ranked methods the win splits **five ways**. Run through the four tabulations BetterVoting supports, one electorate yields **three different winners** — and one of them is a documented LH-vs-BetterVoting tiebreak divergence.*

→ **Level: Voting 301** — Curriculum [301.10](../../00_start_here/CURRICULUM.md). See also: [the ranked-ballot method zoo](../../00_start_here/topics/ranked_ballot_methods_zoo.md) · [cycle resolution](../../00_start_here/RCV_Ranked_Robin/cycle_resolution.md) · [RR tiebreak: LH vs BV](../../00_start_here/RCV_Ranked_Robin/rr_tiebreak_lh_vs_bv.md).

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
| **Ranked Robin (Copeland)** | **Abby** (LH) / **Brad** (BV) | *see divergence below* |
| **STAR (ranks→scores)** | **Brad** | LH · **BV** |
| Borda, Coombs, Baldwin, Raynaud, Schulze | Abby | LeGrand · pref_voting |
| Nanson, Tideman (Ranked Pairs), Small | Brad | LeGrand · pref_voting |
| Dodgson, Simpson (Minimax) | Cora | LeGrand · pref_voting |
| Bucklin | Erin | LeGrand · pref_voting |

Every candidate in the Smith set wins under *some* method, and even the Condorcet **loser** Cora wins under Dodgson/Simpson (she loses every duel, but only barely). This is the strongest possible statement of the repo's thesis: **with no Condorcet winner, "who won?" has no method-independent answer.**

## The Ranked Robin divergence: LH ≠ BetterVoting

Copeland (Ranked Robin's core) **ties Abby and Brad** — each wins three head-to-heads and loses two. The two engines break that tie by different rules, and here the rules disagree:

```
   Abby  beats Cora   461 – 460      Brad  beats Abby   463 – 458
   Abby  beats Erin   511 – 410      Brad  beats Cora   461 – 460
   Abby  beats Dave   485 – 436      ...
```

- **LH** breaks the Copeland tie by **total margin, then lot** → **Abby** (her wins are by larger margins).
- **BetterVoting** breaks it **head-to-head** → **Brad** (Brad beats Abby directly, 463–458).

Both are deterministic here; they simply encode different notions of "who deserves the tie." This is the same LH-vs-BV Ranked Robin tiebreak split documented in [`rr_tiebreak_lh_vs_bv.md`](../../00_start_here/RCV_Ranked_Robin/rr_tiebreak_lh_vs_bv.md). The `.yaml`'s `expected_winners` is LH's **Abby** (that's what the LH engine computes and the test suite checks); BetterVoting's live result is **Brad**. Note that STAR's automatic runoff *also* resolves Abby-vs-Brad head-to-head → Brad, so BV's Ranked Robin and STAR agree, and LH's Ranked Robin is the lone Abby.

## The rank→score conversion (STAR race)

As in [BV2137](../center_squeeze_bv2137/bv2137_ywckmg_center_squeeze.md), the STAR race maps each ranking to 0–5 scores linearly, **top → 5, bottom → 1**:

> `score(rank) = round( 1 + 4·(N − rank) / (N − 1) )`  → for N = 5 candidates: **5, 4, 3, 2, 1**.

STAR then gives Abby the top score total (2836) but the automatic runoff flips to **Brad**, who beats Abby head-to-head 463–458 — a compact demonstration that STAR's runoff, not its score round, decides.

## Which methods are on BetterVoting — and which aren't

BetterVoting natively runs **four** of the ~15 methods (IRV, Ranked Robin, STV, STAR-via-scores). The other eleven — Borda, Bucklin, Coombs, Dodgson, Simpson, Schulze, Tideman, Nanson, Baldwin, Raynaud, Small — have no BetterVoting equivalent and are verified with [`pref_voting`](../../00_start_here/tabulation_engines/cross_checking_with_pref_voting.md) and LeGrand's calculator. That's why the table above lists more winners than BetterVoting alone can show: it's a limit of BV's method menu, not of the election.

## Sources

- Robert LeGrand, ranked-ballot calculator — [calc.html](https://cs.angelo.edu/~rlegrand/rbvote/calc.html) · [method descriptions](https://cs.angelo.edu/~rlegrand/rbvote/desc.html)
- Live results: [bettervoting.com/cxrf8v/results](https://bettervoting.com/cxrf8v/results) · frozen export: [`bv2138_cxrf8v_bv_export.json`](cases/bv2138_cxrf8v_bv_export.json)
- Tabulatable sources: [IRV](cases/bv2138_cxrf8v_irv.yaml) · [Ranked Robin](cases/bv2138_cxrf8v_ranked_robin.yaml) · [STV](cases/bv2138_cxrf8v_stv.yaml) · [STAR](cases/bv2138_cxrf8v_star.yaml) · full detail in the sibling `_tabulated` mirrors
