# RCVis (rcvis.com) — the visualizer, not another counter

**Level: reference · deep dive**

**One line:** [rcvis.com](https://www.rcvis.com/) draws ranked-choice results as Sankey diagrams, bar charts and round tables — and it is the only tool on this shelf that **does no counting at all**, which is exactly what makes it useful to a library that already has counting covered.

→ the certified counter that feeds it: [RCTab](rctab.md) · the other visualizer, which *does* count: [RCV Lab](rcv_lab.md) · the shelf: [tabulation engines](README.md).

---

## What it is

RCVis is a free, open-source web service that takes a **finished** [RCV-IRV](../../06_Other/RCV_IRV/README.md) or STV result and turns it into something an audience can read: an interactive bar chart across rounds, a **Sankey diagram** of where each eliminated candidate's votes went, a round-by-round table, and a single summary table that exports as Wikipedia markup. Output can be embedded in a page over the oEmbed protocol, and print-friendly variants exist for newsrooms.

It is built and run by **Armin Samii** ([artoonie](https://github.com/artoonie/rcvis)), previously a visualization lead at Argo AI. The site describes itself as *"free, open-source, and nonpartisan"*, says it has been used *"by millions of voters in the United States and abroad"* for election-night reporting, and lists publication in the Washington Post, Gothamist, Ballotpedia, NBC New York and Fox 5 NY.

**Disclose the lean, per house practice.** RCVis is RCV-branded and RCV-shaped: it draws instant-runoff and STV rounds and nothing else. There is no STAR view, no score view, no pairwise view. Its author's stated motivation is that the main obstacle to RCV adoption is that people don't understand it — a reform-advocacy premise, openly held. None of that touches the drawing, which is faithful to whatever numbers you hand it, but it does mean RCVis will never render the comparison this library exists to make. Take the *pictures*, not the framing. <!-- terminology-ok: RCV-branded names the product's own scope -->

## The distinction that matters: it does not tabulate

This is the whole point of the page, and it is easy to get backwards because RCVis is where a lot of people first *see* an RCV count.

Every other entry on this shelf answers the question *"who won?"* — the [LH engine](LH_starvote/README.md), [BetterVoting](bettervoting_and_the_engine.md), [`pref_voting`](cross_checking_with_pref_voting.md), the vendored [`pyrankvote`](../../06_Other/RCV_IRV/RCV_IRV_tabulation_engine/README.md), [RCTab](rctab.md), and [RCV Lab](rcv_lab.md). RCVis answers a different one: *"what did the count look like?"* It ingests a results summary that some **other** engine produced and renders it. Its own documentation points at RCTab as the certified software that *"creates results summary files which RCVis can then visualize."*

So RCVis is **not a cross-check**. Feeding it our numbers and getting a pretty Sankey back confirms nothing about whether the numbers are right — it is a rendering of our own claim, not an independent witness. That is a genuinely different relationship from every other tool documented here, and worth stating plainly before anyone cites a RCVis chart as corroboration.

What it *is* good for is the thing our text reports structurally cannot show. Our engine prints rounds as columns of numbers, and a column of numbers cannot show a reader where a transferred vote came **from** — which is precisely the subject of every page in this library that argues about [center squeeze](../../06_Other/RCV_IRV/concepts/RCV_IRV_center_squeeze.md) or [exhausted ballots](../../06_Other/RCV_IRV/concepts/RCV_IRV_exhausted_ballots.md).

## What it accepts

Imports are listed as RankedVote.co, RankedChoices.com, RCV123.org, Opavote, ElectionBuddy, Dominion, RCTab, and cast vote record files. ES&S support is named as a future priority rather than a current feature.

Nearly all of those are **tabulated summaries**, not ballots — which follows from the previous section. The parsing is factored out into a separate project, [`rcvformats`](https://github.com/artoonie/rcvformats), and that project's design tells you what the real target format is: every supported input is normalized to **Universal RCV Tabulator JSON** — the format RCTab writes, under RCTab's former name.

There is an API (`POST` to `/api/visualizations/` with a `jsonFile`, or `/api/bp/` with a `resultsSummaryFile`), but it needs an account plus an access request by email to the maintainers, and is rate-limited to 1,000 requests/hour. That gate is why nothing here is automated against it.

## The bridge from this repo

This library can already produce exactly what RCVis eats, and it does not need a new converter to do it.

[`rctab_convert.py`](../../STARVote_LH_tabulation_engine/tools_adam/rctab_tabulation_engine/README.md) turns a ranked case YAML into RCTab's CSV + config; [`rctab_crosscheck.py`](../../STARVote_LH_tabulation_engine/tools_adam/rctab_tabulation_engine/README.md) runs RCTab over them and parses the `*_detailed_report.json` it writes. That JSON **is** Universal RCV Tabulator JSON. So the path is:

```
ranked YAML → rctab_convert.py → RCTab → *_detailed_report.json → RCVis
```

with no format work in the middle. The cost is that it drags a JVM through the pipeline for a drawing, which is why this is documented rather than wired: the [RCTab page](rctab.md) already notes that its runner is *a report, not a guard*, for the same reason.

The lighter alternative is to emit the JSON ourselves from our own round data and skip RCTab entirely — which is worth knowing is possible, and has one sharp edge.

## The trap: an eliminated candidate must leave the table

Our RCV-IRV report keeps eliminated candidates in every later round at zero:

```text title="Abridged for the lesson — not verbatim engine output"
ROUND 2
Ranked Pairs         324  Hopeful
Schulze Method       321  Hopeful
Minimax              262  Rejected
Copeland's Rule        0  Rejected   ← eliminated in round 1, still listed
Flip a Coin            0  Rejected   ← eliminated in round 1, still listed
```

The Universal RCV Tabulator schema **rejects that shape**. Running our published rounds for the [cycle sample](rcv_lab.md) through `rcvformats`' own validator, both ways:

| Round data shaped as… | `rcvformats` verdict |
|---|---|
| our report prints it — eliminated candidates kept at `0` | ❌ **INVALID** |
| eliminated candidates dropped from later tallies | ✅ **VALID** |

with the validator's exact complaint:

```text
Found Copeland's Rule in Round 2, though they were already eliminated.
After a candidate is eliminated, they should be removed from all future vote tallies.
```

Both renderings are defensible — ours keeps the column headers stable down the report, theirs treats a round's tally as the set of candidates still standing — but a converter that passes our rows through unchanged produces a file RCVis will refuse. This is the same class of gotcha as [RCTab's "a rank is not a score"](rctab.md#the-trap-a-rank-is-not-a-score): the two formats look alike and disagree about something quiet.

*(Verified 2026-08-08 against `rcvformats` from PyPI, schema `universaltabulator`, using the round tallies published on the [RCV Lab page](rcv_lab.md). No account and no upload were involved — the check is purely against the format library.)*

## `rcvformats` is the piece we could actually borrow

Worth separating from the visualizer, because the licences differ and the difference decides what we may do:

| Project | Licence | Can this MIT repo vendor it? |
|---|---|---|
| [`artoonie/rcvis`](https://github.com/artoonie/rcvis) — the site | **GPL-3.0** | ❌ no — strong copyleft, incompatible with shipping inside an MIT repo |
| [`artoonie/rcvformats`](https://github.com/artoonie/rcvformats) — the parsers | **MIT** | ✅ yes — same licence as this repo, and it is on PyPI |

So the rule is: **use the hosted site for pictures; depend on `rcvformats` if we ever need the formats.** `pip install rcvformats` gives readers and validators for Universal RCV Tabulator JSON, Opavote JSON, ElectionBuddy CSV, and three Dominion flavours — which makes it a reasonable companion to this library's notes on [ballot interchange formats](../scores_and_ranks/abif_format.md), and a safer thing to lean on than writing another Dominion parser.

**Correction to the old note.** [`LINKS.md`](../LINKS.md) previously described RCVis as *"strong-copyleft (AGPL-style)"*. It is plain **GPL-3.0** — verified in the repository's own `LICENSE` header. The practical advice was right and is unchanged (don't vendor it here), but the reasoning differs: GPL-3 has no network-use clause, so operating a modified copy as a web service would not by itself trigger source release the way AGPL would. That entry now points here.

## How it sits against the other tools

Rows are tools, columns are what each one actually does:

| Tool | Counts? | Draws? | Ranked | Scored / STAR | Licence | Our use |
|---|:--:|:--:|:--:|:--:|---|---|
| **[LH `starvote`](LH_starvote/README.md)** (this repo) | ✅ | text only | ✅ | ✅ | MIT / upstream | the main engine |
| **[BetterVoting](bettervoting_and_the_engine.md)** | ✅ | ✅ | ✅ | ✅ | open | live elections + frozen exports |
| **[`pref_voting`](cross_checking_with_pref_voting.md)** | ✅ | ✗ | ✅ | ✅ | MIT | the neutral referee |
| **[RCTab](rctab.md)** | ✅ | ✗ | ✅ | ✗ | MPL-2.0 | the *certified* witness |
| **[RCV Lab](rcv_lab.md)** | ✅ | ✅ Sankey | ✅ | ✗ | service (beta) | downloadable real CVRs |
| **RCVis** (this page) | ❌ | ✅ Sankey | ✅ | ✗ | GPL-3.0 | pictures only |

Two entries in that table draw Sankey diagrams, and they are not interchangeable. **RCV Lab** counts the ballots itself, so you hand it ballots and it gives you both a tally and a picture — and its tally is a genuine independent leg for our RCV-IRV cases, which is why it has [its own page and a verified reproduction](rcv_lab.md). **RCVis** counts nothing, so you must already have a result; in exchange it will render a result produced by the *certified* tabulator, which RCV Lab's own engine is not. Pick by what you're short of: a second opinion, or a picture of the opinion you have.

## Verdict

**Real, well-established, and deliberately narrow.** RCVis is the best-known RCV results visualizer in the US, it is honest about being a visualizer, and its format library is MIT and genuinely reusable. Cite it for **presentation**, never for **corroboration** — a Sankey of our own numbers is our own numbers in colour. Nothing here is wired up, and the API gate (account + emailed access request) is the reason; the format half of the bridge is verified and recorded above so that anyone who wants the pictures starts from a known-good shape rather than from a rejected upload.

---

*Up: [tabulation engines](README.md) · [07_Concepts](../README.md) · related: [RCTab](rctab.md) · [RCV Lab](rcv_lab.md) · [external links](../LINKS.md).*
