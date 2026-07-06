# Multi-member plurality — Block vs. Limited vs. SNTV (same electorate, three outcomes)

*The three multi-member plurality methods differ in exactly one thing — **how many votes each voter casts** — and that one dial slides a 60/40 electorate from "majority sweeps everything" to "minority tops the poll." A clean demonstration that our engine's multi-winner Plurality (`run_plurality_multi`) tabulates all three correctly (it auto-detects which is which from the ballots).*

## The electorate

10 voters, **3 seats**: a 6-voter **Home** majority (60%) and a 4-voter **Away** minority (40%). Same voters in all three races — only the *number of votes per voter* changes.

| Method | Votes / voter | Winners | Home : Away | src |
|--------|:---:|---------|:---:|:--:|
| [**Block Voting**](mmp_block_voting.yaml) (plurality-at-large) | 3 (= seats) | Ada, Ben, Cal | **3 : 0** — majority sweeps | full slate |
| [**Limited Voting**](mmp_limited_voting.yaml) | 2 (< seats) | Ada, Ben, Uma | 2 : 1 | 2 votes each |
| [**SNTV**](mmp_sntv.yaml) | 1 | **Uma**, Ada, Ben | 2 : 1 — minority *tops the poll* | 1 vote each |

## What the dial does

- **Block voting (3 votes = seats).** Each Home voter votes the full Home slate, so Ada/Ben/Cal each get all 6 majority votes and beat every Away candidate (4). The 60% majority takes **all three seats**; the 40% minority is shut out. Majoritarian.
- **Limited voting (2 votes < seats).** A party can no longer fill every seat with its own votes, so over-nominating splits the vote; disciplined parties run about as many as they can win. Home runs 2 (Ada, Ben = 6), Away runs 2 (Uma, Val = 4) → **2 : 1**. Reducing votes-per-voter below the seat count is what opens the door.
- **SNTV (1 vote).** Pure vote-management: the majority *spreads* its 6 votes (2/2/2) while the minority *concentrates* all 4 on Uma — so **Uma finishes first** and the majority's split leaves its candidates on 2 each. **2 : 1**, and the minority candidate is the overall leader. Roughly proportional — the reason SNTV was used for multi-member districts (Japan, Taiwan) before STV.

The whole family is one tally — *most marks fill the N seats* — so the same engine handles all three; it reads votes-per-voter and labels the output **Block Voting**, **Limited Voting**, or **SNTV** accordingly.

## Why LH-only (a genuine exception)

Block and Limited Voting **can't be reproduced on BetterVoting**: BV's Plurality is *choose-one* (a single mark), so it can't cast the multi-mark ballots those methods require. That's a real "missing voting method" on BV, not a coverage gap — these are marked `lh_only_reason` in their yamls. (SNTV *is* BV-reproducible — it's choose-one — and its tally is BV-confirmed as the [BV2134 governance Bloc Plurality race](../pets_governance/pets_gov_bloc_plurality.yaml); it's kept here LH-side only to complete the comparison.)

## References

- **SNTV** — Wikipedia: [Single non-transferable vote](https://en.wikipedia.org/wiki/Single_non-transferable_vote) · electowiki: [Single non-transferable vote](https://electowiki.org/wiki/Single_non-transferable_vote)
- **Limited voting** — Wikipedia: [Limited voting](https://en.wikipedia.org/wiki/Limited_voting) · electowiki: [Limited voting](https://electowiki.org/wiki/Limited_voting)
- **Block voting** — Wikipedia: [Plurality block voting](https://en.wikipedia.org/wiki/Plurality_block_voting) · electowiki: [Bloc voting](https://electowiki.org/wiki/Bloc_voting)

## See also

- Folder overview: [multi_member_plurality — README](README.md)
- The BV-backed SNTV instance: [Pets Governance — Bloc Plurality](../pets_governance/pets_gov_bloc_plurality.yaml) · the whole [governance set](../pets_governance/)
- Proportional alternatives: [STV](../../06_Other/STV/) · [STAR-PR](../../03_STAR_PR/)
