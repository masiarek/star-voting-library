# BV2151 — Felsenthal Example 4 (2 of 2): two supporters stay home, and their side does better

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/97hbpw) · **[results ↗](https://bettervoting.com/97hbpw/results)** (election `97hbpw`).

The same election as [BV2150](bv2150_dxg8pb_felsenthal_ex4_noshow.md) with one change, *ceteris paribus*: **two of the four `Andy>Beth>Carl` voters don't participate**. Result: the runoff procedure now elects **Beth** — the abstainers' second choice — instead of Carl, their last. Not voting served them better than voting. That is the **No-Show paradox**, live on BetterVoting.

## Source

Dan S. Felsenthal, *"Review of Paradoxes Afflicting Various Voting Procedures Where One Out of m Candidates (m ≥ 2) Must Be Elected"*, University of Haifa / LSE, revised 26 May 2010; Appendix §A2, **Example 4** (continued).

## The one changed datum

```
No. of voters    BV2150 (all vote)       BV2151 (two stay home)
      4 → 2      Andy > Beth > Carl      Andy > Beth > Carl   (two abstain)
      3          Beth > Carl > Andy      Beth > Carl > Andy
      1          Carl > Andy > Beth      Carl > Andy > Beth
      3          Carl > Beth > Andy      Carl > Beth > Andy
```

First choices go from Andy 4, Beth 3, Carl 4 to **Andy 2, Beth 3, Carl 4**. The runoff procedure (= IRV for three candidates) now deletes **Andy** instead of Beth — and Beth beats Carl **5–4**. In BV2150 the same four voters' full turnout deleted Beth and elected Carl 7–4.

## Two paradoxes, one pair

**No-Show** (BV2150 → BV2151): removing two sincere `Andy>Beth>Carl` ballots *improves* the outcome for exactly those voters — from their last choice to their second. Their ballots' first-choice weight propped Andy up just enough to get Beth (their real fallback, and the Condorcet winner) eliminated.

**Twin, weak form** (BV2151 → BV2150): read the other direction. Start here, with two `Andy>Beth>Carl` voters. Two *twins* — voters with the identical ordering — join the electorate. One would expect reinforcement of their shared preference; instead the twins' arrival elects **Carl**, the group's common worst choice.

Both are elimination-order diseases, and both vanish on the same ballots under pairwise or score counting: Ranked Robin and STAR elect **Beth** in *both* electorates (Beth is the Condorcet winner both times — 6–5/7–4 with 11 voters, 6–3/5–4 with 9). Teaching page: [no_show.md](../../00_start_here/voting_paradoxes/no_show.md). (Condorcet methods are not participation-proof in general — Moulin's theorem — but this electorate doesn't trigger it.)

## View 1 — BetterVoting

Live results: **[bettervoting.com/97hbpw/results ↗](https://bettervoting.com/97hbpw/results)**. BV elects **Beth** in all three races — matching LH, no tiebreaks.

## View 2 — LH engine

Runoff/IRV race ([bv2151_97hbpw_irv.yaml](cases/bv2151_97hbpw_irv.yaml)):

```
 Tabulating 9 ballots (ranked ballots).

ROUND 1
Candidate      Votes  Status
-----------  -------  --------
Carl               4  Hopeful
Beth               3  Hopeful
Andy               2  Rejected

FINAL RESULT
Candidate      Votes  Status
-----------  -------  --------
Beth               5  Elected
Carl               4  Rejected
Andy               0  Rejected

Winner(s) — RCV / Instant-Runoff Voting (single winner)
  Beth
```

Ranked Robin ([bv2151_97hbpw_ranked_robin.yaml](cases/bv2151_97hbpw_ranked_robin.yaml)) → **Beth** (6–3, 5–4). STAR ([bv2151_97hbpw_star.yaml](cases/bv2151_97hbpw_star.yaml)): **Andy 19, Beth 31, Carl 31** — Beth and Carl advance over Andy, Beth wins the runoff **5–4**. Full detail: [IRV mirror](cases/cases_tabulated/bv2151_97hbpw_irv_tabulated.txt) · [RR mirror](cases/cases_tabulated/bv2151_97hbpw_ranked_robin_tabulated.txt) · [STAR mirror](cases/cases_tabulated/bv2151_97hbpw_star_tabulated.txt).

## Agreement

| Election | Race | BetterVoting | LH engine | Agree? |
|---|---|---|---|---|
| BV2150 all vote | Runoff (IRV) | **Carl** | **Carl** | ✓ |
| BV2151 two no-shows | Runoff (IRV) | **Beth** | **Beth** | ✓ |
| BV2150 / BV2151 | Ranked Robin | Beth / Beth | Beth / Beth | ✓ |
| BV2150 / BV2151 | STAR | Beth / Beth | Beth / Beth | ✓ |

Frozen export: [bv2151_97hbpw_bv_export.json](cases/bv2151_97hbpw_bv_export.json) · Part 1: [BV2150 — everyone votes](bv2150_dxg8pb_felsenthal_ex4_noshow.md).
