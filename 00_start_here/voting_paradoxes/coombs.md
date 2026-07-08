# Coombs' procedure — eliminate the most-hated, inherit IRV's diseases (§A7 worked)

*The **Coombs procedure**: if no candidate is ranked first by an absolute majority, delete the candidate ranked **last** by the most voters; repeat until someone holds a majority.* IRV's mirror image — it eliminates by *last*-place counts instead of first-place counts — and it inherits the whole elimination-order disease family: Felsenthal lists Coombs as vulnerable to the Condorcet Winner, Monotonicity, Reinforcement, No-Show, Twin, Truncation, and SCC paradoxes. Coombs has **no tabulator on BetterVoting or in the LH engine** (pref_voting can cross-check), so this page works Felsenthal's §A7 examples; two of them are backed by live elections carrying the same electorates under supported methods.

**Source:** Dan S. Felsenthal, *"Review of Paradoxes Afflicting Various Voting Procedures Where One Out of m Candidates (m ≥ 2) Must Be Elected"*, University of Haifa / LSE, revised 26 May 2010; Appendix §A7, Examples 17–22.

## Example 17 — the Condorcet winner is deleted *first* (live: [BV2164](../../method_comparisons/felsenthal_paradoxes/bv2164_xbqq8t_coombs_cw.md))

33 voters, four candidates; Arlo is the Condorcet winner *and* the most-frequent last choice (12 ballots). Coombs deletes Arlo first and elects Bree. Felsenthal conjectures **four candidates are the minimum** for a Coombs Condorcet failure (most Condorcet-inconsistent procedures manage it with three). Live: STAR and Ranked Robin elect Arlo; Choose-One agrees with Coombs on Bree.

## Example 18 — non-monotonicity (paper only; same electorate as Ex.17)

*Ceteris paribus*, the four `Cole>Arlo>Dana>Bree` voters **raise Bree** to `Cole>Arlo>Bree>Dana`. Arlo is still the Condorcet winner — but the last-place counts shift (Dana now 11+4=15), so **Dana** is deleted first instead of Arlo, then Cole, and **Arlo wins**. Bree, who won Example 17 under Coombs, *loses by being raised*: [non-monotonicity](non_monotonicity.md). The live races are unchanged by the raise (STAR/RR still Arlo, Plurality still Bree), so no separate election exists — this one belongs to Coombs alone.

## Example 19 — No-Show and Truncation (live pair: [BV2165](../../method_comparisons/felsenthal_paradoxes/bv2165_9vxcj7_coombs_noshow.md) → [BV2166](../../method_comparisons/felsenthal_paradoxes/bv2166_b7b8dv_coombs_noshow.md))

15 voters: 4×(Amy>Boone>Cass), 4×(Boone>Cass>Amy), 5×(Cass>Amy>Boone), 2×(Cass>Boone>Amy). Coombs deletes Amy (6 last-place votes) and elects **Boone**. If the two `Cass>Boone>Amy` voters stay home, Coombs deletes *Boone* (5 last-places of 13) and elects **Cass — the abstainers' top preference**: the [No-Show paradox](no_show.md). The same flip arises if they merely truncate to Cass-only: the [Truncation paradox](truncation.md). **Live bonus, shown honestly: STAR flips the same way** (Boone 8–7 with 15 voters; Cass 9–4 with 13) — a genuine score-family participation failure via STAR's runoff stage, the first such case in the live library.

## Example 20 — Reinforcement (paper only; source typo flagged)

District I (34 voters: 9 abc, 9 bca, 11 cab, 5 cba): Coombs deletes a (14 last-places) and elects **b** (18 of 34). District II (printed as "6 voters" but listing 1 abc + 6 bac = **7** — the amalgamated table sums to 41, so we take the tables as authoritative and flag the typo): **b** wins outright. Amalgamated (41 voters): the last-place counts make **c** the deletion (16), and **a** — not b — is elected. Both districts chose b; their union chooses a: the [Reinforcement paradox](multiple_districts.md) under Coombs.

## Example 21 — Twin (paper only; the post state is a random tie)

20 voters, four candidates (5 abdc, 5 bcda, 1 badc, 6 cadb, 1 cbad, 2 cbda): Coombs deletes a (7 last-places) and elects **b** (11 of 20 after transfers). Two more `b>a>d>c` **twins** join: now **c** is deleted first — and the count ends in an a/b **tie**. The twins' arrival *decreased* their candidate's chances from certain win to coin flip: the weak [Twin paradox](no_show.md). Because the post state is a random tie, it cannot be frozen as a BV case (the BV2142 caveat) — paper only.

## Example 22 — SCC (paper only)

29 voters (11 abcd, 12 bcda, 2 badc, 4 cadb): Coombs deletes a (last on 12 ballots, the most) and elects **b**. Now let **c drop out** before the election: a is then ranked first by 15 of 29 — an absolute majority — and **wins immediately**. A loser's exit flipped the winner: [SCC](spoiler_scc.md) under Coombs.

## The pattern

Every failure on this page is the same machinery seen throughout this folder: **elimination order**. Coombs merely reads the ballots from the bottom instead of the top, so where IRV punishes candidates for having too few *friends*, Coombs punishes them for having too many *enemies* — and a broad consensus candidate (everyone's second choice, some faction's last) is exactly who accumulates both. The live comparisons ([BV2164](../../method_comparisons/felsenthal_paradoxes/bv2164_xbqq8t_coombs_cw.md), [BV2165/66](../../method_comparisons/felsenthal_paradoxes/bv2166_b7b8dv_coombs_noshow.md)) show pairwise and score counting on the same ballots — mostly stable, and where STAR's own runoff stage wobbles (BV2166), the repo says so out loud.
