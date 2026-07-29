# 06_Other/Range — pure Score/Range voting examples

Score (Range) voting: sum every candidate's scores, highest total wins — STAR's scoring round with no runoff. These cases make the Score-vs-STAR difference tabulatable, including one on a **0–10 scale** (the library's 0–5 cap is a STAR teaching guardrail, not an engine limit).

**New to Range/Score?** The concept pages for this method live in [`concepts/`](concepts/README.md) — start with [Range / Score Voting](concepts/range_voting.md) (the ballot, the count, and the exaggeration problem). Everything below is the **runnable examples**.

| Case | Page | YAML |
|---|---|---|
| Range / Score Voting 101 — highest total score wins | [page](cases/cases_pages/range_101_c3_b5.md) | [`range_101_c3_b5.yaml`](cases/range_101_c3_b5.yaml) |
| Range / Score — Sullivan's Example 5.2 (0–10 scale) | — | [`range_sullivan_score_c4_b10.yaml`](cases/range_sullivan_score_c4_b10.yaml) |

The Range tabulator (pref_voting `score_voting` + hand-sum cross-check) lives in [`Range_tabulation_engine/`](Range_tabulation_engine/README.md); full mirrors in `Range_tabulated/`. Concepts: [The Score Ballot](../../07_Concepts/scores_and_ranks/score_ballot.md) · [Scale granularity can flip the winner](../../07_Concepts/scores_and_ranks/scale_granularity_flips_the_winner.md).
