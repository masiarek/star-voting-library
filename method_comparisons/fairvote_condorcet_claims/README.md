# FairVote's Condorcet article, counted — the claim-check demos (BV2168/BV2169, live)

The tabulatable evidence behind [Claim check — FairVote's "Why the Condorcet Criterion Is Less Important Than It Seems"](../../00_start_here/topics/condorcet/fairvote_condorcet_claim_check.md). The article argues the [Condorcet criterion](../../00_start_here/topics/condorcet/) mostly just guarantees moderates; these two matched elections count its own hypothetical and a shifted-electorate companion, and the numbers say otherwise — while honestly preserving the article's one good point (pairwise order is blind to *intensity*; the score sum here disagrees with the pairwise majority).

**Both are LIVE BetterVoting elections**, each with two races on the same 100 voters — a STAR race and an RCV-IRV race — so the center squeeze is clickable, not just claimed:

- **BV2168** — [vote](https://bettervoting.com/6w2gq7) · **[results ↗](https://bettervoting.com/6w2gq7/results)** (election `6w2gq7`)
- **BV2169** — [vote](https://bettervoting.com/2jrfpg) · **[results ↗](https://bettervoting.com/2jrfpg/results)** (election `2jrfpg`)

**BV agrees with LH in all four races** (frozen exports beside the yamls: `*_bv_export.json`). BV2168: STAR → Moderate (pairwise 55/57, matching the LH matrix), RCV-IRV → Liberal (Moderate eliminated round one, final 51–49). BV2169: STAR and RCV-IRV → Liberal. Ballot multisets verified identical to the yaml blocs.

Read the reader-friendly **pages** (`fairvote_condorcet_claims_pages/`); the `.yaml` beside each is the tabulatable source.

| Page (read this) | What it shows | src |
|---|---|:--:|
| [BV2168 — FairVote's own hypothetical (45/12/43)](fairvote_condorcet_claims_pages/bv2168_6w2gq7_fairvote_40_15_40_moderate_cw.md) | the Moderate is the Condorcet winner by 55- and 57-voter majorities; the live RCV-IRV race eliminates them round one (center squeeze); the score sum narrowly says Liberal — the intensity nuance, shown honestly | [`.yaml`](bv2168_6w2gq7_fairvote_40_15_40_moderate_cw.yaml) |
| [BV2169 — electorate shifts left, the pole IS the Condorcet winner](fairvote_condorcet_claims_pages/bv2169_2jrfpg_fairvote_shifted_left_liberal_cw.md) | same cast, 56% now rank the strong Liberal first — a *pole* candidate is the Condorcet winner, refuting "centrist by nature, regardless of the preferences of the electorate"; STAR and the live IRV race agree | [`.yaml`](bv2169_2jrfpg_fairvote_shifted_left_liberal_cw.yaml) |

Concept hubs: [Condorcet efficiency](../../00_start_here/topics/condorcet/) · [center squeeze](../../00_start_here/topics/center_squeeze/) · up: [method_comparisons — same ballots, different methods](../)

# file: README.md
