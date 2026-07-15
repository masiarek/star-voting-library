# center_squeeze_bv2137 — one electorate, four tabulations (center squeeze)

The textbook **center squeeze** from Robert LeGrand's [ranked-ballot calculator](https://cs.angelo.edu/~rlegrand/rbvote/calc.html), reproduced on BetterVoting (election `ywckmg`, Test ID **BV2137**). 100 voters rank three candidates; the centrist **Anderson** is the Condorcet winner but has the fewest first-choices, so IRV/STV eliminate him and elect Carter, while Ranked Robin and STAR elect Anderson.

**Read the lesson:** [bv2137_ywckmg_center_squeeze.md](bv2137_ywckmg_center_squeeze.md) — the four-way result, the LeGrand ↔ pref_voting ↔ LH ↔ BV agreement table, and the rank→score conversion.

| Race | Method | Winner | src |
|---|---|---|:--:|
| IRV (Hare) | RCV-IRV | Carter | [`.yaml`](bv2137_ywckmg_irv.yaml) |
| STV, 1 seat | STV | Carter | [`.yaml`](bv2137_ywckmg_stv.yaml) |
| Ranked Robin | Copeland | **Anderson** (Condorcet) | [`.yaml`](bv2137_ywckmg_ranked_robin.yaml) |
| STAR | STAR (ranks→scores) | **Anderson** | [`.yaml`](bv2137_ywckmg_star.yaml) |

Up: [method_comparisons](../) · sibling: [no_condorcet_bv2138](../no_condorcet_bv2138/) · field guide: [ranked-ballot method zoo](../../00_start_here/topics/ranked_ballot_methods_zoo.md)
