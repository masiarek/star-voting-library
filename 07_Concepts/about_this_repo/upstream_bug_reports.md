# Upstream bug reports — what we've filed, and what we're waiting on

This repo finds bugs. Building teaching cases means running the same election through several engines and comparing, which is a fairly good bug detector — and when the engines disagree, one of them is usually wrong. Those findings get filed upstream, and then they get forgotten, because the page that motivated the report goes on to say something else.

This is the follow-up list: every report **we** filed against a project we don't own, what it was, and where it stands. It is not a list of every upstream issue this repo cites — only the ones we opened and are waiting on.

**Before adding a row:** if the finding is a *missing guard* in BetterVoting (a validation that isn't there, a state that can't be reached through the UI), it goes to Arend first, privately, before it goes on any page. That rule lives in the `bettervoting-qa` README and it outranks the convenience of this table.

---

## BetterVoting — [Equal-Vote/bettervoting](https://github.com/Equal-Vote/bettervoting/issues)

| Issue | Filed | State | What it is |
|---|---|---|---|
| [#1582](https://github.com/Equal-Vote/bettervoting/issues/1582) | 2026-08-20 | open | Multi-winner races export only the **final** seat's `tieBreakType` / `tied` — `runBlocTabulator` (`Util.ts:312–316`) copies them from the last seat, so a random draw that decided seat 1 of a Bloc STAR / Approval / Plurality / Ranked Robin race reports `none`; the per-seat values survive in `roundResults`. Confirmed on production `/API/Sandbox` for all four methods and on three live Bloc STAR elections (`9ff9jk`, `dkj9dx`, `484mbm`); for STAR and Ranked Robin the elected *set* can turn on the unflagged draw. Third `tieBreakType` sibling after #1507 (over-reports) and its IRV comment (under-reports). **2026-08-21 — correction posted:** the issue's closing note said our own engine had the mirror of this and was *"queued for a fix on our side"*; it was in fact already fixed, in [`85c5d3b`](https://github.com/masiarek/star-voting-library/commit/85c5d3b00f664f8497ff91b639bc5978b96ee61f), before the issue was filed — the note was written from a stale checkout. [The comment](https://github.com/Equal-Vote/bettervoting/issues/1582#issuecomment-5373487772) says so, describes the shape our fix took (the tiebreaker logs its own calls and the result builder reads that log, so a reported tie is read off the object that broke it), and declines the clean bill of health: rungs *below* the lot inside a bloc/PR round stay invisible |
| [#1525](https://github.com/Equal-Vote/bettervoting/issues/1525) | 2026-08-15 | open | A table filtered to zero rows renders the *new-user* empty state, so a search that matches nothing reports the account as empty — on `/manage`, complete with a CREATE ELECTION button. It masks every search shortcoming as data loss, which is how it was found: an admin searching by election ID ([#1059](https://github.com/Equal-Vote/bettervoting/issues/1059), our PR [#1524](https://github.com/Equal-Vote/bettervoting/pull/1524)) was told they had no elections. Cases and prototypes: [bettervoting-qa BV2285](https://masiarek.github.io/bettervoting-qa/test_cases/BV2285-index.html) |
| [#1513](https://github.com/Equal-Vote/bettervoting/issues/1513) | 2026-08-14 | open | **Add Voters** keys its duplicate check on `email` alone, so in admin-managed-voter-ID mode every row collides on `""`: any list of 2+ rows is reported as duplicate emails and answering Yes adds one voter, discarding the rest silently. Found in the screen recording attached to [#1512](https://github.com/Equal-Vote/bettervoting/issues/1512) (someone else's issue, about scrolling). Test plan and a draft help page: [bettervoting-qa BV250](https://masiarek.github.io/bettervoting-qa/test_cases/BV250-post-fix-verification.html) |
| [#1508](https://github.com/Equal-Vote/bettervoting/issues/1508) | 2026-08-09 | open | A ballot scoring every candidate the same (`5,5`) is dropped from the STAR tally as an abstention, so its scores never reach the totals. Minimal case, [BV2283 `hb4qvv`](https://bettervoting.com/hb4qvv/results); supersedes the diagnosis in #1478 |
| [#1507](https://github.com/Equal-Vote/bettervoting/issues/1507) | 2026-08-09 | open | STAR-PR results always report `tieBreakType: "random"`, even with no tie — the mislabel that hid the count-vs-weight divergence for a year (and heads every STAR-PR results page "Tied!"). Fix written and parked behind the PR freeze (`fix/1507-star-pr-tiebreaktype`, [bettervoting-qa PARKED §7](https://github.com/masiarek/bettervoting-qa/blob/master/docs_proposals/PARKED_ready_for_bv.md)). 2026-08-20: [comment added](https://github.com/Equal-Vote/bettervoting/issues/1507#issuecomment-5369326181) with the mirror-image gap in `IRV.ts` — an elimination tie among three or more standing candidates is broken (previous rounds, then the shuffle) with `tieBreakType` left `none`, even when the shuffle picked the winner; cross-referenced to [#1432](https://github.com/Equal-Vote/bettervoting/issues/1432). When #1507 closes, re-check the IRV half separately |
| [#1469](https://github.com/Equal-Vote/bettervoting/issues/1469) | 2026-08-01 | open | Ranked Robin never runs the method's own tiebreakers: a tie among 3+ candidates skips both published degrees and goes straight to the random rung, so the winner tracks the candidate listing order. With three candidates and no drawn matchups *every* Condorcet cycle is such a tie. **A fix is written, tested and parked** behind the PR freeze — and asking the same question of our own engine found the mirror-image bug in it, which changed the winner on 11 of this repo's 100 RR cases ([degrees of ties](../../05_Ranked_Robin/03_Criteria/rr_tiebreaks/degrees_of_ties.md)) |
| [#1468](https://github.com/Equal-Vote/bettervoting/issues/1468) | 2026-08-01 | open | Ranked Robin's chart stars the wrong candidate when a Copeland tie is broken by the head-to-head runoff — the header names the winner, the chart stars whoever sorts first |
| [#1488](https://github.com/Equal-Vote/bettervoting/issues/1488) | 2026-08-06 | open | Bloc STAR ballot never says the count repeats — a multi-seat ballot explains only the first seat |
| [#1487](https://github.com/Equal-Vote/bettervoting/issues/1487) | 2026-08-06 | open | Range-of-Scores chart and the page headline use different denominators on flat ballots |
| [#1486](https://github.com/Equal-Vote/bettervoting/issues/1486) | 2026-08-06 | open | Bulk ballot upload needs a defined ballot format — the parser #810 plans to reuse is rank-only and takes the method from the filename |
| [#1485](https://github.com/Equal-Vote/bettervoting/issues/1485) | 2026-08-06 | open | Record the abstention policy on the race, so an export says what was *allowed* |
| [#1484](https://github.com/Equal-Vote/bettervoting/issues/1484) | 2026-08-06 | open | STAR Race Details tables use the second-highest scorer instead of the tiebreak runner-up |
| [#1480](https://github.com/Equal-Vote/bettervoting/issues/1480) | 2026-08-04 | closed | Winner highlighting is positional — the star and the gold row mark the first rows of `summaryData.candidates`, not `elected`, so a runoff-broken Copeland tie decorates a candidate that did not win (live: [`8h4bvh`](https://bettervoting.com/8h4bvh/results)). Closed 2026-08-20 as by-design (the frontend trusts the backend's order by convention) — which relocates the defect rather than resolving it: every other tabulator delivers a winners-first order and Ranked Robin doesn't, so the display on `8h4bvh` is still wrong and [BV2270's caveat](../../05_Ranked_Robin/03_Criteria/rr_tiebreaks/bv2270_8h4bvh_head_to_head_vs_margin.md) stands. A one-line backend fix is parked in bettervoting-qa's frozen queue; a reply offering the reframe (reopen or a backend-scoped ticket) is with Arend |
| [#1478](https://github.com/Equal-Vote/bettervoting/issues/1478) | 2026-08-04 | open | A partial ballot whose marks are all equal is dropped from the tally as an abstention — re-test once the #1470 fix deploys; same root cause if those ballots reach the tabulator as missing keys |
| [#1471](https://github.com/Equal-Vote/bettervoting/issues/1471) | 2026-08-03 | open | Results bar chart: percentage labels and the majority marker use different denominators |
| [#1470](https://github.com/Equal-Vote/bettervoting/issues/1470) | 2026-08-03 | open | Approving a write-in silently discards ballots that scored every official candidate equally — and can change the winner (live: [`43jp39`](https://bettervoting.com/43jp39/results), 3 ballots tallied out of 7). **A fix is written, tested and parked** behind the PR freeze — [bettervoting-qa write-up](https://masiarek.github.io/bettervoting-qa/issues/1470-writein-abstention-discards-ballots.html) |
| [#1456](https://github.com/Equal-Vote/bettervoting/issues/1456) | 2026-07-26 | open | Results page: unify "Equal Support" vs "no preference" wording |
| [#1444](https://github.com/Equal-Vote/bettervoting/issues/1444) | 2026-07-17 | open | Summary bar view — the results bars may need a clarifying report |
| [#1434](https://github.com/Equal-Vote/bettervoting/issues/1434) | 2026-07-13 | open | Elections created via the API can't manage their write-ins |
| [#1432](https://github.com/Equal-Vote/bettervoting/issues/1432) | 2026-07-11 | open | Surface tie-break explanations in the results UI and the JSON/CSV export (split from #1379) |
| [#1421](https://github.com/Equal-Vote/bettervoting/issues/1421) | 2026-07-05 | **closed** | When "None of the Above" wins a race it is seated with no special handling — intended? **Answered 2026-08-19, not-planned: yes, by design.** Arend: if NOTA wins, next steps are "up to the bylaws of the organization running the election … out of scope for the BetterVoting site." That is a design stance, not a defect, and it has a teaching consequence we now state on the page — a NOTA option is only meaningful if the convening body has written down what a NOTA win *does*, because the platform will simply seat it. Recorded on [the case](../../01_STAR/03_Criteria/none_of_the_above/bv215_26khr3_nota_wins.md) |
| [#1420](https://github.com/Equal-Vote/bettervoting/issues/1420) | 2026-07-05 | open | Download JSON export leaks the tabulator's internal object shape |
| [#1417](https://github.com/Equal-Vote/bettervoting/issues/1417) | 2026-07-04 | **closed** | STAR random tie-break yielded a non-reproducible winner |
| [#1407](https://github.com/Equal-Vote/bettervoting/issues/1407) | 2026-06-28 | open | Reconciling the pets election between the LH and BV reports |
| [#1379](https://github.com/Equal-Vote/bettervoting/issues/1379) | 2026-05-23 | **closed** | BV555 — STAR scoring round, three-way tie. **Closed 2026-08-16, not-planned, at our own request:** BV's protocol deliberately skips head-to-head once 3+ candidates are tied, so the divergence from LH is working-as-intended on BV's side, and our reference output predated that protocol update. Nothing to retire — [tiebreak_ladders](../tabulation_engines/tiebreak_ladders.md) and [tie_breaking](../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md) already document it as deliberate. The surviving transparency ask lives on in **[#1432](https://github.com/Equal-Vote/bettervoting/issues/1432)** (open), which is tracked separately above |
| [#1090](https://github.com/Equal-Vote/bettervoting/issues/1090) | 2025-11-13 | open | Equal Opposition (0-score) mislabeled as "Abstained" in the UI and the export |
| [#1086](https://github.com/Equal-Vote/bettervoting/issues/1086) | 2025-11-12 | open | UI says "STAR Voting" instead of "Bloc STAR", with the wrong help link |
| [#1063](https://github.com/Equal-Vote/bettervoting/issues/1063) | 2025-11-02 | open | Implement deterministic tie-breaking using candidate lot numbers |
| [#1052](https://github.com/Equal-Vote/bettervoting/issues/1052) | 2025-10-30 | open | "No ballots have been cast" shown when ballots exist |
| [#904](https://github.com/Equal-Vote/bettervoting/issues/904) | 2025-04-11 | open | Method naming — STAR / STAR Bloc / STAR PR |
| [#894](https://github.com/Equal-Vote/bettervoting/issues/894) | 2025-04-04 | **closed** | Deactivated selection in the Plurality CSV download |
| [#778](https://github.com/Equal-Vote/bettervoting/issues/778) | 2025-02-09 | open | YAML file standard |

## starvote — [larryhastings/starvote](https://github.com/larryhastings/starvote/issues)

Larry's engine, which this repo forks. Fork-side findings and their local fixes are written up in [`FORK_NOTES.md`](../../STARVote_LH_tabulation_engine/FORK_NOTES.md) and [the engine's README](../tabulation_engines/LH_starvote/README.md).

| Issue | Filed | State | What it is |
|---|---|---|---|
| [#20](https://github.com/larryhastings/starvote/issues/20) | 2026-08-09 | open | Allocated Score fills the quota by ballot COUNT, not weight — diverges from the reference implementation the package ships (fixed in this fork; [the divergence page](../../03_STAR_PR/03_Criteria/allocated_count_vs_weight/README.md)) |
| [#19](https://github.com/larryhastings/starvote/issues/19) | 2026-08-09 | open | SSS silently discards ballots that scored the winner 0, whenever any ballot exhausts in the same round |
| [#18](https://github.com/larryhastings/starvote/issues/18) | 2026-08-04 | open | `UnbreakableTieError` message never interpolated (missing `f` prefix in `_star_round()`) |
| [#17](https://github.com/larryhastings/starvote/issues/17) | 2026-06-17 | open | SSS returns different winners depending on `verbosity` — the one that changed results |

## prefsampling — [COMSOC-Community/prefsampling](https://github.com/COMSOC-Community/prefsampling/issues)

The profile generators behind `pref_voting`'s `generate_profile`, so a defect here reaches this repo through the [cross-check engine](../tabulation_engines/cross_checking_with_pref_voting.md).

| Issue | Filed | State | What it is |
|---|---|---|---|
| [#6](https://github.com/COMSOC-Community/prefsampling/issues/6) | 2026-08-22 | open | Seeding the Euclidean samplers degenerates them, silently. `GAUSSIAN_BALL` returns **one point repeated** `num_points` times (the seed is pinned inside `inner_sampler_args`; `ball_resampling`'s outer loop advances it only on a *rejected* draw, and although that fires for ~31% of seeds, the advanced seed **persists** into later iterations, so every point after the first accepted one is a deterministic re-draw of it — identical points with probability 1); separately, `sample_election_positions` passes the same seed to both position calls, so **candidates land exactly on the first voters** — on 4 of 6 spaces at unequal counts, and on **all six without exception** when `num_voters == num_candidates`. Per-side seed arguments are clobbered, so there is no caller-side workaround short of abandoning the named spaces for a sampler of your own. Unseeded calls are fine, which inverts the usual expectation that seeding only fixes the stream. Found because 20,000 seeded spatial elections reported a suspiciously clean **0.00% Condorcet cycles** in every cell — every voter lands on one point and the candidates collapse onto that same point, so every distance is zero, all ballots tie, and the count falls back to index order. Correct rates are 0.15–1.25%: [how often does each Condorcet method tie?](../topics/ties/how_often_condorcet_methods_tie.md). Reader-facing lesson: [the six Euclidean spaces](../topics/euclidean_spaces.md); full mechanism + probe: [the companion QA repo's writeup](https://masiarek.github.io/bettervoting-qa/analysis/prefsampling-seeding/index.html) |

## pref_voting — [voting-tools/pref_voting](https://github.com/voting-tools/pref_voting/issues)

| Issue | Filed | State | What it is |
|---|---|---|---|
| [#186](https://github.com/voting-tools/pref_voting/issues/186) | 2026-08-22 | open | Downstream half of prefsampling [#6](https://github.com/COMSOC-Community/prefsampling/issues/6): `generate_profile(probmodel="euclidean", seed=…)` inherits both degeneracies. `space="gaussian_ball"` returns **the same profile for every seed** (300 seeds → 1 profile); `uniform_cube` / `gaussian_cube` / `unbounded_gaussian` put candidate *j* on voter *j* (200/200); the default `uniform_ball` escapes **unless** `num_voters == num_candidates`, when every space collides. `generate_spatial_profile` uses global `np.random` and is unaffected. Measured reproduction of every number: [the companion QA repo's writeup](https://masiarek.github.io/bettervoting-qa/analysis/prefsampling-seeding/index.html) |

## GitHub Pages

| Report | Filed | State | What it is |
|---|---|---|---|
| [community #204454](https://github.com/orgs/community/discussions/204454) | 2026-08-09 | open | Pages serves `.yaml` as `text/yaml` with no `charset`, so browsers mis-decode every non-ASCII character. Background and our workaround: [`website_build.md`](website_build.md) |

---

## Refreshing this page

States go stale silently — nobody emails us when an issue closes. To re-check every row at once:

```bash
for r in "Equal-Vote/bettervoting 1582 1525 1513 1508 1507 1488 1487 1486 1485 1484 1480 1478 1471 1470 1469 1468 1456 1444 1434 1432 1421 1420 1417 1407 1379 1090 1086 1063 1052 904 894 778" "larryhastings/starvote 20 19 18 17" "COMSOC-Community/prefsampling 6" "voting-tools/pref_voting 186"; do set -- $r; repo=$1; shift; for n in "$@"; do curl -s "https://api.github.com/repos/$repo/issues/$n" | python3 -c "import json,sys; d=json.load(sys.stdin); print(f\"{d['state']:8} $repo#{d['number']}  {d['title'][:70]}\")"; done; done
```

The GitHub Pages one is a discussion, not an issue, so it isn't in that loop — open it and look.

**When one closes:** don't just flip the word. Check whether the fix changes anything this repo *teaches* — a page that documents the old behavior, a case whose expected winner depended on it, a workaround that can now be retired. That is the whole reason for tracking these, and it's the step that gets skipped.
