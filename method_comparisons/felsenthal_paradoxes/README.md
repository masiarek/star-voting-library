# felsenthal_paradoxes — Felsenthal's paradox examples, run for real

Worked examples from Dan S. Felsenthal, *"Review of Paradoxes Afflicting Various Voting Procedures Where One Out of m Candidates (m ≥ 2) Must Be Elected"* (University of Haifa / LSE, revised 26 May 2010; Leverhulme Trust *Voting Power in Practice* workshop, Château du Baffy, Normandy). Each example becomes a live BetterVoting election plus LH-engine YAML case(s), tagged by paradox (`paradoxes:` field) and indexed in the [paradox registry](../../00_start_here/YAML_test_case_index/PARADOX_index.md). Teaching pages: [voting_paradoxes/](../../00_start_here/voting_paradoxes/README.md).

## Cases

| Case | What it shows | Races | Live | YAML |
|---|---|---|---|---|
| [BV2144 — Felsenthal Ex.1](bv2144_mxfmhm_felsenthal_ex1.md) | Four plurality paradoxes at once (Condorcet winner, Condorcet loser, absolute loser, SCC/spoiler) in a 7-voter election; STAR resolves all four | Choose-One → Ana · STAR → Bo | [results ↗](https://bettervoting.com/mxfmhm/results) | [plurality](bv2144_mxfmhm_plurality.yaml) · [star](bv2144_mxfmhm_star.yaml) |

More examples from the same appendix (§A2 onward — the paradoxes afflicting other procedures) are planned; specs go through the standard BV-backed case workflow.
