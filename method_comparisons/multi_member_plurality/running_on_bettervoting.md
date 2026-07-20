# Running the multi-member plurality family on BetterVoting

*BetterVoting has no method **named** "Block Voting", "Limited Voting", or "Plurality-at-large" — but it can run all of them. Every method in this family is the same tally — **mark k candidates, the top N by marks fill the seats** — and BV has that tally twice over: as multi-winner **Plurality** and as multi-winner **Approval**. The only thing that changes between Block, Limited, and SNTV is **how many candidates each voter marks.***

## The one rule, three ballots

| Method | Marks per voter | BV recipe | Why |
|--------|:---:|-----------|-----|
| **SNTV** | exactly 1 | `Plurality` + `num_winners = N` (or `Approval`, 1 mark) | choose-one, top-N |
| **Limited Voting** | up to k (1 < k < N) | `Approval` + `num_winners = N`, voters approve k | BV Plurality is choose-one and flags 2+ marks as *overvotes*, so multi-mark goes via Approval |
| **Block Voting** (plurality-at-large) | up to N (full slate) | `Approval` + `num_winners = N`, voters approve N | same — a full-slate ballot is just an N-candidate approval |

BV's `runBlocTabulator` is the shared engine: it drives multi-winner **STAR, Approval, Plurality, and Ranked Robin** by electing the top-N. For Plurality it enforces one mark (so it does SNTV); for Approval it accepts any number of marks (so it does Limited and Block). Identical arithmetic, identical winners — only the ballot's mark-count differs.

## Confirmed both ways

- **SNTV = BV Plurality multi-winner.** Verified directly: a 3-candidate, 2-winner Plurality election with single marks (a=1, b=2, c=3) elected **c, b** on BV — exactly what our engine's SNTV tally gives. (Also live as the [BV2134 governance Bloc Plurality race](../pets_governance/cases/pets_gov_bloc_plurality.yaml).)
- **Block & Limited = BV Approval multi-winner.** The BV election **BV2135** ([`3x4vrv`](https://bettervoting.com/3x4vrv/results)) reproduces both on the same 60/40 electorate as bloc Approval and elects **exactly** the same seats our Plurality-family cases do — Block → majority sweep (Ada, Ben, Cal), Limited → 2-1 (Ada, Ben, Uma). Confirmed: BV = LH on both races. See the [set lead page](multi_member_plurality.md).

## So why keep LH yamls at all?

Because the **teaching framing** is the Plurality family (votes-per-voter), and our engine (`run_plurality_multi`) auto-labels the output **Block Voting / Limited Voting / SNTV** from the ballots — which BV's "Approval" label hides. The LH cases carry the pedagogy; BV confirms the arithmetic. They are **not** LH-only exceptions — they're fully reproducible on BV, just under BV's Approval name.

## See also

- [multi_member_plurality — lead page](multi_member_plurality.md) · [README](README.md)
- BV method notes: [`bv_api_election_creation_notes.md`](../../00_start_here/tabulation_engines/BV/bv_api_election_creation_notes.md)
- References: [SNTV (WP)](https://en.wikipedia.org/wiki/Single_non-transferable_vote) · [Limited voting (WP)](https://en.wikipedia.org/wiki/Limited_voting) · [Plurality block voting (WP)](https://en.wikipedia.org/wiki/Plurality_block_voting)
