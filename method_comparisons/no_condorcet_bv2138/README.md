# no_condorcet_bv2138 — one electorate, no Condorcet winner, five winners

Robert LeGrand's flagship "the method decides everything" example from his [ranked-ballot calculator](https://cs.angelo.edu/~rlegrand/rbvote/calc.html), reproduced on BetterVoting (election `cxrf8v`, Test ID **BV2138**). 921 voters rank five candidates with **no Condorcet winner** (Smith set = Abby, Brad, Dave, Erin); across ~15 methods the win splits five ways.

**Read the lesson:** [bv2138_cxrf8v_no_condorcet.md](bv2138_cxrf8v_no_condorcet.md) — the five-way split, the LH-vs-BetterVoting Ranked Robin tiebreak divergence, and which methods BetterVoting can and can't run.

| Race | Method | Winner | src |
|---|---|---|:--:|
| IRV (Hare) | RCV-IRV | Dave | [`.yaml`](bv2138_cxrf8v_irv.yaml) |
| STV, 1 seat | STV | Dave | [`.yaml`](bv2138_cxrf8v_stv.yaml) |
| Ranked Robin | Copeland | **Abby** (LH) / **Brad** (BV) — tiebreak divergence | [`.yaml`](bv2138_cxrf8v_ranked_robin.yaml) |
| STAR | STAR (ranks→scores) | **Brad** | [`.yaml`](bv2138_cxrf8v_star.yaml) |

Full field (Cora, Erin also win under other methods): see the lesson page. Up: [method_comparisons](../) · sibling: [center_squeeze_bv2137](../center_squeeze_bv2137/) · field guide: [ranked-ballot method zoo](../../00_start_here/ranked_ballot_methods_zoo.md)
