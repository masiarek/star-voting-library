# BV — BetterVoting (the live web app)

[BetterVoting.com](https://bettervoting.com) is the web app voters use to run a real STAR election (help & FAQ: [docs.bettervoting.com](https://docs.bettervoting.com)). Its result is the **visual** report — the Scoring Round / Automatic Runoff charts and the Race Details tables.

**Live result for the worked pets example:** [bettervoting.com/pet/results](https://bettervoting.com/pet/results) — the interactive version of the screenshots used throughout these pages (toggle the bar/pie views there).

For the worked pets example, BetterVoting's own screenshots live in [`../../STAR_Voting/img/`](../../STAR_Voting/img) — `pets_rounds_bars.png`, `pets_rounds_pie.png`, `pets_race_details_tables.png` — and are walked through in the overview, [BetterVoting and the LH Engine — One Election, Two Reports](../bettervoting_and_the_engine.md), and in [Reading the Runoff Percentages — Two Denominators, One Winner](../../STAR_Voting/the_count/runoff_percentages.md).

The matching **text** report — the same election counted by Larry Hastings' `starvote` engine — is in [reading a STAR report](../LH_starvote/reading_a_star_report.md). Same election, same winner, two reports.

**Creating BV elections via the API** (for test cases): the [`create_bv_test_election.py` tool guide](../../../STARVote_LH_tabulation_engine/tools_adam/create_bv_test_election.md) (purpose + how to run), and the platform notes on [what works and the one thing that doesn't](bv_api_election_creation_notes.md) (API-created elections are public and listable but not UI-administrable).

**Website / UI testing backlog:** [BV website TO-DO](BV_website_TODO.md) — hands-on tasks to test or learn on the live app (e.g. entering **district** data to BV-back the summability demo).

**Deeper BV internals** (reference docs, moved here from the repo root):
- [**tabulation_engine/**](tabulation_engine/README.md) — notes on BV's own tabulator (`RankedRobin.ts` etc.), running it locally, and contributing changes.
- [**database_schema/**](database_schema/README.md) — BV's data model: ballot / election / election-roll / email-events tables.
