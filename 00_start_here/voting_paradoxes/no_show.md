# The No-Show paradox — when staying home beats voting (and its Twin)

*The **No-Show paradox** (participation failure): a group of voters gets a **better** outcome by not voting than by casting their sincere ballots. The **Twin paradox** (weak form) is the same failure read forward: voters are made worse off by the arrival of "twins" — additional voters whose preference ordering is identical to theirs.* (Both are **conditional** paradoxes in Felsenthal's taxonomy: the one changed datum is who participates.)

→ Glossary: [`no-show paradox`](../GLOSSARY.md) · Felsenthal's taxonomy: [README](README.md)

## The live demonstration (a pair of elections)

Felsenthal's Example 4, run for real: [BV2150](../../method_comparisons/felsenthal_paradoxes/bv2150_dxg8pb_felsenthal_ex4_noshow.md) (11 voters, all participate) — plurality-with-runoff (= IRV for three candidates) deletes Beth and elects **Carl**, the *last* choice of the four `Andy>Beth>Carl` voters. [BV2151](../../method_comparisons/felsenthal_paradoxes/bv2151_97hbpw_felsenthal_ex4_noshow.md) (two of those four stay home) — the deletion flips to Andy and **Beth** wins 5–4. The abstainers got their second choice by not voting; their full turnout had bought their last.

The Twin paradox is the same pair traversed the other way: start at BV2151, where two `Andy>Beth>Carl` voters are joined by two *twins* with the identical ordering — and the reinforced group's worst choice wins. "More voters like us" made things worse.

The paradox also lurks in [BV2159 (Brams' sampler)](../../method_comparisons/paradoxes_and_whoops/bv2159_f4cjpy_brams_irv_pathologies.md), packed alongside truncation and non-monotonicity in one 21-voter election.

## Where it comes from

The same elimination-order machinery as [non-monotonicity](non_monotonicity.md): under RCV-IRV and plurality-with-runoff, a ballot's first-choice weight can prop up its *own* favorite just enough to get its *fallback* eliminated — after which the ballot's lower preferences are worthless. In BV2150 the four Andy-first ballots kept Andy alive, which is precisely what killed Beth. Removing two of them let Andy die early and Beth (the Condorcet winner in both electorates) survive to win.

Score-summing methods (Score, Approval) cannot produce a no-show paradox — an added sincere ballot only adds support in the direction the voter intends. STAR's runoff stage costs it the formal guarantee, and Condorcet methods provably fail participation in some electorates (Moulin's theorem). On *this* pair both STAR and Ranked Robin elect Beth with 11 voters and with 9 — but the repo now carries a live case where STAR itself flips: [BV2165→BV2166 (Coombs' Example 19 electorate)](../../method_comparisons/felsenthal_paradoxes/bv2166_b7b8dv_coombs_noshow.md), where two abstainers get their favorite under STAR's runoff as well as under Coombs. Shown out loud, per the honest-limits framing in [reading_these_fairly.md](../../method_comparisons/paradoxes_and_whoops/reading_these_fairly.md).

## Why it matters

"Vote — it can only help your side" is the civic promise every method should keep. A procedure where organizers can rationally tell two supporters *please stay home* corrodes the point of turnout itself, and unlike most paradoxes this one has a perverse *action item* baked in. Eleven voters and two BetterVoting elections show the whole mechanism end to end.
