# multi_member_plurality — Block vs. Limited vs. SNTV (LH-only)

The three multi-member plurality methods on **one** 60/40 electorate (6-voter Home majority, 4-voter Away minority; 3 seats). They differ only in **votes per voter**, and that alone slides the result from majority sweep to minority-tops-the-poll.

Each row links the **page** — the readable write-up with the ballots and the engine's full count — and the **yaml** you feed the engine to run it yourself.

| Method | Votes/voter | Winners | Home : Away | Read · run |
|--------|:---:|---------|:---:|:--|
| Block Voting (plurality-at-large) | 3 | Ada, Ben, Cal | **3 : 0** | [page](cases/cases_pages/mmp_block_voting.md) · [yaml](cases/mmp_block_voting.yaml) |
| Limited Voting | 2 | Ada, Ben, Uma | 2 : 1 | [page](cases/cases_pages/mmp_limited_voting.md) · [yaml](cases/mmp_limited_voting.yaml) |
| SNTV | 1 | Uma, Ada, Ben | 2 : 1 (Uma leads) | [page](cases/cases_pages/mmp_sntv.md) · [yaml](cases/mmp_sntv.yaml) |

Plus a fourth case on the same family — **[the majority ceiling](cases/cases_pages/mmp_majority_ceiling.md)** ([yaml](cases/mmp_majority_ceiling.yaml)): with *k* marks per voter no candidate can exceed **1/k** of the votes cast, so a *unanimous* candidate still shows 33.3% at 3 seats. That kills the common "the winner got under 50%, so the vote was split" reading in any multi-seat race — see [How often does vote splitting actually happen?](../split_voting/how_often_does_vote_splitting_happen.md).

Confirms our engine's multi-winner Plurality (`run_plurality_multi`) tabulates the whole family (it auto-detects Block / Limited / SNTV from votes-per-voter).

**All BV-confirmed** (not exceptions). BV has no method *named* Block/Limited Voting, but all three are "mark k, top N win" = BV's **multi-winner Approval** with each voter approving k (full slate = block, k<N = limited, 1 = SNTV). Block & Limited are backed by BV election **BV2135** ([`3x4vrv`](https://bettervoting.com/3x4vrv/results)) — same ballots, same winners; SNTV by the BV2134 governance Bloc Plurality race. The LH yamls carry the Plurality-family teaching label; BV runs them as Approval. Full recipe: [running it on BetterVoting](running_on_bettervoting.md).

→ **Full lesson (with Wikipedia + electowiki links):** [Block, Limited & SNTV — the multi-member plurality family](multi_member_plurality.md)

# file: README.md
