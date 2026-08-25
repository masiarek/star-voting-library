---
tags:
  - simulation
---

# A reproduction command nobody runs — what auditing vse-sim turned up

*The Center for Election Science's [`vse-sim`](https://github.com/electionscience/vse-sim) publishes a guide telling you how to regenerate the data behind its charts. The command in that guide does not run, and has not run since two minutes after it was written. This page records the finding, the evidence, the two-line fix, and — because the failure mode is not specific to that project — the same audit run against this repo.*

**Level: reference · deep dive** Companion: [vse-sim, read from source](../topics/vse_sim.md) (what the simulator actually assumes) · [Upstream bug reports](upstream_bug_reports.md) (the follow-up list for things we file).

---

## Why we were looking

A VSE-under-increasing-strategy chart circulated in a reform Slack in August 2026. Reading it needed the things a chart cannot show — which electorate, how many candidates, what "a strategic voter" does, how good their polls are — and all of that is public, so the plan was simply to look it up and, where possible, re-run it. Reading the source worked, and produced [its own page](../topics/vse_sim.md). Re-running it did not.

## What we found

`docs/chart-reproduction.md` is the repo's advertised path to the published data, linked from the front page:

```bash
uv run python scripts/generate_published_results.py --elections 15000 --output artifacts/published-results
```

Run against a clean clone at `ef44ce4` (upstream `main` HEAD), with the election count dropped to 2 for speed:

```
Using CPython 3.14.2
Creating virtual environment at: .venv
      Built vse-sim @ file:///…/vse-sim
Installed 17 packages in 172ms
Traceback (most recent call last):
  File ".../scripts/generate_published_results.py", line 15, in <module>
    from debugDump import setDebug
ModuleNotFoundError: No module named 'debugDump'
EXIT CODE: 1
```

The script's first two imports name modules that no longer exist:

```python
from debugDump import setDebug
from vse import CsvBatch, KSModel, allSystems, fuzzyMediaFor
```

Nothing rescues them. There is no `vse.py`, no `debugDump.py`, no shim, no `.pth`, no `conftest.py` anywhere in the tree; `pyproject.toml` packages only `src/`, which contains `vse_sim` alone. The script's own `sys.path.insert(0, parents[1])` adds the **repo root**, which holds no importable module — it is vestigial, left from the layout that existed when the line was written.

## How it happened: a two-minute window

The interesting part is that this was never a slow rot.

| Commit | Time (2026-07-14) | What it did |
|---|---|---|
| `d999795` | 19:50 UTC | Created the script **and** the reproduction guide — while a root `vse.py` still existed. The script worked. |
| `f77a30f` | 19:52 UTC | "Modernize package and move to Python 3.14" — introduced `src/vse_sim/`, retired the root modules, and did not touch the script. |

Two minutes. And the script has not been edited since; upstream HEAD is `ef44ce4` (2026-07-17).

## Why nothing caught it

`.github/workflows/python-app.yml` runs `uv run python -m pytest --doctest-modules`, and `testpaths = ["src/vse_sim", "tests"]`. **`scripts/` is never collected.** CI has been green throughout, correctly, because it is not looking at the file. The sibling script `scripts/recalculate_irv_pages.py` and the whole test suite import `vse_sim.*`; these two lines are the only stale references left in the repository.

## What is *not* wrong

Worth stating plainly, because "the VSE simulator is broken" would be a false headline:

- **The library is fine.** `src/vse_sim/` imports cleanly, the tests pass, the doctests run.
- **The published charts are not in question.** They were generated before the refactor, from a script that worked at the time.
- **A bare `python3 scripts/…` was never supported** — the imports resolve because `uv run` installs the project into the environment. The documented invocation is the right one; it is the script that drifted.

This is one file, missed by one commit, in a place CI structurally cannot see.

## The fix, verified

Two lines, because `simulation.py` re-exports `KSModel` and `fuzzyMediaFor` in its `__all__`:

```python
from vse_sim.diagnostics import setDebug
from vse_sim.simulation import CsvBatch, KSModel, allSystems, fuzzyMediaFor
```

Applied to a copy outside the clone and run end-to-end: **exit 0 in about a second**, printing the output filename, producing a valid 67 KB CSV whose first line records model, methods, seed, media, `nvot`, `ncand` and `niter` exactly as the guide promises. `CsvBatch.__init__`'s signature matches the script's call, and nothing else fails past the import line. The `sys.path.insert` can go too, as dead weight.

That form also matches the sibling script's own style, which already imports `fuzzyMediaFor` from `vse_sim.simulation`.

## Not a duplicate

All 13 open issues on the repo are older feature trackers (multi-winner, SODA, graph colours); there are no open pull requests; searching issues and PRs in every state for "import" and for "generate_published_results" returns nothing related. The script's only commit ever is its creation.

## Why it matters for this library

This repo quotes VSE. Not as decoration — the ordering *STAR ≳ Approval > RCV-IRV > Plurality* appears on [what makes a good winner](../topics/what_makes_a_good_winner.md), and the standing caveat that [every such number is conditional on its model](../topics/election_simulation_models.md) is one of the load-bearing honesty commitments here. That caveat is only worth something if the model can be inspected — and inspection has two levels:

- **Read the settings.** Still possible, and now written down: hierarchical-cluster `KSModel`, **40 voters, 6 candidates**, 15,000 elections, polls fuzzed by one standard deviation, an "Approval" line the code itself calls `IdealApproval`, and a STAR line on a 0–10 rather than the real-world 0–5 ballot. Those are not trivia; each one is a place a published ordering could move.
- **Re-run them.** Not possible from the documented path until this lands. Which is the difference between a reproducible artifact and a well-documented one.

## The same audit, on ourselves

The transferable lesson is uncomfortable enough to be worth testing here rather than only saying: **a reproduction command that no test executes is not a reproduction command.** So the same question was asked of this repo — which of our tool scripts are named in Markdown as things a reader should run, while no test imports or executes them?

**Twenty scripts**, including ones named on many pages: `create_bv_test_election.py` (20 pages), `bv_replay_tiebreak.py` (10), `bv_ballot_sheet.py` (8), `fetch_bv_export.py` (7). Every one of them was probed by resolving every top-level module it imports — the exact failure mode above.

**All twenty resolve.** Two were flagged on the first pass and both are false alarms on inspection: `create_bv_test_election.py` wraps `jwt` / `cryptography` in a `try` that exits with an instruction to use `uv run`, and `bv_result_screenshot.py` declares `websockets` in a **PEP 723** inline `# /// script` header — both are correct by design, run the documented way. The probe was resolving against `.venv` rather than the per-script environment.

So: clean, this time, and by luck as much as design — nothing in the suite would have told us otherwise. The gap that bit vse-sim is open here too.

## Status

**Found, verified, not filed.** Filing is an outward-facing action and the decision is Adam's; if it goes upstream, it gets a row in [upstream bug reports](upstream_bug_reports.md), which tracks only reports we actually opened.

## Provenance of this finding

Written down per the house rule that a claim-check discloses its own sourcing. The first pass read the script's imports and the packaging config and *inferred* the failure — a static argument that could have been wrong in several ways (a shim, a path hack, an editable install). The confirmation was done independently by a second model, which cloned, installed, ran the documented command, captured the traceback verbatim, applied the proposed fix to a copy and ran that too, and recovered the commit timeline that turned "it drifted" into "it broke two minutes after it was written." The dates, the CI explanation, and the fact that the fix is two lines rather than four all come from that pass, not the first one.
