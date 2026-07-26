# Tournament solutions, counted — five defensible winners from three ballots

The tabulatable evidence behind [Tournament solutions — the theory of the win-loss graph](../../00_start_here/topics/tournament_solutions.md). A **tournament solution** is a rule that reads *only* the win-loss graph — who beat whom, margins thrown away — which is [Fishburn's C1 tier](../../00_start_here/topics/what_a_method_reads.md). [Ranked Robin](../../00_start_here/RCV_Ranked_Robin/ranked_robin.md) is one member of that family (it is Copeland); the academic literature holds a dozen more, and they disagree.

The first two cases are the *textbook's own figures* turned back into ballots — Brandt, Brill & Harrenstein, "Tournament Solutions," ch. 3 of the [Handbook of Computational Social Choice](https://procaccia.info/wp-content/uploads/2020/03/comsoc.pdf) (2016). The chapter draws graphs; [McGarvey's theorem](../../00_start_here/topics/tournament_solutions.md) guarantees some electorate produces each one, and these three-voter profiles are the smallest we found that do. Candidate labels stay bare `A`–`E` on purpose, matching the figures, so the book can be read beside the tabulation.

All three are **LH-only**. The `five_answers` case turns on a Copeland tiebreak, and BetterVoting breaks Ranked Robin ties [at random](../../00_start_here/RCV_Ranked_Robin/rr_tiebreak_lh_vs_bv.md) — an unfreezable result. The `copeland_vs_clones` case needs no live tally at all; its point is a disagreement between two published rules. The `star_elects_a_covered_candidate` case has an engine-independent STAR result, but its Ranked Robin comparison line depends on which tiebreak ladder you run.

| Case (source) | Ballots | What it shows |
|---|:--:|---|
| [`five_answers_one_election_c4_b3.yaml`](cases/five_answers_one_election_c4_b3.yaml) | 3 | **Five different defensible winners from one election.** Top cycle `{A,B,C,D}` · uncovered = Banks = bipartisan `{A,B,D}` · Copeland `{A,B}` · Slater = Markov `{A}`. Ranked Robin lands on `{A,B}` and breaks it by **margin**, electing **B** — where Slater and Markov both elect A. (Chapter Figure 3.3.) |
| [`star_elects_a_covered_candidate_c4_b5.yaml`](cases/star_elects_a_covered_candidate_c4_b5.yaml) | 5 | **STAR lands outside the [uncovered set](../../00_start_here/topics/uncovered_set.md)** — the weakest structural filter there is. Chicago beats Denver *and* beats Austin, the only city Denver beats, so **Denver is covered**; the uncovered set is `{Austin, Boston, Chicago}` and STAR elects the fourth. Strict ballots throughout, so no result is a tie-breaking artifact. Both halves stated: no graph-only rule would elect Denver, but Denver is **not** Pareto-dominated and outscores two of the three. Ranked Robin stays inside, as it must |
| [`copeland_vs_clones_c5_b3.yaml`](cases/copeland_vs_clones_c5_b3.yaml) | 3 | **Copeland vs composition-consistency.** `{A,B,C}` is a component inside a bigger cycle, so "choose the best from the best components" forces a solution to return **all five**; uncovered, Banks and bipartisan do. Copeland returns **`{D}`** alone and Ranked Robin elects D outright — the published failure of composition-consistency, and the arithmetic behind RR's [teaming weakness](../../00_start_here/RCV_Ranked_Robin/rr_clone_independence.md). (Chapter Figures 3.1–3.2.) |

## Running them

The LH engine tabulates the Copeland / Ranked Robin column and writes the `_tabulated` mirror:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/tournament_solutions/cases/five_answers_one_election_c4_b3.yaml
```

The other six solutions have no LH implementation. This repo tool prints them all at once — plus the tournament `M(T)` itself, the outdegrees, and the chapter's axiom table — via `pref_voting`:

```bash
uv run STARVote_LH_tabulation_engine/tools_adam/pref_voting_tabulation_engine/tournament_solutions_report.py method_comparisons/tournament_solutions/cases/five_answers_one_election_c4_b3.yaml
```

Its closing line is the one that matters for this library:

```
The tournament does NOT decide this election: Copeland ties {A, B}.
LH's Ranked Robin breaks that tie by TOTAL MARGIN — A +1, B +3 — electing B.
Margins are not in the tournament. The moment Ranked Robin reaches for
them it has stepped out of C1 and is reading C2 information.
```

## Two caveats the tool prints for you

- **A choice set with several names has not failed.** Irresoluteness is the normal state of a tournament solution — narrowing to a single winner always takes information from outside the graph, or a lot.
- **A tournament requires no pairwise ties.** Real ballots tie, and then the object is a *weak* tournament (chapter §3.5) where these rules are generalizations with no canonical extension. Both cases here are tie-free by construction; the tool warns when a file isn't.

## Related

- [Tournament solutions](../../00_start_here/topics/tournament_solutions.md) — the teaching page · [what a method reads](../../00_start_here/topics/what_a_method_reads.md) — the C1/C2/C3 tiers
- [The math behind Condorcet](../../00_start_here/RCV_Ranked_Robin/the_math_behind_condorcet.md) — tournaments, Smith/Schwartz · [the Smith set](../../00_start_here/topics/smith_set.md)
- [Cycle resolution, counted](../cycle_resolution/README.md) — the **C2** sibling: what Minimax, Ranked Pairs and Schulze do with the margins these rules discard
