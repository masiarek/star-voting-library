# BV — BetterVoting (the live web app)

[BetterVoting.com](https://bettervoting.com) is the web app voters use to run a real STAR election (help & FAQ: [docs.bettervoting.com](https://docs.bettervoting.com)). Its result is the **visual** report — the Scoring Round / Automatic Runoff charts and the Race Details tables.

**Start here if a results page is confusing you:** [How to read a BetterVoting results page](reading_a_bv_results_page.md) — the four decks (headline, round charts, Race Details, Stats for Nerds), panel by panel, with the denominator each one uses named out loud. It's the BV counterpart to [reading a STAR report](../LH_starvote/reading_a_star_report.md).

**Start here if a downloaded `_bv_export.json` is confusing you:** [The BetterVoting JSON export — field-by-field](bv_json_export_format.md) — every key in `Election` / `Ballots` / `Results`, checked against the 211 frozen exports in this repo; the `score`-means-rank trap, the `null`-vs-`0` distinction, which fields a mint can populate, and the open issue to clean the format up.

**Live result for the worked pets example:** [bettervoting.com/pet/results](https://bettervoting.com/pet/results) — the interactive version of the screenshots used throughout these pages (toggle the bar/pie views there; the **percent ↔ raw-counts** flip on the bar view is walked through, on the five-voter lunch election, in [Reading the Runoff Percentages](../../../01_STAR/01_Learn/the_count/runoff_percentages.md#percent-or-raw-counts-the-toggle)).

For the worked pets example, BetterVoting's own screenshots live in `01_STAR/01_Learn/img/` — `pets_rounds_bars.png`, `pets_rounds_pie.png`, `pets_race_details_tables.png` — and are walked through in the overview, [BetterVoting and the LH Engine — One Election, Two Reports](../bettervoting_and_the_engine.md), and in [Reading the Runoff Percentages — Two Denominators, One Winner](../../../01_STAR/01_Learn/the_count/runoff_percentages.md).

The matching **text** report — the same election counted by Larry Hastings' `starvote` engine — is in [reading a STAR report](../LH_starvote/reading_a_star_report.md). Same election, same winner, two reports.

**Creating BV elections via the API** (for test cases): the [`create_bv_test_election.py` tool guide](../../../STARVote_LH_tabulation_engine/tools_adam/create_bv_test_election.md) (purpose + how to run), and the platform notes on [what works and the one thing that doesn't](bv_api_election_creation_notes.md) (API-created elections are public and listable but not UI-administrable).

**Website / UI testing backlog:** [BV website TO-DO](BV_website_TODO.md) — hands-on tasks to test or learn on the live app (e.g. entering **district** data to BV-back the summability demo).

**Start here if you're wondering whether an election was a "demo":** [BetterVoting's six voter-authentication modes](bv_voter_authentication_modes.md) — there is no demo flag; it's derived from three settings, only one of the six modes is genuinely unlimited, and the mode decides whether turnout, quorum and delivery reporting exist at all.

**Deeper BV internals** (reference docs, moved here from the repo root):
- [**bv_json_export_format.md**](bv_json_export_format.md) — the export's field-by-field reference (and the direction back: what a mint can actually set).
- [**bv_voter_authentication_modes.md**](bv_voter_authentication_modes.md) — the six canonical `{voter_access, voter_authentication, invitation}` shapes, and what each one lets a report claim.
- [**tabulation_engine/**](tabulation_engine/README.md) — notes on BV's own tabulator (`RankedRobin.ts` etc.), running it locally, and contributing changes.
- [**database_schema/**](database_schema/README.md) — BV's data model: ballot / election / election-roll / email-events tables.
