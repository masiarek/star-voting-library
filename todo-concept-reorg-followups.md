# TODO — follow-ups parked from the concept reorganization (2026-07-29)

Working notes to pick up later. Not site content (excluded via `todo-*.md` in `mkdocs.yml`). Delete sections as they're done.

Context: the "one door per voting method" reorganization moved every method's concept pages out of `07_Concepts/` and into that method's own folder under `concepts/`. Commits `69916ba` · `88af3f5` · `49cc43b` · `f06cb46`.

## 1. Rescue any one-liner descriptions worth keeping

`07_Concepts/README.md` used to carry per-method concept tables — 20 rows of hand-written one-line descriptions. They were deleted in `f06cb46` because they duplicated indexes that now live in each method's own `concepts/README.md`, and two lists of the same pages drift apart.

*(Two further rows in those tables — the LH engine pages under `07_Concepts/tabulation_engines/` — are NOT lost: they were kept and moved up into the cross-method table on that same page, so they are deliberately absent below.)*

**The descriptions themselves were good.** The method folders' indexes cover the same pages but word them differently. If while reading you miss a particular line, lift it from below into that method's own index — the parked text is here so this needs no git archaeology:

Recover the whole page as it stood: `git show 49cc43b:07_Concepts/README.md`
(that is `f06cb46^` — the last commit before the deletion).

### RCV-IRV rows (8)

| Concept | One line |
|---------|----------|
| [**RCV is a confusing name**](06_Other/RCV_IRV/concepts/RCV-IRV-confusing-name.md) | "RCV" is an umbrella for many ranked methods; in the US it usually means RCV-IRV (Hare) |
| [**Is IRV "just plurality"?**](06_Other/RCV_IRV/concepts/RCV_IRV_and_plurality.md) | the defensible kernel (round-by-round first-choice elimination) vs. the overclaim |
| [**Is RCV "simple"? (201)**](06_Other/RCV_IRV/concepts/RCV_IRV_is_simple.md) | ranking is simple to *mark*; IRV's *count* isn't |
| [**Center squeeze**](06_Other/RCV_IRV/concepts/RCV_IRV_center_squeeze.md) | a broadly-liked moderate eliminated early under IRV; STAR avoids it |
| [**IRV non-monotonicity**](06_Other/RCV_IRV/concepts/RCV_IRV_non_monotonicity.md) | under IRV, *more* first-choice support can make the winner **lose** |
| [**Exhausted ballots**](06_Other/RCV_IRV/concepts/RCV_IRV_exhausted_ballots.md) | a validly-cast ranked ballot can stop counting; IRV's "majority" is of active ballots |
| [**IRV isn't summable**](06_Other/RCV_IRV/concepts/RCV_IRV_lack_of_summability.md) | the winner depends on elimination order, so every ballot must be counted centrally |
| [**Fails the Equal Vote**](06_Other/RCV_IRV/concepts/RCV_IRV_equal_vote.md) | opposite voters can't reliably cancel under sequential elimination — the equal-vote / spoiler failure (with an honest "is this fair?" caveat) |

### STAR rows (12)

| Concept | One line |
|---------|----------|
| [**STAR's hybrid nature**](01_STAR/concepts/the_count/STAR_hybrid_nature.md) | expressive scoring to find the finalists + a majority runoff to pick the winner — the design the rest of these pages build on |
| [**The Automatic Runoff Round**](01_STAR/concepts/the_count/STAR_Automatic_Runoff.md) | STAR's second step, end to end — finalists, the For/Against/Equal Support counts, percentages, tie-breaking, and Runoff Reversal; the hub for all runoff topics |
| [**Runoff Reversal — top scorer ≠ winner**](01_STAR/runoff_overturns_leader/) | the Scoring Round picks two finalists; the Automatic Runoff lets the *majority-preferred* finalist win — even with fewer total stars |
| [**Reading the runoff percentages**](01_STAR/concepts/the_count/runoff_percentages.md) | the same runoff vote shown two ways — % of all voters vs % of the voters *with a preference*; why the winner needs a majority of the decided voters, and where Equal Support goes |
| [**Three notions of "winner"**](01_STAR/concepts/properties_and_limits/STAR_three_winner_notions.md) | Condorcet vs Score vs Runoff can name three different candidates in one election |
| [**STAR is monotone**](01_STAR/concepts/properties_and_limits/STAR_monotonicity.md) | raising a candidate's score can never make them lose — the failure IRV has, STAR doesn't |
| [**STAR is summable**](01_STAR/concepts/properties_and_limits/STAR_summability.md) | tally by adding independent precinct totals; precinct-auditable, meaningful partials |
| [**Residual vote-splitting**](01_STAR/concepts/properties_and_limits/residual_vote_splitting.md) | STAR ends *forced* splitting; the narrow leftover is self-inflicted bullet-voting / the chicken dilemma |
| [**Equally Weighted Vote (Equal Vote Criterion)**](01_STAR/concepts/properties_and_limits/equally_weighted_vote.md) | every ballot has an exact opposite that cancels it (the Test of Balance) — why STAR fully ends *forced* vote-splitting; Choose-One and RCV-IRV fail it |
| [**STAR — honest limits**](01_STAR/concepts/properties_and_limits/STAR_honest_limits.md) | not Condorcet-compliant, not FBC-proof, gives up Later-No-Harm, residual splitting, strategic scoring — stated plainly |
| [**Tie-breaking — the full chain**](01_STAR/concepts/Tie_Breaking_STAR/tie_breaking.md) | ties fall through pairwise → five-star → lot order, in both rounds |
| [**Tie-breaking in BetterVoting JSON**](01_STAR/concepts/Tie_Breaking_STAR/tie_breaking_JSON.md) | how a BV export pre-draws the official lot order, and its YAML mapping |

Note: the links above are rewritten **relative to the repo root** (this file's location), not to `07_Concepts/` where they originally sat. They already point at the post-move paths, so the targets are right — just fix the relative depth when pasting one into a method folder's `concepts/README.md`.

## 2. `00_start_here/` renamed to `07_Concepts/` — DONE (2026-07-29)

The folder held only cross-cutting material after the method concepts moved out, so it was renamed and **renumbered to sort last**: the numeric prefix drives sidebar order, and the methods should lead rather than a reference folder. 2,322 link targets and 909 literal mentions rewritten across 1,235 files; 144 new redirects.

One hazard was specific to renaming *this* folder: `mkdocs.yml` already held 120 redirect entries whose SOURCE keys begin `00_start_here/`. Those keys are historical URLs — rewriting them would have pointed every one of those redirects at a URL that never existed, silently breaking the earlier migration including the two permanent BetterVoting backlinks. The script grew an `--exclude` flag for exactly this; `mkdocs.yml` was excluded and hand-edited instead, and the BV URL was re-verified to still resolve after the rename.

**Still open — where should `00_START_HERE.md` live?** It is now `07_Concepts/00_START_HERE.md`: a guided reading path for newcomers, sitting inside a reference folder that deliberately sorts last. The site homepage is the real front door and links to it directly, so nothing is broken, but "start here" being the last folder is odd. Options: leave it; move it to the repo root as `START_HERE.md`; or fold it into the homepage. Cheap to change — it is one file plus its inbound links.

## 3. Standing rule that came out of this

**Never delete a `redirect_maps` entry in `mkdocs.yml`.** Published URLs are quoted inside permanent BetterVoting election descriptions, which cannot be edited once an election goes live — two of them point at former `07_Concepts/STAR_Voting/` pages. A removed redirect is an unfixable 404. Recorded in `CLAUDE.md` and `ORGANIZATION.md` too.
