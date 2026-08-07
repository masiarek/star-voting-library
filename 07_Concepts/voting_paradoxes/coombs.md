# Coombs' procedure — eliminate the most-hated, inherit IRV's diseases (§A7 worked)

*The **Coombs procedure**: if no candidate is ranked first by an absolute majority, delete the candidate ranked **last** by the most voters; repeat until someone holds a majority.* IRV's mirror image — it eliminates by *last*-place counts instead of first-place counts — and it inherits the whole elimination-order disease family: Felsenthal lists Coombs as vulnerable to the Condorcet Winner, Monotonicity, Reinforcement, No-Show, Twin, Truncation, and SCC paradoxes. Coombs has **no tabulator on BetterVoting or in the LH engine**, so this repo counts it with [`coombs_report.py`](../../STARVote_LH_tabulation_engine/tools_adam/pref_voting_tabulation_engine/coombs_report.py), which prints the deletion round by round and is cross-checked against `pref_voting` on every run. Two examples are backed by live elections carrying the same electorates under supported methods; **every example below is a runnable case file** — the ballots are real YAML, not prose.

```bash
uv run STARVote_LH_tabulation_engine/tools_adam/pref_voting_tabulation_engine/coombs_report.py method_comparisons/felsenthal_paradoxes/cases/coombs_ex18_monotonicity.yaml
```

**Source:** Dan S. Felsenthal, *"Review of Paradoxes Afflicting Various Voting Procedures Where One Out of m Candidates (m ≥ 2) Must Be Elected"*, University of Haifa / LSE, revised 26 May 2010; Appendix §A7, Examples 17–22.

## Example 17 — the Condorcet winner is deleted *first* (live: [BV2164](../../method_comparisons/felsenthal_paradoxes/bv2164_xbqq8t_coombs_cw.md))

