---
name: research-topics
description: The private companion repo of research-paper prospectuses (masiarek/star-voting-research-topics) — its fixed page structure, the five-agent adversarial novelty check and how to state a topic's vetting level honestly, and keeping both repos pointing at each other. Load before adding, editing or looking for a research topic.
---

# Research-paper topics (companion repo)

*Migrated out of `CLAUDE.md` on 2026-09-12 so it loads on demand instead of in every session. The rules below are unchanged.*

- **Companion repo — research-paper topics live OUTSIDE this repo.**
  <https://github.com/masiarek/star-voting-research-topics> (**private**) holds the
  vetted research-paper prospectuses that use this library as their reproducibility
  artifact — one `topics/NN_<slug>.md` per topic, plus a `README.md` slate table.
  Each topic page follows a fixed structure: status/venues/supporting-library header,
  Abstract, Research question, Methodology, Literature gap and closest prior work,
  Cautions and framing corrections, Supporting assets in star-voting-library (links
  into *this* repo at `blob/master/…`), Execution sketch. Topics 1–5 were produced by
  a 12-agent workflow (2026-07-24) and each passed a five-agent **adversarial novelty
  check**; anything added later must state its vetting level honestly rather than
  inherit that badge (topic 6, the metric distortion of STAR, started with a
  *preliminary* check and passed the full five-agent protocol on 2026-07-26 —
  its status line records the run and the residual caveats). **Don't search this repo for research topics —
  they aren't here**; clone the companion, match the house structure, update the
  README slate table, and keep the two repos pointing at each other. Working the
  other direction: when a teaching page states an open gap in print (as
  `07_Concepts/topics/distortion.md` does for STAR's missing distortion bound), that's exactly
  the raw material for a new topic page.
