# LH engine — consolidated changelog (methods, reports, fixes)

**The one canonical index of everything this repo adds to or changes in the LH tabulator.** Everything below is either (a) a tiny, deliberate edit to the vendored upstream algorithm, or (b) our presentation/analysis **wrapper** and helper engines built on top. If you only read one page about "what's ours vs Larry's," read this.

Scope note — three related docs feed this one; this page is the union:

- [`FORK_NOTES.md`](FORK_NOTES.md) — the *upstream* `starvote/` package baseline (tag `starvote-upstream-2.1.6`) and the handful of edits inside it.
- [`README_larry_hastings.md`](README_larry_hastings.md) — the wrapper's display options + a running display change log.
- [`../07_Concepts/tabulation_engines/LH_starvote/README.md`](../07_Concepts/tabulation_engines/LH_starvote/README.md) — the narrative "what we added" overview.

**The golden rule (unchanged):** the voting *algorithm* stays pristine. Larry Hastings' `starvote` core is edited almost never (see §1); every method dispatch, report, and fix below the STAR core lives in our wrapper `starvote_larry_hastings.py` or a separate vendored/cross-check engine. Full credit for STAR/Bloc/PR tabulation belongs upstream.

---

## 1. Edits to the vendored upstream algorithm (`starvote/`) — kept minimal

The vendored `starvote 2.1.6` package is ~97% character-identical to PyPI (the rest is line-reflow). Only seven functional edits exist — two output toggles and five bug fixes; all are candidates to offer upstream:

