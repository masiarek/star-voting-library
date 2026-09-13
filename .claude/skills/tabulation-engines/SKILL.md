---
name: tabulation-engines
description: Reference for this repo's tabulation engines — how the LH engine dispatches each voting method and multi-winner variant, the Ranked Robin triple-check and its published tiebreak ladder, what BetterVoting's seeded-shuffle tiebreak records and why a lot-decided winner stays LH-only, the Minimax, Coombs, successive-elimination and grade-method tools, abcvoting, the 0–5 score cap, and the engine's error messages. Load before tabulating or cross-checking a case, or writing about how a count or a tiebreak works.
---

# The tabulation engines

*Migrated out of `CLAUDE.md` on 2026-09-12 so it loads on demand instead of in every session. The rules below are unchanged.*

- `STARVote_LH_tabulation_engine/starvote_larry_hastings.py` — STAR + Bloc/
  proportional; reporting options; `blocs:` vote-splitting check; quorum;
  `[Divergence from STAR]` comparison; optional `show_runoff_percent` runoff
  summary line (decided-voters denominator; forced on in `_tabulated`).
  Auto-dispatches to RCV-IRV / Approval / **Ranked Robin** by `voting_method`, or
  to RCV-IRV when ballots contain ranked `>` (comments with `->` are ignored).
  **Ranked Robin (RCV-RR / Copeland)** is first-class: `voting_method: RankedRobin`
  (aliases `RCV_RR` / `Copeland` / `Consensus`) prints the round-robin report
  (ballots + pairwise table + win-loss record), flags a Condorcet cycle, and
  writes its `_tabulated` mirror — it does **not** fall through to the IRV rounds.
  **Bloc RR (multi-winner):** `num_winners > 1` now elects the **top-N by the
  same ladder as single-winner RR** (Copeland → 1st Degree → 2nd Degree → lot),
  printing a seats list and flagging a lot-decided
  last seat — it no longer silently downgrades to one winner. **Multi-winner
  Plurality = SNTV / Bloc Plurality** (`run_plurality_multi`): `Plurality` +
  `num_winners > 1` elects the top-N by first-choice count (ties → lot);
  single-winner Plurality prints its own choose-one report (`run_plurality_single`
  — it no longer falls through to the STAR path). So LH multi-winner
  coverage is now complete for BV's bloc set: STAR→**Bloc STAR**,
  Approval→**Approval_Multi_Winner**, RankedRobin→**Bloc RR**, Plurality→**SNTV**,
  plus STV and STAR_PR/allocated/sss/rrv. (The old "LH has no Plurality" caveat is
  retired — single-winner via `run_plurality_single`, multi-winner via SNTV.
  The full tie-break ladders, per method and per engine, are written down in
  `07_Concepts/tabulation_engines/tiebreak_ladders.md`.)
  **RR triple-check — always cross-verify a Ranked Robin case three ways:** this
  native tally, BetterVoting's `RankedRobin.ts` (the frozen `_bv_export.json`
  Results), and **`pref_voting`'s independent Copeland** via
  `tools_adam/pref_voting_tabulation_engine/ranked_robin_report.py` (declared in
  `pyproject.toml`; `uv sync` then `uv run …`). The `pref_voting` leg is the
  **third-party cross-check** — a library nobody here wrote — and it is the one that
  makes an RR result trustworthy rather than self-confirming, so **run it on every
  RR case, not just the awkward ones**. On a tie it reports the whole Copeland
  **leader set** and declines to pick, then tells you whether LH's winner sits
  inside that set (`CONSISTENT ✓`) — which is exactly the check you want, since the
  disagreement between engines is never about the tally, only about the tiebreak.

  **Tiebreak ladder — the method publishes one, and follow it (corrected 2026-08-19).**
  Ranked Robin's own protocol (electowiki, *Degrees of ties*) resolves a Copeland tie
  by the **1st Degree** — each tied finalist's sum of win margins **over the other
  finalists** — and only then by the **2nd Degree**, margins **over all candidates**.
  It defines a 3rd and 4th Degree but explicitly does not recommend them for public
  elections, preferring a lot. LH now implements exactly that: Copeland → 1st Degree
  → 2nd Degree → **lot** (`lot_numbers`, published in the YAML). **Two things this
  ordering makes true, both of which were got wrong for two years:** with exactly two
  finalists the 1st Degree *is* their head-to-head, so **BV's head-to-head rung was
  right and LH's total-margin rung was not** — the "LH vs BV rung 2 divergence"
  documented across this repo was our bug, and correcting it changed the winner on
  **11 of 100** RR cases, every one a two-way tie whose head-to-head was decisive;
  and BV, which has no rung at all for 3+ tied candidates, sends every
  three-candidate cycle straight to its shuffle (filed as bettervoting#1469, fix
  written, parked behind the PR freeze). The remaining genuine divergence is only the
  last rung: LH's published lot vs BV's seeded shuffle. Full account, with the two
  discriminating cases:
  `05_Ranked_Robin/03_Criteria/rr_tiebreaks/degrees_of_ties.md`. The engine's win-loss
  table prints a **"vs finalists"** column whenever there is a tie for the lead — that
  column is the 1st Degree, and it is what makes the winner checkable by hand.

  **BV's JSON export records the tie-breaking SEQUENCE just fine — don't repeat the
  old "can't be frozen" claim** (corrected 2026-07-29). BV's rung 3 is labelled
  `"random"` but is a **seeded shuffle**, documented as deliberately deterministic in
  `shuffleCandidatesForRandomTiebreak.ts`: `seed = (rawVoteCount + hash(raceId)) >>> 0`,
  shuffled once by TinyRand, each candidate's index written back as `tieBreakOrder`.
  The export publishes the **complete order** — `perm` (ids in tiebreak order),
  per-candidate `tieBreakOrder`, `tied[]` and `other[]` sorted by it, `tieBreakType`,
  and a `logs` line — so winner **and** runners-up survive, and a re-tally reproduces
  them. Pin `lot_numbers:` to BV's `perm` and LH replays the draw exactly. Verified
  live at 3 candidates (**BV2261** `y2fbpc`) and 9 (**BV2262** `2gvwr9`, all nine
  positions matched). Replay the shuffle yourself with
  `tools_adam/bv_replay_tiebreak.py <frozen export>` (stdlib-only Python port).
  **The real limit is narrower:** BV's order is *recorded* but not *derivable* — a
  function of the ballot **count** and the race id, **never of how anyone voted** —
  so a case whose **winner** turns on it is still **LH-only** (only LH's published
  lot lets a reader derive the result from the file). Publishing such a case on BV is
  fine when the *recording mechanism* is the subject and the page says to ignore who
  won. Worked: `05_Ranked_Robin/01_Learn/rr_tiebreak_lh_vs_bv.md`,
  `05_Ranked_Robin/03_Criteria/rr_tiebreaks/bv2261_…md` / `bv2262_…md`.
