# Matchups won vs. preference votes — the units bug in STAR's first tiebreaker

**Level: 301 · deep dive**

**One line:** STAR's first scoring-round rung asks "who won the most head-to-head matchups?", and there are two arithmetically different ways to answer that question — count each *matchup* once after deciding it by ballots, or count each *ballot's* pairwise opinions and add them up. They agree when exactly two candidates are tied and can disagree when three or more are, and the disagreement is severe enough to advance a candidate who loses every head-to-head.

→ Builds on [STAR Tie-Breaking — The Full Chain](tie_breaking.md) · engine-side companion: [Tiebreak ladders — every method, every engine](../../../07_Concepts/tabulation_engines/tiebreak_ladders.md) · sibling note in the same genre: [The "dead rung"](dead_rung_note_for_equal_vote.md) · the probe: [Matchups won, not preference votes](../../03_Criteria/tie_break_ladder/cases/cases_pages/tie_break_ladder_matchups_eliminate_loser.md).

---

## The rung, and the two ways to read it

Equal Vote's [Official Tiebreaker Protocol](https://www.starvoting.org/ties) resolves a scoring-round tie like this:

> Ties in the scoring round should be determined in favor of the candidate who was preferred (scored higher) by more voters. If there are only two candidates this will be the majority preferred candidate. If there are multiple candidates who are scored equally, ties are broken by comparing the tied candidates head to head and eliminating the candidate(s) who lost the most match-ups.

That last clause names a unit: **match-ups**. A matchup is a *pair of candidates*, and it is won by whichever candidate more **ballots** preferred. Decide each pair first, then count the pairs. This is the [Copeland](../../../05_Ranked_Robin/01_Learn/README.md) score computed over the tied group — aggregate, then compare.

The other reading walks the ballots instead. For each ballot, look at every pair of tied candidates and credit whoever that ballot rated higher; sum those credits across all ballots. Compare, then aggregate.

Both descriptions can be said out loud as "preferred in the most head-to-head matchups." Only one of them counts matchups.

## Why they agree at two candidates and diverge at three

With exactly two tied candidates there is exactly one pair. Counting the pair's winner and counting the ballots that preferred each side are the same comparison asked twice — one is just the other with a threshold applied. Every two-way tie gives the same answer under both readings.

Add a third candidate and the readings decouple, because the second one lets a **lopsided loss in one matchup subsidise a narrow loss in another**. A candidate can lose every pair and still collect a large total, if the pairs they lose are close and the ballots that do favour them favour them across the board.

That is not a hypothetical. It is the difference between "wins no matchups" and "was somebody's preference quite often," and STAR's rung is supposed to measure the first.

## The failure it permits

Five voters, four candidates, all four tied at 11 in the scoring round:

<!-- ballots:tie_break_ladder_matchups_eliminate_loser -->
*(No ballot art for `tie_break_ladder_matchups_eliminate_loser` — draw it with `build_style_ballot_images.py --from-yaml 01_STAR/03_Criteria/tie_break_ladder/cases/tie_break_ladder_matchups_eliminate_loser.yaml`.)*

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Ada,Ben,Cara,Doug
0,0,0,5      # Doug bloc — a 5 for Doug, nothing for anyone else
0,0,0,5      # Doug bloc
5,4,2,1      # Ada first
2,5,4,0      # Ben first
4,2,5,0      # Cara first
```
<!-- /ballots -->

Ada, Ben and Cara form a cycle — Ada beats Ben, Ben beats Cara, Cara beats Ada. Doug loses to all three, which makes him the [Condorcet loser](../../../07_Concepts/topics/condorcet/README.md). But the two voters who like Doug rate him 5 and everyone else 0, so Doug holds **two** maximum-score votes to everybody else's one.

Now walk the rung both ways:

| Reading | Ada | Ben | Cara | Doug | Result |
|---|---|---|---|---|---|
| **Matchups won** (the protocol) | 2 | 2 | 2 | **0** | Doug eliminated; five-star decides between the other three |
| **Preference votes summed** | 6 | 6 | 6 | **6** | nobody separated; five-star runs over all four — and **Doug wins it 2–1** |

Under the second reading the candidate no majority prefers over anyone becomes a finalist, on the strength of two enthusiastic ballots. The rung that exists to eliminate him instead scored him a perfect tie with the three candidates who each beat him.

<!-- report:tie_break_ladder_matchups_eliminate_loser -->
```text
[Divergence from STAR]
  STAR                   = Ada
  Choose-One (Plurality) = Doug   (differs from STAR)

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 5 ballots.
Count × Ada,Ben,Cara,Doug
    2 ×   0,  0,   0,   5
    1 ×   5,  4,   2,   1
    1 ×   2,  5,   4,   0
    1 ×   4,  2,   5,   0

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Ada           -- 11 -- Tied for first place
   Ben           -- 11 -- Tied for first place
   Cara          -- 11 -- Tied for first place
   Doug          -- 11 -- Tied for first place
 There's a four-way tie for first.

