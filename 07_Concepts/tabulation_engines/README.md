# Tabulation engines — who counts the votes, and how we know they're right

Every claim in this library is backed by a runnable election, and every election is counted by a real engine. This section documents the engines and — just as importantly — how they check each other.

## The engines

- **[LH `starvote`](LH_starvote/README.md)** — the main engine: Larry Hastings' STAR tabulator, vendored as a lightly-documented fork, plus this repo's reporting wrapper. Start here; [reading a STAR report](LH_starvote/reading_a_star_report.md) decodes the output line by line.
- **[BetterVoting](BV/README.md)** — the Equal Vote Coalition's live election platform. Real elections are imported from it and re-tabulated independently, turning them into regression cases.
- **[RCV-IRV](RCV_IRV/README.md)** — the vendored `pyrankvote` engine that counts ranked ballots (IRV/STV), so ranked-vs-scored comparisons run on a real implementation of each side.

## The cross-checks

- **[BetterVoting and the LH engine — one election, two reports](bettervoting_and_the_engine.md)** — why the two independent implementations agree on winners, and the one bookkeeping detail where their reports can differ.
- **[Cross-checking with `pref_voting`](cross_checking_with_pref_voting.md)** — Eric Pacuit's peer-reviewed social-choice library as an outside referee for the Condorcet / RCV-IRV / Plurality machinery.

*Up: [07_Concepts](../README.md) · the vendored fork's own ledger: [LH_ENGINE_CHANGES.md](../../STARVote_LH_tabulation_engine/LH_ENGINE_CHANGES.md).*
