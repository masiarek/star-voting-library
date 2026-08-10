# Multi-member plurality — Block, Limited, SNTV and the rest of the block voting family

*These methods differ in exactly one thing — **how many candidates each voter may mark** — and that one dial slides a 60/40 electorate from "majority sweeps everything" to "minority tops the poll." Then a second electorate turns the dial the other way, on the case that decides real arguments about at-large elections: a bloc that most voters voted against taking every seat. A clean demonstration that our engine's multi-winner Plurality (`run_plurality_multi`) tabulates the whole family (it auto-detects which is which from the ballots).*

## The first electorate

10 voters, **3 seats**: a 6-voter **Home** majority (60%) and a 4-voter **Away** minority (40%). Same voters in all three races — only the *number of votes per voter* changes.

| Method | Votes / voter | Winners | Home : Away | Read · run |
|--------|:---:|---------|:---:|:--|
| [**Block Voting**](cases/cases_pages/mmp_block_voting.md) (plurality-at-large) | 3 (= seats) | Ada, Ben, Cal | **3 : 0** — majority sweeps | [page](cases/cases_pages/mmp_block_voting.md) · [yaml](cases/mmp_block_voting.yaml) |
| [**Limited Voting**](cases/cases_pages/mmp_limited_voting.md) | 2 (< seats) | Ada, Ben, Uma | 2 : 1 | [page](cases/cases_pages/mmp_limited_voting.md) · [yaml](cases/mmp_limited_voting.yaml) |
| [**SNTV**](cases/cases_pages/mmp_sntv.md) | 1 | **Uma**, Ada, Ben | 2 : 1 — minority *tops the poll* | [page](cases/cases_pages/mmp_sntv.md) · [yaml](cases/mmp_sntv.yaml) |

*Each method name links to its page — the ballots and the engine's full count, written up; the **yaml** is the same election as raw source. A companion case on the same electorate, [the majority ceiling](cases/cases_pages/mmp_majority_ceiling.md) ([yaml](cases/mmp_majority_ceiling.yaml)), is why a multi-seat winner's "%" can never reach 50 — see the [folder README](README.md).*

## What the dial does

- **Block voting (3 votes = seats).** Each Home voter votes the full Home slate, so Ada/Ben/Cal each get all 6 majority votes and beat every Away candidate (4). The 60% majority takes **all three seats**; the 40% minority is shut out. Majoritarian.
- **Limited voting (2 votes < seats).** A party can no longer fill every seat with its own votes, so over-nominating splits the vote; disciplined parties run about as many as they can win. Home runs 2 (Ada, Ben = 6), Away runs 2 (Uma, Val = 4) → **2 : 1**. Reducing votes-per-voter below the seat count is what opens the door.
- **SNTV (1 vote).** Pure vote-management: the majority *spreads* its 6 votes (2/2/2) while the minority *concentrates* all 4 on Uma — so **Uma finishes first** and the majority's split leaves its candidates on 2 each. **2 : 1**, and the minority candidate is the overall leader. Roughly proportional — the reason SNTV was used for multi-member districts (Japan, Taiwan) before STV.

The whole family is one tally — *most marks fill the N seats* — so the same engine handles all three; it reads votes-per-voter and labels the output **Block Voting**, **Limited Voting**, or **SNTV** accordingly.

## Second electorate: the bloc that sweeps is a minority

A 60% majority taking every seat is the mild version. The version that decides real arguments about at-large elections is a faction **most voters voted against** taking every seat — and that needs only one extra ingredient: an opposition split across more than one group.

9 voters, 3 seats, 9 candidates. Party Oak (Alma, Bram, Cleo) has 4 voters, Party Pine (Dev, Enzo, Finn) has 3, and 2 voters prefer the independents (Gus, Hugo, Iris). Every bloc marks its own slate, so every candidate simply collects their own bloc.

| Rule | Marks/voter | Oak | Pine | Independents | Winners |
|---|:---:|:---:|:---:|:---:|---|
| [Plurality block voting](cases/cases_pages/mmp_minority_sweep.md) | 3 | **4** | 3 | 2 | **Oak sweeps on 44%** |
| [Block approval voting](cases/cases_pages/mmp_block_approval.md) | uncapped | 4 | **5** | 2 | **Pine sweeps**, one round |
| [Majority block voting](cases/cases_pages/mmp_majority_block_runoff.md), round 2 | 3 | 4 | **5** | — | **Pine sweeps** with a 5-of-9 majority |

One unchanged set of opinions, two opposite clean sweeps. Read down the rows:

- **Capped at 3 marks, Oak sweeps.** The 56% of voters who wanted someone else elect nobody, because they are split two ways and neither group out-polls Oak on its own. Block voting rewards the largest *bloc*, not the largest agreement.
- **Uncapped, Pine sweeps.** The two independent voters approve their three independents *and* the Pine slate they prefer to Oak. Their opinion did not change — only how much of it the ballot could hold. Pine goes 3 → 5 and Oak's unchanged 4 stops being the largest number on the page.
- **Two rounds, Pine sweeps.** Round 1 *is* the plurality-block row: Oak leads on 4, but a majority is 5, so nobody is elected and the trailing independents drop out. Their voters must now choose between the slates, and Pine crosses the line.

