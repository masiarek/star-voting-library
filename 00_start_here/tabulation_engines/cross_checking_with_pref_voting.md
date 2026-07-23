# Cross-checking the LH engine with `pref_voting`

**One line:** an independent referee. The repo's results are checked against [`pref_voting`](https://github.com/voting-tools/pref_voting) (Eric Pacuit's peer-reviewed Python social-choice library), so we know the LH engine's ranked-ballot machinery — **Condorcet, RCV-IRV, Plurality** — is correct, not just internally consistent.

→ engine: [the pref_voting engine](../../STARVote_LH_tabulation_engine/tools_adam/pref_voting_tabulation_engine/) · test: [`tests/test_pref_voting_crosscheck.py`](../../STARVote_LH_tabulation_engine/tests/test_pref_voting_crosscheck.py).

---

## Why have a second engine at all?

A tabulation engine that only checks itself can be *consistently wrong*. `pref_voting` is written by a different author, on different code, for academic social-choice research — so when it agrees with the LH engine on the same ballots, that agreement is real evidence. This is the same logic behind reconciling against BetterVoting, but `pref_voting` is a **neutral third party** (it isn't STAR-affiliated) and covers the classic ranked methods in depth.

## What it can and can't check

| Method | Cross-checked? | Notes |
|--------|:---:|-------|
| **Condorcet winner** | ✅ always | tie-aware on both sides (equal scores = no preference) |
| **RCV-IRV** | ✅ | truncation preserved (unranked = exhausted, like the LH engine) |
| **Plurality** | ✅ | first-choice (top score) winner |
| **Copeland (= Ranked Robin)** | ➕ bonus | `pref_voting` computes it; the LH engine doesn't — shown for interest |
| **Borda** | ➕ bonus | same |
| **STAR** | ❌ | `pref_voting` has **no STAR** (score-then-runoff). STAR's runoff is covered by the [STAR positive tests](../../STARVote_LH_tabulation_engine/tests/test_single_winner_positive.py) instead. |

So this validates the *machinery around* STAR (the pairwise matrix, the RCV-IRV cross-count, first-choice tallies) — exactly the parts most prone to subtle bugs.

## How ties are handled (the important subtlety)

`pref_voting` methods return the **set of co-winners**. When that set has more than one member, the election is genuinely tied under that method, and different engines break the tie by different rules — both legitimate. So the cross-check only requires the LH engine's single winner to be **among** `pref_voting`'s co-winners; it does *not* demand the same tie-break. (Two real cases this matters: a 1–1 IRV final round, and bullet/truncated ballots where unranked candidates are exhausted.)

## Current status

Run across **87 single-winner elections** in the repo (every ranked file plus every STAR score file, rankings derived from the scores): **0 mismatches.** Every Condorcet, IRV, and Plurality winner the LH engine reports is confirmed by `pref_voting`.

## Run it yourself

```
pip install pref_voting            # optional dev dependency
cd STARVote_LH_tabulation_engine/tools_adam/pref_voting_tabulation_engine
python pref_voting_tabulation.py --all                     # full repo
python pref_voting_tabulation.py ../path/to/election.yaml
# the guard (from the LH engine dir):
pytest ../STARVote_LH_tabulation_engine/tests/test_pref_voting_crosscheck.py
```

Two companion reports live in the same folder, for the methods the LH engine doesn't implement at all:

```bash
uv run …/pref_voting_tabulation_engine/ranked_robin_report.py FILE.yaml         # the independent Copeland third opinion
uv run …/pref_voting_tabulation_engine/cycle_resolution_report.py FILE.yaml     # Minimax / Ranked Pairs / Schulze / Split Cycle / Stable Voting
uv run …/pref_voting_tabulation_engine/cycle_resolution_report.py FILE.yaml --drop Bryce   # …and the same field minus a candidate
```

`cycle_resolution_report.py` is what makes the [cycle-resolution](../RCV_Ranked_Robin/cycle_resolution.md) and [Split Cycle](../topics/condorcet/split_cycle.md) pages runnable rather than asserted: it prints the pairwise margins, the Smith set, and every cycle-resolution rule's winner *set*, tagged by [Fishburn class](../topics/condorcet/condorcet_reading_list.md). The `--drop` flag re-runs the same ballots with a candidate removed, which is how a spoiler or IIA failure gets demonstrated. It's a *report*, not a guard — there's no LH result to compare against.

The pytest **skips cleanly** if `pref_voting` isn't installed, so it never blocks the core suite. Declared as the `crosscheck` optional-dependency extra in the engine's `pyproject.toml` (`pip install -e .[crosscheck]`).

## Other independent calculators (quick hand-checks)

For a fast manual second opinion on a *ranked* example, Rob LeGrand's [**ranked-ballot voting calculator**](https://www.cs.angelo.edu/~rlegrand/rbvote/calc.html) computes the winners under many ranked methods (Condorcet variants, Borda, Hare/IRV, Coombs, Bucklin…). Handily, it takes the **same `count:A>B>C` ballot syntax** our RCV-IRV YAMLs use — so you can paste a file's ballots straight in. It also ships ready-made teaching inputs (the Tennessee example, a "Hare jumps to extremes" center squeeze, and a Hitler/Washington/Stalin case). Use it as a sanity check, not an automated guard — the `pref_voting` cross-check above is the gate.

## Mining `pref_voting` for new teaching scenarios (balance-aware)

`pref_voting` ships profile **generators** (`generate_profiles`, spatial models) and axiom checkers (monotonicity, no-show, etc.) that can *find* fresh paradox cases automatically — a great source for the [paradoxes & whoops gallery](../../method_comparisons/paradoxes_and_whoops/).

**House rule when mining:** respect the gallery's [balance ledger](../../method_comparisons/paradoxes_and_whoops/README.md#balance-ledger). The generators make IRV failures especially easy to surface — so deliberately search for cases that embarrass the **score family (STAR/Approval)** and **Condorcet/Ranked Robin** too, not just IRV. A mismatch the cross-check ever flags is itself a candidate teaching case (and a bug report): investigate before adding.
