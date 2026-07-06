# multi_member_plurality — Block vs. Limited vs. SNTV (LH-only)

The three multi-member plurality methods on **one** 60/40 electorate (6-voter Home majority, 4-voter Away minority; 3 seats). They differ only in **votes per voter**, and that alone slides the result from majority sweep to minority-tops-the-poll.

| Method | Votes/voter | Winners | Home : Away | src |
|--------|:---:|---------|:---:|:--:|
| Block Voting (plurality-at-large) | 3 | Ada, Ben, Cal | **3 : 0** | [`.yaml`](mmp_block_voting.yaml) |
| Limited Voting | 2 | Ada, Ben, Uma | 2 : 1 | [`.yaml`](mmp_limited_voting.yaml) |
| SNTV | 1 | Uma, Ada, Ben | 2 : 1 (Uma leads) | [`.yaml`](mmp_sntv.yaml) |

Confirms our engine's multi-winner Plurality (`run_plurality_multi`) tabulates the whole family (it auto-detects Block / Limited / SNTV from votes-per-voter).

**Genuine LH-only exception:** Block and Limited Voting have **no BetterVoting equivalent** (BV Plurality is choose-one / single-mark), so they can't be reproduced there — marked `lh_only_reason` in the yamls. SNTV *is* BV-reproducible (BV-confirmed as the BV2134 governance Bloc Plurality race); it's here only to complete the comparison.

→ **Full lesson (with Wikipedia + electowiki links):** [multi_member_plurality.md](multi_member_plurality.md)

# file: README.md