None of this makes block approval the good one — it hands one bloc all three seats here too, and that is the family's signature, not an accident of this profile. Proportionality is a property of the *count*, not of the mark limit: for that, see [STAR-PR](../../03_STAR_PR/README.md) or [STV](../../06_Other/STV/README.md).

**How small can this get?** The floor for a minority sweep is [**5 voters**](cases/cases_pages/mmp_sweep_floor.md): two mark a full 3-candidate slate, three each bullet-vote a different name, and 40% of the electorate takes 100% of the seats, 2 votes to 1. Four voters cannot do it — a bloc big enough to out-poll every rival would be half the electorate. Nine is likewise the floor for the three-row table above, which needs Oak > Pine > independents *and* Pine + independents > Oak all at once; one independent voter makes that impossible for any Pine bloc size, and 4/3/2 is the smallest that works.

That matters because the textbook version of this table — the one in [Wikipedia's block voting article](https://en.wikipedia.org/wiki/Block_voting) — uses **10,000 voters, 12 candidates and 28,000 marks**, and its columns are *asserted totals* rather than ballots, so there is nothing to divide down. To shrink an example like that you have to rebuild the profile behind it and shrink *that*: collapse the voters into blocs, keep only the candidates that touch a seat or absorb a mark, and rescale to the smallest integers that keep every inequality the lesson uses strict. Then check the one freedom such tables use silently — that a voter **need not use every mark** (the article's own total is 28,000 of a possible 30,000). Remove that freedom and the minority sweep disappears, because the independents' spare marks would land on Pine.

## Can these run on BetterVoting? Yes — as bloc Approval.

BV has no method *named* "Block Voting" or "Limited Voting" (its **Plurality** is choose-one), but that's a naming point, not a capability gap. All three are "mark k candidates, top N win" — which is exactly what BV's **multi-winner Approval** (`Approval` + `num_winners`) does. So each is reproducible on BV with the same 0/1 ballots and the same winners:

- **Block voting** = bloc Approval where each voter approves their **full N-candidate slate**.
- **Limited voting** = bloc Approval where each voter approves **k < N**.
- **SNTV** = bloc Approval (or Plurality) where each voter approves **exactly 1** — already BV-confirmed as the [BV2134 governance Bloc Plurality race](../pets_governance/cases/cases_pages/pets_gov_bloc_plurality.md).

This set's *point* is the Plurality-family framing (votes-per-voter), and our engine labels the tally Block / Limited / SNTV accordingly — but the arithmetic is **BV-confirmed end-to-end**. Block and Limited are backed by BV election **BV2135** ([`3x4vrv`](https://bettervoting.com/3x4vrv/results)), which runs both as bloc Approval and elects exactly the same seats (Block → Ada, Ben, Cal; Limited → Ada, Ben, Uma). SNTV is BV-backed separately as the [governance Bloc Plurality race](../pets_governance/cases/cases_pages/pets_gov_bloc_plurality.md). Full recipe: [running_on_bettervoting.md](running_on_bettervoting.md).

**▶ Block & Limited live on BetterVoting:** [results ↗](https://bettervoting.com/3x4vrv/results) (election `3x4vrv`, Test ID BV2135) · frozen export [`mmp_bv2135_3x4vrv_bv_export.json`](cases/mmp_bv2135_3x4vrv_bv_export.json).

The second electorate's four cases are **LH-only so far**. Nothing blocks them: they are 0/1 ballots and top-N-wins like the rest, block approval is bloc Approval with no cap, and the two-round case is just its two rounds run as two races.

## References

- **SNTV** — Wikipedia: [Single non-transferable vote](https://en.wikipedia.org/wiki/Single_non-transferable_vote) · electowiki: [Single non-transferable vote](https://electowiki.org/wiki/Single_non-transferable_vote)
- **Limited voting** — Wikipedia: [Limited voting](https://en.wikipedia.org/wiki/Limited_voting) · electowiki: [Limited voting (Wikipedia)](https://en.wikipedia.org/wiki/Limited_voting)
- **Block voting** — Wikipedia: [Plurality block voting](https://en.wikipedia.org/wiki/Plurality_block_voting) · electowiki: [Bloc voting](https://electowiki.org/wiki/Bloc_voting)
- **The class these belong to** — Wikipedia: [Block voting](https://en.wikipedia.org/wiki/Block_voting) (the umbrella: plurality block, approval block, two-round block, party block, and the ranked member below) · [Block preferential voting](https://en.wikipedia.org/wiki/Block_preferential_voting)

## See also

- Folder overview: [multi_member_plurality — README](README.md)
- The BV-backed SNTV instance: [Pets Governance — Bloc Plurality](../pets_governance/cases/cases_pages/pets_gov_bloc_plurality.md) ([yaml](../pets_governance/cases/pets_gov_bloc_plurality.yaml)) · the whole [governance set](../pets_governance/README.md)
- The **ranked** member of the same class: [Block preferential voting](../block_preferential/README.md) — instant runoff run once per seat. Same majoritarian outcome as block voting, reached the long way round ([concept page](../../06_Other/RCV_IRV/concepts/variants/RCV-IRV-block-preferential.md))
- Proportional alternatives: [STV](../../06_Other/STV/README.md) · [STAR-PR](../../03_STAR_PR/README.md)