| Change | Where | Note |
|--------|-------|------|
| `print_averages` toggle (default off) + CLI `-a` / config `print averages` | `starvote/__init__.py` | Suppresses the averages line unless asked. |
| `print_maximum_score` toggle (default off) + CLI `-M` / config `print maximum score` | `starvote/__init__.py` | Suppresses the "Maximum score is …" line. |
| **Five-star tiebreak default-score fix** (`ballot_get(candidate1, 1)` → `…, 0`) | `starvote/__init__.py`, `_maximum_score_count_round()` 2-candidate fast path | Latent correctness bug: a ballot omitting candidate1 contributed a phantom score of 1. Dormant for 0–5 STAR; now agrees with the general path. Guard: `01_STAR/03_Criteria/tie_break_dead_rung/`. |
| **SSS verbosity fix** — ballot allocation dedented out of `if options.verbosity:` | `starvote/__init__.py`, `sequentially_spent_score()` "Ballot allocation round" | Real correctness bug (upstream [issue #17](https://github.com/larryhastings/starvote/issues/17), still open): at the default `verbosity=0` no ballots were ever spent/reweighted, so SSS degenerated into repeated bloc score voting and returned different winners than verbose runs. Only the printing stays guarded now. Details: [BUG_sss_verbosity.md](BUG_sss_verbosity.md). Guard: `tests/test_verbosity_invariance.py`. |
| **SSS zero-score-ballot fix** — the remaining-ballots append dedented out of `if score:` | `starvote/__init__.py`, `sequentially_spent_score()` "Ballot allocation round" | Real correctness bug (upstream [issue #19](https://github.com/larryhastings/starvote/issues/19), filed 2026-08-09): in any round where a supporter exhausts (raw 5, no surplus), every ballot that scored the winner 0 was silently removed with its full unspent budget — a vote-unitarity violation that flips the committee on ~1.4% of tie-free impartial-culture 2-seat profiles. Interacts with the SSS verbosity fix above: upstream only manifests it at `verbosity>=1`; the #17 dedent promoted it to every run until found. All 5 repo SSS cases verified byte-identical (no case ever exhausts a ballot). Details: [BUG_sss_zero_score_ballots.md](BUG_sss_zero_score_ballots.md). Guard: `tests/test_sss_zero_score_ballots.py`. |
| **Allocated Score count-vs-weight fix** — the allocation round's overfill test, quota subtraction, and surplus factor switched from the score group's row count to its weight sum (`allocation_weight`) | `starvote/__init__.py`, `allocated_score_voting()` "Ballot allocation round" | Real correctness bug (upstream [issue #20](https://github.com/larryhastings/starvote/issues/20), filed 2026-08-09): the quota was charged one full ballot per row regardless of remaining fractional weight, so a bloc holding 3+ quotas paid a geometrically shrinking price per seat (D'Hondt-flavored) instead of a full quota — on the 41/19/6 fingerprint it elected 4-1-0 where BetterVoting production and the reference implementation `starvote` itself ships both elect 3-1-1. Two repo cases flipped to the correct committee with the fix (`coop_board_scores_allocated`, `bv2130`). Round-1 output stays byte-identical; later rounds add a `remaining weight` line when weight ≠ count. Details: [BUG_allocated_count_vs_weight.md](BUG_allocated_count_vs_weight.md). Guard: `tests/test_allocated_weight_accounting.py`. Teaching page: [the count-vs-weight divergence](../03_STAR_PR/03_Criteria/allocated_count_vs_weight/README.md). |
| **Unbreakable-tie message fix** (`"{int_to_words(…)}…"` → `f"…"`, 2 chars) | `starvote/__init__.py`, `_star_round()` — both `options.break_tie()` calls | Cosmetic, not a winner change (upstream [issue #18](https://github.com/larryhastings/starvote/issues/18), still open): the two `UnbreakableTieError` strings lacked their `f` prefix, so the message read `{int_to_words(len(tie), flowery=False)}-way tie in Scoring Round` instead of `three-way tie…`. `_star_round()` serves STAR *and* Bloc STAR, so both raised it; `allocated_score_voting()` / `sequentially_spent_score()` already had the prefix. Printed reports were never affected — API callers only. Errata: [`.starvote` file format](../07_Concepts/tabulation_engines/LH_starvote/starvote_file_format.md#errata-the-unbreakable-tie-message-leaks-a-placeholder). Guard: `tests/test_unbreakable_tie_message.py`. |

Everything else people call "the LH engine's improvements" is **not** an algorithm edit — it's the wrapper (§2–§4).

## 2. New methods (auto-dispatch on `voting_method`)

The wrapper reads `voting_method` + `num_winners` and routes to the right tabulator, so one command and the same `_tabulated` discipline cover the whole family. Upstream `starvote` natively provides only the STAR-family score methods; the rest are ours or a separate vendored engine.

| Method (`voting_method`) | Winners | Source | Notes / test |
|--------------------------|---------|--------|--------------|
| `STAR` | single | upstream `starvote` | STAR core; we wrap display. `tests/test_single_winner_positive.py` |
| `bloc` / `Bloc STAR` | multi | upstream `starvote` | `tests/test_method_positive.py` |
| `allocated` / `sss` / `rrv` (proportional STAR) | multi | upstream `starvote` | Allocated Score / Sequentially Spent Score / Reweighted Range Voting |
| `STAR_PR` | multi | upstream `starvote` | proportional STAR |
| **`RankedRobin`** (aliases `RCV_RR` / `Copeland` / `Consensus`) | single | **ours** (`run_ranked_robin`) | First-class: round-robin report (ballots + pairwise table + win–loss record), Condorcet-cycle flag; does **not** fall through to IRV. `tests/test_ranked_robin.py` |
| **Bloc RR** (`RankedRobin` + `num_winners > 1`) | multi | **ours** | Top-N by record (wins → margin → lot); flags a lot-decided last seat. No longer downgrades to one winner. `tests/test_ranked_robin.py::test_ranked_robin_bloc_multiwinner` |
| `Approval` (single) | single | **ours** (routes via STAR path) | `tests/test_approval_mirror.py` |
| `Approval` (multi) — Bloc/Block Approval | multi | **ours** + `abcvoting` cross-check | `av` cross-checked; `seqpav`/`pav`/`seqphragmen` via abcvoting engine. `tests/test_abcvoting_crosscheck.py` |
| **`Plurality`** (single) | single | **ours** (routes via STAR path) | Single-winner plurality. |
| **`Plurality` (multi) = SNTV / Bloc Plurality** | multi | **ours** (`run_plurality_multi`) | Top-N by first-choice count (ties → lot). Auto-detects SNTV / Block / Limited. `tests/test_ranked_robin.py::test_plurality_multiwinner_sntv` |
| `IRV` (Hare) / `STV` | single / multi | **vendored `pyrankvote`** (`06_Other/RCV_IRV/…`) | Ranked ballots (`A>B>C`) route here; also auto-detected when ballots contain `>`. |

## 3. New reports & presentation (the wrapper's analysis layer)

All in `starvote_larry_hastings.py`; none touch the algorithm. The on-screen report renders the engine's built-in house defaults (a file's `options:` may still override any of them, and `--full` puts the mirror's everything-on render on screen); the saved **`_tabulated.txt` mirror** always renders every analysis on, stamped with source name + mtimes.

| Report / feature | What it adds | Reference |
|------------------|--------------|-----------|
| **Runoff (Preference) Matrix** | Head-to-head / pairwise grid (`For – Equal Support – Against` per cell) — the summable heart of the count. | `show_matrix` · `matrix_finalists_only` |
| **Round-Robin report** (RR) | Ballots + full pairwise table + Copeland win–loss record + margin tiebreak. | `tests/test_ranked_robin.py` |
| **`No Preference` → `Equal Support`** relabel | Equal Vote Coalition term for the no-preference runoff bucket (wrapper-only; the package still prints "No Preference" internally). | `GLOSSARY.md` |
| **`[Runoff Reversal]` summary** | Plain-English sentence naming *why* the runoff winner beat the score leader when they differ — the runoff elects the finalist preferred by the majority (of voters with a preference). Header renamed 2026-07 from "Majority Preference Enforcement Principle" (the old name overclaimed: STAR fails the formal majority criterion; the real guarantee is conditional, majority preference *between the finalists*). | Runoff-Reversal set |
| **`[Divergence from STAR]`** | Flags when Approval / pure score / RCV-IRV would pick someone else; prints whenever methods disagree. | `build_divergence_index.py` |
| **Self-reconciling runoff line** | `show_runoff_percent`: winner's share of **decided** voters, Equal-Support gap named inline; mirror expands it into a "Runoff math" funnel. | `tests/test_runoff_percent.py` |
| **Score distribution** | Per-candidate star histogram; **Avg** via exact-rational `ROUND_HALF_UP` (not float `/`). | `show_score_counts` · [score distribution](../01_STAR/01_Learn/reporting/score_distribution_and_averages.md) |
| **Condorcet line**, **lot-number tiebreak cascade** | On demand on screen, always in the mirror; tiebreak shown step by step (head-to-head → most 5s → lot). | `show_condorcet` · `tests/test_lot_number_tiebreak.py` |
| **Color palette + round separators** | Distinct colors per phase; auto-off when piped / `NO_COLOR`. | — |
| **`blocs:` vote-splitting check**, **quorum / eligible-voter** accounting | Extra STAR-race diagnostics. | — |
| **House defaults built in** (2026-08-09) | `DEFAULT_OPTIONS` now *is* the house on-screen style: finalists matrix + runoff line on by default (matrix auto-suppressed for multi-winner and two-candidate races); case files carry no `options:` block (501 removed repo-wide, an `options:` override remains legal); new `--full` CLI flag puts the mirror's everything-on render on screen; `show_irv` is vestigial, accepted for parse-compat only. | `DEFAULT_OPTIONS` · `--full` |
| **Multi-winner matrix renders unmarked** (2026-08-09) | The on-screen auto-gate hid the matrix for multi-winner races, but the always-full mirror / `--full` still carried a "Top 2 Finalist" grid from the silent seats=1 STAR analysis — a single-winner concept printed over a Bloc/PR count. Now any multi-winner render of the grid (mirror, `--full`, or a file's `show_matrix: true`) prints plain head-to-head data: retitled "Preference Matrix", no finalist markers or tiebreak note, and an "Informational only — not part of the N-winner count" legend line. 71 mirrors + generated pages regenerated. | `print_matrix(seats=…)` · `tests/test_default_render.py` |

## 4. Input ergonomics & clear errors

- **Tolerant loader:** flat files, a single `election:` wrapper, or a `races:` list; weighted ballots (`42 × 5,4,3,2`); zero-scoring **markers** `-` blank, `~` race abstention, `&` candidate abstention, `?` spoiled, `%` reissued.
- **Equal-rankings in ranked ballots (`A=B>C`)** — RR reads each `>` level split on `=`, so tied candidates share a rank (Equal Support head-to-head). *(See §5 — this was a fix.)*
- **Errors clearly, no tracebacks:** bad YAML, missing `ballots:` block (prints the template), wrong column counts, out-of-range scores, ranked ballots under a score method, method/seats mismatch. Missing `voting_method` / `num_winners` is a non-fatal NOTE. `tests/test_negative_validation.py`
- **Count separator** configurable (`×` / `:` / `x`); all round-trip to valid input. `tests/test_separator_and_errors.py`

## 5. Bug fixes (chronological, newest first)

- **2026-08 — SSS zero-score ballots discarded on exhaustion** (upstream `starvote/`, see §1; upstream [issue #19](https://github.com/larryhastings/starvote/issues/19)). Second SSS defect in the same allocation loop as the verbosity fix: whenever any ballot exhausted, every ballot that scored the round's winner 0 was dropped with its full unspent budget. Found 2026-08-08 by an independent SSS reimplementation during the STAR-PR research sprint; fixed 2026-08-09. No repo case affected. Details: [BUG_sss_zero_score_ballots.md](BUG_sss_zero_score_ballots.md).
- **2026-08 — Unbreakable-tie message placeholder** (upstream `starvote/`, see §1). Exception text only; no winner ever changed.
- **2026-07 — Approval tiebreak now honors `lot_numbers`.** The Approval dispatcher never passed the file's `lot_numbers` into `tabulate_approval` (whose `priority` parameter already existed), so an approval-count tie always fell back to ballot **column order** and a pre-published lot was silently ignored. One-line fix: the dispatcher now passes `priority=election.get("lot_numbers")`. Files without `lot_numbers` are byte-for-byte unchanged (fallback stays column order). Found building Felsenthal Ex.6 (`felsenthal_ex6_pareto_approval.yaml`), which pins an adversarial lot to exhibit Approval electing a Pareto-dominated candidate on a 3–3 tie.
- **2026-07 — Ranked Robin equal-rankings parser.** `run_ranked_robin`'s ranked-ballot reader split only on `>`, so an equal-rank level like `Ava=Bianca=Cedric` was mis-read as a **single phantom candidate** by that literal name — inflating the field and electing the wrong winner. Now each `>` level is split on `=` so tied candidates share a rank (scored Equal Support head-to-head). Strict ballots (all singletons) are byte-for-byte unchanged. Equal ranking is a core Ranked Robin feature, so the engine now reads the weak orders RR is defined on natively (e.g. the [electowiki worked example](https://electowiki.org/wiki/Ranked_Robin) tabulates correctly to Ava, 3 pairwise wins). Guard: `tests/test_ranked_robin.py::test_equal_rankings_are_ties`.
- **2025 — Five-star tiebreak default score** (upstream `starvote/`, see §1).

## 6. Cross-check engines (trust, but verify)

Independent referees confirm the LH picks; not part of the LH engine, but part of the "is it right" story.

- **`pref_voting`** (Eric Pacuit) — independent Condorcet / IRV / Plurality / Copeland referee across the library (currently 0 mismatches). `tools_adam/pref_voting_tabulation_engine/`, `tests/test_pref_voting_crosscheck.py`.
- **`abcvoting`** (Martin Lackner) — multi-winner Approval (`av` cross-check + proportional `seqpav`/`pav`/`seqphragmen`). `06_Other/abcvoting_tabulation_engine/`, `tests/test_abcvoting_crosscheck.py`.
- **BetterVoting** — the frozen `_bv_export.json` Results give a third tally for BV-backed cases. **RR tiebreak caveat:** LH breaks a Copeland tie by margin → lot (deterministic); BV by head-to-head → random, so a tie-deciding RR case is LH-only.

---

*Keep this current: when adding a method, report, or fix, add a row here and link its authoritative doc + test. To see the exact upstream-package diff at any time: `git diff starvote-upstream-2.1.6 -- STARVote_LH_tabulation_engine/starvote/`.*
