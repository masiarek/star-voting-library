# Multi-member plurality — Block vs. Limited vs. SNTV (same electorate, three outcomes)

*The three multi-member plurality methods differ in exactly one thing — **how many votes each voter casts** — and that one dial slides a 60/40 electorate from "majority sweeps everything" to "minority tops the poll." A clean demonstration that our engine's multi-winner Plurality (`run_plurality_multi`) tabulates all three correctly (it auto-detects which is which from the ballots).*

## The electorate

10 voters, **3 seats**: a 6-voter **Home** majority (60%) and a 4-voter **Away** minority (40%). Same voters in all three races — only the *number of votes per voter* changes.

| Method | Votes / voter | Winners | Home : Away | src |
|--------|:---:|---------|:---:|:--:|
| [**Block Voting**](cases/mmp_block_voting.yaml) (plurality-at-large) | 3 (= seats) | Ada, Ben, Cal | **3 : 0** — majority sweeps | full slate |
| [**Limited Voting**](cases/mmp_limited_voting.yaml) | 2 (< seats) | Ada, Ben, Uma | 2 : 1 | 2 votes each |
| [**SNTV**](cases/mmp_sntv.yaml) | 1 | **Uma**, Ada, Ben | 2 : 1 — minority *tops the poll* | 1 vote each |

## What the dial does

- **Block voting (3 votes = seats).** Each Home voter votes the full Home slate, so Ada/Ben/Cal each get all 6 majority votes and beat every Away candidate (4). The 60% majority takes **all three seats**; the 40% minority is shut out. Majoritarian.
- **Limited voting (2 votes < seats).** A party can no longer fill every seat with its own votes, so over-nominating splits the vote; disciplined parties run about as many as they can win. Home runs 2 (Ada, Ben = 6), Away runs 2 (Uma, Val = 4) → **2 : 1**. Reducing votes-per-voter below the seat count is what opens the door.
- **SNTV (1 vote).** Pure vote-management: the majority *spreads* its 6 votes (2/2/2) while the minority *concentrates* all 4 on Uma — so **Uma finishes first** and the majority's split leaves its candidates on 2 each. **2 : 1**, and the minority candidate is the overall leader. Roughly proportional — the reason SNTV was used for multi-member districts (Japan, Taiwan) before STV.

The whole family is one tally — *most marks fill the N seats* — so the same engine handles all three; it reads votes-per-voter and labels the output **Block Voting**, **Limited Voting**, or **SNTV** accordingly.

## Can these run on BetterVoting? Yes — as bloc Approval.

BV has no method *named* "Block Voting" or "Limited Voting" (its **Plurality** is choose-one), but that's a naming point, not a capability gap. All three are "mark k candidates, top N win" — which is exactly what BV's **multi-winner Approval** (`Approval` + `num_winners`) does. So each is reproducible on BV with the same 0/1 ballots and the same winners:

- **Block voting** = bloc Approval where each voter approves their **full N-candidate slate**.
- **Limited voting** = bloc Approval where each voter approves **k < N**.
- **SNTV** = bloc Approval (or Plurality) where each voter approves **exactly 1** — already BV-confirmed as the [BV2134 governance Bloc Plurality race](../pets_governance/cases/pets_gov_bloc_plurality.yaml).

This set's *point* is the Plurality-family framing (votes-per-voter), and our engine labels the tally Block / Limited / SNTV accordingly — but the arithmetic is **BV-confirmed end-to-end**. Block and Limited are backed by BV election **BV2135** ([`3x4vrv`](https://bettervoting.com/3x4vrv/results)), which runs both as bloc Approval and elects exactly the same seats (Block → Ada, Ben, Cal; Limited → Ada, Ben, Uma). SNTV is BV-backed separately as the [governance Bloc Plurality race](../pets_governance/cases/pets_gov_bloc_plurality.yaml). Full recipe: [running_on_bettervoting.md](running_on_bettervoting.md).

**▶ Block & Limited live on BetterVoting:** [results ↗](https://bettervoting.com/3x4vrv/results) (election `3x4vrv`, Test ID BV2135) · frozen export [`mmp_bv2135_3x4vrv_bv_export.json`](cases/mmp_bv2135_3x4vrv_bv_export.json).

## References

- **SNTV** — Wikipedia: [Single non-transferable vote](https://en.wikipedia.org/wiki/Single_non-transferable_vote) · electowiki: [Single non-transferable vote](https://electowiki.org/wiki/Single_non-transferable_vote)
- **Limited voting** — Wikipedia: [Limited voting](https://en.wikipedia.org/wiki/Limited_voting) · electowiki: [Limited voting (Wikipedia)](https://en.wikipedia.org/wiki/Limited_voting)
- **Block voting** — Wikipedia: [Plurality block voting](https://en.wikipedia.org/wiki/Plurality_block_voting) · electowiki: [Bloc voting](https://electowiki.org/wiki/Bloc_voting)

## See also

- Folder overview: [multi_member_plurality — README](README.md)
- The BV-backed SNTV instance: [Pets Governance — Bloc Plurality](../pets_governance/cases/pets_gov_bloc_plurality.yaml) · the whole [governance set](../pets_governance/)
- Proportional alternatives: [STV](../../06_Other/STV/) · [STAR-PR](../../03_STAR_PR/)
