# multi_member_plurality — the block voting family (LH-only)

Two small electorates, eight cases. The **first** runs Block / Limited / SNTV on one 60/40 electorate (6-voter Home majority, 4-voter Away minority; 3 seats): they differ only in **votes per voter**, and that alone slides the result from majority sweep to minority-tops-the-poll. The **second** adds the rest of the family — plurality block, block approval and two-round majority block — on an electorate where the bloc that sweeps is a **minority**.

All three are **majoritarian** at-large methods — whether you want that at all, or a [proportional](../../03_STAR_PR/README.md) body instead, is the decision that comes first: [Electing more than one, simply](../../07_Concepts/topics/electing_more_than_one.md). The expressive majoritarian alternative to these is [Bloc STAR](../../02_STAR_Bloc/README.md).

Each row links the **page** — the readable write-up with the ballots and the engine's full count — and the **yaml** you feed the engine to run it yourself.

| Method | Votes/voter | Winners | Home : Away | Read · run |
|--------|:---:|---------|:---:|:--|
| Block Voting (plurality-at-large) | 3 | Ada, Ben, Cal | **3 : 0** | [page](cases/cases_pages/mmp_block_voting.md) · [yaml](cases/mmp_block_voting.yaml) |
| Limited Voting | 2 | Ada, Ben, Uma | 2 : 1 | [page](cases/cases_pages/mmp_limited_voting.md) · [yaml](cases/mmp_limited_voting.yaml) |
| SNTV | 1 | Uma, Ada, Ben | 2 : 1 (Uma leads) | [page](cases/cases_pages/mmp_sntv.md) · [yaml](cases/mmp_sntv.yaml) |

Plus a fourth case on the same family — **[the majority ceiling](cases/cases_pages/mmp_majority_ceiling.md)** ([yaml](cases/mmp_majority_ceiling.yaml)): with *k* marks per voter no candidate can exceed **1/k** of the votes cast, so a *unanimous* candidate still shows 33.3% at 3 seats. That kills the common "the winner got under 50%, so the vote was split" reading in any multi-seat race — see [How often does vote splitting actually happen?](../split_voting/how_often_does_vote_splitting_happen.md).

## Second electorate — when the sweeping bloc is a *minority*

Above, a 60% majority sweeps. The sharper version of the same defect is a bloc that **most voters voted against** taking every seat, which happens as soon as the opposition is split. 9 voters, 3 seats, 9 candidates: Party Oak has 4 voters, Party Pine 3, and 2 voters prefer the independents. Same voters in all three rows — only the ballot rule changes.

| Rule | Marks per voter | Winners | Result | Read · run |
|--------|:---:|---------|:--|:--|
| Plurality block voting | 3 | Alma, Bram, Cleo | **Oak sweeps 3 : 0 on 44%** | [page](cases/cases_pages/mmp_minority_sweep.md) · [yaml](cases/mmp_minority_sweep.yaml) |
| Block approval voting | uncapped | Dev, Enzo, Finn | **Pine sweeps** — one round | [page](cases/cases_pages/mmp_block_approval.md) · [yaml](cases/mmp_block_approval.yaml) |
| Majority block voting, round 2 | 3 | Dev, Enzo, Finn | **Pine sweeps** with a real 5-of-9 majority | [page](cases/cases_pages/mmp_majority_block_runoff.md) · [yaml](cases/mmp_majority_block_runoff.yaml) |

Three counts of one unchanged set of opinions, two opposite clean sweeps. The round-2 case's round 1 *is* the plurality-block case — Oak leads on 4, nobody reaches 5, the independents are eliminated, and their voters' marks move to Pine. Uncapping the marks reaches the same place in a single round, because it lets those voters say "independents, and Pine over Oak" the first time they are asked.

And the floor: **[the smallest possible minority sweep](cases/cases_pages/mmp_sweep_floor.md)** ([yaml](cases/mmp_sweep_floor.yaml)) — **5 voters**, two marking a full slate and three each bullet-voting a different name. 40% of the voters take 100% of the seats, and no smaller electorate can do it.

Confirms our engine's multi-winner Plurality (`run_plurality_multi`) tabulates the whole family (it auto-detects Block / Limited / SNTV from votes-per-voter), and its multi-winner Approval covers the uncapped member.

**The first electorate is BV-confirmed** (not exceptions). BV has no method *named* Block/Limited Voting, but all three are "mark k, top N win" = BV's **multi-winner Approval** with each voter approving k (full slate = block, k<N = limited, 1 = SNTV). Block & Limited are backed by BV election **BV2135** ([`3x4vrv`](https://bettervoting.com/3x4vrv/results)) — same ballots, same winners; SNTV by the BV2134 governance Bloc Plurality race. The LH yamls carry the Plurality-family teaching label; BV runs them as Approval. Full recipe: [running it on BetterVoting](running_on_bettervoting.md).

The second electorate's four cases are **LH-only so far**, but reproducible on BV by the same recipe — each is 0/1 ballots and top-N-wins, and the two-round case is simply its two rounds run as two races.

→ **Full lesson (with Wikipedia + electowiki links):** [Block, Limited & SNTV — the multi-member plurality family](multi_member_plurality.md)

# file: README.md