33 voters, four candidates; Arlo is the Condorcet winner *and* the most-frequent last choice (12 ballots). Coombs deletes Arlo first and elects Bree. Felsenthal conjectures **four candidates are the minimum** for a Coombs Condorcet failure (most Condorcet-inconsistent procedures manage it with three) — but this **conjecture is false**: Brandt, Matthäus & Saile (2022, [Minimal voting paradoxes](https://pub.dss.in.tum.de/brandt-research/minpara.pdf), Table 3) exhibit a Coombs Condorcet-winner failure with **just three candidates and 13 voters** (and a four-candidate one needs only 9 voters, not 33). So this example is memorable but far from minimal — see the [minimal-instances cross-check](README.md#minimal-instances-and-how-our-examples-compare). Live: STAR and Ranked Robin elect Arlo; Choose-One agrees with Coombs on Bree.

## Example 18 — non-monotonicity (paper only; same electorate as Ex.17)

**Case:** [the same 33 voters, Bree raised on four ballots](../../method_comparisons/felsenthal_paradoxes/cases/cases_pages/coombs_ex18_monotonicity.md)

*Ceteris paribus*, the four `Cole>Arlo>Dana>Bree` voters **raise Bree** to `Cole>Arlo>Bree>Dana`. Arlo is still the Condorcet winner — but the last-place counts shift (Dana now 11+4=15), so **Dana** is deleted first instead of Arlo, then Cole, and **Arlo wins**. Bree, who won Example 17 under Coombs, *loses by being raised*: [non-monotonicity](non_monotonicity.md). The live races are unchanged by the raise (STAR/RR still Arlo, Plurality still Bree), so no separate election exists — this one belongs to Coombs alone.

## Example 19 — No-Show and Truncation (live pair: [BV2165](../../method_comparisons/felsenthal_paradoxes/bv2165_9vxcj7_coombs_noshow.md) → [BV2166](../../method_comparisons/felsenthal_paradoxes/bv2166_b7b8dv_coombs_noshow.md))

15 voters: 4×(Amy>Boone>Cass), 4×(Boone>Cass>Amy), 5×(Cass>Amy>Boone), 2×(Cass>Boone>Amy). Coombs deletes Amy (6 last-place votes) and elects **Boone**. If the two `Cass>Boone>Amy` voters stay home, Coombs deletes *Boone* (5 last-places of 13) and elects **Cass — the abstainers' top preference**: the [No-Show paradox](no_show.md). The same flip arises if they merely truncate to Cass-only: the [Truncation paradox](truncation.md). **Live bonus, shown honestly: STAR flips the same way** (Boone 8–7 with 15 voters; Cass 9–4 with 13) — a genuine score-family participation failure via STAR's runoff stage, the first such case in the live library.

## Example 20 — Reinforcement (paper only; source typo flagged)

**Cases:** [District I](../../method_comparisons/felsenthal_paradoxes/cases/cases_pages/coombs_ex20_district1.md) · [District II](../../method_comparisons/felsenthal_paradoxes/cases/cases_pages/coombs_ex20_district2.md) · [amalgamated](../../method_comparisons/felsenthal_paradoxes/cases/cases_pages/coombs_ex20_amalgamated.md)

District I (34 voters: 9 A>B>C, 9 B>C>A, 11 C>A>B, 5 C>B>A): Coombs deletes A (14 last-places, against B's 11 and C's 9) and elects **B** (18 of 34). District II (printed as "6 voters" but listing 1 A>B>C + 6 B>A>C = **7** — the amalgamated table sums to 41, so we take the tables as authoritative and flag the typo): **B** wins outright on a first-round majority. Amalgamated (41 voters): the last-place counts make **C** the deletion (16, against A's 14 and B's 11), and **A** — not B — is elected. Both districts chose B; their union chooses A: the [Reinforcement paradox](multiple_districts.md) under Coombs.

The three case files are counted as RCV-IRV, which elects **B in all three** — so on this profile IRV shows no reinforcement failure at all, and the paradox is Coombs' alone. That contrast is why the districts are separate files rather than one.

## Example 21 — Twin (paper only; the post state is a random tie)

**Cases:** [before — 20 voters](../../method_comparisons/felsenthal_paradoxes/cases/cases_pages/coombs_ex21_twin_before.md) → [after — two twins join](../../method_comparisons/felsenthal_paradoxes/cases/cases_pages/coombs_ex21_twin_after.md)

20 voters, four candidates (5 A>B>D>C, 5 B>C>D>A, 1 B>A>D>C, 6 C>A>D>B, 1 C>B>A>D, 2 C>B>D>A): Coombs deletes A (7 last-places) and elects **B** (11 of 20 after transfers). Two more `B>A>D>C` **twins** join: now **C** is deleted first, then D — and the third round leaves A and B tied at 11 last places each, so the final deletion, and with it the winner, falls to a lot. The twins' arrival *decreased* their own candidate's chances from certain win to coin flip: the weak [Twin paradox](no_show.md). Because the post state is a random tie it cannot be frozen as a BV case (the BV2142 caveat), but it is a runnable file here — the `_tabulated` mirror records the determinate RCV-IRV count, and `coombs_report.py` prints the tie and refuses to pretend otherwise.

## Example 22 — SCC (paper only)

**Case:** [29 voters, then C drops out](../../method_comparisons/felsenthal_paradoxes/cases/cases_pages/coombs_ex22_scc.md)

29 voters (11 A>B>C>D, 12 B>C>D>A, 2 B>A>D>C, 4 C>A>D>B): nobody holds a majority (B leads on 14 of 29), so Coombs deletes A (last on 12 ballots, the most) and elects **B**. Now let **C drop out** before the election — C had four first places and was eliminated in every count: A is then ranked first by 15 of 29, an absolute majority, and **wins immediately**, never reaching a deletion. A loser's exit flipped the winner: [SCC](spoiler_scc.md) under Coombs. Recount it with `--drop C`:

```bash
uv run STARVote_LH_tabulation_engine/tools_adam/pref_voting_tabulation_engine/coombs_report.py --drop C method_comparisons/felsenthal_paradoxes/cases/coombs_ex22_scc.yaml
```

RCV-IRV elects **A both with and without C** — no spoiler — and A is precisely the candidate Coombs only reaches once C leaves.

## The pattern

Every failure on this page is the same machinery seen throughout this folder: **elimination order**. Coombs merely reads the ballots from the bottom instead of the top, so where IRV punishes candidates for having too few *friends*, Coombs punishes them for having too many *enemies* — and a broad consensus candidate (everyone's second choice, some faction's last) is exactly who accumulates both. The live comparisons ([BV2164](../../method_comparisons/felsenthal_paradoxes/bv2164_xbqq8t_coombs_cw.md), [BV2165/66](../../method_comparisons/felsenthal_paradoxes/bv2166_b7b8dv_coombs_noshow.md)) show pairwise and score counting on the same ballots — mostly stable, and where STAR's own runoff stage wobbles (BV2166), the repo says so out loud.
