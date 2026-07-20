# Multi-member plurality — Block Voting (3 seats): majority sweeps

*Generated from [`mmp_block_voting.yaml`](../mmp_block_voting.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [plurality](../../../../00_start_here) · **3 seats** · **Expected winners:** Ada, Ben, Cal

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/3x4vrv) · **[results ↗](https://bettervoting.com/3x4vrv/results)** (election `3x4vrv`).

**Official tie-break (lot) order:** Ada > Ben > Cal > Uma > Val > Wren — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

One of three races comparing the multi-member plurality family on the SAME 60/40
electorate (LH-only — see the set README). 10 voters, 3 seats: a 6-voter MAJORITY
(Home party: Ada, Ben, Cal) and a 4-voter MINORITY (Away party: Uma, Val, Wren).

BLOCK VOTING (plurality-at-large): each voter casts as many votes as there are
seats (3) and votes their full slate. So every Home candidate gets all 6 majority
votes and every Away candidate all 4 minority votes — Ada, Ben, Cal (6 each) beat
Uma, Val, Wren (4 each) and the majority SWEEPS all three seats, 3-0. The 40%
minority is shut out entirely. Contrast SNTV and Limited Voting (same electorate),
where the minority earns a seat.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Ada,Ben,Cal,Uma,Val,Wren
6: 1,1,1,0,0,0
4: 0,0,0,1,1,1
```

## What the engine says

Full report from the [`_tabulated` mirror](../cases_tabulated/mmp_block_voting_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Block Voting (plurality-at-large) — 3 winners ---
 Tabulating 10 ballots (3 votes/voter).

Votes (most votes fill the seats):
   Ada      6  <- Elected
   Ben      6  <- Elected
   Cal      6  <- Elected
   Uma      4
   Val      4
   Wren     4

Winners — Block Voting (plurality-at-large), 3 seats:
   1. Ada   (6 votes)
   2. Ben   (6 votes)
   3. Cal   (6 votes)
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/multi_member_plurality/cases/mmp_block_voting.yaml
```

## See also

- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [mmp_limited_voting](mmp_limited_voting.md) · [mmp_sntv](mmp_sntv.md)
