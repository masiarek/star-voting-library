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

So until 2026-08-21 **neither** engine this library runs implemented the published rung, in two different ways — one skipped it, the other substituted a different statistic under its name. The full ladder comparison, engine by engine, is in [tiebreak ladders](../../../07_Concepts/tabulation_engines/tiebreak_ladders.md#star--two-rounds-two-ladders).

## Why the existing tie probes could not catch it

This library carries a dozen deliberately-degenerate tie elections, several of which reach exactly this rung with three or more candidates tied. Not one of them detects the difference, and the reason is structural rather than an oversight: **they are symmetric, and symmetry ties both statistics**.

A rotation like `4,0,0 / 0,4,0 / 0,0,4` gives every candidate the same matchup record *and* the same preference-vote total, because it is built to give every candidate the same everything. A fully flat ballot set gives all zeros under both. The probes were designed to drive the ladder down to its floor, and they do that perfectly — which is precisely why they never exercise the one place the rungs disagree.

Catching this needs the opposite shape: **asymmetric in matchups, symmetric in score**. The tie has to be real (equal totals) while the head-to-head record is lopsided (someone loses everything). That is what the [probe case](../../03_Criteria/tie_break_ladder/cases/cases_pages/tie_break_ladder_matchups_eliminate_loser.md) is, and it is the only case in the corpus with that shape.

One honest limit, written into the case file itself: its `expected_winners` cannot guard the rung. A candidate who loses every matchup also loses the runoff he was wrongly advanced into, so Ada wins under both readings — what moves is the *finalist pair*. The guard is the `_tabulated` mirror, where a regression shows up as `Doug -- 0` disappearing from the first tiebreaker.

## What changed in this library, and what it cost

Across ~500 cases and 2,581 tests, **no winner changed**. Twelve `_tabulated` mirrors changed numbers. One case changed which rung chose the finalists: `cycle_C05_fewV28_bloc_1` had shown a confident-looking `28 / 28 / 21` at rung 1 and separated the field on it; the corrected rung reads `1 / 0 / 0`, advances the one candidate who actually wins a matchup, and hands the second slot to the five-star rung. Same pair, different — and defensible — route.

The report also gained a line it needed. Copeland makes an all-draws tie print `0 / 0 / 0`, which on the dead-rung pages sits directly above a five-star rung that also prints `0 / 0 / 0`, meaning something completely different: there, zero means the rung had nothing to count. The engine now says *"Every head-to-head among the tied candidates is a draw, so none of them won a matchup"* whenever nobody won a pair — which is exactly when all-zero Copeland occurs, so no second classifier was needed.

## See also

- [STAR Tie-Breaking — The Full Chain](tie_breaking.md) — the ladder in words, both rounds.
- [The "dead rung"](dead_rung_note_for_equal_vote.md) — the *other* rung that can quietly decide nothing.
- [Equal Vote's optional Condorcet Tiebreaker](condorcet_tiebreaker.md) — where "total preference votes" is a legitimate rung, as the **second** step of a different protocol.
- [Tiebreak ladders — every method, every engine](../../../07_Concepts/tabulation_engines/tiebreak_ladders.md) — every engine's ladder side by side, and the four floors they bottom out on.
- [Why build "silly" tie elections?](../../../07_Concepts/topics/ties/why_contrived_tie_cases.md) — the map of every tie branch, including the partial-elimination branch this case added.