- **Minimax and Coombs are tabulable** (added 2026-08-07) —
  `tools_adam/pref_voting_tabulation_engine/minimax_report.py` and
  `coombs_report.py`, each cross-checked against `pref_voting` on every run.
  Neither method exists in the LH engine or on BetterVoting, which is why
  Felsenthal's §A7 and §A10 examples were prose for so long; all 18 are now
  runnable case files in `method_comparisons/felsenthal_paradoxes/cases/`.
  Two things to know before quoting a Minimax result: **"worst loss" has three
  published readings** (winning votes = Felsenthal's, margins = `pref_voting`'s,
  pairwise opposition), which agree on an odd electorate with no drawn pairs and
  need not otherwise; and **a truncated ballot's unstated pair is a convention,
  not arithmetic** — this repo counts it for neither candidate, Felsenthal splits
  it ½–½ (`--equal-prob`), and Example 31's winner changes with the choice. Say
  which convention a number came from.
- **Successive elimination and the grade methods are tabulable too** (added
  2026-08-07) — `successive_elimination_report.py` (the parliamentary agenda
  procedure) and `grade_methods_report.py` (Range = mean, Majority Judgment =
  median + Balinski–Laraki), completing Felsenthal's five uncountable
  procedures. Two things that are easy to get wrong: **successive elimination
  takes the agenda as an argument**, not a default — under a cycle the
  agenda-setter picks the winner, so `--agenda` is required and a tied round is
  broken by an explicitly-chosen `--tiebreak` (the published examples disagree:
  alphabetical in Ex.11/12, "random" in Ex.10). And **grade cases are not LH
  election files**: Felsenthal's 1–10 and A–J scales fit neither the engine's
  0–5 validation nor BetterVoting, so they carry a `grades:` block instead of
  `ballots:` — which keeps them invisible to `check_top_level_keys` and
  `check_descriptions` (both gate on `ballots`) and means no `_tabulated`
  mirror and no generated page. Their counts live on the concept pages.
  Rescaling to 0–5 to make them engine-runnable would change the published
  numbers, which is why it wasn't done. **A grade file's scale may be words**
  (`grade_scale: "To Reject|Poor|Acceptable|Good|Very Good|Excellent"`), which is
  what Majority Judgment actually asks for — B&L's claim is not "six levels" but
  a shared *common language*, so the method's own front door
  (`06_Other/Majority_Judgment/`) uses it and its ballots are drawn. **Two
  published tie-breaks, not one:** this tool implements the *iterative* rule
  (strip a shared median, recompute, repeat); `pref_voting` implements the
  **majority gauge** (share above the median vs share below), and on a profile
  where both tied candidates have more detractors than supporters at the median
  the gauge as implemented compares only the losing shares and returns a **tie**
  where the iteration separates them — an observed DISAGREE, not a bug in either.
  Say which reading a number came from.
