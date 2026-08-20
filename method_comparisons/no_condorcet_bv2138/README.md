# no_condorcet_bv2138 — one electorate, no Condorcet winner, five winners

Robert LeGrand's flagship "the method decides everything" example from his [ranked-ballot calculator](https://cs.angelo.edu/~rlegrand/rbvote/calc.html), reproduced on BetterVoting (election `cxrf8v`, Test ID **BV2138**). 921 voters rank five candidates with **no Condorcet winner** (Smith set = Abby, Brad, Dave, Erin); across ~15 methods the win splits five ways.

**Read the lesson:** [bv2138_cxrf8v_no_condorcet.md](bv2138_cxrf8v_no_condorcet.md) — the five-way split, the Copeland tie that this repo's engine broke wrongly for two years, and which methods BetterVoting can and can't run.

| Race | Method | Winner | Read · run |
|---|---|---|:--:|
| IRV (Hare) | RCV-IRV | Dave | [page](cases/cases_pages/bv2138_cxrf8v_irv.md) · [`.yaml`](cases/bv2138_cxrf8v_irv.yaml) |
| STV, 1 seat | STV | Dave | [page](cases/cases_pages/bv2138_cxrf8v_stv.md) · [`.yaml`](cases/bv2138_cxrf8v_stv.yaml) |
| Ranked Robin | Copeland | **Brad** — both engines (LH said *Abby* until the [tie-break fix](../../05_Ranked_Robin/03_Criteria/rr_tiebreaks/degrees_of_ties.md) of 2026-08-19) | [page](cases/cases_pages/bv2138_cxrf8v_ranked_robin.md) · [`.yaml`](cases/bv2138_cxrf8v_ranked_robin.yaml) |
| STAR | STAR (ranks→scores) | **Brad** | [page](cases/cases_pages/bv2138_cxrf8v_star.md) · [`.yaml`](cases/bv2138_cxrf8v_star.yaml) |

Full field (Cora, Erin also win under other methods): see the lesson page. Up: [method_comparisons](../README.md) · sibling: [center_squeeze_bv2137](../center_squeeze_bv2137/README.md) · field guide: [ranked-ballot method zoo](../../07_Concepts/topics/ranked_ballot_methods_zoo.md)
