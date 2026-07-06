# Multi-member plurality — Limited Voting (3 seats): majority 2, minority 1

*Generated from [`mmp_limited_voting.yaml`](../mmp_limited_voting.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [plurality](../../../00_start_here) · **3 seats** · **Expected winners:** Ada, Ben, Uma

**Official tie-break (lot) order:** Ada > Ben > Cal > Uma > Val > Wren — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

One of three races comparing the multi-member plurality family on the SAME 60/40
electorate (LH-only — see the set README). 10 voters, 3 seats: a 6-voter MAJORITY
(Home: Ada, Ben) and a 4-voter MINORITY (Away: Uma, Val).

LIMITED VOTING: each voter casts FEWER votes than there are seats — here 2 votes
for 3 seats. Because a party can't fill every seat with its own supporters, over-
nominating splits its vote, so disciplined parties run about as many candidates
as they can win. Home runs 2 (Ada, Ben → 6 each); Away runs 2 (Uma, Val → 4 each).
The top three are Ada, Ben (6) and Uma (4; Val loses the last seat by lot) — a
2-1 split. Limited Voting sits between Block Voting (majority sweeps 3-0) and SNTV
(minority tops the poll): reducing votes-per-voter below the seat count is what
opens space for the minority.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Ada,Ben,Cal,Uma,Val,Wren
6: 1,1,0,0,0,0
4: 0,0,0,1,1,0
```

## What the engine says

Full report from the [`_tabulated` mirror](../multi_member_plurality_tabulated/mmp_limited_voting_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Limited Voting — 3 winners ---
 Tabulating 10 ballots (2 votes/voter).

Votes (most votes fill the seats):
   Ada      6  <- Elected
   Ben      6  <- Elected
   Uma      4  <- Elected
   Val      4
   Cal      0
   Wren     0

Winners — Limited Voting, 3 seats:
   1. Ada   (6 votes)
   2. Ben   (6 votes)
   3. Uma   (4 votes)
   *** the last seat tied on votes (Uma and Val) — decided by lot order.
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/multi_member_plurality/mmp_limited_voting.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Vote splitting (worked set)](../../split_voting/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [mmp_block_voting](mmp_block_voting.md) · [mmp_sntv](mmp_sntv.md)
