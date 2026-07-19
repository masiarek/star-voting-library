# TIPS — Canonical Elections (the reusable teaching cases)

*A handful of elections in this repo are **canonical**: designed once, frozen, and deliberately reused across many pages. Reuse helps the learner — the second time you meet the lunch vote, you already know the people and the stakes, so all your attention goes to the new idea. But reuse only works under discipline: this page is the registry of which elections are canonical, what job each one does, and the two rules that keep them trustworthy.*

→ Companions: [choosing voter counts](TIPS_choosing_voter_counts.md) · [YAML authoring template](../about_this_repo/YAML_authoring_template.md) · naming rules for *new* casts: [CLAUDE.md](../../CLAUDE.md) (candidate-names conventions)

---

## The two rules

1. **One election per page.** A teaching page sticks to a single cast from its first example to its last. Meeting Sushi/Tacos/Pizza at the top and Choco/Vanilla/Almond at the bottom reads like two different elections — the reader spends attention re-orienting instead of learning. Other scenarios are *linked*, not inlined. (Variety **between** pages is good and encouraged — see the name rules in CLAUDE.md; it's the mid-page cast-switch that breaks the rhythm.)

2. **Canonical = frozen.** Once an election is canonical, its ballots never change — no "let me just tweak voter 2 to show one more thing." A tweak silently changes totals and winners on every page that reuses the election (the shifting-sand problem). BV-backed canonicals are frozen *by construction* (cast ballots can't be edited — a feature, not a limitation). A lesson that needs different ballots gets a **new scenario with a new cast of names**, so no reader can confuse the two. Corollary: **same cast ⇒ same election** — if a page says "Ann, Bob, Cal," the ballots and the winner must be exactly the ones registered below.

## The canonical set

| # | Election | Cast | Size | The job (why this one exists) | Canonical home |
|---|---|---|---|---|---|
| 1 | **Ann, Bob, Cal** — the leading example | Ann, Bob, Cal | 3 cand × 3 ballots · BV2187 [`qrw6wb`](https://bettervoting.com/qrw6wb/results) | **Mechanics & authoring, no twist.** The smallest STAR election where both rounds do visible, different work: Bob 12 / Ann 8 / Cal 7 → finalists Bob & Ann; runoff Bob 2–1. Voter 1's ballot (Ann 5, Bob 4) is the runoff lesson — a friendly 4 for Bob still becomes a full vote for Ann. Bob leads the scores *and* wins the runoff (and is the Condorcet winner) — deliberately boring, so the *procedure* is the whole lesson. Default choice whenever a page needs "a STAR election" and nothing scenario-specific. | [page](../../01_STAR/_main/_main_pages/bv2187_qrw6wb_ann-bob-cal.md) · [`yaml`](../../01_STAR/_main/bv2187_qrw6wb_ann-bob-cal.yaml) — quoted by the [root README](../../readme.md), [authoring template](../about_this_repo/YAML_authoring_template.md), [why YAML](../about_this_repo/why_yaml_test_cases.md) |
| 2 | **The team lunch** | Sushi, Tacos, Pizza | 3 cand × 5 ballots · BV2184 [`fyy886`](https://bettervoting.com/fyy886/results) | **The story / the hook.** Vote-splitting breaks Choose-One (Sushi 2 · Tacos 2 · Pizza 1), STAR elects the compromise everyone is happy with; Choose-One *and* RCV-IRV both pick Sushi here. Foods on purpose: zero politics, instantly relatable. Sofia (a Sushi-lover) is the named voter whose ballot we follow through both rounds. | [STAR — start here](../STAR_Voting/STAR_start_here.md) (the whole spine: story, printed ballot, BV results, the one-ballot-two-rounds graphic) · [count it by hand](../STAR_Voting/hands_on/count_star_by_hand.md) · [page](../../01_STAR/_main/_main_pages/bv2184_fyy886_lunch_vote.md) · [`yaml`](../../01_STAR/_main/bv2184_fyy886_lunch_vote.yaml) |
| 3 | **The runoff reversal** | Almond, Berry, Cocoa | 3 cand · BV2182 [`tg4779`](https://bettervoting.com/tg4779/results) | **Why the runoff exists.** The Scoring-Round leader *loses* the Automatic Runoff — strength of support and number of supporters disagree, and STAR lets the majority decide between the two strongest. The go-to case for "isn't STAR just adding points?" | [page](../../01_STAR/_main/_main_pages/bv2182_tg4779_faq_runoff_reversal.md) · [`yaml`](../../01_STAR/_main/bv2182_tg4779_faq_runoff_reversal.yaml) — the FAQ / runoff-deep-dive pages |
| 4 | **Tennessee capital** | Memphis, Nashville, Chattanooga, Knoxville | 4 cand × 100 ballots | **The textbook classic.** The standard voting-theory profile (geographic factions), big enough for honest percentages — the bridge to method comparisons and center squeeze. Scale is the point; everything smaller should use #1–#3. | [page](../../01_STAR/_main/_main_pages/09_c4_b100_tennessee-capital.md) · [`yaml`](../../01_STAR/_main/09_c4_b100_tennessee-capital.yaml) |
| 5 | **The pets election** | Dog, Cat, … (7 pets) | 7 cand × 461 ballots · real BV election | **Real-world scale & reconciliation.** A genuinely cast BetterVoting election — the denominator/abstention/runoff-percentage material, and the LH↔BV cross-check story. | [case folder](../../01_STAR/pet_real_bv_election/) · [runoff percentages](../STAR_Voting/the_count/runoff_percentages.md) |
| 6 | **The minority winner** | Ada, Ben, Cleo | 3 cand × 100 ballots · BV2215 [`2p33qq`](https://bettervoting.com/2p33qq/results) | **The Choose-One failure, canonical.** Ada wins Choose-One on **34%** (a devoted third) while 66 of 100 score her ≤1; STAR & Ranked Robin elect Cleo, the broadly-liked Condorcet winner. The go-to "a third wins / minority winner" example — 100 voters so the count *is* the percent. Use it wherever a page needs to *show* a plurality/minority winner. | [case + easy page](../../method_comparisons/minority_winner/README.md) · [`yaml`](../../method_comparisons/minority_winner/bv2215_2p33qq_minority_winner.yaml) — quoted by [Choose-One / Plurality](../topics/plurality.md) |

**Plus one canonical *cast* (not a frozen election):** **Andre, Blake, Carmen, David, Ella…** — the Equal Vote Coalition's example names. Use them for **ballot anatomy and ballot-design topics** (they match the official materials a reader will meet on [equal.vote](https://www.equal.vote/star)) — the anatomy home page is [Alternate ballot styles — one voter, three ballots](../topics/ballot_styles.md) — and for large-field score-sheet demos ([runoff overturns leader](../../01_STAR/_main/_main_pages/06b_c9_runoff-overturns-leader.md)). Because this is a cast, not one frozen election, never present two different Andre–Ella elections on the same page.

## Which theme, when

- **Foods / flavors** → stakes-free hook scenarios where "no politics, no wrong answer" is the point: the lunch, the ice-cream progression ([02a](../../01_STAR/_main/_main_pages/02a_c3_b1_three-candidates.md)/[02b](../../01_STAR/_main/_main_pages/02b_c3_b2_three-candidates.md)).
- **Human names** → mechanics, authoring, and anything that should *look like a real ballot* (Ann/Bob/Cal; the EVC cast for anatomy).
- **Cities** → the historical classic (Tennessee) and geography-flavored scenarios.
- **Bare A/B/C** → academic/theory notes only (e.g. the [agenda voting](../other_ranked_methods/agenda_voting.md) digest) — never learner-facing teaching pages.

## Known warts (registered, not hidden)

- [`display_options_demo.yaml`](../../01_STAR/_main/display_options_demo.yaml) reuses **Ann, Bob, Cal (+ Don)** with *different* ballots and a different winner (Don) — it predates this registry and violates "same cast ⇒ same election." It's LH-only, so the cheap fix is to recast its candidates next time it's touched.
- **"Almond" serves two masters**: the ice-cream progression (Choco/Vanilla/**Almond**) and the BV-frozen runoff reversal (**Almond**/Berry/Cocoa). The BV one can't be renamed; if the collision ever confuses a reader, rename the 02-series flavors (LH-only, cheap).

## Adding a canonical election (checklist)

1. It must earn a **distinct job** none of the set above already does — canonical status is about *reuse*, so a one-page example doesn't qualify.
2. Smallest ballots that make the point ([voter-count tips](TIPS_choosing_voter_counts.md)); fresh cast per the CLAUDE.md name rules.
3. Brainstorm in `trash_delete.yaml`, get Adam's go, then **freeze**: BV-back it if the result is deterministic (the standard [BV workflow](../../CLAUDE.md)), register it in this table, and only then start reusing it.
