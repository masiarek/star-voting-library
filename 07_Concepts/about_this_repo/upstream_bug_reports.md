# Upstream bug reports — what we've filed, and what we're waiting on

This repo finds bugs. Building teaching cases means running the same election through several engines and comparing, which is a fairly good bug detector — and when the engines disagree, one of them is usually wrong. Those findings get filed upstream, and then they get forgotten, because the page that motivated the report goes on to say something else.

This is the follow-up list: every report **we** filed against a project we don't own, what it was, and where it stands. It is not a list of every upstream issue this repo cites — only the ones we opened and are waiting on.

**Before adding a row:** if the finding is a *missing guard* in BetterVoting (a validation that isn't there, a state that can't be reached through the UI), it goes to Arend first, privately, before it goes on any page. That rule lives in the `bettervoting-qa` README and it outranks the convenience of this table.

---

## BetterVoting — [Equal-Vote/bettervoting](https://github.com/Equal-Vote/bettervoting/issues)

| Issue | Filed | State | What it is |
|---|---|---|---|
| [#1508](https://github.com/Equal-Vote/bettervoting/issues/1508) | 2026-08-09 | open | A ballot scoring every candidate the same (`5,5`) is dropped from the STAR tally as an abstention, so its scores never reach the totals. Minimal case, [BV2283 `hb4qvv`](https://bettervoting.com/hb4qvv/results); supersedes the diagnosis in #1478 |
| [#1507](https://github.com/Equal-Vote/bettervoting/issues/1507) | 2026-08-09 | open | STAR-PR results always report `tieBreakType: "random"`, even with no tie — the mislabel that hid the count-vs-weight divergence for a year |
| [#1487](https://github.com/Equal-Vote/bettervoting/issues/1487) | 2026-08-06 | open | Range-of-Scores chart and the page headline use different denominators on flat ballots |
| [#1485](https://github.com/Equal-Vote/bettervoting/issues/1485) | 2026-08-06 | open | Record the abstention policy on the race, so an export says what was *allowed* |
| [#1484](https://github.com/Equal-Vote/bettervoting/issues/1484) | 2026-08-06 | open | STAR Race Details tables use the second-highest scorer instead of the tiebreak runner-up |
| [#1478](https://github.com/Equal-Vote/bettervoting/issues/1478) | 2026-08-04 | open | A partial ballot whose marks are all equal is dropped from the tally as an abstention |
| [#1417](https://github.com/Equal-Vote/bettervoting/issues/1417) | 2026-07-04 | **closed** | STAR random tie-break yielded a non-reproducible winner |
| [#1407](https://github.com/Equal-Vote/bettervoting/issues/1407) | 2026-06-28 | open | Reconciling the pets election between the LH and BV reports |
| [#1379](https://github.com/Equal-Vote/bettervoting/issues/1379) | 2026-05-23 | open | BV555 — STAR scoring round, three-way tie |
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

## GitHub Pages

| Report | Filed | State | What it is |
|---|---|---|---|
| [community #204454](https://github.com/orgs/community/discussions/204454) | 2026-08-09 | open | Pages serves `.yaml` as `text/yaml` with no `charset`, so browsers mis-decode every non-ASCII character. Background and our workaround: [`website_build.md`](website_build.md) |

---

## Refreshing this page

States go stale silently — nobody emails us when an issue closes. To re-check every row at once:

```bash
for r in "Equal-Vote/bettervoting 1508 1507 1487 1485 1484 1478 1417 1407 1379 1090 1086 1063 1052 904 894 778" "larryhastings/starvote 20 19 18 17"; do set -- $r; repo=$1; shift; for n in "$@"; do curl -s "https://api.github.com/repos/$repo/issues/$n" | python3 -c "import json,sys; d=json.load(sys.stdin); print(f\"{d['state']:8} $repo#{d['number']}  {d['title'][:70]}\")"; done; done
```

The GitHub Pages one is a discussion, not an issue, so it isn't in that loop — open it and look.

**When one closes:** don't just flip the word. Check whether the fix changes anything this repo *teaches* — a page that documents the old behavior, a case whose expected winner depended on it, a workaround that can now be retired. That is the whole reason for tracking these, and it's the step that gets skipped.
