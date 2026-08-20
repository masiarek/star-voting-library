# Tabulation engines — who counts the votes, and how we know they're right

Every claim in this library is backed by a runnable election, and every election is counted by a real engine. This section documents the engines and — just as importantly — how they check each other.

## The engines

- **[LH `starvote`](LH_starvote/README.md)** — the main engine: Larry Hastings' STAR tabulator, vendored as a lightly-documented fork, plus this repo's reporting wrapper. Start here; [reading a STAR report](LH_starvote/reading_a_star_report.md) decodes the output line by line.
- **[BetterVoting](BV/README.md)** — the Equal Vote Coalition's live election platform. Real elections are imported from it and re-tabulated independently, turning them into regression cases.
- **[RCV-IRV](RCV_IRV/README.md)** — the vendored `pyrankvote` engine that counts ranked ballots (IRV/STV), so ranked-vs-scored comparisons run on a real implementation of each side.

## For implementers

- **[The result contract — running your own engine against this library](result_schema.md)** — the one page here addressed to somebody writing a *different* tabulator. `--json` counts any case file into a versioned JSON object (winners, rounds, pairwise matrix, and which tie-break rung fired), so checking a second implementation is a `diff` instead of a reading exercise. Includes what a pass means, the five places correct implementations legitimately differ, and an honest list of what the suite does not yet cover.

## The cross-checks

- **[BetterVoting and the LH engine — one election, two reports](bettervoting_and_the_engine.md)** — why the two independent implementations agree on winners, and the one bookkeeping detail where their reports can differ.
- **[Cross-checking with `pref_voting`](cross_checking_with_pref_voting.md)** — Eric Pacuit's peer-reviewed social-choice library as an outside referee for the Condorcet / RCV-IRV / Plurality machinery.

## Outside engines and data

- **[RCV Lab (rcv-lab.org)](rcv_lab.md)** — a free RCV platform that publishes its sample elections as downloadable cast vote records, including three full-size real elections with their rules files. Its "Best Cycle-Breaking Rule" sample is [reproduced and re-counted here](../../method_comparisons/cycle_resolution/README.md), matching round for round. It also counts in the other direction: [all 64 of our RCV-IRV cases run through its engine](rcv_lab_irv_crosscheck.md), 63 agreeing outright and the 64th exposing a silent tie in one of our own cases.
- **[RCTab — the certified tabulator that counts real elections](rctab.md)** — the federally-tested engine actual US jurisdictions run on election night for RCV-IRV and STV. Wired up: our ranked cases convert to its CSV and run through it, and on the tie cases it agrees on every winner while being anonymous where our engine isn't.
- **[RCVis (rcvis.com)](rcvis.md)** — the best-known US ranked-choice results *visualizer*: Sankey diagrams, round bars, Wikipedia-ready tables. The one entry on this shelf that does **no counting** — it renders a result some other engine produced, so it is a presentation tool and never a cross-check. Its format library `rcvformats` is MIT and reusable; the site itself is GPL-3.0.

## Not built — what a real-election STAR tabulator would take

- **[The STAR reference package](star_reference_package.md)** — **start here.** Six documents that would make STAR the cheapest new method a vendor or nonprofit could add: a clause-numbered specification, rule-space coverage, the conformance suite published for implementers, a logic-and-accuracy deck, a model VVSG 2.0 implementation statement, and the CVR mapping. Scoped so that one person can finish it and nobody's approval is required.
- **[What would it take to certify STAR Voting software?](certifying_star_software.md)** — the landscape, from primary sources. The EAC sets **no** method-specific requirements and tests a system against the manufacturer's own implementation statement; a nonprofit's open-source RCV tabulator has already been lab-tested and state-approved; and the EAC's own explanation of why a precinct tabulator cannot count RCV alone is [summability](../topics/summability/README.md) stated as a certification constraint — with STAR on the other side of it.
- **[What paper ballots would mean for the LH engine](paper_ballots_in_lh.md)** — the counterpart scoped *down* rather than up: not a certified state tabulator but a co-op board or club AGM running a **hybrid** vote, some members online and some on paper. Eight requirements that follow from one demotion (the YAML stops being the election and becomes a transcript of one), what they'd cost in the file format, and the two that no tabulator can satisfy — a single marked roll across both channels, and a close time. **Design sketch; nothing implemented.**
- **[A Rust tabulation kernel — goals and requirements](rust_kernel_requirements.md)** — the decision document: what such a kernel would be *for* (a menu of nine candidate goals, from in-browser counting to publishing encrypted ballots), the requirements each goal implies, and the preparation that is worth doing in Python whether or not any Rust is ever written. **Draft; nothing decided.**
- **[A Rust tabulation kernel — scope](rust_kernel_scope.md)** — the companion: which methods a kernel would cover (91% of the library's cases in seven methods), what stays in Python permanently, the honest case against building it at all, and the porting hazards that would actually cost time.

*Up: [07_Concepts](../README.md) · the vendored fork's own ledger: [LH_ENGINE_CHANGES.md](../../STARVote_LH_tabulation_engine/LH_ENGINE_CHANGES.md).*
