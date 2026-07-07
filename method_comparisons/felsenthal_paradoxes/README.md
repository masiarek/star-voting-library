# felsenthal_paradoxes — Felsenthal's paradox examples, run for real

Worked examples from Dan S. Felsenthal, *"Review of Paradoxes Afflicting Various Voting Procedures Where One Out of m Candidates (m ≥ 2) Must Be Elected"* (University of Haifa / LSE, revised 26 May 2010; Leverhulme Trust *Voting Power in Practice* workshop, Château du Baffy, Normandy). Each example becomes a live BetterVoting election plus LH-engine YAML case(s), tagged by paradox (`paradoxes:` field) and indexed in the [paradox registry](../../00_start_here/YAML_test_case_index/PARADOX_index.md). Teaching pages: [voting_paradoxes/](../../00_start_here/voting_paradoxes/README.md).

## Cases

| Case | What it shows | Races | Live | YAML |
|---|---|---|---|---|
| [BV2144 — Felsenthal Ex.1](bv2144_mxfmhm_felsenthal_ex1.md) | Four plurality paradoxes at once (Condorcet winner, Condorcet loser, absolute loser, SCC/spoiler) in a 7-voter election; STAR resolves all four | Choose-One → Ana · STAR → Bo | [results ↗](https://bettervoting.com/mxfmhm/results) | [plurality](bv2144_mxfmhm_plurality.yaml) · [star](bv2144_mxfmhm_star.yaml) |
| [BV2145 — Felsenthal Ex.2 (1 of 2)](bv2145_6fj2kg_felsenthal_ex2.md) | Plurality-with-runoff (= IRV for 3 candidates) eliminates the Condorcet winner Ada; + the SCC note (Cleo's exit would elect Ada outright) | IRV → Ben · RR → Ada · STAR → Ada | [results ↗](https://bettervoting.com/6fj2kg/results) | [irv](bv2145_6fj2kg_irv.yaml) · [rr](bv2145_6fj2kg_ranked_robin.yaml) · [star](bv2145_6fj2kg_star.yaml) |
| [BV2146 — Felsenthal Ex.2 (2 of 2)](bv2146_krk2px_felsenthal_ex2_monotonicity.md) | Non-monotonicity, live: two voters RAISE Ben and Ben loses (elimination flips Ada→Cleo); RR & STAR unmoved | IRV → Ada · RR → Ada · STAR → Ada | [results ↗](https://bettervoting.com/krk2px/results) | [irv](bv2146_krk2px_irv.yaml) · [rr](bv2146_krk2px_ranked_robin.yaml) · [star](bv2146_krk2px_star.yaml) |

More examples from the same appendix (§A3 onward — the paradoxes afflicting the other procedures) are planned; specs go through the standard BV-backed case workflow.
