# pref_voting Tabulation Engine (independent cross-check)

A third tabulation engine for the repo — but with a job the other two don't have: it's the **independent referee.** It wraps Eric Pacuit's [`pref_voting`](https://github.com/voting-tools/pref_voting) library (a peer-reviewed Python social-choice package) and runs it on the *same* YAML elections as the LH and RCV-IRV engines, then **compares the results** so we know our winners are right, not just self-consistent.

Unlike the [RCV-IRV engine](../../../06_Other/RCV_IRV/RCV_IRV_tabulation_engine/README.md), `pref_voting` is **not vendored** — it's a large, actively-maintained PyPI package, so it's an optional dependency:

```bash
pip install pref_voting        # or: pip install -e STARVote_LH_tabulation_engine[crosscheck]
```

## Usage

```bash
# one election — shows each method's winner from BOTH engines, side by side
python pref_voting_tabulation.py example_tennessee.yaml

# cross-check every single-winner election in the repo
python pref_voting_tabulation.py --all
```

Any STAR-style (score) **or** ranked (`A>B>C`) YAML works — score ballots are converted to rankings the same way the engines do (higher score = higher preference, 0 = unranked).

## What it checks

| Method | Role |
|--------|------|
| **Condorcet** | cross-checked vs LH (tie-aware) — always |
| **RCV-IRV** | cross-checked vs LH (truncation preserved; unranked = exhausted) |
| **Plurality** | cross-checked vs LH |
| **Copeland (= Ranked Robin)** | bonus — `pref_voting` computes it, the LH engine doesn't |
| **Borda** | bonus |
| **STAR** | *not available* — `pref_voting` has no STAR; the runoff is covered by the STAR positive tests |

When `pref_voting` reports a **tie** (a set of co-winners), the cross-check only requires the LH engine's pick to be *among* them — cross-engine tie-breaking legitimately differs (e.g. a 1–1 IRV final round, or bullet/truncated ballots).

## Status

Run across the repo's single-winner elections: **0 mismatches** — the LH engine's Condorcet / IRV / Plurality machinery is independently confirmed. Wired into [`tests/test_pref_voting_crosscheck.py`](../../tests/test_pref_voting_crosscheck.py) (skips cleanly if `pref_voting` isn't installed). Full write-up: [Cross-checking the LH engine with pref_voting](../../../07_Concepts/tabulation_engines/cross_checking_with_pref_voting.md).

## Ranked Robin report (independent cross-check)

The **LH engine now tabulates Ranked Robin first-class** — set `voting_method: RankedRobin` and it prints the round-robin (ballots + pairwise table + win-loss record) itself. This script is the **independent second opinion**: a dependency-light Ranked Robin (RCV-RR / Copeland) report you can run beside the LH engine to confirm the head-to-heads agree:

```bash
python ranked_robin_report.py ../../../05_Ranked_Robin/02_Examples/cases/ranked_robin_consensus_center.yaml
```

It uses the LH pairwise-matrix helper (`pref_voting` only for an optional Copeland cross-check) and **flags a cycle** when the leaders tie on wins — pointing to [Cycle Resolution — why Minimax, Ranked Pairs, and Schulze exist](../../../05_Ranked_Robin/01_Learn/cycle_resolution.md).

## Coombs and Minimax reports (methods nothing else here counts)

Two rules in Felsenthal's appendix have no tabulator anywhere in the stack — the LH engine sends ranked ballots to pyrankvote (Hare IRV), and BetterVoting offers neither. Their examples were prose for that reason. These two tools count them, each cross-checked against `pref_voting` on every run:

```bash
uv run minimax_report.py ../../../method_comparisons/felsenthal_paradoxes/cases/minimax_ex30_noshow_before.yaml
uv run coombs_report.py  ../../../method_comparisons/felsenthal_paradoxes/cases/coombs_ex18_monotonicity.yaml
```

- **`minimax_report.py`** — the Condorcet / Simpson-Kramer rule: elect the Condorcet winner, else whoever's *worst pairwise loss* is smallest. Prints the full matrix, then the worst-loss table under **winning votes** (Felsenthal's convention) and **margins** (`pref_voting`'s) side by side, saying whether they agree — they must on an odd electorate with no drawn pairs, and need not otherwise. Ends by contrasting **Copeland** (LH's Ranked Robin) reading the very same matrix. `--drop NAME` recounts without a candidate (the SCC test); `--equal-prob` switches to Felsenthal's ½–½ reading of pairs a truncated ballot left unstated, which is the whole of his Example 31.
- **`coombs_report.py`** — delete the candidate ranked *last* by the most voters until someone holds a majority. Prints every round's first- and last-place counts and the deletion, warns when a deletion or the winner falls to a lot, and contrasts Hare IRV on the same ballots. `--drop NAME` for the SCC test.

