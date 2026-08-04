# Handoff — the `.starvote` format page and the 484mbm tie case

*Written 2026-08-04 before a machine change. Everything described here is **pushed**; nothing is left in a scratch directory. Two commits: [`e36e159`](https://github.com/masiarek/star-voting-library/commit/e36e159) (the page) and [`2eb4abd`](https://github.com/masiarek/star-voting-library/commit/2eb4abd) (the case + BV comparison).*

## What was asked, and what shipped

Document Larry Hastings' `.starvote` ballot file format — format, how you run it, what comes out — as an education page, and put the worked example on BetterVoting.

- **[The `.starvote` ballot file format](../07_Concepts/tabulation_engines/LH_starvote/starvote_file_format.md)** — the format spec read off the parser (sections, assignments, list mode, the `n ballots:` pragma, all seven `[options]` keys), the three front doors and their *differing* tiebreak defaults, the worked example with its full report, and the BV comparison. Linked from the LH engine README.
- **[Bloc STAR — a three-way tie no rung can break](../02_STAR_Bloc/02_Examples/b484mbm_tie_every_rung.md)** — the two-view case: `484mbm` on BetterVoting, screenshot, BV's round logs, the LH report with BV's draw pinned. Indexed in `02_STAR_Bloc/README.md`.

Every number on both pages was produced by running the engine, not transcribed. `regen_all.py` has been run, hygiene is clean on everything these commits touch, and the suite was green (1001 passed) before the push.

## The thing to know first: BV2263 names two elections

**`484mbm`'s permanent BetterVoting title reads "BV2263 — …" and that is wrong.** BV2263 belongs to the over-50% control (`xw23m9`), minted concurrently that afternoon. BV titles cannot be edited or deleted, so this is not fixable — it is documented instead, in three places: the case page's warning admonition, the YAML's header comment, and `TIE_EVERY_RUNG_BLOC_SPEC`'s note in `bv_election_specs.py`.

**The case is therefore filed by bvid** (`b484mbm_tie_every_rung`, no `bv_test_id`), per the repo's own rule for cases with no pre-assigned Test ID. BV2263 stays with `xw23m9` in the registry. Quote `484mbm`; ignore the number on the election.

**How it happened, because the gate is supposed to prevent exactly this.** `_minted_test_ids()` reads two sources: committed `bv_test_id:` fields, and the `_demo_dropbox` ledger that every mint writes at mint time. The dropbox is the one that catches a *concurrent, uncommitted* mint — and it was unreachable, because the working copy lives on T7 and T7 was unmounted, so the session ran from a GitHub tarball in a scratch directory. The gate passed on committed data alone and handed out a number another session was already using.

**If you mint from a tarball again, the gate is blind by construction.** Either mount T7, or treat the printed "next free" as advisory and confirm against the master sheet before minting.

## What the case actually found

Worth keeping because both are about BV's *reporting*, not its arithmetic:

1. **BV skips the pairwise rung when more than two candidates are tied** (`pairwise_too_many_candidates`) and drops straight to five-star, then to a seeded draw. The LH engine computes that rung and reports it tied 3–3–3. Here the shortcut costs nothing because the rung was tied anyway — but on ballots where pairwise *would* separate three tied candidates, the two engines part ways. Not verified whether such a profile exists; that is the obvious follow-up.
2. **A lot-decided seat is invisible in the summary.** Round 0 carries `tieBreakType: "random"` and a recorded `perm`, but top-level `tieBreakType` is `"none"` and `tied` is `[]`. The public page shows a flat 12/12/12 then a two-way runoff, with nothing saying the finalists were drawn. Same gap as BV130-r2, now reproducible in three ballots — a good minimal repro if it is ever filed.

## Loose ends

- **Not filed on the BV tracker.** Finding 2 is a reproduction of known behaviour (BV130-r2, #1063, #1417); finding 1 looks new. Neither has an issue. `484mbm` is a ready-made repro for both.
- **Only one screenshot.** `img/484mbm_result.png` is seat 1. The `race-details` preset of `bv_result_screenshot.py` fails on multi-winner Bloc results (`selector not found: #shotTarget`) — the paginated per-seat layout has no `Table` heading for it to anchor on. Seat 2 and the details table are missing; the preset probably needs a Bloc branch.
- **The engine bug found on the way** — both `UnbreakableTieError` strings in `_star_round()` missing their `f` prefix — was fixed and reported upstream as [larryhastings/starvote#18](https://github.com/larryhastings/starvote/issues/18) in a parallel session. Already on master; the page's errata section reflects the fix.
- **Three malformed `**Level:**` tags** in `02_STAR_Bloc/03_Criteria/` (`committee_spoiler`, `participation`, `seat_order`) fail hygiene on master. They came from the concurrent Bloc-criteria work, not from this thread, and were left alone to avoid a conflict. Two are a stray trailing period inside the bold; `seat_order` is missing its audience token.

## Reproducing the worked example

The `.starvote` file is on the page. There is no committed copy — it is four lines of `[options]` and nine of ballots, and the point is that you can type it. Upstream's CLI is the only door that runs it:

```bash
python -m starvote path/to/bloc_three_way.starvote
```

The repo wrapper takes `.yaml` only, which is why the case file exists in parallel.