[STAR Voting: Scoring Round: First tiebreaker]
 The two candidates preferred in the most head-to-head matchups advance.
   Ada           -- 2 -- Tied for first place
   Ben           -- 2 -- Tied for first place
   Cara          -- 2 -- Tied for first place
   Doug          -- 0
   Equal Support -- 0
 There's still a three-way tie for first.

[STAR Voting: Scoring Round: Second tiebreaker]
 The two candidates with the most votes of score 5 advance.
   Ada           -- 1 -- Tied for first place
   Ben           -- 1 -- Tied for first place
   Cara          -- 1 -- Tied for first place
 There's still a three-way tie for first.

*(Ties are resolved by choosing the tied candidate with the highest-priority official lot number.)*
    Lot-number priority order: ['Ada', 'Ben', 'Cara', 'Doug']

[Tiebreaker: Lot Number Priority]
  Tie among: ['Ada', 'Ben', 'Cara']
  Resolved: ['Ada', 'Ben'] (selected by lot-number priority).

[Lot-decided tie — rare]
  ⚠ The ballots did not break this tie: the deterministic rungs
    (pairwise / score, then five-star) all came back equal, so the
    pre-published LOT order chose among the tied candidates — the
    result here was set by lot, not by the votes. Usually the
    "dead rung": no tied candidate held a score-5 vote (five-star
    counts fives, not fours). Verify the tied candidates' 5-counts.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Ada           -- 2 -- First place
   Ben           -- 1
   Equal Support -- 2
 Ada wins.
   Runoff math:
     5  ballots cast
   − 2  Equal Support (no preference between the two finalists)
     ─
     3  voters with a preference  (majority = 2)
           Ada 2 (67%)  ·  Ben 1 (33%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Ada
```
<!-- /report -->

## The ancestry: this is half of a bug already fixed in 2023

The interesting part is that the same function was reported for the same class of error three years ago, and only half of it was repaired.

[`starvote` issue #7](https://github.com/larryhastings/starvote/issues/7) (opened September 2023, fixed in four days) was about the *No Preference* line printed beneath this very rung. On three flat ballots with three candidates it read **9** where the answer is **3**:

```text title="Abridged from starvote#7 — the report as it stood in 2023"
[STAR Voting: Scoring Round: First tiebreaker]
    Andre         -- 0 -- Tied for first place
    Blake         -- 0 -- Tied for first place
    Carmen        -- 0 -- Tied for first place
    No Preference -- 9
```

Nine is three voters × three pairs. The issue's title stated the principle exactly: the number should be *"the number of voters who expressed no preference in a round, not the number of head-to-head contests where no preference was expressed."*

That principle was accepted and the *No Preference* counter was changed to count voters. The **wins** counter in the same function — the one that decides who advances — kept counting head-to-head contests. So the function went on returning two numbers in two different units, and the one left in the wrong unit was the load-bearing one.

The lesson generalises past this rung: when a tally is reported as wrong because it counts the wrong *thing*, check every counter in that function, not the one in the bug report. A units error is rarely lonely.

## What each engine does

| | Rung 1 on a 3+-way scoring tie |
|---|---|
| **Equal Vote's published protocol** | compare head to head, eliminate whoever lost the most matchups, repeat as needed until two advance |
| **This library's engine** (since 2026-08-21) | matchups won, over a tied group of any size — a drawn matchup goes to neither, matching this repo's [Ranked Robin](../../../05_Ranked_Robin/01_Learn/README.md) Copeland convention |
| **Vendored `starvote` before the fix** | summed pairwise preference votes, printed under a label naming matchups |
| **BetterVoting** | skips the rung entirely when more than two are tied and goes straight to five-star ([#1379](https://github.com/Equal-Vote/bettervoting/issues/1379)) |

So until 2026-08-21 **neither** engine this library runs implemented the published rung, in two different ways — one skipped it, the other substituted a different statistic under its name. The full ladder comparison, engine by engine, is in [tiebreak ladders](../../../07_Concepts/tabulation_engines/tiebreak_ladders.md#star-two-rounds-two-ladders).

## Why the existing tie probes could not catch it

This library carries a dozen deliberately-degenerate tie elections, several of which reach exactly this rung with three or more candidates tied. Not one of them detects the difference, and the reason is structural rather than an oversight: **they are symmetric, and symmetry ties both statistics**.

A rotation like `4,0,0 / 0,4,0 / 0,0,4` gives every candidate the same matchup record *and* the same preference-vote total, because it is built to give every candidate the same everything. A fully flat ballot set gives all zeros under both. The probes were designed to drive the ladder down to its floor, and they do that perfectly — which is precisely why they never exercise the one place the rungs disagree.

Catching this needs the opposite shape: **asymmetric in matchups, symmetric in score**. The tie has to be real (equal totals) while the head-to-head record is lopsided (someone loses everything). That is what the [probe case](../../03_Criteria/tie_break_ladder/cases/cases_pages/tie_break_ladder_matchups_eliminate_loser.md) is, and it is the only case in the corpus with that shape.

One honest limit, written into the case file itself: its `expected_winners` cannot guard the rung. A candidate who loses every matchup also loses the runoff he was wrongly advanced into, so Ada wins under both readings — what moves is the *finalist pair*. The guard is the `_tabulated` mirror, where a regression shows up as `Doug -- 0` disappearing from the first tiebreaker.

## What changed in this library, and what it cost

Across ~500 cases and 2,581 tests, **no winner changed** — not one, single-winner or multi-winner. Fourteen committed `_tabulated` mirrors moved: **eleven changed numbers**, and three more, already reading `0 / 0 / 0` because their ballots express no preference at all, gained only the new all-draws line described below. Four of the eleven changed *which rung* chose the finalists, and **two of those changed who the finalists were** — the pair moved, the winner did not, which is exactly the signature a wrong tiebreak rung leaves. All fourteen are listed with their before and after reports in [the appendix](#appendix-all-fourteen-mirrors-before-and-after).

The example the commit message singles out is `cycle_C05_fewV28_bloc_1`, which had shown a confident-looking `28 / 28 / 21` at rung 1 and separated the field on it; the corrected rung reads `1 / 0 / 0`, advances the one candidate who actually wins a matchup, and hands the second slot to the five-star rung. Same pair, different — and defensible — route.

The report also gained a line it needed. Copeland makes an all-draws tie print `0 / 0 / 0`, which on the dead-rung pages sits directly above a five-star rung that also prints `0 / 0 / 0`, meaning something completely different: there, zero means the rung had nothing to count. The engine now says *"Every head-to-head among the tied candidates is a draw, so none of them won a matchup"* whenever nobody won a pair — which is exactly when all-zero Copeland occurs, so no second classifier was needed.

## Appendix — all fourteen mirrors, before and after

Fourteen already-committed `_tabulated` mirrors moved in the fix commit ([`6d627e8`](https://github.com/masiarek/star-voting-library/commit/6d627e86f994a595267cbeb3cb3238b1873a039a)); a fifteenth is the new probe case's own mirror, which has no "before". Nothing here needs re-running to check — git holds both versions of every file:

```text
git show 6d627e8^:<path to the mirror>   # the pre-fix report
git show 6d627e8:<path to the mirror>    # the post-fix report
```

Only the **Scoring Round: First tiebreaker** block moved. Everything above it (ballots, scoring round, distributions) is byte-identical in all fourteen; everything below it is identical except in the four cases marked ⚑, where a changed rung-1 verdict propagates into the rungs beneath. No winner changed in any of them.

### Group 1 — every matchup among the tied group was a draw (7 cases)

The tied candidates are pairwise *tied with each other*, so nobody wins a pair and Copeland reads `0` across the board. The old tally still printed a non-zero number, because a drawn matchup still contains ballots with an opinion, and it counted those. This is also where the new explanatory line appears, so the row is not mistaken for the five-star rung's `0 / 0 / 0` two lines below.

| Case | Ballots | Tied at | Before — preference votes | After — matchups won | Below rung 1 |
|---|---|---|---|---|---|
| [`bv126_ties_every_step_8fvd2x`](../../03_Criteria/tie_break_dead_rung/cases/cases_pages/bv126_ties_every_step_8fvd2x.md) | 7 | Amy · Brian · Chuck at 29 | `2 / 2 / 2` | `0 / 0 / 0` | unchanged |
| [`three_way_dead_rung_A`](../../03_Criteria/tie_break_dead_rung/three_way_dead_rung_tie/three_way_dead_rung_tie_pages/three_way_dead_rung_A.md) | 3 | A · B · C at 4 | `2 / 2 / 2` | `0 / 0 / 0` | unchanged |
| [`three_way_dead_rung_B`](../../03_Criteria/tie_break_dead_rung/three_way_dead_rung_tie/three_way_dead_rung_tie_pages/three_way_dead_rung_B.md) | 3 | A · B · C at 4 | `2 / 2 / 2` | `0 / 0 / 0` | unchanged |
| [`three_way_dead_rung_C`](../../03_Criteria/tie_break_dead_rung/three_way_dead_rung_tie/three_way_dead_rung_tie_pages/three_way_dead_rung_C.md) | 3 | A · B · C at 4 | `2 / 2 / 2` | `0 / 0 / 0` | unchanged |
| [`bv2180_fp62p2_ice_cream_ladder`](../../03_Criteria/tie_break_ladder/cases/cases_pages/bv2180_fp62p2_ice_cream_ladder.md) | 2 | Chocolate · Chocolate Chip · Vanilla at 5 | `2 / 2 / 2` | `0 / 0 / 0` | unchanged |
| ⚑ [`cycle_C10_fewV28_bloc_1`](../../../05_Ranked_Robin/02_Examples/star_vs_rr_divergence/star_vs_rr_divergence_pages/cycle_C10_fewV28_bloc_1.md) | 28 | C · D · F at 119 | `F 14 / C 7 / D 7` | `0 / 0 / 0` | **finalists C + F → C + D** |
| ⚑ [`cycle_C10_fewV29_bloc_2`](../../../05_Ranked_Robin/02_Examples/star_vs_rr_divergence/star_vs_rr_divergence_pages/cycle_C10_fewV29_bloc_2.md) | 29 | A · C · F at 107 | `A 18 / C 9 / F 9` | `0 / 0 / 0` | **finalists A + C → C + F** |

The last two are the sharp ones, and they are the same failure the [probe case](../../03_Criteria/tie_break_ladder/cases/cases_pages/tie_break_ladder_matchups_eliminate_loser.md) was built to isolate, arriving unbidden in elections written for something else entirely. `cycle_C10_fewV29_bloc_2` is the clearer of the two, because its old rung-1 winner was decisive-looking:

```text title="Abridged — rung 1 only, cycle_C10_fewV29_bloc_2 BEFORE the fix"
[STAR Voting: Scoring Round: First tiebreaker]
 The two candidates preferred in the most head-to-head matchups advance.
   A             -- 18 -- First place
   C             --  9 -- Tied for second place
   F             --  9 -- Tied for second place
   Equal Support -- 11
 A advances, but there's still a two-way tie for second.
```

```text title="Abridged — rung 1 only, cycle_C10_fewV29_bloc_2 AFTER the fix"
[STAR Voting: Scoring Round: First tiebreaker]
 The two candidates preferred in the most head-to-head matchups advance.
   A             -- 0 -- Tied for first place
   C             -- 0 -- Tied for first place
   F             -- 0 -- Tied for first place
   Equal Support -- 11
 There's still a three-way tie for first.
 Every head-to-head among the tied candidates is a draw, so none of them won a matchup.
```

`A -- 18 -- First place` reads like a candidate who won the head-to-heads. A drew all three of them. The 18 is the count of ballots that expressed *some* preference involving A across two drawn pairs — a real number about the electorate, but not the number the rung asked for, and the label above it was already promising matchups. With the rung neutralised the five-star count takes over and separates C and F cleanly (`9 / 9 / 0`), so the finalist pair moves from A + C to C + F. The winner is C either way.

### Group 2 — a real matchup record, on the wrong scale (4 cases)

Here the tied candidates genuinely beat each other in a cycle, so Copeland is `1` apiece (or lopsided when the cycle is broken). The old numbers were larger and, in two cases, *ordered differently* — which is what let rung 1 decide something it should have passed on.

| Case | Ballots | Tied at | Before — preference votes | After — matchups won | Below rung 1 |
|---|---|---|---|---|---|
| [`b484mbm_tie_every_rung`](../../../02_STAR_Bloc/02_Examples/cases/cases_pages/b484mbm_tie_every_rung.md) | 3, 2 seats | Arden · Blythe · Corin at 12 | `3 / 3 / 3` | `1 / 1 / 1` | unchanged |
| [`edelman_perfect_component_c3_b30`](../../../method_comparisons/edelman_condorcet_myth/cases/cases_pages/edelman_perfect_component_c3_b30.md) | 30 | Ada · Ben · Cara at 70 | `30 / 30 / 30` | `1 / 1 / 1` | unchanged |
| ⚑ [`06_c4_b24_narrow-bands`](../../../06_Other/ballot_style_lab/cases/cases_pages/06_c4_b24_narrow-bands.md) | 24 | Azure · Beige · Coral at 61 | `Beige 18 / Coral 14 / Azure 12` | `1 / 1 / 1` | rung 1 no longer decides; **five-star picks the same pair** |
| ⚑ [`cycle_C05_fewV28_bloc_1`](../../../05_Ranked_Robin/02_Examples/star_vs_rr_divergence/star_vs_rr_divergence_pages/cycle_C05_fewV28_bloc_1.md) | 28 | A · C · E at 70 | `A 28 / E 28 / C 21` | `E 1 / A 0 / C 0` | rung 1 seats only E; **five-star adds A** — same pair |

`06_c4_b24_narrow-bands` is the cleanest illustration of the units problem, because the two readings disagree about the *ranking* and not merely the scale:

```text title="Abridged — rung 1 only, 06_c4_b24_narrow-bands BEFORE the fix"
[STAR Voting: Scoring Round: First tiebreaker]
 The two candidates preferred in the most head-to-head matchups advance.
   Beige         -- 18 -- First place
   Coral         -- 14 -- Second place
   Azure         -- 12
   Equal Support --  5
 Beige and Coral advance.
```

```text title="Abridged — rung 1 only, 06_c4_b24_narrow-bands AFTER the fix"
[STAR Voting: Scoring Round: First tiebreaker]
 The two candidates preferred in the most head-to-head matchups advance.
   Azure         -- 1 -- Tied for first place
   Beige         -- 1 -- Tied for first place
   Coral         -- 1 -- Tied for first place
   Equal Support -- 5
 There's still a three-way tie for first.

[STAR Voting: Scoring Round: Second tiebreaker]
 The two candidates with the most votes of score 5 advance.
   Beige         -- 8 -- First place
   Coral         -- 3 -- Second place
   Azure         -- 1
 Beige and Coral advance.
```

Azure, Beige and Coral are a three-cycle: each wins exactly one matchup, so the rung is silent by construction and the tie has to fall through. The old `18 / 14 / 12` looked like a clean ordering of the same three candidates and settled the finalists on it. Beige and Coral do advance either way — but before, on a number that was measuring something else; now, on the five-star rung, which is the rung the protocol actually hands the decision to.

`cycle_C05_fewV28_bloc_1` is the partial-separation case the commit message singles out: E wins a matchup, A and C do not, so rung 1 seats E and stops — exactly the "eliminate the candidate(s) who lost the most match-ups, repeat as needed" behaviour the protocol describes, and the only case in the corpus that exercises it.

### Group 3 — the new line only, no number moved (3 cases)

Fully flat or fully indifferent ballots make the two readings agree at zero, so these three mirrors changed by exactly one added line. They are in the list because they are the ones that motivated the line: on a page teaching the dead rung, a `0 / 0 / 0` at rung 1 and a `0 / 0 / 0` at rung 2 mean different things, and now only one of them says why.

| Case | Ballots | Tied at | Before | After | Change |
|---|---|---|---|---|---|
| [`Flat_scores_ties_06_scoring_tie_4way`](../../09_Parked/Flat_scores_ties/cases/cases_pages/Flat_scores_ties_06_scoring_tie_4way.md) | 2 | Ava · Ben · Cara · Dan at 10 | `0 / 0 / 0 / 0` | `0 / 0 / 0 / 0` | all-draws line added |
| [`Flat_scores_ties_07_fully_flat`](../../09_Parked/Flat_scores_ties/cases/cases_pages/Flat_scores_ties_07_fully_flat.md) | 2 | Ararat · Blanc · Cook at 10 | `0 / 0 / 0` | `0 / 0 / 0` | all-draws line added |
| [`bv750_tie_breaking_bloc`](../../../02_STAR_Bloc/02_Examples/cases/cases_pages/bv750_tie_breaking_bloc.md) | 3, 2 seats | a · b · c at 15 | `0 / 0 / 0` | `0 / 0 / 0` | all-draws line added |

### What the three groups add up to

Eleven mirrors changed numbers and three gained a line. Four changed which rung chose the finalists, and two of those changed *who the finalists were* — `cycle_C10_fewV28_bloc_1` (C + F → C + D) and `cycle_C10_fewV29_bloc_2` (A + C → C + F). Both still elect C, and in the first of them the second finalist was decided by lot before the fix and after it, so what moved there is which three candidates the lot was drawn among, not a ballot-driven verdict.

That is the honest summary of the blast radius: the rung was measuring the wrong quantity in every one of these elections, it changed the reported number in eleven of them, it changed the finalists in two — and it never once changed a winner. Which is precisely why nothing caught it for two years. A tiebreak rung sits far enough down the ladder that being wrong there is usually absorbed by the rungs below, and a corpus checked on winners cannot see an error the winner survives.

## See also

- [STAR Tie-Breaking — The Full Chain](tie_breaking.md) — the ladder in words, both rounds.
- [The "dead rung"](dead_rung_note_for_equal_vote.md) — the *other* rung that can quietly decide nothing.
- [Equal Vote's optional Condorcet Tiebreaker](condorcet_tiebreaker.md) — where "total preference votes" is a legitimate rung, as the **second** step of a different protocol.
- [Tiebreak ladders — every method, every engine](../../../07_Concepts/tabulation_engines/tiebreak_ladders.md) — every engine's ladder side by side, and the four floors they bottom out on.
- [Why build "silly" tie elections?](../../../07_Concepts/topics/ties/why_contrived_tie_cases.md) — the map of every tie branch, including the partial-elimination branch this case added.
