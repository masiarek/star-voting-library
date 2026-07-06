# Multi-member plurality — SNTV (3 seats): the minority tops the poll

*Generated from [`mmp_sntv.yaml`](../mmp_sntv.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [plurality](../../../00_start_here) · **3 seats** · **Expected winners:** Uma, Ada, Ben

**Official tie-break (lot) order:** Ada > Ben > Cal > Uma > Val > Wren — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

One of three races comparing the multi-member plurality family on the SAME 60/40
electorate (LH-only — see the set README). 10 voters, 3 seats: a 6-voter MAJORITY
(Home: Ada, Ben, Cal) and a 4-voter MINORITY (Away: Uma).

SNTV (single non-transferable vote): each voter casts exactly ONE vote, no matter
how many seats. Vote management decides everything. The majority spreads its 6
votes evenly (2 Ada, 2 Ben, 2 Cal); the minority concentrates all 4 on Uma. So
Uma FINISHES FIRST with 4, and the majority's split leaves its candidates on 2
each — Uma plus two Home candidates win, 2-1. The 40% minority earns a seat
because SNTV rewards concentrating votes (and punishes over-nominating). This is
the majoritarian sweep of Block Voting turned into rough proportionality.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Ada,Ben,Cal,Uma,Val,Wren
2: 1,0,0,0,0,0
2: 0,1,0,0,0,0
2: 0,0,1,0,0,0
4: 0,0,0,1,0,0
```

## What the engine says

Full report from the [`_tabulated` mirror](../multi_member_plurality_tabulated/mmp_sntv_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- SNTV (single non-transferable vote) — 3 winners ---
 Tabulating 10 ballots (1 vote/voter).

First-choice votes (most votes fill the seats):
   Uma      4  <- Elected
   Ada      2  <- Elected
   Ben      2  <- Elected
   Cal      2
   Val      0
   Wren     0

Winners — SNTV (single non-transferable vote), 3 seats:
   1. Uma   (4 votes)
   2. Ada   (2 votes)
   3. Ben   (2 votes)
   *** the last seat tied on votes (Ben and Cal) — decided by lot order.
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/multi_member_plurality/mmp_sntv.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Vote splitting (worked set)](../../split_voting/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [mmp_block_voting](mmp_block_voting.md) · [mmp_limited_voting](mmp_limited_voting.md)