- `06_Other/RCV_IRV/RCV_IRV_tabulation_engine/rcv_irv_tabulation.py` — vendored pyrankvote; reads
  ranked (`A>C>B`) or score ballots.
- `06_Other/abcvoting_tabulation_engine/abc_tabulation.py` — multi-winner Approval (ABC)
  rules via Martin Lackner's `abcvoting` (in the `dev` dependency group since
  2026-08, so `uv sync` brings it in and the cross-check actually runs — locally
  and in CI). `av` doubles as an independent cross-check of the LH bloc-Approval
  count; `seqpav` / `pav` / `seqphragmen` add the proportional rules the LH
  engine doesn't have. Tested by `tests/test_abcvoting_crosscheck.py` (still
  guards on the import for bare-pip environments).
- **Score / range voting & the 0–5 cap (don't misstate this).** Larry's underlying
  `starvote` engine is *range-parametric*: `starvote.election(starvote.star, rows,
  maximum_score=N)` tabulates any range (verified at 0–10 → C). The **0–5 limit is the
  fork's teaching guardrail, NOT an engine limit** — `validate_star_rows(…,
  max_score=5)` in `starvote_larry_hastings.py` (def ~L2239, called with `max_score=5`
  ~L2366) rejects scores >5 on the YAML-CLI path because STAR ballots are 0–5 by
  convention; it's a single adjustable arg. **Pure Score / Range IS tabulable** — via
  `pref_voting.grade_methods` (`score_voting` = mean, `greatest_median` = the median
  variant, plus `star` / `approval` / `majority_judgement`), `starvote`'s RRV
  (`Reweighted_Range_Voting`, range-based PR), and the sim/divergence tools
  (`06_Other/simulations/star_vs_approval_divergence.py`, `tools_adam/find_divergence.py`)
  which compute the score-total winner. The STAR **Scoring Round** output is itself the
  score tally (the Score-Voting winner = whoever leads the scoring round before the
  runoff). What's absent is only a first-class `voting_method: Score` on the teaching
  CLI — **capability is not the blocker.**
- Quick checks can use system `python3` (engines are vendored); the user runs via
  their `.venv` / `uv`.
- The engine errors *clearly* (no tracebacks) for the common mistakes: bad YAML,
  no `ballots:` block / old nested schema (prints the key-components template),
  wrong column counts, invalid chars / out-of-range scores, ranked ballots under a
  score method, and method/seats mismatches. Missing `voting_method` / `num_winners`
  is a non-fatal NOTE (defaults to STAR / 1). Generated `_tabulated.txt` files are
  refused as input.