Both are used by [`coombs.md`](../../../07_Concepts/voting_paradoxes/coombs.md) and [`minimax.md`](../../../07_Concepts/voting_paradoxes/minimax.md), whose 18 worked examples they reproduce.

## Successive elimination and the grade methods

Three more procedures with no tabulator anywhere in the stack, added for the rest of Felsenthal's worked-tables pages:

- **`successive_elimination_report.py`** — the parliamentary / amendment procedure: candidates meet in pairwise majority votes in a fixed **agenda** order, each round's loser is eliminated, the last survivor wins. `--agenda` is the point rather than a detail: under a Condorcet cycle the agenda-setter picks the winner, which is Felsenthal's Example 9 electing a Pareto-dominated candidate under one order and a different candidate under another. `--tiebreak alpha|agenda` because the published examples disagree on how a tied round breaks, and the report re-runs the other convention and says whether the winner moves. `--drop` for the SCC test. This is the one tool here with **no `pref_voting` counterpart** — the library has no agenda-based method — so its independent check is structural: head-to-heads come from the LH engine's own pairwise matrix, and since the procedure is Condorcet-consistent the report asserts it elected the Condorcet winner whenever one exists.
- **`grade_methods_report.py`** — **Range Voting** (highest mean) and **Majority Judgment** (highest median, with the Balinski–Laraki tie-break) on grade ballots of any scale, numeric `1-10` or letters `A-J`. Reads a `grades:` block — Felsenthal's own table, voters across the header, one row per candidate — because these scales fit neither the LH engine's 0–5 validation nor BetterVoting's ballot, and rescaling would change his numbers. Two separate levers, since the examples need both: `--ungrade CAND/VOTER` strikes one **cell** (truncation — the voter still votes and still grades everyone else), `--abstain VOTER` removes a **voter** (no-show — which changes the denominator, and that is what moves a median). Both winners are cross-checked against `pref_voting`'s `score_voting` and `majority_judgement`.

Used by [`successive_elimination.md`](../../../07_Concepts/voting_paradoxes/successive_elimination.md), [`range_voting.md`](../../../07_Concepts/voting_paradoxes/range_voting.md) and [`majority_judgment.md`](../../../07_Concepts/voting_paradoxes/majority_judgment.md).

## Files

- `pref_voting_tabulation.py` — the cross-check wrapper (parser + both engines + compare).
- `ranked_robin_report.py` — friendly Ranked Robin / Copeland report for one or more files.
- `minimax_report.py` — Minimax / Simpson-Kramer, both worst-loss conventions, vs Copeland.
- `coombs_report.py` — Coombs' procedure round by round, vs Hare IRV.
- `successive_elimination_report.py` — the agenda procedure; `--agenda`, `--tiebreak`, `--drop`.
- `grade_methods_report.py` — Range (mean) and Majority Judgment (median) on any grade scale.
- `contingent_vote_report.py` — the Contingent and Supplementary Vote.
- `tournament_solutions_report.py` — the C1 tournament solutions, side by side.
- `example_tennessee.yaml` — a demo election (the classic 3-methods-3-winners case).
